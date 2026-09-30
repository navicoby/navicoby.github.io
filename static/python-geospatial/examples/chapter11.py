from pathlib import Path

page = (
    '<!doctype html><html lang="ko"><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
    '<title>현장 지도 읽기</title>'
    '<style>body{max-width:52rem;margin:auto;padding:1rem;line-height:1.8}'
    'iframe{width:100%;height:60vh;border:1px solid #aaa}'
    '</style><h1>합성 현장 조사점</h1>'
    '<p>10장에서 만든 field-map.html을 같은 폴더에 두세요.</p>'
    '<iframe src="field-map.html" title="합성 조사점 지도" loading="lazy"></iframe>'
    '<p><a href="field-map.html">지도를 별도 화면으로 열기</a></p>'
    '<p>A와 B는 실습용 가상 조사점입니다.</p></html>'
)
Path("map-page.html").write_text(page, encoding="utf-8")
assert 'width=device-width' in page
print("map-page.html (requires chapter 10 output field-map.html)")
