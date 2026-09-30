---
title: "11 · 웹지도 게시와 모바일 읽기"
description: "웹지도를 정적 페이지에 게시하고 작은 화면과 느린 연결을 고려합니다."
eyebrow: "PART 03 / CHAPTER 11"
---

**학습 목표:** 웹지도를 정적 페이지에 게시하고 작은 화면과 느린 연결을 고려합니다.

**준비:** [실행 환경](../stack.html) · [도구와 용어](../glossary.html). 예제 자료는 별도 표시가 없는 한 합성 자료입니다.

## 개념

HTML은 문서 구조, CSS는 배치와 모양, JavaScript는 브라우저의 동작을 담당합니다. GitHub Pages는 이 정적 파일을 제공하는 호스팅 서비스입니다. 서버에서 Python을 상시 실행하는 분석 서비스가 아니므로 Python 분석 결과를 SVG·GeoJSON·HTML로 미리 만들어 게시합니다.

iframe은 다른 HTML 문서를 현재 페이지 안에 넣는 요소입니다. 지도 제목, 지도 밖 설명, 직접 열기 링크가 있어야 지도가 로드되지 않거나 키보드 조작이 어려워도 내용을 이해할 수 있습니다.

## 왜 필요한가

현장에서는 휴대전화로 읽을 수 있어야 합니다. 가로 1,000px 고정 지도나 긴 코드가 본문 전체를 밀어내면 설명을 읽기 어렵습니다.

## 핵심 API

HTML의 meta viewport, iframe title/loading, CSS의 width:100%, min-width:0, overflow:auto를 조합합니다. 지도는 사용자 선택 후 불러오고, 표와 코드만 내부에서 가로 스크롤하도록 합니다.

## 최소 실행 예제

{{code:chapter11.py}}

## 조경·도시 실무 예제

10장 예제를 먼저 실행하고 같은 폴더에서 이 예제를 실행하세요. 결과 파일 두 개를 함께 열어 검사합니다. 저장소에 올릴 때 소유자 로컬 경로가 아닌 상대 경로를 사용합니다.

## 시각화와 결과 읽기

320px, 375px, 768px, 데스크톱 너비에서 본문·표·코드를 확인합니다. 지도 외부의 설명은 확대·축소 없이 읽을 수 있어야 합니다. [모바일 집필 규칙](https://github.com/navicoby/navicoby.github.io/blob/main/.agents/skills/navicoby-geospatial-author/references/mobile.md)을 함께 사용하세요.

## 흔한 오류

HTML에 API 비밀키를 넣으면 방문자에게 공개됩니다. iframe 높이를 0으로 두거나 모든 요소에 overflow:hidden을 쓰면 내용이 잘립니다. 지도의 배경 타일 표기를 숨기지 않습니다.

## 연습문제

지도 위에 자료 날짜, 아래에 관찰 결과와 출처를 넣고 휴대전화 너비에서 표와 지도가 본문을 밀어내지 않는지 확인하세요.

[전체 예제 내려받기](../examples/chapter11.py) · 실행: `python chapter11.py`

## 다음 단계

[12 · NGII·VWorld·서울·공공데이터포털](data-portals.html)로 이어집니다.

## 출처

[GitHub Pages 소개](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [MDN iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe). 확인 2026-09-30.
