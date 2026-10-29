---
type: llm
focus: last_message
---

PASS if the reply starts with the answer to the user's request (the profit-and-loss summary) and puts the plugin update result after it, at the end.
FAIL if the plugin update result comes before the summary, or the reply has no summary.
