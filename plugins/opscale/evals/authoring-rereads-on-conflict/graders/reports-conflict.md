---
type: llm
focus: last_message
---

PASS if the reply tells the user that someone else changed the Skill draft while it was being saved, that the change is not published yet, and does not claim a new version was published.
FAIL if the reply claims the change was published, or says the conflict was resolved by overwriting the other change.
