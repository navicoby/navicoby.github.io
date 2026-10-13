# 방문자 통계 설치 (SPATIALFLARE)

Hugo 공통 부분 템플릿 `layouts/partials/analytics.html`을 통해 홈 화면과 PaperMod 게시글 전체에 동일한 방식으로 적용합니다.

## 시작하기

1. [Google Analytics](https://analytics.google.com/)에서 웹 데이터 스트림을 만들고 `G-...` 형식의 **측정 ID**를 발급받습니다.
2. [Microsoft Clarity](https://clarity.microsoft.com/)에서 프로젝트를 만들고 **Project ID**를 발급받습니다.
3. `hugo.toml`의 `[params.analytics]`에 두 값을 입력합니다.
4. `hugo --minify`로 빌드하고 배포합니다. 실제 수집은 방문자가 동의 버튼을 누른 다음 시작됩니다.

두 ID를 비워두면 분석 스크립트나 동의 배너는 표시되지 않습니다. 한쪽 ID만 등록해도 동작합니다.

## 확인

- 빌드한 `public/index.html`과 임의의 게시글 HTML에 `sf-analytics-consent`가 있는지 확인합니다.
- 브라우저 개발자 도구 Network 탭에서 동의 **전**에는 `googletagmanager.com/gtag/js`, `clarity.ms/tag` 요청이 없고, 동의 **후** 요청이 생기는지 확인합니다.
- GA4 실시간 보고서와 Clarity 대시보드에서 데이터 유입을 확인합니다. 광고 차단기 등으로 수집이 차단될 수 있습니다.
- 같은 브라우저에서 선택을 다시 시험하려면 개발자 도구 Local Storage의 `sf_analytics_consent_v1` 항목을 삭제합니다.

## 개인정보

- GA4·Clarity를 통해 사이트 운영자에게 방문자 원본 IP 주소가 제공되는 것은 아닙니다.
- 별도 IP 수집 서버를 추가하지 않았습니다.
- 실제 운영 전에 도메인 `spatialflare.com`의 개인정보 처리방침에 분석 목적, 수집 항목, 제공업체, 보유기간, 선택 및 철회 방법을 기재하십시오.
- 동의 철회 기능을 별도로 운영 정책/페이지에 추가하는 것이 좋습니다. 브라우저 저장 정보 삭제만으로는 이용자용 철회 UI를 대체하기 어렵습니다.
- 세션 기록에 개인정보가 들어가지 않도록 Clarity 마스킹 설정을 검토하십시오.
