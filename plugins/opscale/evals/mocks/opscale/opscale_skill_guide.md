# OPSCALE Skill 작성 지침 (요약)

- 번들 루트에 entry 파일 `skill.md`를 둔다. frontmatter의 `name`과 `description`은 필수이며 `name`은 `^[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*$` 형식이다.
- 런타임 tool 이름은 `{org}-{project}-{name}`으로 합쳐지며 128자를 넘을 수 없다.
- 부속 파일은 `references/`, `scripts/`, `assets/` 아래에 두고, entry 본문에서 어떤 파일을 언제 읽을지 명시한다. 런타임은 entry 파일만 inline으로 주고 나머지는 URI로만 준다.
- binary 파일은 `xlsx`, `xls`, `pdf`, `docx`만 허용되고 `pptx`는 지원하지 않는다.
- `opscale_read_bundle_file`, `opscale_get_asset_url`, `opscale_skill_guide`는 예약명이라 skill 이름으로 쓸 수 없다.
