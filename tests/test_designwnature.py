"""Independent static guide checks; no external network or original book needed."""
from pathlib import Path
from html.parser import HTMLParser
import importlib.util
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('chrome', ROOT/'scripts/apply_site_chrome.py')
chrome = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chrome)
class Elements(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.targets=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='a' and a.get('href','').startswith('#'): self.targets.append(a['href'][1:])
class GuideTests(unittest.TestCase):
    def test_anchors(self):
        p=Elements(); p.feed((ROOT/'static/designwnature/index.html').read_text())
        self.assertEqual(len(p.ids),len(set(p.ids)))
        self.assertTrue(set(p.targets)<=set(p.ids))
    def test_home_registration(self):
        for quote in ['"',"'",'']:
            page=f'<section class={quote}section index{quote} id={quote}literature{quote}><div class={quote}entries{quote}><a href="/existing/">Existing</a></div></section>'
            added=chrome.add_designwnature_entry(page)
            self.assertIn('href="/designwnature/"',added)
            self.assertIn('href="/existing/"',added)
            self.assertEqual(added,chrome.add_designwnature_entry(added))
    def test_no_book_assets(self):
        for p in (ROOT/'static/designwnature').rglob('*'):
            if p.is_file(): self.assertIn(p.suffix,{'.html','.css','.js'})
    def test_local_tools_preserved(self):
        page=(ROOT/'static/designwnature/index.html').read_text()
        built=chrome.apply(page,'<spatialflare-header></spatialflare-header>','<spatialflare-footer></spatialflare-footer>')
        self.assertIn('id="dw-water"',built)
        self.assertIn('id="dw-note-form"',built)
        self.assertIn('class="dw-mobile-menu"',built)
        self.assertEqual(built.count('id="dw-map"'),1)
        self.assertNotIn('sf-page-menu-panel',built)
if __name__=='__main__': unittest.main()
