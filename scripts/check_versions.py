"""Check that every manifest and the opscale skill carry the same plugin version.

The agent reads the installed version from the `Plugin version:` line in the opscale skill body
and compares it with the latest version OPSCALE states, so that line must match the manifests.
The plugin sends no version header: `.mcp.json` must not set `headers`, `headersHelper`, or
`http_headers`. A static `headers` entry would also change the key Claude Code stores the
OPSCALE login under and sign every user out on each update.

With --base <git ref>, also fail when files under plugins/ changed since that ref
but the version did not, because Claude Code and Codex update only on a new version.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = "plugins/opscale/skills/opscale/SKILL.md"
HEADER_KEYS = ("headers", "headersHelper", "http_headers")
CLAUDE_MANIFEST = "plugins/opscale/.claude-plugin/plugin.json"


def _load(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


def _skill_version() -> str | None:
    """Return the version on the skill body's `Plugin version:` line, ignoring frontmatter."""
    text = (ROOT / SKILL).read_text()
    body = text.split("---", 2)[2] if text.startswith("---") else text
    matches = re.findall(r"^Plugin version: (\S+)$", body, flags=re.MULTILINE)
    return matches[0] if len(matches) == 1 else None


def collect_versions() -> dict[str, str | None]:
    marketplace = _load(".claude-plugin/marketplace.json")
    entry = next(plugin for plugin in marketplace["plugins"] if plugin["name"] == "opscale")
    return {
        CLAUDE_MANIFEST: _load(CLAUDE_MANIFEST).get("version"),
        "plugins/opscale/.codex-plugin/plugin.json": _load("plugins/opscale/.codex-plugin/plugin.json").get("version"),
        ".claude-plugin/marketplace.json": entry.get("version"),
        f"{SKILL} `Plugin version:` line": _skill_version(),
    }


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="git ref to compare against, e.g. origin/main")
    args = parser.parse_args()

    server = _load("plugins/opscale/.mcp.json")["mcpServers"]["OPSCALE"]
    present = [key for key in HEADER_KEYS if key in server]
    if present:
        print(f"error: .mcp.json must not set {', '.join(present)} (see module docstring)", file=sys.stderr)
        return 1
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
