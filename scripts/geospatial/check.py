"""Check local book links, anchors and publication assets after Hugo build."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import argparse
import html
import json
import re


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.errors = set(), [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append("duplicate id: " + attrs["id"])
            self.ids.add(attrs["id"])
        for key in ("href", "src", "data-map-src"):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == "img" and not attrs.get("alt"):
            self.errors.append("image missing alt")
        if tag == "iframe" and not attrs.get("title"):
            self.errors.append("iframe missing title")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public", type=Path, default=Path("public"))
    root = parser.parse_args().public.resolve()
    book = root / "python-geospatial"
    errors, cache = [], {}
    def parse(path):
        if path not in cache:
            doc = Document()
            doc.feed(path.read_text(encoding="utf-8"))
            cache[path] = doc
        return cache[path]
    pages = [p for p in book.rglob("*.html") if "maps" not in p.parts]
    if not pages:
        raise SystemExit("No book HTML: build the book and Hugo first")
    for page in pages:
        doc = parse(page)
        errors.extend(f"{page.name}: {e}" for e in doc.errors)
        for href in doc.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            target = ((root / path.lstrip("/")) if path.startswith("/")
                      else (page.parent / path if path else page)).resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{page.name}: missing {href}")
            elif url.fragment and target.suffix == ".html":
                if unquote(url.fragment) not in parse(target).ids:
                    errors.append(f"{page.name}: missing anchor {href}")
    # A single curriculum must describe the sidebar, part landings and chapter bodies.
    source_root = Path(__file__).resolve().parents[2]
    parts = json.loads((source_root / 'books/python-geospatial/curriculum.json').read_text(encoding='utf-8'))
    chapters = [c for p in parts for c in p['chapters']]
    for page in pages:
        content = page.read_text(encoding='utf-8')
        side = content.split('<aside', 1)[1].split('</aside>', 1)[0]
        for part in parts:
            expected_part = f"PART {part['number']:02d} · {part['title']}"
            if html.escape(expected_part) not in side:
                errors.append(f'{page.name}: sidebar missing {expected_part}')
            for chapter in part['chapters']:
                expected = f"{chapter['id']:02d} · {chapter['title']}"
                if html.escape(expected) not in side:
                    errors.append(f'{page.name}: sidebar missing {expected}')
                if page.stem == chapter['slug']:
                    if f'<h1>{html.escape(expected)}</h1>' not in content:
                        errors.append(f'{page.name}: chapter heading disagrees with curriculum')
                    match = re.search(r'<details class="nav-part" open>(.*?)</details>', side, re.S)
                    if not match or html.escape(expected_part) not in match[1]:
                        errors.append(f'{page.name}: current part is not expanded')
                    if f'href="../chapters/{chapter["slug"]}.html" aria-current="page"' not in side:
                        errors.append(f'{page.name}: missing current chapter marker')
                    index = chapters.index(chapter)
                    for offset, relation in [(-1, 'prev'), (1, 'next')]:
                        other = index + offset
                        if 0 <= other < len(chapters):
                            target = chapters[other]['slug']
                            if f'rel="{relation}" href="../chapters/{target}.html"' not in content:
                                errors.append(f'{page.name}: incorrect {relation} chapter')
    expected_count = len(parts) + len(chapters) + len(json.loads((source_root / 'books/python-geospatial/pages.json').read_text(encoding='utf-8')))
    if len(pages) != expected_count:
        errors.append(f'Expected {expected_count} pages, found {len(pages)}')
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(pages)} book pages, local links, anchors and image descriptions")


if __name__ == "__main__":
    main()
