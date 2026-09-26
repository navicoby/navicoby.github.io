"""Fail publication if a top-level static page loses its homepage link.

Uses the rendered homepage, so malformed templates and missing build output are
checked as well. Pages served outside this repository are left unchanged.
"""
import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        href = dict(attrs).get("href", "")
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            return
        path = unquote(url.path).lstrip("/")
        if path.endswith("index.html"):
            path = path[:-len("index.html")]
        self.paths.add(path.rstrip("/"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--public", type=Path, default=Path("public"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    homepage = args.public / "index.html"
    if not homepage.is_file():
        print(f"ERROR: Build the homepage first: {homepage}", file=sys.stderr)
        return 1
    links = Links()
    links.feed(homepage.read_text(encoding="utf-8"))
    entries = sorted((root / "static").glob("*/index.html"))
    errors = []
    for entry in entries:
        route = entry.parent.name
        if route not in links.paths:
            errors.append(f"Missing homepage link: /{route}/ (source: static/{route}/index.html)")
        if not (args.public / route / "index.html").is_file():
            errors.append(f"Missing published page: /{route}/index.html")
    if errors:
        print("\n".join("ERROR: " + error for error in errors), file=sys.stderr)
        return 1
    print(f"PASS: All {len(entries)} top-level static pages are linked from the homepage and included in the build.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
