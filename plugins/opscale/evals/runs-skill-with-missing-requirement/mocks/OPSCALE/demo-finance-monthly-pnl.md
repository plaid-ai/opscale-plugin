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

## 필요 조건

- Google Sheets MCP의 `sheets_append_row` 도구

작업 전에 이 도구가 있는지 확인한다. 없으면 작업하지 말고, 무엇이 없고 어떻게 준비하는지 사용자에게 알린다.

## 절차

1. 매출총이익 = 매출 - 매출원가. 영업이익 = 매출총이익 - 판관비.
2. 보고서 제목은 `월간 손익 요약`으로 하고, 금액은 원 단위에 천 단위 구분 기호를 쓴다.
3. `sheets_append_row`로 재경팀 공유 시트에 결과 행을 추가한다.
4. 마지막 줄은 반드시 `검토: 재경팀`으로 끝낸다.
