# OPSCALE Plugin

Use your organization's [OPSCALE](https://github.com/plaid-ai/opscale-plugin) Skills from Claude Code and Codex.

OPSCALE is a multi-tenant platform where organizations author, publish, and govern agent Skills. This plugin does two things:

- connects the agent to the OPSCALE MCP server (`https://mcp-opscale.plaidlabs.ai/`), with sign-in handled by the agent's own OAuth flow
- adds an `opscale` skill that tells the agent to check OPSCALE once per request, run a matching Skill, and read its bundle files correctly

The plugin contains no organization content. What you can see and run is decided by OPSCALE at sign-in and on every call.

## Install

### Claude Code

```
/plugin marketplace add plaid-ai/opscale-plugin
/plugin install opscale@plaidlabs
```

Then run `/mcp`, choose `opscale`, and sign in.

### Codex

```
codex plugin marketplace add plaid-ai/opscale-plugin
codex plugin add opscale@plaidlabs
```

Start a new session, then run `/mcp` to sign in to `opscale`.

## Repository layout

```
.claude-plugin/marketplace.json   Claude Code marketplace catalog
.agents/plugins/marketplace.json  Codex marketplace catalog
plugins/opscale/                  the plugin
  .claude-plugin/plugin.json      Claude Code manifest
  .codex-plugin/plugin.json       Codex manifest
  .mcp.json                       OPSCALE MCP server
  skills/opscale/SKILL.md         procedure skill
  evals/                          claude plugin eval cases
```

One repository serves as both the marketplace and the plugin for both clients.

## Development

```
claude plugin validate ./plugins/opscale --strict
claude plugin validate . --strict
claude plugin eval ./plugins/opscale
```

Evals run against mocked OPSCALE tools under `plugins/opscale/evals/mocks/`, so they need no OPSCALE account.

## Scope

Version 0.1 is deliberately minimal: MCP server plus skill, no hooks. Hooks that force a discovery step, and submission to public plugin catalogs, are planned once the skill-only baseline has been measured.

## License

MIT

---

## 한국어

Claude Code와 Codex에서 조직의 OPSCALE Skill을 바로 쓰기 위한 플러그인입니다. OPSCALE MCP 서버 연결과 절차 스킬 하나만 담고 있으며, 조직 콘텐츠는 들어 있지 않습니다. 접근 권한은 OPSCALE 로그인(OAuth)이 결정합니다.

설치 후 Claude Code는 `/mcp`에서, Codex는 새 세션을 열고 `/mcp`에서 `opscale`에 로그인하면 됩니다.
