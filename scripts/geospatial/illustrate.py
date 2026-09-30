"""Generate original SVG teaching diagrams and their accessible publication registry.
Run with the book environment. No network or external images are used.
"""
from pathlib import Path
from html import escape
import json
import math
from pyproj import Transformer

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "static/python-geospatial/assets/diagrams"
BOOK = ROOT / "books/python-geospatial"
GREEN="#285f44"
INK="#172a20"
MUTED="#53635a"
PALE="#e4eee1"
GOLD="#aa5b29"
SAND="#f1ddc4"
BLUE="#34667b"
WATER="#dcebf0"
LINE="#cbd8cb"
WHITE="#fbfcfa"
REGISTRY={}

def text(x,y,value,size=22,fill=INK,anchor="start",weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(str(value))}</text>'

def rect(x,y,w,h,fill=WHITE,stroke=LINE,r=0,dash=None):
    extra=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"{extra}/>'

def path(d,stroke=GREEN,width=3,fill="none",arrow=False,dash=None):
    extra=(' marker-end="url(#arrow)"' if arrow else "")+(f' stroke-dasharray="{dash}"' if dash else "")
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{extra}/>'

def circle(x,y,r,fill=GREEN,stroke=WHITE):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'

def box(y,label,value=None,color=GREEN):
    out=rect(36,y,288,72,PALE if color==GREEN else WATER,color,10)
    out+=text(180,y+26,label,22,color,"middle",600)
    if value:
        out+=text(180,y+60,value,22,INK,"middle")
    return out

def down(y1,y2,x=180):
    return path(f"M {x} {y1} V {y2}",arrow=True)

def write(name,title,desc,body,height=340):
    ASSETS.mkdir(parents=True,exist_ok=True)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 {height}" width="360" height="{height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8 Z" fill="{GREEN}"/></marker></defs>
<rect width="360" height="{height}" fill="{WHITE}"/>
<g font-family="Malgun Gothic,Apple SD Gothic Neo,Arial,sans-serif">{body}</g>
</svg>
'''
    (ASSETS/f"{name}.svg").write_text(svg,encoding="utf-8")
    return {"file":f"{name}.svg","width":360,"height":height,"alt":desc}

def panel(name,title,desc,body,note,height=340):
    item=write(name,title,desc,body,height)
    item.update(title=title,note=note)
    return item

def register(key,title,panels,caption,takeaway,sources):
    REGISTRY[key]={"title":title,"panels":panels,"caption":caption,
                   "takeaway":takeaway,"sources":[{"label":a,"url":b} for a,b in sources]}

# 1. Libraries: separate the file reader, data representation and calculation.
register("tools","같은 공간도, 자료의 모양에 따라 도구가 달라집니다",[
    panel("tools-vector","좌표와 도형을 가진 표",
          "공원·건물 벡터 파일을 GeoPandas 공간표로 읽고 Shapely로 거리와 겹침을 계산합니다.",
          box(20,"공원 · 건물 파일","GeoPackage / GeoJSON")+down(94,123)
          +box(130,"GeoPandas","속성표 + geometry")+down(204,233)
          +box(240,"Shapely","도형 · 거리 · 교차"),
          "GeoPandas가 공간표를 다루고 Shapely가 도형 연산을 맡습니다. 파일 입출력 엔진으로는 pyogrio 등을 사용합니다."),
    panel("tools-raster","셀마다 숫자가 있는 격자",
          "Rasterio로 DEM·위성영상과 지리참조를 읽고 NumPy 배열을 계산해 결과를 저장합니다.",
          box(20,"DEM · 위성영상","GeoTIFF / JP2",BLUE)+down(94,123)
          +box(130,"Rasterio","파일 읽기 · 위치 정보",BLUE)+down(204,233)
          +box(240,"NumPy","배열 · 마스크 · 계산",BLUE),
          "Rasterio가 파일과 지리참조를, NumPy가 숫자 계산을 맡습니다. 계산 결과는 Rasterio로 다시 저장합니다.")
], "입력 자료 → Python 자료구조 → 계산 도구 순으로 읽습니다. 모든 데이터가 모든 파일 형식에 들어가는 것은 아닙니다.",
   "GeoPandas와 Rasterio는 라이브러리이고, 벡터·래스터는 공간을 표현하는 방식입니다.",
   [("GeoPandas 자료구조","https://geopandas.org/en/stable/docs/user_guide/data_structures.html"),
    ("Rasterio 읽기","https://rasterio.readthedocs.io/en/stable/topics/reading.html")])

# 2. Vector versus raster: same park boundary, raster stores only the park mask.
poly=[(1,1),(5,1),(5,3),(7,3),(7,5),(1,5)]
coords=" ".join(f"{20+x*40},{32+y*40}" for x,y in poly)
vector=rect(20,32,320,240)+f'<polygon points="{coords}" fill="{PALE}" stroke="{GREEN}" stroke-width="3"/>'
vector+=path("M 28 234 L 145 156 L 324 156",GOLD,6)
for x,y in [(97,108),(144,111),(262,205)]:
    vector+=circle(x,y,9)
vector+=text(180,305,"점 · 선 · 면을 각각 보관",22,INK,"middle",600)
raster=""
inside_count=0
for row in range(6):
    for col in range(8):
        inside=(1<=row<3 and 1<=col<5) or (3<=row<5 and 1<=col<7)
        inside_count+=int(inside)
        raster+=rect(20+40*col,32+40*row,40,40,PALE if inside else WHITE)
        raster+=text(40+40*col,59+40*row,int(inside),22,GREEN if inside else MUTED,"middle")
raster+=text(180,305,"공원 안 1 / 공원 밖 0",22,INK,"middle",600)
assert inside_count==20
register("vector-raster","한 공원을 도형과 격자로 표현하면",[
    panel("vector-scene","벡터: 객체의 모양",
          "가상공원의 꺾인 경계는 면, 수목 세 그루는 점, 보행로는 선으로 표시했습니다.",
          vector,"녹색 면은 공원, 녹색 점은 수목, 갈색 선은 보행로입니다. 각 객체는 별도 속성을 가질 수 있습니다."),
    panel("raster-mask","래스터: 셀마다 값 하나",
          "같은 공원의 내부를 1, 외부를 0으로 표현한 6행 8열 격자입니다. 공원 셀은 20개입니다.",
          raster,"여기서는 공원 안/밖만 저장합니다. 수목과 보행로 정보까지 자동으로 보존되는 것은 아닙니다.")
], "직접 만든 개념도입니다. 격자와 맞춘 가상 경계여서 20셀이 정확히 대응합니다. 실제 경계에서는 셀 크기와 포함 규칙에 따라 근사가 생깁니다.",
   "벡터는 객체를, 래스터는 위치별 값을 중심으로 공간을 표현합니다.",
   [("GeoPandas 자료구조","https://geopandas.org/en/stable/docs/user_guide/data_structures.html"),
    ("Rasterio features","https://rasterio.readthedocs.io/en/stable/topics/features.html")])

# 3. CRS: use the exact point from chapter03.py.
lon,lat=126.9780,37.5665
east,north=Transformer.from_crs(4326,5179,always_xy=True).transform(lon,lat)
assert 900000<east<1000000 and 1900000<north<2000000
same=box(24,"원자료 좌표",f"{lon:.4f}, {lat:.4f}")+down(138,151)
same+=text(180,130,"set_crs(4326)",23,GREEN,"middle",600)
same+=box(160,"EPSG:4326 · 단위 도",f"{lon:.4f}, {lat:.4f}")
same+=text(180,292,"숫자는 그대로",25,INK,"middle",600)
transformed=box(24,"EPSG:4326 · 단위 도",f"{lon:.4f}, {lat:.4f}")+down(138,151)
transformed+=text(180,130,"to_crs(5179)",23,GREEN,"middle",600)
transformed+=box(160,"EPSG:5179 · 단위 m",f"{east:,.1f}, {north:,.1f}")
transformed+=text(180,292,"같은 위치, 다른 숫자",24,INK,"middle",600)
register("crs","좌표계 지정과 좌표 변환은 다릅니다",[
    panel("crs-assign","set_crs: 의미를 지정",
          f"경도 {lon}, 위도 {lat}라는 원자료의 좌표계를 확인한 뒤 EPSG 4326을 지정합니다. 숫자는 바뀌지 않습니다.",
          same,"원자료가 경위도라는 근거를 확인한 경우입니다. 숫자만 보고 좌표계를 추측해서 붙이면 안 됩니다."),
    panel("crs-transform","to_crs: 좌표를 계산",
          f"같은 점을 EPSG 5179로 변환하면 동쪽 좌표 {east:,.1f}m, 북쪽 좌표 {north:,.1f}m가 됩니다.",
          transformed,"GeoPandas의 x·y 순서에 맞춰 경도·위도를 입력했습니다. 출력은 소수 첫째 자리로 반올림했습니다.")
], "03장의 점을 pyproj로 변환해 수치를 만들었습니다. 양쪽은 별도의 단계 설명이며 set_crs로 숫자를 바꾸는 과정을 뜻하지 않습니다.",
   "좌표계 정보를 붙이는 일과 좌표값을 변환하는 일을 구별하세요.",
   [("GeoPandas 좌표계","https://geopandas.org/en/stable/docs/user_guide/projections.html")])

# 4. Join vs intersection: identical inputs, different geometry results.
def join_scene(cut=False):
    s=rect(40,48,210,140,PALE,GREEN,14)+text(65,82,"영역 P01",22,GREEN)
    if cut:
        s+=rect(205,123,105,103,"none",GOLD,0,"6 5")
        s+=rect(205,123,45,65,SAND,GOLD)
        s+=text(257,113,"B01",22,GOLD,"middle",600)
    else:
        s+=rect(205,123,105,103,SAND,GOLD)+text(257,176,"B01",23,GOLD,"middle",600)
    s+=down(236,265)
    s+=rect(28,275,304,45,PALE if cut else SAND,GREEN if cut else GOLD,6)
    s+=text(180,305,"교차한 도형만 남김" if cut else "B01 행에 P01 속성 추가",21,INK,"middle",600)
    return s
register("join-overlay","속성을 붙일까, 겹친 도형을 만들까",[
    panel("join-preserve","공간조인: 건물은 그대로",
          "건물 B01의 일부가 영역 P01에 걸쳐 있습니다. intersects 공간조인은 건물 전체 도형을 유지하고 P01 속성을 연결합니다.",
          join_scene(),"건물을 왼쪽 자료로 하는 sjoin입니다. 겹치는 영역이 여러 개면 같은 건물이 여러 행에 나타날 수 있습니다."),
    panel("intersection-cut","Intersection: 공통 부분",
          "같은 입력의 intersection 결과는 B01과 P01이 겹치는 부분만 남습니다. 원래 건물 외곽선은 점선으로 표시했습니다.",
          join_scene(True),"잘린 조각의 면적을 구할 때 사용합니다. 점선 부분은 입력 건물의 원래 크기를 비교하기 위한 표시입니다.")
], "공간 관계를 설명하는 별도 가상 도형이며 축척이 없습니다. 07장 실습의 30m 버퍼 수치를 다시 그린 그림은 아닙니다.",
   "sjoin은 관계를 연결하고, intersection·overlay는 새 도형을 계산합니다.",
   [("GeoPandas 공간조인","https://geopandas.org/en/stable/docs/user_guide/mergingdata.html"),
    ("GeoPandas 겹치기","https://geopandas.org/en/stable/docs/user_guide/set_operations.html")])

# 5. Terrain: section slope and compass aspect.
angle=math.degrees(math.atan(.1))
slope=path("M 46 222 L 286 198 L 286 222 Z",GREEN,3,PALE)
slope+=path("M 46 242 H 286",MUTED,2)+text(166,274,"수평거리 10m",23,INK,"middle")
slope+=path("M 307 198 V 222",GOLD,3)+text(285,169,"높이차 1m",23,GOLD,"middle")
slope+=path("M 85 222 A 39 39 0 0 0 84.8 218.1",GOLD,3)
slope+=text(95,195,f"θ ≈ {angle:.2f}°",24,GOLD)
slope+=text(180,57,"1 ÷ 10 × 100 = 10%",24,INK,"middle",600)
slope+=text(180,99,"10% ≠ 10°",28,GOLD,"middle",600)
aspect=path("M 180 275 V 67",LINE,2)+path("M 75 173 H 285",LINE,2)
aspect+=circle(180,173,85,"none",LINE)
aspect+=text(180,38,"북 0°",23,INK,"middle")+text(316,181,"동",23,INK,"middle")
aspect+=text(180,315,"남 180°",23,INK,"middle")+text(43,181,"서",23,INK,"middle")
aspect+=path("M 138 131 L 237 230",GREEN,6,arrow=True)+circle(138,131,7,GOLD)
aspect+=text(100,101,"높음",22,GOLD,"middle")+text(266,268,"낮음",22,GREEN,"middle")
aspect+=path("M 180 111 A 62 62 0 0 1 223.8 216.8",GOLD,2)
aspect+=text(241,136,"135°",24,GOLD,"middle",600)
register("terrain","경사도는 가파름, 향은 내려가는 방향",[
    panel("slope-angle","경사도: 높이차와 수평거리",
          f"수평거리 10m에서 1m 높아지는 단면은 10퍼센트 경사이고 각도는 약 {angle:.2f}도입니다.",
          slope,"높이차 1m / 수평거리 10m의 별도 단면 예입니다. DEM에서는 동서·남북 두 방향 기울기를 합쳐 경사도를 구합니다."),
    panel("aspect-direction","향: 가장 낮아지는 방향",
          "북을 0도, 동을 90도로 두고 시계 방향으로 읽습니다. 남동쪽으로 가장 낮아지는 경사면의 향은 135도입니다.",
          aspect,"경사면이 남동쪽으로 내려간다는 가정입니다. 평탄한 셀에는 내려가는 방향이 없어 향을 정의하지 않습니다.")
], "직접 제작한 경사와 향의 개념도입니다. Hillshade는 별도로 정한 광원을 이용한 음영 표현이며 실제 일조시간이 아닙니다.",
   "각도(°), 퍼센트(%), 방향(°)은 숫자가 비슷해 보여도 다른 의미입니다.",
   [("NumPy gradient","https://numpy.org/doc/stable/reference/generated/numpy.gradient.html")])

# 6. Satellite: reflectance, categorical resampling, masked index.
bands=rect(35,30,130,100,SAND,GOLD,10)+rect(195,30,130,100,PALE,GREEN,10)
bands+=text(100,65,"B04",24,GOLD,"middle",600)+text(100,101,"0.10",27,GOLD,"middle",600)
bands+=text(260,65,"B08",24,GREEN,"middle",600)+text(260,101,"0.50",27,GREEN,"middle",600)
bands+=text(100,163,"적색 · 10m",22,INK,"middle")+text(260,163,"근적외 · 10m",22,INK,"middle")
bands+=down(184,229)+text(180,267,"보정 후 반사도",25,INK,"middle",600)
bands+=text(180,309,"DN · offset 먼저 확인",22,MUTED,"middle")
scl_values=[[4,9],[5,6]]
scl_colors={4:PALE,9:"#dce1e0",5:SAND,6:WATER}
scl=""
for y,row in enumerate(scl_values):
    for x,value in enumerate(row):
        scl+=rect(58+x*50,28+y*50,50,50,scl_colors[value])
        scl+=text(83+x*50,63+y*50,value,23,INK,"middle")
scl+=text(243,67,"20m",25,INK,"middle",600)+text(243,103,"2 × 2",23,MUTED,"middle")
scl+=down(142,173)+text(225,165,"nearest",22,GREEN,"middle")
for y in range(4):
    for x in range(4):
        value=scl_values[y//2][x//2]
        scl+=rect(58+x*25,192+y*25,25,25,scl_colors[value])
# Boundaries distinguish replicated categories without unreadably small labels.
scl+=path("M 108 192 V 292 M 58 242 H 158",INK,2)
scl+=text(243,230,"10m",25,INK,"middle",600)+text(243,267,"4 × 4",23,MUTED,"middle")
scl+=text(180,328,"분류값은 그대로 유지",22,MUTED,"middle")
ndvi_value=(.5-.1)/(.5+.1)
assert math.isclose(ndvi_value,2/3)
ndvi=text(180,35,"NDVI = (NIR − R) / (NIR + R)",20,INK,"middle",600)
ndvi+=text(180,70,"(0.50 − 0.10) / 0.60 = 0.67",21,GREEN,"middle",600)
for y in range(4):
    for x in range(4):
        cloudy=y<2 and x>=2
        ndvi+=rect(100+x*40,100+y*40,40,40,"#dce1e0" if cloudy else "#b2cc91")
        ndvi+=text(120+x*40,127+y*40,"×" if cloudy else "·",24,MUTED if cloudy else GREEN,"middle",600)
ndvi+=text(180,304,"구름 셀 × → 분석에서 제외",22,INK,"middle",600)
register("satellite","밴드 두 장과 구름 분류를 함께 읽습니다",[
    panel("satellite-bands","01 · 반사도 준비",
          "동일 위치의 적색 B04와 근적외선 B08을 읽습니다. 계산 예의 보정된 반사도는 각각 0.10과 0.50입니다.",
          bands,"예시 숫자는 실제 관측값이 아닙니다. 원본 DN이면 제품 메타데이터의 scale·offset을 확인하고, 이미 보정된 값에는 중복 적용하지 않습니다."),
    panel("satellite-scl","02 · SCL 격자 맞추기",
          "20m SCL의 4·9·5·6 분류를 10m 기준 격자에 nearest로 맞춥니다. 각 분류 셀은 네 개로 나뉘지만 새 관측 정보가 생기지는 않습니다.",
          scl,"4=식생, 9=고확률 구름, 5=비식생, 6=물입니다. 격자 원점·CRS·범위가 맞는 단순 예이며, 실제 작업은 기준 밴드의 transform에 정렬합니다."),
    panel("satellite-ndvi","03 · 유효한 셀만 계산",
          "가상 반사도 0.10과 0.50의 NDVI는 약 0.67입니다. SCL에서 구름으로 표시한 오른쪽 위 네 셀은 제외합니다.",
          ndvi,"초록색은 여기서 남긴 유효 셀, ×는 제외 셀입니다. 색과 NDVI만으로 수종이나 건강 상태가 확정되는 것은 아닙니다.")
], "같은 범위를 가정한 합성 2×2/4×4 격자입니다. 분류 마스크는 범주를 유지하며, 연속값 밴드의 보간 방식과 구별합니다. SCL의 단순 표기는 아래 본문·공식 문서를 함께 읽으세요.",
   "같은 위치·같은 격자로 맞춘 뒤 구름을 제외하고 NDVI를 계산합니다.",
   [("Sentinel-2 처리·SCL","https://sentiwiki.copernicus.eu/web/s2-processing"),
    ("Sentinel-2 제품·밴드","https://sentiwiki.copernicus.eu/web/s2-products")])

# 7. Straight line versus a walkable network, with equal-axis scale.
def walking_scene(route=False):
    s=rect(20,18,320,292)
    s+=rect(122,131,62,52,WATER,BLUE,8)+text(153,164,"연못",21,BLUE,"middle")
    s+=path("M 70 260 V 60 H 220",LINE,10)
    if route:
        s+=path("M 70 260 V 60 H 220",GREEN,5,arrow=True)
        s+=text(92,220,"160m",22,GREEN)
        s+=text(145,44,"120m",22,GREEN,"middle")
    else:
        s+=path("M 70 260 L 220 60",GOLD,3,dash="8 7")
        s+=text(232,204,"200m",25,GOLD,"middle",600)
    s+=circle(70,260,9,GOLD)+circle(220,60,9,GREEN)
    s+=text(110,293,"출발",22,GOLD,"middle")
    s+=text(265,93,"출입구",22,GREEN,"middle")
    s+=text(180,342,"160 + 120 = 280m" if route else "두 점 사이의 직선",24,INK,"middle",600)
    return s
assert math.hypot(120,160)==200 and 120+160==280
register("walking","가까운 공원과 걸어서 가까운 공원",[
    panel("walking-straight","직선거리: 200m",
          "출발점과 공원 출입구 사이 직선거리는 200m입니다. 직선은 연못을 가로지르므로 보행 가능한 길이 아닙니다.",
          walking_scene(),"직선거리는 위치 간 근접성을 나타냅니다. 사이에 무엇이 있는지는 따로 검사해야 합니다.",365),
    panel("walking-network","보행거리: 280m",
          "통행 가능한 길을 따라 160m와 120m 구간을 지나면 출입구까지 280m입니다.",
          walking_scene(True),"연결된 간선의 길이를 더합니다. 담장·횡단보도·출입구와 접근 연결선을 반영하면 결과가 다시 달라질 수 있습니다.",365)
], "거리 개념을 비교하는 별도 가상 예입니다. 두 축의 축척을 같게 그렸으며 25장 코드의 335m 사례와는 다른 입력입니다.",
   "직선 버퍼 안에 들어온다고 그 거리만큼 걸어서 도달할 수 있는 것은 아닙니다.",
   [("NetworkX 최단경로","https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html")])

# 8. TinyUNet corresponds to chapter32.py, including the concatenated channels.
def network_box(y,label,value,fill=PALE):
    return rect(22,y,258,64,fill,GREEN,9)+text(151,y+23,label,22,GREEN,"middle",600)+text(151,y+55,value,22,INK,"middle")
unet=network_box(14,"입력","4 × 16 × 16",WATER)
unet+=down(80,105,151)+network_box(112,"Encoder","8 × 16 × 16")
unet+=down(178,203,151)+network_box(210,"Pool + Bottom","16 × 8 × 8")
unet+=down(276,301,151)+network_box(308,"확대","16 × 16 × 16")
unet+=down(374,399,151)+network_box(406,"채널 합치기","24 × 16 × 16",SAND)
unet+=down(472,497,151)+network_box(504,"Decoder","8 × 16 × 16")
unet+=down(570,595,151)+network_box(602,"분류 점수 출력","2 × 16 × 16",WATER)
unet+=path("M 282 144 H 328 V 438 H 282",GREEN,3,arrow=True,dash="7 5")
unet+=rect(291,271,61,32,WHITE,WHITE,2)+text(322,294,"skip",20,GREEN,"middle",600)
register("unet","U-Net: 줄여서 읽고, 다시 키우며 위치를 연결합니다",[
    panel("unet-tensor-flow","본문 TinyUNet의 실제 크기",
          "입력 4×16×16, Encoder 8×16×16, Pool과 Bottom 16×8×8, 확대 16×16×16을 거칩니다. Encoder의 8채널을 skip으로 연결해 24채널로 합친 뒤 8채널을 거쳐 2범주 점수를 출력합니다.",
          unet,"숫자는 채널 × 높이 × 너비입니다. 배치 N=1은 생략했습니다. 점선은 해상도가 같은 Encoder 특징을 전달하는 skip connection입니다.",690)
], "32장의 교육용 TinyUNet 코드와 일치하는 크기입니다. 원 논문 전체 구조의 복제나 학습 완료 모델을 의미하지 않습니다. 마지막 출력은 두 범주의 logits이며 아직 최종 분류 지도는 아닙니다.",
   "확대된 16채널과 이전 단계의 8채널을 연결하면 24채널이 됩니다.",
   [("U-Net 원 논문·저자 자료","https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/"),
    ("PyTorch Conv2d","https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html")])

(BOOK/"diagrams.json").write_text(json.dumps(REGISTRY,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Generated {len(REGISTRY)} diagram groups and {sum(len(x['panels']) for x in REGISTRY.values())} SVG panels.")
