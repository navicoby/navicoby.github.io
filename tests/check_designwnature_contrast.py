"""Browser regression for the standalone guide + shared chrome CSS cascade.

Run: python tests/check_designwnature_contrast.py
Requires Playwright and Chromium (PLAYWRIGHT_CHROMIUM_EXECUTABLE may override).
Uses representative components with the real repository stylesheets, in both
load orders. This is a color/theme regression, not a complete accessibility audit.
"""
from pathlib import Path
import importlib.util
import json
import os
import re
import shutil
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('site_chrome', ROOT/'scripts/apply_site_chrome.py')
CHROME = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHROME)
FIXTURE = '''<!doctype html><html lang="ko" data-dw-theme="dark"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="/designwnature/style.css"></head><body>
<main class="dw" id="dw-top"><div class="dw-bar"><div class="dw-wrap dw-bar-inner">
<a class="dw-bar-title" href="#dw-start"><span>with nature.</span>자연기반해법</a>
<div class="dw-controls"><button class="dw-button" id="theme-toggle">밝게</button>
<details class="dw-mobile-menu"><summary>목차</summary><nav><a href="#dw-start">01 · 맥하그에서 시작하기</a></nav></details>
</div></div></div><div class="dw-wrap"><section class="dw-hero">
<div class="dw-kicker">SPATIALFLARE / FIELD GUIDE</div><h1>Design<br><em>with</em> nature.</h1>
<p class="dw-subtitle">이안 맥하그의 『Design with Nature』에서 시작하는 자연기반해법</p>
<p class="dw-intro">땅을 바꾸기 전에, 그곳에서 일어나는 일을 읽습니다.</p>
<div class="dw-hero-actions"><a class="dw-button primary" href="#dw-start">처음부터 읽기 ↗</a><a class="dw-button" href="#dw-start">중첩지도 실험하기 ↓</a></div>
</section><section class="dw-section" id="dw-start"><div class="dw-section-heading"><span class="dw-number">01</span><h2>맥하그에서 시작하기</h2></div>
<span class="dw-tag book">원서의 논지</span><span class="dw-tag modern">현대 자료</span><span class="dw-tag editor">독립적인 해석</span>
<p class="dw-lead">자연을 설계의 배경으로 둘 것인가,<br>계획을 함께 결정하는 조건으로 읽을 것인가.</p>
<div class="dw-prose"><p>본문의 배경과 글자색을 함께 확인합니다. <a class="dw-inline-link" href="#source">출처</a></p><p class="dw-source" id="source">출처와 판본 안내</p></div>
<div class="dw-note"><strong>검토 안내</strong><p>읽기 모드가 바뀌어도 배경과 글자의 대비가 유지되어야 합니다.</p></div>
<p class="dw-small">보조 설명을 읽을 수 있는지도 확인합니다.</p>
<details open><summary>책과 함께 읽을 위치</summary><div>접힌 내용도 같은 배경과 글자색을 사용합니다.</div></details>
<div class="dw-lab"><label class="dw-slider">물 관련 검토 <output>45</output><input type="range" value="45"></label><div class="dw-readout"><b>선택 위치</b><br>가상 대상지의 값을 표시합니다.</div><div class="dw-formula">물 × w1 + 열 × w2</div></div>
<label class="dw-field"><span>대상지 검토노트</span><textarea placeholder="대상지에서 관찰한 내용을 적습니다.">입력한 노트</textarea></label>
</section></div></main></body></html>'''
HEADER = '''<spatialflare-header><template shadowrootmode="open"><style>
:host{display:block;background:#f5f6f2;color:#17201c;font:16px/1.5 Arial,sans-serif}
header{padding:22px 20px}a{color:inherit;text-decoration:none}
</style><header><a href="/">SPATIALFLARE</a></header></template></spatialflare-header>'''
SELECTORS = ['h1','h1 em','.dw-subtitle','.dw-intro','.dw-kicker','h2','.dw-number',
             '.dw-tag.book','.dw-tag.modern','.dw-tag.editor','.dw-lead','.dw-prose p',
             '.dw-inline-link','.dw-source','.dw-note p','.dw-note strong','.dw-small',
             '#dw-start summary','#dw-start details>div','.dw-bar-title','.dw-button',
             '.dw-button.primary','.dw-lab','.dw-slider','.dw-readout b','.dw-formula',
             '.dw-field>span','.dw-field textarea']
STYLE_JS = '''el => {
  const style=getComputedStyle(el); let node=el, background='';
  while(node) { const b=getComputedStyle(node).backgroundColor;
    if(b!=='rgba(0, 0, 0, 0)'&&b!=='transparent'){background=b;break;}
    node=node.parentElement;
  }
  return {color:style.color,background,font:style.fontSize};
}'''

def rgb(value):
    return [float(n) for n in re.findall(r'[\d.]+',value)[:3]]

def luminance(values):
    c=[v/255 for v in values]
    c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]

def contrast(pair):
    a,b=sorted([luminance(rgb(pair['color'])),luminance(rgb(pair['background']))])
    return (b+.05)/(a+.05)

def run():
    shared=(ROOT/'static/assets/page-menu.css').read_text(encoding='utf-8')
    local=(ROOT/'static/designwnature/style.css').read_text(encoding='utf-8')
    built=CHROME.apply(FIXTURE,HEADER,'')
    # A changed URL ensures existing clients do not keep the older common CSS.
    cache_versioned=bool(re.search(r'page-menu\.css\?v=[^"\s]+',built))
    executable=os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE') or shutil.which('chromium')
    options={'headless':True}
    if executable: options['executable_path']=executable
    reports=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(**options)
        for reverse in [False,True]:
            page=browser.new_page(viewport={'width':390,'height':844})
            markup=re.sub(r'<link[^>]*>|<script.*?</script>','',built,flags=re.S)
            sheets=[shared,local] if reverse else [local,shared]
            markup=markup.replace('</head>',''.join('<style>'+s+'</style>' for s in sheets)+'</head>')
            page.set_content(markup)
            for width in [360,390,430,768,1440]:
                page.set_viewport_size({'width':width,'height':900})
                for preference in ['light','dark']:
                    page.emulate_media(color_scheme=preference)
                    for theme in ['dark','light']:
                        page.evaluate('(theme)=>document.documentElement.dataset.dwTheme=theme',theme)
                        pairs={s:page.locator(s).first.evaluate(STYLE_JS) for s in SELECTORS}
                        if width<=760:
                            page.locator('.dw-mobile-menu').evaluate('(el)=>el.open=true')
                            pairs['mobile menu']=page.locator('.dw-mobile-menu nav a').evaluate(STYLE_JS)
                            page.locator('.dw-mobile-menu').evaluate('(el)=>el.open=false')
                        ratios={s:contrast(pair) for s,pair in pairs.items()}
                        failing={s:round(v,2) for s,v in ratios.items() if v<4.5}
                        main=page.locator('main').evaluate(STYLE_JS)
                        reports.append({'width':width,'system':preference,'theme':theme,'reversed_css':reverse,
                                        'main':main,'minimum':round(min(ratios.values()),2),'failures':failing})
                        assert not failing,reports[-1]
                        expected='rgb(17, 23, 19)' if theme=='dark' else 'rgb(242, 243, 236)'
                        assert main['background']==expected,main
                        assert page.locator('body').evaluate('(el)=>getComputedStyle(el).colorScheme')==theme
                        assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'),width
            # Check an unthemed page is unaffected by the scoped override.
            page.set_content('<html><head><style>'+shared+'</style></head><body><main>Regular site page</main></body></html>')
            assert page.locator('main').evaluate('(el)=>getComputedStyle(el).backgroundColor')=='rgb(245, 246, 242)'
            page.close()
        browser.close()
    assert cache_versioned,'Shared CSS URL needs a version to refresh previously cached styles.'
    print(json.dumps({'scenarios':len(reports),'minimum_text_contrast':min(r['minimum'] for r in reports),
                      'cache_versioned':cache_versioned,'results':reports},ensure_ascii=False,indent=2))

if __name__=='__main__':
    run()
