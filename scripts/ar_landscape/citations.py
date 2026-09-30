"""Numbered endnotes from explicit, reviewable chapter/section source mappings."""
from collections import OrderedDict
from pathlib import Path
import html,json,re

SITE=Path(__file__).resolve().parents[2]/'static/augmented-reality-landscape'
DATA=json.loads((SITE/'text/citation-data.json').read_text())
SOURCES=DATA['sources']
REPORT={}

def linkify(text):
    """Make recorded URLs/DOIs usable without inventing search-result links."""
    pattern=r'https?://[^\s<>"\u3000]+|(?<![\w/])10\.\d{4,9}/[^\s<>"·]+'
    parts=[];last=0
    for m in re.finditer(pattern,text):
        token=m[0].rstrip('.,;:。')
        while token.endswith(')') and token.count(')')>token.count('('):token=token[:-1]
        # Korean explanatory text sometimes immediately follows a URL.
        token=re.split(r'[가-힣]',token)[0] if not token.startswith('https://ko.wikipedia') else token
        if not token:continue
        parts.append(html.escape(text[last:m.start()]))
        url=token if token.startswith('http') else 'https://doi.org/'+token
        parts.append(f'<a href="{html.escape(url,quote=True)}">{html.escape(token)}</a>')
        last=m.start()+len(token)
    parts.append(html.escape(text[last:]))
    return ''.join(parts)

def annotate(md,key):
    if key not in DATA['sections']:return md
    mapping=DATA['sections'][key]
    level='###' if key.startswith('ch') else '##'
    chunks=re.split(rf'(?m)^({level} .+\n)',md)
    assert len(chunks)==1+2*len(mapping),(key,'section count changed')
    refs=OrderedDict();occurrences={};output=[chunks[0]]
    def cite(ids):
        links=[]
        for sid in dict.fromkeys(ids):
            assert sid in SOURCES,(key,sid)
            if sid not in refs:refs[sid]=len(refs)+1
            n=refs[sid];occurrences[sid]=occurrences.get(sid,0)+1
            links.append(f'<a class="citation" id="cite-{key}-{n}-{occurrences[sid]}" href="#ref-{key}-{n}" role="doc-noteref" aria-label="참고문헌 {n}">[{n}]</a>')
        return '<sup class="citation-group">'+''.join(links)+'</sup>' if links else ''
    for i,row in enumerate(mapping):
        heading,body=chunks[1+2*i:3+2*i]
        assert heading.strip()==level+' '+row['heading'],(key,i,row['heading'])
        blocks=re.split(r'\n\s*\n',body.strip())
        rules=row.get('blocks',[])
        for rule in rules:
            assert body.count(rule['match'])==1,(key,row['heading'],rule['match'],'must match exactly once')
        for j,block in enumerate(blocks):
            matching=[r for r in rules if r['match'] in block]
            if block.lstrip().startswith('|'):
                # A header override covers the whole table; a row override
                # attaches the source number directly to that row's last cell.
                lines=block.splitlines();table_refs=[]
                for r in matching:
                    if r['match'] in lines[0]:table_refs.extend(r['sources'])
                    else:
                        for k,line in enumerate(lines):
                            if r['match'] in line:
                                lines[k]=line.rstrip().removesuffix('|').rstrip()+' '+cite(r['sources'])+' |'
                block='\n'.join(lines)
                if table_refs or not matching:
                    source_ids=table_refs or row['sources']
                    label='표 출처: '+cite(source_ids)+' (본문 기준으로 재구성)' if source_ids else '표: 웹판 필자 작성'
                    block+='\n\n<p class="table-source">'+label+'</p>'
            elif matching:
                block+=' '+cite([sid for r in matching for sid in r['sources']])
            blocks[j]=block
        if row['sources']:
            # A section-ending citation covers its factual background. More
            # specific paragraph/table mappings above take precedence locally.
            target=next((j for j in range(len(blocks)-1,-1,-1) if blocks[j].strip() and blocks[j].strip()!='---'),None)
            assert target is not None,(key,i)
            tail=blocks[target]
            mark=cite(row['sources'])
            if tail.lstrip().startswith(('|','<')):blocks[target]=tail+'\n\n'+mark
            else:blocks[target]=tail+' '+mark
        output.extend([heading,'\n'+'\n\n'.join(blocks)+'\n\n'])
    if refs:
        output.append(f'<section class="references" id="references-{key}" role="doc-endnotes" aria-label="참고문헌">\n<h2>참고문헌</h2>\n')
        output.append('<p class="reference-guide">본문의 번호를 누르면 출처로 이동합니다. 절 끝의 번호는 그 절의 사실 자료를, 표 아래의 번호는 표에 사용한 자료를 가리킵니다. 비교·계산·비유와 결론은 필자의 재구성입니다. 한 번호에 함께 사용한 문헌이 둘 이상이면 묶어서 적었습니다.</p>\n')
        output.append('<p class="reference-guide">서지정보와 확인 메모는 옵시디언 조사 기록을 바탕으로 복원했습니다. 원 기록의 ‘전문 확인’·‘조회’ 표기는 당시 조사 상태이며 이번 웹판에서 모두 재검증했다는 뜻은 아닙니다. 불완전한 서지사항은 임의로 채우지 않았습니다.</p>\n<ol class="reference-list">\n')
        for sid,n in refs.items():
            r=SOURCES[sid];note=r.get('note','')
            if r.get('needs_detail'):note='출처 확인 필요. '+note
            body=linkify(r['bibliography'])
            if note:body+=f'<p class="reference-note">{html.escape(note)}</p>'
            if r.get('checked'):body+=f'<p class="reference-note">{html.escape(r["checked"])}</p>'
            # The original research's methodological caveats remain available
            # without burying the actual bibliographic entry.
            if r.get('record_note'):
                note=r['record_note'] if isinstance(r['record_note'],str) else json.dumps(r['record_note'],ensure_ascii=False)
                body+='<details class="source-context"><summary>원 조사에서 기록한 근거·한계</summary><p>'+html.escape(note)+'</p></details>'
            back=' '.join(f'<a href="#cite-{key}-{n}-{k}" class="citation-back" aria-label="참고문헌 {n} 인용 위치 {k}로 돌아가기">↩{k if occurrences[sid]>1 else ""}</a>' for k in range(1,occurrences[sid]+1))
            output.append(f'<li id="ref-{key}-{n}" data-source="{sid}"><span class="reference-number">[{n}]</span><div>{body} <span class="citation-backs">{back}</span></div></li>\n')
        output.append('</ol>\n</section>\n')
    REPORT[key]={'sections':len(mapping),'cited_sections':sum(bool(x['sources']) for x in mapping),'references':len(refs),'citation_links':sum(occurrences.values()),'sources':list(refs)}
    return ''.join(output)
