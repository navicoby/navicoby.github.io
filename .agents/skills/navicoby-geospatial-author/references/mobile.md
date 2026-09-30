# 모바일 UX 규칙

기준 폭은 320 / 375 / 768 / 1280px. 새 장마다 페이지 전체의 가로 넘침이 없는지 확인한다. 긴 코드·표는 해당 영역 안에서만 스크롤한다.

```css
.layout { display:grid; grid-template-columns:14rem minmax(0,1fr); }
main, article { min-width:0; }
pre { max-width:100%; overflow:auto; white-space:pre; }
code { overflow-wrap:anywhere; }
pre code { overflow-wrap:normal; }
.table-scroll { max-width:100%; overflow-x:auto; }
img, svg { max-width:100%; height:auto; }
.map-frame { width:100%; height:clamp(320px,60vh,540px); border:0; }
@media(max-width:800px) { .layout { display:block; } }
```

본문 17px/1.8 전후, 코드 13~14px 이상, 문장 폭 70~80자 이내를 지향한다. 터치 버튼 최소 높이 44px, 충분한 간격, 키보드 focus, 대비 있는 링크를 제공한다. 모바일의 접는 목차는 native details/summary로 JS 없이도 사용 가능하게 한다.

표의 첫 행은 th, 캡션 또는 인접 제목을 제공한다. 넓은 표는 focus 가능한 role=region 스크롤 영역에 넣고 “가로로 스크롤”을 표시한다. 단순히 모든 표 글자를 줄이지 않는다.

지도는 버튼을 누를 때 iframe을 만들고, `title`, `loading=lazy`, 전체 지도 링크, 정적 SVG 대안을 제공한다. 지도 내부의 휠 줌은 기본 해제한다. 외부 타일/CDN에 연결할 때 출처를 가리지 않는다. iframe이 실패해도 학습 결과는 읽을 수 있어야 한다.

코드 복사는 progressive enhancement로 구현한다. clipboard 접근 실패 시 직접 선택할 수 있게 안내한다. 줄바꿈 토글을 제공해 좁은 화면에서 긴 명령을 읽을 수 있게 한다. 인쇄 시 탐색·버튼·iframe을 숨기고 코드 줄바꿈·정적 그림을 유지한다. 과도한 모션을 피하고 reduced-motion을 존중한다.

검증: 실제 브라우저에서 랜딩·가장 긴 코드 장·표·지도 열기·접는 목차·본문 앵커·키보드 이동을 확인한다. 자동 크기 검사는 시각 검토의 대체가 아니다. 실제 확인한 폭과 확인 못한 항목을 QA 기록에 남긴다.

## 개념도 읽기

여러 패널을 한 장의 넓은 SVG에 몰아넣지 않습니다. 개별 SVG와 HTML 설명을 반응형 격자로 조합해 1100px 이하에서 세로로 쌓습니다. SVG에 viewBox·title·desc, HTML img에 alt·명시적 width/height를 둡니다. 중요한 주석은 이미지 안에만 두지 않고 HTML로 반복하며 '그림 크게 보기' 링크를 제공합니다. 문서 가로 넘침, 이미지 잘림, SVG 글자 겹침, 실제 320/375px에서의 가독성을 확인합니다.

## 부·장 탐색

데스크톱은 10부별 details 그룹으로, 모바일은 상단 전체 목차 안에 같은 그룹으로 표시합니다. 현재 장의 부는 열린 상태이고 현재 장 링크에는 aria-current=page를 둡니다. 각 부에는 소개 링크, 각 장 아래에는 이전/다음 링크를 둡니다. 320px·375px·768px·1280px에서 문서 전체 가로 넘침을 검사하고 표·코드만 내부 스크롤하도록 합니다.
