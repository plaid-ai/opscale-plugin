"""Check that every manifest and the MCP version header carry the same plugin version.

With --base <git ref>, also fail when files under plugins/ changed since that ref
but the version did not, because Claude Code and Codex update only on a new version.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER = "X-Opscale-Plugin-Version"
CLAUDE_MANIFEST = "plugins/opscale/.claude-plugin/plugin.json"


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


def collect_versions() -> dict[str, str | None]:
    server = _load("plugins/opscale/.mcp.json")["mcpServers"]["OPSCALE"]
    marketplace = _load(".claude-plugin/marketplace.json")
    entry = next(plugin for plugin in marketplace["plugins"] if plugin["name"] == "opscale")
    return {
        CLAUDE_MANIFEST: _load(CLAUDE_MANIFEST).get("version"),
        "plugins/opscale/.codex-plugin/plugin.json": _load("plugins/opscale/.codex-plugin/plugin.json").get("version"),
        ".claude-plugin/marketplace.json": entry.get("version"),
        ".mcp.json headers": (server.get("headers") or {}).get(HEADER),
        ".mcp.json http_headers": (server.get("http_headers") or {}).get(HEADER),
    }


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="git ref to compare against, e.g. origin/main")
    args = parser.parse_args()

    versions = collect_versions()
    if len(set(versions.values())) != 1 or None in versions.values():
        for source, version in versions.items():
            print(f"{source}: {version}")
        print("error: plugin versions differ", file=sys.stderr)
        return 1
    version = next(iter(versions.values()))
    print(f"plugin version {version}")

    if args.base:
        changed = [line for line in _git("diff", "--name-only", f"{args.base}...HEAD", "--", "plugins/").splitlines() if line]
        if changed:
            base_version = json.loads(_git("show", f"{args.base}:{CLAUDE_MANIFEST}")).get("version")
            if base_version == version:
                print("\n".join(changed))
                print(f"error: plugins/ changed but the version is still {version}", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
