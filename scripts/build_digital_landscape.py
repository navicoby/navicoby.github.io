"""Build the author-supplied book without rewriting the manuscript.

Inputs: books/digital-landscape-architecture/{manuscript.md,figures.json,
source-manifest.json,review-pages.json,supplements.json}. No remote reads.
Output: static/digital-landscape-architecture/. Original sources stay untouched.
"""
from pathlib import Path
from html import escape
from urllib.parse import urlparse, unquote
import argparse
import hashlib
import json
import re
import unicodedata
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'books/digital-landscape-architecture'
OUT = ROOT / 'static/digital-landscape-architecture'
BASE = '/digital-landscape-architecture/'
ENGINE = MarkdownIt('commonmark', {'html': True}).enable('table')
VERSION = '20261002-book-1'
ASSET_VERSION = VERSION

# MathML is local, accessible and contains the source TeX as an annotation.
MATH = {
 r'D_{raw}=\frac{Q}{P\times N},\qquad D=\lceil D_{raw}\rceil': '<msub><mi>D</mi><mi>raw</mi></msub><mo>=</mo><mfrac><mi>Q</mi><mrow><mi>P</mi><mo>×</mo><mi>N</mi></mrow></mfrac><mo>,</mo><mspace width="2em"/><mi>D</mi><mo>=</mo><mo>⌈</mo><msub><mi>D</mi><mi>raw</mi></msub><mo>⌉</mo>',
 r'e=\sqrt{(8.03-8.00)^2+(8.04-8.00)^2}=0.05\;m': '<mi>e</mi><mo>=</mo><msqrt><mrow><msup><mrow><mo>(</mo><mn>8.03</mn><mo>−</mo><mn>8.00</mn><mo>)</mo></mrow><mn>2</mn></msup><mo>+</mo><msup><mrow><mo>(</mo><mn>8.04</mn><mo>−</mo><mn>8.00</mn><mo>)</mo></mrow><mn>2</mn></msup></mrow></msqrt><mo>=</mo><mn>0.05</mn><mspace width=".3em"/><mi mathvariant="normal">m</mi>',
 r'y_{r,c}=b+\sum_{u=0}^{k_h-1}\sum_{v=0}^{k_w-1}w_{u,v}\,x_{r+u,c+v}': '<msub><mi>y</mi><mrow><mi>r</mi><mo>,</mo><mi>c</mi></mrow></msub><mo>=</mo><mi>b</mi><mo>+</mo><munderover><mo>∑</mo><mrow><mi>u</mi><mo>=</mo><mn>0</mn></mrow><mrow><msub><mi>k</mi><mi>h</mi></msub><mo>−</mo><mn>1</mn></mrow></munderover><munderover><mo>∑</mo><mrow><mi>v</mi><mo>=</mo><mn>0</mn></mrow><mrow><msub><mi>k</mi><mi>w</mi></msub><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>w</mi><mrow><mi>u</mi><mo>,</mo><mi>v</mi></mrow></msub><mspace width=".2em"/><msub><mi>x</mi><mrow><mi>r</mi><mo>+</mo><mi>u</mi><mo>,</mo><mi>c</mi><mo>+</mo><mi>v</mi></mrow></msub>',
 r'\mathrm{Precision}=\frac{TP}{TP+FP}': '<mi mathvariant="normal">Precision</mi><mo>=</mo><mfrac><mi>TP</mi><mrow><mi>TP</mi><mo>+</mo><mi>FP</mi></mrow></mfrac>',
 r'\mathrm{Recall}=\frac{TP}{TP+FN}': '<mi mathvariant="normal">Recall</mi><mo>=</mo><mfrac><mi>TP</mi><mrow><mi>TP</mi><mo>+</mo><mi>FN</mi></mrow></mfrac>',
 r'\mathrm{NDVI}=\frac{\rho_{\mathrm{NIR}}-\rho_{\mathrm{Red}}}{\rho_{\mathrm{NIR}}+\rho_{\mathrm{Red}}}': '<mi mathvariant="normal">NDVI</mi><mo>=</mo><mfrac><mrow><msub><mi>ρ</mi><mi mathvariant="normal">NIR</mi></msub><mo>−</mo><msub><mi>ρ</mi><mi mathvariant="normal">Red</mi></msub></mrow><mrow><msub><mi>ρ</mi><mi mathvariant="normal">NIR</mi></msub><mo>+</mo><msub><mi>ρ</mi><mi mathvariant="normal">Red</mi></msub></mrow></mfrac>',
}

def read_json(name):
    return json.loads((SOURCE / name).read_text(encoding='utf-8'))

def plain(text):
    return BeautifulSoup(ENGINE.render(text), 'html.parser').get_text(' ', strip=True)

def clean_heading(text):
    return re.sub(r'\s*\{#[^}]+\}\s*$', '', text).strip()

def chapter_url(number):
    return BASE + f'chapter-{number:02d}/'

def math_block(match):
    tex = match[1].strip()
    if tex not in MATH:
        raise ValueError('Unreviewed display equation: ' + tex)
    return '<div class="equation" tabindex="0" role="region" aria-label="수식"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><semantics><mrow>' + MATH[tex] + '</mrow><annotation encoding="application/x-tex">' + escape(tex) + '</annotation></semantics></math></div>\n'

def inline_math(match):
    tex = match[1]
    safe = escape(tex).replace(r'\rho', 'ρ').replace(r'\times', '×')
    safe = re.sub(r'([a-z])_([a-z])', r'\1<sub>\2</sub>', safe)
    if '\\' in safe:
        raise ValueError('Unreviewed inline equation: ' + tex)
    return '<span class="inline-math">' + safe + '</span>'

def resolve_link(href, number):
    if href.startswith(('https://', 'http://', 'mailto:')):
        return href
    if href.startswith('#'):
        if href.startswith('#sec-ch'):
            target = int(re.match(r'#sec-ch(\d+)', href)[1])
            return ('' if target == number else chapter_url(target)) + href
        if href.startswith('#ref-') or href == '#refs':
            return BASE + 'references/' + href
        return href
    if 'manuscript/ko/index.md' in href:
        return BASE + '#chapters'
    m = re.search(r'manuscript/ko/ch(\d+)(?:/([0-9]+)[^/]*|\.md)$', href)
    if m:
        return chapter_url(int(m[1])) + (f'#unit-{int(m[2]):02d}' if m[2] else '')
    return None

def render(text, number, figures):
    heading_ids = []
    def heading_line(match):
        level, title = match[1], match[2]
        custom = re.search(r'\s*\{#([^\s}]+)[^}]*\}\s*$', title)
        title = clean_heading(title)
        unit = re.match(r'(\d+)단위', title)
        ident = custom[1] if custom else (f'unit-{int(unit[1]):02d}' if unit and len(level) == 2 else f'section-{len(heading_ids)+1:03d}')
        heading_ids.append(ident)
        return level + ' ' + title
    text = re.sub(r'^(#{1,6}) (.+)$', heading_line, text, flags=re.M)
    text = re.sub(r'\[([^\]\n]+)\]\{\.nocase\}', r'\1', text)
    text = re.sub(r'^:{3,}\s+\{#([^\s}]+)[^}]*\}\s*$', lambda m: f'<div id="{escape(m[1])}" class="reference-entry">\n', text, flags=re.M)
    text = re.sub(r'^:{3,}\s*$', '</div>\n', text, flags=re.M)
    def image(match):
        key = Path(match[2]).stem
        if key not in figures:
            raise ValueError('Missing figure: ' + key)
        return f'\n<figure data-book-figure="{key}"></figure>\n'
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)(?:\{[^}]*\})?', image, text)
    text = re.sub(r'\$\$([\s\S]*?)\$\$', math_block, text)
    text = re.sub(r'\$([^$\n]+)\$', inline_math, text)
    tokens = ENGINE.parse(text)
    pointer = 0
    toc = []
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            token.attrSet('id', heading_ids[pointer]); pointer += 1
            if token.tag in ('h2', 'h3'):
                toc.append({'id': token.attrGet('id'), 'title': tokens[i+1].content, 'level': int(token.tag[1])})
    soup = BeautifulSoup(ENGINE.renderer.render(tokens, ENGINE.options, {}), 'html.parser')
    for element in soup.find_all(['script', 'style', 'iframe']):
        element.decompose()
    for link in soup.find_all('a', href=True):
        href = resolve_link(link['href'], number)
        if href is None:
            link.name = 'span'
            link['class'] = 'unavailable-source'
            link['title'] = '원고에 참조된 별도 파일 · 제공된 두 원고 파일에 포함되지 않아 웹판에서 열 수 없습니다.'
            link['data-source-path'] = link['href']
            del link['href']
        else:
            link['href'] = href
            if href.startswith(('http:', 'https:')):
                link['rel'] = 'noopener noreferrer'
    for table in list(soup.find_all('table')):
        wrapper = soup.new_tag('div', attrs={'class':'table-scroll','tabindex':'0','role':'region','aria-label':'표 · 화면보다 넓으면 가로로 스크롤하세요'})
        table.wrap(wrapper)
        for cell in table.select('thead th'):
            cell['scope'] = 'col'
    for code in soup.select('pre'):
        code['tabindex'] = '0'
    for holder in list(soup.select('figure[data-book-figure]')):
        key = holder['data-book-figure']; info = figures[key]
        holder['id'] = key
        holder['class'] = 'book-figure'
        image = soup.new_tag('img', src=BASE+'assets/figures/'+info['file'], alt=info['alt'], width=str(info['width']), height=str(info['height']), loading='lazy', decoding='async')
        holder.append(image)
        caption = soup.new_tag('figcaption')
        meta = soup.new_tag('div', attrs={'class':'figure-meta'})
        label = soup.new_tag('span'); label.string = f"원고 도판 {info['order']:02d} · PDF {info['pdf_page']}쪽"; meta.append(label)
        zoom = soup.new_tag('a', href=image['src'], attrs={'class':'figure-zoom','data-zoom':'','aria-label':f"도판 {info['order']} 크게 보기"}); zoom.string = '크게 보기 ↗'; meta.append(zoom)
        caption.append(meta)
        description = soup.new_tag('p'); description.string = info['alt']; caption.append(description); holder.append(caption)
    return str(soup), toc

def book_nav(chapters, current=None):
    parts = []
    for ch in chapters:
        active = ' aria-current="page"' if current == ch['number'] else ''
        parts.append(f'<a href="{chapter_url(ch["number"])}"{active}><span>{ch["number"]:02d}</span><span>{escape(ch["title"])}</span></a>')
    return ''.join(parts)

def page(title, main, chapters, current=None, toc=None, route=''):
    local = ''.join(f'<a class="level-{x["level"]}" href="#{x["id"]}">{escape(x["title"])}</a>' for x in (toc or []))
    current_nav = f'<div class="toc-heading">이 장의 목차</div><nav class="unit-nav" aria-label="이 장의 목차">{local}</nav>' if local else ''
    entire = book_nav(chapters, current)
    sidebar = f'<aside class="book-sidebar">{current_nav}<details class="all-chapters" {"" if local else "open"}><summary>전체 15장</summary><nav aria-label="책 전체 목차">{entire}</nav></details><a class="sidebar-meta" href="{BASE}references/">참고문헌 ↗</a><a class="sidebar-meta" href="{BASE}edition/">원고와 웹판 안내 ↗</a></aside>'
    reader_class = ' is-reading' if current else ''
    reading_tools = '<div class="type-tools" role="group" aria-label="본문 글자 크기"><button type="button" data-size="-1" aria-label="본문 글자 작게">A−</button><button type="button" data-size="1" aria-label="본문 글자 크게">A+</button></div>' if current else ''
    return f'''<!doctype html>
<html lang="ko" data-dla="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="theme-color" content="#f5f6f2"><meta name="description" content="디지털 조경학 · Digital Landscape Architecture. 관측과 분석에서 설계·시공·관리까지. 저자 원고의 15장과 도판을 읽는 출간 준비 웹판."><title>{escape(title)} | 디지털 조경학 · SPATIALFLARE</title><link rel="canonical" href="https://navicoby.github.io{BASE+route}"><link rel="icon" href="/assets/spatialflare-logo.png"><link rel="stylesheet" href="{BASE}book.css?v={ASSET_VERSION}"><script defer src="{BASE}book.js?v={ASSET_VERSION}"></script></head><body>
<main class="dla-page{reader_class}" id="book-top"><a class="skip-link" href="#book-content">본문으로 건너뛰기</a><div class="book-toolbar"><div class="book-wrap toolbar-inner"><a class="book-brand" href="{BASE}">디지털 조경학<span>Digital Landscape Architecture</span></a><div class="toolbar-actions">{reading_tools}<button class="search-open" type="button">검색 <span aria-hidden="true">⌕</span></button><details class="mobile-toc"><summary>목차</summary><div class="mobile-toc-panel">{current_nav}<div class="toc-heading">전체 15장</div><nav aria-label="모바일 책 전체 목차">{entire}</nav><a class="sidebar-meta" href="{BASE}references/">참고문헌</a><a class="sidebar-meta" href="{BASE}edition/">원고와 웹판 안내</a></div></details></div></div><div class="reading-progress" aria-hidden="true"></div></div>
<div class="book-wrap book-layout">{sidebar}<div id="book-content" tabindex="-1">{main}</div></div><div class="book-wrap book-colophon"><span>© 2026 김수영 · 출간 준비 원고</span><div><a href="{BASE}edition/">판본 안내</a><a href="/#literature">SPATIALFLARE 자료실 ↗</a></div></div>
<dialog id="book-search" aria-labelledby="search-title"><div class="dialog-bar"><h2 id="search-title">책 안에서 찾기</h2><button type="button" data-close="book-search" aria-label="검색 닫기">닫기 ×</button></div><label class="search-label" for="search-query">본문·단위 제목·보완 설명 검색</label><input type="search" id="search-query" placeholder="예: 관측, IFC, 좌표, 미대응" autocomplete="off"><p id="search-status" role="status">검색어를 입력하세요.</p><ol id="search-results"></ol></dialog>
<dialog id="figure-viewer" aria-label="도판 크게 보기"><div class="dialog-bar"><span id="figure-label">원고 도판</span><button type="button" data-close="figure-viewer" aria-label="도판 닫기">닫기 ×</button></div><div class="figure-full"><img alt="" id="large-figure"></div><p id="figure-description"></p><a id="figure-file" target="_blank" rel="noopener">이미지 원본 열기 ↗</a></dialog>
<noscript><div class="book-wrap no-script">본문·목차·도판은 JavaScript 없이 읽을 수 있습니다. 검색과 글자 크기 조절에는 JavaScript가 필요합니다.</div></noscript></main></body></html>'''

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def register_home(path):
    text = path.read_text(encoding='utf-8')
    if 'href="'+BASE+'"' in text or 'href='+BASE in text:
        print('Book already registered on homepage.'); return
    pattern = r'(<section\b[^>]*\bid=(?:"literature"|\'literature\'|literature)(?=[\s>])[^>]*>.*?<div\b[^>]*\bclass=(?:"entries"|\'entries\'|entries)(?=[\s>])[^>]*>)'
    entry = f'<a class="entry" href="{BASE}"><span class="entry-name">Digital Landscape Architecture — 디지털 조경학</span><span class="tag">Book / Landscape</span></a>'
    result, count = re.subn(pattern, lambda m:m[1]+entry, text, count=1, flags=re.S|re.I)
    if count != 1:
        raise ValueError('Homepage Literature section was not found; existing homepage was not changed.')
    write(path, result)
    print('Registered Digital Landscape Architecture in Literature.')

def build():
    manuscript = (SOURCE/'manuscript.md').read_text(encoding='utf-8')
    meta = read_json('source-manifest.json')
    if hashlib.sha256(manuscript.encode()).hexdigest() != meta['markdown_sha256']:
        raise ValueError('Manuscript snapshot changed. Review the edition manifest before publication.')
    figure_list = read_json('figures.json')
    figures = {Path(f['file']).stem:dict(f,order=i+1) for i,f in enumerate(figure_list)}
    assert len(figures) == 50
    for f in figures.values():
        if not (OUT/'assets/figures'/f['file']).is_file():
            raise FileNotFoundError(f['file'])
    review = read_json('review-pages.json')
    starts = [(int(re.match(r'(\d+)장',title)[1]),page) for level,title,page in review['toc'] if level==1 and re.match(r'\d+장',title)]
    reference_page = next(p for level,title,p in review['toc'] if title.startswith('참고문헌'))
    additions = read_json('supplements.json')
    # Confirm each transcribed supplement still belongs to the supplied PDF edition.
    norm = lambda s:re.sub(r'[^0-9a-z가-힣]','',unicodedata.normalize('NFKC',s).lower())
    for extra in additions:
        source_text=''.join(review['pages'][n-1]['text'] for n in extra['pages'])
        if norm(extra['title']) not in norm(source_text):
            raise ValueError('Supplement heading not found in the PDF: '+extra['title'])
    hits=list(re.finditer(r'^# (\d+)장\.\s*(.+)$',manuscript,re.M))
    assert len(hits)==15
    reference_start=manuscript.index('# 참고문헌')
    chapters=[]
    for i,match in enumerate(hits):
        number=int(match[1]); title=clean_heading(match[2])
        raw=manuscript[match.end():hits[i+1].start() if i+1<len(hits) else reference_start].strip()
        units=len(re.findall(r'^## \d+단위\.',raw,re.M))
        chapters.append(dict(number=number,title=title,raw=raw,units=units,start=starts[i][1],end=(starts[i+1][1] if i+1<len(starts) else reference_page)-1))
    assert sum(ch['units'] for ch in chapters)==63
    rendered=[]; search=[]
    for ch in chapters:
        raw=ch['raw']
        extra_map={}
        for extra in [x for x in additions if x['chapter']==ch['number']]:
            position=raw.find(extra['before'])
            if position<0:
                raise ValueError('Supplement insertion point missing: '+extra['before'])
            key=f'pdf-addition-{ch["number"]:02d}'
            extra_map[key]=extra
            raw=raw[:position]+f'<div data-addition="{key}"></div>\n\n'+raw[position:]
        body,toc=render(raw,ch['number'],figures)
        dom=BeautifulSoup(body,'html.parser')
        for holder in list(dom.select('[data-addition]')):
            key=holder['data-addition']; extra=extra_map[key]
            extra_html,_=render(extra['markdown'],ch['number'],figures)
            page_label='–'.join(map(str,extra['pages']))
            replacement=BeautifulSoup(f'<aside class="revision-addition" id="{key}" aria-label="PDF 검토보완본 추가 설명"><p class="revision-label">검토보완본 추가 설명 · PDF {page_label}쪽</p><h4>{escape(extra["title"])}</h4>{extra_html}</aside>','html.parser')
            holder.replace_with(replacement)
        body=str(dom)
        first_paragraph=next((p.get_text(' ',strip=True) for p in dom.select('p') if len(p.get_text())>90), '')
        ch['excerpt']=first_paragraph[:130]+('…' if len(first_paragraph)>130 else '')
        prev=chapters[ch['number']-2] if ch['number']>1 else None
        nxt=chapters[ch['number']] if ch['number']<15 else None
        prev_link=f'<a href="{chapter_url(prev["number"])}"><small>← 이전 장</small>{escape(prev["title"])}</a>' if prev else f'<a href="{BASE}"><small>← 책 소개</small>디지털 조경학</a>'
        next_link=f'<a href="{chapter_url(nxt["number"])}"><small>다음 장 →</small>{escape(nxt["title"])}</a>' if nxt else f'<a href="{BASE}references/"><small>다음 →</small>참고문헌</a>'
        intro=f'<div class="chapter-head" id="sec-ch{ch["number"]:02d}"><p class="eyebrow">CHAPTER {ch["number"]:02d} / 15</p><h1>{escape(ch["title"])}</h1><div class="chapter-meta"><span>{ch["units"]}개 집필 단위</span><span>PDF {ch["start"]}–{ch["end"]}쪽</span><a href="{BASE}edition/">출간 준비 웹판</a></div></div>'
        notice='<p class="chapter-notice">저자 Markdown 원고를 바탕으로 한 웹판입니다. 2026-09-14 PDF에서 보강된 설명은 별도로 표시했습니다.</p>'
        local_notice='<div class="source-warning"><b>별도 실행자료 안내</b><p>원고의 점선 밑줄 파일명은 제공된 두 원고 파일에 포함되지 않은 실행자료를 가리킵니다. 본문에 적힌 계산·실험의 실행 여부는 원고의 설명을 따르며, 웹페이지 제작 과정에서 새로 실행했다고 표시하지 않습니다.</p></div>' if dom.select('.unavailable-source') else ''
        content=intro+notice+f'<article class="book-prose" id="reading">{body}</article>'+local_notice+f'<nav class="chapter-pagination" aria-label="이전 장과 다음 장">{prev_link}{next_link}</nav>'
        route=f'chapter-{ch["number"]:02d}/'
        write(OUT/route/'index.html',page(ch['title'],content,chapters,ch['number'],toc,route))
        rendered.append((ch,dom))
        # Search entries follow the original 63 writing units, not artificial summaries.
        current=None
        for element in dom.children:
            if getattr(element,'name',None)=='h2':
                if current: search.append(current)
                current=dict(chapter=ch['number'],chapter_title=ch['title'],title=element.get_text(' ',strip=True),url=chapter_url(ch['number'])+'#'+element['id'],text='')
            elif current and getattr(element,'get_text',None):
                current['text']+=' '+element.get_text(' ',strip=True)
        if current:search.append(current)
    assert len(search)==63
    cards=''.join(f'<article class="chapter-card"><a class="chapter-row" href="{chapter_url(ch["number"])}"><span class="chapter-index">{ch["number"]:02d}</span><div><h3>{escape(ch["title"])}</h3><p>{escape(ch["excerpt"])}</p><span class="row-meta">{ch["units"]}개 단위 · PDF {ch["start"]}–{ch["end"]}쪽</span></div><span class="row-arrow" aria-hidden="true">↗</span></a></article>' for ch in chapters)
    home=f'''<section class="book-hero"><p class="eyebrow">AUTHOR’S MANUSCRIPT / WEB EDITION</p><p class="english-title">Digital Landscape<br><em>Architecture.</em></p><h1>디지털 조경학</h1><p class="book-subtitle">관측과 분석에서 설계·시공·관리까지</p><p class="hero-description">같은 조경공간을 서로 다른 기술로 읽고,<br>관측·계산·판단의 근거를 이어갑니다.</p><div class="hero-byline">김수영 지음 <span>·</span> 출간 준비 원고</div><div class="book-actions"><a class="button solid" href="{chapter_url(1)}">1장부터 읽기 <span aria-hidden="true">↗</span></a><a class="button" href="#chapters">전체 목차 ↓</a></div><dl class="book-stats"><div><dt>CHAPTERS</dt><dd>15<span>장</span></dd></div><div><dt>WRITING UNITS</dt><dd>63<span>단위</span></dd></div><div><dt>FIGURES</dt><dd>50<span>도판</span></dd></div></dl></section><section class="book-introduction"><p class="eyebrow">ABOUT THIS BOOK</p><h2>도구의 이름보다,<br>조경의 질문에서 시작합니다.</h2><p>이 책은 현장에 무엇이 있는지 관측하고, 자료를 공간분석과 설계 검토에 사용하며, 선택한 설계를 시공·유지관리의 기록으로 이어가는 과정을 다룹니다. GIS와 BIM·IFC, 영상과 드론, 공간표현과 그래프, AI와 시뮬레이션을 같은 공원의 질문 안에서 연결합니다.</p><p>공통 사례는 <strong>40×30m 가상 공원 D03</strong>입니다. 실측·설계 가정·계산 결과·예측을 구별하고, 실행된 교육용 계산과 미실행 실험을 나누어 읽습니다.</p><p class="source-caption">원고 1장 「책의 흐름과 읽는 방법」을 바탕으로 구성한 소개입니다.</p></section><section id="chapters" class="chapter-catalogue"><div class="catalogue-heading"><div><p class="eyebrow">CONTENTS</p><h2>전체 목차</h2></div><a href="{BASE}figures/">도판 모아보기 ↗</a></div>{cards}<a class="references-row" href="{BASE}references/">참고문헌 <span>→</span></a></section><section class="edition-teaser"><p class="eyebrow">A BOOK IN PROGRESS</p><h2>원고를 읽는 웹판,<br>출판을 준비하는 기록.</h2><p>2026년 9월 14일 검토보완 PDF와 저자 Markdown 원고를 함께 사용했습니다. 원고의 장·단위 구성과 본문을 유지하고, 판본 간 추가 설명은 구분하여 담았습니다. 최종 탈고·출판 교정을 마친 책으로 표시하지 않습니다.</p><a class="text-link" href="{BASE}edition/">원고·도판·웹판의 관계와 편집 기록 ↗</a></section>'''
    write(OUT/'index.html',page('Digital Landscape Architecture',home,chapters))
    reference_raw=manuscript[reference_start:].split('\n',1)[1]
    reference_html,_=render(reference_raw,None,figures)
    refs='<div class="chapter-head"><p class="eyebrow">REFERENCES</p><h1>참고문헌</h1><p>제공된 원고의 참고문헌 목록입니다. 본문의 직접 출처 링크도 각 장에 유지했습니다.</p></div><article class="book-prose reference-prose">'+reference_html+'</article>'
    write(OUT/'references/index.html',page('참고문헌',refs,chapters,route='references/'))
    extra_items=''.join(f'<li><a href="{chapter_url(x["chapter"])}#pdf-addition-{x["chapter"]:02d}"><span>{x["chapter"]:02d}장</span> {escape(x["title"])} <small>PDF {"–".join(map(str,x["pages"]))}쪽</small></a></li>' for x in additions)
    edition=f'''<div class="chapter-head"><p class="eyebrow">EDITION & EDITORIAL RECORD</p><h1>원고와 웹판 안내</h1><p>저자 원고의 구조와 근거를 남기면서 웹에서 읽을 수 있도록 옮겼습니다.</p></div><article class="book-prose"><h2>두 원고의 역할</h2><p><strong>『디지털 조경학_전권 검토보완본_2026-09-14.pdf』</strong>는 189쪽의 검토·보완본입니다. 부제는 ‘관측과 분석에서 설계·시공·관리까지’이며, 15장·63개 집필 단위를 담고 있습니다. PDF에 있는 도판을 웹용 이미지로 옮겼습니다.</p><p><strong>『디지털조경학.md』</strong>는 웹 본문의 바탕입니다. 장과 단위, 문단, 표, 수식, 코드, 출처의 순서를 유지했습니다. 6–14장에서 PDF에 추가된 아래 설명은 원래 읽기 위치에 구분해서 삽입했습니다. 웹판에서 새로 작성한 본문인 것처럼 섞지 않았습니다.</p><h2>검토보완본에서 반영한 추가 설명</h2><ul class="edition-list">{extra_items}</ul><h2>웹 표시를 위해 바꾼 것</h2><p>장별 주소와 내부 목차를 만들고, Pandoc 편집용 속성을 화면에서 정리했습니다. 수식 여섯 개는 원문의 기호를 유지한 MathML로 표시합니다. 도판 50개는 PDF의 이미지에서 무손실 WebP로 변환했으며, 그림 설명과 크게 보기 기능을 붙였습니다. 표와 코드는 작은 화면에서 내용이 잘리지 않도록 가로 스크롤 영역에 둡니다.</p><h2>별도 파일을 만들어낸 것은 아닙니다</h2><p>원고가 참조하는 데이터·실행 코드·검토 기록 중 제공되지 않은 파일은 다운로드 링크로 만들지 않았습니다. 해당 파일명은 본문에 남기고 점선 밑줄로 표시했습니다. 웹 제작을 위해 새로운 현장 실험을 수행하거나 원고의 수치·성능 주장을 재검증한 것으로 표시하지 않습니다.</p><h2>출간 준비 상태</h2><p>두 파일은 저자 검토와 전체 탈고, 출판 편집을 앞둔 원고입니다. 이 웹판은 원고를 읽고 개정해 나가는 공간이며, 완성 출판물이나 동료평가를 거친 교재라는 표시를 하지 않습니다. 날짜가 있는 기술·법규·도구 설명은 해당 원고 판본의 서술입니다.</p><h2>권리와 원본</h2><p>김수영 저자의 요청에 따라 제공된 원고와 도판을 게시했습니다. 본문에서 인용하거나 참조한 외부 자료는 각각 표시된 출처를 따릅니다. 구글드라이브의 원본 파일과 공유 설정은 변경하지 않았습니다.</p><h2>편집 이력</h2><p>웹판 1 · 2026-10-02. 최초 웹 전환. 15장, 63단위, 참고문헌, 50도판, PDF 보완 설명 9개를 구성했습니다.</p><details class="source-hashes"><summary>원본 대조용 SHA-256</summary><p>Markdown<br><code>{meta['markdown_sha256']}</code></p><p>PDF<br><code>{meta['pdf_sha256']}</code></p></details></article>'''
    write(OUT/'edition/index.html',page('원고와 웹판 안내',edition,chapters,route='edition/'))
    gallery=''.join(f'<article class="gallery-item"><a href="{chapter_url(int(re.search(r"fig-ch(\d+)",key)[1]))}#{key}"><img src="{BASE}assets/figures/{f["file"]}" width="{f["width"]}" height="{f["height"]}" alt="{escape(f["alt"])}" loading="lazy"><span>도판 {f["order"]:02d} · PDF {f["pdf_page"]}쪽</span><p>{escape(f["alt"])}</p></a></article>' for key,f in figures.items())
    write(OUT/'figures/index.html',page('도판 모아보기','<div class="chapter-head"><p class="eyebrow">FIGURE INDEX / 50</p><h1>도판 모아보기</h1><p>도판을 선택하면 해당 장의 설명으로 이동합니다. 그림은 본문의 조건·가정과 함께 읽습니다.</p></div><div class="figure-gallery">'+gallery+'</div>',chapters,route='figures/'))
    write(OUT/'search-index.json',json.dumps(search,ensure_ascii=False,separators=(',',':')))
    manifest=dict(version=VERSION,chapters=15,units=63,figures=50,supplements=9,pages=19,source_edition=meta['source_edition'],source_sha256=meta['markdown_sha256'],chapter_titles=[ch['title'] for ch in chapters])
    write(OUT/'page-manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    validate()
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

def validate():
    # Files resolve against the output root, not untrusted source paths.
    for file in OUT.rglob('index.html'):
        soup=BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser')
        ids=[x['id'] for x in soup.select('[id]')]
        if len(ids)!=len(set(ids)):
            raise ValueError('Duplicate id in '+str(file))
        if soup.select('textarea'):
            raise ValueError('This book must not contain a notebook form.')
        for link in soup.select('a[href]'):
            href=unquote(link['href']); parsed=urlparse(href)
            if href.startswith('#'):
                if parsed.fragment not in ids:
                    raise ValueError('Broken same-page anchor: '+href+' in '+str(file))
            elif parsed.path.startswith(BASE):
                dest=OUT/parsed.path[len(BASE):]
                if parsed.path.endswith('/'):dest=dest/'index.html'
                if not dest.exists():
                    raise ValueError('Broken book link: '+href)
                if parsed.fragment and dest.suffix=='.html':
                    target=BeautifulSoup(dest.read_text(encoding='utf-8'),'html.parser')
                    if target.find(id=parsed.fragment) is None:
                        raise ValueError('Broken cross-chapter anchor: '+href)
        for image in soup.select('img[src]'):
            if image['src'].startswith(BASE):
                assert (OUT/image['src'][len(BASE):]).exists(),image['src']

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--register-home',type=Path)
    args=parser.parse_args()
    if args.register_home:register_home(args.register_home)
    else:build()
