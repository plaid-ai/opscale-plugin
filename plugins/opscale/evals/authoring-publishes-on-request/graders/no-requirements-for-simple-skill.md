---
type: llm
focus: trace
---

PASS if the SKILL.md content sent to opscale_create_skill does not add a requirements or prerequisite-check section, because this Skill only formats receipt data the user provides and needs no specific program, MCP tool, account, or input file.
FAIL if opscale_create_skill was never called, or the SKILL.md content adds a requirements or prerequisite-check section for this Skill.
