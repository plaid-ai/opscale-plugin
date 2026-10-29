---
type: llm
focus: trace
---

PASS if, after the first opscale_update_skill call returns SKILL_DRAFT_REVISION_CONFLICT, the agent calls opscale_get_skill_draft again before any further opscale_update_skill call or before it stops and reports to the user.
FAIL if the agent retries opscale_update_skill after the conflict without reading the draft again, or never reads the draft again after the conflict.
