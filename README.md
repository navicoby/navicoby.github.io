# navicoby.github.io
Spaitial Ai, BIM, SLAM, Landscape Architecture

## 게시 전 확인

다른 컴퓨터에서 작업할 때는 먼저 최신 `main`을 받아 기존 페이지 연결을 유지합니다. `static/<이름>/index.html`을 추가할 때는 `layouts/index.html`의 메인 화면에도 링크를 추가합니다.

```sh
hugo --minify
python3 scripts/check_static_navigation.py --public public
```

배포 과정에서도 같은 검사를 실행합니다. 최상위 정적 페이지가 메인 화면에서 누락되거나 빌드에 포함되지 않으면 게시를 중단합니다. 별도로 제공되는 외부 페이지와 각 글의 하위 자료는 이 검사 대상이 아닙니다.
