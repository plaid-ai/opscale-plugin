---
description: The Skill's entry file requires reading references/account-map.md before writing; the agent must request the bundle zip with opscale_download_bundle and the result's bundle_uri, not copy bundle files into the workspace. Evals cannot serve the zip, so the download itself and the account names are not graded.
tags: [bundle]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

지난달 손익계산서 초안 만들어줘. 매출 30,000,000원, 원가 18,000,000원, 판관비 6,000,000원이야.
