"""Build the static AR landscape library from its checked-in Markdown exports.

Install requirements.txt, then run from any working directory. No vault access
or network is needed. Generated pages are checked in for the normal Hugo build.
"""
from pathlib import Path
import csv, html, json, re
import markdown
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'static/augmented-reality-landscape'
BASE='https://spatialflare.com/augmented-reality-landscape/'
E=html.escape
CHAPTERS=json.loads((OUT/'text/chapters.json').read_text())
PAPERS=json.loads((OUT/'downloads/literature.json').read_text())
PARTS=[('개념과 역사','겹침의 역사에서 AR의 정의까지'),('사람의 시각','깊이·초점·지각의 조건'),('작동 원리','좌표·센서·추적·렌더링·입력'),('분야별 전개','군사에서 교육·문화유산까지'),('플랫폼과 사회','AI·표준·프라이버시·기기'),('조경과 증강현실','실무·지형·참여·식생의 질문')]
SEARCH=[]

def write(name,content):
    f=OUT/name; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(content)

def page(title,body,name='index.html',prefix='',active=''):
    description='증강현실의 개념과 기술에서 조경 실무·식생·현장 검증까지. 옵시디언 원고 29개 장과 140개 문헌 기록을 엮은 연구 웹판.'
    full_title = title + (' · 웹 개정판' if name == 'index.html' else ' · 증강현실과 조경')
    canonical = BASE + ('' if name == 'index.html' else name)
    nav=''.join(f'<a href="{prefix}{url}"'+(' aria-current="page"' if active==label else '')+f'>{label}</a>' for label,url in [('전체 목차','index.html#contents'),('현장 가이드','practice.html'),('사례·근거','evidence.html'),('문헌','literature.html'),('검색','search.html')])
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{E(full_title)}</title><meta name="description" content="{description}"><link rel="canonical" href="{canonical}"><meta property="og:type" content="article"><meta property="og:title" content="{E(full_title)}"><meta property="og:description" content="{description}"><meta property="og:url" content="{canonical}"><link rel="stylesheet" href="{prefix}assets/site.css"><script defer src="{prefix}assets/site.js"></script></head>
<body><a class="skip" href="#main">본문으로 건너뛰기</a><div id="progress" aria-hidden="true"></div><header class="top"><div class="top-inner"><a class="brand" href="{prefix}index.html"><span class="brand-icon">S/F</span><span>SpatialFlare <small>RESEARCH LIBRARY</small></span></a><nav aria-label="주요 메뉴">{nav}</nav></div></header>{body}
<footer><div class="wrap footer-inner"><a href="/">← SpatialFlare 홈</a><span>증강현실과 조경 · 웹 개정판 · 2026.09.30</span><a href="{prefix}editorial.html">구성·편집 기록</a><a href="{prefix}index.html#downloads">자료 내려받기</a><a href="https://github.com/navicoby/navicoby.github.io/tree/main/static/augmented-reality-landscape">GitHub</a></div></footer></body></html>'''

def render(md):
    md=md.replace('\\newpage','')
    # No HTML scripts from source notes; this collection uses plain Markdown.
    raw=markdown.markdown(md,extensions=['tables','fenced_code','footnotes','sane_lists'])
    soup=BeautifulSoup(raw,'html.parser')
    for t in soup(['script','iframe','object','embed','style']): t.decompose()
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.startswith('on'):del tag[attr]
        if tag.get('href','').lower().startswith(('javascript:','data:')):del tag['href']
    toc=[]
    for i,h in enumerate(soup.find_all(['h2','h3','h4']),1):
        h['id']=f'section-{i}'
        if h.name in ('h2','h3'):toc.append((h['id'],h.get_text()))
    for table in soup.find_all('table'):
        wrapper=soup.new_tag('div',attrs={'class':'table-scroll','tabindex':'0','role':'region','aria-label':'표 — 가로로 스크롤할 수 있습니다'})
        table.wrap(wrapper)
    for a in soup.find_all('a',href=True):
        if a['href'].startswith('http'):a['rel']='noreferrer'
    return str(soup),toc,soup.get_text(' ',strip=True)

def add_search(title,url,text,kind):
    SEARCH.append(dict(title=title,url=url,text=text,kind=kind))

def reading_page(title,md,name,eyebrow,summary,chapter=None):
    prefix='../' if name.startswith('chapters/') else ''
    body_md='\n'.join(md.splitlines()[1:]).strip()
    if chapter:
        # The original chapter has h2 title, h3 sections; use a semantic h1/h2 outline.
        body_md=re.sub(r'^(#{3,6})(?= )',lambda m:m[1][1:],body_md,flags=re.M)
    content,toc,plain=render(body_md)
    add_search(title,name,plain,'본문' if chapter else '보완 글')
    sidenav=''.join(f'<a href="#{anchor}">{E(label)}</a>' for anchor,label in toc)
    note=''
    if chapter:
        n=chapter['n']
        if chapter['corrections']:note='<aside class="editor-note"><strong>웹판 보완</strong><p>'+E(' '.join(chapter['corrections']))+f'</p><a href="{prefix}evidence.html">근거와 수정 범위 보기 ↗</a></aside>'
        end='<nav class="pager" aria-label="장 이동">'
        if n>1:end+=f'<a href="ch{n-1:02}.html">← 이전 장 <span>{E(CHAPTERS[n-2]["title"])}</span></a>'
        end+=f'<a href="../index.html#part-{chapter["part"]}">전체 목차 <span>제{chapter["part"]}부</span></a>'
        if n<33:end+=f'<a href="ch{n+1:02}.html">다음 장 → <span>{E(CHAPTERS[n]["title"])}</span></a>'
        end+='</nav>'
        source=f'<p class="source-note">옵시디언 원고 기반 · 웹판 편집 2026.09.30 · <a href="../text/ch{n:02}.md">이 장의 Markdown</a> · <a href="../editorial.html">편집 범위</a></p>'
        if chapter['status']=='planned':
            content='<div class="planned-note"><p class="eyebrow">집필 예정</p><h2>이 장의 본문은 아직 없습니다.</h2><p>원래 기획의 장 번호를 유지했습니다. 현재 읽을 수 있는 29개 장과 웹판 보완 글은 전체 목차에서 찾을 수 있습니다.</p><a class="button" href="../index.html#contents">수록된 본문 보기</a></div>'
        else:
            source+='<p class="source-note">이 본문은 조사 당시의 연구 원고입니다. 제품 상태·가격·수치와 해석은 출처·조사 범위와 함께 읽어 주세요.</p>'
    else:
        end='<nav class="pager" aria-label="관련 페이지"><a href="index.html#contents">← 전체 목차</a><a href="practice.html">현장 가이드</a><a href="evidence.html">사례·근거</a></nav>'
        source='<p class="source-note">웹판 보완 글 · 2026.09.30</p>'
    return page(title,f'''<main id="main" class="wrap reading"><div class="breadcrumb"><a href="{prefix}index.html">연구 라이브러리</a> / {E(eyebrow)}</div><div class="reader-grid"><aside class="reader-sidebar"><details open><summary>이 글의 목차</summary><nav aria-label="절 목차">{sidenav or '<span>집필 예정</span>'}</nav></details><a class="back-link" href="{prefix}index.html#contents">← 전체 6부 목차</a></aside><article><header class="article-head"><p class="eyebrow">{E(eyebrow)}</p><h1>{E(title)}</h1><p class="lead">{E(summary)}</p>{source}</header>{note}<div class="prose">{content}</div>{end}</article></div></main>''',name,prefix)

def chapter_list(part):
    rows=''
    for c in CHAPTERS:
        if c['part']!=part:continue
        badge='<span class="status">집필 예정</span>' if c['status']=='planned' else ''
        rows+=f'<li><a href="chapters/ch{c["n"]:02}.html"><span class="chapter-number">{c["n"]:02}</span><span><strong>{E(c["title"])}</strong><small>{E(c["summary"])}</small></span><span class="row-end">{badge} ↗</span></a></li>'
    return rows

def home():
    parts=''.join(f'<a href="#part-{i}"><b>0{i}</b><span>{title}</span></a>' for i,(title,_) in enumerate(PARTS,1))
    contents=''.join(f'<section class="part" id="part-{i}"><div class="part-heading"><span class="eyebrow">PART 0{i}</span><h3>{title}</h3><p>{desc}</p></div><ol class="chapter-list">{chapter_list(i)}</ol></section>' for i,(title,desc) in enumerate(PARTS,1))
    return page('증강현실과 조경',f'''<main id="main">
<section class="hero"><div class="wrap hero-grid"><div><p class="eyebrow">LANDSCAPE × AUGMENTED REALITY / 2026</p><h1>아직 자라지 않은<br>풍경을, <em>지금 여기.</em></h1><p class="hero-title">증강현실과 조경</p><p class="hero-description">겹쳐 보이는 기술에서, 변해가는 경관으로.<br>AR의 개념과 원리, 조경의 현장과 식생을 하나의 읽기 흐름으로 엮었습니다.</p><div class="actions"><a class="button" href="#contents">전체 원고 읽기 <span>↓</span></a><a class="text-link" href="practice.html">조경 현장 가이드 ↗</a></div></div><figure class="cover-art"><img src="assets/landscape.svg" alt="동일한 지형 위에 현재 수목과 미래 수관 시나리오를 겹쳐 표현한 개념도"><figcaption><span>FIELD NOTES / 01</span><span>현재의 장소 + 시간의 시나리오</span></figcaption></figure></div><div class="wrap hero-bottom"><span><strong>29</strong> 수록 장</span><span><strong>6</strong> 주제의 흐름</span><span><strong>140</strong> 문헌 기록</span><a href="editorial.html">웹 개정판 · 2026.09.30 ↗</a></div></section>
<section class="wrap start"><div class="section-label"><span class="eyebrow">START HERE</span><h2>어디서부터 읽을까요?</h2></div><div class="paths"><a href="chapters/ch04.html"><b>01 / 개념부터</b><h3>AR을 처음 읽는다면</h3><p>정의 → 깊이 지각 → 좌표와 정합 → 조경의 질문</p><span>4 · 6 · 10 · 12 · 26 · 33장 →</span></a><a href="practice.html"><b>02 / 현장부터</b><h3>조경 업무에 연결한다면</h3><p>현장 가이드 → 실무 기록 → 지형 → 주민참여 → 식생</p><span>가이드 · 26 · 27 · 29 · 32 · 33장 →</span></a><a href="chapters/ch10.html"><b>03 / 구현부터</b><h3>개발과 연구를 한다면</h3><p>좌표 → 센서 → 추적 → 지연 → AI와 플랫폼</p><span>10 · 11 · 12 · 13 · 22 · 23 · 28장 →</span></a></div></section>
<section class="wrap feature"><div><p class="eyebrow">FROM RESEARCH TO PRACTICE</p><h2>가능한 것과<br>입증된 것을 구분합니다.</h2><p>공식 기능, 연구 시연, 현장 적용, 운영 성과는 서로 다른 근거입니다. 원고의 단정적인 표현을 다듬고, 생장·계절과 야외 깊이 표현을 공식 자료로 보완했습니다.</p><a class="text-link" href="evidence.html">사례와 근거 읽기 ↗</a></div><div class="feature-list"><a href="practice.html"><span>01</span><div><h3>현장 적용 가이드</h3><p>의사결정·좌표·식물 속성·검증·성과품을 연결하는 여섯 단계</p></div>↗</a><a href="chapters/ch33.html"><span>02</span><div><h3>자라는 것을 어떻게 보여줄까</h3><p>생장과 계절, 수관과 가림, 아직 오지 않은 경관의 불확실성</p></div>↗</a><a href="literature.html"><span>03</span><div><h3>140개 문헌을 주제별로</h3><p>지형·수문부터 주민참여·식생까지, 검색과 DOI로 이어 읽기</p></div>↗</a></div></section>
<section class="wrap contents" id="contents"><div class="section-label"><div><p class="eyebrow">THE READING COLLECTION</p><h2>여섯 부로 읽는 전체 목차</h2></div><a href="search.html">본문 검색 ↗</a></div><p class="contents-note">원래의 33개 장 번호를 유지했습니다. 본문 29개 장을 수록하고, 미집필 2·3·7·8장은 ‘집필 예정’으로 표시했습니다.</p><nav class="part-nav" aria-label="부별 목차">{parts}</nav>{contents}</section>
<section class="downloads" id="downloads"><div class="wrap"><div class="section-label"><div><p class="eyebrow">KEEP & READ</p><h2>자료 내려받기</h2></div><a href="editorial.html">원본과 웹판의 차이 ↗</a></div><p>PDF와 원본 합본은 옵시디언의 보존본입니다. 웹판의 수정·보완 내용은 편집 기록과 웹판 합본에서 확인하세요.</p><div class="download-grid"><a href="downloads/web-edition.md" download><b>웹 개정판 합본</b><span>본문 + 보완 글 · Markdown ↓</span></a><a href="downloads/landscape-ar-original.pdf"><b>증강현실과 조경</b><span>원본 PDF · 6.6 MB ↓</span></a><a href="downloads/research-original.pdf"><b>조사 원본</b><span>원본 PDF · 7.1 MB ↓</span></a><a href="downloads/preliminary-research.pdf"><b>사전조사</b><span>원본 PDF · 0.7 MB ↓</span></a><a href="downloads/literature.csv" download><b>문헌 목록</b><span>140개 기록 · CSV ↓</span></a><a href="downloads/field-checklist.csv" download><b>현장 검증 기록표</b><span>빈 양식 · CSV ↓</span></a></div><div class="minor-links"><a href="downloads/obsidian-manuscript.md">옵시디언 원본 합본</a><a href="downloads/research-notes.md">조사 노트 원본</a><a href="v1.html">이전 웹판 v1</a><a href="downloads/source-manifest.json">원본 목록</a></div></div></section></main>''')

def literature():
    categories=list(dict.fromkeys(p['category'] for p in PAPERS))
    options=''.join(f'<option>{E(c)}</option>' for c in categories)
    rows=''
    for p in PAPERS:
        title=E(p['title']);doi=p.get('doi','').strip()
        link=f'<a href="https://doi.org/{E(doi)}" rel="noreferrer">DOI ↗</a>' if doi and not re.search(r'[\s<>]',doi) else '<span>DOI 미기재</span>'
        text=' '.join(str(p.get(k,'')) for k in ['title','category','summary','use','caution','year','doi'])
        rows+=f'<article class="paper" data-category="{E(p["category"])}" data-search="{E(text.lower())}"><div class="paper-meta"><span>{E(p["category"])}</span><span>{p.get("year") or "연도 미상"}</span></div><h2>{title}</h2><p class="venue">{E(p.get("venue", "") or "게재처 미기재")}</p><p>{E(p.get("summary", ""))}</p><details><summary>조경과의 연결 · 해석 주의점</summary><p><strong>활용 관점</strong> {E(p.get("use", ""))}</p><p><strong>주의점</strong> {E(p.get("caution", ""))}</p></details><div class="paper-link">{link}</div></article>'
        add_search(p['title'],'literature.html?q='+__import__('urllib.parse',fromlist=['quote']).quote(p['title']),text,'문헌')
    body=f'''<main id="main" class="wrap collection"><p class="eyebrow">RESEARCH INDEX</p><h1>문헌으로 이어 읽기</h1><p class="lead">조경 관련 조사에서 분류한 140개 문헌 기록. 원고의 질문을 논문과 연구 자료로 연결합니다.</p><p class="notice">분류·요약은 옵시디언 조사자료를 옮겼습니다. 동일 연구의 다른 판본이 포함될 수 있으며, 모든 전문을 재검증한 목록은 아닙니다. 인용 수와 현재 제품 상태는 제공하지 않습니다.</p><div class="filter-bar"><label>제목·주제·키워드<input type="search" id="paper-query" placeholder="예: 식생, flood, 참여설계" autocomplete="off"></label><label>주제<select id="paper-category"><option value="">전체 주제</option>{options}</select></label><button type="button" id="paper-reset">초기화</button><a href="downloads/literature.csv" download>CSV 내려받기 ↓</a></div><p id="paper-count" role="status" aria-live="polite">140개 문헌 기록</p><div class="papers">{rows}</div><p id="paper-empty" hidden>검색 결과가 없습니다. 다른 단어나 전체 주제로 검색해 보세요.</p><noscript><p>검색 필터에는 JavaScript가 필요합니다. 전체 목록은 아래에서 그대로 읽을 수 있습니다.</p></noscript></main>'''
    return page('문헌으로 이어 읽기',body,'literature.html',active='문헌')

def main():
    write('index.html',home())
    for c in CHAPTERS:
        md=(OUT/'text'/f'ch{c["n"]:02}.md').read_text()
        write(f'chapters/ch{c["n"]:02}.html',reading_page(c['title'],md,f'chapters/ch{c["n"]:02}.html',f'제{c["part"]}부 · {PARTS[c["part"]-1][0]} / 제{c["n"]}장',c['summary'],c))
    for key,title,summary in [('practice','조경 AR 현장 적용 가이드','의사결정을 정하고, 데이터를 준비하고, 현장에서 검증하고, 다시 확인할 수 있는 기록을 남기는 방법.'),('evidence','사례와 기술을 읽는 기준','공식 자료로 확인한 기능과, 별도로 검증해야 할 현장 성과를 나눕니다.'),('editorial','이 웹판의 구성과 편집 기록','어떤 원고를 옮겼고 무엇을 보완했는지, 확인 범위와 남은 작업을 기록합니다.')]:
        write(key+'.html',reading_page(title,(OUT/'text'/f'{key}.md').read_text(),key+'.html','웹판 보완 · 2026.09.30',summary))
    write('literature.html',literature())
    searchbody='''<main id="main" class="wrap collection search-page"><p class="eyebrow">SEARCH THE COLLECTION</p><h1>원고와 문헌 검색</h1><p class="lead">장 제목, 본문, 보완 글, 문헌 기록에서 찾습니다.</p><form id="search-form" class="search-form"><label for="search-query">검색어</label><div><input id="search-query" type="search" name="q" placeholder="예: 수관, 좌표, SLAM, 주민참여" required><button type="submit">검색</button></div></form><p id="search-status" role="status" aria-live="polite">단어를 입력해 검색하세요. 검색 결과에서 해당 글로 이동할 수 있습니다.</p><div id="search-results"></div><noscript><p>전체 검색에는 JavaScript가 필요합니다. <a href="index.html#contents">전체 목차</a> 또는 <a href="downloads/web-edition.md">합본</a>에서 내용을 찾을 수 있습니다.</p></noscript></main>'''
    write('search.html',page('원고와 문헌 검색',searchbody,'search.html',active='검색'))
    write('assets/search-index.json',json.dumps(SEARCH,ensure_ascii=False,separators=(',',':')))
    with (OUT/'downloads/literature.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f,lineterminator="\n");w.writerow(['주제','연도','제목','게재처','DOI','요약','활용 관점','주의점'])
        for p in PAPERS:w.writerow([p.get(k,'') for k in ['category','year','title','venue','doi','summary','use','caution']])
    with (OUT/'downloads/field-checklist.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f,lineterminator="\n");w.writerow(['프로젝트','시험일시','관찰점 ID','관찰 위치','과제','기기·OS·앱 버전','모델 버전','좌표계·표고 기준','관찰 거리(m)','조명·날씨·수관 조건','위치 편차(m)','높이 편차(m)','방향 편차(도)','추적 회복 시간(s)','판정 기준','결과·문제','대안·시점·계절','생장 가정·출처','화면 파일','검토자','결정·후속 조치']);w.writerow(['']*21)
    combined=['# 증강현실과 조경 — 웹 개정판\n\n편집일: 2026-09-30\n\n本文 29개 장, 집필 예정 4개 장. 보완 범위는 편집 기록을 참조하세요.\n']
    for key in ['editorial','evidence','practice']:combined.append((OUT/'text'/f'{key}.md').read_text())
    for c in CHAPTERS:
        content=(OUT/'text'/f'ch{c["n"]:02}.md').read_text()
        if c['corrections']:content=content.split('\n',1)[0]+'\n\n> 웹판 보완: '+' '.join(c['corrections'])+'\n\n'+content.split('\n',1)[1]
        combined.append(content)
    combined_text='\n\n---\n\n'.join(combined).replace('本文','본문')
    combined_text=re.sub(r'\]\(((?:chapters/|downloads/|text/)[^)]+|(?:index|editorial|practice|evidence|v1)\.html[^)]*|manuscript-v1\.md)\)',lambda m:']('+BASE+m[1]+')',combined_text)
    write('downloads/web-edition.md',combined_text)
    print(f'Built 39 HTML pages, {len(SEARCH)} search documents, {len(PAPERS)} literature records')

if __name__=='__main__':main()
