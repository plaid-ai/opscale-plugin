---
expect:
  bundle_uri: /^ops-skill:\/\/[a-z]+\/demo\/[a-z0-9_]+[a-zA-Z0-9_\/.-]*$/
---
번들 zip URL (2개 파일, 90초 안에 최대 3번 받을 수 있음):
https://opscale-api.plaidlabs.ai/asset/v1/mock-bundle-token

새 임시 폴더에 받아 풀고 그 폴더에서 작업한 뒤, 끝나면(실패해도) 폴더를 지우세요.
macOS·Linux: curl -fsSL -o bundle.zip '<URL>' && unzip -q bundle.zip -d <임시 폴더>
Windows: curl.exe -fsSL -o bundle.zip "<URL>"; tar -xf bundle.zip -C <임시 폴더>
파일 내용은 entry 지시가 필요로 할 때만 여세요. 파일별 sha256은 structuredContent.files에 있습니다.
