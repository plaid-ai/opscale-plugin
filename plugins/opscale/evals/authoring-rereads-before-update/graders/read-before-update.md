---
type: llm
focus: trace
---

PASS if every opscale_update_skill call is preceded by an opscale_get_skill_draft call made after the previous opscale_update_skill call (or after the start, for the first one), and the update changes the existing `skill.md` instead of adding a second entry file.
FAIL if any opscale_update_skill call is made without a fresh opscale_get_skill_draft call before it, or the update adds a new entry file such as `SKILL.md` next to `skill.md`.
