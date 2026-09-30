"""Build the book from one curriculum; no network access."""
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
SITE_URL = "https://" + (ROOT / "static/CNAME").read_text(encoding="utf-8").strip()

def read_page(name):
    text = (BOOK / "pages" / name).read_text(encoding="utf-8")
    _, meta, body = text.split("---", 2)
    return yaml.safe_load(meta), body.strip()

def code_block(match):
    name, _, region = match[1].partition("#")
    path = (BOOK / "examples" / name).resolve()
    if not path.is_relative_to((BOOK / "examples").resolve()):
        raise ValueError("Example path must stay inside examples/")
    code = path.read_text(encoding="utf-8")
    if region:
        code = code.split(f"# start:{region}\n", 1)[1].split(f"# end:{region}", 1)[0]
    fence = chr(96) * 3
    return fence + "python\n" + code.strip() + "\n" + fence

def href(name, prefix=""):
    return prefix + Path(name).with_suffix(".html").as_posix()

def chapter_name(chapter):
    return f"chapters/{chapter['slug']}.md"

def part_name(part):
    return f"parts/{part['slug']}.md"

def chapter_title(chapter):
    return f"{chapter['id']:02d} · {chapter['title']}"

def part_title(part):
    return f"PART {part['number']:02d} · {part['title']}"

def diagram_block(key, prefix, registry):
    diagram = registry[key]
    identifier = 'diagram-' + key
    panels = []
    for panel in diagram['panels']:
        path = OUT / 'assets/diagrams' / panel['file']
        if not path.is_file() or not path.resolve().is_relative_to((OUT/'assets/diagrams').resolve()):
            raise ValueError('Missing or invalid diagram asset: ' + panel['file'])
        url = prefix + 'assets/diagrams/' + panel['file']
        panels.append('<div class="diagram-panel">'
            + '<h4>' + html.escape(panel['title']) + '</h4>'
            + f'<img src="{url}" width="{panel["width"]}" height="{panel["height"]}" loading="lazy" alt="{html.escape(panel["alt"], quote=True)}">'
            + '<p>' + html.escape(panel['note']) + '</p>'
            + f'<a class="diagram-open" href="{url}" target="_blank" rel="noopener" aria-label="{html.escape(panel["title"], quote=True)} 크게 보기">그림 크게 보기 ↗</a></div>')
    sources = ' · '.join('<a href="' + html.escape(s['url'], quote=True) + '">' + html.escape(s['label']) + '</a>' for s in diagram['sources'])
    return (f'<figure class="concept-figure" id="{identifier}" aria-labelledby="{identifier}-title">'
        + '<div class="diagram-heading"><span>그림으로 이해하기</span>'
        + f'<h3 id="{identifier}-title">{html.escape(diagram["title"])}</h3></div>'
        + f'<div class="diagram-panels" data-panels="{len(panels)}">' + ''.join(panels) + '</div>'
        + '<figcaption><strong class="diagram-takeaway">' + html.escape(diagram['takeaway']) + '</strong>'
        + '<p>' + html.escape(diagram['caption']) + '</p>'
        + '<p class="diagram-sources">직접 제작한 교육용 개념도 · 설명 근거: ' + sources + '</p></figcaption></figure>')

def curriculum_markdown(parts):
    sections = []
    for part in parts:
        sections.append(f"## {part_title(part)}\n\n{part['intro']}\n\n"
                        f"[{part['number']}부 안내와 학습 시작]({href(part_name(part))})\n")
        for chapter in part["chapters"]:
            sections.append(f"- [{chapter_title(chapter)}]({href(chapter_name(chapter))})")
        sections.append("")
    return "\n".join(sections)

def navigation(name, support, parts, prefix):
    def link(entry, title, cls=""):
        current = ' aria-current="page"' if entry == name else ""
        return f'<a class="{cls}" href="{href(entry, prefix)}"{current}>{html.escape(title)}</a>'
    items = [link(n, meta["title"]) for n, (meta, _) in support.items()]
    for part in parts:
        active = name == part_name(part) or any(
            chapter_name(c) == name for c in part["chapters"])
        items.append(f'<details class="nav-part"{" open" if active else ""}>'
                     f'<summary>{html.escape(part_title(part))}</summary>')
        items.append(link(part_name(part), f"{part['number']}부 안내", "part-overview"))
        items.extend(link(chapter_name(c), chapter_title(c)) for c in part["chapters"])
        items.append("</details>")
    return "\n".join(items)

def build():
    diagrams = json.loads((BOOK / 'diagrams.json').read_text(encoding='utf-8'))
    parts = json.loads((BOOK / "curriculum.json").read_text(encoding="utf-8"))
    chapters = [c for p in parts for c in p["chapters"]]
    ids = [c["id"] for c in chapters]
    if ids != list(range(1, len(chapters)+1)):
        raise ValueError("Chapter ids must be unique, consecutive and ordered")
    if len({c["slug"] for c in chapters}) != len(chapters):
        raise ValueError("Duplicate chapter slug")
    names = json.loads((BOOK / "pages.json").read_text(encoding="utf-8"))
    support = {name: read_page(name) for name in names}
    pages = dict(support)
    ownership = {}
    for part in parts:
        pmeta = {"title": part_title(part), "description": part["intro"],
                 "eyebrow": f"PART {part['number']:02d} / OVERVIEW"}
        body = ("이 부의 모든 장에는 개념 설명과 실행 예제가 있습니다. 아래 제목을 눌러 순서대로 읽으세요."
                "\n\n## 이 부에서 배우는 것\n\n" + part["intro"] +
                "\n\n## 장별 본문\n\n")
        for c in part["chapters"]:
            name = chapter_name(c)
            meta, source = read_page(name)  # Missing source must fail the build.
            meta["title"] = chapter_title(c)
            meta["eyebrow"] = f"PART {part['number']:02d} / CHAPTER {c['id']:02d}"
            pages[name] = (meta, source)
            ownership[name] = part
            body += f"- [{chapter_title(c)}]({href(name, '../')}) — {meta['description']}\n"
        first = part["chapters"][0]
        body += (f"\n## 학습 순서\n\n[{chapter_title(first)}]({href(chapter_name(first), '../')})"
                 "부터 시작하고 본문 아래의 ‘다음 장’을 따라가세요. "
                 "[전체 10부 목차](../roadmap.html)에서도 같은 순서를 확인할 수 있습니다.\n")
        pages[part_name(part)] = (pmeta, body)
        ownership[part_name(part)] = part
    template = Template((BOOK / "templates/page.html").read_text(encoding="utf-8"))
    order = [chapter_name(c) for c in chapters]
    for name, (meta, source) in pages.items():
        target = OUT / Path(name).with_suffix(".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        prefix = "../" * (len(Path(name).parts)-1)
        source = source.replace("{{curriculum}}", curriculum_markdown(parts))
        source = re.sub(r"\{\{diagram:([a-z0-9-]+)\}\}", lambda m: diagram_block(m[1], prefix, diagrams), source)
        source = re.sub(r"\{\{code:([^}]+)\}\}", code_block, source)
        md = markdown.Markdown(extensions=["fenced_code", "tables", "toc", "sane_lists"],
                               extension_configs={"toc":{"toc_depth":"2-3"}})
        body = md.convert(source)
        body = body.replace("<table>", '<div class="table-scroll" tabindex="0" role="region" aria-label="표, 가로로 스크롤할 수 있습니다"><table>')
        body = body.replace("</table>", "</table></div>")
        breadcrumbs = f'<a href="{prefix}index.html">책 소개</a>'
        if name in ownership:
            part = ownership[name]
            breadcrumbs += f' <span>›</span> <a href="{href(part_name(part), prefix)}">{html.escape(part_title(part))}</a>'
        adjacent = ""
        if name in order:
            index = order.index(name)
            links = []
            for offset, label in ((-1,"이전 장"), (1,"다음 장")):
                other = index + offset
                if 0 <= other < len(order):
                    links.append(f'<a rel="{"prev" if offset < 0 else "next"}" href="{href(order[other],prefix)}">'
                                 f'<small>{label}</small>{html.escape(chapter_title(chapters[other]))}</a>')
            adjacent = '<nav class="chapter-pager" aria-label="이전·다음 장">' + "".join(links) + "</nav>"
        source_path = ("curriculum.json" if name.startswith("parts/") else "pages/" + name)
        target.write_text(template.substitute(
            title=html.escape(meta["title"]),
            description=html.escape(meta["description"], quote=True),
            page_title=html.escape("파이썬 공간데이터 사이언스 — GeoPandas에서 Spatial AI까지"
                if name == "index.md" else meta["title"] + " · 파이썬 공간데이터 사이언스"),
            eyebrow=html.escape(meta["eyebrow"]), prefix=prefix, body=body,
            nav=navigation(name, support, parts, prefix),
            breadcrumbs=breadcrumbs, adjacent=adjacent,
            lead="" if name == "index.md" else '<p class="description">' + html.escape(meta["description"]) + '</p>',
            page_toc="" if name == "index.md" else '<details class="page-toc"><summary>이 페이지에서</summary>' + md.toc + '</details>',
            source_url="https://github.com/navicoby/navicoby.github.io/blob/main/books/python-geospatial/" + source_path,
            canonical=SITE_URL + "/python-geospatial/" + ("" if name == "index.md" else href(name)),
        ), encoding="utf-8")
    downloads = OUT / "examples"
    downloads.mkdir(parents=True, exist_ok=True)
    for path in (BOOK / "examples").glob("*.py"):
        shutil.copy2(path, downloads / path.name)
    for path in BOOK.glob("requirements*.txt"):
        shutil.copy2(path, downloads / path.name)
    for directory, pattern in (("assets", "*.svg"), ("maps", "*.html")):
        for path in (OUT / directory).glob(pattern):
            text = path.read_text(encoding="utf-8")
            path.write_text("\n".join(line.rstrip() for line in text.splitlines()) + "\n", encoding="utf-8")
    print(f"Built {len(pages)} pages: {len(parts)} parts, {len(chapters)} chapters, {len(support)} guides")

if __name__ == "__main__":
    build()
