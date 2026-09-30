"""Build the geospatial book into Hugo's static directory; no network access."""
from pathlib import Path
import html
import json
import re
import shutil
from string import Template
import markdown
import yaml

ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "books/python-geospatial"
OUT = ROOT / "static/python-geospatial"
DOMAIN = (ROOT / "static/CNAME").read_text(encoding="utf-8").strip()
SITE_URL = "https://" + DOMAIN


def read_page(name):
    text = (BOOK / "pages" / name).read_text(encoding="utf-8")
    _, meta, body = text.split("---", 2)
    return yaml.safe_load(meta), body.strip()


def code_block(match):
    spec = match[1]
    name, _, region = spec.partition("#")
    path = (BOOK / "examples" / name).resolve()
    if not path.is_relative_to((BOOK / "examples").resolve()):
        raise ValueError("Example path must stay inside examples/")
    code = path.read_text(encoding="utf-8")
    if region:
        code = code.split(f"# start:{region}\n", 1)[1].split(f"# end:{region}", 1)[0]
    return "```python\n" + code.strip() + "\n```"


def build():
    names = json.loads((BOOK / "pages.json").read_text(encoding="utf-8"))
    pages = {name: read_page(name) for name in names}
    template = Template((BOOK / "templates/page.html").read_text(encoding="utf-8"))
    for name, (meta, source) in pages.items():
        target = OUT / Path(name).with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        prefix = "../" * (len(Path(name).parts)-1)
        nav = []
        for entry, (other, _) in pages.items():
            url = prefix + str(Path(entry).with_suffix(".html")).replace("\\", "/")
            current = ' aria-current="page"' if entry == name else ""
            nav.append(f'<a href="{url}"{current}>{html.escape(other["title"])}</a>')
        md = markdown.Markdown(extensions=["fenced_code", "tables", "toc", "sane_lists"],
                               extension_configs={"toc": {"toc_depth": "2-3"}})
        source = re.sub(r"\{\{code:([^}]+)\}\}", code_block, source)
        body = md.convert(source)
        body = body.replace("<table>", '<div class="table-scroll" tabindex="0" role="region" aria-label="표, 가로로 스크롤할 수 있습니다"><table>')
        body = body.replace("</table>", "</table></div>")
        target.write_text(template.substitute(
            title=html.escape(meta["title"]), description=html.escape(meta["description"], quote=True),
            page_title=html.escape("파이썬 공간데이터 사이언스 — GeoPandas에서 Spatial AI까지"
                                  if name == "index.md" else meta["title"] + " · 파이썬 공간데이터 사이언스"),
            eyebrow=html.escape(meta["eyebrow"]), prefix=prefix, body=body,
            nav="\n".join(nav), toc=md.toc,
            lead="" if name == "index.md" else '<p class="description">' + html.escape(meta["description"]) + '</p>',
            page_toc="" if name == "index.md" else '<details class="page-toc"><summary>이 페이지에서</summary>' + md.toc + '</details>',
            source_url="https://github.com/navicoby/navicoby.github.io/blob/main/books/python-geospatial/pages/" + name,
            canonical=SITE_URL + "/python-geospatial/" + ("" if name == "index.md" else str(Path(name).with_suffix(".html")).replace("\\", "/")),
        ), encoding="utf-8")
    downloads = OUT / "examples"
    downloads.mkdir(parents=True, exist_ok=True)
    for path in (BOOK / "examples").glob("*.py"):
        shutil.copy2(path, downloads / path.name)
    for name in ("requirements.txt", "requirements-build.txt", "requirements-lock.txt"):
        if (BOOK / name).exists():
            shutil.copy2(BOOK / name, downloads / name)
    # Third-party HTML/SVG generators emit trailing spaces; normalize text only.
    for directory, pattern in (("assets", "*.svg"), ("maps", "*.html")):
        for path in (OUT / directory).glob(pattern):
            text = path.read_text(encoding="utf-8")
            path.write_text("\n".join(line.rstrip() for line in text.splitlines()) + "\n",
                            encoding="utf-8")
    print(f"Built {len(pages)} pages in {OUT}")


if __name__ == "__main__":
    build()
