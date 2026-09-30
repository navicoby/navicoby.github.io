"""Regression checks for script-dependent controls and protected article content."""
import unittest
from apply_site_chrome import apply

class SiteChromeTests(unittest.TestCase):
    def test_controls_exist_before_page_bootstrap(self):
        page = '<html><head></head><body><header><div id="progressBar"></div><button id="themeToggle">Theme</button></header><main>Article</main><script src="app.js"></script></body></html>'
        result = apply(page, '<spatialflare-header></spatialflare-header>', '<spatialflare-footer></spatialflare-footer>')
        bootstrap = result.index('<script src="app.js">')
        self.assertLess(result.index('id="progressBar"'), bootstrap)
        self.assertLess(result.index('id="themeToggle"'), bootstrap)
        self.assertIn('class="sf-page-menu"', result)

    def test_article_header_and_footer_are_preserved(self):
        article = '<main><article><header><h1>Research</h1></header><p>Body</p><footer>Scientific caveat</footer></article></main>'
        page = '<html><head></head><body><header>Site</header>' + article + '<footer>Site footer</footer></body></html>'
        self.assertIn(article, apply(page, '<spatialflare-header></spatialflare-header>', '<spatialflare-footer></spatialflare-footer>'))

    def test_repeated_processing_does_not_duplicate_controls(self):
        page = '<html><head></head><body><header><nav><a href="tools.html">Tools</a></nav></header><main>Body</main></body></html>'
        result = apply(page, '<spatialflare-header></spatialflare-header>', '<spatialflare-footer></spatialflare-footer>')
        self.assertEqual(result, apply(result, 'unused', 'unused'))

if __name__ == '__main__':
    unittest.main()
