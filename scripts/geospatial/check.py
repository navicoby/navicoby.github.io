"""Check local book links, anchors and publication assets after Hugo build."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import argparse


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
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(pages)} book pages, local links, anchors and image descriptions")


if __name__ == "__main__":
    main()
