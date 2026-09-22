"""Build a portable GitHub Pages site from the Markdown guide. Requires Pandoc."""
from pathlib import Path
import html
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
 ('01-basics','RE100 기본 개념'),('02-trends','2026 국내외 동향'),
 ('03-procurement','조달 방식 비교'),('04-reading-claims','숫자와 주장 읽기'),
 ('05-checklist','첫 검토 체크리스트'),('06-faq','FAQ와 용어'),('sources','출처와 편집 기준')]

def header(prefix='', current=''):
 return f'''<a class="skip" href="#main">본문으로 바로가기</a><header class="top"><div class="wrap"><a class="brand" href="{prefix}index.html">RE100<span>/ 2026</span></a><nav aria-label="주 메뉴"><a href="{prefix}pages/02-trends.html">최신 동향</a><a class="desktop-only" href="{prefix}pages/03-procurement.html">조달 방식</a><a href="{prefix}pages/sources.html">출처</a><a class="desktop-only" href="https://github.com/navicoby/navicoby.github.io/tree/main/static/2026-re100">GitHub ↗</a></nav></div></header>'''

def footer(prefix=''):
 return f'''<footer class="foot"><div class="wrap"><div><strong>RE100 / 2026</strong><p>재생전력 전환을 이해하고 근거를 확인하는 공익 정보 프로젝트.<br>공식 기관의 인증·자문 서비스가 아닌 독립적인 공개 안내 자료입니다.</p><p>자료 확인일 2026.09.23 · 기준일 이후 자동 갱신되지 않습니다.</p></div><div class="links"><a href="{prefix}pages/sources.html">출처와 편집 기준</a><br><a href="https://github.com/navicoby/navicoby.github.io/issues">오류·새 자료 제안</a><br><a href="https://creativecommons.org/licenses/by/4.0/deed.ko">직접 작성 콘텐츠 CC BY 4.0</a></div></div></footer>'''

def document(title, body, prefix='', canonical=''):
 return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{html.escape(title)} | 2026 RE100 동향 안내</title><meta name="description" content="2026년 RE100 국내외 동향, 재생전력 조달 방식, 증빙과 수치의 의미를 공식 출처와 함께 읽는 한국어 공개 안내서."><meta property="og:title" content="{html.escape(title)} | 2026 RE100 동향 안내"><meta property="og:description" content="재생전력 전환을 이해하고, 숫자와 주장에 담긴 의미를 함께 읽습니다. 자료 확인일 2026-09-23."><meta property="og:type" content="website"><meta property="og:locale" content="ko_KR"><link rel="canonical" href="https://navicoby.github.io/2026-re100/{canonical}"><link rel="stylesheet" href="{prefix}assets/style.css"></head><body>{header(prefix)}{body}{footer(prefix)}</body></html>'''

def convert(name):
 raw=subprocess.run(['pandoc',str(ROOT/'docs'/f'{name}.md'),'-f','gfm','-t','html5','--wrap=none'],capture_output=True,text=True,check=True).stdout
 def link(m):
  url=m.group(1)
  if url=='../README.md':url='../index.html'
  elif not url.startswith(('https:','http:','../')) and url.endswith('.md'):url=url[:-3]+'.html'
  elif url in ('../CHANGELOG.md','../CONTRIBUTING.md','../LICENSE.md'):url='https://github.com/navicoby/navicoby.github.io/blob/main/static/2026-re100/'+url[3:]
  return 'href="'+url+'"'
 raw=re.sub(r'href="([^"]+)"',link,raw)
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
 body=f'''<main id="main" class="wrap doc-shell"><aside class="side" aria-label="안내서 목차"><p>GUIDE / 2026</p>{nav}<a href="../index.html">← 안내서 처음으로</a></aside><div><div class="mobile-nav"><label for="page-select">안내서 목차</label><select id="page-select">{options}</select></div><article class="article">{convert(name)}<div class="doc-bottom">공개 자료 확인일: 2026-09-23 · <a href="https://github.com/navicoby/navicoby.github.io/blob/main/static/2026-re100/docs/{name}.md">원고 보기</a> · <a href="https://github.com/navicoby/navicoby.github.io/issues">수정 제안</a></div></article></div></main><script src="../assets/navigation.js" defer></script>'''
 (ROOT/'pages'/f'{name}.html').write_text(document(title,body,'../','pages/'+name+'.html'))

cards=[('01','01-basics','RE100 기본 개념','글로벌 RE100, K-RE100, 탄소중립은 무엇이 다를까요?'),('02','02-trends','2026 국내외 동향','최근 발표와 지침에서 확인한 변화를 모았습니다.'),('03','03-procurement','조달 방식 비교','녹색프리미엄부터 PPA와 자가소비까지 살펴봅니다.'),('04','04-reading-claims','숫자와 주장 읽기','기업의 ‘100%’ 발표를 읽을 때 확인할 다섯 가지.'),('05','05-checklist','첫 검토 체크리스트','목적과 사용량부터 비용·증빙·공개까지 점검합니다.'),('06','06-faq','FAQ와 용어','자주 생기는 오해와 어려운 용어를 풀어 설명합니다.')]
cardhtml=''.join(f'<a class="topic" href="pages/{n}.html"><span class="num">{i} / GUIDE</span><h3>{t}</h3><p>{d}</p><span class="arrow" aria-hidden="true">읽어보기 →</span></a>' for i,n,t,d in cards)
timeline=[('2026.09','조달량과 인정 실적을 함께 읽기','2025 RE100 연차보고서가 공개됐습니다. 발행연도와 실제 전력사용 기간을 구분해야 합니다.','공시 분석'),('2026.07–08','보고 지침과 회계 기준의 변화','RE100 보고 지침이 갱신되고 Scope 2 의견수렴 결과가 공개됐습니다. 현행 규칙과 개정 논의를 나눠 봅니다.','지침 · 논의'),('2026.02','국내 공공부문 이행의 확대','공공기관 K-RE100 출범 발표는 경영평가와 이행실적의 연결을 담고 있습니다. 적용대상 확인이 필요합니다.','정책 발표')]
timehtml=''.join(f'<div class="timeline"><time>{d}</time><div><h3>{t}</h3><p>{v}</p></div><span class="tag">{tag}</span></div>' for d,t,v,tag in timeline)
body=f'''<main id="main"><div class="wrap"><section class="hero" aria-labelledby="hero-title"><div><p class="eyebrow">PUBLIC KNOWLEDGE / RENEWABLE ELECTRICITY</p><h1 id="hero-title">2026 RE100<br><em>동향을 읽는<br>안내서</em></h1><p class="intro">재생전력 전환은 어디까지 왔을까요?<br>국내외 변화와 조달 방식, 숫자의 의미를<br>누구나 확인할 수 있는 근거와 함께 정리했습니다.</p><a class="button" href="pages/02-trends.html">최근 동향 읽기 ↗</a><a class="button secondary" href="pages/01-basics.html">기본부터 알아보기</a><p class="hero-note">자료 확인일 2026.09.23 &nbsp; / &nbsp; 한국어 공개 안내 · v1.0</p></div><aside class="signal" aria-labelledby="signal-title"><span class="eyebrow">READ THE NUMBERS</span><h2 id="signal-title">보고한 비율과<br>인정된 비율은 다릅니다.</h2><div class="bar-row"><div class="bar-meta"><span>기업이 보고한 재생전력</span><strong>59%</strong></div><div class="bar-track" aria-hidden="true"><div class="bar reported"></div></div></div><div class="bar-row"><div class="bar-meta"><span>RE100이 인정한 재생전력</span><strong>43%</strong></div><div class="bar-track" aria-hidden="true"><div class="bar recognized"></div></div></div><p>2025 RE100 연차보고서 · 2026년 9월 발행<br>408개사 분석, 대부분 2024년 실적.<br>차이에는 인정 조건과 보고자료의 누락 등이 관여합니다.</p><a href="pages/02-trends.html" class="label">숫자의 범위와 원문 확인 →</a></aside></section><section class="section" aria-labelledby="guide-title"><div class="section-head"><h2 id="guide-title">필요한 내용부터 읽어보세요</h2><p>처음 만나는 개념부터 실무의 첫 질문까지</p></div><div class="topic-grid">{cardhtml}</div></section><section class="section" aria-labelledby="trend-title"><div class="section-head"><h2 id="trend-title">지금 살펴볼 변화</h2><a href="pages/02-trends.html">동향 전체 보기 →</a></div>{timehtml}<p class="source-mini">각 항목의 적용 범위와 공식 원문은 동향 안내에 연결했습니다.</p></section><section class="section" aria-label="자료와 다운로드"><div class="downloads"><a href="pages/sources.html">출처 15건 살펴보기 ↗</a><a href="data/indicators.csv" download>핵심 지표 CSV ↓</a><a href="templates/re100-checklist.csv" download>체크리스트 CSV ↓</a><a href="https://github.com/navicoby/navicoby.github.io/tree/main/static/2026-re100">GitHub에서 함께 보완하기 ↗</a></div></section></div></main>'''
(ROOT/'index.html').write_text(document('재생전력 전환, 지금 어디까지 왔을까요?',body,canonical=''))
(ROOT/'.nojekyll').write_text('')
print('Built index and',len(PAGES),'guide pages')
