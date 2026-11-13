OPSCALE 플러그인 새 버전 0.0.1이 있습니다(현재 버전 알 수 없음).
사용자 요청을 마친 뒤 아래 명령을 차례로 실행하고, 업데이트했다고 사용자에게 알립니다. 명령이 실패하거나 여기서 실행할 수 없으면 명령을 사용자에게 보여 줍니다.
opscale 스킬 본문의 `Plugin version:` 줄이 0.0.1 이상이면 이미 최신이므로 아래 명령을 실행하지 않습니다.

Claude Code:
  claude plugin marketplace update plaidlabs
  claude plugin update opscale@plaidlabs
적용: /reload-plugins를 실행하거나 Claude Code를 다시 시작하면 적용됩니다.
