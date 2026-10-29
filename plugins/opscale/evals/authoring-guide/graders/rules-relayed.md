---
type: llm
focus: last_message
---

PASS if the reply states that the Skill needs exactly one entry file SKILL.md with required name and description frontmatter, that binary files are limited to xlsx, xls, pdf, and docx, and that the folder layout and other file names are up to the author.
FAIL if the reply says particular folders such as references/, scripts/, or assets/ are required, omits the binary-type restriction, or answers only with generic advice not tied to OPSCALE rules.
