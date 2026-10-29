# OPSCALE Plugin

Use your organization's [OPSCALE](https://github.com/plaid-ai/opscale-plugin) Skills from Claude Code and Codex.

OPSCALE is a multi-tenant platform where organizations author, publish, and govern agent Skills. This plugin does two things:

- connects the agent to the OPSCALE MCP server (`https://mcp-opscale.plaidlabs.ai/`), with sign-in handled by the agent's own OAuth flow
- adds an `opscale` skill that tells the agent to check OPSCALE once per request, run a matching Skill, and read its bundle files correctly
- adds an `opscale-skill-authoring` skill with the rules and procedure for creating and updating OPSCALE Skills through the OPSCALE authoring tools, which publish immediately
- sends its version to OPSCALE in the `X-Opscale-Plugin-Version` header, so OPSCALE can tell an out-of-date plugin to update itself (see [Updates](#updates))

The plugin contains no organization content. What you can see and run is decided by OPSCALE at sign-in and on every call.

## Install

### Claude Code

```
/plugin marketplace add plaid-ai/opscale-plugin
/plugin install opscale@plaidlabs
```

Then run `/mcp`, choose `OPSCALE`, and sign in.

### Codex

```
codex plugin marketplace add plaid-ai/opscale-plugin
codex plugin add opscale@plaidlabs
```

Start a new session, then run `/mcp` to sign in to `OPSCALE`.

## Updates

When a newer plugin is released, OPSCALE shows an out-of-date plugin the `opscale_plugin_update` tool. After finishing your request, the agent runs the update commands that tool returns and tells you; the new version applies from the next session. The agent runs only `claude plugin …` or `codex plugin …` commands for this marketplace.

To update by hand:

```
claude plugin marketplace update plaidlabs
claude plugin update opscale@plaidlabs
```

```
codex plugin marketplace upgrade plaidlabs
```

## Repository layout

```
.claude-plugin/marketplace.json   Claude Code marketplace catalog
.agents/plugins/marketplace.json  Codex marketplace catalog
plugins/opscale/                  the plugin
  .claude-plugin/plugin.json      Claude Code manifest
  .codex-plugin/plugin.json       Codex manifest
  .mcp.json                       OPSCALE MCP server
  assets/                         plugin logo and composer icon (Codex UI, Anthropic directory listing)
  skills/opscale/SKILL.md         procedure skill
  skills/opscale/agents/openai.yaml  skill display name and icon for the Codex UI
  skills/opscale/assets/          skill icons referenced by openai.yaml
  skills/opscale-skill-authoring/ authoring skill (same layout as skills/opscale/)
  evals/                          claude plugin eval cases
scripts/check_versions.py         CI check that every manifest and the version header agree
```

One repository serves as both the marketplace and the plugin for both clients.

## Development

```
claude plugin validate ./plugins/opscale --strict
claude plugin validate . --strict
claude plugin eval ./plugins/opscale
python3 scripts/check_versions.py
```

Release rule: any change under `plugins/` bumps the version in `plugins/opscale/.claude-plugin/plugin.json`, `plugins/opscale/.codex-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and both version headers in `plugins/opscale/.mcp.json`. Claude Code and Codex decide whether to update by this version.

Evals run against mocked OPSCALE tools under `plugins/opscale/evals/mocks/`, so they need no OPSCALE account.

## Scope

Version 0.3 is deliberately minimal: MCP server plus skills, no hooks. Hooks that force a discovery step, and submission to public plugin catalogs, are planned once the skill-only baseline has been measured.

## License

MIT

---

## 한국어

Claude Code와 Codex에서 조직의 OPSCALE Skill을 바로 쓰기 위한 플러그인입니다. OPSCALE MCP 서버 연결과 절차 스킬(`opscale`), Skill 저작 스킬(`opscale-skill-authoring`)만 담고 있으며, 조직 콘텐츠는 들어 있지 않습니다. 저작 도구로 저장한 Skill은 바로 조직에 게시됩니다. 접근 권한은 OPSCALE 로그인(OAuth)이 결정합니다.

설치 후 Claude Code는 `/mcp`에서, Codex는 새 세션을 열고 `/mcp`에서 `OPSCALE`에 로그인하면 됩니다.

새 버전이 나오면 OPSCALE이 구버전 플러그인에 `opscale_plugin_update` 도구를 보여 주고, 에이전트가 요청을 마친 뒤 업데이트 명령을 실행하고 알려 줍니다. 새 버전은 다음 세션부터 적용됩니다. 직접 업데이트하려면 Claude Code는 `claude plugin marketplace update plaidlabs` 후 `claude plugin update opscale@plaidlabs`, Codex는 `codex plugin marketplace upgrade plaidlabs`를 실행합니다.
