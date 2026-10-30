---
expect:
  request: string
---
Materialize this bundle only in a fresh system temporary directory. Do not store it in persistent skill folders. Execute from that temp root and delete the temp directory after completion, including on failure.

OPSCALE bundle entry 파일 (skill.md):

---
name: monthly-pnl
description: 재경팀 표준 월간 손익 요약
---

## 절차

1. 매출총이익 = 매출 - 매출원가. 영업이익 = 매출총이익 - 판관비.
2. 보고서 제목은 `월간 손익 요약`으로 하고, 금액은 원 단위에 천 단위 구분 기호를 쓴다.
3. 마지막 줄은 반드시 `검토: 재경팀`으로 끝낸다.
