"""Source and navigation regression tests for the author book build."""
from pathlib import Path
import importlib.util,json,re,unicodedata,unittest,hashlib
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'static/digital-landscape-architecture'
SOURCE=ROOT/'books/digital-landscape-architecture'
SPEC=importlib.util.spec_from_file_location('book_build',ROOT/'scripts/build_digital_landscape.py')
BUILD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(BUILD)
NORM=lambda x:re.sub(r'[^0-9a-z가-힣]','',unicodedata.normalize('NFKC',x).lower())
class BookTests(unittest.TestCase):
    def test_manifest_and_sources(self):
        manifest=json.loads((OUT/'page-manifest.json').read_text())
        self.assertEqual((manifest['chapters'],manifest['units'],manifest['figures'],manifest['supplements']),(15,63,50,9))
        source=json.loads((SOURCE/'source-manifest.json').read_text())
        self.assertEqual(hashlib.sha256((SOURCE/'manuscript.md').read_bytes()).hexdigest(),source['markdown_sha256'])
        self.assertEqual(len(list(OUT.rglob('index.html'))),19)
    def test_links_and_forms(self):
        BUILD.validate()
        for p in OUT.rglob('index.html'):
            text=p.read_text()
            self.assertNotIn('dw-notebook',text)
            self.assertNotIn('<textarea',text)
            self.assertNotIn('data-dw-theme',text)
    def test_original_units_and_figures(self):
        md=(SOURCE/'manuscript.md').read_text()
        originals=re.findall(r'^## (\d+단위\..+)$',md,re.M)
        actual=[];figures=0;equations=0
        for p in sorted(OUT.glob('chapter-*/index.html')):
            soup=BeautifulSoup(p.read_text(),'html.parser')
            actual.extend(h.get_text(' ',strip=True) for h in soup.select('#reading > h2'))
            figures+=len(soup.select('#reading .book-figure'))
            equations+=len(soup.select('#reading math'))
        self.assertEqual([BUILD.clean_heading(t) for t in originals],actual)
        self.assertEqual(figures,50);self.assertEqual(equations,6)
        self.assertEqual(len(json.loads((OUT/'search-index.json').read_text())),63)
    def test_pdf_supplements_are_source_text(self):
        review=json.loads((SOURCE/'review-pages.json').read_text())
        for entry in json.loads((SOURCE/'supplements.json').read_text()):
            # Remove the repeated four-line page header before joining paragraphs.
            original=NORM(''.join('\n'.join(review['pages'][n-1]['text'].splitlines()[4:]) for n in entry['pages']))
            soup=BeautifulSoup(BUILD.ENGINE.render(entry['markdown']),'html.parser')
            self.assertIn(NORM(entry['title']),original)
            for piece in soup.find_all(['p','tr']):
                text=NORM(piece.get_text(' ',strip=True))
                self.assertIn(text,original,msg=f"Chapter {entry['chapter']}: {piece.get_text()[:70]}")
    def test_home_registration(self):
        import tempfile
        for quote in ['',"'",'"']:
            with tempfile.TemporaryDirectory() as d:
                p=Path(d)/'index.html'
                source=f'<section id={quote}literature{quote}><div class={quote}entries{quote}><a href="/existing/">Existing</a></div></section>'
                p.write_text(source)
                BUILD.register_home(p);first=p.read_text();BUILD.register_home(p)
                self.assertEqual(p.read_text(),first)
                self.assertIn('href="/existing/"',first)
                self.assertIn('href="/digital-landscape-architecture/"',first)
if __name__=='__main__':unittest.main()
