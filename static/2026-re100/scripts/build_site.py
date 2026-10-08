"""Build a portable GitHub Pages site from the Markdown guide. Requires Pandoc."""
from pathlib import Path
import html
import json
import re
import subprocess
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.2'
POLICY_DATE = '2026-10-08'
SOURCE_COUNT = len(json.loads((ROOT/'data'/'sources.json').read_text(encoding='utf-8')))
PAGES = [
 ('01-basics','RE100 기본 개념'),('02-trends','2026 국내외 동향'),
 ('03-procurement','조달 방식 비교'),('04-reading-claims','숫자와 주장 읽기'),
 ('05-checklist','실행계획과 체크리스트'),('06-faq','FAQ와 용어'),
 ('07-kgx','K-GX 전략과 실행계획'),('sources','출처와 편집 기준')]

def header(prefix='', current=''):
 return f'''<a class="skip" href="#main">본문으로 바로가기</a><header class="top"><div class="wrap"><a class="brand" href="{prefix}index.html">RE100<span>/ 2026</span></a><nav aria-label="주 메뉴"><a href="{prefix}pages/07-kgx.html">K-GX 해설</a><a class="desktop-only" href="{prefix}pages/02-trends.html">최신 동향</a><a class="desktop-only" href="{prefix}pages/03-procurement.html">조달 방식</a><a href="{prefix}pages/sources.html">출처</a><a class="desktop-only" href="https://github.com/navicoby/navicoby.github.io/tree/main/static/2026-re100">GitHub ↗</a></nav></div></header>'''

def footer(prefix=''):
 return f'''<footer class="foot"><div class="wrap"><div><strong>RE100 / 2026</strong><p>재생전력 전환을 이해하고 근거를 확인하는 공익 정보 프로젝트.<br>공식 기관의 인증·자문 서비스가 아닌 독립적인 공개 안내 자료입니다.</p><p>기존 동향 2026.09.23 · 실무 계산 2026.10.05 · K-GX 반영 {POLICY_DATE}<br>출처별 재확인 범위는 출처 목록에 표시합니다. · v{VERSION}</p></div><div class="links"><a href="{prefix}pages/sources.html">출처와 편집 기준</a><br><a href="https://github.com/navicoby/navicoby.github.io/issues">오류·새 자료 제안</a><br><a href="https://creativecommons.org/licenses/by/4.0/deed.ko">직접 작성 콘텐츠 CC BY 4.0</a></div></div></footer>'''

def document(title, body, prefix='', canonical=''):
 return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{html.escape(title)} | 2026 RE100 동향 안내</title><meta name="description" content="K-GX 전략과 RE100 국내외 동향, 조달 비용·증빙·공공주택·건물 실행계획을 공식 출처와 원문 쪽수로 읽는 한국어 공개 안내서."><meta property="og:title" content="{html.escape(title)} | 2026 RE100 동향 안내"><meta property="og:description" content="재생전력 전환의 물량·비용·실적과 K-GX 실행계획. 기존 동향 2026-09-23 · 실무 계산 2026-10-05 · K-GX 반영 {POLICY_DATE}."><meta property="og:type" content="website"><meta property="og:locale" content="ko_KR"><link rel="canonical" href="https://spatialflare.com/2026-re100/{canonical}"><link rel="stylesheet" href="{prefix}assets/style.css"></head><body>{header(prefix)}{body}{footer(prefix)}</body></html>'''

def convert(name):
 raw=subprocess.run(['pandoc',str(ROOT/'docs'/f'{name}.md'),'-f','gfm','-t','html5','--wrap=none'],capture_output=True,text=True,encoding="utf-8",check=True).stdout
 def link(m):
  parts=urlsplit(html.unescape(m.group(1)))
  path=parts.path
  if not parts.scheme and not parts.netloc:
   if path=='../README.md':path='../index.html'
   elif path in ('../CHANGELOG.md','../CONTRIBUTING.md','../LICENSE.md'):
    path='https://github.com/navicoby/navicoby.github.io/blob/main/static/2026-re100/'+path[3:]
   elif not path.startswith(('../','/')) and path.endswith('.md'):path=path[:-3]+'.html'
  url=urlunsplit((parts.scheme,parts.netloc,path,parts.query,parts.fragment))
  return 'href="'+html.escape(url,quote=True)+'"'
 raw=re.sub(r'href="([^"]+)"',link,raw)
 raw=re.sub(r'<input\b[^>]*>',lambda m: m.group(0) if 'type="checkbox"' not in m.group(0) or re.search(r'\bdisabled\b',m.group(0)) else m.group(0).replace('<input','<input disabled',1),raw)
 raw=re.sub(r'<table>', '<p class="table-hint">표가 잘리면 좌우로 움직여 보세요.</p><div class="table-scroll" role="region" aria-label="가로로 스크롤할 수 있는 표" tabindex="0"><table>',raw)
 raw=raw.replace('</table>','</table></div>')
 flow='<div class="flow" aria-label="실적 확인 순서">'+'<b aria-hidden="true">→</b>'.join('<span>'+s+'</span>' for s in ['조직·기간','사용량 확인','조달·증빙 대조','인정 실적','범위·한계 공개'])+'</div>'
 raw=re.sub(r'<pre class="mermaid">.*?</pre>',flow,raw,flags=re.S)
 raw=re.sub(r'<pre><code class="language-mermaid">.*?</code></pre>',flow,raw,flags=re.S)
 return raw

(ROOT/'pages').mkdir(exist_ok=True)
for name,title in PAGES:
 nav=''.join(f'<a href="{n}.html"'+(' aria-current="page"' if n==name else '')+f'>{t}</a>' for n,t in PAGES)
 options=''.join(f'<option value="{n}.html"'+(' selected' if n==name else '')+f'>{t}</option>' for n,t in PAGES)
 body=f'''<main id="main" class="wrap doc-shell"><aside class="side" aria-label="안내서 목차"><p>GUIDE / 2026</p>{nav}<a href="../index.html">← 안내서 처음으로</a></aside><div><div class="mobile-nav"><label for="page-select">안내서 목차</label><select id="page-select">{options}</select></div><article class="article">{convert(name)}<div class="doc-bottom">기존 동향: 2026-09-23 · 실무 계산: 2026-10-05 · K-GX 반영: {POLICY_DATE} · <a href="https://github.com/navicoby/navicoby.github.io/blob/main/static/2026-re100/docs/{name}.md">원고 보기</a> · <a href="https://github.com/navicoby/navicoby.github.io/issues">수정 제안</a></div></article></div></main><script src="../assets/navigation.js" defer></script>'''
 (ROOT/'pages'/f'{name}.html').write_text(document(title,body,'../','pages/'+name+'.html'),encoding='utf-8')

cards=[('07','07-kgx','K-GX 전략과 실행계획','100GW 목표에서 조달·건물·도시·증빙의 실행계획까지.'),('01','01-basics','RE100 기본 개념','글로벌 RE100, K-RE100, 탄소중립은 무엇이 다를까요?'),('02','02-trends','2026 국내외 동향','최근 발표와 지침에서 확인한 변화를 모았습니다.'),('03','03-procurement','조달 방식 비교','동일 물량의 비용 계산과 PPA 계약 질문을 확인합니다.'),('04','04-reading-claims','숫자와 주장 읽기','Scope 2 계산과 증빙 원장으로 실적의 근거를 살펴봅니다.'),('05','05-checklist','실행계획과 체크리스트','공공기관·임대건물 경계부터 90일 실행계획까지.'),('06','06-faq','FAQ와 용어','자주 생기는 오해와 어려운 용어를 풀어 설명합니다.')]
cardhtml=''.join(f'<a class="topic" href="pages/{n}.html"><span class="num">{i} / GUIDE</span><h3>{t}</h3><p>{d}</p><span class="arrow" aria-hidden="true">읽어보기 →</span></a>' for i,n,t,d in cards)
timeline=[('2026.10.07','K-GX: 공급 확대를 기관 실행계획으로','재생에너지 100GW 목표, REC 개편, PPA 지원과 건물 전환을 발표했습니다. 원문 쪽수와 추진상태를 함께 확인합니다.','정책 목표 · 추진'),('2026.09','조달량과 인정 실적을 함께 읽기','2025 RE100 연차보고서가 공개됐습니다. 발행연도와 실제 전력사용 기간을 구분해야 합니다.','공시 분석'),('2026.07–08','보고 지침과 회계 기준의 변화','RE100 보고 지침이 갱신되고 Scope 2 의견수렴 결과가 공개됐습니다. 현행 규칙과 개정 논의를 나눠 봅니다.','지침 · 논의'),('2026.02','국내 공공부문 이행의 확대','공공기관 K-RE100 출범 발표는 경영평가와 이행실적의 연결을 담고 있습니다. 적용대상 확인이 필요합니다.','정책 발표')]
timehtml=''.join(f'<div class="timeline"><time>{d}</time><div><h3>{t}</h3><p>{v}</p></div><span class="tag">{tag}</span></div>' for d,t,v,tag in timeline)
body=f'''<main id="main"><div class="wrap"><section class="hero" aria-labelledby="hero-title"><div><p class="eyebrow">PUBLIC KNOWLEDGE / K-GX UPDATE</p><h1 id="hero-title">2026 RE100<br><em>정책에서<br>실행계획으로</em></h1><p class="intro">K-GX 전략을 전력수요·조달·건물·도시의<br>실행계획으로 연결합니다.<br>정책의 목표와 시행 조건을 구분하고,<br>물량·비용·증빙을 공식 근거와 함께 살펴봅니다.</p><a class="button" href="pages/07-kgx.html">K-GX 해설 읽기 ↗</a><a class="button secondary" href="pages/01-basics.html">기본부터 알아보기</a><p class="hero-note">K-GX 반영 {POLICY_DATE} · 한국어 공개 안내 v{VERSION}<br>기존 동향 2026.09.23 · 실무 계산 2026.10.05</p></div><aside class="signal" aria-labelledby="signal-title"><span class="eyebrow">READ THE NUMBERS</span><h2 id="signal-title">보고한 비율과<br>인정된 비율은 다릅니다.</h2><div class="bar-row"><div class="bar-meta"><span>기업이 보고한 재생전력</span><strong>59%</strong></div><div class="bar-track" aria-hidden="true"><div class="bar reported"></div></div></div><div class="bar-row"><div class="bar-meta"><span>RE100이 인정한 재생전력</span><strong>43%</strong></div><div class="bar-track" aria-hidden="true"><div class="bar recognized"></div></div></div><p>2025 RE100 연차보고서 · 2026년 9월 발행<br>408개사 분석, 대부분 2024년 실적.<br>차이에는 인정 조건과 보고자료의 누락 등이 관여합니다.</p><a href="pages/02-trends.html" class="label">숫자의 범위와 원문 확인 →</a></aside></section><section class="policy-update" aria-labelledby="kgx-title"><div><p class="eyebrow">2026.10.07 POLICY / {POLICY_DATE} REVIEW</p><h2 id="kgx-title">K-GX 전략을 읽고<br>계획에서 바꿀 것</h2><p>국가의 공급 확대부터 기관의 전력 조달과 도시공간의 전환까지, 원문 쪽수를 따라 확인합니다.</p><a href="pages/07-kgx.html">K-GX 전체 해설 →</a></div><div class="policy-links"><a href="pages/07-kgx.html#targets"><strong>100GW</strong><span>2030년 국가 설비용량 목표<br>기관의 인정 물량과 구분하기</span></a><a href="pages/07-kgx.html#procurement"><strong>REC · PPA</strong><span>개편 세부안과 지원조건<br>계약·예산의 확인 항목으로</span></a><a href="pages/07-kgx.html#buildings"><strong>건물 · 도시</strong><span>절감·전기화·태양광<br>자산과 수요를 함께 계획하기</span></a></div></section><section class="section" aria-labelledby="guide-title"><div class="section-head"><h2 id="guide-title">필요한 내용부터 읽어보세요</h2><p>처음 만나는 개념부터 실무의 첫 질문까지</p></div><div class="topic-grid">{cardhtml}</div></section><section class="section" aria-labelledby="practice-title"><div class="section-head"><h2 id="practice-title">실무에서 자주 막히는 네 가지 질문</h2><p>가상 계산과 검토표로 구체화했습니다</p></div><div class="topic-grid"><a class="topic" href="pages/01-basics.html"><span class="num">물량 산정</span><h3>1MW면 얼마나 전환할까요?</h3><p>설비이용률 15% 가정에서 연 1,314MWh. 발전량과 인정량의 차이도 확인하세요.</p></a><a class="topic" href="pages/03-procurement.html"><span class="num">예산 비교</span><h3>같은 2,000MWh의 비용은?</h3><p>프리미엄·인증서·PPA를 같은 수요와 비용 범위로 비교합니다. 단가는 교육용 가정입니다.</p></a><a class="topic" href="pages/04-reading-claims.html"><span class="num">실적 확인</span><h3>전환비율과 배출량은 어떻게 연결될까요?</h3><p>지역기반·시장기반 계산, 계약·공급·증빙 물량을 구분합니다.</p></a><a class="topic" href="pages/05-checklist.html"><span class="num">실행계획</span><h3>어떤 자료부터 모을까요?</h3><p>사옥·임차공간·임대자산의 경계와 담당자, 90일 산출물을 정리합니다.</p></a></div></section><section class="section" aria-labelledby="trend-title"><div class="section-head"><h2 id="trend-title">지금 살펴볼 변화</h2><a href="pages/02-trends.html">동향 전체 보기 →</a></div>{timehtml}<p class="source-mini">각 항목의 적용 범위와 공식 원문은 동향 안내에 연결했습니다.</p></section><section class="section" aria-label="자료와 다운로드"><div class="downloads"><a href="pages/sources.html">출처 {SOURCE_COUNT}건 살펴보기 ↗</a><a href="data/indicators.csv" download>핵심 지표 CSV ↓</a><a href="templates/re100-checklist.csv" download>체크리스트 CSV ↓</a><a href="https://github.com/navicoby/navicoby.github.io/tree/main/static/2026-re100">GitHub에서 함께 보완하기 ↗</a></div></section></div></main>'''
(ROOT/'index.html').write_text(document('K-GX와 RE100, 정책에서 실행계획으로',body,canonical=''),encoding='utf-8')
(ROOT/'.nojekyll').write_text('')
print('Built index and',len(PAGES),'guide pages')

