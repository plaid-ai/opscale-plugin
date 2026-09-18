---
expect:
  request: string
---
Materialize this bundle only in a fresh system temporary directory. Do not store it in persistent skill folders. Execute from that temp root and delete the temp directory after completion, including on failure.

# skill.md (entry)

---
name: monthly-pnl
description: 재경팀 표준 월간 손익 요약
---

## 절차

1. 보고서를 쓰기 전에 `references/account-map.md`를 읽고, 그 표의 보고서 계정명을 그대로 쓴다. 읽기 전에는 작성하지 않는다.
2. 매출총이익 = 매출 - 매출원가. 영업이익 = 매출총이익 - 판관비.
3. 보고서 제목은 `월간 손익 요약`으로 하고, 금액은 원 단위에 천 단위 구분 기호를 쓴다.
4. 마지막 줄은 반드시 `검토: 재경팀`으로 끝낸다.

# Other bundle files (read only when the entry file asks)

- references/account-map.md → ops-skill://bundle/demo/sv_0001/files/references/account-map.md

If this host does not expose MCP resources, read them with the opscale_read_bundle_file tool using the same URI.
