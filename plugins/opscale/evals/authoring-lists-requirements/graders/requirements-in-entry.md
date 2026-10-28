---
type: llm
focus: trace
---

PASS if the SKILL.md content sent to opscale_create_skill lists the Jira MCP tool as a requirement near the top of the file, tells the agent to check that it is available before starting the work, and tells the agent to stop and tell the user what is missing when it is not available.
FAIL if opscale_create_skill was never called, the SKILL.md content has no such requirement and check, or it tells the agent to work around a missing Jira tool in a way the file does not define.
