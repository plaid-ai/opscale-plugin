---
type: llm
focus: last_message
---

PASS if the reply tells the user that they have no write access to any OPSCALE project for this Skill, that a project admin or organization admin can make the change, and that nothing was changed.
FAIL if the reply claims the change was made or published, offers to create a copy of the Skill elsewhere, or blames a technical error instead of permissions.
