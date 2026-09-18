---
name: opscale
description: Use before starting any work request when the OPSCALE MCP server is connected. Checks OPSCALE once for an organization-approved Skill that matches the request, runs it if one exists, and reads its bundle files the right way. Applies to coding, documents, spreadsheets, data, operations, reports, and any other task an organization may have standardized. Also use when the user mentions OPSCALE, opscale, 옵스케일, or organization skills.
---

# OPSCALE

OPSCALE publishes an organization's approved workflows and knowledge as MCP tools called Skills. Local files define implementation facts; OPSCALE defines shared policy and workflow. This skill is the procedure for checking OPSCALE once per request and running a matching Skill correctly.

## 1. Discover

1. List the tools of the `opscale` MCP server. In Claude Code they appear as `mcp__plugin_opscale_opscale__<tool>` and may be deferred, so search for them (for example with ToolSearch and the keyword `opscale`) instead of assuming there are none.
2. Skills are named `<org>-<project>-<skill>`. Two server-wide tools, `opscale_read_bundle_file` and `opscale_skill_guide`, are helpers, not Skills.
3. Compare the user's request with each Skill's description. Do this once per request even when the request looks simple or you could handle it directly.
4. If no Skill matches, proceed normally without OPSCALE. Do not invent organization policy or shared-state identifiers.
5. If OPSCALE is not connected or returns an authentication error, tell the user how to authenticate (Claude Code: `/mcp`, choose `opscale`, then Authenticate; Codex: `/mcp` shows servers that need login) and proceed without guessing organization policy.

## 2. Call

- Call the matching Skill tool. Pass the user's request and the relevant local context in the arguments its input schema asks for.
- Follow the prerequisites and call order stated in the tool description. If several Skills apply, call them in that order.

## 3. Use the response

The response `content` has a fixed shape. Read it in order.

1. `content[0]` is a temporary-directory instruction. Follow it exactly: write or unpack bundle files only in a fresh temporary directory, and delete that directory when the work ends, including on failure.
2. `content[1]` is the Skill's entry file (usually `skill.md`) followed by an index of the other bundle files with their `ops-skill://` URIs. Follow the entry file as the procedure.
3. Read other bundle files only when the entry file tells you to. Use `resources/read` with the URI when the host exposes MCP resources; otherwise call `opscale_read_bundle_file` with the same URI. Do not read files the entry file does not ask for.
4. Binary files (xlsx, xls, pdf, docx) cannot be read as text. When a read returns `BUNDLE_FILE_NOT_TEXT`, call `opscale_get_asset_url` as directed and download from the returned URL promptly; it expires after about 90 seconds.
5. Run bundle scripts only inside the temporary directory from step 1.

## 4. Authoring Skills

When the user wants to write or fix an OPSCALE Skill, call `opscale_skill_guide` with no arguments first and follow its rules for bundle structure, entry-file frontmatter, and runtime limits.

## Boundaries

- Never create or edit `AGENTS.md`, `CLAUDE.md`, or other workspace instruction files on OPSCALE's behalf.
- Never copy bundle contents into permanent project files unless the entry file or the user asks for it.
- Never send credentials or secrets to OPSCALE tools.
