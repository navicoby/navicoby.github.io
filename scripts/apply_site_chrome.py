"""Apply shared site navigation to Hugo output without altering article content."""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import re

class Regions(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text = text
        self.lines = [0]
        self.lines.extend(m.end() for m in re.finditer('\n', text))
        self.stack = []
        self.regions = []
        self.body_start = self.body_end = self.head_end = None

    def position_offset(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        pos = self.position_offset()
        end = pos + len(self.get_starttag_text())
        if tag == 'body':
            self.body_start = end
        protected = any(t in ('main', 'article', 'section', 'aside', 'figure', 'template') for t, *_ in self.stack)
        candidate = tag in ('header', 'footer') and not protected
        if tag not in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'):
            self.stack.append((tag, pos, end, candidate, attrs))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pos = self.position_offset()
        if tag == 'body': self.body_end = pos
        if tag == 'head': self.head_end = pos
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                _, start, inner, candidate, attrs = self.stack[i]
                if candidate:
                    self.regions.append((start, self.text.find('>', pos) + 1, tag, inner, pos, attrs))
                del self.stack[i:]
                break


def apply(text, header, footer, is_home=False):
    if '<spatialflare-header' in text:
        return text
    parser = Regions(text)
    parser.feed(text)
    if parser.body_start is None or parser.body_end is None or parser.head_end is None:
        return text
    edits = []
    page_controls = []
    for start, end, tag, inner, closing, attrs in parser.regions:
        replacement = ''
        if tag == 'header' and not is_home:
            content = text[inner:closing]
            # Retain the page's reading menus and tools, but remove its competing brand.
            content = re.sub(r'<a\b[^>]*class=["\'][^"\']*\b(?:brand|site-title)\b[^"\']*["\'][^>]*>.*?</a>', '', content, flags=re.S | re.I)
            content = re.sub(r'<div\b[^>]*class=["\']logo["\'][^>]*>.*?</div>', '', content, flags=re.S | re.I)
            if re.search(r'<(?:a|button|input|select)\b', content):
                opening = text[start:inner].replace('<header', '<div', 1)
                opening = re.sub(r'\sstyle=["\'][^"\']*["\']', '', opening)
                opening = opening[:-1] + ' data-sf-local-nav style="position:static;top:auto;width:100%;z-index:auto">'
                page_controls.append(opening + content + '</div>')
        edits.append((start, end, replacement))
    controls = ''
    if page_controls:
        controls = '<details class="sf-page-menu"><summary>페이지 메뉴</summary><div class="sf-page-menu-panel">' + ''.join(page_controls) + '</div></details>'
    edits.extend([
        # Existing inline scripts initialize these controls while parsing the page.
        # Keep their DOM before those scripts; CSS handles the bottom-right placement.
        (parser.body_start, parser.body_start, '\n' + header + '\n' + controls),
        (parser.body_end, parser.body_end, '\n' + footer + '\n'),
        (parser.head_end, parser.head_end, '<link rel="stylesheet" href="/assets/page-menu.css"><script defer src="/assets/site-chrome.js"></script>'),
    ])
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument('--public', type=Path, default=Path('public'))
    args = cli.parse_args()
    root = Path(__file__).resolve().parents[1]
    header = (root / 'scripts/site-chrome/header.html').read_text(encoding='utf-8')
    footer = (root / 'scripts/site-chrome/footer.html').read_text(encoding='utf-8')
    count = 0
    for path in args.public.rglob('*.html'):
        text = path.read_text(encoding='utf-8')
        # Hugo redirect documents do not represent content pages.
        if re.search(r'http-equiv=["\']?refresh', text, re.I): continue
        updated = apply(text, header, footer, path == args.public / 'index.html')
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            count += 1
    print(f'Applied shared header and footer to {count} pages.')

if __name__ == '__main__':
    main()
