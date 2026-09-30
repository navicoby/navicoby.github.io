# 증강현실 · 조경 — 조사 원본

본문 집필에 쓴 조사 결과 전체다. 각 항목은 웹 조사 뒤 검증자 3명이 독립적으로
반박을 시도하는 절차를 거쳤다. 정정 내역을 함께 실었다.

---
| 조사 | 항목 | 정정 |
| --- | --- | --- |


\newpage

# 증강현실 기술

## definition
항목 11개 · 검증 정정 지적 28건


### Ivan E. Sutherland, 「The Ultimate Display」 (궁극의 디스플레이)
| 항목 | 내용 |
| --- | --- |
| 주체 | Ivan E. Sutherland — Information Processing Techniques Office, ARPA, OSD (당시 ARPA IPTO 실장) |
| 연도 | 발표 1965년 (IFIP Congress 65에서 발표·수록) |
| 수치 | 논문 분량 3쪽(IFIP Congress Proceedings, pp. 506-508); 참고문헌 2건(Knowlton BEFLIX 1964, Sutherland Sketchpad 1963) |
| 출처 | Ivan E. Sutherland, "The Ultimate Display", Proceedings of IFIP Congress, pp. 506-508, 1965. 전문 PDF: https://worrydream.com/refs/Sutherland_1965_-_The_Ultimate_Display.pdf (전문 대조 완료) |

AR/VR 전체 계보의 출발점이지만 하드웨어 논문이 아니라 **디스플레이 철학 선언문**이다. 서덜랜드의 핵심 논지는 '컴퓨터에 연결된 디스플레이는 물리세계에서 실현 불가능한 개념과 친숙해질 기회를 준다'는 것이다. 즉 디스플레이의 목적은 현실의 재현이 아니라 **현실에 없는 것을 감각 가능하게 만드는 것**이다. 이 논문은 시각에만 한정하지 않고 역감(kinesthetic display, 힘 되먹임 조이스틱), 청각, 그리고 '가능한 한 많은 감각'에 봉사해야 한다고 명시한다. 흔히 인용되는 '궁극의 디스플레이=물질의 존재를 제어하는 방'은 마지막 문단의 사고실험일 뿐, 논문의 실질은 그 앞의 다감각·상호작용 논의다. 조경에 직접 연결되는 대목은 시선 의존 렌더링의 예언이다 — '우리가 어디를 보는지에 따라 표시가 달라지게 만드는 실험'은 오늘날 비전프로의 포비티드 렌더링(foveated rendering)과 정확히 같은 발상이다.

'디스플레이=현실의 창(window)'이라는 통념을 '디스플레이=수학적 원더랜드로 들어가는 거울(looking glass)'로 뒤집었다. 재현(representation)에서 경험(experience)으로 목표를 옮긴 최초의 문서다. 또한 시각 단일 감각 가정을 깨고 역감·청각을 동급으로 놓았다 — Azuma 2001이 40년 뒤 'AR은 시각에 한정되지 않는다'고 못 박은 것의 원형이다.

'증강현실'이라는 용어도, 실세계와 가상물의 정합(registration) 개념도 이 논문에는 없다. 실제 구현·측정치도 없는 개념 에세이다. 흔히 인용되는 '궁극의 디스플레이' 문장을 VR의 정의처럼 쓰는 것은 과잉 인용이며, 원문에서는 마지막 한 문단의 비유다.

### Ivan E. Sutherland, 「A head-mounted three dimensional display」 (머리에 쓰는 3차원 디스플레이)
| 항목 | 내용 |
| --- | --- |
| 주체 | Ivan E. Sutherland — The University of Utah (논문 작성 당시). 연구 수행은 하버드대학에서 ARPA(SD 265)·ONR(1866(16)) 지원. |
| 연도 | 발표 1968년 (AFIPS Fall Joint Computer Conference, 1968, pp. 757-764) |
| 수치 | 시야각 40°; 가상상 거리 각 눈 앞 약 18인치(≈46cm); 소형 CRT 화면 약 0.5인치 사각, 공칭 스폿 크기 0.6mil(≈15µm); 머리 이동 작업체적 지름 약 6피트(≈1.8m)×높이 3피트(≈0.9m), 상하 틸트 약 ±40°; 머리 위치 센서 목표 분해능 1/100인치(≈0.25mm) 및 회전 1/10,000; 요구 정확도 약 1/10인치(≈2.5mm); 광학계 핀쿠션 왜곡 약 3% → 최대 0.3인치(≈7.6mm) 오차; 초음파 송신기 3개(37 / 38.6 / 40.2 kHz)·수신기 4개·경로 12개, 40kHz 파장 약 1/3인치로 1/3인치 간격 모호성; 표시 성능 3,000선 @ 30 fps(선당 약 10µs); 행렬 승산기 끝점당 약 5µs·16회 누산 곱셈·초당 약 3,0 |
| 출처 | Ivan E. Sutherland, "A head-mounted three dimensional display", Proceedings of the AFIPS Fall Joint Computer Conference, Washington, D.C.: Thompson Books, 1968, pp. 757-764. ACM DOI 10.1145/1476589.1476686. 스캔본 전문 대조: https://www.cise.ufl.edu/~lok/teaching/ve-s07/papers/sutherland-headmount.pdf |

세계 최초의 실동 HMD 시스템 논문이며, **광학 시스루(optical see-through) AR의 원형**이다. 핵심 원리는 이렇다. 머리에 부착한 소형 CRT 두 개가 선화(wire frame) 영상을 그리고, 그 빛을 프리즘 속 **반투명 거울(half-silvered mirror)**로 접어 눈에 넣는다. 반투명 거울이므로 사용자는 CRT 영상과 방 안의 실물을 **동시에** 본다. 머리 위치는 천장에 매단 기계식 팔 또는 초음파 센서가 측정하고, 그 값으로 행렬 승산기가 관측자 좌표계 변환을, 클리핑 디바이더가 시야 절단과 원근 나눗셈을 실시간 수행한다. 서덜랜드는 안구 회전은 아예 측정하지 않고 머리 위치·자세만 측정한다고 명시했다 — 시선 추적을 포기한 대신 프레임 단위 재계산으로 버틴 설계다.

이 논문의 한 문장이 AR을 VR에서 갈라놓았다. '표시된 내용을 공간에 떠 있게 할 수도, 지도·책상·벽·타자기 자판에 겹쳐 일치시킬 수도 있다' — **가상 정보를 실세계의 특정 물체에 좌표적으로 고정시킨다**는 발상, 곧 오늘날의 정합(registration)이 여기서 처음 실물로 구현됐다. 또 1965년 논문이 개념이었다면 1968년 논문은 지연·정확도·시야각이라는 **공학적 예산(budget)**을 처음 수치로 제시했다.

은선 제거(hidden line problem)를 포기해 모든 물체가 투명 와이어프레임이다. '불투명 물체 표시는 현재 능력 밖'이라고 원문이 명시한다. 머리 추적은 천장에 고정된 기계팔 또는 초음파에 묶여 있어 방 밖으로 나갈 수 없고, 초음파 방식은 파장 모호성 때문에 완전 보고가 불가능하다고 적었다. '증강현실'이라는 용어는 등장하지 않는다.

### Thomas P. Caudell & David W. Mizell, 「Augmented reality: an application of heads-up display technology to manual manufacturing processes」 — 'augmented reality' 용어의 탄생
| 항목 | 내용 |
| --- | --- |
| 주체 | Thomas P. Caudell, David W. Mizell — Boeing Computer Services, Research and Technology (보잉 항공기 조립 현장 연구) |
| 연도 | 발표·수록 1992년 (Proceedings of the 25th Hawaii International Conference on System Sciences, HICSS-92) |
| 수치 | 논문에 정량 사양은 제시되지 않음(설계·프로토타이핑 단계 보고). IEEE DOI 10.1109/HICSS.1992.183317 |
| 출처 | T.P. Caudell, D.W. Mizell, "Augmented reality: an application of heads-up display technology to manual manufacturing processes", Proc. Hawaii International Conference on System Sciences (HICSS), vol.2, pp.659-669, 1992. DOI 10.1109/HICSS.1992.183317 (초록 원문 대조, 본문 전문은 유료) |

'증강현실(augmented reality)'이라는 **용어 자체가 처음 쓰인 논문**이다. 문제는 대단히 구체적이었다. 보잉은 항공기 배선 하네스(wiring harness)를 조립할 때 실물 크기 도면판(formboard)과 템플릿을 항공기 형식마다 따로 만들어야 했다. 코델과 미젤은 이 물리적 치구를 **투시형 헤드마운트 디스플레이(HUDset)로 대체**하자고 제안했다. 원리는 머리 위치 센서와 실세계 정합(registration) 시스템을 결합해, 컴퓨터가 만든 도면을 실제 작업 대상물의 지정된 위치에 겹쳐 고정(superimposed and stabilized)시키는 것이다. 즉 AR의 산업적 정의는 처음부터 '정보를 띄우기'가 아니라 **'물리적 치구를 정보로 대체하기'**였다.

개념(1965)과 장치(1968)는 있었으나 **이름과 산업적 정당화**가 없었다. 이 논문이 둘 다 제공했다. 특히 '무엇을 없앨 수 있는가(템플릿·도면판·마스킹 장치)'로 가치를 논증한 점이 중요하다. 조경 AR의 사업 논리도 같은 형태를 취해야 한다 — 새 볼거리를 더하는 것이 아니라, 현장에 반복 설치하던 기준점·규준틀·말뚝 같은 물리적 치구를 정보로 대체하는 것.

전문(full text)을 확보하지 못해 초록만 원문 대조했다. 본문 안에서 'augmented reality'를 어떻게 정의했는지의 정확한 문장은 이 조사에서 확인하지 못했다. 또한 실제 현장 배치 성과·정합 오차 수치는 이 논문 단계에서 보고되지 않았다.

### Steven Feiner, Blair MacIntyre & Dorée Seligmann, 「Knowledge-based augmented reality」 (KARMA)
| 항목 | 내용 |
| --- | --- |
| 주체 | Steven Feiner, Blair MacIntyre — Columbia University; Dorée Seligmann — AT&T Bell Labs |
| 연도 | 발표·게재 1993년 (Communications of the ACM 36(7), July 1993, pp. 53-62) |
| 수치 | CACM 36권 7호 pp.53-62; 인용 약 969회(OpenAlex 기준, 본 조사 수집 시점) |
| 출처 | S. Feiner, B. MacIntyre, D. Seligmann, "Knowledge-based augmented reality", Communications of the ACM 36(7), 1993, pp.53-62. DOI 10.1145/159544.159587. 인용문은 컬럼비아대 KARMA 프로젝트 공식 페이지 원문: https://graphics.cs.columbia.edu/projects/karma/karma.html |

AR을 '겹쳐 보여 주는 장치'에서 **'무엇을 겹칠지 스스로 결정하는 시스템'**으로 끌어올린 논문이다. KARMA(Knowledge-based Augmented Reality for Maintenance Assistance)는 레이저 프린터의 간단한 유지보수를 설명하는 시제품으로, 프린터 주요 부품에 Logitech 3D 트래커를 붙여 위치·자세를 감시한다. 핵심은 IBIS라는 규칙 기반 도해 생성 시스템이 오버레이 그래픽을 **실시간으로 자동 설계**한다는 점이다. 예컨대 '사용자에게 어떤 물체의 위치를 보여 주라'는 목표가 주어지면, 시스템은 그 물체가 다른 물체에 가려졌는지 판단해 가려졌으면 투시되게 그리고, 이미 실세계에서 보인다면 **아예 그리지 않는다**. 즉 오버레이의 최적 형태는 '적게 그리기'일 수 있다는 것을 규칙으로 명시했다.

이전까지 AR의 콘텐츠는 사람이 미리 만들어 둔 것이었다. KARMA는 세계 모델(무엇이 어디에 있고 무엇에 가려져 있는가)로부터 표시 내용을 **연역**했다. 밀그램의 'Extent of World Knowledge' 축이 왜 필요한지를 실물로 보여 준 사례이며, 조경 AR에서 '식재 도면 전체를 띄울 것인가, 지금 심을 한 그루만 띄울 것인가'라는 문제의 최초 형식화다.

인용문은 논문 본문이 아니라 저자 연구실의 KARMA 프로젝트 공식 설명 페이지에서 가져온 것이다(CACM 본문은 유료). 대상은 레이저 프린터 한 대 규모의 실내 환경이며, 트래커를 부품마다 물리적으로 부착해야 했다 — 야외·대규모 지형에는 그대로 적용되지 않는다.

### Paul Milgram & Fumio Kishino, 「A Taxonomy of Mixed Reality Visual Displays」 — 가상성 연속체(virtuality continuum)와 3축 분류
| 항목 | 내용 |
| --- | --- |
| 주체 | Paul Milgram — University of Toronto 산업공학과 (1993-94년 ATR 초빙 연구); Fumio Kishino — ATR Communication Systems Research Laboratories, 교토 |
| 연도 | 투고 1994년 7월 8일, 개정 1994년 8월 25일, 게재 1994년 12월 (IEICE Transactions on Information and Systems, Vol. E77-D, No.12) |
| 수치 | IEICE Trans. Inf. & Syst., Vol. E77-D, No.12, 1994년 12월, 시작 페이지 1321; 혼합현실 하이브리드 디스플레이 6개 부류 제시(1995 SPIE 논문에서는 7개로 확장); 분류축 3개(EWK, RF, EPM); 선행 분류체계 4건 검토(Sheridan 1992, Zeltzer 1992, Naimark 1991, Robinett 1992); 인용 약 4,635회(OpenAlex 기준, 본 조사 수집 시점) |
| 출처 | P. Milgram, F. Kishino, "A Taxonomy of Mixed Reality Visual Displays", IEICE Transactions on Information and Systems, Vol. E77-D, No.12, December 1994, p.1321-. 저자 공개 전문(토론토대 ETC Lab, 웹아카이브 보존본) 대조: http://etclab.mie.utoronto.ca/people/paul_dir/IEICE94/ieice.html |

AR과 VR을 **대립항이 아니라 하나의 축 위의 위치**로 재정의한 논문이다. 왼쪽 끝은 실물만으로 이루어진 환경, 오른쪽 끝은 가상물만으로 이루어진 환경이고, 그 사이 전부가 혼합현실(Mixed Reality)이다. 여기서 '증강현실'은 축의 왼쪽 절반, '증강가상(Augmented Virtuality)'은 오른쪽 절반을 가리킨다. 그런데 밀그램의 진짜 기여는 이 1차원 축이 **불충분하다**고 스스로 선언한 데 있다. 그는 세 가지 질문 — 표시되는 세계를 우리가 얼마나 알고 있는가(EWK), 얼마나 '사실적으로' 표시할 수 있는가(RF), 관찰자가 그 세계 안에 있다는 착각은 어느 정도인가(EPM) — 을 세 축으로 세운다. 또한 '실물/가상물', '직접 관찰/재합성 관찰', 광학적 의미의 '실상/허상'을 구별해, 실물의 영상과 자기 손의 실재성이 같은 '실(real)'이 아님을 못 박았다.

연속체 도식 하나로 AR·VR·텔레프레즌스를 같은 좌표계에 올려놓았다. 이 그림은 이후 30년간 거의 모든 AR/VR 논문의 첫 그림이 되었다. 조경 실무에 중요한 것은 EWK 축이다 — '컴퓨터가 그 장소에 대해 무엇을 아는가'가 표시 가능한 것의 상한을 정한다. 지형 모델·수목 위치·경계 정보가 없으면 오버레이는 그저 떠 있는 그림에 머문다.

원문이 스스로 밝히듯 **시각 디스플레이에만 한정**된다(청각·촉각·전정감각 AR은 언급만 하고 다루지 않음). 또 논문 스스로 EPM 축이 RF 축과 '완전히 직교하지는 않는다'고 인정한다 — 이 비직교성이 2021년 Skarbez의 재검토에서 두 축을 하나로 합치는 근거가 된다. 끝 페이지 번호(통상 1321-1329로 인용됨)는 이 조사에서 원문으로 확인하지 못했다.

### Paul Milgram, Haruo Takemura, Akira Utsumi & Fumio Kishino, 「Augmented Reality: A class of displays on the reality-virtuality continuum」 — EWK/RF/EPM 축의 상세 정의
| 항목 | 내용 |
| --- | --- |
| 주체 | Paul Milgram(당시 ATR 초빙, University of Toronto), Haruo Takemura(현 NAIST), Akira Utsumi, Fumio Kishino — ATR Communication Systems Research Laboratories, 교토 |
| 연도 | 학술대회 1994년(SPIE Vol. 2351, Telemanipulator and Telepresence Technologies) / 프로시딩 정식 출판 1995년으로 색인되는 경우가 많음(DOI 10.1117/12.197321). 저자 원고 표지에는 '1994'로 표기 |
| 수치 | SPIE Vol. 2351 'Telemanipulator and Telepresence Technologies'; 혼합현실 디스플레이 7개 부류(1994 IEICE의 6부류에서 확장); 분류축 3개; 인용 약 2,367회(OpenAlex 기준, 본 조사 수집 시점) |
| 출처 | P. Milgram, H. Takemura, A. Utsumi, F. Kishino, "Augmented Reality: A class of displays on the reality-virtuality continuum", Proc. SPIE Vol. 2351, Telemanipulator and Telepresence Technologies, 1994/1995, pp.282-292. DOI 10.1117/12.197321. 저자 공개 전문(웹아카이브 보존본) 대조: http://etclab.mie.utoronto.ca/people/paul_dir/SPIE94/SPIE94.full.html |

1994년 IEICE 논문의 자매편이자, 세 분류축을 **가장 상세히 서술한 정본**이다. 여기서 혼합현실(MR)의 표준 정의가 나온다 — '실세계 물체와 가상세계 물체가 하나의 디스플레이 안에 함께 제시되는 환경'. 그리고 AR을 시스루 HMD에만 한정할 것인가라는 당시의 논쟁에 '아니다'로 답한다. EWK 축은 '어디에(where)'와 '무엇(what)'이라는 두 종류의 지식으로 쪼개지고, 그 사이 구간(어디는 알지만 무엇은 모름, 또는 그 반대)이 실제 AR 시스템이 놓이는 자리임을 밝힌다. RF 축은 실물 재현과 가상물 렌더링을 **같은 축 위에** 놓는데, 광학 시스루가 이 축의 오른쪽 끝(직접 관찰된 현실=궁극의 충실도)에 놓인다는 지적이 날카롭다. EPM 축은 '바깥에서 들여다보기(exocentric)'에서 '그 안에 있기(egocentric)'까지의 범위다.

AR을 장치(시스루 HMD)가 아니라 **좌표(연속체 위의 위치)**로 정의함으로써, 모니터 기반 오버레이·비디오 시스루·태블릿 AR을 모두 같은 이론 틀에 넣었다. 또한 EWK 축에 대해 '세계 지식 부족은 AR의 한계가 아니라 강점'이라는 역발상을 제시했다 — 사람이 가상 포인터로 실측하면서 **세계 모델을 점진적으로 쌓아 간다**는 것. 조경 현장에서 측량 없이 시작해 관측할수록 모델이 채워지는 워크플로의 이론적 근거가 여기 있다.

연도 표기가 문헌마다 엇갈린다(저자 원고 1994, SPIE 색인 1995). 인용 시 반드시 둘을 병기해야 한다. 논문 스스로 '시각 디스플레이에 엄격히 한정'한다고 밝히며, RF 축은 '복잡한 주제의 심한 단순화이며 디스플레이 하드웨어·신호처리·렌더링 기법을 한데 뭉뚱그린 것'이라고 원문이 자인한다. 페이지 범위(282-292)는 통상 인용값이며 원문 대조로 확인하지 못했다.

### Ronald T. Azuma, 「A Survey of Augmented Reality」 — AR의 3조건
| 항목 | 내용 |
| --- | --- |
| 주체 | Ronald T. Azuma — Hughes Research Laboratories, Malibu, California (UNC Chapel Hill 박사) |
| 연도 | 게재 1997년 8월 (Presence: Teleoperators and Virtual Environments 6(4), pp.355-385) |
| 수치 | 전형적 종단간(end-to-end) 지연 100ms, 부하가 큰 네트워크 시스템은 250ms 이상; 지연 100ms + 머리 회전 50°/s → 각도 오차 5° → 팔 길이 68cm에서 정합 오차 약 60mm; 각도 오차를 0.5° 이하로 유지하려면 회전 50°/s에서 지연 10ms 이하 필요(60Hz 프레임버퍼 스캔아웃만으로 16.67ms 소모); 중심와(fovea) 원추세포 밀도 약 120개/도 → 약 0.5분각(arcminute) 간격; 보름달 시직경 약 0.5°, 팔 길이의 10센트 동전 1.2~2.0°; 지연 약 80ms 이하에서 예측(prediction)이 동적 오차를 최대 한 자릿수(order of magnitude) 감소, 관성센서 사용 시 예측 정확도 2~3배 향상; 광학 시스루의 실세계 광 |
| 출처 | Ronald T. Azuma, "A Survey of Augmented Reality", Presence: Teleoperators and Virtual Environments 6(4), August 1997, pp.355-385. 저자 공개 전문: https://www.ronaldazuma.com/papers/ARpresence.pdf (전문 대조 완료) |

오늘날 교과서에 실린 **AR의 표준 정의**가 이 논문에서 나왔다. 아주마는 당시 일부 연구자가 AR을 HMD 사용 시스템으로 한정하던 관행을 명시적으로 거부하고, 장치가 아니라 **성질** 세 가지로 AR을 정의했다 — ①실재와 가상의 결합, ②실시간 상호작용, ③3차원 정합. 이 정의의 힘은 무엇을 배제하는지가 분명하다는 데 있다. 「쥬라기 공원」 같은 영화는 실사와 가상을 3차원으로 완벽히 섞지만 상호작용이 없어 AR이 아니고, 생중계 화면 위의 2차원 자막 오버레이는 실시간이지만 3차원 정합이 아니어서 AR이 아니다. 반면 모니터 기반 인터페이스, 단안 시스템, 시스루 HMD는 모두 AR에 포함된다. 논문의 나머지 절반은 이 세 번째 조건, 곧 정합이 왜 그토록 어려운지를 **정량적으로** 해부한다.

'AR이란 무엇인가'를 장치 목록에서 조건 명제로 바꿨다. 그 결과 1997년에는 존재하지도 않던 스마트폰 AR·태블릿 AR·프로젝션 매핑이 이 정의에 그대로 포섭된다 — 30년을 버틴 정의다. 동시에 시스템 지연(latency)이 정합 오차의 **단일 최대 원인**이며 다른 모든 원인을 합친 것보다 크다는 것을 수치로 못 박아, AR 공학의 최우선 과제를 지정했다.

논문 스스로 '시각'을 전제로 서술한다 — 청각·촉각 AR은 1997년판 정의에서 명시적으로 다루지 않는다(2001년판에서 보완). 인용되는 성능 수치는 1990년대 중반 하드웨어 기준이므로 오늘날 기기에 그대로 적용하면 안 된다. 다만 '각도 오차를 0.5° 이하로'라는 **요구 조건** 쪽은 인간 시각계의 성질에서 나온 것이라 지금도 유효하다.

### Ronald Azuma, Yohan Baillot, Reinhold Behringer, Steven Feiner, Simon Julier & Blair MacIntyre, 「Recent Advances in Augmented Reality」 — 1997 정의의 갱신
| 항목 | 내용 |
| --- | --- |
| 주체 | Ronald Azuma(HRL Laboratories), Yohan Baillot·Simon Julier(NRL Virtual Reality Lab/ITT), Reinhold Behringer(Rockwell Scientific), Steven Feiner(Columbia University), Blair MacIntyre(Georgia Institute of Technology) |
| 연도 | 게재 2001년 11/12월 (IEEE Computer Graphics and Applications 21(6), pp.34-47) |
| 수치 | IEEE CG&A 21권 6호, 2001년 11/12월, pp.34-47; 1997년 서베이 이후 약 4년간의 진전을 정리; ARToolkit 무료 공개를 대표 사례로 언급 |
| 출처 | R. Azuma, Y. Baillot, R. Behringer, S. Feiner, S. Julier, B. MacIntyre, "Recent Advances in Augmented Reality", IEEE Computer Graphics and Applications 21(6), Nov./Dec. 2001, pp.34-47. 저자 공개 전문: https://www.ronaldazuma.com/papers/cga2001.pdf (전문 대조 완료) |

1997년 정의를 **네 군데 손본** 갱신판이다. 첫째, 세 조건의 표현이 바뀐다 — '실재 환경 안에서 실물과 가상물을 결합한다', '상호작용적으로, 그리고 실시간으로 동작한다', '실물과 가상물을 서로 정합(정렬)시킨다'. 특히 셋째 조건이 '3차원 정합'에서 '실물과 가상물을 서로 정렬'로 바뀌어 기준이 좌표계가 아니라 **물체 대 물체 관계**로 옮겨졌다. 둘째, HMD 같은 특정 디스플레이 기술에 한정하지 않는다고 재차 못 박는다. 셋째, **시각에 한정하지 않는다** — 청각·촉각·후각까지 잠재적으로 AR의 대상이다. 넷째, 실물을 지우는 일(mediated reality, diminished reality)도 AR의 부분집합으로 흡수한다. 그리고 이 네 번째가 조경에 결정적이다 — 원문이 든 예시가 바로 '어떤 장소에 서 있던 건물을 지우고 새 건물을 보여 주는 시각화'다.

1997년 정의는 '더하기'만 다뤘다. 2001년 정의는 **'빼기'를 AR 안으로 끌어들였다.** 조경 설계 검토에서 가장 자주 필요한 조작 — 기존 수목을 지우고, 콘크리트 옹벽을 지우고, 그 자리에 대안을 세우는 일 — 이 이 갱신으로 비로소 AR의 정의 안에 들어온다. 또 감각을 시각에서 전 감각으로 확장해, 소리(물소리·차량 소음 차폐)나 촉각까지 포함하는 환경 시뮬레이션의 이론적 자리를 열었다.

'모든 감각에 적용될 수 있다'는 것은 원문 표현대로 **잠재적(potentially)** 가능성이며, 2001년 시점에 시각 외 감각의 실증 사례는 사실상 없었다. 또 diminished reality를 AR 부분집합으로 규정한 것은 저자들의 입장이며, 이를 별개 범주로 두는 문헌도 있다(Mann의 mediated reality 계열).

### Richard Skarbez, Missie Smith & Mary C. Whitton, 「Revisiting Milgram and Kishino's Reality-Virtuality Continuum」 — 연속체는 불연속이다
| 항목 | 내용 |
| --- | --- |
| 주체 | Richard Skarbez(La Trobe University, 호주), Missie Smith(독립연구자, 디트로이트), Mary C. Whitton(University of North Carolina at Chapel Hill). 심사자에 Mark Billinghurst, Dieter Schmalstieg. |
| 연도 | 투고 2020년 12월 30일, 채택 2021년 3월 5일, 게재 2021년 3월 24일 (Frontiers in Virtual Reality 2:647997) |
| 수치 | Frontiers in Virtual Reality 2:647997, 총 15쪽; DOI 10.3389/frvir.2021.647997; 밀그램 논문 발표 후 '지난 25년'을 검토 대상 기간으로 설정; 1990년대 중반 연구실 표준 구성(헤드셋+고성능 워크스테이션+트래킹)의 총 시스템 비용이 10만(통화 단위는 PDF 추출에서 확인 못 함, 문맥상 미국 달러)을 쉽게 넘었다고 기술 |
| 출처 | R. Skarbez, M. Smith, M.C. Whitton, "Revisiting Milgram and Kishino's Reality-Virtuality Continuum", Frontiers in Virtual Reality 2:647997, 24 March 2021. DOI 10.3389/frvir.2021.647997. 오픈액세스 전문: https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2021.647997/pdf (전문 대조 완료) |

밀그램 연속체를 27년 만에 정면 재검토한 논문이며, 주장은 세 가지다. 첫째, **연속체는 사실 불연속이다.** 오른쪽 끝의 '완전한 가상현실'은 도달 불가능하다 — 기존 VR 기기는 시각·청각·촉각 같은 외수용감각(exteroceptive)만 자극할 뿐 고유수용감각·내장감각 같은 내수용감각(interoceptive)은 건드리지 못하기 때문이다. 아무리 정교한 식사 장면을 보여 줘도 사용자는 여전히 배가 고프다. 이 감각 충돌 때문에 '외부형 가상환경'과 「매트릭스」식 직접 뇌 자극 VR 사이에는 **건널 수 없는 틈**이 생긴다. 둘째, 그렇다면 현재의 VR도 전부 혼합현실이다 — 헤드셋 자체가 실세계에 놓인 실물이기 때문이다. 밀그램의 MR 정의에서 '하나의 디스플레이(display) 안에'를 '하나의 지각(percept) 안에'로 바꾸자는 제안이 여기서 나온다. 셋째, 3축 분류를 **EWK / 몰입(Immersion, IM) / 정합성(Coherence, CO)**으로 재편한다. RF와 EPM은 밀그램 자신이 비직교라고 인정했으므로 Slater식 '몰입=시스템이 지원하는 유효 행위의 집합'으로 통합하고, 그 대신 사용자 경험의 일관성을 재는 CO를 새로 세운다.

밀그램의 3축이 **디스플레이 장치**를 분류했다면, 이 재편은 **사용자 경험**을 분류한다. 조경 AR에 직접 쓰이는 개념이 CO의 내부/외부 구분이다 — VR에서는 가상물끼리의 내적 정합성이 문제지만, **AR에서 정합성은 주로 외적**이다. 즉 '가상 수목이 실제 지면 위에 앉아 있는가, 허공에 떠 있는가'가 곧 품질이다. 30년 전 '정합(registration)'이라 부르던 공학 문제가 여기서 '외적 정합성'이라는 경험 품질 지표로 번역된다.

논문 형식이 'Perspective'(관점 논문)이며 실증 연구가 아니다. 저자들 스스로 '우리의 MR 정의가 지나치게 포괄적이어서 혼란을 준다'는 비판이 가능함을 인정하고 반박을 제시한다. 또 EWK 축에 대해서는 밀그램 이후 후속 연구가 거의 없다고 지적하며, 이 부분은 여전히 미개척지로 남겨 둔다.

### Philipp A. Rauschnabel 외, 「What is XR? Towards a Framework for Augmented and Virtual Reality」 — 용어 혼란의 정리 시도
| 항목 | 내용 |
| --- | --- |
| 주체 | Philipp A. Rauschnabel 외 (Computers in Human Behavior 게재) |
| 연도 | 게재 2022년 |
| 수치 | Computers in Human Behavior 게재, DOI 10.1016/j.chb.2022.107289; 인용 약 917회(OpenAlex 기준, 본 조사 수집 시점) |
| 출처 | P.A. Rauschnabel et al., "What is XR? Towards a Framework for Augmented and Virtual Reality", Computers in Human Behavior, 2022. DOI 10.1016/j.chb.2022.107289 (초록 원문 대조; 본 조사 수집 코퍼스 judged.json 및 candidates.json 수록) |

AR·VR·MR·XR이라는 네 용어가 학계와 산업계에서 서로 다른 뜻으로 쓰이면서 생긴 개념 혼란을 정리하려는 시도다. 논문의 진단은 간명하다 — 용어들이 '현실을 어떻게 생성하거나 변형하는가'를 가리키는 데 쓰이지만 그 사용이 일관되지 않아 개념적 경계가 불분명해졌다는 것이다. 저자들은 XR을 'extended reality(확장현실)'의 약어로 쓰는 관행을 오해를 부르는 것으로 보고, X를 **미지수(unknown variable)**로 읽어 'xReality'라는 더 열린 접근을 제안한다. 즉 특정 기술 묶음을 가리키는 고정 명칭이 아니라, 아직 정해지지 않은 변수를 담는 틀로 쓰자는 것이다.

1994년 밀그램, 1997년 아주마의 정의는 연구 공동체 안에서 만들어졌다. 2020년대의 혼란은 다르다 — 제조사(마이크로소프트·인텔 등)가 마케팅 목적으로 서로 다른 정의를 유포하면서 생긴 혼란이다. 이 논문은 **산업 용어와 학술 용어가 어긋난 상태**를 정면으로 다룬 드문 사례이며, 조경 실무자가 제품 홍보 문구의 'MR'과 논문의 'MR'을 같은 것으로 읽어서는 안 되는 이유를 제공한다.

본문 전문을 확보하지 못해 초록만 원문 대조했다. 저자 전체 명단·정확한 권/호/페이지·저자 소속을 이 조사에서 확인하지 못했다. 제안된 'xReality' 프레임의 구체적 축 구성도 초록만으로는 알 수 없다.

### Maximilian Speicher, Brian D. Hall & Michael Nebeling, 「What is Mixed Reality?」 — MR 정의의 실증적 조사
| 항목 | 내용 |
| --- | --- |
| 주체 | Maximilian Speicher, Brian D. Hall, Michael Nebeling (University of Michigan 계열; CHI 2019 발표) |
| 연도 | 발표·게재 2019년 (ACM CHI Conference on Human Factors in Computing Systems) |
| 수치 | 본 조사에서 확인된 정량 수치 없음(전문 미확보) |
| 출처 | M. Speicher, B.D. Hall, M. Nebeling, "What is Mixed Reality?", Proc. CHI 2019, ACM. DOI 10.1145/3290605.3300767. — 단, 본 조사에서는 전문을 확보하지 못했고, 위 인용문과 'MR의 네 가지 상충 정의' 요약은 모두 Skarbez, Smith & Whitton (2021), Frontiers in Virtual Reality 2:647997 본문의 인용을 통해 대조했다(2차 출처). |

'혼합현실'이라는 말이 실제로 어떻게 쓰이는지를 문헌 검토와 전문가 인터뷰로 조사한 논문이다. 결과는 통일된 정의가 없다는 것이었다. Skarbez 등이 이 논문을 인용해 요약한 바에 따르면, MR은 ①AR과 VR의 합, ②AR의 동의어, ③AR의 '더 강한' 판본, ④밀그램·키시노가 정의한 그대로 — 이렇게 서로 충돌하는 방식으로 정의되어 왔다. 이 논문이 남긴 가장 유명한 문장은 인터뷰 대상자의 항변이다 — '콘솔 비디오게임이 MR이라면, 그럼 전부 다 MR이다.' 정의를 넓히면 변별력을 잃고, 좁히면 실제 시스템을 못 담는다는 딜레마를 압축한 말이다.

정의를 **규범적으로 선언**하는 대신(밀그램·아주마의 방식) **경험적으로 조사**했다는 점이 방법론적 전환이다. 정의는 논문이 정하는 것이 아니라 공동체가 쓰는 것이라는 관점이며, 2020년대 XR 용어 논쟁의 출발점이 되었다.

**2차 출처에 의존한 항목이다.** 원 논문 전문을 읽지 못했으므로, 검토한 논문 편수·인터뷰한 전문가 수·제안한 프레임워크의 구체적 구성은 이 조사에서 확인하지 못했다. 책에 쓸 때는 반드시 ACM DL 원문을 확보해 재확인해야 한다. 저자 소속도 확정하지 못했다.

#### 검증에서 잡힌 정정
- [틀림] Skarbez, Smith & Whitton (2021) '총 15쪽' → 실제 8쪽. Frontiers 공식 PDF(https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2021.647997/pdf)의 pdfinfo 결과 Pages: 8이고, 'March 2021 \| Volume 2 \| Article 647997' 하단 러닝풋도 정확히 8개다. Frontiers는 권내 연속 페이지를 부여하지 않으므로 '15쪽'의 근거가 없다. 15는 오히려 같은 목록의 Speicher, Hall & Nebeling, 'What is Mixed Reality?', CHI 2019의 pp.1-15(OpenAlex biblio: first_page 1, last_page 15)와 일치하므로 두 항목이 뒤섞인 것으로 보인다.
- [틀림/불필요한 유보] Skarbez 2021 '총 시스템 비용이 10만(통화 단위는 PDF 추출에서 확인 못 함, 문맥상 미국 달러)' → 원문은 통화 단위를 명시한다. 4.2절 'Total system cost could easily exceed 100,000' 다음 단 첫 줄이 'USD. Except for demonstration programs...'로 이어지므로 원문 문장은 'Total system cost could easily exceed 100,000 USD.'다. 2단 조판 때문에 추출 시 'USD'가 다음 단으로 분리된 것일 뿐이며, '확인 못 함'으로 남길 사안이 아니다. 정정: 100,000 USD(원문 명시).
- [틀림] Milgram, Takemura, Utsumi & Kishino (SPIE 2351) 저자 소개의 'Haruo Takemura(현 NAIST)' → 현재 소속은 오사카대학(The University of Osaka)이다. Crossref 저자 소속 필드 실조회 결과 2021~2025년 논문 전부가 'Graduate School of Information Science and Technology, Osaka University', 'Cybermedia Center, Osaka University, 1-32 Machikaneyama, Toyonaka, Osaka 560-0043', 'D3 Center, Osaka University', 'The University of Osaka'로 기재돼 있다. NAIST는 1990년대 후반~2001년 소속이며 '현재'가 아니다. (SPIE 논문 집필 당시 ATR 소속이라는 기술 자체는 맞다.)
- [검증 방법 오기] Sutherland 1968에 대한 '스캔본 전문 대조: https://www.cise.ufl.edu/~lok/teaching/ve-s07/papers/sutherland-headmount.pdf' → 해당 PDF는 Acrobat 5.0 Scan Plug-in으로 만든 순수 이미지 스캔이라 텍스트층이 없다(pdftotext 산출물 8바이트, 본 조사 스크래치패드의 sut68.txt가 그 증거). 통상적 '전문 대조'가 성립할 수 없는 파일이다. 본 검증에서 8쪽 전부를 Apple Vision OCR로 재추출해 확인한 결과 기재된 18개 수치는 전부 원문과 일치했다(시야각 40°, 가상상 18인치, CRT 1/2인치 사각·공칭 0.6 mil 스폿, 작업체적 지름 6피트×높이 3피트·틸트 약 40°, 목표 분해능 1/100인치·회전 1/10,000, 요구 정확도 1/10인치, 핀쿠션 왜곡 'about three percent'→3/10인치 오차, 송신기 3개 37/3
- [확인 못 함] Milgram & Kishino (1994, IEICE E77-D No.12) '인용 약 4,635회(OpenAlex)' → 검증 불가. 이 논문은 DOI가 없어 OpenAlex DOI 조회가 불가능하고, 제목 검색은 OpenAlex 일일 무료 쿼터 소진(HTTP 429, Retry-After 약 10시간)으로 실패했다. Semantic Scholar도 429. 참고로 같은 세션에서 DOI로 조회에 성공한 나머지 인용수는 전부 보고서와 정확히 일치했다 — KARMA 1993 = 969, SPIE 2351 = 2,367, Rauschnabel 2022 = 917. 따라서 4,635도 같은 시점 값일 개연성이 높으나 독립 확인은 못 했다.
- [누락/과소보고] Caudell & Mizell (1992) 항목에 인용수가 빠져 있다. OpenAlex DOI 10.1109/HICSS.1992.183317 조회 결과 cited_by_count = 1,463, biblio first_page 659 / last_page '669 vol.2'로 보고서의 쪽수 기재는 맞다. 'AR 용어의 탄생' 논문인데 다른 항목과 달리 인용수만 비어 있으므로 1,463회를 채워 넣는 편이 정합적이다.
- [과소보고] Speicher, Hall & Nebeling (2019) '본 조사에서 확인된 정량 수치 없음(전문 미확보)' → 전문이 없어도 서지 정량값은 확인된다. OpenAlex DOI 10.1145/3290605.3300767 기준 pp.1-15(15쪽), cited_by_count = 691, 발행연도 2019. 다만 저자 소속 'University of Michigan 계열'은 ACM DL이 403을 반환해 본 검증에서도 1차 확인하지 못했다.
- [사소] Azuma et al. (2001) 항목의 'ARToolkit' 표기는 논문 본문 표기를 그대로 따른 것이어서 대조상 문제는 없으나, 프로젝트 공식 명칭은 ARToolKit(K 대문자)이다. 본문 실제 문장은 'A software toolkit (the ARToolkit) for rapidly building AR applications is now freely available at http://www.hitl.washington.edu/research/shared_space/'로, '무료 공개' 기술은 정확하다. 쪽수 34-47도 본문 페이지 마커 34~47 전부 확인됨.
- [연도 오류] Milgram, Takemura, Utsumi & Kishino 논문을 IEICE 항목에서 '1995 SPIE 논문'으로 지칭하고 '1994 IEICE 6부류 → 1995 SPIE 7부류 확장'이라는 선후 서사를 만든 것은 틀렸다. 올바른 값: 1994년. 근거 — (a) SPIE 논문 자신의 참고문헌 1이 'H. Das (ed). Telemanipulator and Telepresence Technologies, SPIE Vol. 2351, Bellingham, WA, 1994'로 수록 권을 1994년으로 명기, (b) 같은 논문 참고문헌 2가 IEICE 논문을 'Dec. 1994'로 인용(= 두 논문이 동일 연도의 자매 논문), (c) 저자 공개 원고 표지 '(c) Copyright 1994', (d) Skarbez 외(2021) 본문 'appeared later that year' 및 서지 'Milgram, P., Takemura, H., Utsumi, A., a
- [쪽수 오류] Skarbez, Smith & Whitton (2021), Frontiers in Virtual Reality 2:647997 '총 15쪽' → 올바른 값: 8쪽. Frontiers 공식 OA PDF의 마지막 쪽 푸터가 'Frontiers in Virtual Reality \| www.frontiersin.org  8  March 2021 \| Volume 2 \| Article 647997'이며 pdfinfo도 Pages: 8. (덧붙여 논문 유형은 일반 원저가 아니라 'PERSPECTIVE'다.)
- [선후관계 오류] Caudell & Mizell (1992)을 "'augmented reality' 용어의 탄생 (발표·수록 1992년)"으로 규정한 것은 출판 연도와 창안 연도를 혼동한 것이다. 올바른 값: 용어 창안 1990년(보잉 재직 중 Thomas P. Caudell), 최초 학술 출판 1992년 1월 7일(HICSS-25, Kauai). 근거 — Wikipedia 'Augmented reality' 연표 '1990: The term augmented reality is attributed to Thomas P. Caudell, a former Boeing researcher'(출처 Lee, TechTrends 56(2), 2012, DOI 10.1007/s11528-012-0559-3); Semantic Scholar publicationDate 1992-01-07.
- [관계 규정 오류] Azuma 외 (2001)을 '1997 정의의 갱신'으로 규정한 것은 틀렸다. 올바른 값: 갱신이 아니라 보완(complement). 2001 논문 원문 'Our goal here is to complement, rather than replace, the original survey by presenting representative examples of the new advances.' 제시된 3조건도 실질 동일 — 1997: 'Combines real and virtual / Interactive in real time / Registered in 3-D'; 2001: 'combines real and virtual objects in a real environment / runs interactively, and in real time / registers (aligns) real and virtual objects with each other'. 'HMD
- [출처 연대 착오] KARMA(1993) 인용문의 출처로 든 컬럼비아대 프로젝트 페이지(graphics.cs.columbia.edu/projects/karma/karma.html)는 1993년 7월 CACM 논문 본문이 아니다. 근거 — 해당 페이지 감사문에 ONR 계약 N00014-94-1-0564(1994년 이후)와 NSF CDA-92-23009가 기재되어 있어 1993년 7월 시점 문서일 수 없고, 정식 서지도 '[Feiner, MacIntyre, and Seligmann 93]'로만 표기되어 있으며, AR의 정식 정의문이 없다. 또 그 페이지는 AR 개념을 'This idea, introduced by Ivan Sutherland's pioneering work on head-mounted displays, is often referred to as augmented reality'라 하여 Caudell(1990/1992)이 아닌 Sutherland에게 귀속한다. 1993년 
- [귀속 부정확] 'EWK/RF/EPM 축의 상세 정의'를 SPIE 논문에만 배정한 것은 부정확하다. 올바른 값: IEICE 1994 본문에 이미 4.1 Extent of World Knowledge, 4.2 Reproduction Fidelity, 4.3 Extent of Presence Metaphor 절과 Figure 3/4/5가 모두 들어 있다(약어 EWK·RF·EPM도 IEICE에서 이미 사용).
- [불필요한 미확인 표시] Skarbez 2021의 '총 시스템 비용 10만(통화 단위 확인 못 함)'은 확정 가능하다. 올바른 값: 미국 달러(USD). 원문 문장이 페이지 경계에서 끊겨 4쪽 끝 'Total system cost could easily exceed 100,000' 다음 5쪽 첫 단어가 'USD.'다.
- [축약 왜곡] Azuma 1997의 '부하가 큰 네트워크 시스템은 250ms 이상'은 원문 3개 조건을 1개로 합친 것이다. 올바른 값: 'Delays of 250 ms or more can exist on slow, heavily loaded, or networked systems'(느리거나, 부하가 크거나, 네트워크 기반인 시스템).
- [연대 표현 주의] Skarbez 2021의 '지난 25년'은 논문 원문 표현('over the last 25 years', 'In the succeeding quarter century')과 일치하나, Milgram & Kishino 1994 → 2021의 실제 경과는 27년이다. 조사 결과가 이를 밀그램 발표 후 실경과로 오독하지 않도록 구분 필요.
- [검증 불가] Caudell & Mizell (1992) '논문에 정량 사양은 제시되지 않음'은 확인 못 했다 — IEEE Xplore 전문이 유료이고 Semantic Scholar도 초록을 elide 처리(openAccessPdf status: CLOSED)했다.
- [검증 불가] Milgram & Kishino (1994) IEICE '인용 약 4,635회(OpenAlex)'는 확인 못 했다 — OpenAlex 무API키 일일 공용 쿼터가 소진되어 해당 레코드를 조회하지 못했다. 다만 같은 세션에서 조회에 성공한 나머지 3건은 조사 결과와 정확히 일치했다(KARMA 969, Milgram 외 SPIE 2,367, Rauschnabel 외 917).
- [누락, 선후관계] definition 축 연표가 1968 → 1992(Caudell) → 1993(KARMA) → 1994(Milgram)로 이어지면서 1992년 Louis Rosenberg의 Virtual Fixtures(USAF Armstrong Laboratory) — 최초의 실동작 몰입형 AR 시스템 중 하나로 널리 인용됨 — 가 빠져 있다. '기술적 점프' 서술을 보강하려면 같은 1992년 안의 선후로 포함해야 한다.
- [확정 오류] Skarbez, Smith & Whitton (2021) '총 15쪽' → 실제 8쪽. Frontiers 공식 PDF(https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2021.647997/pdf)는 pdfinfo 기준 Pages: 8이고, 본문 각 쪽 하단 푸터가 'Frontiers in Virtual Reality \| www.frontiersin.org  1 … 8  March 2021 \| Volume 2 \| Article 647997'로 1~8까지만 이어진다. '15쪽'은 아마 같은 목록의 Speicher, Hall & Nebeling(CHI 2019) 서지(Crossref page: 1-15)와 혼동된 것으로 보인다.
- [근거 없음 → 정정] Skarbez 2021의 '10만(통화 단위는 PDF 추출에서 확인 못 함, 문맥상 미국 달러)' → 통화 단위는 PDF에 실제로 명시되어 있다. 원문은 'Total system cost could easily exceed 100,000 USD.'이며, 'USD'가 단 넘김 직후(추출 텍스트 315행)에 나와 추출 시 끊겼을 뿐이다. '확인 못 함'이 아니라 'USD로 확인됨'이 맞다. 또한 이 서술의 대상은 '1990년대 중반(in the mid-1990s)' 연구실 표준 구성(헤드 착용 디스플레이+고성능 워크스테이션+트래킹 시스템)이 맞다.
- [검증 불가 + 과잉 단정] Caudell & Mizell (1992) '논문에 정량 사양은 제시되지 않음(설계·프로토타이핑 단계 보고)' → 이 진술은 초록만 보고 본문 전체의 부재를 단정한 것으로 논리적으로 성립하지 않는다. 본 검증에서도 전문을 열 수 없었다(IEEE Xplore 접근 차단, Semantic Scholar openAccessPdf status: CLOSED). 따라서 '정량 사양 없음'은 사실 주장으로 쓰면 안 되고 '본문 미확보로 확인 불가'로 표기해야 한다. 서지 자체(HICSS-25, 1992, pp.659-669 vol.2, DOI 10.1109/HICSS.1992.183317)는 Crossref·Semantic Scholar에서 모두 확인됨.
- [오늘 재확인 실패] Milgram & Kishino (1994) '인용 약 4,635회(OpenAlex 기준)' → 오늘 OpenAlex API 일일 무료 예산이 해당 IP에서 소진되어(429 Rate limit exceeded, 자정 UTC 리셋) 재확인하지 못했다. 다만 같은 목록의 OpenAlex 인용수 3건(Feiner 969, Milgram SPIE 2367, Rauschnabel 917)이 오늘 조회값과 소수점 없이 정확히 일치했으므로 4,635도 같은 시점의 OpenAlex 값일 개연성은 높다. '미확인'으로 표기 권장.
- [출처 링크 상태] Milgram 계열 2건의 '저자 공개 전문' 원 URL(http://etclab.mie.utoronto.ca/people/paul_dir/IEICE94/ieice.html, .../SPIE94/SPIE94.full.html)은 현재 죽어 있다(connect ECONNREFUSED 128.100.48.96:443). 조사문이 '웹아카이브 보존본'이라고 밝힌 점은 정확하나, 재현 가능한 인용을 위해서는 라이브 URL이 아니라 Wayback 스냅샷 URL(http://web.archive.org/web/2017id_/http://etclab.mie.utoronto.ca/...)을 출처로 적어야 한다. 아카이브본은 정상 취득되어 전문 대조에 사용했다.
- [미검증 추정] Sutherland (1965) '논문 분량 3쪽' → 페이지 범위 506-508에서 역산한 추정이며 원본으로 확인되지 않았다. 조사문이 '전문 대조 완료'라고 한 worrydream PDF는 원 프로시딩 스캔이 아니라 2007년에 재입력·재조판된 2쪽짜리 전사본이다(pdfinfo: Pages 2, Author 'Oliver Staadt', Creator 'Firefox', Producer 'Mac OS X 10.4.9 Quartz PDFContext'). 내용·참고문헌 2건·소속은 이 전사본으로 확인되지만, 원본 조판 분량은 이 자료로 확정할 수 없다.
- [표기 정밀도, 오류 아님] Sutherland (1968) '상하 틸트 약 ±40°' → 원문은 두 군데에서 다르게 표현한다. 서론은 'can tilt his head up or down thirty or forty degrees', 헤드 포지션 센서 절은 'may tilt his head up or down approximately forty degrees'. '약 ±40°'는 후자에 부합하나 서론의 '30~40도' 표현을 함께 적는 편이 정확하다.
- [표기 정밀도, 오류 아님] Milgram & Kishino 1994 저널명: 저자 공개 전문 머리말에는 'IEICE Transactions on Information Systems'로 적혀 있고, 조사문이 쓴 'IEICE Transactions on Information and Systems'가 공식 명칭이다(둘 다 같은 저널). 또 선행 분류 중 'Naimark 1991'은 원문에서 'Naimark (1991a,b)' 두 건으로 인용된다.

## display — AR 디스플레이 광학(결합기·도파관·광엔진)의 계보
항목 12개 · 검증 정정 지적 38건


### 광학 시스루(optical see-through) vs 비디오 시스루(video see-through) — Azuma 서베이의 원리 구분
| 항목 | 내용 |
| --- | --- |
| 주체 | Ronald T. Azuma, Hughes Research Laboratories |
| 연도 | 1997 (Presence 6권 4호, 355~385쪽 게재) |
| 수치 | 결합기 투과율 예: Holmgren(1992) HMD는 실세계 입사광의 약 30%만 투과 / 60Hz 모니터의 프레임 시간 16.67ms / AR의 세 조건 3가지 |
| 출처 | Azuma, R. T. (1997). A Survey of Augmented Reality. Presence: Teleoperators and Virtual Environments, 6(4), 355-385. https://www.ronaldazuma.com/papers/ARpresence.pdf (본문 3절 전문 추출·확인) |

AR 디스플레이는 실세계 빛과 가상 이미지를 어떻게 합치느냐에 따라 두 계열로 갈린다. 광학 시스루는 눈앞에 부분 투과·부분 반사하는 **결합기(optical combiner)**를 두고, 사용자는 결합기를 직접 통과한 실세계 빛을 보면서 동시에 결합기에 반사된 소형 디스플레이의 상을 겹쳐 본다. 실세계 빛의 지연은 사실상 0(수 나노초)이고 실세계 해상도는 눈의 해상도 그대로다. 비디오 시스루는 밀폐형 HMD에 카메라를 달아 실세계를 촬영하고, 그 영상과 가상 이미지를 디지털로 합성한 뒤 눈앞 패널에 띄운다. 실세계와 가상이 모두 화소로 환원되므로 픽셀 단위 가림(occlusion) 처리가 가능한 대신, 실세계 해상도·밝기·지연이 전부 디스플레이 성능에 묶인다.

'AR 디스플레이'라는 것을 기술 목록이 아니라 **결합 방식의 선택 문제**로 정식화했다. 이후 30년의 모든 기기가 이 두 갈래 중 하나에 속한다. 특히 '광학 시스루는 가상 물체가 실물을 완전히 가릴 수 없다'는 지적은 지금도 풀리지 않았고, 이것이 비전 프로가 비디오 시스루를 택한 직접적 이유다.

1997년 시점이라 도파관(waveguide) 결합기는 논의에 없다. 당시의 결합기는 하프미러(반투명 거울) 계열뿐이다. 또한 Azuma 본인이 '가림 문제를 해결한 광학 시스루 HMD는 존재하지 않는다'고 적었는데, 2026년 현재도 매직리프 2의 세그먼트 디밍이 부분적 해결에 그친다.

### 자유공간 결합기 — 하프미러(half-mirror)와 버드배스(birdbath)
| 항목 | 내용 |
| --- | --- |
| 주체 | 원리 계보는 Ivan Sutherland(1968) → 항공 HUD → 구글글래스·엑스리얼. 효율 수치는 Xiong, Hsiang, He, Zhan & Wu (2021) 리뷰 |
| 연도 | 1968년 서덜랜드 HMD 이래의 고전 방식 / 상용화는 구글글래스 2013, 엑스리얼 계열 2020년대 |
| 수치 | 하프미러 투과율 50% 가정 + 기타 광학계 효율 50% → 결합기 효율 약 4,200 nit/lm / 전통 기하광학 AR의 전형적 성능: 대각 시야각 약 60도, 아이박스 8mm / 반사형 결합기의 광효율 최대 50%(회절 격자는 10% 미만) |
| 출처 | Xiong, J., Hsiang, E.-L., He, Z., Zhan, T., Wu, S.-T. (2021). Augmented reality and virtual reality displays: emerging technologies and future perspectives. Light: Science & Applications, 10, 216. https://pmc.ncbi.nlm.nih.gov/articles/PMC8546092/ · 반사/회절 효율 비교는 iScience 22(8), 101397 (2020) Table 2 |

가장 단순한 결합기다. 45도로 기울인 반투명 거울(빔스플리터) 한 장을 눈앞에 두고, 위나 옆에 둔 마이크로 디스플레이의 빛을 눈으로 꺾어 보낸다. **버드배스**는 여기에 오목 반사경을 더해 광로를 접은 변형으로, 빔스플리터에서 한 번 꺾은 빛을 오목거울에서 반사시켜 다시 빔스플리터를 통과시킨다. 광로를 접기 때문에 두께가 줄고, 곡면 거울이 확대와 수차 보정을 동시에 맡아 화질이 좋다. 그러나 빛이 빔스플리터를 두 번 지나므로 이론상 75%가 버려지고, 실세계 투과율도 크게 떨어진다.

도약이라기보다 **기준선**이다. 설계가 단순하고 화질이 좋아 지금도 엑스리얼 같은 '디스플레이 안경'이 쓴다. 도파관이 등장한 이유는 오직 하나 — 버드배스는 부피가 눈앞으로 튀어나와 안경 형태가 안 되기 때문이다.

두께를 줄일 수 없다. 눈과 결합기 사이에 오목거울 초점거리만큼의 공간이 필요해 '고글'을 벗어나지 못한다. 또한 버드배스는 실세계 투과율이 보통 25~50%로 낮아 실외에서는 선글라스처럼 어둡다.

### Microsoft HoloLens 1 — LCoS 광엔진 + 회절 도파관의 첫 대량 상용화
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft (광학: 노키아에서 인수한 회절 도파관 특허 계열) |
| 연도 | 2015년 1월 발표 / 2016년 3월 30일 개발자판 출하 |
| 수치 | 시야각 30도(수평)×17.5도(수직), 대각 약 34도 / 양안 합계 230만 화소, 한쪽 눈 1268×720 / 각해상도 약 1.46 각분/화소 = 약 41 PPD / 무게 579g / 가격 3,000달러(개발자판), 5,000달러(상용판) / 초점 고정 약 2m |
| 출처 | Karl Guttag, KGOnTech, 'Near Eye AR/VR and HUD Metrics for Resolution, FOV, Brightness and Eyebox/Pupil' (2016-10-13) 및 'HoloLens 2 Display Evaluation Part 2' (2020-07-08); 무게·가격·출하일은 Wikipedia 'Microsoft HoloLens' |

LCoS(실리콘 액정) 마이크로 디스플레이가 만든 상을 **회절 격자(diffraction grating)**로 얇은 유리판 안에 꺾어 넣는다. 빛은 유리판 내부에서 전반사(TIR)로 옆으로 이동하다가, 눈앞의 출력 격자를 만나 다시 꺾여 밖으로 나온다. 핵심은 격자가 빛을 여러 갈래로 복제하며 퍼뜨리는 **출사동 확장(exit pupil expansion, EPE)**이다. 이 덕분에 작은 광엔진으로도 눈이 조금 움직여도 상이 보이는 아이박스를 만든다. 색마다 회절각이 다르므로 RGB를 나눠 담을 도파관 판이 여러 장 필요하다.

결합기를 **눈앞에서 유리판 옆으로 치웠다.** 하프미러·버드배스는 광학 부피가 시선 방향으로 쌓이지만, 도파관은 빛을 옆에서 끌고 와 얇은 판 한 장으로 끝낸다. AR 기기가 '안경'을 지향할 수 있게 된 분기점이다.

시야각 30×17.5도는 엽서를 팔 길이에 든 정도다. 시야가 잘려 가상 물체가 화면 경계에서 싹둑 잘린다. 초점이 2m에 고정돼 수렴-조절 불일치(VAC)가 생긴다.

### Microsoft HoloLens 2 — MEMS 레이저 빔 스캐닝(LBS) 도입
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft (LBS 기술은 MicroVision에서 라이선스, 핵심 인력도 영입) |
| 연도 | 2019년 2월 발표(MWC19) / 2019년 11월 7일 출시 / 2024년 단종, 소프트웨어 지원은 2027년 12월 31일까지 |
| 수치 | 마이크로소프트 공식: '2k 3:2 광엔진', 홀로그래픽 밀도 '2.5k radiants 초과(라디안당 광점 수)', 무게 566g, 스냅드래곤 850, 가격 3,500달러 / 시야각 대각 52도(계산상 수평 41.6도×수직 31.2도) / 빠른축 MEMS 거울 54,000 사이클/초, 60Hz에서 프레임당 900사이클 중 활성 표시 영역은 약 720사이클 / 마이크로소프트 주장 47 PPD vs 측정 20 PPD 미만(약 3 각분/화소) / 화면 중앙 실측 주사선 854줄, 유효 해상도는 600줄 수준 |
| 출처 | Microsoft Learn, 'HoloLens 2 hardware' (공식 사양) https://learn.microsoft.com/en-us/hololens/hololens2-hardware · Karl Guttag, KGOnTech, 'HoloLens 2 First Impressions: the LBS resolution math fails' (2019-02-27), 'HoloLens 2 Display Evaluation Part 2' (2020-07-08), 'Microsoft HoloLens reportedly in trouble' (2022-02-04) |

패널 대신 **레이저 두 줄기와 흔들리는 미세 거울(MEMS mirror)**로 상을 그린다. 빠른 축 거울이 초당 5만 4천 번 좌우로 흔들리며 한 줄씩 훑고, 느린 축 거울이 위아래로 움직여 화면을 채운다. 화소가 물리적으로 존재하지 않고 레이저의 밝기를 시간축으로 변조해 만들어낸다. 레이저는 파장이 좁아 회절 도파관의 색분산 문제에 유리하고, 광엔진 크기가 극히 작으며 광효율(40 lm/W)이 모든 방식 중 가장 높다. 마이크로소프트는 이 방식으로 시야각을 대각 34도에서 52도로 넓혔다.

광엔진 방식 자체를 바꾼 유일한 상용 사례다. 시야각은 실제로 넓어졌다. 그러나 **해상도는 홀로렌즈 1보다 후퇴**했다 — 스캐닝은 시야각을 넓히면 같은 스캔 횟수를 더 넓게 펴는 것이라 화소밀도가 그대로 희석된다. AR에서 '시야각과 화소밀도는 맞바꾸는 관계'라는 사실이 가장 노골적으로 드러난 사건이다.

마이크로소프트는 시야각을 '면적 기준'으로 비교해 '홀로렌즈 1의 두 배'라 발표했는데, 이는 선형 배율을 제곱한 수치다. 선형으로는 약 1.5배다. 또한 레이저 스페클과 인터레이스 주사로 텍스트 가독성이 나빴다. 마이크로소프트 공식 자료는 화소 수를 직접 밝히지 않는다('2k 3:2 광엔진'이라는 모호한 표현) — 이 점이 위 논쟁의 근원이다.

### Magic Leap One — 다중 도파관 2초점면(multi-focal) 구조
| 항목 | 내용 |
| --- | --- |
| 주체 | Magic Leap (LCoS 광엔진, 6층 회절 도파관) |
| 연도 | 2017년 12월 공개 / 2018년 8월 출시 |
| 수치 | LCoS 패널 1280×960(4:3), 시야각 약 50도 / 도파관 6층(RGB×초점면 2) / LED 6개 + 입력 격자 6개 / 실측 밝기 약 210 nit(Guttag, 2018) |
| 출처 | Karl Guttag, KGOnTech, 'iFixit's Magic Leap One Teardown Confirms KGOnTech's Analysis from November 2016' (2018-08-23) 및 'Magic Leap 2 for Enterprise' (2021-10-13) |

수렴-조절 불일치(VAC)를 광학적으로 풀려 한 유일한 상용 시도다. 도파관 판을 여섯 장 쌓았다 — RGB 3색 × 초점면 2개. 즉 **같은 색을 서로 다른 초점거리로 내보내는 도파관 쌍**을 만들어, 가까운 물체는 가까운 초점면에, 먼 물체는 먼 초점면에 그린다. 눈이 실제로 초점을 바꿔야 선명해지므로 수렴과 조절이 어긋나는 피로가 줄어든다. 입력 격자도 6개, LED도 6개(RGB 두 세트)였다.

AR 광학이 '평면 이미지를 어디에 띄우는가'를 넘어 **깊이를 광학적으로 구현**하려 한 첫 상용 도전이다. 그러나 초점면 2개로는 연속적 깊이를 흉내 낼 수 없었고, 판이 여섯 장이면 두께·무게·투과율·비용이 모두 무너진다. 매직리프 2에서 이 구조는 폐기됐다.

초점면 2개는 사실상 '가까움/멂' 두 단계일 뿐이다. 필드 시퀀셜 방식이라 머리나 눈을 움직이면 흰색이 적·녹·청으로 갈라지는 색분리 아티팩트가 보였다. 실측 210 nit는 실내에서도 어두운 수준이다.

### Magic Leap 2 — 고굴절률(n=2.0) 유리 3층 도파관 + 세그먼트 디밍
| 항목 | 내용 |
| --- | --- |
| 주체 | Magic Leap (LCoS 패널은 옴니비전으로 추정) |
| 연도 | 2021년 10월 예고 / 2022년 9월 출시 |
| 수치 | 활성 표시 영역 한쪽 눈 1440×1760(그중 96×96은 눈 정렬용) / 시야각 약 70도 / 최대 밝기 2,000 nit / 도파관 3층(R·G·B 각 1장) / 유리 굴절률 n=2.0 / 실세계 투과율 최선 22%(실세계 빛의 78%를 차단) / 초점면 1개 |
| 출처 | Karl Guttag, KGOnTech, 'Magic Leap 2 at SPIE AR/VR/MR 2022' (2022-01-31) |

초점면을 하나로 줄이는 대신 **시야각을 50도에서 70도로 키웠다.** 이를 위해 굴절률 n=2.0의 고굴절 유리를 썼다 — 굴절률이 높을수록 유리 안에서 전반사로 가둘 수 있는 각도 범위가 넓어지고, 그 각도 범위가 곧 시야각이기 때문이다. 도파관은 RGB 각 1장씩 3층이다. 또 하나의 시도는 **세그먼트 디밍**이다. 액정 셀로 실세계 빛을 구역별로 어둡게 만들어, 가상 물체가 놓인 자리만 실세계를 가린다. Azuma가 1997년에 '광학 시스루로는 불가능하다'고 적은 가림 문제에 대한 부분적 답이다.

'시야각을 넓히려면 굴절률을 올려라'는 도파관 광학의 제1 법칙을 상용 제품으로 증명했다. 동시에 그 대가도 드러냈다 — 실세계 투과율이 22%로 떨어져 기기가 사실상 짙은 선글라스가 된다.

화소밀도는 매직리프 1과 거의 같다 — 시야각 면적과 화소 수가 함께 두 배가 됐기 때문이다. 투과율 22%는 실외 조경 현장에서 치명적이다. 디밍은 '소프트 에지'라 경계가 뿌옇게 번진다. 시야각의 수평/수직 정확한 분해값은 공식 공개 자료에서 확인하지 못했다.

### Lumus 반사형(기하학적) 도파관 — 회절 대신 부분반사 거울 배열
| 항목 | 내용 |
| --- | --- |
| 주체 | Lumus (이스라엘) |
| 연도 | Maximus 2021년 발표 / Z-Lens 2023년 발표 |
| 수치 | Maximus: 대각 시야각 50도, 1440×1440, 밝기 3,000 nit/W(LED 기준) 이상, 아이박스 12×12mm, 도파관 두께 1.7mm / Z-Lens: 대각 50도, 1024×1024, 1,400 nit/W 이상, 아이박스 11×11mm, 두께 1.3mm / 실세계 투과율 80% 초과 / 반사형 결합기 광효율 최대 50% vs 회절 격자 10% 미만 |
| 출처 | Lumus 공식 제품 페이지 https://lumus.com/products/ · 반사 vs 회절 효율 비교는 iScience 22(8), 101397 (2020) Table 2 |

도파관 안에 격자를 새기는 대신, **유리 내부에 부분반사 거울을 여러 장 비스듬히 심어 놓는다.** 빛이 전반사로 이동하다가 이 거울들을 차례로 만나면 일부씩 밖으로 새어 나오며 출사동이 확장된다. 회절이 아니라 반사이므로 파장 의존성이 없다 — 즉 RGB를 한 장에 다 담을 수 있고, 무지개 아티팩트(주변광이 격자에 회절돼 생기는 색번짐)가 원리적으로 발생하지 않는다. 무엇보다 광효율이 회절 방식보다 한 자릿수 높다.

회절 도파관이 업계 주류가 된 뒤에도 **효율에서는 반사형이 5~10배 앞선다**는 사실을 상용 수치로 보여줬다. 밝기 = 배터리인 안경형 기기에서 이 차이가 결국 결정적이었고, 2025년 메타 레이밴 디스플레이가 루머스 방식을 채택했다.

거울 배열을 유리 안에 미크론 정밀도로 심고 코팅해야 해서 제조 난이도와 단가가 높다. 시야각은 50도에서 멈춰 있다 — 굴절률로 시야각을 밀어붙이는 회절/SiC 계열의 70도에 미치지 못한다.

### Meta Ray-Ban Display — 반사형 도파관의 첫 대중 소비자 제품
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta + EssilorLuxottica (도파관 Lumus, LCoS 패널 옴니비전 OPO3010, 프로젝션 엔진 Goertek) |
| 연도 | 2025년 9월 발표·출시 |
| 수치 | 시야각 대각 20도(정사각 화면비) / 패널 600×600, 유효 해상도 약 400×400 / 화소밀도 40 PPD / 눈에 도달하는 밝기 약 5,000 nit / 프로젝터 광출력 최대 약 1 lumen / 소비전력 약 0.38W(LED·디스플레이·오디오 포함) / 시스템 명암비 실측 600:1 / 90fps, 필드 시퀀셜 컬러 270Hz / 눈부심 누출(eye glow) 밝기의 1.5% |
| 출처 | Karl Guttag, KGOnTech, 'Meta Ray-Ban Display Part 1: Lumus Waveguide, OmniVision LCOS, and Goertek Projection Engine' (2025-10-30) |

'AR 안경'의 정의를 뒤집은 제품이다. 넓은 시야각을 포기하고 **한쪽 눈 대각 20도짜리 작은 창**만 띄운다. 대신 그 작은 창 안에서 화소밀도 40 PPD, 눈에 도달하는 밝기 5,000 nit를 확보했다. 광엔진 소비전력은 0.38W에 불과하다. 시야각을 줄이면 같은 화소 수가 좁은 각도에 몰려 화소밀도가 올라가고, 같은 광량이 좁은 입체각에 모여 밝기가 올라간다 — 앞선 기기들이 반대 방향으로 밀어붙였던 교환관계를 거꾸로 탄 설계다.

기술적 도약이 아니라 **설계 철학의 전환**이다. '세상을 덮는 홀로그램' 대신 '읽을 수 있는 작은 자막'을 택했고, 그 결과 처음으로 안경 형태와 하루치 배터리를 동시에 만족했다. 조경 현장에서 수종명·수량 라벨을 띄우는 용도라면 이 수준이 홀로렌즈보다 실용적일 수 있다.

단안(한쪽 눈)이며 3차원 정합이 아니다. 즉 Azuma의 세 조건 중 '3차원 정합'을 충족하지 않으므로 엄밀히는 AR이 아니라 헤드업 정보 표시에 가깝다. 정확한 무게와 소매가격은 확인하지 못했다(기사 내 이미지 캡션에 '800달러 AR 안경'이라는 표현만 있다).

### Apple Vision Pro — 마이크로 OLED + 팬케이크 광학의 비디오 시스루
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple (마이크로 OLED 패널 공급사는 애플 공식 문서에 명시되지 않음) |
| 연도 | 2023년 6월 5일 발표 / 2024년 2월 2일 출시 (M5 모델 2026년) |
| 수치 | 애플 공식: 마이크로 OLED, 총 2,300만 화소, 화소 피치 7.5μm, 지원 재생률 90/96/100/120Hz, 색역 DCI-P3 92%, R1 칩 광자-대-광자 지연 12ms, 무게 750~800g, 가격 3,499달러(2026년 6월 3,699달러로 인상) / 2차 출처: 한쪽 눈 약 3660×3200, 패널 대각 1.41인치, 수평 시야각 약 100도·수직 약 73도 / 실측: 중심 화소밀도 44.4 PPD, 선명한 '스위트스팟'은 45~50도에 불과, 주변부는 중심의 약 1/3 |
| 출처 | Apple 공식 기술사양 https://www.apple.com/apple-vision-pro/specs/ · Karl Guttag, KGOnTech, 'Apple Vision Pro's Optics Blurrier & Lower Contrast than Meta Quest 3' (2024-03-01) 및 'Part 4: Hypervision Pancake Optics Analysis' (2023-06-26) · 화소수·시야각·가격은 Wikipedia 'Apple Vision Pro' |

광학 시스루를 버리고 **비디오 시스루로 되돌아간 고성능 사례**다. 외부 카메라가 찍은 실세계를 가상 콘텐츠와 합성해 눈앞 마이크로 OLED에 띄운다. 마이크로 OLED는 실리콘 웨이퍼 위에 OLED를 직접 증착해 화소 피치를 7.5μm까지 줄인 패널로, 1.41인치 대각 크기에 3660×3200 화소가 들어간다(양안 합계 2,300만 화소). 이 작은 패널을 눈앞에서 크게 보이게 하려면 강한 배율이 필요한데, 이를 **팬케이크 광학**(편광과 반사를 이용해 짧은 거리 안에서 광로를 세 번 접는 렌즈)으로 해결했다. 비디오 시스루의 치명적 약점인 지연은 R1 전용 칩으로 광자-대-광자 12ms까지 낮췄다.

비디오 시스루가 실용 가능해진 분기점이다. 지연 12ms와 2,300만 화소는 Azuma가 1997년에 지적한 비디오 방식의 두 약점(시간 불일치, 실세계 해상도 저하)을 처음으로 견딜 만한 수준까지 끌어내렸다. 동시에 **가림 문제는 원리적으로 완전히 해결된다** — 실세계도 화소이므로 가상 물체가 실물을 완전히 덮을 수 있다.

애플은 nit 단위 밝기, 한쪽 눈 화소 수, 시야각을 공식 사양에 공개하지 않는다. 위의 3660×3200과 100도는 2차 출처다. 팬케이크 광학은 편광 반사를 반복하므로 광효율이 매우 낮아(수 % 수준) 패널이 극도로 밝아야 하고, 이것이 발열과 배터리의 원인이다. 750~800g은 머리에 얹기에 무겁다. 야외 조경 현장에서 카메라가 포착한 실세계는 여전히 실제 눈보다 어둡고 동적 범위가 좁다.

### Meta Orion — 탄화규소(SiC, n≈2.6) 도파관으로 시야각 70도
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta Reality Labs |
| 연도 | 2024년 9월 25일 공개(Meta Connect, 시제품 — 판매 없음) |
| 수치 | 시야각 70도 / SiC 굴절률 가시광에서 약 2.6(비교: 일반 도파관 유리 1.7~2.0) / 마이크로LED 패널 640×480 / 화소밀도 13 PPD(일부 시연은 26 PPD 버전), 유효 해상도로 환산하면 약 720×540 / 4인치급 SiC 웨이퍼 한 장에서 도파관 4개(유리 대구경 웨이퍼는 12개 이상) / SiC 열전도율은 유리의 200~400배 |
| 출처 | Karl Guttag, KGOnTech, 'Meta Orion AR Glasses Pt. 1 — Waveguides' (2024-10-06), 'Pt. 2 — Orion vs. WaveOptics, Snap, and Magic Leap Waveguides' (2024-10-17), 'Silicon Carbide Waveguides Pros and Cons' (2026-09-08), 'Meta Orion Through the Optics Pictures' (2024-12-05) |

도파관의 시야각 한계를 **재료로 돌파한** 사례다. 도파관은 유리 안에서 전반사로 빛을 가두는데, 가둘 수 있는 각도 범위가 굴절률에 직결된다. 굴절률이 높을수록 임계각이 작아져 더 넓은 각도의 빛을 붙잡을 수 있고, 그 각도 범위가 곧 시야각이다. 일반 도파관 유리는 굴절률 1.7~2.0인데, 탄화규소는 가시광에서 약 2.6이다. 메타는 SiC 단일 판 양면에 회절 격자를 새겨(앞뒷면 격자가 교차 배치) 70도 시야각을 얻었다. 광원은 마이크로LED 프로젝터다.

'유리로는 시야각 50도가 한계'라는 벽을 재료로 넘었다. 동시에 SiC는 열전도율이 유리의 200~400배(구리에 근접)여서 마이크로LED의 발열 방출에도 유리하다. 그러나 이 도약의 청구서가 명확하다 — 시야각을 70도로 펴자 화소밀도가 13 PPD로 주저앉았다.

13 PPD는 사람 눈 기준(60 PPD)의 4분의 1도 안 된다. 텍스트를 읽기 어려워 메타는 서체(Optimistic)를 곡선을 줄이고 획을 굵게 고쳐야 했다. 색균일도가 나빠 UI를 일부러 '보석 같은 색 그라디언트'로 디자인해 결함을 감췄다. 웨이퍼당 4개 생산은 단가를 감당하기 어렵다. 판매 제품이 아니라 시제품이며, 밝기(nit) 수치는 공개되지 않았다.

### 단층 풀컬러 SiC 회절 도파관 — 무지개 아티팩트의 원리적 제거
| 항목 | 내용 |
| --- | --- |
| 주체 | Boqu Chen 외 6인 |
| 연도 | 2024년 9월 22일 arXiv 투고 / eLight 5권 21호(2025) 게재 |
| 수치 | 완성 도파관 두께 0.55mm, 무게 2.6856g(패키징·레이저 컷 후) / 설계 시야각 30도, 실측 45.7도(프로젝터 시야각 50도 때문) / 격자 주기 262nm(바이너리) — 입력부 듀티비 58%·높이 169nm, 확장부 50.5%·167nm, 출력부 42.1%·27nm / 굴절률 n=1.9 유리로 30도 풀컬러를 하려면 주기 370nm 필요 → 무지개 발생 / 4인치 4H-SiC 웨이퍼 / RGB 혼합광 밝기 균일도 3.18%, 광효율 175.45 nit/lm / MTF@22PPD 0.2669(수평)·0.3055(수직) / 왜곡 1.48% / 봉지층 편면 30μm · 후속 연구(Li 외, arXiv 2609.07648, 2026)는 두께 0.35mm·무게 1.98g·시야각 30도·투과율 92%  |
| 출처 | Chen, B. 외 (2024/2025). Ultra-Thin, Ultra-Light, Rainbow-Free AR Glasses Based on Single-Layer Full-Color SiC Diffractive Waveguide. arXiv:2409.14487 / eLight 5, 21 (2025). 전문 PDF 직접 추출·확인 |

메타 오리온과 같은 SiC 재료를 학술적으로 정량화한 논문이다. 핵심은 **격자 주기(period)를 굴절률로 줄일 수 있다**는 점이다. 굴절률이 높으면 같은 시야각을 더 짧은 주기의 격자로 구현할 수 있고, 주기가 짧으면 주변광이 격자에 회절되는 각도가 커져 그 빛이 아예 눈에 들어오지 않는다. 즉 AR 안경의 고질적 결함인 무지개 아티팩트(주변광 회절로 생기는 색번짐)가 광학적으로 사라진다. 굴절률 1.9 유리로 같은 30도 시야각을 만들면 주기가 370nm여야 하고, 이 경우 회절된 청·녹색 성분이 아이박스로 들어와 무지개가 보인다. SiC는 262nm면 된다.

'고굴절률 → 넓은 시야각'만이 아니라 '고굴절률 → 짧은 격자 주기 → 무지개 소거 → 단일 판으로 풀컬러'라는 두 번째 이득을 정량적으로 입증했다. RGB 3장을 1장으로 줄이면 두께·무게·투과율·비용이 동시에 개선된다.

실측 시야각 45.7도는 프로젝터 시야각(50도)에 끌려 올라간 값이고 설계값은 30도다. 메타 오리온의 70도와는 격차가 크다. MTF@22PPD 0.27~0.31은 텍스트 가독성이 충분하지 않다는 뜻이다. SiC 웨이퍼 단가와 취성(깨지면 날카로운 파편)이 상용화의 실질적 장벽이다.

### 시야각을 넓히기 어려운 광학적 이유 — 에텐듀 보존과 전반사 임계각
| 항목 | 내용 |
| --- | --- |
| 주체 | Jianghao Xiong, En-Lin Hsiang, Ziqian He, Tao Zhan, Shin-Tson Wu (University of Central Florida) |
| 연도 | 원리 자체는 고전 광학 / AR 맥락 정식화는 Xiong 외 2021 리뷰 |
| 수치 | 사람 눈의 목표 해상도: 20/20 시력 = 1 각분 = 60 PPD / 맑은 날 주변 휘도 약 3,000 nit, 흐린 날 약 300 nit / 실외에서 명암비(ACR) 10:1을 얻으려면 디스플레이가 최소 30,000 nit 필요(3:1이면 인지 가능, 5:1이면 읽을 만함) / 대각 60도 시야각 + 10mm 정사각 출사동에서 결합기 효율의 이론적 최댓값 약 17,000 nit/lm / 동공 추적형(pupil steering)이면 80도×80도 시야각·4mm 동공에서 47,000 nit/lm까지 가능 / 광엔진 광효율: MEMS-LBS 40 lm/W, DMD 15(LED)~30(레이저), LCoS 10(LED)~30(레이저), 마이크로LED 5(RGB)~10(QD), 마이크로 OLED 4~8 / 도파관 |
| 출처 | Xiong, J., Hsiang, E.-L., He, Z., Zhan, T., Wu, S.-T. (2021). Augmented reality and virtual reality displays: emerging technologies and future perspectives. Light: Science & Applications, 10, 216. https://pmc.ncbi.nlm.nih.gov/articles/PMC8546092/ · 굴절률 수치는 iScience 22(8), 101397 (2020) |

시야각이 넓어지지 않는 이유는 공학적 미숙이 아니라 두 개의 물리 법칙이다. 첫째 **에텐듀 보존**: 광학계를 통과하는 빛의 '면적 × 입체각' 곱은 보존된다. 즉 시야각(입체각)을 넓히면 아이박스(면적)가 좁아지고, 둘을 다 키우려면 광학계 자체를 키워야 해 안경 형태가 무너진다. 둘째 **전반사 임계각**: 도파관은 굴절률 n인 유리 안에서 임계각 arcsin(1/n)보다 큰 각도로 부딪히는 빛만 가둘 수 있다. 가둘 수 있는 각도 범위가 시야각의 상한이고, 그 범위는 오직 굴절률로만 넓어진다. 여기에 셋째 제약이 붙는다 — 시야각을 넓히면 같은 화소가 더 넓게 퍼지므로 화소밀도가 반비례로 떨어진다.

이 세 법칙이 지난 10년의 AR 디스플레이 계보 전체를 설명한다. 홀로렌즈 2가 시야각을 52도로 넓히며 화소밀도를 잃은 것, 매직리프 2가 굴절률 2.0으로 70도를 얻으며 투과율 22%를 대가로 낸 것, 메타 오리온이 굴절률 2.6으로 70도를 얻으며 13 PPD로 떨어진 것, 반대로 메타 레이밴 디스플레이가 20도로 줄여 40 PPD와 5,000 nit를 얻은 것 — 전부 같은 방정식의 다른 해다.

이 리뷰는 굴절률 n과 최대 시야각을 잇는 **닫힌 형태의 공식을 명시하지 않는다.** 임계각이 arcsin(1/n)이라는 사실과 '굴절률이 높을수록 시야각이 넓어진다'는 정성적 관계, 그리고 제품별 실측값(n=2.0 → 70도, n=2.6 → 70도, n=1.7~1.8 → 50도 전후)은 확인했으나, 'n=1.5이면 최대 몇 도'라는 식의 계산식은 이번 조사에서 1차 출처로 확인하지 못했다.

#### 검증에서 잡힌 정정
- [틀림·3곳 반복] 'iScience 22(8), 101397 (2020)' → 올바른 값은 **iScience 23(8), 101397 (2020)**. Crossref(DOI 10.1016/j.isci.2020.101397) 및 Europe PMC(PMCID PMC7404571) 모두 Volume 23으로 확인. 논문명은 Zhan, Yin, Xiong, He, Wu, 'Augmented Reality and Virtual Reality Displays: Perspectives and Challenges'. 자유공간 결합기 항목·Lumus 항목·에텐듀 항목 세 곳 모두 수정 필요.
- [틀림] Apple Vision Pro 'M5 모델 2026년' → **2025년 10월 15일 발표, 10월 22일 출시**. (Wikipedia 'Apple Vision Pro' 확인). 가격 인상 '2026년 6월 3,699달러'는 2026-06-25로 확인되어 맞음.
- [틀림/출처 불일치] 자유공간 결합기 항목의 '아이박스 8mm' → Xiong 외 2021 원문은 **10mm 정사각 출사동(exit pupil 10 mm square)**을 가정한다. 원문: 'the maximum combiner efficiency for a typical diagonal FoV of 60° and exit pupil (10 mm square) is around 17,000 nit/lm'. 같은 조사 결과의 에텐듀 항목은 10mm로 적어 자기모순.
- [틀림/출처 오적용] Lumus 항목의 '반사형 결합기 광효율 최대 50% vs 회절 격자 10% 미만' → iScience 23(8) Table 2에서 **<50%는 freeform mirror·freeform prism(자유공간 결합기)** 값이고, Lumus가 쓰는 **cascaded mirrors(계단식 거울 도파관)는 <20%**, 버드배스는 <25%다. 회절(VBG·SRG·PVG·HPDLC) <10%는 맞음. 즉 Lumus 방식에 50%를 붙인 것은 오적용이며 올바른 값은 20% 미만.
- [자기모순/부정확] HoloLens 1 '양안 합계 230만 화소, 한쪽 눈 1268×720' → 1268×720×2 = **약 183만**으로 230만과 맞지 않는다. 마이크로소프트 표현은 '화소'가 아니라 '2.3 million total light points(총 광점)'이며 Wikipedia도 '2.3 megapixel widescreen'으로만 적는다. '양안 230만 화소'와 '1268×720/눈'을 병기하면 안 됨.
- [틀림/구식 추정치] HoloLens 2 '시야각 대각 52도(계산상 수평 41.6도×수직 31.2도)' → 41.6×31.2는 **4:3 비율 분해**다. 마이크로소프트 공식 사양은 '2k 3:2 light engines'(3:2)이므로 52도 대각을 3:2로 분해하면 **약 43.3도(수평)×28.9도(수직)**다. 41.6×31.2는 Guttag가 2019-02-27 글에서 화면비 확정 전에 계산한 값으로 이후 정정됨.
- [자기모순] Meta Orion '마이크로LED 패널 640×480 / 13 PPD / 유효 해상도로 환산하면 약 720×540' → 유효 해상도가 패널 해상도보다 클 수 없다. 720×540은 Guttag가 2024-10-06 글에서 패널 사양을 모르던 시점에 13 PPD×70도로 역산한 추정치이고, 640×480은 2026-09-08 글에서 확정한 실제 패널값이다. 640×480(대각 800화소)을 70도 대각에 대입하면 **약 11.4 PPD**로 13 PPD와도 어긋난다. 둘 중 하나만 써야 함.
- [세대 혼동] Apple Vision Pro 항목이 '2024년 2월 2일 출시' 제품에 '무게 750~800g'과 '120Hz'를 붙였다 → 750~800g과 120Hz는 **2025년 M5 모델** 사양이다. 2024년 출시 M2 모델은 **600~650g, 최대 100Hz**(지원 재생률 90/96/100Hz). 현재 apple.com 사양 페이지가 M5 기준이라 750~800g·90/96/100/120Hz로 표시될 뿐, 출시 연도와 함께 적으면 틀린 서술이 된다.
- [반올림 오차] 에텐듀 항목 '광엔진 광효율: DMD 15(LED)~30(레이저), LCoS 10(LED)~30(레이저)' → Xiong 외 2021 원문은 레이저 광원일 때 DMD·LCoS 모두 **32 lm/W**. MEMS-LBS 40, 마이크로LED 5(RGB)/10(QD), 마이크로 OLED 4~8은 원문과 일치.
- [확인 불가] Meta Ray-Ban Display의 '화소밀도 40 PPD'는 Guttag(2025-10-30) 값으로 원문과 일치하나, 메타 공식 사양(20도 시야각 기준 42 PPD로 알려짐)과의 대조는 이 세션의 웹 검색 한도 소진 및 meta.com 제품 페이지 본문 추출 실패로 확인하지 못했다.
- [확인 불가] Magic Leap One '시야각 약 50도'는 인용된 Guttag 2018-08-23 티어다운 글 본문에 없다(해당 글에서 확인된 것은 1280×960 4:3, 도파관 6층, 초점면 2개, LED 6개·입력격자 6개). 밝기 210 nit은 2021-10-13 글의 'Back in 2018, I measured the ML1's brightness and only got about 210 nits'로 확인됨. 50도는 제조사 공식값(40도×30도) 대조를 못 했다.
- [확인 불가] Lumus 'Z-Lens 2023년 발표' → lumus.com 제품 페이지에는 발표 연도가 없다(시야각 50도·1024×1024·>1,400 nit/W·아이박스 11×11mm·두께 1.3mm·투과율 >80%는 전부 일치). Maximus 2021년은 Guttag 2021-05-24 'Exclusive: Lumus Maximus…' 글로 간접 확인됨.
- [연도 오류] Apple Vision Pro 'M5 모델 2026년' → 실제 2025년 10월 22일 출시. (Wikipedia 'Apple Vision Pro' 대조). 발표 2023-06-05·원본 출시 2024-02-02·2026년 6월 25일 3,699달러 인상은 모두 맞음.
- [세대 혼동] Apple Vision Pro 무게 '750~800g'은 2025년 M5 모델(Dual Knit Band 포함) 수치. 해당 항목이 기술하는 2024년 M2 원본은 600~650g(배터리 353g 별도). 현재 apple.com/apple-vision-pro/specs/는 M5 기준이라 750~800g으로 표기되어 있어 인용 시점 혼동이 발생.
- [세대 혼동] Apple Vision Pro '지원 재생률 90/96/100/120Hz'에서 120Hz는 M5(2025) 전용. 2024년 M2 원본은 90/96/100Hz까지. (Wikipedia: M2 up to 100Hz, M5 up to 120Hz)
- [출처 권호 오류·3회 반복] 'iScience 22(8), 101397 (2020)' → 정확히는 iScience 23(8), 101397 (2020), Zhan, T., Yin, K., Xiong, J., He, Z., Wu, S.-T., 'Augmented Reality and Virtual Reality Displays: Perspectives and Challenges', doi:10.1016/j.isci.2020.101397. iScience 22권은 2019년 발행분이므로 '22권(2020)' 조합 자체가 성립하지 않음. (Crossref API 대조)
- [선후관계 역전] '원리 계보는 Ivan Sutherland(1968) → 항공 HUD → 구글글래스·엑스리얼' → 항공 HUD가 Sutherland HMD보다 앞선다. 실전 배치형 항공 HUD는 1950년대 말(영국 해군 Buccaneer, 1958년경), 그 직계 조상인 반사식 조준기(reflector gunsight)는 1930~40년대. Azuma(1997) 본문도 'optical see-through HMDs have sometimes been described as a "HUD on a head"'라며 HUD를 선행 기술로 서술 — 인용한 출처가 오히려 이 계보를 반박한다.
- [기술 분류 오류] 구글글래스(2013)를 '하프미러·버드배스' 계열 상용화 사례로 넣은 것은 부정확. 구글글래스는 LCoS + 편광 빔스플리터 프리즘(도광 프리즘) 방식이며, 버드배스(곡면 반투과 거울+빔스플리터)는 엑스리얼/Nreal 계열의 구조다. 또한 구글글래스 Explorer Edition은 2013년 4월 개발자 한정 배포이고 일반 판매는 2014년 5월이므로 '상용화 2013'도 단서가 필요.
- [내부 모순·수치 오류] HoloLens 2 '시야각 대각 52도(계산상 수평 41.6도×수직 31.2도)' → 41.6:31.2 = 4:3 비율로, 같은 항목에 인용된 Microsoft 공식 '2k 3:2 광엔진'과 모순. 3:2 기준 52° 대각은 약 43.3°×28.9°(통상 보고치 43°×29°).
- [선후관계 과장] 'HoloLens 1 = LCoS + 회절 도파관의 첫 대량 상용화' → 다툼의 여지 큼. 소니 SmartEyeglass Developer Edition SED-E1(홀로그래픽 도파관)이 2015년 3월 판매 개시로 HoloLens 개발자판(2016-03-30)보다 1년 앞섬. BAE Systems Q-Sight(홀로그래픽 도파관 헬멧 디스플레이)는 2000년대 후반 군용 실전 배치. '첫'이라는 단정 대신 '첫 대중 인지도 제품' 수준으로 완화 필요. ※소니 출하일은 이번 세션에서 재확인 실패(sony.com·해당 위키 페이지 접근 불가).
- [출처 오귀속] Magic Leap One '실측 밝기 약 210 nit(Guttag, 2018)' → 인용된 KGOnTech 'iFixit's Magic Leap One Teardown...'(2018-08-23) 본문에는 밝기(nit) 수치가 없음. 해당 글이 확인해 주는 것은 LCoS 1280×960(4:3, 옴니비전), LED 6개·입력 격자 6개, 2개 심도면까지. 210 nit는 다른 글에서 왔거나 미확인.
- [경미한 수치 차이] Xiong 2021 광엔진 효율 'DMD 30(레이저), LCoS 30(레이저)' → 논문 대조 시 각 32 lm/W. MEMS-LBS 40, 마이크로 OLED 4~8은 일치.
- [미확인] Lumus 'Maximus 2021년 발표 / Z-Lens 2023년 발표' → lumus.com 제품·뉴스 페이지에 발표 연도 표기가 없고 사이트 검색이 동작하지 않아 이번 세션에서 확인 실패. 단, 사양(Maximus 50°·1440×1440·>3,000 nit/W_LED·12×12mm·1.7mm / Z-Lens 50°·1024×1024·>1,400 nit/W_LED·11×11mm·1.3mm·투과율 >80%)은 공식 페이지와 완전 일치.
- [미확인] KGOnTech 'HoloLens 2 First Impressions: the LBS resolution math fails'(2019-02-27) 및 'HoloLens 2 Display Evaluation Part 2'(2020-07-08) URL이 해석되지 않고 사이트 검색도 오동작하여, MEMS 54,000 사이클/초·프레임당 900사이클·활성 720사이클·주사선 854줄·유효 600줄·마이크로소프트 주장 47 PPD 대 측정 20 PPD 미만은 이번 세션에서 1차 확인 실패(글 자체가 존재하지 않는다는 뜻은 아님 — 같은 블로그의 2018-08-23, 2022-01-31, 2024-10-06, 2025-10-30, 2026-09-08 글은 모두 정상 확인됨).
- [미확인/보충] Meta Ray-Ban Display '화소밀도 40 PPD'는 Guttag 실측 기준으로 정확(인용 글에서 확인). 다만 메타 공식 발표치는 42 PPD로 알려져 있어 '제조사 공식값'과는 다른 값임을 명시하는 편이 안전(meta.com 제품 페이지 접근 실패로 이번 세션 미확인).
- [미확인] Apple Vision Pro '패널 대각 1.41인치', '중심 44.4 PPD', '스위트스팟 45~50도', HoloLens 1 '노키아 인수 회절 도파관 특허 계열' — 1차 출처로 확인하지 못함.
- [확정 오류·3회 반복] iScience 권호가 틀림. 'iScience 22(8), 101397 (2020)' → 정확히는 **iScience 23(8), 101397 (2020)**. Crossref(DOI 10.1016/j.isci.2020.101397)와 PMC7404571 모두 Volume 23, Issue 8, 2020년 8월. 권 22는 2019년치다. 본문에서 자유공간 결합기·Lumus·에텐듀 세 항목에 각각 인용돼 있어 3곳 모두 수정 필요.
- [확정 오류·귀속] 위 iScience 논문의 저자를 Xiong 외 2021 LSA 리뷰와 같은 계열로 묶어 인용했으나, 실제 저자는 **Zhan, T., Yin, K., Xiong, J., He, Z., Wu, S.-T.**이고 제목은 'Augmented Reality and Virtual Reality Displays: Perspectives and Challenges'다. Xiong이 제1저자가 아니며 별개 논문이다. 다만 내용(Table 2: 반사형 <50%, 캐스케이드 미러 <20%, 회절형 <10%; n_d=1.50±0.03 / 고굴절 1.7~1.8 / 최근 상용화 n_d≥1.9)은 원문과 일치한다.
- [확정 오류·연도] Apple Vision Pro 'M5 모델 2026년' → **2025년 10월 15일** 발표(Wikipedia 'Apple Vision Pro'). 가격 인상 '2026년 6월 3,699달러'는 맞음(2026-06-25).
- [확정 오류·측정값] Magic Leap One '실측 밝기 약 210 nit(Guttag, 2018)' → Guttag 원문은 **'The ML1 supports about 220 cd/m2'** = 약 220 nit. 또한 이 측정치의 출처는 인용된 2018-08-23 iFixit 티어다운 기사가 **아니라** 2018-10-22 'Magic Leap, HoloLens, and Lumus Resolution Shootout (ML1 Review Part 3)'다. 티어다운 기사에는 밝기 측정값이 없다(LCoS 1280×960, LED 6개+입력격자 6개, 2초점면만 있음).
- (외 8건)

## tracking — AR 트래킹·정합(registration) 기술의 계보
항목 13개 · 검증 정정 지적 37건


### Azuma 서베이 — '정합(registration)' 문제의 정식화
| 항목 | 내용 |
| --- | --- |
| 주체 | Ronald T. Azuma, Hughes Research Laboratories (3011 Malibu Canyon Road, Malibu, CA) |
| 연도 | 발표 1997년 8월 (Presence: Teleoperators and Virtual Environments 6권 4호, 355–385쪽) |
| 수치 | 인간 중심와(fovea)의 색각 원추세포 밀도 약 120개/도 → 분해 간격 0.5분각(arcminute). 관찰자는 명암 줄무늬가 각각 1분각을 차지할 때 구별 가능. 팔 길이에서 10센트 동전 지름 = 1.2~2.0도, 보름달 지름 = 0.5도. 1990년대 시스템의 종단간 지연 약 100ms(느린 시스템은 250ms 이상). 지연 100ms + 머리 회전 50도/초 → 각오차 5도 → 팔 길이 68cm에서 위치 오차 약 60mm. 각오차 0.5도 이하로 억제하려면 지연 10ms 이하 필요하나, 60Hz 프레임버퍼 스캔아웃만으로 16.67ms 소요. 트래커에 요구되는 정확도: 약 1mm, 1도의 작은 분수. |
| 출처 | Azuma, R. T. (1997) "A Survey of Augmented Reality", Presence: Teleoperators and Virtual Environments 6(4), 355–385. 원문 PDF: https://ronaldazuma.com/papers/ARpresence.pdf (본 조사에서 전문 텍스트 추출하여 직접 확인) |

AR을 '특정 기기(HMD)'가 아니라 '세 가지 성질'로 정의한 문헌이다. 그중 세 번째 조건인 '3차원 정합'이 이후 30년간 AR 트래킹 연구의 문제 정의 그 자체가 되었다. 아주마는 정합 오차의 원인을 정적(static) 오차와 동적(dynamic) 오차로 나눴다. 정적 오차는 사용자와 물체가 완전히 정지해 있을 때조차 남는 오차(광학 왜곡, 트래커 오차, 시점 보정 오류, 시스템 모델 오류)이고, 동적 오차는 움직이기 시작해야만 나타나는 오차, 즉 시스템 지연(lag)이 만드는 오차다. 그리고 동적 오차가 나머지 전부를 합친 것보다 크다고 못 박았다. 대응책도 네 가지로 정리했다 — 지연 자체를 줄이기, 겉보기 지연을 줄이기(이미지 편향·워핑), 실·가상 영상의 시간축 맞추기(비디오 방식에서만 가능), 그리고 미래 위치를 예측하기.

이전까지 '가상 물체가 실제와 어긋난다'는 현상 서술에 머물던 것을, '오차를 정적/동적으로 분해하고 각각의 원인과 대응책을 지목하는' 공학 문제로 바꿨다. 특히 지연(ms)과 각오차(도)와 위치오차(mm)를 하나의 식으로 연결해, 지연 1ms가 몇 mm의 어긋남인지 계산 가능하게 만든 것이 결정적이다. 조경에 그대로 옮기면, 현장에서 고개를 돌릴 때 가상 수목이 '헤엄치는' 이유를 정량적으로 설명할 수 있게 된 것이다.

아주마 자신이 '정합 문제는 전혀 해결되지 않았다(far from solved)'고 적었다. 당시 성공 사례는 대부분 시점이 고정되어 있거나, 물체가 고정되어 있거나, 이동 범위가 제한되거나, 기준마커가 붙은 단 하나의 물체에만 작동했다. 야외·대규모·자연물에 대한 정합은 논의조차 못 했다.

### 예측 트래킹(predictive tracking)과 하이브리드 트래커 — Azuma & Bishop
| 항목 | 내용 |
| --- | --- |
| 주체 | Ronald Azuma, Gary Bishop — University of North Carolina at Chapel Hill 컴퓨터과학과 |
| 연도 | 1994년 (SIGGRAPH '94), 후속 분석 1995년 |
| 수치 | 개방루프(open-loop) 시스템으로 팔 길이 거리의 물체에 대해 여러 시점에서 통상 ±5mm 이내 정합 달성. 지연 약 80ms 이하 구간에서 예측은 동적 오차를 최대 한 자릿수(order of magnitude, 약 10배) 감소시킴. 관성 센서를 쓰면 예측 정확도가 2~3배 향상. 비교: 폐쇄루프(closed-loop, 영상 피드백) 시스템은 1픽셀 이내의 거의 완벽한 정합 달성. |
| 출처 | Azuma, R. & Bishop, G. (1994) "Improving Static and Dynamic Registration in an Optical See-Through HMD", Proc. SIGGRAPH '94, 197–204. 본 조사에서는 원논문 PDF 접근에 실패했고, 위 수치는 모두 Azuma(1997) 서베이 4.3·4.5절이 [Azuma94]를 인용하며 명시한 값을 직접 추출한 것이다. |

지연을 없앨 수 없다면 미래를 맞추자는 접근이다. 트래커가 시각 t에 머리 위치를 측정하면, 화면에 그림이 뜨는 시각 t2에는 이미 머리가 움직여 있다. 그러므로 t의 위치가 아니라 t2의 예상 위치로 그린다. 관성 센서(자이로·가속도계)가 각속도와 각가속도를 직접 알려주므로, 광학 트래커만 쓸 때보다 예측이 훨씬 정확해진다. 이것이 이후 모든 AR·VR 장비가 채택하는 '광학 + 관성 하이브리드' 구조의 원형이다. 아주마의 시스템은 천장에 LED를 격자로 깔고 헬멧의 광전 센서가 그것을 보는 방식(optoelectronic ceiling tracker)이었다.

'센서를 더 정확하게 만든다'는 하드웨어 경쟁에서 '같은 센서로 시간을 앞질러 계산한다'는 알고리즘 경쟁으로 축을 옮겼다. 오늘날 Vision Pro의 12ms, Quest의 타임워프, 자동차 AR HUD의 예측 렌더링이 모두 이 발상의 자손이다. 다만 예측에는 한계가 있다 — 지연이 길어질수록 예측 오차는 급격히 커진다.

예측은 지연이 짧을 때만 통한다. 지연이 80ms를 넘으면 예측 자체가 오차원이 되어 물체가 '앞질러 튀는' 현상을 만든다. 또 천장 LED 격자 방식이라 작업 범위가 방 하나로 묶였고, 야외로 나갈 수 없었다.

### ARToolKit — 마커 기반 정합의 표준화
| 항목 | 내용 |
| --- | --- |
| 주체 | Hirokazu Kato(加藤博一, 히로시마시립대학 정보과학부) & Mark Billinghurst(워싱턴대학 HIT Lab) |
| 연도 | 논문 발표 1999년 10월 (IWAR'99), 라이브러리 v1.0 배포 2001년, 오픈소스 재공개 2015년 (DAQRI 인수 후 v5.2) |
| 수치 | 실험 장비: 263×234 픽셀 카메라. 정확도 평가에 한 변 80mm 마커 사용, 깊이 방향으로 이동시키며 오차 측정. 사용자 실험의 눈–마커 거리 조건: 300mm / 400mm / 800mm. 결과는 '마커가 가까울 때 좋고, 카메라에서 멀어질수록 정확도가 떨어진다'. |
| 출처 | Kato, H. & Billinghurst, M. (1999) "Marker Tracking and HMD Calibration for a Video-based Augmented Reality Conferencing System", Proc. 2nd IEEE and ACM International Workshop on Augmented Reality (IWAR'99). PDF: https://www.hitl.washington.edu/artoolkit/Papers/IWAR99.kato.pdf (본 조사에서 전문 텍스트 추출) |

검은 정사각형 테두리 안에 패턴을 넣은 '기준마커(fiducial marker)'를 현실에 붙이고, 카메라 영상만으로 그 마커에 대한 카메라의 6자유도 자세를 실시간 계산한다. 처리 순서가 단순해서 빨랐다 — ①영상 이진화(임계값 처리) ②연결요소 추출 ③외곽선이 네 개의 직선으로 맞춰지는 영역만 남김 ④내부 패턴을 템플릿 매칭으로 식별 ⑤네 모서리의 화면좌표와 알려진 마커 크기로부터 변환행렬 계산. 마커의 실제 크기를 알고 있으므로 단안 카메라만으로 절대 스케일(미터 단위)이 나온다는 점이 핵심이다. 논문 자체는 원격 협업 회의 시스템과 광학 시스루 HMD 보정법이 주제였지만, 부산물인 마커 추적 코드가 세계 표준이 됐다.

그 전까지 정합은 자기식 트래커·기계식 암·천장 LED 같은 전용 하드웨어를 요구했다. ARToolKit은 '웹캠 + 종이에 인쇄한 마커'로 같은 일을 하게 만들어, AR 연구의 진입 비용을 사실상 0으로 떨어뜨렸다. 2000년대 AR 논문 대부분이 이 라이브러리 위에서 쓰였다. 조경에서 지금도 쓰이는 '모형 위에 마커를 놓고 태블릿으로 비추면 3D 수목이 뜬다'는 시연 방식이 정확히 이 계보다.

세 가지 한계가 그대로 남았다. ①마커가 카메라 시야에서 벗어나거나 일부만 가려도 즉시 추적 실패 ②거리에 따라 정확도가 급격히 열화 ③마커를 물리적으로 설치해야 하므로 '붙일 데가 없는' 야외 대규모 지형에는 적용 불가. 이 세 번째 한계가 조경 AR의 근본 병목이며, 마커 없는(markerless) SLAM 계보를 부른 이유다.

### MonoSLAM — 카메라 한 대로 실시간 지도를 만들다
| 항목 | 내용 |
| --- | --- |
| 주체 | Andrew J. Davison, Ian D. Reid, Nicholas D. Molton, Olivier Stasse — Imperial College London / Oxford |
| 연도 | 학회 발표 2003년 (ICCV), 확장판 저널 게재 2007년 6월 (IEEE TPAMI 29권 6호) |
| 수치 | 일반 PC와 일반 카메라에서 30Hz 동작. EKF의 계산 복잡도는 특징점 수 N에 대해 O(N²)이며, 지도 표현의 크기도 O(N²). 그 결과 실시간을 유지하며 관리 가능한 특징점 수가 30Hz 구현 기준 약 100개로 제한됨. 시야각 약 100도의 광각 카메라 사용. 작동 범위는 '방 한 칸(room-sized)' 규모. |
| 출처 | Davison, A. J., Reid, I. D., Molton, N. D., Stasse, O. (2007) "MonoSLAM: Real-Time Single Camera SLAM", IEEE Transactions on Pattern Analysis and Machine Intelligence 29(6). 최초 발표는 Davison (2003) "Real-Time Simultaneous Localisation and Mapping with a Single Camera", ICCV 2003. PDF: https://www.doc.ic.ac.uk/~ajd/Publications/davison_etal_pami2007.pdf (본 조사에서 전문 텍스트 추출) |

로봇공학에서 레이저 스캐너로 하던 SLAM(동시적 위치추정 및 지도작성)을 '카메라 한 대'만으로 실시간 수행한 최초의 성공 사례다. 화면 안의 눈에 띄는 점들(자연 특징점)을 골라 그 3차원 위치를 추정하고, 동시에 카메라 자신의 위치를 추정한다. 방식은 확장칼만필터(EKF)다 — 카메라 상태 13개 변수(3차원 위치, 방향 쿼터니언, 속도, 각속도)와 모든 특징점의 좌표를 하나의 거대한 상태벡터와 공분산 행렬에 넣고 매 프레임 갱신한다. 특징점끼리의 상관관계를 '꽉 찬 공분산(full covariance)'으로 전부 유지하기 때문에, 예전에 본 곳으로 되돌아오면 누적된 드리프트가 저절로 보정된다. 논문은 이 기술로 손에 든 카메라 영상에 가상 가구를 얹는 AR 데모를 직접 보였다.

마커를 없앴다. 사전 지도도 없앴다. '카메라를 켜고 걸어 들어가면 그 자리에서 지도가 생긴다'는 오늘날 AR의 기본 전제가 여기서 처음 실증됐다. 이전의 SFM(Structure from Motion)은 영상 전체를 모아 놓고 사후에 계산하는 오프라인 방식이었는데, MonoSLAM은 이를 온라인·실시간·드리프트 없는 방식으로 뒤집었다.

O(N²) 복잡도가 치명적이었다. 특징점 100개로는 방 한 칸이 한계이고, 정원이나 공원 같은 야외 규모는 원리적으로 불가능했다. 또 급격하거나 거친 카메라 움직임에 추적이 끊겼고, 끊기면 복구 수단이 없었다.

### PTAM — 추적과 지도작성을 두 갈래로 쪼개다
| 항목 | 내용 |
| --- | --- |
| 주체 | Georg Klein & David Murray — Oxford University Active Vision Laboratory |
| 연도 | 2007년 11월 (ISMAR 2007, 일본 나라) |
| 수치 | 지도 규모 M=2,000~6,000개 점, N=40~120개 키프레임(MonoSLAM의 약 100개 특징점과 대조). 하드웨어 Intel Core 2 Duo 2.66GHz. 카메라 640×480 YUV411, 30Hz, 2.1mm 광각 렌즈. 지도 4,000점 기준 한 프레임 추적 총 19.2ms(키프레임 준비 2.2ms + 특징점 투영 3.5ms + 패치 탐색 9.8ms + 자세 반복갱신 3.7ms). 지역 번들 조정 소요시간: 키프레임 2~49개일 때 170ms, 50~99개 270ms, 100~149개 440ms. 논문 표지 그림의 실제 장면: 약 3,000점 지도에서 1,000점을 찾으려 시도해 660점 관측, 그 프레임 추적에 18ms. |
| 출처 | Klein, G. & Murray, D. (2007) "Parallel Tracking and Mapping for Small AR Workspaces", Proc. 6th IEEE/ACM International Symposium on Mixed and Augmented Reality (ISMAR). PDF: https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf (본 조사에서 전문 텍스트 추출) |

MonoSLAM의 O(N²) 벽을 구조적으로 부순 논문이다. 핵심 발상은 '추적(tracking)'과 '지도작성(mapping)'을 서로 다른 두 스레드로 분리하는 것이다. 추적 스레드는 매 프레임(30Hz) 카메라 자세만 빠르게 구하고, 지도작성 스레드는 실시간 제약 없이 느긋하게 돌면서 모든 키프레임을 한꺼번에 최적화한다(번들 조정, bundle adjustment). 매 프레임을 다 쓰지 않고 '키프레임'만 골라 쓴다는 점도 핵심이다 — 사용자가 한 자리에 가만히 있으면 새 키프레임이 생기지 않으므로 지도작성 스레드가 놀지 않고 기존 지도의 정밀도를 올린다. 그 결과 특징점 수천 개짜리 지도를 프레임레이트로 추적할 수 있게 됐다. 논문 제목이 명시하듯 처음부터 '작은 AR 작업공간'을 겨냥해 만든 시스템이다.

필터(EKF) 기반에서 최적화(번들 조정) 기반으로 SLAM의 중심축이 옮겨간 전환점이다. 이후 ORB-SLAM, ARKit, ARCore, 헤드셋의 인사이드아웃 트래킹까지 사실상 모든 현대 AR 트래킹이 PTAM의 '두 스레드 + 키프레임 + 번들 조정' 구조를 물려받았다. 특징점 100개에서 수천 개로, 두 자릿수가 늘었다.

논문 제목의 'Small AR Workspaces'가 곧 한계 선언이다. 키프레임 150개를 넘으면 전역 번들 조정이 수렴하는 데 수십 초가 걸려 탐색 중에는 사실상 포기된다. 큰 루프를 닫는 기능이 없어 넓은 공간을 돌면 드리프트가 누적된다. 또 빠른 카메라 움직임이 만드는 모션블러가 FAST 코너를 지워버려 추적이 끊긴다. '장면이 충분히 질감이 있고, 비교적 정적이며, 자기가림이 심하지 않을 때'라는 전제가 붙는다 — 바람에 흔들리는 식생은 이 전제를 정면으로 위반한다.

### MSCKF — 관성 센서와 카메라를 융합한 VIO의 원형
| 항목 | 내용 |
| --- | --- |
| 주체 | Anastasios I. Mourikis & Stergios I. Roumeliotis — University of Minnesota (이후 Mourikis는 UC Riverside) |
| 연도 | 2007년 4월 (IEEE ICRA 2007, 이탈리아 로마) |
| 수치 | 실험 장비: Pointgrey FireFly 카메라 640×480, 3Hz + Inertial Science ISIS IMU 100Hz(주목 — IMU가 카메라보다 33배 빠르다). 필터 상태에 최대 30개 카메라 자세 유지. 미니애폴리스 주택가를 자동차로 약 9분 주행, 1,598장 영상, 총 142,903개 특징점 사용. 주행거리 3.2km에 대한 최종 위치 오차 약 10m = 이동거리의 0.31%. 이 모든 것을 루프 폐쇄(loop closing) 없이, 도로지도 같은 사전정보 없이, Intel T7200 2GHz 단일 코어에서 14Hz로 처리. |
| 출처 | Mourikis, A. I. & Roumeliotis, S. I. (2007) "A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation", Proc. IEEE International Conference on Robotics and Automation (ICRA), 3565–3572. PDF: https://www-users.cse.umn.edu/~stergios/papers/ICRA07-MSCKF.pdf (본 조사에서 전문 텍스트 추출) |

카메라만으로는 어둡거나 질감 없는 벽면, 빠른 회전에서 추적이 끊긴다. 반대로 IMU(관성측정장치)는 어떤 상황에서도 값을 내지만 시간이 지나면 드리프트한다. 두 센서의 약점이 정확히 상보적이므로 합치면 된다 — 이것이 VIO(visual-inertial odometry)다. MSCKF의 결정적 기여는 '어떻게 합치느냐'에 있다. 기존 SLAM은 특징점의 3차원 좌표를 전부 칼만필터 상태벡터에 넣었기 때문에 복잡도가 특징점 수의 제곱으로 늘었다(MonoSLAM의 O(N²) 문제). MSCKF는 특징점 좌표를 상태벡터에서 빼고, 대신 '하나의 정지한 점이 여러 카메라 자세에서 관측되었다'는 기하학적 제약만을 측정 모델로 표현했다. 그 결과 복잡도가 특징점 수에 대해 선형이 됐다.

'카메라+IMU를 스마트폰이 감당할 수 있는 계산량으로' 융합하는 법을 제시했다. ARKit과 ARCore가 2017년에 특별한 하드웨어 없이 일반 스마트폰에서 6자유도 추적을 돌릴 수 있었던 알고리즘적 근거가 이 계보다. 카메라가 못 보는 짧은 순간(빠른 회전, 순간적 가림)을 IMU가 메우기 때문에, 추적이 '끊기지 않는' 체감이 처음 나왔다.

오도메트리(odometry)이지 SLAM이 아니다 — 루프를 닫지 않으므로 드리프트가 누적되기만 하고 결코 보정되지 않는다. 3.2km에 10m는 훌륭하지만, 같은 자리로 돌아와도 10m 어긋난 채로 남는다. 또 실험은 오프라인 처리였고 GPS 참값이 없어 정량 검증이 지도 대조 수준에 머물렀다. 야외 절대좌표 문제(이 공원의 이 지점이 지구상 어디인가)는 손대지 못했다.

### ORB-SLAM — 대규모·평생 운용을 겨냥한 통합 설계
| 항목 | 내용 |
| --- | --- |
| 주체 | Raúl Mur-Artal, J. M. M. Montiel, Juan D. Tardós — Universidad de Zaragoza (스페인 사라고사대학) |
| 연도 | arXiv 투고 2015년 2월 3일, IEEE Transactions on Robotics 게재 2015년 |
| 수치 | FAST 코너를 8개 스케일 레벨(스케일 인자 1.2)에서 추출. 512×384~752×480 해상도에서는 프레임당 1,000개, KITTI의 1241×376 같은 고해상도에서는 2,000개 추출. 각 특징은 256비트 서술자. 27개 공개 데이터셋 시퀀스에서 평가. 실험 하드웨어 Intel Core i7-4700MQ(4코어 2.40GHz), 8GB RAM. 루프 후보 검색 39ms(특징 추출 포함). 정확도: 좁은 실내에서 통상 1cm 이하, 넓은 야외에서 수 미터 수준. 비교 대상 SIFT 약 300ms, SURF 약 300ms, A-KAZE 약 100ms — 33ms 프레임 예산 안에서는 전부 사용 불가. |
| 출처 | Mur-Artal, R., Montiel, J. M. M., Tardós, J. D. (2015) "ORB-SLAM: a Versatile and Accurate Monocular SLAM System", IEEE Transactions on Robotics 31(5), 1147–1163. arXiv:1502.00956. PDF: https://arxiv.org/pdf/1502.00956v2 (본 조사에서 전문 텍스트 추출) |

PTAM의 구조를 계승하되 '실내 책상 위'에서 '도시 규모'로 확장한 시스템이다. 결정적 설계 결정은 추적·지도작성·재위치추정(relocalization)·루프 폐쇄 네 가지 작업에 전부 동일한 ORB 특징을 쓴 것이다. ORB는 256비트 이진 서술자를 가진 방향성 FAST 코너로, SIFT나 SURF보다 두 자릿수 빠르면서도 시점·회전 변화에 견딘다. 여기에 두 종류의 그래프를 도입했다 — 어느 키프레임들이 같은 점을 함께 보는지 기록하는 '공시성 그래프(covisibility graph)', 그리고 그중 강한 연결만 남긴 성긴 부분그래프인 '핵심 그래프(Essential Graph)'다. 루프를 닫을 때 빽빽한 공시성 그래프 전체가 아니라 핵심 그래프만 최적화하므로 도시 규모에서도 실시간을 유지한다. '적자생존(survival of the fittest)' 방식으로 중복 키프레임을 솎아내, 장면이 바뀔 때만 지도가 자라게 만든 것도 평생 운용을 위한 장치다.

'끊기면 끝'이던 SLAM에 회복력을 붙였다. 추적이 끊겨도 bag-of-words 방식으로 현재 화면과 비슷한 과거 키프레임을 찾아내 즉시 재위치추정하고, 큰 루프를 닫아 누적 드리프트를 되돌린다. 그리고 소스코드를 공개했다 — 이후 대부분의 학술 AR·로봇 시스템의 기준선이 됐다.

두 가지가 조경에 직접 걸린다. 첫째, '척도를 참값에 맞춰 정렬한 뒤'라는 단서 — 단안 카메라 SLAM은 절대 크기를 모른다. 이 나무가 3m인지 6m인지 SLAM 혼자서는 판정할 수 없다(그래서 ARKit·ARCore는 IMU를, 헤드셋은 스테레오 카메라를 반드시 함께 쓴다). 둘째, 야외 정확도가 '수 미터'다. 실내 1cm와 야외 수 미터 사이의 이 간극이 조경 AR이 실무 도면 수준에 도달하지 못하는 이유다. 또 특징점 기반이므로 질감 없는 면(잔디밭, 콘크리트 포장, 하늘)과 움직이는 물체(흔들리는 잎, 지나가는 사람)에 취약하다.

### ARKit / ARCore — VIO가 주머니 속으로 들어오다
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple(ARKit) / Google(ARCore). 애플은 2015년 5월 독일 뮌헨의 AR 기업 Metaio를 인수했고, 여기에는 엔지니어 인력과 100건 이상의 AR 특허 출원이 포함됐다. 메타이오 엔지니어들은 애플 Technology Development Group에 합류한 뒤 ARKit 공개를 맞았다. |
| 연도 | ARKit 발표 2017년 6월 WWDC, 출시 2017년 9월(iOS 11). ARCore 발표 2017년 8월(당시 시제품), 정식 출시 2018년 2월 23일 |
| 수치 | ARKit 요구사양: Apple A9 칩 이상. LiDAR 스캐너 기반 기능은 iPhone 12 Pro/Pro Max 이후 및 2020년 이후 iPad Pro. 애플의 Metaio 인수: 2015년 5월, AR 특허 출원 100건 이상 포함. ARKit 확장 경로: iOS 11(2017) → iPadOS 13(2019) → visionOS 1.0(2024). ARCore 정식 출시일 2018년 2월 23일. |
| 출처 | Apple Developer, "ARKit in iOS" (https://developer.apple.com/documentation/arkit/arkit-in-ios); Wikipedia "ARKit" 및 "ARCore" 항목 (Metaio 인수, 출시일). ARCore 기술 설명은 Google, "ARCore overview" 참조. |

위의 SLAM·VIO 계보 전체를 '설치 없이 이미 손에 들려 있는 기기'에 얹은 사건이다. 두 SDK 모두 핵심은 VIO — 카메라 영상의 특징점 추적과 IMU의 관성 적분을 융합해 6자유도 자세를 낸다. 여기에 AR 앱이 실제로 필요로 하는 상위 기능이 붙는다: 평면 검출(바닥·벽 찾기), 광원 추정(가상 물체의 그림자·밝기를 실제 조명에 맞춤), 앵커(특정 지점에 가상 물체를 고정), 그리고 이후의 장면 재구성(공간을 삼각망으로 만듦)과 깊이 지도. 개발자가 SLAM 논문을 읽지 않고도 '이 자리에 나무를 놓아라'라고 쓸 수 있게 됐다.

2017년 이전 AR 연구는 장비 조달이 연구의 절반이었다. 2017년 이후에는 아이폰만 있으면 됐다. 본 조사의 문헌 분포가 이를 그대로 보여준다 — AR 조경·경관 논문이 2014년 14편에서 2021년 61편으로 네 배가 되는데, 꺾이는 지점이 정확히 2019년, 곧 ARKit·ARCore 보급 시점이다. 기술적 도약이 아니라 '유통의 도약'이었고, 결과적으로 연구 총량을 바꿨다.

실내 책상 규모의 상대좌표 추적이다. '이 기기 기준 3m 앞'은 알아도 '이곳이 지구상 어디인가'는 모른다. 세션이 끊기면 지도가 사라져 어제 배치한 가상 수목을 오늘 같은 자리에 다시 띄우지 못한다. 넓은 대지에서 걸어다니면 드리프트가 누적된다. 이 세 가지가 조경 실무에 그대로 걸리며, 이를 풀려는 시도가 다음 항목의 VPS와 클라우드 앵커다. 주의: 'ARCore 2017년 8월 발표'는 시제품 공개였고 정식 SDK 출시는 2018년 2월이다 — 책에서 연도를 쓸 때 둘을 구분해야 한다.

### Microsoft HoloLens — 인사이드아웃 6자유도 추적을 전용 실리콘에 얹다
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft. HPU(Holographic Processing Unit)는 홀로렌즈 전용으로 자체 설계한 보조 프로세서 |
| 연도 | HoloLens 1세대: 발표 2015년 1월, 개발자판 출시 2016년 3월 30일($3,000, 상용판 $5,000). HoloLens 2: 발표 2019년 2월 24일(MWC), 가격 $3,500 |
| 수치 | HoloLens 1: Tensilica 커스텀 DSP 28개, 환경 인식 센서 4개(양측 각 2개), 시야각 120°×120°의 깊이 카메라, 240만 화소 사진/동영상 카메라, 4채널 마이크 배열, 230만 화소 디스플레이(초점 거리 약 2m 고정), RAM 2GB(SoC) + 1GB(HPU), 저장장치 64GB. 실사용 시야각은 시연 기준 추정치 약 30°×17.5°. ─ HoloLens 2: 헤드 트래킹용 가시광 카메라 4개, 시선 추적용 적외선 카메라 2개, 100만 화소 ToF 깊이 센서, IMU(가속도계·자이로·지자기계). 가시광 카메라 초점거리 1.08mm, 대각 시야각 96.1도, 스테레오 기선 98.6mm. 디스플레이 2k 3:2 광학엔진, 홀로그램 밀도 2.5k 라디안(라디안당 광점 수)  |
| 출처 | Microsoft Learn, "HoloLens 2 hardware" (https://learn.microsoft.com/en-us/hololens/hololens2-hardware, 본 조사에서 사양표 직접 확인). HoloLens 1세대 사양·가격·HPU 구성은 Wikipedia "Microsoft HoloLens" 항목. |

외부 기지국 없이 헤드셋 스스로가 자기 위치를 아는 '인사이드아웃 6자유도 추적'을 상용 제품에 처음 실었다. 결정적 설계는 이 계산을 범용 CPU가 아니라 전용 보조칩 HPU에 떠넘긴 것이다. 1세대 HPU는 Tensilica의 커스텀 DSP 28개를 써서 공간 매핑, 제스처 인식, 음성 인식을 전담했다. CPU가 응용프로그램을 돌리는 동안 HPU가 센서 융합과 정합을 계속 돌리므로, 아주마가 지목한 '동적 오차'의 근원인 종단간 지연을 구조적으로 낮출 수 있다. 여기에 광학 시스루 도파관(waveguide) 디스플레이를 결합해, 비디오 합성이 아니라 진짜 '실제 세계 위에 빛을 더하는' 방식을 택했다.

연구실의 천장 LED와 자기식 트래커를 없애고, '쓰고 걸어나가면 그만'인 자립형 정합을 만들었다. 조경 현장처럼 기반시설을 설치할 수 없는 곳에서 AR이 성립하려면 반드시 이 구조여야 한다. 또 정합 계산을 전용 하드웨어로 분리한 발상이 이후 Apple R1으로 이어진다.

세 가지가 남았다. ①시야각 — 1세대의 약 30°×17.5°는 팔 길이에서 손바닥만 한 창으로, 넓은 경관을 담을 수 없다. ②가격 — $3,000~$3,500은 현장 보급 가격이 아니다. ③광학 시스루의 원리적 제약 — 도파관은 빛을 '더하기'만 하므로 검은색을 표현할 수 없고, 야외 직사광선 아래서는 홀로그램이 씻겨 사라진다. 조경 AR의 무대가 대부분 야외임을 생각하면 이 세 번째가 가장 무겁다.

### 비동기 재투영(timewarp / late-stage reprojection) — 예측 트래킹의 산업적 구현
| 항목 | 내용 |
| --- | --- |
| 주체 | Oculus(현 Meta) — Asynchronous Timewarp / Asynchronous Spacewarp. Valve — Interleaved Reprojection, SteamVR Motion Smoothing. Microsoft — Late-Stage Reprojection |
| 연도 | Oculus 비동기 타임워프 도입 2015년경, 비동기 스페이스워프 이후 도입. HoloLens의 late-stage reprojection은 2016년 1세대부터 탑재 |
| 수치 | 참조 하드웨어 — Meta Quest 3(발표 2023년 6월 1일, 출시 2023년 10월 10일, 128GB $499.99 / 512GB $649.99): Snapdragon XR2 Gen 2, 눈당 2064×2208 RGB-스트라이프 LCD 2장, 재생빈도 90~120Hz, 패스스루용 400만 화소 RGB 카메라 2개, 추적용 400×400 화소 적외선 카메라 4개, 적외선 패턴광 투사식 깊이 센서. 아주마의 기준선과 대조: 각오차 0.5도 유지에 필요한 지연 10ms 이하, 60Hz 프레임버퍼 스캔아웃만으로 16.67ms. |
| 출처 | Wikipedia, "Asynchronous reprojection" (기법 분류와 정의). Meta Quest 3 사양은 Wikipedia "Meta Quest 3" 항목. 지연 수치 기준선은 Azuma (1997) 4.3절. |

아주마가 1997년에 '겉보기 지연 줄이기(reduce apparent lag)'로 분류했던 이미지 편향·워핑 기법이 산업 표준이 된 것이다. 원리는 이렇다 — 렌더링 파이프라인은 프레임 하나를 그리는 데 십수 밀리초가 걸린다. 그 사이에 머리는 이미 움직였다. 그래서 완성된 프레임을 화면에 내보내기 직전에, 가장 최신의 자세 측정값을 읽어 이미 그려진 영상을 살짝 회전·이동시켜 보정한다. 회전만 보정하는 것이 타임워프, 깊이 정보를 써서 시차(perspective)까지 보정하는 것이 스페이스워프다. GPU가 목표 프레임레이트를 못 맞출 때도 헤드셋이 머리 움직임에 즉각 반응하는 것처럼 느껴지게 만든다.

'렌더링을 더 빠르게'라는 정면 승부를 포기하고 '마지막 순간에 결과를 고친다'로 우회했다. 아주마가 계산한 대로 각오차 0.5도를 지키려면 지연 10ms 이하가 필요한데, 60Hz 스캔아웃만으로 16.67ms가 든다 — 정면 돌파가 불가능한 문제다. 재투영은 이 불가능을 우회한 해법이고, 오늘날 모든 소비자용 헤드셋이 이것 없이는 성립하지 않는다.

재투영은 이미 그린 그림을 고치는 것이므로 없던 정보를 만들 수 없다. 회전 보정은 거의 완벽하지만, 위치 이동(translation) 보정은 가려졌던 영역에 구멍을 만든다. 움직이는 물체는 왜곡되고, 프레임레이트가 심하게 떨어지면 물체가 겹쳐 보이거나 번지는 현상(judder, ghosting)이 생긴다. 즉 '지연을 감춘' 것이지 '지연을 없앤' 것이 아니다.

### Apple Vision Pro / R1 — 정합 전용 실리콘과 12밀리초
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple. 메인 SoC는 M2(초기)·M5(2025년판), 센서 전담 보조칩이 R1 |
| 연도 | 발표 2023년 6월 5일(WWDC), 미국 출시 2024년 2월 2일. M5 탑재 개정판 2025년 |
| 수치 | R1 칩 12밀리초 photon-to-photon 지연(애플 표현으로 '눈 깜빡임보다 8배 빠르다'). 센서 구성: 고해상도 메인 카메라 2개, 외부 인식용 트래킹 카메라 6개, 시선 추적 카메라 4개, TrueDepth 카메라 1개, LiDAR 스캐너 1개, IMU 4개, 플리커 센서, 주변광 센서. 애플 발표 문구 기준 카메라 12개 + 센서 5개 + 마이크 6개를 R1이 처리. 디스플레이: 마이크로 OLED, 눈당 약 3,660×3,200, 양안 합계 2,300만 화소(우표 크기 패널 2장), 재생빈도 90/96/100/120Hz, 시야각 약 100°×73°. 시선 추적은 고속 카메라와 적외선 LED 링이 눈에 보이지 않는 광 패턴을 투사하는 방식. M5 사양: 10코어 CPU(고성능 4 + 효율 6) |
| 출처 | Apple, "Apple Vision Pro 기술 사양" (https://www.apple.com/apple-vision-pro/specs/ — '12-millisecond photon-to-photon latency' 및 센서 목록 직접 확인); Apple Newsroom, "Introducing Apple Vision Pro" 2023년 6월 5일 (https://www.apple.com/newsroom/2023/06/introducing-apple-vision-pro/) |

홀로렌즈의 HPU 발상을 극단까지 밀어붙인 설계다. M 계열 칩이 앱과 그래픽을 맡고, R1이라는 별도 칩이 오직 센서 입력 처리와 화면 출력만 전담한다. 애플은 이 구조로 '광자에서 광자까지(photon-to-photon)' 12밀리초라는 수치를 공식 사양에 명시했다 — 바깥 세상의 빛이 카메라에 들어와서, 처리를 거쳐, 눈앞 디스플레이의 빛으로 나오기까지의 전체 시간이다. Vision Pro는 광학 시스루가 아니라 비디오 패스스루 방식이므로, 사용자가 보는 '현실'조차 전부 이 12ms만큼 지연된 영상이다. 그래서 이 숫자가 곧 제품의 성립 조건이 된다. 아주마가 1997년에 '각오차 0.5도를 지키려면 10ms 이하가 필요하나 현실적이지 않다'고 적었던 그 선에, 26년 만에 상용 제품이 도달한 것이다.

정합의 병목을 소프트웨어가 아니라 실리콘 배치로 풀었다. 그리고 이 수치를 마케팅 문구가 아니라 기술 사양표의 항목으로 공표했다 — AR 산업에서 지연이 처음으로 '스펙'이 된 사건이다. 조경 서술에 쓸 대목: 아주마가 계산한 '지연 100ms → 팔 길이에서 60mm 어긋남'을 12ms에 대입하면 약 7mm가 된다. 이것이 26년간의 진보를 한 줄로 보여주는 수치다.

12ms는 '센서에서 화면까지'의 지연이지 '정합 정확도'가 아니다. 애플은 가상 물체가 실제 위치에서 몇 밀리미터 어긋나는지는 공표하지 않았다. 또 비디오 패스스루이므로 사용자가 보는 현실 자체가 카메라 해상도·동적 범위·색재현의 한계를 물려받는다 — 야외 직사광선과 그늘이 동시에 있는 조경 현장은 동적 범위 측면에서 가장 가혹한 조건이다. 실외 장시간 착용, 이동 중 사용, 그리고 절대좌표 정합(이 나무가 도면상 어느 좌표인가)은 여전히 미해결이다.

### VPS(Visual Positioning System) — 야외·대규모 절대좌표 정합
| 항목 | 내용 |
| --- | --- |
| 주체 | Google(ARCore Geospatial API, Street View 기반 VPS) / Niantic(Lightship VPS, 사용자 스캔 기반). 현재 Niantic의 지리공간 사업부는 Niantic Spatial로 분리 |
| 연도 | Google 'Live View' 도보 내비게이션 2019년, ARCore Geospatial API 개발자 공개 2022년. Niantic Lightship SDK 공개 2021년 11월, Large Geospatial Model 발표 2024년 11월 |
| 수치 | 구글 VPS: 스트리트뷰 영상 수집 기간 15년 이상, 3차원 점군 계산에 사용한 영상 '수백억 장(tens of billions of images)', 완성된 위치추정 모델은 '조 단위 점(trillions of points)'으로 구성되며 '거의 모든 국가(nearly all countries)'에 걸침. Niantic Lightship SDK 공개 2021년 11월(Unity 기반). |
| 출처 | Google, "ARCore Geospatial API" 개발자 문서 (https://developers.google.com/ar/develop/geospatial — VPS 원리와 규모 수치 직접 확인). Niantic Lightship 출시 시점은 Wikipedia "Niantic, Inc." 항목. |

SLAM·VIO가 못 푸는 마지막 문제, 곧 '여기가 지구상 어디이고 어느 방향을 보고 있는가'를 영상으로 푸는 기술이다. GPS는 수평 오차가 수 미터에 달하고 방위(heading)는 지자기계에 의존해 건물 사이에서 크게 틀어진다. VPS는 대신 거대한 사전 지도와 현재 카메라 영상을 대조한다. 구글의 방식은 이렇다 — 15년 넘게 전 세계에서 촬영한 스트리트뷰 영상을 심층신경망에 통과시켜, 장기간 변하지 않고 알아볼 수 있을 만한 부분(건물 모서리, 간판, 창틀 배열 등)을 골라 기술한다. 수백억 장 규모의 영상에서 뽑은 이 기술자들을 합쳐 조 단위 점으로 된 3차원 점군 모델을 만든다. 사용자 기기가 위치를 요청하면, 신경망이 현재 화면의 픽셀을 이 모델에 대응시켜 GPS보다 훨씬 정확한 위치와 방향을 계산한다. 나이앤틱은 스트리트뷰 대신 포켓몬고 이용자들이 직접 스캔한 영상으로 같은 일을 한다.

상대좌표에서 절대좌표로 넘어갔다. 이전까지 AR 앵커는 '이 세션 안에서만' 유효했다. VPS 이후에는 위도·경도·고도·방위로 앵커를 지정할 수 있어, 어제 다른 사람이 같은 자리에 놓은 가상 수목을 오늘 내 기기에서 같은 자리에 볼 수 있다. 조경에서 이것이 결정적인 이유 — 설계 도면은 본질적으로 절대좌표 문서다. VPS 없이는 AR 조감이 '대충 저쯤'에 머물지만, VPS가 있으면 도면 좌표와 현장 좌표가 연결된다. 구글은 앵커 종류를 세 가지로 나눴다: WGS84(위경도+고도 직접 지정), Terrain(지표면 기준 상대 고도), Rooftop(건물 옥상 기준).

조경에 걸리는 한계가 명확하다. ①VPS는 스트리트뷰 차량이 다닌 길, 곧 도로변에서만 작동한다 — 공원 내부, 산책로 안쪽, 정원 깊숙한 곳은 지도가 없다. ②지도의 근거가 건물·간판 같은 인공 구조물의 안정적 특징이다. 계절마다 모습이 완전히 바뀌는 식생은 오히려 오차원이 된다. ③구글 공식 문서는 정확도를 미터·도 단위 수치로 공표하지 않는다 — 본 조사에서 여러 공식 페이지를 확인했으나 수평·고도·방위 정확도의 구체적 임계값을 찾지 못했다. 책에 '몇 센티미터 정확도'라고 쓰면 안 된다. ④서비스가 사업자 인프라에 종속된다 — 나이앤틱의 지리공간 자산이 2025년 기업 분할을 거친 사실이 이 위험을 보여준다.

### 남은 문제 — 야외·식생·대규모 환경의 정합
| 항목 | 내용 |
| --- | --- |
| 주체 | 해당 없음(계보 전체의 공백) |
| 연도 | 1997년 Azuma가 제기, 2026년 현재 미해결 |
| 수치 | 비교 기준선 — 아주마가 제시한 이상적 요구치: 트래커 정확도 약 1mm 및 1도의 작은 분수, 인간 눈의 분해 한계 1분각(0.017도). 현재 도달치: ORB-SLAM 실내 1cm 이하 / 야외 수 미터, MSCKF 3.2km 주행에 0.31% 오차(=10m), Vision Pro 지연 12ms(아주마 기준 각오차 0.5도 유지에 필요한 10ms에 근접). |
| 출처 | Azuma (1997) 4.5절 "Current status" 원문(본 조사에서 전문 추출); 현재 도달치는 위 각 항목의 원논문·공식 사양에서 인용. |

위 11개 항목을 관통하는 미해결 지점을 하나로 묶으면 이렇게 된다. 첫째, 절대 스케일 — 단안 SLAM은 크기를 모르고, IMU·스테레오·LiDAR가 이를 메우지만 야외 장거리에서는 여전히 누적 오차가 남는다. 둘째, 비정적 장면 — PTAM 이래 모든 특징점 SLAM이 '장면이 비교적 정적일 것'을 전제한다. 바람에 흔들리는 수관, 계절마다 형태가 바뀌는 낙엽수, 물결치는 수면은 이 전제를 정면으로 깬다. 셋째, 질감 없는 표면 — 잔디밭, 균질한 포장, 하늘은 특징점을 주지 않는다. 넷째, 조명 — 야외 직사광선은 광학 시스루의 홀로그램을 씻어내고, 그늘과 양지가 공존하는 장면은 패스스루 카메라의 동적 범위를 넘는다. 다섯째, 규모 — ORB-SLAM의 자기 보고로도 실내 1cm 대 야외 수 미터다. 설계 도면이 요구하는 정밀도와 두 자릿수 이상 차이가 난다.

도약이 아니라 도약의 부재를 기록하는 항목이다. 1997년 아주마가 '정합 문제는 전혀 해결되지 않았다'고 적은 이유(시점이 고정되었거나, 물체가 고정되었거나, 이동이 제한되거나, 기준마커가 붙은 하나의 물체에만 작동)를 오늘의 조경 조건에 대입하면 항목별 성적이 갈린다. 시점 이동은 해결됐다(VIO·SLAM). 마커 의존은 해결됐다(markerless SLAM). 절대좌표는 부분적으로 해결됐다(VPS, 단 도로변 한정). 그러나 '움직이고 계절마다 변하는 자연물'에 대한 정합은 1997년 이후 실질적 진전이 없다. 조경 AR이 교육·개념 시연에는 두텁고 실무 도면 검증에는 얇은 이유가 여기 있다.

이 항목 자체가 한계의 목록이다. 다만 서술상 주의할 점 — '아직 안 된다'가 '영영 안 된다'는 아니다. 최근의 신경 표현(NeRF·3D Gaussian Splatting) 계열과 대규모 지리공간 모델이 비정적·비질감 장면 문제를 다른 방향에서 공략하고 있으나, 본 조사에서는 그 실제 정합 정확도 수치를 확인하지 못했다.

#### 검증에서 잡힌 정정
- [확정 오류] ARToolKit 항목 '실험 장비: 263×234 픽셀 카메라' → 틀림. 263×234는 카메라가 아니라 Virtual i-O i-glasses HMD의 디스플레이 해상도다. 원문: "The iglasses are full color, can be used in either a see-through or occluded mode and have a resolution of 263x234 pixels." 논문은 헤드마운트 카메라의 화소수를 명시하지 않는다. 명시된 장비 수치는 SGI O2(R5000SC 180MHz)와 처리속도 7~10fps(전체)/10~15fps(화이트보드 제외)다.
- [제조사값 충돌] HoloLens 1세대 'Tensilica 커스텀 DSP 28개' → 24개일 가능성이 매우 높고, 28은 DSP 개수가 아니라 공정 노드(TSMC 28nm)로 보인다. 위키백과 Tensilica 항목: "Microsoft HoloLens incorporates a custom coprocessor fabricated on TSMC's 28nm process node, integrating 24 Tensilica DSP cores." 반면 조사가 인용한 위키백과 Microsoft HoloLens 항목은 "28 custom DSPs from Tensilica"로 자기모순이다. Microsoft Learn의 현행 공식 사양 문서에는 DSP 개수 자체가 없어 이번 조사에서 제조사 공식값 확정에는 실패했다(웹검색 쿼터 소진, 검색엔진 CAPTCHA로 Hot Chips 2016 1차 자료 접근 불가).
- [출처 귀속 오류] Vision Pro '눈당 약 3,660×3,200'과 '시야각 약 100°×73°'를 애플 공식 사양(apple.com/apple-vision-pro/specs)에서 확인했다고 적었으나, 애플 공식 페이지에는 눈당 해상도도 시야각도 없다. 애플이 공표하는 값은 '23 million pixels'(양안 합계)와 '우표 크기 패널 2장'뿐이다. 3,660×3,200과 100°×73°는 위키백과 사양표/제3자 추정치이며 제조사 공식값이 아니다.
- [세대 혼재] Vision Pro '재생빈도 90/96/100/120Hz' → 2024년 출시 M2 모델의 공식 최대는 100Hz(90/96/100Hz)이고, 120Hz는 2025년 M5 개정판(2025-10-15 발표, 10-22 출시)부터다. 두 세대 사양을 한 줄로 합쳐 적었다.
- [조건 누락] ORB-SLAM '루프 후보 검색 39ms(특징 추출 포함)' → 원문은 "requiring less than 39ms (including feature extraction) to retrieve a loop candidate from a 10K image database"로 (1) '39ms 미만'이고 (2) '1만 장 DB' 조건이 붙으며 (3) ORB-SLAM 자체의 측정치가 아니라 저자들의 선행 인식기(DBoW2 기반) 논문 결과를 인용한 값이다.
- [맥락 왜곡] MSCKF '카메라 3Hz + IMU 100Hz(주목 — IMU가 카메라보다 33배 빠르다)' → 3Hz는 설계상의 선택이 아니라 기록 제약이다. 원문: "images were only recorded at 3Hz due to limited hard disk space on the test system." 또한 14Hz 처리 역시 실시간 온라인 구동이 아니라 "processing was done off-line"인 오프라인 재처리 성능이다.
- [실험 귀속 혼동] ARToolKit '사용자 실험의 눈–마커 거리 300/400/800mm'는 마커 검출 정확도 실험이 아니라 6.2절 HMD 캘리브레이션 평가(task 1/2/3, 사용자 A~D)의 조건이다. 마커 검출 정확도 실험(6.1절, 80mm 마커)의 측정 거리 범위는 그림 10·11 기준 0~700mm이며, 이 실험에는 300/400/800mm 구분이 없다.
- [근거 없음] '홀로렌즈의 late-stage reprojection은 2016년 1세대부터 탑재'는 조사가 인용한 위키백과 'Asynchronous reprojection' 문서에 전혀 나오지 않는다. 해당 문서가 제시하는 날짜는 Oculus ATW 2015-03-02, ASW 2016-11-10, Valve Interleaved Reprojection 2016-03-26, SteamVR Motion Smoothing 2018-11-27뿐이다. 이번 조사에서 1세대 탑재 시점은 확인하지 못했다.
- [비교 축 불일치] '남은 문제' 절의 'Vision Pro 지연 12ms가 아주마 기준 10ms에 근접' → 애플의 12ms는 패스스루 영상의 photon-to-photon 지연이고, 아주마의 10ms는 머리 회전 50도/초에서 각오차 0.5도를 유지하기 위한 트래킹 종단간 지연이다. 서로 정의가 다른 값이라 '근접'이라는 직접 비교는 성립하지 않는다.
- [선후 역전] MSCKF는 ICRA 2007(2007년 4월, 로마), PTAM은 ISMAR 2007(2007년 11월, 나라)로 MSCKF가 약 7개월 앞선다. 보고서는 PTAM → MSCKF 순으로 배열해 'PTAM 이후에 VIO가 나왔다'는 인상을 준다. 둘 다 '2007년'이라 연도만으로는 드러나지 않으므로 월까지 명시해야 함.
- [계보 오귀속] '비동기 재투영 = 예측 트래킹(Azuma&Bishop 1994)의 산업적 구현'은 틀렸다. Azuma(1997) 4.4절은 동적 오차 대책을 4범주로 나누고, timewarp의 원형인 image deflection을 '2) Reduce apparent lag'에, prediction을 '4) Predict'에 **따로** 넣는다. 원문: 'Image deflection is a clever technique for reducing the amount of apparent system delay ... Therefore, it is a feed-forward technique. ... Then just before scanout, the system reads the most recent orientation report'이며 출처는 [Burbidge89][Regan94][Riner92][So92]. 즉 timewarp의 선행 문헌은 1989~1994년으로 Azuma
- [연도 정밀화 필요] ARToolKit '라이브러리 v1.0 배포 2001년'은 오해를 부른다. 라이브러리는 1999년부터 존재했고, 2001년은 ARToolWorks 설립과 함께 HIT Lab을 통해 **오픈소스판** v1.0이 공개된 해다(en.wikipedia.org/wiki/ARToolKit). DAQRI 재공개는 '2015년'이 아니라 **2015년 5월 13일 v5.2**로 날짜까지 특정 가능.
- [출처 충돌·미해결] 加藤博一의 1999년 소속을 보고서는 Hiroshima City University로 적었고 IWAR'99 원문 PDF도 'Faculty of Information Sciences, Hiroshima City University'로 확인된다(보고서가 맞음). 그러나 영문 위키백과는 'developed by Hirokazu Kato of Nara Institute of Science and Technology in 1999'로 적고 있어 2차 출처와 충돌한다 — 보고서에 이 충돌을 명시하지 않으면 독자가 위키를 보고 오류로 오인한다.
- [선행자 누락] ARKit/ARCore 항목이 Metaio(2015)만 계보로 달고 Google Project Tango를 빠뜨렸다. Tango는 2014년 공개(위키 출시일 2014-06-05), Peanut 폰·Yellowstone 태블릿(2014)·Lenovo Phab 2 Pro(2016)·Asus ZenFone AR(2017)로 이미 소비자 기기에 VIO+깊이를 넣었고, 구글은 2017-12-15에 종료를 발표해 **2018년 3월 1일** 지원을 끊었다 — ARCore 1.0 정식 출시(2018-02-23) 불과 1주 뒤다. 'VIO가 2017년에 주머니로 들어왔다'는 서술은 2014~2017년 Tango 구간을 지운다.
- [세대 혼합] Apple Vision Pro '재생빈도 90/96/100/120Hz'는 **2025년 M5 개정판** 기준이다(현행 apple.com 사양 페이지). 2024년 2월 출시된 초기 M2 모델은 최대 100Hz(90/96/100)이며 120Hz는 지원하지 않는다. 보고서는 '발표 2023·출시 2024' 제품 설명에 2025년 사양을 섞었다.
- [출처 오기] Vision Pro '시야각 약 100°×73°'와 '눈당 약 3,660×3,200'을 apple.com/apple-vision-pro/specs/ 에서 직접 확인했다고 적었으나, 애플 공식 사양 페이지에는 **FOV도 눈당 해상도도 없다**. 공식 표기는 '23 million pixels', '마이크로 OLED', '7.5-micron pixel pitch'뿐이며, 두 수치는 위키백과 등 제3자 추정치다(위키: '~100°×73°', '약 3660×3200').
- [내부 모순] Vision Pro 센서 열거(메인 2 + 트래킹 6 + 시선 4 + TrueDepth 1 = 카메라 13개)와 같은 문단의 애플 발표 문구 '카메라 12개 + 센서 5개 + 마이크 6개'(2023-06-05 뉴스룸 원문 'processes ... 12 cameras, five sensors, and six microphones')가 서로 맞지 않는다. 애플 자료 자체의 불일치이므로 그대로 병기하지 말고 주석을 달아야 한다.
- [1차 출처 확인 실패] HoloLens 1세대 'Tensilica 커스텀 DSP 28개'는 이번 세션에서 확정할 수 없었다. 근거는 영문 위키백과 문장 'The HPU uses 28 custom DSPs from Tensilica' 하나뿐이고 그 각주는 Ars Technica 2016-08-23 기사 1건인데 arstechnica.com과 web.archive.org 모두 이 환경에서 차단됐다. 마이크로소프트 공식 1세대 하드웨어 문서(learn.microsoft.com/en-us/hololens/hololens1-hardware)는 현재 404이고, 공식 HoloLens 2 문서는 HPU 1.0의 DSP 수를 적지 않는다. 'DSP 24개'라는 수치도 널리 유통되므로 '28(2차 출처 1건, 1차 출처 미확인)'로 낮춰 표기할 것.
- [소속 오기] MonoSLAM 저자 소속 'Imperial College London / Oxford'는 절반만 맞다. TPAMI 2007 원문 각주: Davison=Department of Computing, Imperial College / Reid=Robotics Research Group, University of Oxford / **Molton=Imagineer Systems Ltd, Surrey Technology Centre, Guildford** / **Stasse=Joint Japanese-French Robotics Laboratory(JRL), CNRS/AIST, 일본 쓰쿠바**.
- [선후 과장] ARToolKit을 마커 기반 정합의 출발점처럼 배치했으나, 폐쇄루프 피듀셜 정합은 3~4년 앞선다. Azuma(1997) 4.5절 원문: 'Closed-loop systems, however, have demonstrated nearly perfect registration, accurate to within a pixel [Bajura95][Mellor95a][Mellor95b][Neumann96][State96a]' — 즉 1995~96년에 이미 1픽셀 정합이 보고됐다. Kato&Billinghurst(1999)의 기여는 정합 정확도의 발명이 아니라 **배포 가능한 표준 도구화**로 한정해야 한다.
- [선후 과장] 'MSCKF = VIO의 원형'은 과하다. 시각-관성 융합 자체는 1990년대에 이미 있었다. Azuma(1997)는 하이브리드(관성+광학) 트래커를 미래 해법으로 지목하며 [Azuma93][Durlach95][Foxlin96][Zikan94b]를 인용하고, '관성 센서를 쓰면 예측이 2~3배 정확해진다'고 적는다(1994~96년 실적). MSCKF의 원조성은 '다중상태 제약(multi-state constraint) EKF 정식화'에 국한된다.
- [맥락 누락] ORB-SLAM '루프 후보 검색 39ms(특징 추출 포함)'는 본 시스템의 측정치가 아니다. 원문은 선행 인식기(DBoW2 기반)를 설명하며 'requiring less than 39ms (including feature extraction) to retrieve a loop candidate from a **10K image database**'라고 적고, 본 논문은 그 개선판을 쓴다고 이어간다. DB 규모(1만 장)와 '선행 연구 수치'라는 단서를 빼면 과장된다.
- [날짜 누락] HoloLens 2는 발표 2019-02-24(MWC)만 적혀 있는데 실제 출하는 **2019년 11월 7일**이다(영문 위키). 발표-출하 간격(약 8.5개월)이 1세대(2015-01-21 발표 → 2016-03-30 출하)와 비교되는 지점이므로 연대표에 필요하다.
- [미확인] 'Google Live View 도보 내비게이션 2019년'과 'ARCore Geospatial API 개발자 공개 2022년'의 정확한 날짜는 이번 세션에서 1차 확인 못 함(웹검색 쿼터 소진, Google Maps 위키 문서에 Live View 발표일·VPS 언급 없음). 다만 구글의 VPS 개념 자체는 2022년보다 앞서 I/O에서 Tango 기반 실내 측위로 먼저 공개된 것으로 알려져 있어, '2022년 공개'를 VPS의 시작점처럼 읽히게 두면 선후가 왜곡될 수 있다 — 확인 필요 항목으로 남김.
- [미확인] Niantic 'Lightship SDK 공개 2021년 11월'은 확인됨(위키: 'In November 2021, Niantic launched the Lightship SDK'). 그러나 **Lightship VPS 자체의 공개 시점(2022년 5월로 알려짐)**과 Large Geospatial Model 발표일(2024-11로 서술)은 확인 못 했다 — Niantic 공식 블로그 URL이 scopely.com으로 301 이전된 뒤 404다. Niantic Spatial 분사는 확인됨(Scopely 인수 완료 2025-05-29, 지리공간 사업 분사).
- [확정 오류] ARToolKit 항목 '실험 장비: 263×234 픽셀 카메라' → 틀림. Kato&Billinghurst(1999) 원문: "The iglasses are full color, can be used in either a see-through or occluded mode and have a resolution of 263x234 pixels." 즉 263×234는 Virtual i-O iglasses **HMD 디스플레이** 해상도다. 카메라 해상도는 논문에 명시되지 않았다. 함께 빠진 실제 사양: 연산기는 SGI O2(R5000SC 180MHz CPU), 성능은 풀버전 7~10fps / 공유 화이트보드 제외 시 10~15fps.
- [확정 오류] MonoSLAM 저자 소속 '(Imperial College London / Oxford)' → 틀림. TPAMI 원문 각주: Davison=Imperial College London(Dept. of Computing), Reid=University of Oxford(Robotics Research Group), **Molton=Imagineer Systems Ltd(Guildford, UK)**, **Stasse=Joint Japanese-French Robotics Laboratory(JRL), CNRS/AIST, 일본 쓰쿠바**. 4인 중 2인이 영국 두 대학 소속이 아니다.
- [출처 불일치] HoloLens 1세대 'RAM 2GB(SoC) + 1GB(HPU)' → 인용 출처인 위키백과 'Microsoft HoloLens' 원문은 "The SoC and the HPU **each have 1GB LPDDR3** and share 8MB SRAM"이다. 즉 SoC 1GB + HPU 1GB(합계 2GB)이며, 8MB SRAM 공유는 누락됐다. (마이크로소프트의 옛 공식 hololens1-hardware 페이지는 현재 404로 내려가 제조사 공식값으로 교차확인 불가.)
- [출처 없음] Apple Vision Pro '눈당 약 3,660×3,200' 및 '시야각 약 100°×73°' → 애플 공식 사양표(apple.com/apple-vision-pro/specs)에는 **눈당 해상도도 시야각도 전혀 게재되어 있지 않다**(직접 확인). 애플이 공개한 값은 '23 million pixels', 'Micro-OLED', '7.5-micron pixel pitch'뿐이다. 두 수치는 제3자 분해분석·패널 공급망 추정치이므로 애플 출처로 표기하면 안 된다.
- [연대 혼동] Vision Pro '재생빈도 90/96/100/120Hz' → 120Hz는 2025년 M5 개정판에서 추가된 값이다. 2024년 출시 초기 M2 모델의 지원 재생빈도는 90/96/100Hz였다. 항목이 '초기 M2·2025년 M5'를 함께 묶어 서술하므로 세대 구분 없이 120Hz를 쓰면 오도한다. (현재 애플 사양표는 M5 기준으로 '90Hz, 96Hz, 100Hz, 120Hz' 표기 — 직접 확인)
- (외 7건)

## rendering
항목 13개 · 검증 정정 지적 44건


### 포비티드 렌더링의 생리학적 근거 — 중심와(fovea)와 이심률에 따른 시력 저하
| 항목 | 내용 |
| --- | --- |
| 주체 | Christine A. Curcio, Kenneth R. Sloan, Robert E. Kalina, Anita E. Hendrickson (해부학 정본, 1990) / 요약 집계는 Wikipedia 'Fovea centralis' |
| 연도 | 1990 (Curcio 등 광수용체 밀도 측정) — 이 원리를 그래픽스에 끌어온 것은 1990년대 이후 |
| 수치 | 중심와 지름 1.5mm ≈ 시야각 5°; 중심소와 0.35mm ≈ 1°; 무혈관대 0.5mm ≈ 1.5°; 최대 원뿔세포 밀도 약 147,000개/mm²(개인 범위 <100,000 ~ >324,000); 중심소와 50개/100μm vs 주변부 12개/100μm; 시신경 섬유의 약 50%가 중심와 담당 |
| 출처 | Curcio CA, Sloan KR, Kalina RE, Hendrickson AE (1990), "Human photoreceptor topography," Journal of Comparative Neurology 292(4):497-523 / 집계: https://en.wikipedia.org/wiki/Fovea_centralis |

사람 눈의 망막은 균질하지 않다. 중심와는 지름 약 1.5mm로 시야각 약 5°에 해당하고, 그 한복판의 중심소와(foveola)는 지름 0.35mm, 시야각 약 1°에 불과하다. 이 좁은 영역에 원뿔세포가 극단적으로 밀집해 있어 최대 밀도가 약 147,000개/mm²에 이른다(개인차가 커서 100,000개/mm² 미만도, 324,000개/mm² 초과도 드물지 않다). 중심소와에서는 100μm당 원뿔세포가 50개인 반면 주변부(perifovea)에서는 12개로 떨어진다. 시신경 섬유의 약 절반이 이 중심 2°의 정보를 나른다. 즉 사람은 시야 전체를 고해상도로 보고 있다고 '느끼지만' 실제로 고해상도로 받아들이는 것은 손을 뻗어 엄지손톱을 세웠을 때 그 손톱이 가리는 정도의 면적뿐이다. 나머지는 눈을 굴려(saccade) 순간순간 채워 넣은 기억의 합성이다. 렌더링 입장에서 이것은 명백한 낭비다 — 시선이 닿지 않는 화소를 중심와와 똑같은 정밀도로 계산하고 있기 때문이다.

'화면 전체를 균일하게 그린다'는 컴퓨터 그래픽스의 암묵적 전제를 깨뜨린 생리학적 근거. 눈이 요구하는 정보량 자체가 시야 중심에 몰려 있으므로, 시선을 알면 렌더링 비용을 원리적으로 한 자릿수 이상 줄일 수 있다는 결론이 따라 나온다.

원뿔세포 밀도의 개인차가 3배 이상이라 '표준 눈'을 가정한 포비티드 파라미터는 일부 사용자에게 과하거나 부족하다. 또한 밀도는 정적 해부 수치일 뿐, 주변시가 여전히 민감한 움직임·플리커·대비 변화는 설명하지 못한다(이것이 뒤의 시간적 안정성 문제로 이어진다).

### Foveated 3D Graphics — 포비티드 렌더링의 원형 논문
| 항목 | 내용 |
| --- | --- |
| 주체 | Brian Guenter, Mark Finch, Steven Drucker, Desney Tan, John Snyder (Microsoft Research) |
| 연도 | 2012 (ACM SIGGRAPH Asia, 2012년 11월 발표) |
| 수치 | 1920×1080 데스크톱 HD 화면에서 5~6배 가속 / 셰이딩 화소 수 10~15배 감소 / 이심률 계수 1.32~1.65 arcmin per degree / 레이어 3겹 / 저자들은 시야 70°의 더 크고 선명한 미래 디스플레이에서는 100배까지 가능하다고 예측 |
| 출처 | https://www.microsoft.com/en-us/research/publication/foveated-3d-graphics/ (ACM Trans. Graph. 31(6), SIGGRAPH Asia 2012) |

시선 추적기로 응시점을 받아, 그 점을 중심으로 세 겹의 이미지 레이어를 동심원처럼 쌓아 렌더링한다. 안쪽 레이어는 좁지만 화소 밀도가 높고, 바깥 레이어로 갈수록 각도상 면적은 커지지만 샘플링 비율은 뚝 떨어진다. 세 레이어를 각각 그린 뒤 합성해 최종 화면을 만든다. 저자들은 사용자 실험으로 '어느 정도까지 해상도를 떨어뜨려도 사람이 눈치채지 못하는가'를 측정해 이심률 1도당 1.32~1.65 각분(arc minute)이라는 기울기 값을 얻었고, 이 값이 이후 거의 모든 포비티드 렌더링 구현의 파라미터 기준이 된다. 1920×1080 데스크톱 화면에서 셰이딩하는 화소 수를 10~15배 줄여 실제 렌더링 속도를 5~6배 끌어올렸다.

이전까지 포비티드 아이디어는 개념 수준이었다. 이 논문은 (1) 다층 레이어라는 구현 가능한 구조, (2) 사람이 눈치채지 못하는 한계를 실측한 파라미터, (3) 실제 GPU에서의 속도 향상 수치를 한꺼번에 제시했다. '시선을 알면 그래픽스는 근본적으로 싸진다'는 명제를 처음으로 숫자로 증명한 논문.

주변부를 단순히 흐리게 하면 시간적 깜박임(temporal aliasing)이 생겨 오히려 눈에 띈다. 또 시선 추적 지연이 크면 눈이 먼저 도착하고 고해상도 영역이 뒤늦게 따라오는 것이 보인다 — 이 두 문제는 각각 2016년(Patney)과 2017년(Albert)에 가서야 정면으로 다뤄진다.

### Towards Foveated Rendering for Gaze-Tracked Virtual Reality — 대비 보존과 시간적 안정성
| 항목 | 내용 |
| --- | --- |
| 주체 | Anjul Patney, Marco Salvi, Joohwan Kim, Anton Kaplanyan, Chris Wyman, Nir Benty, David Luebke, Aaron Lefohn (NVIDIA Research) |
| 연도 | 2016 (ACM Transactions on Graphics, SIGGRAPH Asia 2016) |
| 수치 | 셰이딩 횟수 최대 70% 감소 / 중심와로부터 30° 더 가까운 지점까지 성긴 셰이딩 허용 / 대비 보정 시 수용 가능한 흐림 반경 2배 증가 |
| 출처 | https://research.nvidia.com/publication/2016-12_towards-foveated-rendering-gaze-tracked-virtual-reality (ACM Trans. Graph. 35(6), SIGGRAPH Asia 2016) |

Guenter 방식의 약점 — 주변부를 흐리게 하면 사람이 '뭔가 이상하다'고 느낀다 — 를 지각 실험으로 파고들었다. 핵심 발견은 사람의 주변시가 해상도에는 둔감하지만 대비(contrast)에는 민감하다는 것이다. 그래서 주변부를 저해상도로 그린 뒤 후처리 필터로 대비를 다시 살려주면, 같은 흐림 정도에서도 사람이 훨씬 잘 참는다. 실험 참가자들은 대비 보정이 들어갔을 때 최대 2배 큰 흐림 반경까지 수용했다. 그 결과 Guenter 등의 방식보다 중심와에서 30도나 더 가까운 지점부터 셰이딩을 성기게 할 수 있었고, 셰이딩 횟수를 최대 70% 줄였다. 또 결과 영상이 시간적으로 안정적이어서, 시간 필터를 건 비포비티드 렌더링과 비슷한 품질을 냈다.

포비티드 렌더링의 병목이 '화소 수'가 아니라 '지각 품질'임을 밝혔다. 단순히 덜 그리는 것이 아니라 '사람이 놓치지 않는 신호(대비)는 복원하고 놓치는 신호(고주파 세부)만 버린다'는 지각 기반 렌더링의 문법을 세웠다. 오늘날 Quest Pro·PSVR2의 포비테이션 맵 설계가 모두 이 계보에 있다.

대비 보정 필터 자체가 연산 비용이고, 콘텐츠 종류(텍스트·가는 선·격자 무늬)에 따라 오히려 아티팩트를 키운다. 조경 설계 도면처럼 가는 선과 텍스트가 많은 콘텐츠는 포비테이션에 가장 불리한 종류다.

### Latency Requirements for Foveated Rendering in Virtual Reality — 시선 추적이 얼마나 빨라야 하는가
| 항목 | 내용 |
| --- | --- |
| 주체 | Rachel Albert (UC Berkeley / NVIDIA), Anjul Patney, David Luebke, Joohwan Kim (NVIDIA) |
| 연도 | 2017 (ACM Transactions on Applied Perception, SAP 2017 특집호) |
| 수치 | 추가 지연 20~40ms: 수용 포비테이션 수준 저하 없음 / 80~150ms: 뚜렷한 저하 / 권고 전체 시스템 지연 허용치 50~70ms |
| 출처 | https://research.nvidia.com/publication/2017-09_latency-requirements-foveated-rendering-virtual-reality (ACM Trans. Appl. Percept. 14(4)) |

포비티드 렌더링에서 가장 자주 얼버무려지는 숫자 — '시선 추적이 얼마나 빨라야 하는가'를 정면으로 실측한 논문. 눈이 도약안구운동(saccade)으로 새 지점에 도착했는데 고해상도 영역이 아직 따라오지 못하면, 사용자는 주변부의 열화를 직접 보게 된다. 저자들은 시선 추적 지연을 인위적으로 늘려가며 참가자가 수용하는 포비테이션 강도를 측정했다. 결과: 추가 지연이 20~40ms 범위에 머무르면 수용 가능한 포비테이션 수준이 거의 떨어지지 않지만, 80~150ms에 이르면 뚜렷하게 떨어진다. 이로부터 시선 추적부터 화면 갱신까지 전체 시스템 지연의 허용 한계를 50~70ms로 제안했다.

'시선 추적 하드웨어가 몇 Hz여야 하는가'라는 구매·설계 질문에 처음으로 근거 있는 답을 준 연구. 이 50~70ms라는 예산이 이후 상용 HMD의 시선 추적 카메라 프레임레이트(예: Varjo XR-4의 200Hz)와 렌더링 파이프라인 설계의 기준선이 됐다.

50~70ms는 '평균적으로 참을 만한' 값이지 '알아채지 못하는' 값이 아니다. 또 실험은 특정 콘텐츠·특정 포비테이션 강도 조건이므로, 고대비 텍스트나 빠른 시선 이동이 잦은 작업(도면 검토 등)에서는 더 엄격한 예산이 필요할 가능성이 높다.

### 가변 셰이딩률(Variable Rate Shading)과 Quest Pro의 시선 추적 포비테이션(ETFR)
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft (Direct3D 12 VRS 사양) · NVIDIA (Turing 아키텍처 하드웨어 VRS) · Meta (Quest Pro ETFR/FFR) |
| 연도 | VRS: 2018~2019년 (NVIDIA Turing 출시 2018, D3D12 VRS 문서 2019-04) / Quest Pro ETFR: 2022년 출시 |
| 수치 | D3D12 Tier 2 타일 크기 8·16·32 텍셀 / 셰이딩률 1x1·1x2·2x1·2x2 필수, 2x4·4x2·4x4 선택 / 셰이딩률 이미지 포맷 DXGI_FORMAT_R8_UINT(타일당 1바이트) / NVIDIA Turing: 16×16 화소 타일, 7가지 셰이딩률, 샘플당 1회 ~ 16샘플당 1회 / ETFR 요건: Vulkan 전용, Multiview 필수, Quest Pro 한정 |
| 출처 | https://learn.microsoft.com/en-us/windows/win32/direct3d12/vrs · https://developer.nvidia.com/vrworks/graphics/variablerateshading · https://developers.meta.com/horizon/documentation/unity/unity-eye-tracked-foveated-rendering/ |

포비티드 렌더링이 논문에서 제품으로 내려오려면 GPU가 '화면 영역마다 다른 정밀도로 셰이딩하라'는 명령을 하드웨어로 받아들여야 한다. 그것이 가변 셰이딩률(VRS)이다. Direct3D 12의 Tier 2 VRS는 화면 전체를 8·16·32 텍셀짜리 정사각 타일로 나누고, 타일마다 1바이트짜리 '셰이딩률 이미지'로 정밀도를 지정한다. 셰이딩률은 1x1(화소마다 한 번)부터 1x2·2x1·2x2가 모든 하드웨어에서, 2x4·4x2·4x4가 선택적으로 지원된다. 4x4면 16개 화소를 한 번만 셰이딩하고 결과를 복사하는 것이다. NVIDIA Turing은 16×16 화소 타일에 7가지 셰이딩률을 지원하며, 가시성 샘플당 1회(슈퍼샘플링)부터 16 샘플당 1회까지 조절된다. 중요한 것은 깊이·스텐실·커버리지는 언제나 전체 샘플 해상도로 계산된다는 점이다 — 실루엣은 뭉개지지 않고 셰이딩(빛·재질 계산)만 싸진다. Meta Quest Pro는 이 위에 시선 추적을 얹은 ETFR을 올렸다. 시선 없이 렌즈 왜곡만 보고 화면 가장자리를 낮추는 고정 포비테이션(FFR)과 달리, ETFR은 응시점을 실제 해상도로 그리고 주변을 더 공격적인 포비테이션 맵으로 낮춘다. 단 Vulkan + Multiview 스테레오 렌더링이 필수다.

소프트웨어 트릭(여러 번 렌더링해 합성)으로 하던 것을 래스터라이저 단계의 하드웨어 기능으로 내려, 포비테이션의 오버헤드를 사실상 0에 가깝게 만들었다. 이것이 없었다면 모바일 SoC를 쓰는 독립형 HMD에서 포비티드 렌더링은 수지가 맞지 않았다.

Meta 문서는 ETFR이 'FFR보다 평균적으로 GPU 절감이 크다'고만 쓰고 구체적 퍼센트를 공개하지 않는다. 또 거친 화소는 화면공간 미분값을 키워 밉맵 선택을 흐리게 만들므로, 텍스처가 예상보다 더 흐려지는 부작용을 셰이더에서 보정해야 한다.

### Apple Vision Pro — 마이크로 OLED 2,300만 화소와 R1의 12ms 광자-대-광자 지연
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple Inc. (디스플레이 패널은 Sony 공급으로 널리 보도됨 — 다만 Apple 공식 사양서에는 공급사 명기 없음) |
| 연도 | 발표 2023년 6월 5일(WWDC) / 미국 출시 2024년 2월 2일 / M5 탑재 개정판 발표 2025년 10월 15일 |
| 수치 | 양안 합계 2,300만 화소 / 화소 피치 7.5μm / DCI-P3 92% / 주사율 90·96·100·120Hz / R1 광자-대-광자 지연 12ms / 메모리 대역폭 256GB/s / 시선 추적 카메라 4대 / 전방 추적 카메라 6대 + 메인 카메라 2대 + TrueDepth + LiDAR + IMU 4개 / 패널 대각 1.41인치 |
| 출처 | https://www.apple.com/apple-vision-pro/specs/ (공식) · https://en.wikipedia.org/wiki/Apple_Vision_Pro (눈당 해상도·시야각 등 3자 출처) |

양안 합계 2,300만 화소를 우표 크기의 마이크로 OLED 패널 두 장에 담았다. 화소 피치는 7.5마이크로미터로, 일반 스마트폰 OLED의 수십분의 일 수준이다(비교하자면 사람 머리카락 굵기가 약 70μm이니 화소 하나가 머리카락 굵기의 10분의 1이다). 색역은 DCI-P3의 92%를 덮고, 90·96·100·120Hz 주사율을 지원한다. 눈에 띄는 것은 R1 보조 칩이다. M2가 앱을 돌리는 동안 R1은 카메라 12대·센서 5개·마이크 6개의 입력만 전담해, 실제 세계의 빛이 카메라에 들어와 다시 디스플레이에서 광자로 나오기까지 12밀리초를 보장한다. 메모리 대역폭은 256GB/s. 시선 추적은 전용 적외선 카메라 4대와 LED 링으로 이뤄지며, 이 시선 정보가 포비티드 렌더링과 사용자 입력(응시+손가락 탭)을 동시에 구동한다. visionOS는 앱이 직접 포비테이션을 구현하지 않아도 컴포지터 단계에서 적용한다.

'헤드셋 화질'의 기준선을 통째로 올렸다. 화소 피치 7.5μm 마이크로 OLED는 그전까지 시제품에만 있던 것이고, 12ms 광자-대-광자 지연은 비디오 패스스루가 '화면을 본다'가 아니라 '창밖을 본다'에 가까워진 첫 사례다. 렌더링 관점에서는 2,300만 화소를 90Hz 이상으로 전부 그리는 것이 불가능하므로, 포비티드 렌더링이 선택지가 아니라 전제 조건이 된 첫 상용 제품이기도 하다.

Apple은 눈당 해상도와 시야각을 공식 사양서에 쓰지 않는다. 널리 인용되는 눈당 3,660×3,200과 시야 약 100°×73°는 3자 분석·분해에서 나온 값이며 Apple이 확인한 적 없다. 또 12ms는 Apple의 자체 측정치이며 독립 검증된 수치가 아니다.

### 수렴-조절 불일치(Vergence-Accommodation Conflict) — AR·VR이 눈을 피로하게 만드는 근본 원인
| 항목 | 내용 |
| --- | --- |
| 주체 | David M. Hoffman, Ahna R. Girshick, Kurt Akeley, Martin S. Banks (UC Berkeley / Microsoft Research) · 편안한 범위 수치는 Takashi Shibata 등 |
| 연도 | Hoffman 등 2008 (Journal of Vision) / Shibata 등 2011 (Journal of Vision, "The zone of comfort: Predicting visual discomfort with stereo displays") |
| 수치 | 대부분의 사람이 견디는 불일치 한계 약 0.4디옵터 / 증상: 눈 피로, 두통, 방향감각 상실, 근거리 물체 응시 곤란 |
| 출처 | Hoffman DM, Girshick AR, Akeley K, Banks MS (2008), "Vergence–accommodation conflicts hinder visual performance and cause visual fatigue," Journal of Vision 8(3):33 / 요약 및 0.4D 수치: https://en.wikipedia.org/wiki/Vergence-accommodation_conflict |

사람의 두 눈은 물체를 볼 때 두 가지를 동시에 한다. 눈알을 안쪽으로 모아 시선을 맞추는 수렴(vergence), 그리고 수정체 두께를 바꿔 초점을 맞추는 조절(accommodation)이다. 자연 상태에서 이 둘은 평생 같은 거리에 묶여 있다 — 가까운 것을 보면 눈이 모이면서 동시에 수정체가 두꺼워진다. 그런데 스테레오 HMD에서는 화면이 고정된 물리적 거리(보통 1.3~2m에 상당하는 광학 거리)에 있으므로 조절은 언제나 그 거리에 고정되고, 수렴만 가상 물체의 깊이를 따라 움직인다. 신경계가 평생 학습한 연결이 끊어지는 것이다. Hoffman 등은 조절 거리를 자유롭게 바꿀 수 있는 4면 광학 벤치를 만들어, 불일치가 없을 때 대비 입체시 정확도가 떨어지고 융합 시간이 길어지며 피로·두통이 늘어남을 실험으로 보였다. Shibata 등은 이를 이어받아 '편안한 구역(zone of comfort)'을 정량화했고, 대체로 0.4디옵터 이내의 불일치는 대부분의 사람이 무리 없이 견딘다는 기준이 널리 쓰인다.

VR 멀미와 눈 피로가 '적응하면 되는 것'이 아니라 광학 구조에서 필연적으로 나오는 문제임을 입증했다. 이 논문 이후 varifocal·multifocal·light field·holographic이라는 네 갈래의 디스플레이 연구가 모두 '이 하나의 불일치를 어떻게 없앨 것인가'라는 질문 아래 정렬된다.

논문 원문(Journal of Vision 8(3):33, 2008)의 초록 전문은 이번 조사에서 확보하지 못했다 — JOV와 PubMed 모두 봇 차단으로 접근이 막혔다. 위 내용은 제목과 2차 출처 요약에 기반한다. 또 0.4디옵터라는 편안 한계는 개인차·연령차(노안이 오면 조절 자체가 줄어 문제가 달라진다)가 크다.

### Varifocal 디스플레이 — Meta Half Dome 시제품 계열
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta(Facebook) Reality Labs Research, Douglas Lanman 주도 |
| 연도 | Half Dome 1 공개 2018년 (F8) / Half Dome 2·3 공개 2019년 (Oculus Connect 6) / 상용 제품 없음 |
| 수치 | Half Dome 3: 액정 렌즈 적층으로 64개 이산 초점면 / Half Dome 1: 기계식 패널 이동 방식 / 상용 출시 제품 0개 |
| 출처 | https://en.wikipedia.org/wiki/Vergence-accommodation_conflict (Half Dome 관련 서술) — 1차 출처 미확보 |

수렴-조절 불일치를 푸는 가장 직접적인 방법은 화면의 광학적 거리를 실시간으로 옮기는 것이다. 시선 추적으로 사용자가 지금 어느 깊이를 보고 있는지 알아낸 뒤, 그 깊이에 맞춰 초점면을 이동시킨다. Half Dome 1세대는 디스플레이 패널 자체를 기계적으로 앞뒤로 움직이는 방식이었다 — 작동은 하지만 모터와 가동부 때문에 무겁고 소음이 있으며 수명이 문제였다. 3세대에서는 가동부를 없애고 액정 렌즈를 여러 장 쌓은 전자식 구조로 바꿨다. 각 액정 층이 켜짐/꺼짐 두 상태를 가지므로 층을 조합하면 이산적인 초점 상태를 여러 개 만들 수 있고, Half Dome 3는 이 방식으로 64개의 이산 초점면을 구현한 것으로 알려져 있다. 렌더링 쪽에서는 시선 깊이 추정 → 초점면 전환 → 그에 맞춘 피사계 심도(defocus blur) 렌더링이 한 프레임 안에 맞물려야 하므로, 포비티드 렌더링과 마찬가지로 시선 추적 지연이 곧 품질이 된다.

수렴-조절 불일치를 '없애는' 최초의 착용 가능한 형태. 기계식에서 액정 적층 전자식으로 넘어간 것이 결정적인데, 가동부가 사라지면서 소비자 기기에 들어갈 수 있는 두께·무게·신뢰성의 경로가 처음 보였다.

Half Dome 각 세대의 시야각·디옵터 범위·전환 지연·무게 같은 핵심 수치를 이번 조사에서 1차 출처로 확인하지 못했다(Meta의 원문 블로그 URL들이 모두 404였다). 64개 초점면이라는 숫자도 2차 출처 기반이다. 더 근본적으로는, 이산 초점면은 어디까지나 근사이고 완전한 연속 조절은 제공하지 못한다. 그리고 8년째 시제품 단계에 머물러 있다는 사실 자체가 이 접근의 난이도를 말해 준다.

### Near-Eye Light Field Displays — 마이크로렌즈 배열로 광선장을 재현하다
| 항목 | 내용 |
| --- | --- |
| 주체 | Douglas Lanman, David Luebke (NVIDIA Research) |
| 연도 | 2013 (ACM Transactions on Graphics 32(6), 2013년 11월, SIGGRAPH Asia) |
| 수치 | 논문은 해상도·시야각·피사계 심도의 정량적 교환 관계를 정식화했으나, 시제품의 마이크로렌즈 피치·유효 해상도·시야각·디옵터 범위의 구체 수치는 이번에 확보한 초록 범위에서는 제시되지 않았다 |
| 출처 | https://research.nvidia.com/publication/near-eye-light-field-displays (ACM Trans. Graph. 32(6), 2013) |

varifocal이 '초점면 하나를 옮기는' 접근이라면, 광선장(light field) 디스플레이는 '눈에 들어오는 광선 자체를 재현하는' 접근이다. 디스플레이 패널 앞에 마이크로렌즈 배열을 놓아, 각 렌즈가 패널의 작은 화소 묶음을 서로 다른 방향의 광선으로 쏘아 보낸다. 눈의 동공에 여러 방향의 광선이 동시에 들어오면, 수정체는 어느 거리에 초점을 맞추느냐에 따라 실제 물체를 볼 때와 똑같이 선명해지거나 흐려진다. 즉 수렴·조절·양안 시차·망막 흐림(retinal defocus)이라는 네 가지 깊이 단서가 모두 동시에, 자연스럽게 제공된다. 저자들은 이 구조에서 해상도·시야각·피사계 심도 사이에 근본적인 교환 관계가 있음을 정식화했다. 방향 정보를 얻으려면 화소를 각도에 나눠 써야 하므로, 광선장이 풍부해질수록 공간 해상도는 떨어진다.

수렴-조절 불일치를 시선 추적이나 가동부 없이 광학만으로 해결할 수 있음을 보인 최초의 착용형 시제품. 또한 마이크로렌즈 배열 덕분에 두께가 극적으로 얇아져, '안경형 VR'이라는 형태 인자의 가능성을 처음 제시했다.

공간 해상도의 희생이 치명적이다. 각 마이크로렌즈가 방향 정보를 담는 대가로 유효 해상도가 크게 떨어져, 2013년 시제품의 화질은 당시 일반 HMD보다도 낮았다. 이 교환 관계가 광선장 디스플레이가 아직 상용화되지 못한 핵심 이유다. 구체 수치는 논문 본문 확인 필요.

### 메타표면 도파관 기반 풀컬러 3D 홀로그래픽 AR 디스플레이
| 항목 | 내용 |
| --- | --- |
| 주체 | Manu Gopakumar, Gun-Yeal Lee, Suyeon Choi, Brian Chao, Yifan Peng, Jonghyun Kim, Gordon Wetzstein (Stanford Computational Imaging Lab, NVIDIA 공동) |
| 연도 | 2024 (Nature) |
| 수치 | 메타표면 격자 주기 384nm, 높이 220nm / 동작 파장: 적 638nm, 녹 521nm, 청 445nm / 알고리즘: 해석적 물리 모델 + CNN 결합한 학습된 도파관 모델 |
| 출처 | Gopakumar M, Lee G-Y, Choi S, Chao B, Peng Y, Kim J, Wetzstein G (2024), "Full-colour 3D holographic augmented-reality displays with metasurface waveguides," Nature. https://www.computationalimaging.org/publications/holographicar/ |

홀로그래픽 디스플레이는 빛의 진폭뿐 아니라 위상까지 제어해 파면 자체를 재구성하므로, 원리적으로 깊이 단서를 완전하게 제공하고 수렴-조절 불일치가 생기지 않는다. 문제는 광엔진이 부피가 크다는 것이었다. 이 연구는 세 가지를 결합해 이를 안경 형태로 줄였다. 첫째, 역설계(inverse design)로 만든 풀컬러 메타표면 격자 — 주기 384nm, 높이 220nm의 나노 구조물로 적(638nm)·녹(521nm)·청(445nm) 세 파장을 모두 다룬다. 둘째, 파장별 분산을 상쇄하는 소형 도파관 구조. 셋째, AI 기반 홀로그래피 알고리즘 — 해석적 물리 모델과 합성곱 신경망(CNN)을 결합해 실제 도파관의 비이상적 거동까지 학습한 '학습된 물리 도파관 모델'로 위상 패턴을 계산한다. 즉 광학의 불완전함을 소프트웨어가 보정하는 구조다.

홀로그래픽 AR이 광학 벤치 위의 실험에서 안경형 시제품으로 내려온 첫 사례. 특히 '광학을 완벽하게 만들 수 없다면 그 오차를 신경망으로 학습해 보정한다'는 접근은 이후 근안 디스플레이 설계의 표준 문법이 될 가능성이 크다.

시야각·아이박스 크기·도파관 두께·시제품 전체 크기 같은 형태 인자 수치를 이번 조사에서 확인하지 못했다(Nature 본문이 인증 차단). 홀로그래픽 디스플레이는 일반적으로 스페클 잡음과 좁은 아이박스가 고질적 문제이며, 실시간 위상 계산의 연산 부담도 크다. 연구 시제품이며 상용화 일정은 없다.

### Microsoft HoloLens 2 — 투시형 도파관과 레이저 광엔진
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft |
| 연도 | 발표 2019년 2월 24일(MWC) / 출시 2019년 11월 7일 / 가격 3,500달러 |
| 수치 | 홀로그래픽 해상도 '2k 3:2 광엔진' / 홀로그래픽 밀도 2.5k radiants 초과 / 대각 시야각 52°(1세대 34°) / 깊이 센서 1MP ToF / 시선 추적 적외선 카메라 2대 / 헤드 트래킹 가시광 카메라 4대(스테레오 베이스라인 98.6mm, 대각 FOV 96.1°, 초점거리 1.08mm) / 무게 566g / 가격 3,500달러 |
| 출처 | https://learn.microsoft.com/en-us/hololens/hololens2-hardware (공식 사양) · https://en.wikipedia.org/wiki/HoloLens_2 (시야각·가격·Guttag 반박) |

Vision Pro·Quest가 카메라로 바깥을 찍어 화면에 다시 그리는 '비디오 패스스루' 방식이라면, HoloLens 2는 사용자가 유리를 통해 실제 세계를 직접 보고 그 위에 빛을 얹는 '광학 투시(optical see-through)' 방식이다. 광엔진의 빛이 도파관(waveguide) 렌즈 안으로 들어가 전반사로 눈앞까지 전달된 뒤 회절 격자로 눈을 향해 빠져나온다. Microsoft는 이를 '2k 3:2 광엔진', '2.5k radiants 이상의 홀로그래픽 밀도(라디안당 광점 수)'로 표기한다. 대각 시야각은 52°로 1세대의 34°에서 두 배 이상(면적 기준) 넓어졌고, 확장은 주로 세로 방향이었다(16:9를 벗어나 3:2가 된 이유). 센싱은 헤드 트래킹용 가시광 카메라 4대, 시선 추적용 적외선 카메라 2대, 그리고 1메가픽셀 ToF(Time-of-Flight) 깊이 센서로 이뤄진다. 이 깊이 센서가 실시간 환경 메시(spatial mapping)를 만들어 가림 처리와 배치의 근거가 된다. 무게 566g, Snapdragon 850 + 2세대 전용 홀로그래픽 처리 장치(HPU), 배터리 2~3시간.

'눈 위치에 맞춘 디스플레이 최적화(eye-based rendering)'를 명시적 사양으로 내건 첫 상용 AR 기기. 시선 추적이 인터랙션뿐 아니라 광학 보정에까지 쓰였다. 또 ToF 깊이 센서를 표준 장비로 넣어 환경 메시 기반 가림 처리를 기본 기능으로 제공한 것이 이후 모든 MR 기기의 기준이 됐다.

실효 해상도에 대한 논란이 있다. Microsoft는 도당 47화소(47 PPD)를 주장했으나, 디스플레이 분석가 Karl Guttag는 레이저 빔 스캐닝 방식의 특성상 실측 해상도가 도당 20화소 미만이라고 반박했다 — 스캐닝 방식은 '화소'가 고정 격자가 아니라 빔이 그리는 궤적이므로 정격 수치와 실효 선명도가 크게 다를 수 있다. 또 52° 시야각은 여전히 좁아 가상 물체가 시야 가장자리에서 잘려 나가고, 광학 투시 방식의 구조적 한계로 검은색을 표현할 수 없다(빛을 더할 수만 있고 뺄 수 없다 — 가상 물체가 언제나 반투명하게 보이는 이유). Microsoft는 2024년 HoloLens 2 생산 종료를 발표했다.

### 패스스루 영상의 지연·왜곡과 재투영(reprojection) 보정
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta(Quest 3, Asynchronous TimeWarp·SpaceWarp·Application SpaceWarp) · Apple(Vision Pro R1) · Varjo(XR-4) · Valve |
| 연도 | ATW 2015년 3월 / ASW 2016년 11월 / ASW 2.0 2019년 8월 / Application SpaceWarp 2021년 11월(V34) / Quest 3 2023년 10월 / Vision Pro 2024년 2월 / Varjo XR-4 2023년 말 |
| 수치 | Vision Pro 광자-대-광자 지연 12ms / Quest 3: 눈당 2064×2208 LCD, 90~120Hz, 팬케이크 렌즈, 컬러 패스스루 카메라 4MP 2대, 적외선 패턴 투사기 기반 깊이 센싱, Snapdragon XR2 Gen 2 / Varjo XR-4: 눈당 3840×3744, 도당 51화소, 시야 120°×105°, 패스스루 카메라 2,000만 화소 2대, 300 KPIX LiDAR(7m), 시선 추적 200Hz / AppSW: 최대 70% 추가 연산 여유, 렌더링 36/45/60fps → 표시 72/90/120Hz, 모션 벡터·깊이 버퍼는 컬러보다 낮은 해상도로 가능 |
| 출처 | https://www.apple.com/apple-vision-pro/specs/ · https://developers.meta.com/horizon/blog/introducing-application-spacewarp/ · https://en.wikipedia.org/wiki/Meta_Quest_3 · https://varjo.com/products/xr-4/ · https://en.wikipedia.org/wiki/Asynchronous_reprojection |

비디오 패스스루에는 두 가지 구조적 문제가 있다. 첫째는 지연이다. 빛이 카메라에 들어와 처리를 거쳐 디스플레이에서 다시 나오기까지의 시간이 길면, 고개를 돌렸을 때 세상이 뒤늦게 따라와 멀미가 난다. Apple은 R1 전용 칩으로 이를 12ms로 잡았다. 둘째는 왜곡이다. 카메라는 눈이 있는 자리에 있지 않다 — 이마 바깥쪽에 몇 센티미터 떨어져 있다. 그래서 카메라가 찍은 영상을 그대로 보여주면 시차(parallax)가 틀어져 손이 부자연스럽게 커 보이거나 가까운 물체의 거리감이 어긋난다. 이를 보정하려면 장면의 깊이를 추정해 카메라 시점의 영상을 눈 시점으로 재투영해야 하고, 깊이 추정이 틀린 경계에서 물결치는 왜곡이 남는다. 렌더링 쪽에서는 같은 재투영 기술이 프레임레이트 방어에도 쓰인다. 비동기 타임워프(ATW)는 머리 회전 정보만으로 이미 그린 프레임을 마지막 순간에 비틀어 표시 시점의 자세에 맞춘다. 비동기 스페이스워프(ASW)는 여기에 깊이 정보를 더해 새 프레임을 외삽한다. Application SpaceWarp(AppSW)는 한 발 더 나가, 앱이 아예 표시 주사율의 절반으로만 그리고(72Hz 표시에 36fps 렌더링) 나머지 프레임을 모션 벡터 버퍼와 깊이 버퍼로 합성한다. Meta는 초기 테스트에서 최대 70%의 추가 연산 여유를 얻었다고 보고했다.

'못 그린 프레임을 사후에 만들어낸다'는 발상이 모바일 SoC에서 고주사율 MR을 가능하게 만들었다. 렌더링 예산이 절반이 되면 조경 시각화처럼 폴리곤과 식생 인스턴스가 많은 장면에서 결정적이다. 동시에 패스스루의 12ms 지연은 '화면을 보는 경험'과 '창밖을 보는 경험'을 가르는 임계점을 넘어섰다.

Quest 3·Vision Pro 모두 패스스루 영상의 실효 해상도(도당 화소)를 공식 공개하지 않는다. Vision Pro의 12ms도 Apple 자체 측정치이며 독립 검증이 없다. 재투영은 근본적으로 외삽이라 빠르게 움직이는 물체의 경계나 반투명·반사 표면에서 유령상(ghosting)과 찢어짐이 남는다. 패스스루 카메라의 시차 왜곡은 손이 얼굴에 가까울 때 여전히 뚜렷하며, 이것이 Meta가 Flamera 같은 광선장 패스스루 카메라를 연구하는 이유다.

### 가림(occlusion) 처리와 깊이 센싱 — 실제 물체가 가상 물체를 가리게 하기
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta(Depth API) · Microsoft(HoloLens 2 ToF) · Apple(ARKit / LiDAR) · 이론적 기반은 Ronald Azuma 1997 서베이 |
| 연도 | Azuma 서베이 1997 / HoloLens 2 ToF 2019 / ARKit People Occlusion 2019 / Meta Depth API 2023(Quest 3와 함께) |
| 수치 | HoloLens 2 깊이 센서: 1MP Time-of-Flight / Meta Depth API: Quest 3·3S 전용, 최소 유효 거리 약 0.2m(20cm), 그보다 가까우면 깊이 추정이 불안정 / Varjo XR-4: 300 KPIX LiDAR, 유효 거리 7m / Apple: LiDAR 스캐너 + TrueDepth 카메라 |
| 출처 | https://learn.microsoft.com/en-us/hololens/hololens2-hardware · https://developers.meta.com/horizon/documentation/unity/unity-depthapi/ · Azuma R (1997), "A Survey of Augmented Reality," Presence: Teleoperators and Virtual Environments 6(4):355-385 |

AR이 '겹쳐 보이는 화면'이 아니라 '거기 있는 물건'이 되려면, 실제 세계가 가상 물체를 가려야 한다. 가상 나무가 실제 건물 앞에 떠 있으면 그 순간 거짓말이 들통난다. 문제는 렌더러가 실제 세계의 깊이를 모른다는 것이다. 해법은 세 갈래다. 첫째, 정적 환경 메시 — HoloLens 2의 1메가픽셀 ToF 깊이 센서가 공간을 스캔해 실시간 환경 메시를 만들고, 렌더러가 이 메시를 깊이 버퍼에만 쓰고 색은 그리지 않는 '가림 전용 지오메트리'로 처리한다. 벽·바닥·가구처럼 움직이지 않는 것은 이걸로 충분하다. 둘째, 실시간 깊이 맵 — Meta Quest 3/3S의 Depth API가 매 프레임 깊이 맵을 앱에 넘겨, 지나가는 사람·손·반려동물처럼 움직이는 것까지 가릴 수 있게 한다(동적 가림). 셋째, 의미 분할 — Apple ARKit의 People Occlusion은 사람을 따로 분할해 사람 뒤로 가상 물체를 보낸다. 조경 시각화 관점에서 이것은 실무의 핵심이다. 현장에 서서 심을 나무를 미리 보려면, 그 나무가 기존 수목과 건물에 제대로 가려져야 크기와 위치를 판단할 수 있다.

Azuma가 1997년 서베이에서 AR의 3대 요건으로 못 박은 '정확한 3D 정합(accurate 3D registration)'이 실제로 구현되기 시작한 지점. 가림은 정합이 시각적으로 검증되는 가장 엄격한 시험대다 — 몇 센티미터만 어긋나도 경계에서 바로 보인다.

Meta는 깊이 맵의 해상도·갱신 주기·정확도를 공개하지 않는다(문서에 명시되어 있지 않음). 근거리 0.2m 미만에서는 손 가림의 정확도가 떨어져 손가락 윤곽이 뭉개진다. 또 Depth API는 가림과 레이캐스팅에는 쓸 수 있지만 물리 충돌에는 쓸 수 없다. 더 근본적으로, 실외 조경 현장은 실내보다 훨씬 불리하다 — ToF와 구조광 방식 모두 직사광선에 취약하고, 나뭇잎처럼 미세하고 반투명한 경계는 깊이 센서가 가장 못 다루는 형태다. 야외 원거리 가림은 여전히 미해결이며 GNSS·SLAM·의미 분할을 결합한 접근이 연구 단계에 있다.

#### 검증에서 잡힌 정정
- [치명적] '최대 원뿔세포 밀도 약 147,000개/mm² — 출처 Curcio 등 1990'은 오귀속. Curcio CA, Sloan KR, Kalina RE, Hendrickson AE (1990) 초록 원문은 'Peak foveal cone density averages 199,000 cones/mm² and is highly variable between individuals (100,000-324,000 cones/mm²)'. 정확한 값은 평균 최대 199,000개/mm²이며, 147,000은 Wikipedia 'Fovea centralis'가 Shroff(2011) 'An Eye on Numbers: A Ready Reckoner in Ophthalmology'를 인용한 수치다. 약 26% 과소 + 출처 뒤바뀜. (확인: OpenAlex 10.1002/cne.902920402 초록, Wikipedia 특수:Export 원문 인용 템플릿)
- '개인 범위 <100,000 ~ >324,000'의 부등호는 Curcio 원문에 없음. 원문은 8개 망막 실측 범위 '(100,000-324,000 cones/mm²)'이며, '미만/초과도 드물지 않다'는 Wikipedia 편집자의 확대 서술이다. 1차 출처 인용처럼 적으면 안 됨.
- '중심소와 0.35mm ≈ 1°'는 1차 출처와 불일치. Curcio 1990 초록 원문: 'In the fovea, the diameter of the rod-free zone is 0.350 mm (1.25 degrees).' 정확한 값은 1.25°(주장값 대비 25% 과소).
- 중심와 축의 mm→각도 환산 3건이 서로 모순: 1.5mm→5°(3.33°/mm), 0.35mm→1°(2.86°/mm), 0.5mm→1.5°(3.00°/mm). 표준 망막 환산(Drasdo & Fowler, 약 3.5°/mm)을 쓰면 각각 약 5.2°, 1.2°, 1.75°가 되어야 한다. 특히 무혈관대 0.5mm는 1.5°가 아니라 약 1.75°.
- '중심소와 50개/100μm vs 주변부 12개/100μm'는 같은 항목의 147,000개/mm²와 자기모순. 50개/100μm는 선밀도 500개/mm → 면밀도 약 250,000개/mm²를 뜻하는데, 같은 Wikipedia 문서가 147,000개/mm²에 대응하는 선밀도를 '383 cones per millimeter'로 병기하고 있다. 두 숫자를 동시에 인용하면 25만 vs 14.7만이 충돌한다.
- '시신경 섬유의 약 50%가 중심와 담당'은 Curcio 1990에 없는 내용. 해당 논문은 광수용체 밀도 지도만 다루며 시신경 섬유 배분을 다루지 않는다. Wikipedia 수준의 2차 서술이므로 1차 출처로 표기하면 안 됨.
- Apple Vision Pro '주사율 90·96·100·120Hz'는 세대 혼동. 항목이 명시한 2024년 2월 2일 출시 M2 모델의 공식 지원 주사율은 90Hz/96Hz/100Hz이며(최대 100Hz), 120Hz는 2025년 10월 15일 발표·10월 22일 출시된 M5 탑재 개정판부터다. 현재 apple.com 사양 페이지의 '90Hz, 96Hz, 100Hz, 120Hz'는 M5 모델 기준값.
- Apple Vision Pro '메모리 대역폭 256GB/s'는 주체 오귀속. Apple 공식 사양 페이지에서 256GB/s는 R1 보조 칩의 메모리 대역폭이고, 메인 칩 대역폭은 M5 모델 153GB/s(16GB 통합 메모리), 2024년 M2 모델은 100GB/s다. 기기 전체 대역폭처럼 적으면 오해를 부른다.
- HoloLens 2 '대각 시야각 52°'와 '가격 3,500달러'를 learn.microsoft.com/hololens/hololens2-hardware(공식 사양)로 표기한 것은 잘못. 해당 공식 페이지 전문에는 시야각 수치도 가격도 없다(디스플레이 항목은 '2k 3:2 light engines', '>2.5k radiants'뿐). 52°/34°/$3,500은 Wikipedia 등 3자 출처에서만 확인된다.
- HoloLens 2 '헤드 트래킹 가시광 카메라 4대(스테레오 베이스라인 98.6mm, 대각 FOV 96.1°, 초점거리 1.08mm)'는 적용 범위 오류. Microsoft 공식 표는 이 값들을 VLC 일반 설계값으로 주되, 98.6mm 베이스라인과 coplanar 조건은 명시적으로 '전방을 향한 VLC(for forward-facing VLCs)' 한정이다. 4대 전체의 베이스라인이 아님.
- Quest 3 '90~120Hz'는 불완전. Quest 3의 실제 선택 가능 주사율은 72/80/90/120Hz이며, 72Hz·80Hz가 누락됐다(Wikipedia 사양표는 '90–120 Hz'로만 적어 3자 요약을 그대로 옮긴 결과).
- 수렴-조절 불일치 '약 0.4디옵터'를 Hoffman 등 2008과 묶어 제시한 것은 부정확. 0.4D는 Shibata 등 2011 'The zone of comfort' (Journal of Vision 11(8):11)에서 유도된 수치이고, Hoffman 2008(J Vis 8(3):33)은 이 단일 상수를 제시하지 않는다. 또한 Shibata의 편안한 영역은 고정 상수가 아니라 시청 거리 의존적이고 교차/비교차 시차에 대해 비대칭이므로 '한계 0.4D'라는 단일값 서술은 과단순화.
- [확인 못 함] Lanman & Luebke 2013 시제품의 마이크로렌즈 피치·유효 해상도·시야각·디옵터 범위 — 서지사항(ACM TOG 32(6):1-10, 2013년 11월, 저자 Lanman·Luebke, DOI 10.1145/2508363.2508366)은 Crossref로 확인했으나, 본문 PDF가 10MB 초과로 수신 실패해 시제품 수치는 이번에도 검증하지 못했다. '초록에 없다'는 서술 자체는 사실이나, 해당 수치는 논문 본문에 존재할 가능성이 높으므로 '미확보'로 남겨야지 '제시되지 않았다'로 단정하면 안 된다.
- [확인 못 함] Half Dome 1의 F8 2018 공개 시점, Half Dome 2·3의 OC6 2019 공개 시점 — Wikipedia 'Vergence-accommodation conflict'는 1번 시제품의 기계식 액추에이터와 3번 시제품의 LC 6층·64 이산 초점면, 상용 제품 부재만 확인해 줄 뿐 공개 연도·행사명은 담고 있지 않다. Meta 1차 출처 미확보 상태 그대로.
- [확인 못 함] Varjo XR-4 '2023년 말' 출시 시점 — varjo.com/products/xr-4/ 사양 페이지에서 해상도·PPD·FOV·LiDAR·200Hz 시선추적은 모두 확인했으나 출시 시점 및 XR-4 / Focal Edition / Secure Edition 간 사양 차이(특히 51 PPD가 기본형 전체에 적용되는지 포커스 영역 한정인지)는 해당 페이지에 명시되어 있지 않다.
- [참고] Curcio 1990 인용 시 쓸 수 있는 추가 정본 수치: 평균 망막당 원뿔 460만 개(408만~529만), 간상체 약 9,200만 개(7,790만~1억 730만). 조사 결과에는 이 1차 수치가 전혀 들어 있지 않고 2차 요약 수치만 들어 있다.
- [수치 오류] '최대 원뿔세포 밀도 약 147,000개/mm²' → 틀림. Curcio CA, Sloan KR, Kalina RE, Hendrickson AE (1990) J Comp Neurol 292(4):497-523 원문은 'Peak foveal cone density averaged 199,000 cones/mm²'. 147,000은 Wikipedia 'Fovea centralis'의 일반 밀도 서술이지 Curcio의 peak 값이 아니며, 같은 문장에 붙인 개인 범위 100,000~324,000은 199,000에 딸린 값이라 내부 모순이다. (Crossref 10.1002/cne.902920402 초록으로 확인)
- [선후관계] '이 원리를 그래픽스에 끌어온 것은 1990년대 이후' → 틀림. Levoy M, Whitaker R, 'Gaze-directed volume rendering', Proceedings of the 1990 Symposium on Interactive 3D Graphics / ACM SIGGRAPH Computer Graphics 24(2):217-223 (1990) — Curcio 논문과 같은 해다. Wikipedia 'Foveated rendering'도 'Research into foveated rendering dates back at least to 1991'로 적는다. 또한 이심률에 따른 시력 저하 자체는 Østerberg(1935) 이래 알려진 사실이므로 Curcio 1990이 그래픽스 적용의 출발 근거가 될 수 없다.
- [선후관계] Guenter 등 2012를 '포비티드 렌더링의 원형 논문'으로 규정 → 틀림. 선행 연구로 Levoy & Whitaker 1990(위), Luebke D, Hallen B, 'Perceptually Driven Simplification for Interactive Rendering', Eurographics Rendering Techniques 2001, pp.223-234가 존재한다(Crossref 확인). 2012 논문의 기여는 '원형'이 아니라 '3레이어 실시간 GPU 구현 + 정신물리 사용자 실험을 결합한 첫 사례'로 한정해야 한다. 수치(5~6배, 10~15배, 1.32~1.65 arcmin/deg, 3레이어, 70° 100배 예측)는 Microsoft Research 공식 페이지와 일치하여 반박 없음.
- [세대 혼동] Apple Vision Pro '주사율 90·96·100·120Hz'를 '발표 2023-06-05 / 출시 2024-02-02' 기기의 사양으로 제시 → 틀림. M2 탑재 초기 모델은 최대 100Hz(90/96/100Hz)이며, 120Hz는 2025-10-15 발표된 M5 모델부터다(Wikipedia: M2 'up to 100 Hz', M5 'up to 120 Hz refresh rate'). 두 세대 사양을 한 항목에 섞었다.
- [출처 시점 오류] 인용한 https://www.apple.com/apple-vision-pro/specs/ 는 2026년 현재 M5 모델 사양 페이지다(M5 10코어 CPU/10코어 GPU, 153GB/s). 2023/2024 출시 기기의 근거로 이 URL을 그대로 인용하면 시점이 어긋난다.
- [귀속 오류] '메모리 대역폭 256GB/s'를 기기/SoC 사양처럼 제시 → 부정확. Apple 사양서는 R1 칩에 '256GB/s memory bandwidth', M5 칩에 '153GB/s memory bandwidth'를 각각 표기한다. 256GB/s는 R1 코프로세서 값이다. (12ms photon-to-photon, 2,300만 화소, 7.5μm, DCI-P3 92%, 세계향 추적 카메라 6대·시선 추적 4대·LiDAR·IMU 4개는 공식값과 일치)
- [선후관계] VRS/포비테이션 연표를 '2018~2022'로 잡은 것 → 선행 누락. NVIDIA VRWorks 공식 페이지 자체가 Turing VRS의 선행으로 Maxwell의 Multi-Res Shading(MRS), Pascal의 Lens Matched Shading(LMS)을 명시한다(2015~2016). 고정 포비티드 렌더링(FFR)도 Quest Pro(2022)가 아니라 Oculus Go/Quest 세대(2018~2019)에 이미 상용화되었다 — 다만 FFR 상용화 시점의 1차 출처는 이번 세션에서 확인하지 못했다.
- [문서 내부 불일치] 'D3D12 Tier 2 타일 크기 8·16·32 텍셀' → Microsoft 문서 자체가 모순된다. 같은 페이지의 Tier 2 요약은 'Screen-space image tile size is 16x16 or smaller'인데, 타일 크기 절에서는 '8, 16, 32' 중 하나라고 적는다. 인용 시 단서를 달아야 한다. (셰이딩률 1x1·1x2·2x1·2x2 필수, 2x4·4x2·4x4 선택, DXGI_FORMAT_R8_UINT, NVIDIA Turing 16×16 타일·7가지 rate·샘플당 1회~16샘플당 1회는 모두 공식 문서와 일치)
- [선후관계] 가림 처리의 '이론적 기반 = Azuma 1997 서베이' → 틀림. AR 가림 처리의 1차 문헌은 Wloka MM, Anderson BG, 'Resolving occlusion in augmented reality', Proceedings of the 1995 Symposium on Interactive 3D Graphics (SI3D '95), pp.5-12, DOI 10.1145/199404.199405 (1995). Azuma 1997은 이를 인용·정리한 서베이다(Crossref 확인).
- [선후관계] 깊이 센싱 기점을 'HoloLens 2 ToF 2019'로 잡음 → 선행 누락. HoloLens 1(2016년 출시)이 이미 ToF 깊이 센서를 탑재했고, 그 계보는 Kinect(2010)까지 올라간다. HoloLens 2의 1MP ToF는 2세대 개선이지 최초가 아니다.
- [연도 오류] 'Apple(ARKit / LiDAR)'를 2019로 묶음 → LiDAR 스캐너는 2020년 3월 iPad Pro(이후 2020년 10월 iPhone 12 Pro)부터다. 2019년에 해당하는 것은 ARKit 3의 People Occlusion뿐이다.
- [선후관계] 수렴-조절 불일치의 근거를 Hoffman 등 2008에서 시작 → 선행 누락. Wann JP, Rushton S, Mon-Williams M, 'Natural problems for stereoscopic depth perception in virtual environments', Vision Research 35:2731-2736 (1995)가 HMD에서의 조절-수렴 충돌을 이미 보고했다(Crossref 확인). 0.4디옵터 수치가 Shibata 등 2011 출처라는 서술 자체는 Wikipedia 기술과 일치해 맞다.
- [선후관계] Varifocal을 'Meta Half Dome 시제품 계열'로 대표시킴 → 선행 누락. Akeley K, Watt SJ, Girshick AR, Banks MS, 'A stereo display prototype with multiple focal distances', ACM TOG 23(3):804-813, SIGGRAPH 2004가 다초점면 디스플레이의 선행이다(Crossref 확인). Half Dome 3의 'LC 6층 → 64 이산 초점면', Half Dome 1의 기계식, '상용 제품 0개'는 Wikipedia 기술과 일치하나, Half Dome 1의 F8 2018 / Half Dome 2·3의 OC6 2019 공개 연도는 인용된 문서에 연도 기재가 없어 이번 조회로 확인하지 못했다.
- [출처 귀속] 중심와 치수 계열 수치(1.5mm≈5°, 중심소와 0.35mm≈1°, 무혈관대 0.5mm≈1.5°, 중심소와 50개/100μm vs 주변부 12개/100μm, 시신경 섬유 약 50%)를 'Curcio 해부학 정본'으로 귀속 → 부정확. 이들은 Wikipedia 'Fovea centralis' 서술이며, Curcio 1990 초록에 나오는 대응 수치는 rod-free zone 0.350mm 하나뿐이다. 수치 자체는 Wikipedia와 일치하므로 출처 표기만 고치면 된다.
- (외 14건)

## devices
항목 12개 · 검증 정정 지적 45건


### Google Glass Explorer Edition (구글 글래스)
| 항목 | 내용 |
| --- | --- |
| 주체 | Google X (현 X Development), 프로젝트 리더 Babak Parviz·Thad Starner |
| 연도 | 발표 2012년 4월(Project Glass) / Explorer Edition 배포 2013년 4월 16일 / 일반 판매 2014년 4월 15일 / 소비자판 중단 2015년 1월 |
| 수치 | 디스플레이 640×360 px(2.4m 거리 25인치 화면 상당) · 카메라 5MP 사진/720p 영상 · TI OMAP4430 듀얼코어 1.2GHz(ARMv7) · RAM 1GB(v1)→2GB(v2) · 저장 16GB(가용 12GB) · 무게 36g · 배터리 570mAh · 가격 $1,500 (영국 £1,000) |
| 출처 | https://en.wikipedia.org/wiki/Google_Glass (제원 표), Google Project Glass 발표(2012-04) |

LCoS(Liquid Crystal on Silicon) 마이크로 디스플레이에 필드 시퀀셜 컬러 LED를 쏘아 만든 상을, 관자놀이 옆 프리즘(빔 스플리터)으로 꺾어 오른쪽 눈 위쪽에 띄우는 단안(monocular) 헤드업 디스플레이다. 640×360 픽셀의 상이 눈앞이 아니라 시야 우상단에 '떠 있는 작은 화면'으로 보이며, 구글은 이를 '2.4m 거리의 25인치 화면'에 해당한다고 설명했다. 중요한 점은 이 장치가 공간을 인식하지 않는다는 것이다. 깊이 센서도, SLAM도, 6자유도 추적도 없기 때문에 화면은 머리를 돌려도 늘 같은 자리에 붙어 다닌다. 따라서 엄밀히 말해 Azuma(1997) 기준의 3차원 정합(registration) AR이 아니라 '착용형 알림 화면'에 가깝다.

기술적 도약이라기보다 '사회적 실험'으로서의 도약이었다. 36g이라는 안경 수준 무게와 하루 착용을 전제한 최초의 대량생산 착용형 디스플레이였고, 바로 그 때문에 프라이버시 반발('Glasshole')과 사회적 수용성이라는, 이후 모든 AR 기기가 반드시 풀어야 할 문제를 처음으로 드러냈다. 메타가 2024년 Orion 발표문에서 '다른 사람의 눈과 표정이 보여야 한다'를 설계 원칙으로 못 박은 것은 이 실패의 직접적 상속이다.

단안·고정 위치 화면이라 공간 정합이 불가능하다. 배터리 570mAh로 영상 촬영 시 1시간을 넘기기 어려웠고, 카메라가 늘 켜져 있다는 인상이 주는 프라이버시 거부감 때문에 공공장소 착용 금지 사례가 잇따랐다. 2015년 소비자판이 중단되고 Glass Enterprise Edition(2017·2019)으로 산업용으로만 살아남았다.

### Microsoft HoloLens (1st gen)
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft, 수석 발명가 Alex Kipman |
| 연도 | 발표 2015년 1월 21일 / Development Edition 출하 2016년 3월 30일 / Commercial Suite 2016년 8월 |
| 수치 | 시야각 약 30°×17.5°(대각 약 34°, 마이크로소프트 비공개·실측 추정) · 홀로그래픽 해상도 2.3M 광점(light points) · 홀로그래픽 밀도 >2.5k radiants(라디안당 광점, 즉 약 43.6 PPD) · CPU Intel Atom x5-Z8100 1GHz(Cherry Trail) · HPU 1세대 = Tensilica DSP 28코어 · RAM 2GB + HPU 1GB · 저장 64GB · 무게 579g · 배터리 2~3시간(대기 2주) · 깊이 카메라 화각 120°×120° · 가격 $3,000(개발자판)/$5,000(Commercial Suite) |
| 출처 | https://en.wikipedia.org/wiki/Microsoft_HoloLens ; Microsoft HoloLens (1st gen) 공식 제원(현재 문서 아카이브) |

투명한 회절 도파관(diffractive waveguide) 렌즈에 상을 실어 보내면서, 동시에 4대의 환경 인식 카메라와 ToF 깊이 카메라로 방을 실시간 삼각측량해 메시(mesh)를 만드는 완전 독립형(untethered) AR 컴퓨터다. 핵심은 HPU(Holographic Processing Unit)라는 전용 보조 칩으로, 28개의 Tensilica DSP 코어가 센서 융합과 SLAM만을 전담해 CPU를 거치지 않고 머리 위치를 추정한다. 이 덕분에 홀로그램이 CPU 부하와 무관하게 방의 좌표계에 고정되며(spatial anchor), 사용자가 걸어 다녀도 제자리에 남는다. 다만 도파관의 초점은 약 2m에 고정되어 있어, 눈의 수렴(vergence)과 초점 조절(accommodation)이 어긋나는 VAC(vergence-accommodation conflict)가 발생한다.

외부 마커도, 베이스 스테이션도, 케이블도 없이 스스로 방을 이해하고 그 위에 세계 고정형 홀로그램을 얹은 최초의 상용 기기였다. 그 이전의 AR은 반드시 외부 인프라(마커·트래커·PC 테더)에 의존했다. '방 안에서 자유롭게 걸어다니는 AR'이 이 기기에서 처음 성립했고, 이후 모든 기기가 이 inside-out 6DoF 구조를 물려받았다.

시야각 30°×17.5°는 '우편함 구멍(letterbox)'이라 불릴 만큼 좁아, 실물 크기 나무나 건물을 한 화면에 담을 수 없었다. 초점면이 약 2m에 고정되어 가까운 거리의 홀로그램은 눈이 피로하다. 입력은 시선(gaze) + 에어탭 제스처뿐이고, 579g의 무게 배분과 2~3시간 배터리로 장시간 현장 작업에는 부적합했다.

### Magic Leap One Creator Edition
| 항목 | 내용 |
| --- | --- |
| 주체 | Magic Leap, Inc. (창업자 Rony Abovitz) |
| 연도 | 출시 2018년 8월 8일(미국, AT&T 독점) / 회사 설립 2010년, 누적 투자 약 $3.5B |
| 수치 | 눈당 해상도 1280×960 · 시야각 대각 50°(수평 40°×수직 30°) · 초점면 2개 · 디스플레이 LCoS + 6층 도파관 · SoC NVIDIA Tegra X2(Parker, Pascal GPU) · RAM 8GB(앱 가용 약 4GB) · 저장 128GB(가용 95GB) · 헤드셋 316g + Lightpack 415g = 약 731g · 가격 $2,295 |
| 출처 | https://en.wikipedia.org/wiki/Magic_Leap ; https://vrarwiki.com/wiki/Magic_Leap_One (커뮤니티 위키, 2차 출처) |

6층으로 적층한 도파관(six-layer waveguide)에 LCoS 프로젝터의 상을 실어 보내되, 그 층들이 서로 다른 두 개의 초점면(dual focal planes)을 만든다는 점이 핵심이다. 눈이 가까운 물체를 볼 때는 가까운 초점면으로, 먼 물체를 볼 때는 먼 초점면으로 전환해 VAC를 완화하려 했다. 연산부는 헤드셋에서 분리해 허리에 차는 'Lightpack'(NVIDIA Tegra X2, 8GB RAM)에 두어, 발열과 배터리 무게를 머리에서 내려놓는 분리형 구조를 택했다. 시선 추적 카메라와 6DoF 컨트롤러가 기본 제공됐다.

초점면을 복수로 둔 최초의 상용 AR 헤드셋이다. HoloLens 1이 단일 고정 초점면이었던 것과 달리, '눈의 초점 거리'까지 디스플레이 변수로 끌어들였다. 또한 헤드셋(316g)과 연산부(415g)를 물리적으로 분리하는 설계는 이후 Meta Orion의 compute puck, Magic Leap 2의 compute pack으로 이어졌다.

초점면이 2개뿐이라 연속적인 깊이 조절은 불가능했고, 50° 대각 시야각도 HoloLens 1보다 넓을 뿐 여전히 좁았다. 26억 달러 이상을 모으며 '광계(light field)'를 약속했지만 실제 결과물은 도파관 기기였다는 점에서 기대와 결과의 격차가 컸다. 소비자 시장 진입에 실패하고 2022년 Magic Leap 2(대각 70°, 세그먼트 동적 디밍)로 기업 전용 전환.

### Microsoft HoloLens 2
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft, Alex Kipman |
| 연도 | 발표 2019년 2월 24일(MWC 바르셀로나) / 출하 2019년 11월 7일 / 단종(소프트웨어 지원 2027년 12월 31일까지) |
| 수치 | 시야각 대각 52°(1세대 34°에서 확대) · 광학엔진 2k 3:2(눈당 1440×936) · 홀로그래픽 밀도 >2.5k radiants ≒ 43.6 PPD · SoC Qualcomm Snapdragon 850 + Adreno 630 · HPU 2.0: 트랜지스터 2 billion, 다이 79mm², SRAM 125MB, >1 TOPS · RAM 4GB LPDDR4x · 저장 64GB UFS 2.1 · 무게 566g · 헤드 트래킹 카메라 4대(초점거리 1.08mm, 대각 FOV 96.1°, 스테레오 베이스라인 98.6mm) · 시선추적 IR 카메라 2대 · 깊이 1MP ToF · 카메라 8MP 스틸/1080p30 · 마이크 5채널 · 배터리 2~3시간 · 전원 18W(9V 2A) · 가격 $3,500 |
| 출처 | https://learn.microsoft.com/en-us/hololens/hololens2-hardware (마이크로소프트 공식) ; https://en.wikipedia.org/wiki/HoloLens_2 (HPU 2.0 다이 제원) |

MEMS 미러로 레이저를 주사(laser beam scanning)해 상을 그린 뒤 나비형(butterfly) 도파관으로 보내는 방식으로 바꿔, 시야각을 대각 34°에서 52°로 넓혔다. 2대의 적외선 카메라가 동공을 실시간 추적해 두 가지 일을 한다 — 사용자의 3차원 눈 위치에 맞춰 렌더링을 보정하고(eye-based rendering), 홍채로 사용자를 식별한다. 1MP ToF 깊이 센서와 2세대 HPU(트랜지스터 20억 개, 79mm² 다이, SRAM 125MB, 초당 1조 연산 이상, DNN 코어 내장)가 손을 25관절 완전 관절 모델로 추적한다. 그 결과 입력이 '시선+에어탭'에서 '홀로그램을 손가락으로 직접 누르고 잡는' 직접 조작(direct manipulation)으로 바뀌었다.

완전 관절형 양손 추적과 시선 추적을 동시에 기본 탑재한 최초의 상용 기기다. 이전까지 손은 '탭하는 클릭커'였지만, 여기서 처음으로 손가락 마디 하나하나가 공간 좌표를 갖고 가상 버튼을 물리적으로 누를 수 있게 됐다. 이 상호작용 문법(핀치·그랩·프레스)이 이후 Quest, Vision Pro, Spectacles의 표준이 됐다.

52°로 넓어졌어도 실물 규모 조경 공간을 덮기엔 여전히 좁고, 초점면은 여전히 단일이다. 566g과 2~3시간 배터리, $3,500이라는 가격 탓에 기업·군수용에 머물렀다. 레이저 주사 방식 특유의 색 균일도(color uniformity) 편차와 도파관 무지개 현상도 지적됐다.

### Varjo XR-3 (바이오닉 디스플레이 / 하드웨어 포비티드)
| 항목 | 내용 |
| --- | --- |
| 주체 | Varjo Technologies (핀란드) |
| 연도 | 발표 2020년 12월 / 출하 2021년 / 단종(XR-4로 대체) |
| 수치 | 포커스 영역 27°×27°, 눈당 1920×1920 μOLED, 70 PPD · 주변 영역 눈당 2880×2720 LCD, 30 PPD 이상 · 수평 시야각 115° · 색역 99% sRGB / 93% DCI-P3 · 시선 추적 200Hz, 1° 미만 정확도, 1점 캘리브레이션 · LiDAR + RGB 융합, 작동 범위 40cm~5m · 패스스루 듀얼 12MP, 90Hz · 무게 594g + 헤드밴드 386g |
| 출처 | https://varjo.com/products/varjo-xr-3/ (Varjo 공식 제원) ; https://en.wikipedia.org/wiki/Varjo (출시 시점) |

사람의 눈은 중심와(fovea) 약 2~3° 범위에서만 최고 해상도로 보고 주변으로 갈수록 급격히 흐려진다. Varjo는 이 생리를 하드웨어로 구현해, 한 눈에 두 개의 패널을 광학적으로 겹쳤다 — 시야 중앙 27°×27°에는 1920×1920 마이크로 OLED를 70 PPD로, 그 바깥 주변부에는 2880×2720 LCD를 30 PPD 이상으로 배치한 '바이오닉 디스플레이'다. 200Hz 시선 추적이 눈이 향한 곳을 읽어 GPU가 그곳만 고해상도로 렌더링한다(foveated rendering). 실사 합성은 12MP 패스스루 카메라 2대를 90Hz로 돌리고 LiDAR와 RGB를 융합해 40cm~5m 범위의 깊이를 얻어 실물에 의한 가림(occlusion)을 처리한다.

사람 눈의 해상도 한계인 60 PPD(1 아크분/픽셀, 시력 1.0 기준)를 처음으로 넘어선 상용 기기다. 중앙 70 PPD는 '픽셀이 보이지 않는' 영역이며, 조경·건축처럼 도면 텍스트와 재질 질감을 판독해야 하는 검토 작업에서 결정적이다. '눈이 보는 곳에 디테일을 더 담는다'는 개념을 소프트웨어(렌더링)가 아니라 광학 하드웨어로 구현한 첫 사례다.

PC 테더 필수(독립 구동 불가)이고 헤드셋+헤드밴드 합계 약 980g으로 장시간 착용이 어렵다. 포커스 패널과 주변 패널의 경계선(seam)이 시야 이동 시 인지되며, 가격이 기업용 수준이라 개인 설계자가 접근할 수 없다.

### Meta Quest Pro
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta Platforms (Reality Labs) |
| 연도 | 공개 2022년 10월 11일 / 출시 2022년 10월 25일 / 단종 2024년 9월(판매 종료 2025년 1월) |
| 수치 | 눈당 해상도 1800×1920 · 주사율 72~90Hz · 디스플레이 미니LED LCD + 퀀텀닷 + 500존 이상 FALD · 팬케이크 렌즈(본체 40% 박형화) · SoC Snapdragon XR2+ Gen 1 · RAM 12GB LPDDR5 · 저장 256GB · 무게 722g · 배터리 1~2시간 · 가격 $1,499.99 → 2023년 3월 $999.99로 인하 |
| 출처 | https://en.wikipedia.org/wiki/Meta_Quest_Pro |

팬케이크(pancake) 광학계를 메타 제품 최초로 채택했다. 편광을 이용해 빛을 반투과 거울과 반사 편광판 사이에서 3번 접어 왕복시키므로, 광학 경로 길이는 유지한 채 패널-렌즈 물리 거리를 크게 줄일 수 있어 본체가 약 40% 얇아졌다. 디스플레이는 미니LED LCD에 퀀텀닷 층을 얹고 500개 이상의 로컬 디밍 존(FALD)을 두어 검정 표현을 개선했다. 안쪽을 향한 카메라로 시선 추적과 얼굴 표정 추적을 동시에 수행해, 시선 기반 포비티드 렌더링(ETFR)과 아바타의 눈맞춤·표정 재현이 가능해졌다.

대중 브랜드 헤드셋 중 시선 추적 + 얼굴 추적 + 팬케이크 광학을 한 번에 담은 첫 제품이다. HoloLens 2가 기업용 $3,500에서 보여준 시선 추적을, 절반 이하 가격대의 소비자 생태계로 끌어내렸다. 이 시선 추적이 없었다면 1년 뒤 Vision Pro의 '보고 집는' 입력 문법도 시장에서 낯설었을 것이다.

컬러 패스스루가 여전히 노이즈가 많고 해상도가 낮아 실물 판독에 부적합했다. 722g에 배터리 1~2시간, $1,499라는 조합으로 상업적으로 실패했고 2년 만에 단종됐다. 얼굴 추적도 실사용 콘텐츠가 부족해 활용되지 못했다.

### Meta Quest 3
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta Platforms (Reality Labs) |
| 연도 | 공개 2023년 6월 1일 / 출시 2023년 10월 10일 |
| 수치 | 눈당 2064×2208 RGB 스트라이프 LCD(Quest 2 대비 화소 약 30% 증가) · 주사율 90~120Hz · 팬케이크 2매 구성 · IPD 53~75mm 무단 조절 · 패스스루 4MP RGB 카메라 2대 · 트래킹 IR 카메라 4대(각 400×400px) · IR 구조광 깊이 센서 1개 · SoC Snapdragon XR2 Gen 2 + Adreno 740 @640MHz · RAM 8GB LPDDR5 · 무게 515g · Wi-Fi 6E, Bluetooth 5.2 · 가격 $499.99(128GB) / $649.99(512GB) |
| 출처 | https://en.wikipedia.org/wiki/Meta_Quest_3 |

눈당 2064×2208 LCD와 2매 구성 팬케이크 렌즈를 쓰고, 전면에 4MP RGB 카메라 2대 + 적외선 구조광(structured light) 깊이 센서를 달았다. 깊이 센서가 핵심인데, 방의 3차원 메시를 자동 생성해 가상 객체가 실제 소파나 벽 뒤로 자연스럽게 가려지도록(occlusion) 만든다. 즉 Quest 3에서 '패스스루'는 배경 영상이 아니라 기하학적으로 이해된 공간이 됐다. 다만 이것은 광학 투과(optical see-through)가 아니라 카메라 영상 투과(video passthrough)이므로, 사용자가 보는 현실은 어디까지나 카메라가 재구성한 화면이다.

499달러짜리 대량생산 기기가 컬러 패스스루 MR을 기본 모드로 만든 전환점이다. HoloLens 2($3,500)의 1/7 가격에 더 높은 화소수를 제공했고, 깊이 센서를 소비자 헤드셋에 처음 넣어 '스캔 없이 방을 이해하는' 경험을 표준화했다. 조경·설계 분야에서 현실적으로 다수 대여·보급이 가능한 최초의 기기이기도 하다.

광학 투과가 아니라 영상 투과라서 현실은 카메라 지연·왜곡·저조도 노이즈를 거친 상태로 보인다. 515g의 전면 하중, 2시간 남짓한 배터리, 그리고 완전히 눈을 가리는 형태라 현장 답사용으로는 안전상 제약이 크다. 깊이 센서의 유효 거리도 실내 규모에 맞춰져 있어 넓은 옥외 공간 인식에는 한계가 있다.

### Apple Vision Pro
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple Inc. |
| 연도 | 발표 2023년 6월 5일(WWDC) / 미국 출시 2024년 2월 2일 / M5 개정판 2025년 10월 15일 |
| 수치 | 총 2,300만 화소 · 눈당 약 3,660×3,200(iFixit 실측, 애플 미공개) · 마이크로 OLED 화소 피치 7.5μm · 색역 92% DCI-P3 · 주사율 90/96/100Hz(M5판 최대 120Hz) · M2: 8코어 CPU(성능 4+효율 4), 10코어 GPU, 16코어 Neural Engine, 통합메모리 16GB, 대역폭 256GB/s · R1: 광자 대 광자 지연 12ms · 카메라 12대(고해상도 메인 2, 외부 트래킹 6, 시선 추적 4) + TrueDepth + LiDAR + IMU 4개 + 플리커 센서 + 조도 센서 · 마이크 6개 빔포밍 · 메인 카메라 18mm ƒ/2.00, 스테레오 6.5MP · IPD 51~75mm · 무게 600~650g(라이트실·밴드 구성에 따라 변 |
| 출처 | https://www.apple.com/apple-vision-pro/specs/ (2024-01 아카이브판) ; https://www.apple.com/newsroom/2023/06/introducing-apple-vision-pro/ ; iFixit, "Vision Pro Teardown Part 2 - Is the Apple Vision Pro Really 4K?", 2024-02-07, 1:36 지점(눈당 해상도 실측) |

두 개의 칩을 역할로 쪼갠 것이 이 기기의 뼈대다. M2가 앱과 OS를 돌리는 동안, 오직 센서 융합만 담당하는 R1 칩이 12대의 카메라·5개 센서·6개 마이크의 입력을 받아 12밀리초 안에 디스플레이로 새 영상을 밀어낸다. 표시부는 우표 크기 실리콘 웨이퍼 위에 7.5마이크로미터 화소 피치로 만든 마이크로 OLED 2장으로, 합계 2,300만 화소(iFixit 실측 눈당 약 3,660×3,200)다. 4대의 적외선 카메라와 LED 링이 동공에 보이지 않는 패턴을 쏘아 시선을 읽고, 이 시선이 곧 커서가 되어 손가락 핀치가 클릭을 대신하므로 컨트롤러가 없다. 바깥쪽에는 렌티큘러 렌즈를 덮은 곡면 OLED(EyeSight)를 두어 착용자의 눈을 외부에 재현한다.

'광자 대 광자 12밀리초'라는 수치가 도약의 본질이다. 카메라로 찍은 현실을 눈에 다시 보여주기까지의 지연을 멀미 임계 아래로 낮췄고, 눈당 3,660픽셀급 해상도와 결합되어 사상 처음으로 '패스스루 화면 너머로 종이 글씨를 읽을 수 있는' 수준에 도달했다. 또한 시선+손만으로 OS 전체를 조작하는 최초의 주류 제품이며, 착용자의 눈을 바깥에 표시하는 EyeSight는 Google Glass가 남긴 사회적 고립 문제에 대한 하드웨어적 응답이다.

$3,499의 가격, 얼굴에 얹히는 600~650g, 케이블로 연결된 353g 외장 배터리와 2시간 사용 시간이 현장 활용을 제한한다. 시야각은 애플이 공식 발표하지 않았고(제3자 추정 약 100°×73°), EyeSight 외부 디스플레이는 렌티큘러로 화면을 분할하는 구조상 어둡고 해상도가 낮다고 iFixit이 지적했다. 광학 투과가 아니므로 밝은 옥외에서는 카메라 노출 한계가 그대로 드러난다.

### Meta Orion (프로토타입, 구 코드명 Project Nazare)
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta Platforms (Reality Labs) |
| 연도 | 공개 2024년 9월 25일(Meta Connect) / 판매 없음, 사내 및 선별 외부 대상 개발 키트 |
| 수치 | 시야각 약 70°(메타 공식, 축 미명시 / 2차 출처 추정 수평 70°×수직 52°) · 도파관 재료 광학급 탄화규소 · 광원 마이크로LED 프로젝터 · 프레임 마그네슘 · 무게 98g(보도 기준, 메타 공식 수치 아님) · 각해상도 약 13 PPD(2차 출처) · 제조원가 약 $10,000/대(보도) · 배터리 2~3시간(2차 출처) · 입력: 음성 + 시선 추적 + 손 추적 + EMG 손목밴드 · 무선 컴퓨트 퍽 별도 |
| 출처 | https://www.meta.com/emerging-tech/orion/ 및 https://www.meta.com/emerging-tech/orion/silicon-carbide/ (메타 공식) ; https://about.fb.com/news/2024/09/introducing-orion-our-first-true-augmented-reality-glasses/ ; 무게·PPD·원가는 https://vrarwiki.com/wiki/Meta_Orion 등 2차 출처 |

도파관 기판 재료를 유리가 아닌 광학급 탄화규소(silicon carbide, SiC)로 바꾼 것이 핵심 발명이다. 도파관이 전반사로 가둘 수 있는 각도 범위는 굴절률에 비례하는데, SiC는 굴절률이 약 2.6으로 일반 광학유리보다 훨씬 높아 같은 두께에서 훨씬 넓은 시야각을 만들 수 있고, 고굴절 유리에서 흔한 무지개(rainbow) 산란도 줄인다. 광원은 관자놀이 안에 들어갈 만큼 작고 효율 높은 마이크로LED 프로젝터를 쓰며, 프레임은 마그네슘이다. 무거운 연산은 무선 '컴퓨트 퍽'으로 내보내고, 입력은 음성·시선·손 추적에 더해 손목에 차는 EMG(근전도) 밴드가 담당해, 손이 카메라 시야 밖에 있거나 어두워도 손가락 미세 동작을 읽는다.

안경 형태를 유지한 채 약 70°의 시야각을 낸 최초의 진짜 시스루 AR 안경이다. HoloLens 2(대각 52°, 566g)와 비교하면 시야는 넓히고 무게는 약 1/6(보도 기준 98g)로 줄였다. 동시에 sEMG 손목밴드라는 '신경 입력'을 제품 수준으로 시연해, 카메라가 손을 봐야만 하는 제스처 입력의 근본 제약을 깼다.

제품이 아니다. 메타 스스로 '제조 공정이 너무 복잡하고 비싸서' 소비자 판매를 포기했다고 밝혔다. 약 13 PPD로 각해상도가 매우 낮아 세밀한 도면이나 작은 글자는 읽기 어렵고, 무선 퍽이 반드시 필요하며, 밝기·명암비 수치는 메타가 공개하지 않았다.

### Snap Spectacles (5세대, 2024 개발자판)
| 항목 | 내용 |
| --- | --- |
| 주체 | Snap Inc. |
| 연도 | 공개·개발자 배포 2024년 9월 17일(Snap Partner Summit) |
| 수치 | 무게 226g · 시야각 대각 46° · 해상도 37 PPD(10피트 거리 100인치 화면 상당) · 디스플레이 LCoS 마이크로 프로젝터 + 나노구조 도파관 · 카메라 4대(공간 인식·손 추적) · 듀얼 스냅드래곤 SoC 구조 · 티타늄 증기챔버 방열 · 연속 독립 구동 45분 · 모션-투-포톤 지연 13ms · 자동 틴팅 · 개발자 프로그램 월 $99, 1년 약정 |
| 출처 | https://newsroom.snap.com/sps-2024-spectacles-snapos (스냅 공식) ; https://en.wikipedia.org/wiki/Spectacles_(product) |

스냅이 자체 설계한 '옵티컬 엔진'은 아주 작은 LCoS 마이크로 프로젝터가 만든 상을, 수십억 개의 나노 구조가 새겨진 도파관을 통해 눈으로 밀어 넣는 구조다. 이 나노 구조 덕분에 사용자마다 별도의 광학 캘리브레이션이나 맞춤 피팅 없이 바로 쓸 수 있다. 연산은 하나의 칩이 아니라 두 개의 스냅드래곤을 병렬로 두어 작업을 분산시키고, 티타늄 증기챔버(vapor chamber)로 열을 빼낸다. 주변 밝기에 따라 렌즈 틴트가 자동으로 짙어져 직사광선 아래에서도 상이 보이도록 했고, 모션-투-포톤 지연은 13밀리초다.

226g이라는, VR 헤드셋의 절반 이하 무게로 완전 독립 구동하는 스테레오(양안) 시스루 AR 안경을 공개 프로그램으로 실제 배포한 최초 사례다. HoloLens 2의 43.6 PPD에 근접한 37 PPD를 안경 형태에서 냈고, 13ms 모션-투-포톤은 Vision Pro의 12ms와 같은 급이다. '연구실 프로토타입'이 아니라 누구나 월 구독으로 받아 쓸 수 있었다는 점이 중요하다.

연속 구동 45분은 현장 작업에 결정적 제약이다. 대각 46° 시야각, 개발자 전용 월 $99 구독(1년 약정) 구조라 일반 소비자가 구매할 수 없었다. 밝기(니트) 수치는 스냅이 공개하지 않았다.

### Meta Ray-Ban Display + Meta Neural Band
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta Platforms + EssilorLuxottica (Ray-Ban) |
| 연도 | 발표 2025년 9월 17일(Meta Connect 2025) / 미국 판매 개시 2025년 9월 30일 |
| 수치 | 가격 $799(안경 + Neural Band 포함) · 안경 배터리 혼합 사용 최대 6시간, 휴대용 접이식 충전 케이스 포함 총 30시간 · Neural Band 배터리 최대 18시간, IPX7 방수 · Transitions 변색 렌즈 · 2차 출처 기준 디스플레이: LCoS 600×600, 밝기 5,000니트(OmniVision 패널), 시야각 대각 20°(대각 42 PPD에 해당), Lumus 도파관 · sEMG 연구 참가자 약 200,000명 · 미국 오프라인 판매처 Best Buy, LensCrafters, Sunglass Hut, Ray-Ban Store |
| 출처 | https://about.fb.com/news/2025/09/meta-ray-ban-display-ai-glasses-emg-wristband/ (메타 공식: 가격·배터리·출시일) ; https://www.microled-info.com/meta-launches-its-first-ai-ar-glasses-lcos-display (디스플레이 제원, 2차 출처) |

Orion의 기술 가운데 상용화 가능한 두 조각 — 작은 디스플레이와 EMG 입력 — 만 떼어내 레이밴 안경테에 넣은 제품이다. 오른쪽 렌즈 안에 단안(monocular) 컬러 디스플레이가 들어가며, 필요할 때만 켜지고 평소에는 사라진다. 조작은 안경을 만지지 않고 손목의 Meta Neural Band가 담당한다. 이 밴드는 근육이 수축할 때 피부 표면에 나타나는 전위(표면 근전도, sEMG)를 읽어 손가락의 미세한 움직임을 명령으로 번역하므로, 주머니 속이나 책상 아래에서도 조작이 가능하다. 메타는 이 기술이 약 20만 명의 연구 참가자 데이터를 토대로 만들어졌다고 밝혔다.

시야에 정합되는 6DoF AR은 아니지만, '디스플레이 + 신경 입력'을 $799라는 스마트폰 액세서리 가격대에서 일반 소비자에게 판매한 최초의 제품이다. 연구 단계였던 sEMG 입력이 처음으로 소매점 진열대에 올라왔다는 점에서, 입력 방식의 역사에서 마우스·터치스크린과 같은 층위의 사건으로 평가할 만하다.

단안이고 시야각이 대각 20°에 불과해 공간에 고정되는 홀로그램을 표시하지 못한다. 즉 Azuma(1997)의 3차원 정합 조건을 충족하지 않는 헤드업 디스플레이에 가깝다. 디스플레이 해상도·밝기·도파관 공급사는 메타 공식 자료가 아니라 산업 매체(microLED-Info)의 보도에 근거하므로 검증이 필요하다.

### Snap SPECS (소비자용, 2026)
| 항목 | 내용 |
| --- | --- |
| 주체 | Snap Inc. (specs.com) |
| 연도 | 발표 2026년 6월 16일 / 2026년 9월 현재 미국·영국·프랑스 선주문(보증금) 단계, 배송 시작 전 |
| 수치 | 시야각 51°(약 3m 거리의 115인치 스크린 상당) · 무게 132g(47mm Narrow Fit) / 136g(52mm Wide Fit) · 프레임 스위스 TR90 폴리머 · MEMS 마이크 6개(고 SNR) + 관자놀이 내장 스테레오 스피커 · 색 표현 1,600만 색 · 선주문 지역 미국·영국·프랑스 · 반품 14일, 보증 1년 |
| 출처 | https://www.specs.com/ (스냅 공식 제품 페이지, 2026-09-29 확인) ; https://en.wikipedia.org/wiki/Spectacles_(product) (발표일 2026-06-16) |

2024년 개발자판 Spectacles의 후속으로, 같은 나노구조 시스루 도파관 구조를 유지하면서 시야각을 46°에서 51°로 넓히고 무게를 226g에서 132g으로 거의 절반까지 줄인 소비자용 모델이다. 프레임은 스위스산 TR90 폴리머로 47mm(Narrow Fit)와 52mm(Wide Fit) 두 가지 크기로 나오며, 코받침을 교체해 맞춘다. 관자놀이 부분에 스테레오 스피커와 신호대잡음비가 높은 MEMS 마이크 6개를 내장해 통화와 음성 명령을 처리한다. 1,600만 색을 표현하는 대화면 가상 스크린을 띄우는 것이 주요 활용 시나리오로 제시됐다.

2년 만에 무게 226g → 132g(-42%), 시야각 46° → 51°를 동시에 달성해, AR 안경이 '개발자 장비'에서 '일반 안경 무게의 착용물'로 넘어가는 지점을 보여준다. 132g은 Meta Orion의 98g과 일반 선글라스(약 30~50g) 사이에 위치한다.

2026년 9월 29일 현재 스냅이 가격, 배송 일정, 해상도(PPD), 밝기, 프로세서, 배터리 지속시간을 공개하지 않았다. 선주문은 환불 가능한 보증금 단계이며 주문 확정이 아니다. 따라서 실제 성능은 아직 검증 불가.

#### 검증에서 잡힌 정정
- [확정 오류] Apple Vision Pro — "M2: … 통합메모리 16GB, 대역폭 256GB/s"는 오귀속. 애플 공식 제원 페이지에서 256GB/s는 M칩이 아니라 **R1 칩**의 memory bandwidth 항목이다(현행 M5판 페이지: M5=153GB/s, R1=256GB/s로 별도 기재). 베이스 M2의 대역폭은 128비트 버스 **100GB/s**(en.wikipedia.org/wiki/Apple_M2). 즉 M2 대역폭은 100GB/s로, 256GB/s는 R1 항목으로 옮겨야 한다.
- [확정 오류] Microsoft HoloLens 2 — "HPU 2.0: … SRAM 125MB"는 단위 오류. 인용 출처(en.wikipedia.org/wiki/HoloLens_2)는 "125 **Mb** SRAM"(메가비트)로 기재. 125 Mb ≈ 15.6 MB이므로 보고서 값은 약 8배 과장. 같은 문단의 2 billion transistors·79 mm² 다이·>1 TOPS는 출처와 일치.
- [시점 오류] Apple Vision Pro 가격 "$3,499" — 2024년 출시가로는 맞으나 현재(2026-09-29) 기준 틀림. 2026년 6월 $3,699로 인상됨(en.wikipedia.org/wiki/Apple_Vision_Pro). '출시가 $3,499 → 현재 $3,699'로 명시 필요.
- [시점/구성 오류] Apple Vision Pro "무게 600~650g", "배터리 일반 2시간/영상 2.5시간" — M2 모델 기준으로는 정확하나, 현행 M5 모델 공식 제원은 **750~800g**, **일반 최대 2.5시간/영상 최대 3시간**. 표에 M5 개정판을 병기해 놓았으므로 세대 구분 없이 M2 값만 적으면 오독을 낳는다.
- [날짜 오류] Apple Vision Pro "M5 개정판 2025년 10월 15일" — 10월 15일은 **발표일**이고 실제 **출시(판매 개시)는 2025년 10월 22일**(선별 지역). 다른 기기는 발표일/출시일을 구분해 적었으므로 일관성이 깨짐.
- [연도 귀속 오류] Magic Leap "회사 설립 2010년, 누적 투자 약 $3.5B" — $3.5B는 en.wikipedia.org/wiki/Magic_Leap 기준 **2024년 8월 시점의 누적** 조달액("at least $3.5 billion"). Magic Leap One이 출시된 2018년 8월 시점 누적 조달액은 약 $2.3~2.6B 수준이므로, 2018년 제품 항목에 $3.5B를 병기한 것은 시점 오귀속.
- [출처 오류] Magic Leap One의 하드웨어 제원(1280×960, 대각 50°(40°×30°), 2개 초점면, LCoS+6층 도파관, Tegra X2, RAM 8GB(가용 4GB), 저장 128GB(가용 95GB), 316g+415g) 전부를 en.wikipedia.org/wiki/Magic_Leap 에 귀속시켰으나, 해당 위키 문서에는 이 수치가 **하나도 없다**(회사 연혁·투자·LCoS 언급만 존재). 실제로 이 수치들과 일치하는 것은 2차 출처 vrarwiki.com/wiki/Magic_Leap_One 뿐이므로, 1차 출처 표기를 정정해야 한다. (수치 자체는 vrarwiki와 전부 일치)
- [출처 오류] Microsoft HoloLens 2의 "시야각 대각 52°"와 "광학엔진 2k 3:2(눈당 1440×936)"를 learn.microsoft.com/en-us/hololens/hololens2-hardware(공식)에 귀속시켰으나, 해당 공식 페이지는 **시야각을 전혀 기재하지 않으며** 홀로그래픽 해상도도 "2k 3:2 light engines"라고만 적고 눈당 픽셀 수를 제시하지 않는다. 52°와 1440×936은 위키피디아/커뮤니티 수치다. (반면 같은 항목의 566g, 4GB LPDDR4x, 64GB UFS 2.1, 1MP ToF, 8MP/1080p30, 마이크 5채널, VLC 4대·초점거리 1.08mm·대각 96.1°·베이스라인 98.6mm, 18W(9V 2A)는 공식 페이지와 정확히 일치)
- [죽은 출처] HoloLens 1세대 항목이 인용한 "Microsoft HoloLens (1st gen) 공식 제원" 문서(learn.microsoft.com/en-us/hololens/hololens1-hardware)는 현재 **HTTP 404**로 접근 불가. 1세대의 2.3M 광점·>2.5k radiants는 현재 검증 가능한 1차 출처가 없는 상태이므로 아카이브 URL을 명시하거나 '공식 페이지 삭제됨'을 병기해야 한다.
- [내부 산술 불일치] HoloLens 2에 대해 ">2.5k radiants ≒ 43.6 PPD"와 "눈당 1440×936", "대각 52°"를 동시에 적었으나 서로 맞지 않는다. 1440×936의 대각 픽셀 수는 1717px이고 이를 대각 52°로 나누면 **약 33 PPD**(43.6이 아님). 43.6 PPD는 2k(2048px)급 광학엔진을 가정해야 나오는 값이다(≈47 PPD). 참고로 HoloLens 1은 1268×720/대각 34.7° ≈ 42 PPD로 43.6과 정합하므로, 불일치는 2세대 행에만 있다. 위키피디아 HoloLens 2 문서도 실측 각해상도가 "20 PPD 미만"이라는 반론을 병기하고 있다.
- [미확인/출처 충돌] HoloLens 1세대 "HPU 1세대 = Tensilica DSP **28**코어" — 인용한 위키피디아는 "28 custom DSPs from Tensilica"로 적고 있어 표기 자체는 출처와 일치하나, 마이크로소프트가 Hot Chips 2016에서 직접 공개한 HPU 1.0 제원은 **24 Tensilica DSP 코어**(TSMC 28nm, 로직 게이트 6,500만, SRAM 8MB)로 널리 인용된다. '28'은 공정 노드 28nm와 혼동된 수치일 가능성이 높다. 이번 세션은 WebSearch 예산 소진 + wikichip 접속 실패로 1차 확인에 실패했으므로 **'24 또는 28, 1차 출처 재확인 필요'**로 유보 표기할 것.
- [미확인] HoloLens 1세대 "Commercial Suite 2016년 8월" — 위키피디아는 Development Edition 출하일(2016-03-30)과 Commercial Suite 가격($5,000, 2017년 5월 기준)만 확인해 줄 뿐 2016년 8월이라는 **출시월을 뒷받침하지 않는다**. 출처 보강 또는 삭제 필요.
- [저신뢰] Google Glass "무게 36g" — 인용한 위키피디아 제원표와는 일치하나, 구글은 Glass의 무게를 공식 제원으로 공표한 적이 없고 실제 계측 리뷰는 대체로 42~50g 범위를 보고했다. '위키피디아 기재값(비공식)'임을 명시할 것. 같은 항목의 640×360(2.4m/25인치), 5MP·720p, OMAP4430 1.2GHz, 1GB→2GB, 16GB(가용 12GB), 570mAh, $1,500/£1,000, 배포 2013-04-16, 일반판매 2014-04-15, 중단 2015년 1월은 위키피디아와 일치.
- [정확성 보강] Google Glass "일반 판매 2014년 4월 15일"은 미국에서의 **1일 한정 판매**였으므로 상시 판매 개시로 읽히지 않도록 단서가 필요.
- [검증 통과 — 반박 없음] Meta Quest 3(2064×2208 RGB-stripe LCD, 90~120Hz, 팬케이크 2매, IPD 53~75mm, 4MP RGB 2대, 400×400 IR 4대, IR 구조광, XR2 Gen 2+Adreno 740@640MHz, 8GB LPDDR5, 515g, Wi-Fi 6E/BT 5.2, $499.99/$649.99, 2023-06-01 공개·2023-10-10 출시) 전 항목 위키피디아와 일치. Quest 3의 '화소 약 30% 증가'도 Quest 2(1832×1920=3.52M) 대비 4.56M로 +29.5%로 산술 정합.
- [검증 통과 — 반박 없음] Meta Quest Pro(1800×1920, 72~90Hz, MiniLED LCD+퀀텀닷+>500존 FALD, 팬케이크 40% 박형화, XR2+ Gen 1, 12GB LPDDR5, 256GB, 722g, 1~2시간, $1,499.99→2023년 3월 $999.99, 2024년 9월 단종·2025년 1월 판매종료), Varjo XR-3(27°×27° 1920×1920 μOLED 70 PPD, 주변 2880×2720 LCD 30 PPD 초과, 수평 115°, 99% sRGB/93% DCI-P3, 시선추적 200Hz·1° 미만·1점 캘리브레이션, LiDAR+RGB 40cm~5m, 듀얼 12MP 90Hz, 594g+386g), Snap Spectacles 5세대(226g, 대각 46°, 37 PPD, LCoS+나노구조 도파관, 카메라 4대, 듀얼 스냅드래곤, 티타늄 증기챔버, 45분, 13ms, 월 $99·1년 약정, 2024-09-17) 모두 공식 출처와 일
- [검증 통과 — 반박 없음] Meta Ray-Ban Display($799, 2025-09-30 미국 판매, 안경 6시간/케이스 포함 30시간, Neural Band 18시간·IPX7, Best Buy·LensCrafters·Sunglass Hut·Ray-Ban Store, sEMG 참가자 약 20만 명)는 메타 공식 발표문과 일치하고, 디스플레이(LCoS 600×600, 5,000니트, OmniVision, Lumus 도파관, 대각 20°)는 microled-info 2차 출처와 일치하며 2차 출처임을 올바르게 표기했다. 600×600의 대각 848px÷20°=42.4 PPD도 산술 정합. 다만 캐나다·프랑스·이탈리아·영국 확대(2026년 초 예정)가 누락되어 있다.
- [검증 통과 — 반박 없음] Meta Orion: 메타 공식 페이지가 '약 70도 시야각·광학등급 탄화규소(SiC)·마그네슘 프레임'을 직접 명시하고, about.fb.com 발표문이 'Orion, previously codenamed Project Nazare'를 확인해 준다. 98g·13 PPD·$10,000·2~3시간·수평 70°×수직 52°는 vrarwiki 기재값과 정확히 일치하며 보고서가 '2차 출처'로 정직하게 표기했다.
- [검증 통과 — 반박 없음] Snap SPECS(2026): specs.com 공식 페이지가 51° 시야각·약 10피트 거리 115인치 상당, 47mm Narrow 132g/52mm Wide 136g, 스위스 TR90, 고SNR MEMS 마이크 6개+관자놀이 스테레오 스피커, 1,600만 색, 미국·영국·프랑스 선주문(환불 가능 보증금), 14일 반품·1년 보증을 모두 확인. 발표일 2026-06-16도 위키피디아와 일치하며 '배송 시작 전'도 맞다(예상 배송 2026년 가을).
- HoloLens 2 HPU 2.0 'SRAM 125MB' → 틀림. 원출처(Wikipedia HoloLens 2, Microsoft HotChips 발표)는 '125 Mb SRAM' 즉 125 메가비트 = 약 15.6 MB. 단위(Mb↔MB) 오독으로 8배 과장.
- Magic Leap '누적 투자 약 $3.5B'를 2018년 8월 출시 정보와 함께 제시 → 시점 오류. $3.5B는 사우디 PIF $750M을 포함한 2024년 8월 기준 누계(Wikipedia). 2018년 8월 Magic Leap One 출시 당시 누적 조달액은 약 $2.3B.
- 목록 배열 선후 역전: Snap Spectacles 5세대는 2024년 9월 17일 공개, Meta Orion은 2024년 9월 25일 공개. Spectacles 5세대가 8일 앞서므로 Orion 앞에 와야 하는데 뒤에 배치됨.
- Snap SPECS '발표 2026년 6월 16일' → 인용한 Wikipedia(Spectacles 제품 문서)는 'In June 2026 Specs Inc. Announced SPECS'까지만 기술하며 '16일'이라는 일자는 없음. specs.com 공식 페이지에도 발표 일자 명기 없음. 일자 미확인.
- Snap SPECS 연혁 누락으로 선후 왜곡: 'In June 2025, Snap revealed that they will start selling a consumer version of their AR glasses in 2026'(최초 공표 2025년 6월, AWE)과 '2026년 1월 28일 자회사 Specs Inc. 설립'이 빠져, 2026년 6월이 최초 발표인 것처럼 읽힘. 2026년 6월은 제품 공개·선주문 개시 시점.
- HoloLens (1st gen) 'Commercial Suite 2016년 8월' → 확인 불가. 인용한 Wikipedia는 'As of May 2017, the suite sold for US$5,000'만 기술하고 가용 개시일을 제시하지 않음. Microsoft 공식 블로그(blogs.windows.com / news.microsoft.com 2016-08-02 URL 후보)는 모두 404. 어떤 1차 출처로도 2016년 8월을 확인하지 못함.
- HoloLens 2 '광학엔진 2k 3:2(눈당 1440×936)' → 인용한 Microsoft 공식 페이지(learn.microsoft.com/en-us/hololens/hololens2-hardware)에는 '2k 3:2 light engines'만 있고 1440×936은 없음. 해당 수치는 Wikipedia 등 2차 출처. 공식 출처로 오귀속.
- Apple Vision Pro 출처 불일치: 인용 URL(apple.com/apple-vision-pro/specs/)은 2026-09-29 현재 M5 모델을 기술 — 무게 '26.4–28.2 ounces (750–800 grams)', '일반 사용 최대 2.5시간 / 영상 재생 최대 3시간', 'M5 10코어 CPU(super core 4 + efficiency core 6) + 10코어 GPU', 지원 주사율 '90Hz, 96Hz, 100Hz, 120Hz'. 본문의 600~650g·2시간/2.5시간·M2 8코어 CPU·10코어 GPU는 2024년 M2 모델에만 유효하며 현재 공식 페이지 값이 아님.
- Apple Vision Pro 가격 '$3,499' → 2026-09-29 기준 낡음. Wikipedia에 따르면 2026년 6월 25일 시작가가 $3,699(256GB)로 인상됨.
- Google Glass 프로젝트 리더 'Babak Parviz·Thad Starner' → 인용한 Wikipedia Google Glass 문서에는 두 사람 이름이 없음(문서는 'developed by Google X'와 Sergey Brin의 프로토타입 착용만 언급). 인용 출처가 뒷받침하지 않는 주장.
- Meta Ray-Ban Display 'sEMG 연구 참가자 약 200,000명' → Meta 공식 문구는 'nearly 200,000 research participants'(20만 명에 근접, 즉 20만 미만). '약 200,000명'은 방향성이 반대로 읽힐 수 있는 반올림.
- (외 15건)

## interaction
항목 12개 · 검증 정정 지적 42건


### HoloLens 2 관절형 손 추적 (articulated hand tracking, 26관절)
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft (검증 연구: Bertolasi, Garcia-Hernandez, Memeo, Guarischi, Gori — Istituto Italiano di Tecnologia) |
| 연도 | 2019년 2월 발표(MWC), 2019년 11월 출시 / 정확도 검증 논문 2025년 |
| 수치 | 한 손 26관절(HandJointKind 0~25, OpenXR XR_EXT_hand_tracking도 동일하게 26). 깊이 센서 1-MP ToF, 머리 추적 가시광 카메라 4대, 시선 추적 IR 카메라 2대, 마이크 5채널, 무게 566 g, Snapdragon 850 + 2세대 HPU, 배터리 2~3시간. 가시광 카메라 초점거리 1.08 mm, 대각 FOV 96.1도, 스테레오 베이스라인 98.6 mm. 정확도(Vicon 모션캡처 대조): 손끝 위치 오차 2~4 mm, 관절 굽힘각 평균 오차 5도. |
| 출처 | https://learn.microsoft.com/en-us/windows/mixed-reality/design/direct-manipulation · https://learn.microsoft.com/en-us/uwp/api/windows.perception.people.handjointkind · https://learn.microsoft.com/en-us/hololens/hololens2-hardware · Bertolasi, J., Garcia-Hernandez, N., Memeo, M., Guarischi, M., Gori, M. (2025) "Evaluation of HoloLens 2 for Hand Tracking and Kinematic Features Assessment", Virtual  |

HoloLens 2는 손을 '점 하나'가 아니라 **뼈대 모델 전체**로 추적한다. Windows Perception API의 HandJointKind 열거형은 손바닥(Palm)·손목(Wrist)에 더해 엄지 4개, 나머지 네 손가락 각 5개(중수골·근위·중간·원위·끝)를 합쳐 한 손당 **0~25번, 총 26개 관절**을 정의한다. 이 관절들은 1-MP Time-of-Flight 깊이 센서가 만든 거리 영상과 4대의 가시광 카메라가 만든 머리 추적 좌표계 위에서 매 프레임 자세(위치+방향)로 풀려 나온다. 각 관절은 '전방(-z)은 손끝, 위(+y)는 손등' 규약으로 방향까지 갖기 때문에, 손가락이 굽은 각도까지 앱이 직접 읽을 수 있다. 즉 개발자는 '탭했다/안 했다'는 이벤트가 아니라 손의 기하학 자체를 입력으로 받는다. 이것이 마커나 컨트롤러 없이 맨손으로 홀로그램을 잡는 상호작용의 물리적 토대다.

HoloLens 1세대(2016)는 손 전체를 '한 점 + 에어탭/블룸 두 가지 상징 제스처'로만 읽었다. 사용자는 기계가 알아듣는 동작을 **외워야** 했다. 2세대는 26관절 전체를 풀어냄으로써 '버튼을 손가락으로 누른다', '모서리를 잡아 늘린다' 같은 현실 세계의 동작을 그대로 쓸 수 있게 했다. Microsoft 문서는 이를 두고 'HoloLens 2에서는 상징적 제스처를 외우게 하지 않는다(we don't ask users to memorize any symbolic gestures)'고 못 박는다. 외워야 하는 인터페이스에서 몸이 이미 아는 인터페이스로 넘어간 지점이다.

카메라 시야(FOV) 밖으로 손이 나가면 추적이 끊긴다. 손이 손을 가리는 자가폐색(self-occlusion) 상황에서 오차가 커진다. 촉각 피드백이 없어 '눌렀다'는 감각을 시각·청각으로 대체해야 한다. 정확도 검증은 실내 통제 환경에서 이뤄졌고, 야외 직사광 아래 IR·ToF 센서 성능은 별도 문제다(조경 현장에 그대로 옮기기 어려운 이유).

### 직접 조작(Direct manipulation) — 충돌 가능한 손끝과 근접 셰이더
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft Mixed Reality 디자인팀 |
| 연도 | 2019년(HoloLens 2와 함께 공개) |
| 수치 | 충돌체는 검지 1개만 권장(양손 10개 아님). 구 충돌체 지름 = 손가락 굵기(핸드 API에서 조회). 근거리 상호작용 권장 범위 = 팔 길이 이내. 터치 제스처 4종: 한 손가락 누르기·한 손가락 탭·두 손가락 누르기·다섯 손가락 누르기. |
| 출처 | https://learn.microsoft.com/en-us/windows/mixed-reality/design/direct-manipulation |

손 뼈대를 얻었다고 바로 '만질 수 있게' 되지는 않는다. 손끝 10개 전부에 충돌체(collider)를 붙이면, 촉각 피드백이 없는 탓에 사용자가 의도하지 않은 충돌이 끊임없이 일어난다. Microsoft의 해법은 **검지 끝 하나에만 구(球) 충돌체를 두고**, 그 지름을 손가락 굵기에 맞추는 것이다. 여기에 손끝이 표면에 다가갈수록 작아지는 도넛 모양 '손끝 커서'와, 홀로그램 표면에 스포트라이트를 비추는 '근접 셰이더(proximity shader)'를 더해 깊이 감각을 시각으로 대신한다. 버튼은 손끝을 따라 실제로 눌려 들어가다가(depression) 정해진 깊이에 도달하면 발화한다. 즉 **없는 촉각을 시각·청각·기하학적 변형으로 합성**하는 설계다.

AR에서 '손으로 만진다'의 진짜 난관은 추적 정확도가 아니라 **촉각의 부재**다. 실제 버튼은 손끝이 닿는 순간 반발력으로 접촉을 알려주지만 홀로그램은 그러지 못한다. 이 설계는 문제를 센서 성능으로 풀지 않고 '피드백 채널을 바꾼다'는 인터랙션 설계로 풀었다. 조경 현장에서 손으로 지형을 다듬거나 수목을 배치하는 인터페이스를 만들 때 그대로 적용되는 원칙이다.

근거리 전용이다(팔 길이 이내). 공중에 손을 들고 있으면 피로가 쌓인다(gorilla arm). 촉각 대체는 어디까지나 대체이므로 정밀 작업(밀리미터 단위 정렬)에는 부적합하다.

### 핸드 레이(Hand ray)와 Point-and-commit — 원거리 조작
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft Mixed Reality 디자인팀 |
| 연도 | 2019년 |
| 수치 | 근/원 전환 임계 약 50 cm. 광선 원점 = 손바닥 중심. 상태 2종(pointing: 점선+도넛 / commit: 실선+점). |
| 출처 | https://learn.microsoft.com/en-us/windows/mixed-reality/design/point-and-commit |

팔이 닿지 않는 곳의 홀로그램을 다루기 위해 HoloLens 2는 **손바닥 중심에서 광선을 쏜다**. 손가락으로 가리키는 방식이 아니라 손바닥에서 쏘는 이유는, 다섯 손가락을 집기·쥐기 같은 조작 제스처에 온전히 남겨두기 위해서다. 광선 끝에는 도넛 모양 커서가 붙어 교차 지점을 표시하고, 엄지-검지 에어탭으로 '확정(commit)'한다. 가리키는 상태에서는 점선 + 도넛 커서, 확정 상태에서는 실선 + 점 커서로 시각이 바뀐다. 근거리와 원거리의 전환은 자동이며 **약 50 cm**가 경계다. 결정적으로 근거리와 원거리가 **같은 손 제스처**를 쓴다 — 사용자는 하나의 심성 모형만 익히면 된다.

VR의 모션 컨트롤러가 쏘던 레이저 포인터를 맨손으로 옮겨온 것이다. 이로써 HoloLens 2는 '손 닿는 것은 직접 만지고, 먼 것은 광선으로 집는다'는 거리 연속체를 하나의 제스처 언어로 통합했다. 넓은 야외를 다루는 조경 AR에서는 대부분의 대상이 팔 밖에 있으므로 이쪽이 사실상 기본 모드가 된다.

손 떨림이 광선 끝에서 증폭된다 — 거리가 멀수록 각도 오차가 위치 오차로 확대되어 원거리 정밀 지시가 어렵다. 팔을 들어야 해서 장시간 사용 시 피로하다.

### HoloLens 2 시선 추적 (eye tracking, 1.5도 · 30 Hz)
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft |
| 연도 | 2019년 |
| 수치 | 정확도 시각 약 1.5도(설계 권장 여유 2.0~3.0도). 표본율 기본 약 30 FPS, 확장 API에서 30/60/90 fps 선택. 최소 표적 크기 권장 시각 2도 이상(팔을 뻗었을 때 엄지손톱 크기). 센서 = IR 카메라 2대. 시선 추적 실패 시 head-gaze로 되돌리는 타임아웃 권장값 500~1500 ms. |
| 출처 | https://learn.microsoft.com/en-us/windows/mixed-reality/design/eye-tracking · https://learn.microsoft.com/en-us/hololens/hololens2-hardware |

바이저 안쪽 **적외선 카메라 2대**가 눈에 비친 각막 반사와 동공 윤곽을 잡아 시선 광선(원점 + 방향) 하나를 만들어낸다. 기본 API는 약 **30 FPS(30 Hz)**로 이 광선을 내보내고, 확장 API(Extended Eye Tracking)는 좌/우 눈 각각의 시선 벡터를 30·60·90 fps 중 선택해 받을 수 있다. 사용자마다 눈의 광축과 시축이 다르므로 **개인별 보정(calibration)**이 필수다. Microsoft가 공식적으로 밝힌 정확도는 실제 표적으로부터 **시각(視角) 약 1.5도 이내**이며, 여유를 두고 2.0~3.0도로 설계하라고 권한다. 이 각도는 거리에 비례한 크기로 환산된다 — 2 m 거리에서 1.5도는 약 5 cm다.

시선 추적이 연구실 장비에서 **소비자용 착용 기기의 기본 센서**로 내려온 순간이다. 이전 세대(HoloLens 1)는 머리 방향(head-gaze)을 시선 대신 썼다. 머리는 몸 전체를 움직여야 했지만 눈은 그럴 필요가 없다. Microsoft 문서의 표현대로 '안구 근육은 인체에서 가장 빠르게 반응하는 근육'이므로, 시선은 사실상 지연 없는 포인팅 채널이 된다.

보정에 실패하는 사용자가 존재한다(특정 콘택트렌즈·안경, 눈 수술 이력, 눈 생리 차이). 외부 요인도 치명적이다 — 바이저 얼룩, **강한 직사광**, 머리카락 가림. 조명이 변하면 정확도가 떨어져 재보정이 필요할 수 있다. 야외 조경 현장은 직사광·급격한 조도 변화가 기본값이라는 점에서 구조적 약점이다. 눈 데이터는 생체정보이므로 앱마다 사용자 권한 승인이 필요하다.

### 미다스의 손 문제(Midas Touch problem) — 시선 입력의 원죄
| 항목 | 내용 |
| --- | --- |
| 주체 | Robert J. K. Jacob (Naval Research Laboratory, Human-Computer Interaction Lab) |
| 연도 | 1990년 CHI 학회 발표 / 1991년 4월 ACM TOIS 논문 게재 |
| 수치 | 논문: ACM Transactions on Information Systems, Vol. 9, No. 3, April 1991, pp. 152–169. 실사용 시선 정확도 2도(양호 시 1도, 24인치 거리에서 화면상 약 0.4인치). 중심와(fovea) 폭 약 1도. 고시(fixation) 지속 200~600 ms, 고시 중 미세 떨림 1도 미만. 고시 인식 알고리즘: 100 ms 동안 0.5도 이내 유지 시 고시 시작으로 판정 → 100 ms의 원천적 지연. 체류 선택(dwell) 시간은 150~250 ms를 사용. |
| 출처 | Jacob, R.J.K. (1991) "The Use of Eye Movements in Human-Computer Interaction Techniques: What You Look At is What You Get", ACM Transactions on Information Systems 9(3), 152–169. https://www.cs.tufts.edu/~jacob/papers/tois.pdf · 관련: Jacob, "Eye Tracking in Advanced Interface Design" https://www.cs.tufts.edu/~jacob/papers/barfield.pdf |

시선을 마우스처럼 쓰면 왜 안 되는가를 못 박은 논문이다. Jacob의 진단은 단순하다 — **눈은 끄지 못한다.** 눈꺼풀을 뜨는 순간부터 눈은 계속 무언가를 본다. 따라서 '본 것 = 선택한 것'으로 매핑하면, 사용자는 아무것도 그냥 볼 수 없게 된다. 손대는 것마다 금으로 변해 굶어 죽은 미다스 왕처럼, 보는 것마다 명령이 실행된다. Jacob은 이 문제를 **관찰(observation)과 제어(control)의 이중 역할**로 정식화했다 — 벽에 걸린 액자를 눈으로 수평 맞추려면 액자와 주변을 번갈아 봐야 하는데, 그 눈이 동시에 액자를 움직이는 입력이라면 작업 자체가 성립하지 않는다. 그의 실험 장비는 Applied Science Laboratories 3250R 아이트래커였고, 실사용 정확도는 통상 2도, 잘 되면 1도였다.

이 논문이 정한 문제 설정이 **35년간 시선 인터페이스 설계의 헌법**으로 남았다. HoloLens 2의 '시선 + 음성/제스처 조합', Vision Pro의 '보고 집기(look and pinch)'는 전부 미다스의 손 문제에 대한 답이다. 시선만으로 확정하지 않고 반드시 다른 채널로 '확정' 신호를 받는다는 원칙이 여기서 나왔다. 정의가 먼저 있었고, 하드웨어가 30년 늦게 따라온 사례다.

Jacob 자신이 밝혔듯 '의도한 응시'와 '그냥 본 것'은 **일반적으로 구분이 불가능하다**. 그는 특정 상황별 상호작용 기법으로 우회할 뿐이라고 썼다. 또한 빠른 선택에서는 사용자의 시선이 손의 클릭보다 먼저 다음 대상으로 떠나버리는 '클릭 전 이탈(leave before click)' 현상이 생겨, 느린 확정 채널과의 동기화가 별도 문제로 남는다.

### Gaze + Pinch — 시선이 고르고 손이 조작한다
| 항목 | 내용 |
| --- | --- |
| 주체 | Ken Pfeuffer, Benedikt Mayer, Diako Mardanbegi, Hans Gellersen (Lancaster University) |
| 연도 | 2017년 (ACM Symposium on Spatial User Interaction, SUI '17) |
| 수치 | SUI 2017 게재. 피인용 369회(Semantic Scholar, 2026년 기준). DOI 10.1145/3131277.3132180. |
| 출처 | Pfeuffer, K., Mayer, B., Mardanbegi, D., Gellersen, H. (2017) "Gaze + pinch interaction in virtual reality", Proc. ACM Symposium on Spatial User Interaction (SUI '17). DOI 10.1145/3131277.3132180 |

미다스의 손 문제에 대한 가장 널리 채택된 답을 학술적으로 정식화한 논문이다. 핵심 분업은 이렇다 — **눈은 '무엇을'을 정하고, 손은 '어떻게'를 정한다.** 시선은 빠르지만 부정확하고 끌 수 없다. 손은 정밀하지만 느리고 피로하다. 두 채널의 강점만 취해, 시선으로 대상을 지목한 뒤 손의 집기(pinch) 동작으로 확정하고 이어서 조작한다. 결정적인 이점은 손을 **들어 올릴 필요가 없다**는 것이다. 무릎 위에 손을 둔 채로도 시야 어디든 닿는다. 이 논문은 이후 상용 기기의 표준 상호작용이 된 패턴의 학술적 원본으로 인용된다(현재 피인용 약 369회).

그 이전의 지배적 대안은 **체류 시간(dwell time)**이었다 — 일정 시간 이상 응시하면 선택. 그러나 dwell은 '느려서 답답하거나, 빨라서 오발동하거나' 둘 중 하나로 귀결된다. Gaze+Pinch는 확정 신호를 아예 다른 신체 채널로 넘겨 이 교환관계 자체를 없앴다. 6년 뒤 Apple Vision Pro가 이 조합을 운영체제의 기본 입력으로 채택하면서, 학계 제안이 소비자 제품 표준이 된 드문 사례가 됐다.

논문 초록이 출판사 정책으로 공개 API에서 차단돼 있어, 이번 조사에서 원문 문장을 직접 확보하지 못했다(아래 uncertain 참조). 기법 자체의 한계로는, 시선 정확도가 낮은 영역에서 인접한 작은 대상들을 구분하지 못하는 문제와, 집기 동작 직전에 시선이 이미 다음 대상으로 이동하는 '클릭 전 이탈'이 남는다.

### Apple Vision Pro의 "Look and Pinch" — 눈과 손만으로 쓰는 OS
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple |
| 연도 | 2023년 6월 발표(WWDC23) / 2024년 2월 2일 미국 출시 / 2025년 10월 M5 탑재 모델 |
| 수치 | 총 화소 2,300만(양안 합계, Micro-OLED, 화소 피치 7.5 마이크로미터). 지원 주사율 90/96/100/120 Hz. 카메라·센서: 고해상도 메인 카메라 2대, 월드 트래킹 카메라 6대, **아이트래킹 카메라 4대**, TrueDepth 카메라, LiDAR 스캐너. 마이크 6개 어레이. R1 칩 **광자-대-광자 지연 12 ms**. M5 모델 무게 750~800 g, 일반 사용 최대 2.5시간. 시선 표적 최소 면적 **60 포인트**(요소 자체는 더 작아도 되며, 크기와 여백을 합쳐 60포인트를 확보). |
| 출처 | https://www.apple.com/apple-vision-pro/specs/ · Apple WWDC23 session 10073 "Design for spatial input" https://developer.apple.com/videos/play/wwdc2023/10073/ |

Vision Pro는 컨트롤러를 아예 주지 않는다. 입력은 **눈·손·목소리** 셋뿐이다. 사용자는 버튼을 바라보고 엄지와 검지를 맞부딪치면 선택된다 — 손을 들어 올릴 필요 없이 무릎 위에서 해도 된다. Apple의 표현으로 '손가락을 맞붙이는 것은 아이폰 화면을 누르는 것과 동등한 동작'이다. 눈 안쪽을 향한 **아이트래킹 카메라 4대**와 바깥쪽 **월드 트래킹 카메라 6대**가 이를 지탱하고, 별도 실리콘인 **R1 칩**이 센서 입력만 전담해 **광자-대-광자 지연 12 밀리초**를 만든다. 확대·회전 같은 양손 제스처도 지원하며, 결정적으로 확대의 **기준점이 그 순간 눈이 머문 지점**으로 정해진다 — 시선이 조작의 좌표계를 제공하는 것이다.

Gaze+Pinch를 실험실 기법이 아니라 **운영체제 전체의 기본 입력**으로 만든 첫 상용 제품이다. HoloLens 2에서 시선은 어디까지나 보조 신호였고(홀로그래픽 셸의 기본 입력이 아니었다), 손을 들어 광선을 쏘는 것이 주된 방식이었다. Vision Pro는 그 관계를 뒤집었다 — 시선이 커서이고 손은 클릭이다. 팔을 들지 않으므로 장시간 사용에서 피로가 극적으로 줄어든다.

Apple은 시선 정확도를 각도로 공개하지 않는다(60포인트라는 UI 규칙으로만 제시). 눈은 한 번에 하나의 거리에만 초점을 맞추므로, 깊이가 자주 바뀌는 UI는 눈의 피로를 부른다 — Apple 스스로 '상호작용 콘텐츠는 같은 깊이에 두라'고 권한다. 시야 가장자리를 보는 것은 중앙보다 불편하다. 직접 터치(손을 뻗어 만지기)는 공중에 손을 들어야 해서 곧 피로해진다.

### visionOS의 시선 프라이버시 모델과 27관절 손 골격
| 항목 | 내용 |
| --- | --- |
| 주체 | Apple |
| 연도 | 2023년 발표 / 2024년 출시 |
| 수치 | visionOS ARKit HandSkeleton.JointName: forearmArm·forearmWrist·wrist(3) + 엄지 4 + 검지/중지/약지/소지 각 5 = **27개 관절**(HoloLens/OpenXR의 26개와 달리 팔뚝 2개를 포함). 손 데이터 접근 조건: 몰입형 공간 필수 + 사용자 승인 + Info.plist 사용 목적 문자열. |
| 출처 | https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy · https://developer.apple.com/documentation/arkit/handskeleton/jointname |

Vision Pro의 설계에서 기술적으로 가장 특이한 점은, **앱이 사용자의 시선을 모른다**는 것이다. 시스템이 카메라·센서 입력을 직접 처리하고 앱에는 전달하지 않는다. 사용자가 어떤 버튼을 바라보면 그 버튼의 하이라이트(호버 효과)는 **앱 프로세스 바깥에서** 시스템이 그려준다. 앱이 사용자의 시선 위치를 알게 되는 것은 오직 사용자가 손가락을 집었을 때, 그 '탭' 좌표 하나뿐이다. 손 데이터도 마찬가지로 제한적이다 — 실제 손 관절 좌표(ARKit의 HandTrackingProvider)를 받으려면 몰입형 공간(immersive space)을 열어야 하고, Info.plist에 사용 목적을 명시한 뒤 사용자 승인을 받아야 한다. 승인된 경우 얻는 손 골격은 팔뚝 2 + 손목 1 + 엄지 4 + 나머지 네 손가락 각 5개 = **한 손 27개 관절**이다.

시선은 단순한 포인터가 아니라 **주의(attention)의 기록**이다. 어디를 얼마나 오래 보았는지는 광고 반응·인지 부하·질병 징후까지 드러낸다. Apple은 이 데이터를 앱에 주지 않으면서도 시선을 기본 입력으로 쓰는 구조를 OS 층위에서 설계했다. HoloLens 2가 '앱 권한 승인'으로 푼 문제를 Apple은 '아예 주지 않는다'로 푼 것이다. AR이 일상 기기가 될 때 무엇이 쟁점이 되는지를 보여주는 설계 결정이며, 조경 분야에서 이용자 시선 데이터로 경관 선호를 측정하려는 연구에는 곧바로 제약이 된다.

시선 데이터를 앱이 못 쓰므로, 시선 히트맵·주의 분석 같은 연구용 응용은 Vision Pro에서 원천적으로 불가능하다(HoloLens 2는 권한만 받으면 가능). 손 데이터를 쓰려면 몰입형 공간을 열어야 하는데, 그러면 시스템이 다른 앱을 숨긴다 — 여러 앱을 띄워놓고 쓰는 방식과 양립하지 않는다. 사용자가 손 데이터 접근을 거부할 수 있으므로 앱은 데이터 없는 경우를 반드시 처리해야 한다.

### 표면 근전도(sEMG) 손목밴드 — Meta의 신경운동 인터페이스
| 항목 | 내용 |
| --- | --- |
| 주체 | CTRL-labs at Reality Labs, Meta (David Sussillo, Patrick Kaifosh, Thomas Reardon 외 — 저자 331명) |
| 연도 | 2024년 2월 23일 bioRxiv 프리프린트 / 2025년 7월 23일 Nature 게재 / 2025년 9월 Meta Neural Band로 제품화 |
| 수치 | 하드웨어: 금도금 전극 48개 → 16 양극 채널, 표본율 2 kHz, 노이즈 2.46 µVrms, 손목밴드 4가지 크기, 블루투스 무선, 배터리 4시간 이상. 데이터셋: 필기 6,350명 / 이산 제스처 4,800명 / 손목 자세 389명, 폐루프 검증은 과제당 20~24명. 성능(Nature 게재본): 연속 탐색 **초당 0.66회 표적 획득**, 이산 제스처 **초당 0.88회 검출**, 필기 **분당 20.9 단어**. 개인화 시 필기 디코딩 **16% 향상**. 논문: Nature 645권 702–711쪽, 2025년 7월 23일, DOI 10.1038/s41586-025-09255-w, 피인용 84회. |
| 출처 | Nature 645, 702–711 (2025), DOI 10.1038/s41586-025-09255-w · 프리프린트: Sussillo, Kaifosh, Reardon, bioRxiv 2024.02.23.581779 https://www.biorxiv.org/content/10.1101/2024.02.23.581779v1.full |

카메라가 아니라 **근육이 내는 전기**를 읽는다. 뇌의 운동 명령이 척수를 거쳐 운동 뉴런에 도달하면, 각 운동 단위가 활동 전위(MUAP)를 내고 이것이 피부 표면까지 전파된다. 손목밴드에 둘린 **금도금 전극 48개**가 이를 **16개의 양극(bipolar) 채널**로, **초당 2,000회(2 kHz)** 표본화한다. 카메라 기반 손 추적과 결정적으로 다른 점은 두 가지다. 첫째, **가려짐이 없다** — 주머니 속이든 책상 밑이든 근육 신호는 읽힌다. 둘째, **움직임이 실제로 일어나기 전에** 신호가 나온다. Meta는 수천 명 규모의 데이터로 신경망 디코더를 학습시켜, **개인별 보정 없이 처음 착용한 사람에게도 바로 작동하는** 범용 모델을 만들었다. 이것이 논문의 핵심 주장이다.

기존 근전도 인터페이스는 예외 없이 **사용자마다 보정**이 필요했다 — 팔 굵기, 지방층 두께, 전극 위치가 조금만 달라져도 신호가 달라지기 때문이다. 그래서 의수 제어 같은 특수 용도를 벗어나지 못했다. Meta는 이를 '데이터 규모' 문제로 재정의했다. 필기 과제 6,350명, 이산 제스처 4,800명, 손목 자세 389명의 데이터로 학습하자, 한 명의 데이터로 학습한 모델이 다른 사람에게서 77~83% 오류를 내던 것이 범용 모델에서는 처음 보는 사람에게도 90% 이상 분류 정확도로 바뀌었다. **개인화는 선택 사항으로 강등됐다.** 이는 손 추적이 '보이는 손'에서 '의도 자체'로 옮겨간 도약이다.

분당 20.9 단어는 숙련된 스마트폰 타이핑(분당 35~40 단어 수준)에 못 미친다. 손목 자세 분류 정확도는 제스처·필기(90% 이상)보다 낮은 75% 이상에 머문다. 손목밴드는 손의 **절대 위치**를 모른다 — 공간상 어디에 있는지는 다른 센서가 알려줘야 한다. 프리프린트(2024)와 Nature 게재본(2025)의 수치가 다르다(필기 17.0 → 20.9 wpm, 개인화 이득 8.35% → 16%). 책에 쓸 때는 **Nature 게재본 수치**를 쓰고 프리프린트와 구분해야 한다.

### 음성 입력과 "See it, Say it" — 시선이 대명사를 대신한다
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft |
| 연도 | 2016년(HoloLens 1세대) / 2019년 HoloLens 2에서 시선 결합으로 확장 |
| 수치 | 마이크 5채널 어레이. 음성 인식 스트림 16 kHz / 24 bit 모노, 주변음 스트림 48 kHz / 24 bit 스테레오. 시스템 예약어 3개("Hey Cortana", "Select", "Go to start"). 권장 설계: 명령어는 2음절 이상, 파괴적이지 않고 되돌릴 수 있을 것. |
| 출처 | https://learn.microsoft.com/en-us/windows/mixed-reality/design/voice-input |

AR에서 음성의 진짜 값어치는 '명령을 말하는 것'이 아니라 **중첩된 메뉴를 한 번에 관통하는 것**이다. Microsoft의 설계 원칙은 '보이면 말할 수 있다(see it, say it)' — 버튼에 적힌 이름이 곧 음성 명령이므로 사용자가 명령어를 외울 필요가 없다. HoloLens 2에서 결정적 진화는 **시선과의 결합**이다. 사용자가 홀로그램을 바라보며 "이걸 놓아줘(put this)"라고 말한 뒤, 놓을 자리를 바라보며 "저기에(over here)"라고 말하면 된다. 즉 **시선이 '이것'과 '저것'이라는 지시대명사의 지시 대상을 제공한다.** 하드웨어는 5채널 마이크 어레이이고, 음성 인식용 스트림은 16 kHz 24비트 모노로, 주변음 녹음용 스트림은 48 kHz 24비트 스테레오로 분리 처리된다. 이 오디오 처리는 전부 하드웨어 가속되어 CPU 전력을 쓰지 않는다.

1980년 MIT의 Richard Bolt가 제시한 "Put-that-there"의 개념이 40년 만에 착용형 기기에서 실현된 것이다(음성 + 지시). 차이는 지시 채널이 손가락에서 **시선**으로 바뀐 점이다. 손을 쓸 수 없는 작업 상황 — 조경 시공 현장에서 도구를 들고 있는 상태 — 에서 유일하게 남는 입력 채널이라는 점이 실무적 의미다.

연속량의 미세 조정에 약하다 — "조금 더 크게"의 '조금'을 정량화할 수 없다. 사회적 수용성 문제가 크다(도서관, 공유 사무실, 공공장소에서 혼잣말하는 모습). 고유명사·은어·약어는 인식이 어렵다. 소음 환경에서 취약하다. Microsoft 문서는 HoloLens의 음성 인식이 **미국 영어 원어민에 맞춰 최적화**돼 있다고 명시한다 — 한국어 현장 적용의 직접적 제약이다.

### 공간 앵커(Spatial Anchor)와 공유 좌표계
| 항목 | 내용 |
| --- | --- |
| 주체 | Google(ARCore Cloud Anchors) · Meta(Shared Spatial Anchors) · Microsoft(Azure Spatial Anchors, 서비스 종료) |
| 연도 | ARCore Cloud Anchors 2018년 / Azure Spatial Anchors 2019년(2024년 서비스 종료) / Meta Shared Spatial Anchors 2023년, 그룹 공유 방식은 v71(2024년) |
| 수치 | ARCore: 동시 진행 가능한 Cloud Anchor 작업 **최대 40개**. API 키 인증 시 앵커 수명 **최대 24시간**, 그 이상은 키리스(keyless) 인증 필요. 할당량: 호스트 요청 분당 30회, 리졸브 요청 분당 300회(IP·프로젝트당). 특징점 지도 품질 3등급(INSUFFICIENT / SUFFICIENT / GOOD). Meta SSA: 현재 **단일 실내 공간의 로컬 멀티플레이**만 지원. |
| 출처 | https://developers.google.com/ar/develop/cloud-anchors · https://developers.google.com/ar/develop/java/cloud-anchors/developer-guide-android · https://developers.meta.com/horizon/documentation/unity/unity-shared-spatial-anchors/ |

여러 사람이 같은 자리에서 **같은 가상 물체를 같은 곳에서 보게** 하려면 공통 좌표 원점이 필요하다. 공간 앵커가 그 역할을 한다. ARCore Cloud Anchors의 원리는 이렇다 — 기기가 앵커 주변 공간을 여러 각도에서 촬영해 **3차원 특징점 지도(feature map)**를 만들어 서버에 올린다(host). 다른 기기가 같은 장소에서 카메라를 들면, 서버는 그 화면의 시각 특징을 저장된 지도와 대조해 기기의 위치와 방향을 역산한다(resolve). 지도 품질은 INSUFFICIENT / SUFFICIENT / GOOD 세 등급으로 실시간 피드백된다. Meta Quest의 Shared Spatial Anchors는 임의의 그룹 UUID로 앵커를 공유하며, 공유받은 기기에서는 로컬 앵커처럼 동작한다.

단독 사용자의 AR에서 **협업 AR**로 넘어가는 전제 조건이다. 1997년 Feiner의 투어링 머신이 혼자 쓰는 야외 AR이었다면, 공간 앵커는 여러 사람이 같은 가상 설계안을 같은 자리에서 함께 보며 논의하는 것을 가능하게 한다. 조경 설계 검토회나 현장 시공 협의처럼 **여러 사람이 한 장소에 모여 같은 안을 본다**는 상황이 조경 실무의 기본값이라는 점에서 핵심 기술이다.

특징점 지도는 **환경이 변하면 무효가 된다** — 계절에 따라 잎이 지고, 꽃이 피고, 눈이 쌓이는 조경 공간에서는 지도 수명이 짧다. 기기를 제자리에서 회전시키는 것으로는 부족하고 **실제로 걸어 이동**하며 여러 시점에서 촬영해야 한다. 특징이 부족한 면(균질한 잔디, 콘크리트 포장, 수면)에서는 지도 품질이 확보되지 않는다. Azure Spatial Anchors는 2024년 11월 서비스가 종료되어, Microsoft 계열 해법은 현재 공백 상태다(종료 시점은 아래 uncertain 참조).

### ARCore Geospatial API와 VPS — 야외에 좌표를 심는 법
| 항목 | 내용 |
| --- | --- |
| 주체 | Google (ARCore / Google Maps Street View) |
| 연도 | 2022년 5월 발표(Google I/O) / 2023년 Streetscape Geometry·Rooftop 앵커 확장 |
| 수치 | 정확도는 상수가 아니라 **실시간 추정치**로 제공된다: getHorizontalAccuracy(수평, 미터), getVerticalAccuracy(수직, 미터), getOrientationYawAccuracy(방위각, 도). 셋 다 **68번째 백분위 신뢰 수준의 반경**으로 정의된다 — 즉 참값이 그 반경 안에 있을 확률이 68%다. 스트리트뷰 커버리지는 '거의 모든 국가'. 앵커 3종(WGS84 / Terrain / Rooftop). |
| 출처 | https://developers.google.com/ar/develop/geospatial · https://developers.google.com/ar/reference/java/com/google/ar/core/GeospatialPose |

실내는 벽에 마커를 붙이면 되지만 **야외에는 붙일 벽이 없다.** Google의 해법은 지구 전체를 마커로 쓰는 것이다. VPS(Visual Positioning System)는 15년 넘게 축적한 스트리트뷰 수십억 장에서 뽑아낸 **전 지구 3차원 점군(point cloud)**과 기기 카메라 화면의 특징을 대조해 위치를 정한다. GPS만으로는 도시 협곡에서 수 미터~수십 미터가 틀리지만, VPS는 건물 모서리·간판·가로 구조 같은 영속적 지형지물을 직접 맞춰 훨씬 정밀한 위치와 **방위각**을 준다. 앵커는 세 종류다 — WGS84 앵커(위경도 + 타원체 기준 고도), **지형(Terrain) 앵커**(지면 기준 높이), 지붕(Rooftop) 앵커(건물 옥상 기준). 조경에서 결정적인 것은 지형 앵커다. 지반고를 몰라도 '이 지점의 땅 위 1.5 m'라고 지정할 수 있기 때문이다.

1990년대 이래 야외 AR의 병목은 한결같이 **정합(registration)**이었다 — 1997년 Feiner의 투어링 머신은 GPS와 자력계에 의존해 수 미터의 오차를 감수했다. VPS는 그 문제를 '기기의 센서를 좋게 만든다'가 아니라 '세계 전체를 미리 스캔해 둔다'로 뒤집었다. 야외 조경 AR — 아직 심지 않은 수목을 대지 위에 세워 보는 일 — 이 특수 장비 없이 스마트폰만으로 가능해진 전환점이다.

Google은 **고정된 정확도 수치를 공표하지 않는다** — 장소·시간대·날씨·촬영 각도에 따라 달라지기 때문이다. 앱이 매 프레임 정확도 값을 읽어 임계값과 비교하는 구조로 짜야 한다. 스트리트뷰가 들어가지 못한 곳(공원 내부 보행로, 산지, 신규 조성지)은 VPS가 작동하지 않는다. 식생은 계절·생장에 따라 외형이 크게 바뀌므로 특징 대조가 어긋날 수 있다. 조경 대상지의 상당수가 정확히 이 사각지대에 있다는 점이 실무적 제약이다.

#### 검증에서 잡힌 정정
- [Meta sEMG] '손목 자세 389명' → 틀림. Nature 게재본 Methods는 '162 participants, 96 of whom recorded 2 sessions'. 389는 bioRxiv 프리프린트 Methods의 'The wrist pose training corpus included sEMG recordings from 389 participants' 값이며, Nature 게재본 전문에 '389'라는 문자열은 단 한 번도 등장하지 않는다.
- [Meta sEMG] '이산 제스처 4,800명' → 틀림. Nature 게재본은 'The discrete-gesture training corpus was composed of data from 4,900 participants'. 4,800은 프리프린트 값.
- [Meta sEMG] '필기 6,350명' → 틀림. 정답 6,627명. Nature 게재본·프리프린트 Methods 모두 'a total of 6,627 participants'로 동일하다. 6,350은 프리프린트 본문의 요약 범위 '200-6350 participants, depending on task' 상한을 잘못 옮긴 것으로, 그 프리프린트조차 자기 Methods(6,627)와 어긋난다. Nature 게재본의 대응 문장은 '162–6,627 participants, depending on the task'.
- [Meta sEMG] '폐루프 검증은 과제당 20~24명' → Nature 게재본 기준 틀림. 원문은 'n = 17 (wrist), n = 24 (discrete gestures) and n = 20 (handwriting)'로 하한이 17명이다. 20~24는 프리프린트 값(wrist pose와 handwriting이 N=20, discrete gestures가 N=24).
- [Meta sEMG] '저자 331명' → 근거 없음. Nature 게재본 저자 표기는 'Patrick Kaifosh, Thomas R. Reardon & CTRL-labs at Reality Labs'이고, PMC12443603의 컨소시엄 명단을 직접 세면 Kaifosh·Reardon 포함 245명이다(Semantic Scholar의 자체 파싱은 350명). 331이라는 수는 어느 판본·어느 색인에서도 나오지 않는다.
- [Meta sEMG] 저자 표기 'David Sussillo, Patrick Kaifosh, Thomas Reardon 외' → Nature 게재본 기준으로는 부정확. Sussillo는 게재본 저자 줄에 없고 CTRL-labs 컨소시엄 명단 내부(알파벳순 208번째)에 있다. Sussillo가 저자 줄에 오르는 것은 bioRxiv 프리프린트('Ctrl-labs at Reality Labs, D. Sussillo, P. Kaifosh, T. Reardon')뿐이다.
- [Meta sEMG] 'bioRxiv 프리프린트 2024년 2월 23일' → 게시일은 2024년 2월 28일(bioRxiv API details: v1 2024-02-28, v2 2024-07-23). 2024.02.23은 DOI에 박힌 접수 스탬프이지 게시일이 아니다.
- [Jacob 1991] 'ACM Transactions on Information Systems, Vol. 9, No. 3' → 정본 서지는 Vol. 9, Issue 2. Crossref(10.1145/123078.128728) 및 ACM DL 모두 'Volume 9, Issue 2, April 1991, pp. 152-169'. 다만 PDF 인쇄 푸터 자체가 'Vol. 9, No. 3, April 1991, Pages 152-169'로 잘못 찍혀 있어, 이 오류는 원 저널 인쇄 오류를 그대로 따라간 것이다. 인용 시에는 9(2)를 써야 색인과 맞는다.
- [Apple Vision Pro] '지원 주사율 90/96/100/120 Hz'를 2024년 출시 모델까지 포괄해 서술 → 120 Hz는 2025년 10월 M5 모델부터다. 2024년 M2 초판 스펙은 90/96/100 Hz뿐이었다. 현재 apple.com 스펙 페이지가 M5 기준이라 120 Hz가 보이는 것이므로, 모델 구분 없이 쓰면 초판 사양을 잘못 전달한다.
- [Apple Vision Pro] 'R1 칩 광자-대-광자 지연 12 ms' → 12 ms 자체는 맞으나 'photon-to-photon(광자-대-광자)'은 Apple 용어가 아니다. Apple 뉴스룸 원문은 'R1 streams new images to the displays within 12 milliseconds — 8x faster than the blink of an eye'로, 센서 입력부터 디스플레이 출력까지의 전체 광자-대-광자 지연이 아니라 디스플레이로의 이미지 스트리밍 지연을 가리킨다.
- [확인 불가] Azure Spatial Anchors '2024년 서비스 종료' → 서비스 폐지로 MS Learn 문서가 Azure 허브로 리다이렉트되고 azure.microsoft.com/updates 검색도 0건이라 은퇴 공지 원문을 확보하지 못했다. 이 환경에서 web.archive.org는 차단됨. 참/거짓 판정 불가.
- [확인 불가] 발표·출시 연월 전반(HoloLens 2 2019-02 MWC/2019-11 출시, Vision Pro 2023-06/2024-02-02/2025-10 M5, ARCore Cloud Anchors 2018, Geospatial API 2022-05 I/O 및 2023 Streetscape·Rooftop 확장, Meta SSA 2023 도입, Meta Neural Band 2025-09 제품화) → 웹 검색 예산(200/200)이 소진되어 1차 출처 페이지로 개별 대조하지 못했다. 다만 Meta SSA 문서가 그룹 공유를 'Supported in v71 and later'로 명시한 점, Apple 스펙 페이지가 M5 사양을 반영 중인 점은 해당 서술과 모순되지 않는다.
- [치명] Meta sEMG 데이터셋 — 필기 참가자 '6,350명'은 틀림. Nature 게재본 원문: "The handwriting recognition corpus comprised sEMG recordings from a total of 6,627 participants" → 정정: 6,627명 (출처 PMC12443603)
- [치명] Meta sEMG 데이터셋 — 이산 제스처 '4,800명'은 틀림. 원문: "The discrete-gesture training corpus was composed of data from 4,900 participants" → 정정: 4,900명
- [치명] Meta sEMG 데이터셋 — 손목 자세 '389명'은 틀림(2배 이상 과다). 원문: "The wrist decoder training corpus included ... from 162 participants" → 정정: 162명
- [오류] Meta sEMG 폐루프 검증 '과제당 20~24명'은 불완전. 실제: 손목 17명 / 이산 제스처 24명 / 필기 20명 → 하한은 17명이지 20명이 아님
- [오류] Nature 논문 '저자 331명'은 근거 없음. Crossref 저자 배열은 246개 항목(연구단 표기 'CTRL-labs at Reality Labs' 포함, David Sussillo 포함) → 정정: 약 246명
- [오류] bioRxiv 프리프린트 게시일 '2024년 2월 23일'은 DOI 스탬프(2024.02.23)일 뿐 게시일이 아님. bioRxiv API: v1 게시 2024-02-28, v2 게시 2024-07-23 → 정정: 2024년 2월 28일
- [표기] Nature 게재본 제목은 'A generic non-invasive neuromotor interface for human-computer interaction'(하이픈). 'noninvasive'는 bioRxiv 프리프린트 제목 표기
- [선후관계] '핸드 레이와 Point-and-commit (2019년, Microsoft Mixed Reality 디자인팀)' — 2019년은 손에 이식된 해이지 창안 연도가 아님. MS 공식 문서 원문: "The concept of point and commit for far interaction was created and defined for the Mixed Reality Portal (MRP). In this scenario, a user wears an immersive headset and interacts with 3D objects via motion controllers. ... We apply the interaction model of rays and attached them to both hands." → 원조는 2017년 Windows Mixed Reality 모션 컨트롤러 레이
- [선후관계/사양혼동] '음성 입력과 See it, Say it (2016년 HoloLens 1세대)' 항목의 '마이크 5채널 어레이'는 HoloLens 2 사양. HoloLens (1st gen) 공식 사양: 마이크 4개(4 microphones), 무게 579 g, HPU 1.0 → 2016년 항목에 2019년 하드웨어 수치를 붙임
- [선후관계/세대혼동] Apple Vision Pro '지원 주사율 90/96/100/120 Hz'와 '무게 750~800 g'은 2025년 10월 M5 모델 값. 2024년 2월 출시 초대 모델은 90/96/100 Hz, 600~650 g(배터리 353 g 제외) → 2023 발표·2024 출시와 M5 사양을 한 줄에 병기해 세대 구분이 무너짐
- [선후관계] ARCore Geospatial '2022년 5월 발표' 항목의 getOrientationYawAccuracy는 2022년 5월에 존재하지 않았음. ARCore 1.31.0(2022-05-11) 출시 시점에는 getHeadingAccuracy였고, ARCore v1.35.0(2022-12-08) 릴리스노트: "All Geospatial poses now expose their orientation accuracy of the Yaw rotation, replacing heading accuracy" → 야우 정확도는 2022년 12월부터
- [선후관계] '앵커 3종(WGS84/Terrain/Rooftop)'을 2022년 발표 시점 기능처럼 묶은 것은 부정확. ARCore GitHub 릴리스: WGS84 = 1.31.0(2022-05-11), Terrain anchor = 1.33.0(2022-08-18, 'ARCore Geospatial Terrain anchor API - new'), Rooftop anchor + Streetscape Geometry = 1.37.0(2023-05-10) → 3단계 확장
- [인용 메타데이터 불일치] Jacob 1991의 'Vol. 9, No. 3'은 인쇄본 러닝푸터('ACM Transactions on Information Systems, Vol. 9, No 3, April 1991, Pages 152-169')와는 일치하나, ACM DL/Crossref/OpenAlex 메타데이터는 Volume 9, **Issue 2**, April 1991로 색인함(DOI 10.1145/123078.128728). 또 ACM 색인 제목은 부제 없는 'The use of eye movements in human-computer interaction techniques'임. 연구 결과의 오류라기보다 ACM 자체 메타데이터 충돌이므로 인용 시 양쪽 표기를 병기할 것
- [확인불가] Azure Spatial Anchors '2019년 발표 / 2024년 서비스 종료' — 이번 세션에서 1차 출처 도달 실패(웹검색 예산 소진). learn.microsoft.com/en-us/azure/spatial-anchors 경로가 Azure 문서 허브로 리다이렉트되어 전용 페이지가 사라진 점만 확인(종료와 정합). 통상 인용되는 2024년 11월 20일 종료일은 미검증
- [확인불가] Meta Shared Spatial Anchors '2023년' 최초 도입 — Meta 공식 문서는 도입 연도를 명시하지 않음. 확인된 것은 'v71 이후 사용자 기반이 아닌 그룹 기반 공유'와 'Currently, SSA supports local multiplayer games in a single room'뿐
- [확인불가] Meta Neural Band '2025년 9월 제품화' — Meta 공식 발표문(about.fb.com / meta.com) 도달 실패로 미검증
- [sEMG 데이터셋 — 필기] 틀림: '필기 6,350명' → 올바른 값 6,627명. Nature 논문 Methods의 'Handwriting corpus' 절 원문: 'The handwriting recognition corpus comprised sEMG recordings from a total of 6,627 participants.' (PMC12443603 전문 확인)
- [sEMG 데이터셋 — 이산 제스처] 틀림: '이산 제스처 4,800명' → 올바른 값 4,900명. 원문: 'The discrete-gesture training corpus was composed of data from 4,900 participants.' 참고로 4,800이라는 숫자는 논문에 등장하긴 하나 코퍼스 크기가 아니라 일반화 성능 절편 실험의 학습 그룹 구간(40, 80, 160, 320, 640, 1,280, 2,800, 4,800명) 중 마지막 값이다 — 절편 실험 구간을 코퍼스 규모로 오인한 것으로 보인다.
- (외 12건)

\newpage

# 증강현실 전사와 분야별 전개

## prehistory
항목 14개 · 검증 정정 지적 39건

> 증강현실의 뿌리는 컴퓨터가 아니라 유리와 렌즈에 있다. 1806년 월러스턴의 카메라 루시다(英 특허 2993호)는 프리즘으로 바깥 풍경과 스케치북 위를 한 눈에 겹쳐 보게 했고, 1838년 휘트스톤의 입체경은 양안시차만으로 깊이가 생김을 증명했다. 1862년 12월 런던 왕립 폴리테크닉에서 공개된 '페퍼의 유령'은 45도 판유리를 광학 결합기로 써서 실제 배우 옆에 다른 상을 세웠다 — AR 하드웨어의 원형이다. 산업화는 군사에서 일어났다. 1900년 하워드 그럽의 반사 조준경 특허(제12108호)는 무한대 허상으로 시차를 없애 '머리를 움직여도 표식이 대상에 붙어 있게' 만들었고, 1918년 Oigee 조준경이 알바트로스 D.Va에 실려 실전에 들어갔다. 1941년 페란티 자이로 조준경은 겹친 상을 속도·선회율로 '계산'하기 시작했고, 1942년 10월 영국 TRE는 레이더 화면과 GGS Mk.II를 앞유리에 합쳐 HUD의 직계 조상을 만들었으며, 1958년 4월 30일 초도비행한 블랙번 버캐니어가 이를 실용화했다(엘리엇, 375대, 25년 운용). 같은 시기 민간에서는 하일리그가 1955년 「미래의 영화」로 다감각 이론을 세우고, 1957년 출원·1960년 10월 4일 등록된 US 2,955,156으로 개인용 HMD의 형태(140도 시야, 이어폰, 송풍 노즐)를 확정했다. 그러나 1962년 센소라마는 자금을 얻지 못해 소멸했다. 1961년 필코의 헤드사이트는 자기식 헤드트래킹으로 원격 카메라를 돌려 '추적'을 더했다. 1968년 서덜랜드에게 남은 과제는 무엇을 겹칠지 실시간으로 계산하는 일뿐이었다.


### 카메라 루시다 (Camera Lucida)
| 항목 | 내용 |
| --- | --- |
| 주체 | William Hyde Wollaston (영국 화학자) |
| 연도 | 1806 (특허), 1611 케플러 『Dioptrice』에 광학 원리 기술 |
| 수치 | 영국 특허 제2993호, 특허명 'An Instrument Whereby Any Person May Draw in Perspective'. 단순형은 45도 반투명 거울, 월러스턴형은 4면 프리즘의 2회 전반사 |
| 출처 | Wikipedia 'Camera lucida' (https://en.wikipedia.org/wiki/Camera_lucida) — 특허번호·케플러 1611·탤벗 1833 확인 |

눈앞에 작은 프리즘(또는 45도 반투과 거울)을 두어, 화가가 종이를 내려다보는 동시에 바깥 풍경이 그 종이 위에 겹쳐 보이게 하는 휴대용 광학기구다. 월러스턴의 프리즘형은 두 번의 전반사를 이용해 상이 뒤집히거나 좌우가 바뀌지 않게 했고 빛 손실도 적었다. 케플러가 1611년 『Dioptrice』에서 200년 앞서 원리를 기술했으나 실물을 만든 증거는 없다. AR의 관점에서 이것은 '가상의 상을 실제 작업면에 정합시켜 겹치는 광학 결합(optical combining)'의 최초 실용 도구이며, 무엇보다 결과물이 관람용이 아니라 '작업(그리기)'을 돕는 도구였다는 점에서 후대의 작업지원형 AR과 직결된다.

19세기 초 측량·탐험·박물학은 정확한 원근 기록을 대량으로 요구했는데, 사진은 아직 없었고 자유 스케치는 원근이 틀렸다. 문제는 '보는 것'이 아니라 '보는 것과 그리는 손을 같은 좌표계에 올리는 것'이었고, 그 정합 문제가 곧 AR의 정합(registration) 문제다.

성공했으나 사진술 보급 후 쇠퇴. 다만 현미경 도해 도구로 1980년대까지 표준 기구로 살아남았다. 1833년 폭스 탤벗이 이 기구에 실망한 것이 사진술 발명의 직접 동기가 되었다 — 즉 AR 계열 도구의 실패가 기록매체 혁신을 낳았다.

### 휘트스톤 입체경 (Stereoscope)
| 항목 | 내용 |
| --- | --- |
| 주체 | Sir Charles Wheatstone; 개량 David Brewster |
| 연도 | 1838 (휘트스톤), 1849 브루스터 렌즈식 개량, 1939 View-Master 대중화 |
| 수치 | 1838년 발표, 1849년 브루스터 렌티큘러형, 1939년 View-Master 출시 |
| 출처 | Wikipedia 'Virtual reality' (https://en.wikipedia.org/wiki/Virtual_reality), VRS 'History of VR' (https://www.vrs.org.uk/virtual-reality/history.html) |

좌우 눈에 시차(disparity)가 있는 두 장의 그림을 각각 보여주면 뇌가 이를 하나의 입체로 합성한다는 것을 장치로 증명했다. 이것은 '깊이는 세계에 있는 것이 아니라 두 눈에 주는 두 장의 이미지로 만들어낼 수 있다'는 명제이며, 이후 모든 HMD의 전제가 된다. 브루스터가 렌즈식으로 소형화하면서 빅토리아 시대의 대중 오락기구가 되었고, 1939년 View-Master로 산업화되었다. AR 측면에서는 결합(combining)이 아니라 '입체 생성'이라는 별개의 요소를 미리 확보한 것이다.

1830년대 생리광학은 단안 원근 단서만으로 깊이를 설명하려 했고, 양안시차의 역할을 두고 논쟁 중이었다. 휘트스톤은 논쟁을 이기기 위해 장치를 만들었다 — 기술이 아니라 학술 논쟁이 장치를 낳았다.

성공. 다만 입체경 계열은 '겹침'이 없는 순수 몰입 장치였고, 이 분기(입체 몰입 vs 광학 결합)는 이후 VR과 AR의 갈림길로 그대로 이어진다.

### 페퍼의 유령 (Pepper's Ghost)
| 항목 | 내용 |
| --- | --- |
| 주체 | Henry Dircks (원안, 공학자), John Henry Pepper (왕립 폴리테크닉 연구소 관장·무대화) |
| 연도 | 1858 디륵스 착안·모형, 1862년 12월 공개 실용화, 1863년 2월 임시특허·10월 확정 |
| 수치 | 공개: 1862년 12월, 런던 Royal Polytechnic Institution. 판유리 경사각 통상 45도. 공연작: 찰스 디킨스 『The Haunted Man and the Ghost's Bargain』의 한 장면. 1863년 내내 흥행하여 더 큰 극장으로 이전. 디즈니 유령의 저택: 길이 90피트 장면, 높이 30피트 판유리 |
| 출처 | Wikipedia "Pepper's ghost" (https://en.wikipedia.org/wiki/Pepper%27s_ghost) — 디륵스 1858, 1862년 12월 공개, 1863년 특허, 디킨스 작품, 디즈니·Musion·2012 코첼라 확인 |

객석과 무대 사이에 거대한 판유리를 45도로 세우고, 객석 아래 감춰진 '블루 룸'을 조명해 그 상을 유리에 반사시키면, 관객에게는 실제 배우 옆에 반투명한 인물이 서 있는 것으로 보인다. 조명 밝기를 조절하면 유령이 나타나고 사라진다. 유리 모서리는 바닥 문양에 숨긴다. 핵심은 이것이 '스크린 위의 영상'이 아니라 '실제 3차원 공간에 겹쳐진 상'이라는 점이며, AR이 말하는 광학 시스루 결합기(optical see-through combiner)와 원리가 동일하다. 오늘날 시스루 HMD의 half-silvered mirror는 이 무대 장치의 축소판이다.

19세기 중반 흥행 산업은 팬텀마고리아(환등 유령쇼)로 이미 포화 상태였고, 관객은 '스크린에 비친 것'이 아니라 '무대 위에 실재하는 것'을 요구했다. 즉 문제는 밝기나 해상도가 아니라 '실제 공간과 같은 깊이에 상을 놓는 것'이었다 — AR이 푸는 문제와 동일하다.

대성공. 다만 디륵스는 자신의 원안이 페퍼의 이름으로 알려진 데 불만을 품었고, 공동특허에도 불구하고 명칭은 페퍼에게 귀속되었다. 기술은 소멸하지 않고 160년간 살아남아 디즈니 유령의 저택, Musion Eyeliner(45도 금속화 필름 + LED/프로젝터), 2012년 코첼라 Dr. Dre·Snoop Dogg 공연의 투팍 '홀로그램'으로 재사용되었다. 언론이 이를 홀로그램이라 부른 것은 오보이며, 실제로는 1862년 원리 그대로다.

### 반사 조준경 (Reflector sight) — 그럽 특허에서 항공 실전까지
| 항목 | 내용 |
| --- | --- |
| 주체 | Howard Grubb (아일랜드 광학설계자); 항공 실용화: Optische Anstalt Oigee, 베를린 |
| 연도 | 1900 (그럽 특허), 1918 (항공 실전 투입), 1930년대 (각국 공군 전면 채택) |
| 수치 | 영국 특허 제12108호(1900), 명칭 'Gun Sight for large and small Ordnance'. 1918년 Oigee Reflector Sight — 탑재 기종 Albatros D.Va, Fokker Dr.I. 1943년 영국 Mark III Free Gun Reflector Sight 양산. 독일 Revi C12/A(1937년 설계), 일본 98식 조준기, 독일 Flakvisier 40 |
| 출처 | Wikipedia 'Reflector sight' (https://en.wikipedia.org/wiki/Reflector_sight) — 그럽 1900 특허 12108, Oigee 1918, 탑재 기종, Mark III 1943 확인 |

광원으로 비춘 조준 표식(레티클)을 콜리메이터 렌즈로 평행광으로 만들어 반투명 유리에 반사시키면, 사수는 바깥 표적과 무한대에 맺힌 표식을 동시에 본다. 무한대 허상이므로 눈 위치가 흔들려도 표식과 장비의 정렬이 유지된다 — 즉 시차(parallax)가 제거된다. AR 용어로 말하면 이것이 '정합(registration)이 눈 위치에 불변인 오버레이'의 최초 구현이다. 발표(1900)와 실전 투입(1918) 사이에 18년이 걸렸고, 그 지연의 이유는 원리가 아니라 항공기라는 수요처가 아직 없었기 때문이다.

1차대전 공중전에서 조종사는 기체를 조종하면서 전방을 보고 동시에 기계식 가늠쇠 두 개를 정렬해야 했다. 눈을 조준기로 내리는 순간 표적과 자세를 놓친다. 문제는 '조준 정확도'가 아니라 '시선을 전방에서 떼지 않는 것'이었다 — 이것이 이후 head-up이라는 단어 자체의 기원이며, AR을 군용으로 밀어붙인 최초의 고유 문제다.

성공. 1930년대 이후 모든 주요 공군의 표준이 되었고, 지상 대공포·자유선회 기관총까지 확산되었다. 오늘날 소총용 도트사이트로 여전히 대량 생산된다. 이 계보가 직접 HUD로 이어진다.

### L. Frank Baum 『The Master Key』 — '캐릭터 마커' 안경
| 항목 | 내용 |
| --- | --- |
| 주체 | L. Frank Baum (『오즈의 마법사』 저자) |
| 연도 | 1901 |
| 수치 | 등장 도구 3종 중 하나. 표시 문자 6종: G(good), E(evil), W(wise), F(foolish), K(kind), C(cruel) |
| 출처 | L. Frank Baum, 『The Master Key: An Electrical Fairy Tale』(1901) 원문 — Project Gutenberg eBook #436 (https://www.gutenberg.org/cache/epub/436/pg436-images.html)에서 인용문 직접 확인; Wikipedia 'Augmented reality' 역사절도 이 작품을 AR 선구로 명시 |

소년이 전기의 악마에게서 받는 세 가지 선물 중 하나가 '캐릭터 마커'라는 안경이다. 원문은 이렇게 말한다: "While you wear them every one you meet will be marked upon the forehead with a letter indicating his or her character. The good will bear the letter 'G,' the evil the letter 'E.' The wise will be marked with a 'W' and the foolish with an 'F.' The kind will show a 'K' upon their foreheads and the cruel a letter 'C.'" 즉 착용자가 만나는 모든 사람의 이마에 그 사람의 속성을 나타내는 문자가 겹쳐 보인다. 이것은 광학 결합도, 입체도 아니고 '실세계의 객체를 인식하여 그에 결박된 문자 정보를 덧씌운다'는 개념 — 오늘날의 객체 인식 + 라벨 오버레이 — 을 정확히 앞서 기술한 것이다.

1901년은 전기가 만능의 미래 기술로 상상되던 시기였고, 바움은 '전기 요정담'이라는 부제로 그 기대를 소설화했다. 여기서 중요한 것은 기술이 아니라 요구다 — 사람들이 원한 것은 더 잘 보이는 화면이 아니라 '눈에 보이지 않는 속성을 보이게 하는 것'이었다. AR의 본질적 약속이 기술보다 100년 가까이 앞서 문학에 기록되어 있다.

허구. 그러나 AR 문헌이 관습적으로 인용하는 가장 오래된 '정보 오버레이 안경'의 선례다. 다만 소설 속에서 소년은 이 안경 때문에 오히려 곤경에 빠지는데, 이는 정보 과잉 오버레이의 부작용을 처음 지적한 사례로도 읽힌다.

### 링크 트레이너 (Link Trainer, 'Blue Box')
| 항목 | 내용 |
| --- | --- |
| 주체 | Edwin A. Link |
| 연도 | 1929 (제작·특허), 1934년 6월 23일 (미 육군항공대 최초 구매) |
| 수치 | 1934년 6월 23일 미 육군항공대 6대 구매, 대당 $3,500. 2차대전 중 10,000대 이상 생산, 45분에 1대 출하. 미군 조종사 50만 명 이상 훈련. 계기비행 미숙으로 78일간 조종사 12명 사망(항공우편 사건) |
| 출처 | Wikipedia 'Link Trainer' (https://en.wikipedia.org/wiki/Link_Trainer) — 1934-06-23 6대 $3,500, 78일 12명 사망, 10,000대·45분, 50만 명 확인. 특허 연도는 자료 간 불일치(아래 uncertain 참조) |

모터로 피치·롤을 움직여 난기류까지 흉내내는 전기기계식 비행 시뮬레이터로, 조종사는 덮개를 닫고 계기만 보며 비행한다. AR/VR의 직접 조상은 아니지만 결정적 명제를 확립했다 — '훈련은 실제 환경 없이 합성 환경에서 더 안전하고 싸게 할 수 있다'. 이 명제가 이후 수십 년간 몰입형 디스플레이 연구비의 근거가 되었고, 서덜랜드 이후의 HMD 연구를 실제로 지불한 주체(군·항공)도 같은 논리를 따랐다.

1934년 항공우편 스캔들 당시 육군항공대가 우편 수송을 떠맡았는데, 조종사들이 계기비행에 익숙하지 않아 78일 동안 12명이 죽었다. 링크는 평가단이 비행 불가라고 판단한 안개 속을 직접 계기비행으로 뚫고 착륙해 보임으로써 계약을 따냈다. 즉 채택 동기는 기술 성숙이 아니라 사망 사고였다.

압도적 성공. 합성 환경 훈련이 하나의 산업이 되었고, 미국·영국·독일·일본·소련이 모두 채택했다. AR 서사에서 이 항목의 교훈은, 새 디스플레이 기술의 첫 지속 가능한 시장은 오락이 아니라 '사고를 줄여 돈을 아끼는 훈련'이었다는 점이다.

### 자이로 조준경 (Gyro Gunsight, GGS Mk I / Mk II, K-14, EZ 42)
| 항목 | 내용 |
| --- | --- |
| 주체 | 영국 Farnborough(RAE) 개발, Ferranti 제조 (에든버러 Crewe Toll 신공장); 미국 Sperry가 K-14로 생산; 독일 Askania EZ 42 |
| 연도 | 1941 (Mk I 제한생산·7월 실전), 1943 (Mk II 시험·배치) |
| 수치 | Mk I: 1941년 봄 제한생산, 1941년 7월 실전. Mk II: 1943년 말 시험·배치. 미 육군항공대 K-14 / 해군 Mk18. 독일 EZ 42: 1942년 여름 개발 착수, 1944년 7월 초도 33대 중 3대 인도, 이후 770대(대부분 1945년 초), 중량 13.6kg(30lb), 1대당 공수 130시간, Fw 190·Me 262에 약 200대 장착 |
| 출처 | Wikipedia 'Gyro gunsight' (https://en.wikipedia.org/wiki/Gyro_gunsight) — Mk I 1941·Ferranti, Mk II 1943, K-14/Mk18, EZ 42 33대·770대·13.6kg·130시간·약 200대 확인 |

자이로스코프로 기체의 선회율과 속도를 측정해 필요한 '리드각(예측 조준각)'을 계산하고, 그 결과에 따라 반사 조준경의 레티클 위치를 실시간으로 움직인다. 반사 조준경이 정적인 표식을 겹친 것이라면, 자이로 조준경은 겹치는 내용 자체를 센서 입력으로부터 연산해 만들어낸다. AR 관점에서 이것이 결정적 전환이다 — 오버레이가 '고정 그래픽'에서 '실시간 계산 결과'로 바뀌었다. 서덜랜드의 1968년 장치가 한 일도 본질적으로 같은 일이며, 다만 계산 주체가 자이로에서 디지털 컴퓨터로 바뀌었을 뿐이다.

공중전의 명중률을 지배하는 것은 조준의 정밀도가 아니라 '얼마나 앞을 겨누느냐'였고, 이는 표적 속도·각속도·탄속의 함수라 사람이 순간적으로 계산할 수 없었다. 특히 편각 사격(deflection shooting)은 숙련 조종사만 가능한 기술이어서, 대량 양성된 신참 조종사에게는 재현 불가능했다. 문제는 인간 계산 능력의 한계였고, 해법은 계산을 기계에 넘기고 결과만 시야에 겹치는 것이었다.

성공. 다만 독일 EZ 42는 실패에 가깝다 — 중량 13.6kg, 1대당 130시간의 공수로 생산이 지체되었고 전쟁 말기 200대 장착에 그쳤으며, 안정성 문제로 조종사들이 신뢰하지 않았다. 동일한 원리인데 영국·미국은 성공하고 독일은 실패한 이유는 기술이 아니라 생산공학과 시기였다 — AR 역사에서 반복되는 '원리는 맞는데 제조가 못 따라간' 실패 유형의 초기 사례다.

### TRE의 레이더–앞유리 결합 실험 (HUD의 직계 조상)
| 항목 | 내용 |
| --- | --- |
| 주체 | 영국 Telecommunications Research Establishment (TRE) |
| 연도 | 1942년 10월 |
| 수치 | 1942년 10월. 결합 대상: 레이더 표시관 영상 + 표준 GGS Mk.II 자이로 조준경 투사상. 투사면: 항공기 앞유리의 평평한 영역 |
| 출처 | Wikipedia 'Head-up display' (https://en.wikipedia.org/wiki/Head-up_display) 역사절 — 1942년 10월 TRE, GGS Mk.II 및 레이더관 영상의 앞유리 결합 확인 |

TRE는 야간전투기의 레이더 화면 영상과 자이로 조준경의 투사상을 앞유리의 평평한 부분 위에 겹쳐 놓는 데 성공했다. 이것은 두 가지 점에서 새롭다. 첫째, 겹치는 내용이 '표적이 아니라 센서 데이터(레이더)'다 — 즉 사람 눈에 보이지 않는 정보를 시야에 넣었다. 둘째, 투사면이 별도의 조준경 유리가 아니라 조종석 앞유리 자체다 — 특정 장비의 부속이 아니라 '조종석 창 전체가 디스플레이'라는 개념이 여기서 나온다. AR의 정의 중 '실세계에 정합된 컴퓨터/센서 정보의 중첩'에 가장 먼저 도달한 실험이다.

야간전투기 조종사는 레이더 조작수의 구두 유도에 의존했는데, 교전 직전 몇 초 동안은 구두 전달의 지연이 치명적이었다. 문제는 레이더 성능이 아니라 '레이더 화면을 보는 사람과 조준하는 사람이 다르고, 시선이 두 곳에 나뉘어 있다'는 것이었다. 정보를 조종사의 시선 한 곳에 모으는 것이 유일한 해법이었다.

실험은 성공했으나 즉시 실전 배치되지는 않았다 — 종전과 함께 우선순위에서 밀렸고, 실용 HUD가 나오기까지 16년이 더 걸렸다. 발표와 실용화의 간극이 큰 전형적 사례다.

### 최초의 실용 HUD — 블랙번 버캐니어 'Strike Sight'
| 항목 | 내용 |
| --- | --- |
| 주체 | Royal Aircraft Establishment (설계), Rank Cintel (초기 양산), 이후 Elliott Flight Automation이 사업 인수 |
| 연도 | 1958년 4월 30일 (시제기 초도비행), 1958 (양산기 최초 통합), 1959 (잉글리시 일렉트릭 라이트닝 파생형) |
| 수치 | 버캐니어 시제기 초도비행 1958년 4월 30일. Elliott, Mark III까지 버캐니어용 375대 생산, 약 25년간 운용, 'fit and forget'이라는 평판. 1959년 라이트닝에 미사일 공격용 파생형. 1975년 계기비행(IFR) HUD 접근 절차 개발. 1970년대 민항 도입. 1988년 올즈모빌 커틀러스 슈프림 — 세계 최초 HUD 탑재 양산차 |
| 출처 | Wikipedia 'Head-up display' (https://en.wikipedia.org/wiki/Head-up_display) — 버캐니어 1958-04-30, Rank Cintel 1958 통합, Elliott 375대·Mark III·25년, 라이트닝 1959, 클롭슈타인, 1975 IFR, 1988 올즈모빌, 4세대 구분 확인 |

'head-up display'라는 용어 자체가 이 시기에 처음 쓰였다. 버캐니어는 초저공 고속 침투 공격기여서 조종사가 계기판을 내려다볼 여유가 물리적으로 없었고, RAE는 비행 정보와 무기 조준 정보를 하나의 결합기에 통합한 Strike Sight를 설계했다. 이는 반사 조준경(무한대 허상) + 자이로 조준경(실시간 연산) + TRE 실험(센서 정보 중첩)의 세 계보가 하나의 제품으로 합쳐진 지점이다. 이후 1세대 CRT 형광면, 2세대 LED 백라이트 LCD, 3세대 광도파로 결합기, 4세대 투명 매질 위 레이저 주사로 세대가 나뉘는데, 3세대의 광도파로(waveguide)는 오늘날 AR 글래스가 그대로 물려받은 광학계다.

1950년대 말 전술 교리가 고고도 폭격에서 초저공 침투로 바뀌면서, 조종사가 계기를 보려고 시선을 내리는 1~2초가 곧 지면 충돌을 뜻하게 되었다. 즉 HUD를 요구한 것은 디스플레이 기술의 성숙이 아니라 '고도 60m에서 시속 900km로 나는 임무'라는 새 요구였다.

완전한 성공이자, 프리히스토리 항목 중 유일하게 오늘날까지 끊기지 않고 산업으로 이어진 계보다. 군용 → 민항(1970년대) → 자동차(1988) → 소비자 AR 글래스로 광학계와 용어를 물려주었다.

### Morton Heilig, 「미래의 영화 (The Cinema of the Future / El Cine del Futuro)」
| 항목 | 내용 |
| --- | --- |
| 주체 | Morton Leonard Heilig (1926.12.22 ~ 1997.5.14), 영화촬영감독 |
| 연도 | 1955 (원 발표), 1992 (MIT Press 『Presence』 재수록 영역본) |
| 수치 | 1955년 에세이. 재수록: Presence: Teleoperators and Virtual Environments, Vol.1 No.3 (1992), pp.279-294 (제목 'El Cine del Futuro: The Cinema of the Future') |
| 출처 | Presence: Teleoperators and Virtual Environments 1(3):279-294 (1992), MIT Press 재수록 (https://direct.mit.edu/pvar/article/1/3/279 — 접근 403으로 서지정보만 확인); Wikipedia 'Sensorama' 및 'Morton Heilig'가 1955년 에세이 존재를 확인 |

하일리그는 영화를 '시각 매체'가 아니라 '의식 전달 매체'로 재정의하고, 미래의 영화는 시각뿐 아니라 청각·후각·촉각·평형감각까지 동원해 관객의 감각 전체를 점유해야 한다고 주장했다. 그는 인간 감각의 주의 배분을 백분율로 추정해 각 감각에 얼마의 대역폭을 할당해야 하는지까지 논했다. 중요한 것은 이것이 장치 설명이 아니라 '설계 요구사항 명세'였다는 점이다 — 이후 그가 만든 텔레스피어 마스크와 센소라마는 모두 이 에세이가 먼저 규정한 요구를 하드웨어로 구현한 것이다. AR/VR 역사에서 이론이 장치를 앞선 드문 사례다.

1950년대 초 미국 영화산업은 텔레비전에 관객을 빼앗기고 있었고, 시네라마(1952)·3D 영화(1952-54)·시네마스코프(1953)·Smell-O-Vision 같은 감각 확장 실험이 쏟아지던 시기였다. 즉 하일리그의 이론은 순수한 발상이 아니라 '텔레비전이 줄 수 없는 것을 극장이 주어야 한다'는 산업적 생존 문제에 대한 답이었다.

이론으로는 성공, 산업적으로는 소멸. 감각 확장 영화 유행은 1950년대 말 대부분 사라졌고 하일리그의 구상도 함께 묻혔다. 그러나 1992년 『Presence』 창간 초기에 재수록되면서 VR/AR 학계의 정전(canon)으로 복권되었다 — 발표 37년 뒤의 재발견이다.

### Telesphere Mask — US Patent 2,955,156 'Stereoscopic-television apparatus for individual use'
| 항목 | 내용 |
| --- | --- |
| 주체 | Morton L. Heilig |
| 연도 | 1957년 5월 24일 출원, 1960년 10월 4일 등록 |
| 수치 | 미국 특허 2,955,156. 출원 1957-05-24, 등록 1960-10-04. 시야각 수평·수직 약 140도. 구성: 중공 케이싱 1, 광학유닛 2, 텔레비전관 2(컬러 권장), 이어폰 2, 공기 분출 노즐 2 |
| 출처 | Google Patents US2955156A (https://patents.google.com/patent/US2955156A/en) — 발명자·출원일 1957-05-24·등록일 1960-10-04·약 140도 시야·구성요소 전체 원문 확인 |

특허 원문은 '중공 케이싱, 한 쌍의 광학유닛, 한 쌍의 텔레비전관, 한 쌍의 이어폰, 한 쌍의 공기 분출 노즐'로 구성된다고 명시한다. 주변시 렌즈가 텔레비전관에서 오는 주변 광선을 꺾어 눈 옆쪽으로 입사시켜 수평·수직 약 140도 시야를 만든다. 이어폰은 외이를 덮지 않아 귀가 집음기관으로 계속 기능하게 설계되었다. 노즐은 속도·온도·냄새가 다른 기류를 내보낸다. 좌우 광학유닛과 텔레비전관은 사용자 눈에 맞춰 개별 조정되고, 스트랩으로 머리에 고정한다. 즉 오늘날 HMD의 폼팩터 — 머리 고정, 양안 개별 디스플레이, 동공간거리 조정, 넓은 시야, 헤드폰 — 가 1957년에 이미 전부 명세화되어 있다. 다만 시스루가 아니므로 AR이 아니라 VR 계보의 원형이며, 헤드트래킹도 없다.

「미래의 영화」에서 규정한 요구를 극장 규모가 아니라 1인용 장치로 축소하면 비용이 급감한다는 판단이 있었다. 하일리그의 문제는 감각 몰입 자체가 아니라 '몰입을 누가 지불하는가'였고, 개인용 폼팩터는 그 경제 문제에 대한 답이었다.

실패. 특허는 등록되었으나 제작·상용화되지 못했다. 하일리그는 끝내 투자를 유치하지 못했다. 원인은 기술적 미성숙(소형 컬러 CRT의 부재, 콘텐츠 공급원 부재)과 경제적 요인(투자자가 판매 경로를 상상하지 못함)이 겹친 것인데, 후자가 결정적이었다는 것이 통설이다.

### Philco Headsight — 최초의 헤드트래킹 HMD
| 항목 | 내용 |
| --- | --- |
| 주체 | Charles P. Comeau, James S. Bryan (Philco Corporation 엔지니어) |
| 연도 | 1961 |
| 수치 | 1961년. 원 발표: C. Comeau & J. Bryan, 'Headsight Television System Provides Remote Surveillance', Electronics 誌, 1961년 11월 10일자, pp.86-90 (아래 uncertain 참조). 구성: 헬멧 장착 CRT + 자기식 헤드트래킹 + 원격 폐회로 카메라 |
| 출처 | Wikipedia 'Head-mounted display' (https://en.wikipedia.org/wiki/Head-mounted_display) — Comeau & Bryan 1961, 헬멧 CRT + 자기식 추적 + 원격 카메라 확인; VRS 'History of VR' (https://www.vrs.org.uk/virtual-reality/history.html) 동일 내용 확인. Electronics 誌 서지사항은 미검증(uncertain 참조) |

헬멧에 CRT를 달고, 자기식 추적 장치가 착용자의 머리 움직임을 감지해 멀리 떨어진 곳의 카메라를 같은 방향으로 회전시킨다. 착용자가 고개를 돌리면 원격지의 시야가 함께 돌아가므로, 마치 그곳에 있는 것처럼 주위를 둘러볼 수 있다. AR/VR 계보에서 이 장치가 추가한 요소는 명확하다 — '헤드트래킹', 즉 머리 자세를 측정해 표시 내용을 그에 맞춰 갱신하는 폐루프다. 하일리그의 장치에는 이것이 없었고, 서덜랜드의 1968년 장치는 이것을 계산기와 결합했을 뿐이다. 다만 Headsight가 보여주는 것은 컴퓨터 그래픽이 아니라 실시간 카메라 영상이므로, 이것은 AR이 아니라 원격현전(telepresence)이다.

필코의 동기는 오락이 아니라 위험 환경 원격 감시였다. 방사성 물질 취급, 위험 구역 감시처럼 사람이 직접 갈 수 없는 곳에서, 고정 카메라는 시야가 고정되어 상황 파악이 안 되고 조이스틱으로 카메라를 돌리면 조작에 주의를 빼앗긴다. 문제는 '보는 것'이 아니라 '보려는 의도를 조작 없이 전달하는 것'이었고, 머리 방향이 곧 그 의도의 가장 자연스러운 표현이었다.

기술적으로 성공했으나 제품으로 확산되지 못했다. 이 계보는 1960~70년대 벨 헬리콥터의 야간 착륙용 헬멧 카메라 시스템 등 군용 원격시각으로 이어졌고, 1980년 민스키가 'telepresence'라는 용어를 제안하면서 독립 분야가 되었다.

### Sensorama — US Patent 3,050,870 'Sensorama Simulator'
| 항목 | 내용 |
| --- | --- |
| 주체 | Morton L. Heilig |
| 연도 | 1961년 1월 10일 출원, 1962년 8월 28일 등록, 1962 시연 |
| 수치 | 미국 특허 3,050,870. 출원 1961-01-10, 등록 1962-08-28. 후드당 1~4인 수용. 시야: 눈당 수평 약 150도, 특허 본문 표현으로 '완전 주변시, 3-D' 약 160~180도. 단편영화 5편 제작(자료에 따라 6편). 촬영: 촬영자 몸에 35mm 카메라 3대 장착 |
| 출처 | Google Patents US3050870A (https://patents.google.com/patent/US3050870A/en) — 명칭·출원 1961-01-10·등록 1962-08-28·후각/진동/좌석/자기트랙/시야각 원문 확인; Wikipedia 'Sensorama' 및 'Morton Heilig' (https://en.wikipedia.org/wiki/Morton_Heilig) — 5편, 35mm 3대, 자금 실패 원인 확인 |

아케이드 게임기처럼 생긴 캐비닛으로, 관람자가 후드에 얼굴을 넣으면 입체 영상, 후드 내부의 스테레오 스피커, 전자석 제어 방향(芳香) 분사기, 좌석에 붙은 진동 유닛, 모터로 상하 구동되는 좌석, 송풍 덕트가 동시에 작동한다. 필름의 자기 트랙에 감각 제어 신호가 영상과 동기되어 기록된다. 대표 콘텐츠는 브루클린 거리를 오토바이로 달리는 영상으로, 관람자는 얼굴에 바람, 좌석의 진동, 3D 시야, 도시의 냄새를 함께 느꼈다. 이것은 「미래의 영화」 명세의 완전한 하드웨어 구현이지만 상호작용이 전혀 없다 — 관람자는 시선을 돌릴 수도, 경로를 바꿀 수도 없다. 헤드트래킹의 부재가 이 계보의 한계를 규정한다.

텔레스피어 마스크가 투자를 못 받은 뒤, 하일리그는 개인 착용형에서 '설치형 코인 오퍼레이티드 기기'로 사업 모델을 바꿨다. 즉 기술이 바뀐 것이 아니라 과금 방식이 바뀐 것이며, 이는 하일리그 자신이 문제를 기술이 아니라 경제로 인식했음을 보여준다.

실패. 원인을 분리하면 (1) 경제적 — 콘텐츠 제작비가 감당 불가능했다. 신작 한 편을 찍으려면 촬영자 몸에 35mm 카메라 3대를 매달아야 했고, 하일리그는 그 비용을 댈 자금을 얻지 못했다. (2) 사업적 — 투자자와 업계가 이 물건을 어떻게 팔아야 할지 이해하지 못했다. 기술적 실패가 아니었다는 점이 핵심이다. 장치는 작동했고 사람들은 감탄했지만, 편당 제작비를 회수할 유통 구조가 없었다. 이 실패 유형 — '체험은 훌륭한데 콘텐츠 단가가 시장을 못 만든다' — 은 이후 60년간 VR/AR에서 계속 반복된다.

### '다모클레스의 칼(Sword of Damocles)'이라는 별칭 — 그 출처와 오해
| 항목 | 내용 |
| --- | --- |
| 주체 | Ivan E. Sutherland (1938년생); 학생 Bob Sproull, Quintin Foster, Danny Cohen |
| 연도 | 1966 (MIT 링컨연구소에서 착수), 1968 (하버드에서 완성·발표) |
| 수치 | 서덜랜드: MIT 박사 1963(지도교수 클로드 섀넌, 심사위원 민스키·쿤스), Sketchpad 1962, ARPA IPTO 실장 1964~1965(릭라이더 후임), 하버드 부교수 1965~1968, 유타대 교수 1968~1974. 1965년 에세이 'The Ultimate Display', Proceedings of IFIP Congress, pp.506-508. 1968년 장치는 6개 서브시스템(클리핑 디바이더, 행렬 곱셈기, 벡터 생성기, 헤드셋, 머리위치 센서, 범용 컴퓨터)으로 구성 |
| 출처 | Wikipedia 'The Sword of Damocles (virtual reality)' (https://en.wikipedia.org/wiki/The_Sword_of_Damocles_(virtual_reality)) — 서덜랜드 본인의 '농담 이름' 진술, 6개 서브시스템, 1966 링컨연구소 착수 확인; Wikipedia 'Ivan Sutherland' (https://en.wikipedia.org/wiki/Ivan_Sutherland) — 생년·섀넌·IFIP 1965 pp.506-508·재직연도 확인; VRS 'History of VR' (https://www.vrs.org.uk/virtual-reality/history.html) — '무게 때문에 천장에 매달았다'는 통설 서술 확인(대조용) |

반투명 거울(빔 결합기)로 컴퓨터가 생성한 와이어프레임 선화를 실제 방 위에 겹치고, 천장에 매단 기계식 링크 암이 머리 위치를 측정해 시점에 맞춰 그림을 다시 그린다. 여기서 반드시 바로잡아야 할 오해가 있다. 흔히 '장치가 너무 무거워 천장에 매달았고 그래서 다모클레스의 칼이라 불렸다'고 서술되지만(예: 다수의 대중 해설), 서덜랜드 본인의 설명에 따르면 그 별칭은 '디스플레이를 지지하고 추적하는 기계 시스템에 붙인 농담 이름'일 뿐이며, 머리 위로 뻗은 거대한 십자 모양 구조물의 생김새에서 나온 말장난이다. 즉 별칭이 가리키는 것은 HMD가 아니라 천장 추적 암이다. 또 하나의 오해는 이것을 'VR의 시작'으로 부르는 것인데, 이 장치는 반투명 거울로 실세계를 그대로 보면서 그래픽을 겹치는 광학 시스루 장치이므로 계보상 AR에 더 가깝다.

서덜랜드는 1965년 「The Ultimate Display」에서 '궁극의 디스플레이란 컴퓨터가 물질의 존재 자체를 제어하는 방'이라고 썼다. 그가 1968년에 실제로 푼 문제는 그 방이 아니라 훨씬 좁은 것이었다 — 앞선 60년간 광학(페퍼의 유령·반사 조준경), 연산(자이로 조준경), 추적(Headsight)이 각각 따로 존재했고, 남은 과제는 '겹칠 내용을 머리 자세에 맞춰 실시간으로 계산하는 일'뿐이었다. 그 계산기를 그가 ARPA에서 직접 다뤄본 사람이었다는 점이 결정적이다.

성공했으나 제품은 아니었다. 이 항목의 의의는 '증강현실이 1968년에 갑자기 나왔다'는 통념을 반증하는 데 있다. 서덜랜드가 새로 만든 것은 요소가 아니라 요소들의 결합이었다.

#### 검증에서 잡힌 정정
- 링크 트레이너 특허연도 오류 — 항목 헤더가 '1929 (제작·특허)'라고 적어 제작과 특허를 같은 해로 묶었으나, 실제 특허 US 1,825,462 'Combination training device for student aviators and entertainment apparatus'(Edwin A. Link, Jr.)는 출원 1930-03-12, 등록 1931-09-29이다(Google Patents 원문 확인). 1929는 최초 제작연도일 뿐 특허연도가 아니다. 연구 스스로 '자료 간 불일치'라 하였으나 불일치가 아니라 확정 가능한 오류다. → '1929 제작 / 1931 특허(출원 1930)'로 수정할 것.
- 서덜랜드 ARPA IPTO 재직기간 오류 — '1964~1965'로 적었으나, 연구가 출처로 명시한 위키피디아 'Ivan Sutherland'는 1964~1966으로 기재한다(릭라이더가 1964년 IBM으로 옮기며 승계). 자기 출처와 1년 어긋난다.
- GGS Mk.II 연대 모순 — 서사와 TRE 항목이 '1942년 10월 TRE가 레이더 화면과 표준 GGS Mk.II를 앞유리에 결합'이라 단정했으나, 같은 문서의 자이로 조준경 항목은 Mk.II를 '1943년 말 시험·배치'로 적는다. 1942년 10월에 '표준' Mk.II는 아직 존재하지 않았으므로 둘 중 하나는 반드시 틀리다. (위키피디아 'Head-up display'와 'Gyro gunsight' 두 문서 자체가 상충하므로, Mk.II를 그대로 인용하려면 '시제/초기형 GGS'로 완화하거나 상충 사실을 각주로 노출해야 한다.)
- 센소라마 수용인원 수치 오독 — '후드당 1~4인 수용'이라 적었으나, US 3,050,870 원문은 후드 1개당 1인이고 도시된 장치 전체가 1~4인을 수용하는 구성이다. '후드당'이 아니라 '장치당'이다.
- 휘트스톤 입체경 연도 정밀도 오류 — 서사가 '1838년 휘트스톤의 입체경'이라 발명연도처럼 서술했으나, 위키피디아 'Stereoscope'는 '최초 입체경(반사경식·프리즘식)은 1832년 휘트스톤이 고안하고 광학기사 R. Murray가 제작', 1838년은 왕립학회 발표연도로 기재한다. 항목 표 안의 '1838년 발표'는 맞지만 서사 문장은 발명연도를 6년 늦춰 잡았다.
- Oigee 조준경의 실전 여부 과장 — 서사가 '1918년 Oigee 조준경이 알바트로스 D.Va에 실려 실전에 들어갔다'고 단정했으나, 출처인 위키피디아 'Reflector sight'의 표현은 'used in operational trials on the Albatros D.Va and Fokker Dr.I'(실전 시험/운용 시험)이다. trials → '실전 투입'은 근거를 넘어선 격상이다. (부수적으로 항목 헤더의 '1918 항공 실전 투입'도 같은 문제.)
- 인용 제목 절단 — 카메라 루시다 특허명을 'An Instrument Whereby Any Person May Draw in Perspective'로 따옴표 안에 완결형으로 제시했으나, 실제 특허명은 'An Instrument Whereby Any Person May Draw in Perspective, or May Copy or Reduce Any Print or Drawing'이다. 축약이면 말줄임 표기가 필요하다.
- 서덜랜드 1968년 장치의 완성 장소 — 출처 불일치를 단정으로 처리했다. 항목은 '1968 (하버드에서 완성·발표)'라 적고 근거로 위키피디아 'The Sword of Damocles (virtual reality)'를 들었으나, 그 문서는 1966년 MIT 링컨연구소 착수 후 '컴포넌트 통합은 1960년대 말 유타대학에서' 이루어졌다고 기술한다(하버드 완성은 'Head-mounted display' 문서 쪽 서술). 두 출처가 갈리므로 단정 대신 병기가 맞다.
- 반사 조준경 채택 범위 과장(경미) — '1930년대 이후 모든 주요 공군의 표준'이라 했으나 출처는 '1930년대에 들어서야 널리 채택되었고, 먼저 프랑스, 이후 대부분의 주요 공군'(most other major airforces)이라 적는다. '모든'은 출처의 'most'를 넘는다.
- 링크 트레이너 항목의 '1929 (제작·특허)' — 특허는 1929년이 아니다. Edwin A. Link Jr.의 US 1,825,462 'Combination training device for student aviators and entertainment apparatus'는 1930년 3월 12일 출원, 1931년 9월 29일 등록(Google Patents 원문 확인). 1929는 시제기 제작 연도일 뿐이며, 조사는 이를 'uncertain'으로 남겼지만 실제로는 확정 가능한 오류다.
- TRE 항목: '1942년 10월 … 표준 GGS Mk.II 자이로 조준경 투사상'과 자이로 조준경 항목의 'Mk II: 1943년 말 시험·배치'가 정면 충돌한다. 1942년 10월 시점에 Mk II는 아직 시험조차 되지 않았다. 위키 'Head-up display'와 'Gyro gunsight' 사이의 모순을 양쪽 다 '확인'으로 표시한 채 옮겼고, 이 항목이 'HUD의 직계 조상'이라는 서사 축을 지탱하므로 축 자체가 불확실해진다.
- 서사 문단: '1900년 하워드 그럽의 반사 조준경 특허는 무한대 허상으로 시차를 없애  \"머리를 움직여도 표식이 대상에 붙어 있게\" 만들었다' — 광학적으로 틀렸다. 반사 조준경의 무시차 성질은 레티클이 *총/기체의 조준선*에 고정되어 눈 위치가 바뀌어도 같은 조준점을 가리킨다는 뜻이지, 표식이 *표적*에 붙는다는 뜻이 아니다. 표적이 움직이면 레티클은 따라가지 않는다. 표적 운동을 반영하는 것은 1941년 자이로 조준경의 선도각 계산이며, 그조차 표적이 아니라 계산된 선도각에 고정된다. 이 문장은 AR의 핵심인 world-registration을 1900년으로 소급하려다 생긴 오류다.
- 반사 조준경 항목: '1918년 Oigee 조준경이 알바트로스 D.Va에 실려 실전에 들어갔다' — 인용 출처(Wikipedia 'Reflector sight')의 표현은 'used in operational trials on the biplane Albatros D.Va and triplane Fokker Dr.1', 즉 운용 시험이다. '실전 투입'은 출처가 뒷받침하지 않는 격상 서술.
- 자이로 조준경 항목 머리말의 'Ferranti 제조 (에든버러 Crewe Toll 신공장)'을 1941년 Mk I에 결부한 것 — 출처는 에든버러 신공장을 Mk II 생산을 위해 지었다고 서술한다. 또한 서사 문단의 '1941년 페란티 자이로 조준경은 … 계산하기 시작했고'는 개발 주체를 바꿔치기한다. Mk I 개발은 RAE Farnborough, Ferranti는 제조사다.
- 센소라마 항목의 '후드당 1~4인 수용'과 '시야: 눈당 수평 약 150도' — 인용한 두 출처 어디에서도 확인되지 않는다. US 3,050,870 원문은 '160도~180도'의 완전 주변시를 말하고, Wikipedia 'Sensorama'는 수용 인원도 시야각 수치도 적지 않는다. 150도와 1~4인은 출처 미상 수치.
- 입체경 항목의 '1838 (휘트스톤)'을 발명 연도로 읽히게 쓴 것 — Wikipedia 'Stereoscope'는 '최초의 입체경은 1832년 Wheatstone이 고안하고 옵티션 R. Murray가 제작했으며, 1838년 6월 21일 왕립학회에 결과를 처음 발표했다'고 한다. 1838은 발표 연도다.
- 버캐니어 항목의 결론 '프리히스토리 항목 중 유일하게 오늘날까지 끊기지 않고 산업으로 이어진 계보' — 같은 조사 목록이 스스로 세 개의 반례를 적고 있다: 페퍼의 유령은 160년간 존속해 디즈니 유령의 저택·Musion Eyeliner·2012 코첼라로 이어졌고, 반사 조준경은 '오늘날 소총용 도트사이트로 여전히 대량 생산'되며, 카메라 루시다는 1980년대까지 현미경 표준 기구로 살아남아 고생물학·신경생물학에서 지금도 쓰인다. '유일하게'는 성립하지 않는다.
- 분기 기준의 자기모순: 입체경 항목은 '입체 몰입 vs 광학 결합'을 VR/AR의 갈림길로 선언한다. 그런데 텔레스피어(US 2,955,156 원문: 얼굴에 밀착하는 중공 케이싱 + TV관 2 — 시스루 아님)와 센소라마(밀폐 후드)를 AR 척추 위 '개인용 HMD의 형태 확정' 단계로 배치한다. 자기 기준대로면 둘 다 VR 가지이며, AR 전사(前史)의 인과선에 놓일 수 없다.
- 서사 문단: '1961년 필코의 헤드사이트는 … 원격 카메라를 돌려 \"추적\"을 더했다' — 겹침의 계보에 추적을 더한 사건이 아니다. 헤드사이트는 헬멧 CRT에 원격 폐회로 카메라 영상만 보여주는 텔레프레즌스 장치로, 실제 시야와의 중첩(광학 결합)이 전혀 없다. 서사가 세운 '광학 결합' 축과 다른 축(원격시각)에 속한다.
- 서사 문단의 종결부: '1968년 서덜랜드에게 남은 과제는 무엇을 겹칠지 실시간으로 계산하는 일뿐이었다' — 조사가 인용한 6개 서브시스템(클리핑 디바이더, 행렬 곱셈기, 벡터 생성기, 헤드셋, 머리위치 센서, 범용 컴퓨터) 중 앞선 항목들이 제공한 것은 헤드셋 광학계 정도다. 실시간 3D 파이프라인 3종과 머리위치 센서는 선행 항목 어디에도 없다(필코의 자기식 추적은 카메라 조향용이지 시점 변환용이 아니다). '계산뿐'은 6개 중 4~5개를 지운다.
- 센소라마 실패 원인의 단순화: 서사 문단은 '자금을 얻지 못해 소멸'로 요약하지만, 인용 출처(Wikipedia 'Morton Heilig')는 두 원인을 든다 — 'the high costs of the filmmaking'과 'the business community just couldn't figure out how to sell it'. 후자는 자금 부족이 아니라 판매 경로·수요 부재이며, 조사 항목 본문은 이를 구분해 적어놓고도 요약 서사에서 '자금' 하나로 뭉갰다.
- 계보의 근거 부재: 월러스턴(1806)→휘트스톤(1838)→페퍼(1862)→그럽(1900)을 잇는 전달 경로를 뒷받침하는 출처가 하나도 제시되지 않았다. Wikipedia 'Reflector sight'는 '반사 조준경의 아이디어는 1900년 Howard Grubb에서 비롯되었다'고 독립 기원으로 서술한다. 반대로 카메라 루시다의 문서화된 직계 귀결은 1833년 탤벗의 사진술이며, 이는 '겹침'에서 이탈하는 방향이다. '유리와 렌즈'라는 단일 줄기는 사후적으로 구성된 것이다.
- '1942년 10월 TRE … 1958년 4월 30일 버캐니어가 이를 실용화했다'는 인과 주장 — 인용 출처는 버캐니어 Strike Sight의 동기를 '초저고도·고속에서 수 초 안에 투하'라는 요구로 설명할 뿐, TRE 실험의 계승이라고 말하지 않는다. 16년 간격에 기관도 다르다(TRE vs RAE 설계·Rank Cintel 생산). 연대순 인접을 인과로 바꾼 서술이다.
- 축의 범위 설정 자체: '증강현실'이라는 용어는 1990년 보잉의 Thomas P. Caudell에서, AR의 정의 요건(실·가상 결합 + 실시간 상호작용 + 정확한 3D 정합)은 Azuma에서 온다. 1968년에서 끊는 프리히스토리 구성은 정합(registration) 요건이 언제 왜 정의에 들어왔는지를 다루지 않은 채 '겹침의 계보'를 완성했다고 선언한다.
- 링크 트레이너 '1929 (제작·특허)' — 특허 연도가 틀렸다. 시제기 데뷔는 1929년이 맞지만 특허는 US 1,825,462 'Combination training device for student aviators and entertainment apparatus'로 1930-03-12 출원·1931-09-29 등록이다(Google Patents 원문 확인). 항목이 '자료 간 불일치'로 각주만 달고 헤더에는 1929를 확정 사실처럼 적었다.
- '1918년 Oigee 조준경이 알바트로스 D.Va에 실려 실전에 들어갔다' / 헤더 '1918 (항공 실전 투입)' — 과장. 인용 출처인 위키백과 'Reflector sight' 원문은 'One version was used in operational trials on the biplane Albatros D.Va and triplane Fokker Dr.1 fighters'로 '운용 시험(operational trials)'이라고만 적는다. 실전 투입·전과·생산 수량 기록은 해당 출처에 없다. '실전에 들어갔다'는 출처가 지지하지 않는 승격이다.
- 서덜랜드 'ARPA IPTO 실장 1964~1965' — 인용 출처가 지지하지 않는다. 위키백과 'Ivan Sutherland' 본문은 1964년 릭라이더 후임 취임을 적고 재임 종료를 1966년(후임 로버트 테일러)으로 처리한다. 같은 문서의 구술사 참고문헌 설명은 '1963 to 1965'라고 적어 출처 내부가 서로 어긋난다. 따라서 '1964~1965'는 단정할 수 없는 수치이며, 통상 표기는 1964~1966이다.
- '1968 (하버드에서 완성·발표)' — 인용 출처가 반대로 말한다. 항목이 근거로 든 위키백과 'The Sword of Damocles (virtual reality)'는 현재 'Ivan Sutherland's head-mounted 3D display'로 개명되어 그 URL은 리다이렉트이며, 본문은 'The system was created in 1968 ... at the University of Utah'라고 유타대를 명시한다. 하버드 서술은 다른 문서(위키백과 'Augmented reality')에만 있어 위키백과 내부가 모순된다. 하버드를 확정 사실로 적은 것은 인용 출처와 불일치한다.
- 필코 헤드사이트 항목의 '이 계보는 1960~70년대 벨 헬리콥터의 야간 착륙용 헬멧 카메라 시스템 등 군용 원격시각으로 이어졌고, 1980년 민스키가 telepresence라는 용어를 제안' — 출처 귀속이 허위다. 인용된 위키백과 'Head-mounted display' 위키텍스트를 검색하면 'Bell Helicopter', 'Minsky', 'telepresence' 모두 0건이고, 함께 인용된 VRS 'History of VR' 페이지에도 벨 헬리콥터 언급이 없다. 민스키의 1980년 telepresence 명명 자체는 별개로 사실이지만, 이 두 출처에서 확인했다는 서술은 성립하지 않는다.
- 반사 조준경 '1930년대 이후 모든 주요 공군의 표준이 되었고' — '모든'은 과장. 원문은 'not widely adopted for fighter and bomber aircraft until the 1930s, first by the French, then by most other major airforces'로 '대부분(most)'이다. 또 같은 문서는 미군이 반사 조준경(도트사이트)을 광범위 도입한 시점을 2000년대 초 Aimpoint CompM2로 적어, '1930년대 이후 오늘날까지 끊기지 않은 표준'이라는 계보 서사와 어긋난다.
- (외 9건)

## military
항목 14개 · 검증 정정 지적 51건

> 증강현실의 계보는 "실제 풍경 위에 정보를 겹쳐 보여주면 사람이 더 잘 싸운다"는 군사적 요구에서 시작한다. 1900년 Howard Grubb의 반사식 조준기 특허가 원형이고, 1940년대 초 영국 TRE가 야간전투기 레이더 화면과 자이로 조준기 상을 풍방유리에 겹쳐 띄우면서 '중첩 정보'라는 발상이 실전에 들어왔다. 1958년 시험비행한 해군 공격기 Blackburn Buccaneer의 Strike Sight가 최초의 실용 HUD로 꼽힌다. 저고도 고속 폭격에서 조종사가 시선을 내릴 수 있는 시간이 수 초뿐이라는 고유한 문제가 이 장치를 낳았다. Rank Cintel이 제작하고 Elliott이 Mark III까지 375기를 만들었다. 1960년대 프랑스 시험조종사 Gilbert Klopfstein이 기종 간 이식 가능한 표준 심볼로지를 정리하면서 HUD는 문법을 얻었고, 1975년 계기착륙 HUD를 거쳐 민항으로 넘어갔다.  다음 단계는 시선 자체를 조준선으로 쓰는 헬멧이었다. 1968년 Ivan Sutherland의 Sword of Damocles가 쓴 소형 CRT는 원래 미군 헬기 승무원용 부품이었다. 1969년부터 미 해군은 Honeywell VTAS를 F-4J에 달았고 1974~78년 ACEVAL/AIMVAL에서 호평을 받았지만, 당시 AIM-9의 오프보어사이트 능력이 헬멧을 따라가지 못해 서방에서 20년 가까이 사장됐다. 그 공백을 소련이 채웠다. 1981년 설계된 Shchel-3UM과 R-73을 얹은 MiG-29가 1985년 배치됐고, 독일 통일 후 서방이 구 동독 MiG-29에 접근하면서 격차가 드러나자 1990년대 내내 JHMCS 같은 만회 프로그램이 쏟아졌다.  같은 시기 미 공군의 Tom Furness는 1966년부터 1989년까지 Wright-Patterson에서 조종석 표시장치를 연구했고 1986년 Super Cockpit 프로그램을 조직했다. 이 흐름이 1989년 워싱턴대 HITLab으로, 다시 민간 VR/AR로 흘러나갔다. 육상에서는 1985년 AH-64 아파치의 IHADSS가 40°×30° 단안 디스플레이로 야간 초저공 비행을 가능하게 했고, 2003년 JHMCS가, 2010년대에는 HUD를 아예 없애고 헬멧에 전부 몰아넣은 F-35 HMDS가 등장했다.  그러나 지상 보병에게 같은 것을 주려던 시도는 계속 실패했다. 1989년 시작한 Land Warrior는 무게와 예산 때문에 2007년 2월 취소됐고, 2021년 최대 218.8억 달러 규모로 계약된 육군 IVAS는 두통·구토·야간 발광 같은 문제로 의회 예산이 깎이고 2025년 2월 마이크로소프트가 사업을 Anduril에 넘기며 사실상 재시작됐다. 항공기에서 통한 AR이 보병에게 통하지 않은 이유 — 고정된 좌석·안정된 전원·제한된 시야 대 걷고 뛰고 엎드리는 몸 — 이 이 축의


### 반사식 조준기와 TRE의 레이더-조준기 중첩 (AR의 광학적 원형)
| 항목 | 내용 |
| --- | --- |
| 주체 | Howard Grubb(아일랜드 광학기사), 영국 Telecommunications Research Establishment(TRE), RAF 야간전투기 부대 |
| 연도 | 1900년 (Grubb 특허) / 1940년대 초 (TRE 실전 적용) |
| 수치 | 자이로 건사이트는 격추율을 크게 높인 것으로 평가되나 정확한 배수는 자료마다 다름(uncertain 참조) |
| 출처 | Wikipedia, 'Head-up display' — History/Origins 절 (https://en.wikipedia.org/wiki/Head-up_display) |

반사식 조준기는 조준용 레티클을 반투명 유리에 반사시켜 무한원에 맺히게 한다. 조종사가 표적과 조준선을 동시에, 초점 이동 없이 볼 수 있다는 것이 핵심이며 이것이 오늘날 광학 시스루 AR의 기본 원리 그대로다. 2차대전 중 자이로 건사이트가 여기에 기동 표적의 선행조준(lead)을 자동 계산해 움직이는 레티클을 더했다. 1940년대 초 TRE는 여기서 한 걸음 더 나아가 AI(공중요격) 레이더 화면의 상과 자이로 조준기 상을 야간전투기 풍방유리에 겹쳐 띄웠다. 세계 최초로 '센서가 만든 정보'를 실제 시야에 정합해 올린 사례다.

야간전투기 조종사는 레이더 화면을 보려면 어둠에 적응한 눈을 계기판 빛에 빼앗기고, 표적을 놓친다. '고개를 내리면 진다'는 이 문제는 전투 상황에만 존재하는 고유한 제약이었고, 기술이 준비돼서가 아니라 이 제약 때문에 중첩 표시가 발명됐다.

성공. 반사식 조준기는 2차대전 전 기간 모든 주요 공군이 채택했고, 그 광학 구조는 HUD를 거쳐 오늘날 AR 글라스의 컴바이너(combiner)로 이어진다.

### Blackburn Buccaneer 'Strike Sight' — 최초의 실용 HUD
| 항목 | 내용 |
| --- | --- |
| 주체 | 영국 해군 항공대(Royal Navy), Rank Cintel(생산), Elliott Flight Automation(Cintel 사업 인수 후 개량), 후신 GEC-Marconi Avionics → BAE Systems |
| 연도 | 1958년 (시제기 초도비행 4월 30일, 시스템 통합) / 1960년대 초 실전 배치 |
| 수치 | Mark III 포함 총 375기 생산; 시제기 초도비행 1958-04-30 |
| 출처 | Wikipedia, 'Head-up display' — 'The Blackburn Buccaneer... Rank Cintel... Elliott Flight Automation... 375 total units' (https://en.wikipedia.org/wiki/Head-up_display) |

고도·속도·폭격조준을 하나의 화면으로 통합해 조종사 시선 앞에 띄운 장치다. 별개의 계기 세 개를 읽고 머릿속에서 합치던 작업을 광학적으로 대신했다. BAE Systems는 이것을 '세계 최초의 실용 HUD'로 공식 주장한다. 유사 파생형이 1959년부터 English Electric Lightning에 미사일 공격 모드와 함께 장착됐다.

Buccaneer는 해면 30m 안팎 초저고도로 고속 진입해 폭탄을 던지는 기체다. 폭격 진입 구간이 수 초에 불과해, 계기판으로 시선을 내리는 순간 지형 충돌이나 조준 실패가 난다. 즉 '눈을 뗄 시간이 물리적으로 없다'는 임무 고유의 제약이 HUD를 강제했다.

성공. Mark III까지 총 375기가 생산됐고, 이후 서방 전투기의 표준 장비가 됐다.

### Klopfstein 표준 심볼로지와 HUD의 민간 확산
| 항목 | 내용 |
| --- | --- |
| 주체 | Gilbert Klopfstein(프랑스 시험조종사), 이후 민항기 제작사 및 항공사, Oldsmobile(GM) |
| 연도 | 1960년대 (표준 심볼로지) / 1975년 (계기착륙 HUD) / 1970년대 (민항 도입) / 1988년 (양산 자동차) |
| 수치 | 1958(군용 최초) → 1970년대(민항) → 1988(양산차): 군→민 확산에 약 30년 |
| 출처 | Wikipedia, 'Head-up display' — 'Gilbert Klopfstein created the first modern HUD... modern instrument-landing HUD developed in 1975... Oldsmobile Cutlass Supreme first production car with HUD in 1988' (https://en.wikipedia.org/wiki/Head-up_display) |

초기 HUD는 기종마다 기호가 달라 조종사가 기종을 옮기면 다시 배워야 했다. Klopfstein은 '최초의 현대적 HUD'로 평가되는 표준 심볼로지 체계를 만들어, 기호만 보고도 기체의 자세·비행경로·속도 추세를 읽을 수 있게 했다. 여기서 비행경로 벡터(flight path vector) 같은, 세계 좌표에 정합된 기호 개념이 정립된다. 1975년에는 계기착륙용 현대 HUD가 나왔고, 1970년대에 민항으로, 1988년에는 Oldsmobile Cutlass Supreme으로 최초의 양산차 HUD가 나왔다.

군용에서 민간으로 넘어간 동인은 안전이 아니라 경제였다. 저시정(안개) 상황에서 착륙을 포기하고 회항하면 항공사는 직접 비용을 물고, 취항 신뢰도가 떨어진다. HUD는 저시정 착륙 카테고리를 낮춰 결항·회항을 줄이는 수단으로 채택됐다.

성공했으나 확산은 느렸다. 군용 채택(1958)에서 민항 본격 채택까지 20년 이상 걸렸다. 표준화 이전의 기종별 심볼로지는 사실상 사멸했다.

### VTAS(Visual Target Acquisition System) — 서방 최초의 헬멧 조준 시스템, 그리고 그 사장
| 항목 | 내용 |
| --- | --- |
| 주체 | 미 해군, Honeywell Corporation |
| 연도 | 1969년 (F-4 팬텀 후기형 통합 시작) / 1970년대 초 (F-4J 시험) / 1974~78년 (ACEVAL/AIMVAL 평가) / 1970년대 말 사실상 폐기 |
| 수치 | F-4 후기형 통합 1969년 시작; ACEVAL/AIMVAL 1974~1978; 서방 공백기 약 20년 |
| 출처 | Wikipedia, 'Helmet-mounted display' / 'Helmet-mounted sight' — 'Honeywell... Visual Target Acquisition System... tested in the early 1970s on F-4J... during 1974-78 ACEVAL/AIMVAL trials' (https://en.wikipedia.org/wiki/Helmet-mounted_display) |

조종사 헬멧에 조준 레티클을 띄우고 헬멧의 방향을 추적해, 조종사가 '보는 곳'으로 미사일 탐색기를 돌려주는 장치다. 기수를 표적 쪽으로 돌리지 않고도(off-boresight) 조준할 수 있게 하는 것이 목적이었다. F-4J에서 시험됐고 1974~78년 미 공군·해군 합동 공중전 평가인 ACEVAL/AIMVAL에서 F-14·F-15와 함께 평가받아 오프보어사이트 조준 효과를 인정받았다.

근접 공중전에서 미사일을 쏘려면 기수를 표적에 맞춰야 했고, 그 기동 시간이 곧 피격 위험이었다. 베트남전에서 드러난 낮은 격추 교환비가 '보는 곳으로 쏘게 하라'는 요구를 만들었다.

실패(기술적 이유보다 체계 정합 실패). 헬멧은 작동했지만 당시 AIM-9 사이드와인더 탐색기의 탐색 범위가 헬멧이 지시하는 각도를 따라가지 못했다. 즉 입력장치만 앞서가고 무장이 못 따라온 전형적 사례다. 베트남 이후 예산 축소가 겹쳐 미국은 1990년대까지 약 20년간 헬멧 조준을 사실상 포기했고, 그 사이 소련이 앞서 나갔다.

### Sword of Damocles — 최초의 자세 추적 HMD, 부품은 군용 헬기에서 왔다
| 항목 | 내용 |
| --- | --- |
| 주체 | Ivan Sutherland(하버드대 전기공학 부교수), 학생 Bob Sproull·Quintin Foster·Danny Cohen 등 |
| 연도 | 1968년 |
| 수치 | 1968년; 와이어프레임 렌더링; 천장 현가식 |
| 출처 | Wikipedia, 'Ivan Sutherland' — 'the first head-mounted display that rendered images for the viewer's changing pose... a stock item used by U.S. military helicopter pilots to view video from cameras mounted on the helicopter's belly' (https://en.wikipedia.org/wiki/Ivan_Sutherland) |

사용자의 머리 자세 변화에 맞춰 영상을 다시 그려주는 최초의 머리 장착 디스플레이다. 와이어프레임 방 모형을 띄웠고, 장치가 무거워 천장에 매달았기 때문에 '다모클레스의 검'이라 불렸다. 중요한 사실은 여기 쓰인 소형 CRT 디스플레이가 연구용으로 새로 만든 것이 아니라, 미군 헬기 승무원이 기체 배면 카메라 영상을 보는 데 쓰던 기성 군용 부품이었다는 점이다.

학술 연구였지만 부품 조달이 군에 의존했다는 사실 자체가, 1960년대에 이 정도 소형 디스플레이를 만들 수요와 자금을 가진 곳이 군뿐이었음을 보여준다. AR/VR의 물질적 기반은 처음부터 군수였다.

성공(연구로서). 이후 모든 HMD 계보의 출발점으로 인용된다. 다만 상용화와는 무관했고, 실용 장치가 되기까지 다시 20년 이상 걸렸다.

### Tom Furness의 VCASS와 Super Cockpit 프로그램
| 항목 | 내용 |
| --- | --- |
| 주체 | Thomas A. Furness III, 미 공군 Armstrong Aerospace Medical Research Laboratory 인간공학부 시각표시장치과장, Wright-Patterson AFB (오하이오) |
| 연도 | 1966년 9월~1989년 (Wright-Patterson 재직) / 1986년 (Super Cockpit 프로그램 조직) / 1989년 (HITLab 설립) |
| 수치 | 공군 재직 1966.09~1989 (23년); Super Cockpit 조직 1986; HITLab 설립 1989 |
| 출처 | HIT Lab, University of Washington — Tom Furness 인물 페이지 (https://www.hitl.washington.edu/people/tfurness/); Wikipedia, 'Thomas A. Furness III' |

조종석 계기가 너무 많아져 조종사가 정보를 처리하지 못하는 상태를 '정보 병목'으로 규정하고, 계기판 자체를 없애고 조종사 주위에 3차원 가상 정보 공간을 만들자는 발상이었다. 머리·시선·음성을 입력으로 쓰고 헬멧을 출력으로 쓰는 '시각 결합(visually-coupled) 시스템'을 연구했다. 1986년 Super Cockpit 프로그램을 조직해 프로그램 디렉터를 맡았고 1989년 퇴직할 때까지 이끌었다.

1970~80년대 전투기는 레이더·전자전·항법·무장 정보가 폭증했는데 조종석 면적은 늘릴 수 없었다. '계기를 더 달 수 없다'는 물리적 한계가 문제였고, 그 답으로 나온 것이 계기를 공간에 띄우는 것이었다. 기술이 준비된 게 아니라 좌석 크기가 한계였다.

프로그램 자체로는 전투기에 그대로 실장되지 못했다. 그러나 남긴 것이 훨씬 크다. Furness는 1989년 가을 워싱턴대로 옮겨 HIT Lab(Human Interface Technology Lab)을 세웠고, 여기서 군사 기술과 인간공학 방법론이 민간 VR/AR 연구로 흘러나갔다. 2018년 VR/AR 50년 공로로 최초의 평생공로상을 받았고 IEEE 펠로로 선출됐다.

### IHADSS — AH-64 아파치의 통합 헬멧 표시·조준 시스템
| 항목 | 내용 |
| --- | --- |
| 주체 | Honeywell(M142), 미 육군, AH-64 아파치; 이탈리아 Agusta A129 Mangusta에도 채택 |
| 연도 | 1985년 (실전 배치) |
| 수치 | 시야 40°×30°; 단안 비디오+기호 표시; 1985년 배치 |
| 출처 | Wikipedia, 'Helmet-mounted display' — 'Fielded: 1985... Honeywell (M142)... 40°-by-30° field of view, video-with-symbology monocular display' (https://en.wikipedia.org/wiki/Helmet-mounted_display). 인체 영향은 미 육군 항공의학연구소(USAARL) 다수 보고서 (구체 수치 uncertain) |

단안(한쪽 눈) CRT를 눈앞에 두고 40°×30° 시야에 영상과 기호를 겹쳐 보여준다. 헬멧에 적외선 발광체를 달아 머리 방향을 추적하고, 그 방향으로 기수 아래 열영상 카메라(PNVS)를 종속(slave)시킨다. 조종사가 고개를 돌리면 카메라가 따라 돌고, 그 열영상이 한쪽 눈에 들어온다. 조종사는 사실상 기체 바깥의 센서로 밤을 보며 지형 추수(nap-of-the-earth) 비행을 한다.

공격헬기의 생존 방식은 지형에 붙어 낮게 나는 것인데, 밤에 그렇게 날려면 조종사가 어둠 속 지형을 봐야 한다. 야간투시경은 시야가 좁고 고개와 무기 조준을 따로 놀게 만든다. '밤에, 나무 높이로, 동시에 조준까지' — 이 세 가지를 한꺼번에 요구한 것은 공격헬기뿐이었다.

성공했으나 대가가 컸다. 40년 가까이 현역이지만, 한쪽 눈만 영상을 받는 단안 구조 때문에 시각 경합(binocular rivalry)과 시각 우위(visual dominance) 문제가 보고됐고, 아파치 조종사의 두통·안정피로·방향감각 이상 호소가 다수의 항공의학 연구 주제가 됐다. AR 헬멧이 인체에 부과하는 비용을 최초로 대규모로 드러낸 사례다.

### 남아공 V3A와 소련 Shchel-3UM/R-73 — 서방이 20년 뒤처진 사건
| 항목 | 내용 |
| --- | --- |
| 주체 | 남아공 공군(Mirage IIICZ, Mirage F1AZ) + Armscor V3A 미사일; 소련 MiG-29·Su-27 + Shchel-3UM(ZSh-5/ZSh-7 헬멧) + R-73(NATO명 AA-11 Archer) |
| 연도 | 1975년 (남아공 Mirage 통합) / 1981년 (Shchel-3UM 설계) / 1985년 (MiG-29 배치) / 1990~91년 (통일 후 서방이 구 동독 MiG-29 접근) |
| 수치 | Shchel-3UM 설계 1981; MiG-29 배치 1985; 서방 만회 시작 1990~ |
| 출처 | Wikipedia, 'Helmet-mounted sight' / 'Helmet-mounted display' — 'several nations responded with programs to counter the MiG-29/HMD/R-73 ... principally through access to former East German MiG-29s' (https://en.wikipedia.org/wiki/Helmet-mounted_sight) |

헬멧 조준 시스템과 고기동 단거리 미사일을 한 세트로 묶은 조합이다. 조종사가 고개를 돌려 표적을 보기만 하면 미사일 탐색기가 그쪽으로 돌아가 발사할 수 있다. 서방이 VTAS를 버린 사이 소련은 이 조합을 완성했다. 남아공은 1975년 Mirage에 헬멧 조준기와 V3A를 통합해 앙골라 상공 실전에서 오프보어사이트 공격 효과를 입증했고, 이것이 각국 개발을 자극했다는 것이 통설이다.

근접전에서 기수를 돌리는 시간을 없애는 것이 곧 생존율이었다. 소련은 서방보다 기체 성능 열세를 '조종사의 시선'이라는 인터페이스로 상쇄하려 했다. 하드웨어 격차를 인터페이스로 뒤집으려 한 선택이다.

소련 쪽의 성공이자 서방의 실패. 1990년 독일 통일로 서방이 구 동독 공군의 MiG-29를 직접 시험 비행하면서 R-73 + 헬멧 조합의 실효성이 드러났고, 모의 근접전에서 F-16 등 서방 전투기가 일방적으로 불리하다는 결과가 나왔다. 이 충격이 1990년대 내내 JHMCS, ASRAAM, AIM-9X, IRIS-T 같은 만회 프로그램을 촉발했다.

### DASH — 이스라엘 Elbit의 헬멧 내장형 표시장치
| 항목 | 내용 |
| --- | --- |
| 주체 | Elbit Systems(이스라엘), 이스라엘 공군 F-15·F-16 |
| 연도 | 1980년대 중반 (약 1986년 생산 개시) / 1990년대 초 (GEN III, 실전 운용) |
| 수치 | 생산 개시 약 1986; GEN III 1990년대 초; DASH IV 현역 |
| 출처 | Wikipedia, 'Helmet-mounted display' — 'Elbit Systems... entered production ~1986; GEN III variant early-to-mid 1990s... wholly embedded within helmet; uses CRT with spherical visor; electromagnetic position sensing' (https://en.wikipedia.org/wiki/Helmet-mounted_display) |

이전 헬멧 조준기가 기존 헬멧에 장치를 덧붙이는 방식이었던 데 반해, DASH는 표시장치를 헬멧 구조 안에 완전히 통합했다. CRT와 구면 바이저를 결합하고 전자기식 위치 센서로 머리 방향을 측정한다. F/A-18, F-5에서도 인증됐고 MiG-21 개량형에 수출됐다. 최신형 DASH IV는 인도 HAL Tejas에 통합돼 있다.

이스라엘 공군은 다수 대 소수의 공중전을 전제했고, 첫 발을 먼저 쏘는 능력이 절대적이었다. 또 Python 4 같은 고기동 미사일을 자체 개발하고 있었기 때문에, 미사일과 헬멧을 함께 설계할 수 있는 드문 위치에 있었다.

성공. 1990년대 초 실전 운용에 들어가 Python 4와 짝을 이뤘고, 이 기술 자산이 뒤에 미국 JHMCS의 절반(Elbit 지분)을 이룬다. 즉 미국은 자국 VTAS를 버린 대가로 이스라엘 기술을 사와야 했다.

### JHMCS(Joint Helmet-Mounted Cueing System) — 미국의 만회
| 항목 | 내용 |
| --- | --- |
| 주체 | Vision Systems International(VSI, Rockwell Collins와 Elbit의 합작사), 미 공군·해군; DASH III와 Kaiser Agile Eye 기술 결합 |
| 연도 | 1990년 (개발 착수) / FY2002 (저율초도생산) / 2003년 11월 (미 공군 최초 배치) |
| 수치 | 개발 착수 1990; LRIP FY2002; 최초 배치 2003.11 (12·19전투비행대, Elmendorf AFB); AIM-9X와 좌우 ±80° 표적 지정; 플랫폼 간 95% 공통 |
| 출처 | Wikipedia, 'Helmet-mounted display' — 'Vision Systems International (Rockwell Collins/Elbit joint venture)... Fielded: November 2003 (USAF)... 12th and 19th Fighter Squadrons at Elmendorf AFB... effective target designation up to 80 degrees either side' (https://en.wikipedia.org/wiki/Helmet-mounted_display) |

조종사 바이저에 단색 기호를 투사하고 머리 방향을 추적해, 시선을 무장·레이더·센서의 조준 입력으로 쓰는 시스템이다. AIM-9X와 결합하면 기수 기준 좌우 최대 80°까지 표적 지정이 가능하다. FLIR/IRST 영상을 래스터로 띄워 야간 운용도 지원한다. F/A-18A++/C/D/E/F, F-15C/D/E 계열, F-16 Block 40/50/60/70에 장착되며 플랫폼 간 약 95% 공통 설계다.

1990년 미국이 ASRAAM(공동 단거리 미사일) 사업에서 이탈하면서, 구 동독 MiG-29로 확인된 헬멧+고기동 미사일 격차를 스스로 메워야 했다. 순수한 위협 대응이었다.

성공. 2003년 11월 알래스카 엘멘도르프 공군기지의 제12·19전투비행대에 최초 배치됐고, 같은 해 해군 F/A-18E/F에도 들어갔다. 2009년 3월 호주 공군 F/A-18이 JHMCS로 날개선 뒤쪽 표적에 ASRAAM '발사 후 락온'을 시연했다. 다만 초기형은 단색 기호 위주였고, 야간·완전 영상 표시는 F-35 세대로 넘어가서야 해결된다.

### F-35 HMDS Gen II/Gen III와 DAS 투시 — HUD를 없애고 전부 헬멧에 넣다
| 항목 | 내용 |
| --- | --- |
| 주체 | Vision Systems International + Helmet Integrated Systems Ltd.(주계약), Lockheed Martin, 대체안은 BAE Systems(중단); DAS는 Northrop Grumman(AN/AAQ-37), 2023년 Lot 15부터 Raytheon |
| 연도 | 2011년 (대체 헬멧 사업 착수) / 2013년 10월 (대체안 중단) / 2014년 7월 (운용 준비 선언) / 2016년 (Gen III, LRIP Lot 7) |
| 수치 | 헬멧 단가 약 US$400,000; DAS 적외선 센서 6개; 탄도미사일 추적 1,300km(800마일) 초과 시연; 대체 헬멧 중단 2013년 10월; Gen III LRIP Lot 7 (2016) |
| 출처 | Wikipedia, 'Lockheed Martin F-35 Lightning II' — 'Each helmet costs $400,000... vibration, jitter, night-vision and sensor display problems... development on the alternative HMDS was halted in October 2013' (https://en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II); Wikipedia, 'AN/AAQ-37 Distributed Aperture System' (https://en.wikipedia.org/wiki/AN/AAQ-37_Distributed_Aperture_System) |

F-35는 50년 만에 HUD가 없는 전투기다. 모든 비행·전술 정보가 헬멧 바이저에 투사된다. 여기에 기체 외피에 박힌 6개의 적외선 센서(AN/AAQ-37 분산개구시스템, DAS)가 전방위 360° 영상을 합성해 헬멧으로 보낸다. 조종사가 발밑을 내려다보면 조종석 바닥과 기체 구조를 '투시하고' 그 아래 지형이 보인다. DAS는 동시에 미사일 탐지·발사점 추적을 수행하며, 시험에서 1,300km(800마일) 이상 거리의 탄도미사일을 탐지·추적했다. Gen III는 야간투시 카메라 개선, 새 액정 표시장치, 자동 정렬, 소프트웨어 개선을 담았다.

스텔스기는 외부 형상을 깨는 장비를 달 수 없고, 조종사 혼자서 다수 센서 융합 결과를 처리해야 한다. 계기판과 HUD를 동시에 두면 공간도 시선도 부족하다. '기체 형상을 보존하면서 조종사에게 전방위 인식을 준다'는 요구가 HUD 제거라는 극단적 선택을 낳았다.

성공했지만 고통스러웠다. Gen II는 진동(jitter), 지연, 야간 영상 품질, 센서 표시 결함을 겪었고, 특히 어두운 야간 항모 착함에서 표시 밝기가 밑바닥 수준의 배경광을 덮어버리는 이른바 '그린 글로우(green glow)' 문제가 심각했다. Lockheed Martin과 Elbit은 2011년 야간투시경 기반 대체 헬멧 사양을 만들고 BAE Systems를 선정했으나, 2013년 10월 대체 사업을 중단하고 원래 HMDS 개량으로 갔다. 2014년 7월 완전 운용 가능 선언, 2016년 Gen III 도입. 헬멧 자체가 무거워 저체중 조종사의 사출 시 목 부상 위험이 제기됐다. 단가는 1개당 약 40만 달러다.

### Land Warrior — 보병용 AR의 첫 대형 실패
| 항목 | 내용 |
| --- | --- |
| 주체 | 미 육군; General Electric(초기 시제), Hughes Aerospace(후에 Raytheon), Motorola(무전), Exponent Inc.(1999년 재편), General Dynamics(2003년 LW-SI 계약) |
| 연도 | 1989년 (시작) / 1994년 (정식 명명) / 2007년 2월 (취소) / 2007년 7월 (부분 부활) / 2007년 5월~2008년 6월 (이라크 실전 투입) |
| 수치 | 이라크 투입 229세트 (4-9 보병연대, 2007.05~2008.06); 전투조끼 배터리만 최대 1.1kg(2.5lb); 후속 Nett Warrior 3lb(1.4kg)로 경량화; 취소 2007년 2월 |
| 출처 | Wikipedia, 'Land Warrior' — '229 Land Warrior ensembles were deployed by the 4th Battalion, 9th Infantry Regiment to Iraq from May 2007 to June 2008... cancelled February 2007... limited resources, and issues with the overall weight' (https://en.wikipedia.org/wiki/Land_Warrior) |

보병 개인에게 헬멧 장착 OLED 디스플레이, 무전기, 컴퓨터, 소총 장착 카메라를 주는 체계다. 디지털 지도, 아군 위치, 소총 카메라 영상을 눈앞에 띄워 '모서리 너머를 보고 쏘게' 하는 것이 목표였다. 사실상 전투기 조종석의 정보 통합을 보병 몸에 옮겨놓으려는 시도다.

걸프전 이후 지휘통제망이 차량·항공기 수준까지 디지털화됐는데 정작 최말단 보병만 아날로그로 남았다는 '마지막 전술 마일(last tactical mile)' 문제가 동인이었다. 아군 오인사격(fratricide) 감소도 핵심 명분이었다.

실패. 무게와 예산이 원인이었다. 2007년 2월 취소됐고(허리케인 카트리나 구호로 예산이 전용된 것도 요인), 같은 해 7월 부분 부활했다. 실전에서는 제4대대 9보병연대가 229세트를 2007년 5월부터 2008년 6월까지 이라크에 가져갔다. 병사들은 무게와 배터리 부담을 문제 삼았고, 일부는 장비를 벗어두고 나갔다. 후속 Nett Warrior는 헬멧 디스플레이를 포기하고 손에 드는 스마트폰형 단말로 바꾸며 3파운드(1.4kg)까지 줄였다 — AR을 포기한 것이 해법이었다는 점이 이 실패의 핵심 교훈이다.

### IVAS(Integrated Visual Augmentation System) — 홀로렌즈 기반 육군 AR의 좌초
| 항목 | 내용 |
| --- | --- |
| 주체 | 미 육군, Microsoft(HoloLens 2 기반), 이후 Anduril Industries |
| 연도 | 2018년 9월 25일 (개발 승인) / 2018년 11월 (마이크로소프트 개발 계약) / 2021년 3월 26일 (양산 계약) / 2022~2024년 (시험 실패와 예산 삭감) / 2025년 (전환) |
| 수치 | 계약 상한 약 US$21.88B (2021.03.26, 10년); 계획 도입 최대 121,000대(120,000대 이상); 추정 단가 약 US$29,205/대; 2022년 9월 초도 5,000대 인수; 의회 삭감 US$230M(2020.12, 요구액 US$1.1B 중); 유보 약 US$400M(2022.03); IVAS 1.2용 US$95M / 280대(2023.09); 무게 3.4lb(1.5kg), 목표 2.9lb(1.3kg); 시야 70°→60° |
| 출처 | Wikipedia, 'Integrated Visual Augmentation System' (https://en.wikipedia.org/wiki/Integrated_Visual_Augmentation_System); DoD Inspector General 감사 보고 2022-04-22; DOT&E Annual Report 2023-01 |

마이크로소프트 HoloLens 2를 군용으로 바꾼 헤드셋이다. 열영상·야간투시, 지도, 아군 표시, 무기 조준경 영상 중계, 가상 훈련을 하나의 바이저에 통합해 '싸우고, 시연하고, 훈련한다'는 구호를 내걸었다. 육군은 근접전투부대용으로 12만 대 이상(최대 121,000대 규모) 도입을 계획했다.

Land Warrior와 같은 문제 — 최말단 보병의 상황인식 — 가 20년 뒤에도 그대로였고, 이번에는 상용 AR 기기가 성숙했으니 상용품을 사다 쓰면 된다고 판단했다. 즉 '군이 스스로 만들지 않고 소비자 기술을 가져온다'는 조달 철학의 실험이기도 했다.

대규모 실패·재시작. 2020년 12월 의회는 11억 달러 요구액에서 2.3억 달러를 삭감했고, 2022년 3월에는 초기 운용시험 완료 전까지 약 4억 달러를 유보했다. 2022년 4월 22일 국방부 감사관실(DoD IG)은 병사들이 실제로 쓰지 않으면 예산이 낭비된다고 경고하며 육군이 사용자 만족도를 제대로 측정하지 않았다고 지적했다. 2023년 1월 DOT&E(작전시험평가국) 보고서는 병사들이 IVAS를 쓸 때보다 기존 장비를 쓸 때 임무 수행이 더 나았으며, 대다수가 두통·안정피로·구토 등 신체 이상과 다수의 기술적 결함을 보고했다고 밝혔다. 바이저 발광이 수백 미터 밖에서 보인다는 치명적 지적도 나왔다. 무게는 1.5kg(3.4lb)로 목표치 1.3kg(2.9lb)를 넘었고 시야는 70°에서 60°로 축소됐다. 2021년 목표였던 야전 배치는 2025년으로 밀렸다.

### Anduril로의 이관과 그 이후 — 군용 AR의 재편
| 항목 | 내용 |
| --- | --- |
| 주체 | Anduril Industries, Microsoft, 미 육군 |
| 연도 | 2025년 2월 11일 (Microsoft → Anduril 이관 발표) |
| 수치 | 이관 발표 2025년 2월 11일; 육군 계획 최대 121,000대; 본격 양산은 2025년 중 고강도 실전시험 통과 조건부 |
| 출처 | Wikipedia, 'Anduril Industries' — 'February 11, 2025... Anduril took over development and production of IVAS from Microsoft... The Army planned to order as many as 121,000 of the devices but said the goggles had to pass high-stress operational combat tests later in the year before full production would occur.' (https://en.wikipedia.org/wiki/Anduril_Industries) |

마이크로소프트가 IVAS의 생산·하드웨어/소프트웨어 향후 개발·납기 관리 전체를 Anduril에 넘겼다. 클라우드는 Azure에 남기고 기기와 소프트웨어는 방산업체가 맡는 구조다. 육군은 최대 121,000대 발주 의사를 유지하되, 그해 안에 고강도 실전 운용시험을 통과해야 본격 양산에 들어간다는 조건을 달았다.

소비자 기술 기업이 만든 AR 기기가 군 요구(무게, 전력, 내구성, 야간 은폐, 급조 정비)를 충족하지 못한다는 것이 2022~2024년 시험으로 드러났기 때문이다. 문제는 광학이나 렌더링이 아니라 '군용 체계로서의 성립'이었고, 그래서 사업자가 바뀌었다.

진행 중이며 확정적으로 말하기 이르다. 이관 자체는 IVAS라는 이름의 원래 계획(홀로렌즈 기반 12만 대 배치)이 사실상 소멸했음을 뜻한다. 이후 육군은 사업을 Soldier Borne Mission Command(SBMC) 계열로 재편하고 Anduril이 EagleEye라는 자체 혼합현실 체계를 내놓은 것으로 알려져 있으나, 계약 금액·수량·일정은 이 조사에서 1차 출처로 확인하지 못했다(uncertain 참조).

#### 검증에서 잡힌 정정
- F-35 HMDS '2014년 7월 (운용 준비 선언)' — 인용 출처(Wikipedia 'Lockheed Martin F-35 Lightning II')에 이런 선언은 없다. 해당 문서는 2011년 대체안 착수, 2013년 10월 대체안 중단, 2016년 Gen III(LRIP Lot 7)만 기술한다. 2014년 7월 날짜의 근거를 제시하지 못하면 삭제해야 한다.
- F-35 HMDS 주계약자를 'Vision Systems International + Helmet Integrated Systems Ltd.(주계약)'으로 적은 것은 귀속 오기다. 인용 출처가 명시하는 주체는 VSI(및 사양 공동작성 Elbit, 대체안 BAE Systems)이며 Helmet Integrated Systems Ltd.는 등장하지 않는다. 헬멧 쉘 공급사를 주계약자로 승격시킨 서술이다.
- '그린 글로우'를 Gen II의 결함으로 귀속한 것은 세대 오기다. 야간 항모 착함 시 표시 밝기가 저광량 배경을 덮는 문제(green glow)는 Gen III 헬멧과 F-35C 해상 시험에서 DOT&E가 보고한 사안이며, 인용된 F-35 위키 문서는 green glow를 아예 언급하지 않는다. Gen II의 문서화된 결함은 진동/지터·야간투시·센서 표시 문제까지다.
- 'Elliott이 Mark III까지 375기를 만들었다' — 출처는 'Production units were built by Rank Cintel... The Cintel HUD business was taken over by Elliott Flight Automation... a total of 375 systems made'이다. 375기는 Rank Cintel 생산분을 포함한 사업 전체 누계이지 Elliott의 생산량이 아니다.
- HUD 군→민 확산 기간이 항목 내부에서 모순된다. 수치란은 '1958→1970년대→1988, 약 30년'이라 쓰고 결과란은 '민항 본격 채택까지 20년 이상 걸렸다'고 쓴다. 출처는 'In the 1970s, the HUD was introduced to commercial aviation'뿐이므로 1958년 기준 12~21년이며, '20년 이상'은 상한을 임의로 취한 과장이다.
- VTAS 서술이 시험 플랫폼을 혼동한다. 본문은 'F-4J에 달았고 1974~78년 ACEVAL/AIMVAL에서 호평을 받았'다고 읽히지만, 인용 출처는 'flown in early 1970s in F-4J'와 '1974–78 ACEVAL/AIMVAL on U.S. F-14 and F-15 fighters'를 구분한다. ACEVAL/AIMVAL 평가 기체는 F-14·F-15다.
- TRE 항목의 '1940년대 초 (TRE 실전 적용)' 및 본문의 '실전에 들어왔다' — 출처는 1942년 10월에 레이더상과 GGS Mk.II 상을 풍방유리에 성공적으로 결합했다는 기술 성과만 적고 있으며, 작전 배치·실전 투입 여부는 언급하지 않는다. '실전 적용'은 근거 없는 격상이다.
- '반사식 조준기는 2차대전 전 기간 모든 주요 공군이 채택했고' — 채택은 전쟁 기간에 걸쳐 점진적으로 이뤄졌으며, 개전 초 상당수 기체는 여전히 링·비드 조준기를 썼다. '전 기간 모든 주요 공군'은 출처가 뒷받침하지 않는 전칭 주장이다.
- Klopfstein에 대한 '기종 간 이식 가능한 표준 심볼로지'라는 수식은 출처 범위를 넘는다. 원문은 'created the first modern HUD and a standardized system of HUD symbols'일 뿐, 기종 간 이식성(portability)을 명시하지 않는다.
- DASH GEN III 시점을 '1990년대 초'로 좁힌 것은 출처와 어긋난다. 원문은 'entered production during the early to mid-1990s'로 1990년대 초~중반 구간을 제시한다.
- DAS의 '탄도미사일 추적 1,300km 초과'는 수치 자체는 맞으나 맥락이 빠졌다. 출처는 2011년 군 연습 중의 탐지·추적 시연이라고 명시하며, 상시 운용 성능으로 읽히게 제시하면 과장이 된다.
- IHADSS '40년 가까이 현역' — 1985년 배치 기준 2026년 현재 41년으로, 이미 40년을 넘었다. '40년 넘게'가 맞는 표현이다.
- 연도 오류 — "MiG-29가 1985년 배치": MiG-29는 1983년 8월 소련 공군 취역(위키백과 MiG-29 인포박스 및 본문 "entered service with the Soviet Air Forces in 1983"). 글은 HMD 문서의 "1985년 HMD+고오프보어사이트 무장과 함께 fielded"를 기체 배치 연도로 바꿔 적었다. 2년 오차가 "서방 20년 뒤처짐" 계산의 기준점이다.
- 연도·제원 누락 — "1981년 설계된 Shchel-3UM과 R-73": R-73 취역은 1984년이다. 또한 R-73 표준형 오프보어사이트는 ±40°(수출형 R-73E ±45°)로, 글이 암시하는 압도적 각도 우위와 다르다. 글은 이 수치를 한 번도 제시하지 않는다.
- 인과 날조 — "당시 AIM-9의 오프보어사이트 능력이 헬멧을 따라가지 못해 서방에서 20년 가까이 사장됐다" / "입력장치만 앞서가고 무장이 못 따라온 전형적 사례": AIM-9 위키백과는 AIM-9G의 SEAM이 "allowed the slaving of the optics to a radar or helmet sight"라고 명시한다. 무장은 헬멧 슬레이빙을 지원했다. 인용된 HMD 문서는 VTAS 미확대의 이유를 적지 않는다 — 글이 없는 메커니즘을 창작했다.
- 출처와 정반대 평결 — "VTAS 결과: 실패 ... 1970년대 말 사실상 폐기": 인용된 HMD 문서는 VTAS가 "received praise for its effectiveness in targeting off-boresight missiles"이며 1969년부터 후기형 해군 F-4 팬텀에 AIM-9와 함께 통합됐다고 적는다. 실패도 폐기도 출처에 없다.
- 귀속 오류 — "Rank Cintel이 제작하고 Elliott이 Mark III까지 375기를 만들었다": 원문은 "Production units were built by Rank Cintel", Elliott은 이후 사업을 인수해 Mark III로 개량, "375 systems"는 **양쪽 합계**다. 더 중요한 누락은 설계 주체다 — 원문은 **Royal Aircraft Establishment가 장비를 설계**했다고 적는데, 글은 설계 기관을 인과 사슬에서 통째로 삭제했다.
- 과장된 최초 주장 — "Blackburn Buccaneer의 Strike Sight가 최초의 실용 HUD로 꼽힌다": 인용 문서는 그렇게 말하지 않는다. "the earliest usage of the term 'head-up-display'"라고만 적는다. 같은 문서가 **1955년 미 해군 ONR의 HUD 목업**을 Buccaneer보다 먼저 기술한다(글은 이를 누락). 또 Blackburn Buccaneer 위키백과 문서에는 'Strike Sight'도, RAE도, 최초 HUD 주장도 없다.
- 배치 연도 — "1960년대 초 실전 배치": Buccaneer S.1의 함대항공대(FAA) 비행대 취역은 1963년 1월이다. 또 Buccaneer 총 생산은 시제기 2기 포함 211기이므로, "375기"는 기체 수로 읽힐 수 없다(글의 '기' 표기가 이를 혼동시킨다).
- 출처 강도 왜곡 — "1940년대 초 (TRE 실전 적용)" 및 "'중첩 정보'라는 발상이 실전에 들어왔다": 원문은 TRE가 1942년 10월 레이더 영상과 자이로 건사이트 투영을 풍방유리에 결합하는 것을 "experimented with"했다고만 적는다. 실전 적용(operational deployment)은 출처에 없다.
- 무근거 절대 진술 — "반사식 조준기는 2차대전 전 기간 모든 주요 공군이 채택했고, 그 광학 구조는 HUD를 거쳐 오늘날 AR 글라스의 컴바이너로 이어진다": '모든 주요 공군'도, AR 글라스 컴바이너로의 연속성도 인용 출처에 없다. 현대 AR 글라스는 대부분 회절/반사형 도파관(waveguide)을 쓰며 Grubb식 반투과 평판 컴바이너의 직계가 아니다. 목적론적 서사를 출처 없이 붙였다.
- 시대착오적 기업 귀속 — "Vision Systems International(VSI, Rockwell Collins와 Elbit의 합작사)": VSI는 **Kaiser Electronics**와 Elbit의 합작사로 출발했고 Rockwell Collins는 나중에 Kaiser를 인수했다. 인용 출처조차 괄호로 "(Kaiser Electronics is now owned by Rockwell Collins)"라고 단서를 달았는데, 글은 그 단서를 지우고 1990년대 사건에 현재의 사명을 소급 적용했다.
- 인과 누락 — "JHMCS 1990년 개발 착수 / 미국의 만회": 인용 문서의 실제 인과는 "미국이 ASRAAM에서 철수(withdrawal from ASRAAM)하고 대신 AIM-9X와 JHMCS 개발에 1990년 자금을 댔다"이다. ASRAAM이라는 분기점이 글에 없다. 더욱이 글이 성공 증거로 든 2009년 3월 RAAF F/A-18 사격은 AIM-9X가 아니라 **ASRAAM** 발사였다("a successful 'Lock on After Launch' firing of an ASRAAM").
- 인용 출처에 없는 주장 — IHADSS의 "시각 경합(binocular rivalry)과 시각 우위(visual dominance) 문제가 보고됐고, 아파치 조종사의 [건강 영향]": 인용된 HMD 문서에는 이 내용이 전혀 없다(40°×30° 단안 스펙만 있음). USAARL '다수 보고서'라는 뭉뚱그린 귀속만 있고 보고서명·연도·수치가 없어 검증 불가능한 인용이다.
- 수치 오용 및 자기모순 — IVAS "추정 단가 약 US$29,205/대": 위키백과 원문에서 이 금액은 "IVAS attached to any helmet ... could optionally work independently of the aircraft when the crew dismounts"라는 특정 변형에 붙은 수치이지 12만 대 보병 사업의 단가가 아니다. 게다가 글이 나란히 적은 숫자끼리 충돌한다 — $21.88B ÷ 120,000 ≈ 18.2만 달러/대인데, $29,205 × 120,000 ≈ 35억 달러로 약 6배 차이다. 글은 두 수치를 검증 없이 병렬 배치했다.
- 수량 출처 충돌 은폐 — "계획 도입 최대 121,000대(120,000대 이상)": IVAS 문서는 "Over 40,000 sets were planned to be issued"와 "at least 120,000 members of the Army Close Combat Force" 두 가지를 동시에 적고, 121,000은 Anduril 문서에만 나온다. 서로 다른 세 숫자를 하나의 일관된 계획처럼 제시했다.
- 강한 프레이밍 채택 — "2025년 2월 11일 Microsoft → Anduril 이관" 및 "IVAS라는 이름의 원래 계획이 사실상 소멸": 두 위키백과 문서가 서로 다르게 적는다. IVAS 문서는 "From February 2025 Anduril Industries **was to partner with** Microsoft"(협력), Anduril 문서는 "took over development and production"(인수)이다. 글은 강한 쪽만 골라 확정 서술하고 '소멸'이라는 판정까지 덧붙였다.
- 인용 출처가 뒷받침하지 않는 프로그램명 — "Tom Furness의 VCASS와 Super Cockpit 프로그램": 인용된 HIT Lab 인물 페이지에는 **VCASS가 전혀 등장하지 않는다.** 해당 페이지가 확인해 주는 것은 직함(Chief of the Visual Display Systems Branch, Human Engineering Division, Armstrong Aerospace Medical Research Laboratory), Super Cockpit 조직 1986년, UW 합류 1989년 9월뿐이다.
- 연대 모순 의심 — "1975년 남아공 Mirage 통합 V3A + 헬멧 조준기": 근거는 HMD 문서의 미출처 한 문장뿐인데, Mirage F1AZ는 1975~1976년에 인도가 시작됐고 SAAF Mirage F1의 실전 투입은 1978년 11월(F1CZ, 남서아프리카)부터다. 인도가 막 시작된 기체에 자체 개발 헬멧 조준기가 1975년에 통합·운용됐다는 서술은 연대상 무리다. 통상 SAAF 헬멧 조준기는 후기의 V3B Kukri와 짝지어 논의된다.
- 인과 오귀속 — Land Warrior "취소(2007.02)... 허리케인 카트리나 구호로 예산이 전용된 것도 요인": 원문은 취소 사유로 "limited resources, and issues with the overall weight of the system"만 들고, 카트리나 언급은 **컴퓨터 하위체계 개발**에 한정된 별개 문장이다("Prior to the project's cancellation (when project funds were moved to Hurricane Katrina relief)"). 글은 국소적 사실을 취소의 원인으로 승격시켰다.
- (외 21건)

## medical
항목 14개 · 검증 정정 지적 41건

> 의료는 AR을 가장 먼저 받아들인 분야였다. 기술이 준비돼서가 아니라, 문제가 먼저 있었기 때문이다. 1986년 다트머스의 David Roberts는 CT 영상을 수술 현미경 접안렌즈에 광학적으로 겹쳐 넣었다(J Neurosurg, 656회 인용). 두개골을 열면 종양은 보이지 않고, 외과의는 자기 기구가 어디 있는지 모른 채 전진해야 했다. 1992년 UNC Chapel Hill의 Bajura·Fuchs·Ohbuchi는 초음파 영상을 임신부의 배 '안쪽'에 정합해 넣어, AR이라는 용어가 정착하기도 전에 그 개념을 실증했다(SIGGRAPH '92, 278회 인용). 1996년 MIT Grimson의 자동 정합(211회)이 뒤를 이었고, Brainlab과 StealthStation이 내비게이션을 상품으로 만들었다. 그러나 AR 자체는 20년 가까이 연구실을 벗어나지 못했다. 원인은 정합이었다. Nimsky는 개두 후 피질이 최대 24mm 밀린다고 보고했고(2000), 간 복강경 AR의 정합 오차는 14.0mm로 "수술 안내에는 너무 부정확"하다는 판정을 받았다(Prevost 2020). 움직이지 않는 뼈에서만 AR이 성립한다는 사실을 확인하는 데 20년이 걸린 셈이다. 2013~2015년 Google Glass 열풍은 1시간 미만의 배터리, 720p 화질, 루페 비호환, 환자정보 보호 문제로 소멸했다. 전환점은 2018년 Novarad OpenSight(K172418), 그리고 2019년 12월 20일 Augmedics xvision(K190929)이었다. FDA는 이를 위해 'Orthopedic Augmented Reality'(제품코드 SBF)를 신설했고, 2025년까지 35건이 그 코드로 통과했다. 척추 나사 정확도는 1,259개 메타분석에서 97.2%. 의료 AR은 척추와 관절이라는 좁은 문으로만 실용화됐다.


### 프레임리스 정위수술 + 수술 현미경 영상 중첩 (세계 최초의 수술 AR)
| 항목 | 내용 |
| --- | --- |
| 주체 | David W. Roberts, John W. Strohbehn, J. Hatch, W. Murray, H. Kettenberger — Dartmouth-Hitchcock Medical Center |
| 연도 | 1986 (발표·임상 적용 동시) |
| 수치 | 1986년 J Neurosurg 발표, Semantic Scholar 기준 피인용 656회. 초음파 거리측정 기반 추적. |
| 출처 | Roberts DW, Strohbehn JW, Hatch JF, Murray W, Kettenberger H. "A frameless stereotaxic integration of computerized tomographic imaging and the operating microscope." Journal of Neurosurgery, 1986. 피인용 656 (Semantic Scholar API 조회). |

초음파 방식 3D 위치추적기로 수술 현미경의 위치·자세를 실시간 측정하고, 그 시야에 해당하는 CT 단면 윤곽을 현미경 접안렌즈 광로에 반투과 거울로 투영해 넣었다. 수술자가 화면을 따로 볼 필요 없이 실제 뇌 표면 위에 종양 경계선이 겹쳐 보였다. 정위 프레임(stereotactic frame)을 환자 머리에 나사로 고정하지 않아도 되는 '프레임리스' 방식을 함께 도입한 것이 핵심이다. 오늘날 통용되는 수술 AR의 정의 — 실세계 정합 + 실시간 + 3D — 를 모두 만족한 최초 사례로 인용된다.

뇌종양 수술의 근본 문제는 '종양이 보이지 않는다'는 것이다. 정상 뇌조직과 침윤성 교종은 육안 색·질감 차이가 거의 없다. 1970년대 CT 도입으로 수술 전에는 종양 위치를 정확히 알 수 있게 됐지만, 개두 후 그 정보를 수술 시야에 대응시킬 방법이 없었다. 정위 프레임은 정확했으나 환자에게 침습적이고 개방수술과 병용이 어려웠다. AR은 '프레임 없이 프레임의 정확도를'이라는 요구에서 나왔다.

성공. 이 계보가 상용 신경외과 내비게이션(Brainlab, Medtronic StealthStation)으로 이어졌고, 오늘날 뇌종양 개두술의 표준 도구가 됐다. 다만 Roberts 방식의 '현미경 접안 중첩'은 별도 모니터 방식에 밀려 부수 기능으로 남았다.

### UNC Chapel Hill 초음파 AR → InnerOptic 상용화 (연구에서 FDA까지 20년)
| 항목 | 내용 |
| --- | --- |
| 주체 | Michael Bajura, Henry Fuchs, Ryutarou Ohbuchi (UNC Chapel Hill) → 스핀오프 InnerOptic Technology, Inc. |
| 연도 | 1992 발표 / 2009·2012 FDA 510(k) 실용화 |
| 수치 | SIGGRAPH '92 논문, Crossref 피인용 278회(Computer Graphics 26(2) 판) + 93회(proceedings 판), DOI 10.1145/142920.134061. InnerOptic InVision 510(k) K083728, 승인 2009-08-12. InnerOptic AIM 510(k) K121479, 승인 2012-09-13 (제품코드 IYO). |
| 출처 | Bajura M, Fuchs H, Ohbuchi R. "Merging virtual objects with the real world: seeing ultrasound imagery within the patient." SIGGRAPH '92 (Crossref 피인용 278). FDA openFDA 510(k) API: K083728, K121479. |

HMD를 쓴 관찰자가 임신부의 복부를 볼 때, 초음파 프로브가 훑는 단면 영상이 실제 배 '안쪽' 해당 위치에 3D로 떠 보이도록 정합했다. 수술 AR이 아니라 '진단 영상의 공간적 재배치'였다는 점이 중요하다. 초음파의 근본 약점 — 화면은 2D인데 프로브의 자세를 머릿속에서 3D로 재구성해야 한다 — 을 정면으로 겨눴다. 이 연구실의 후속 연구가 InnerOptic으로 스핀오프해, 초음파 유도 종양 소작(ablation) 시 바늘 궤적과 초음파 평면을 하나의 3D 장면에 합쳐 보여주는 제품이 됐다.

초음파는 실시간·무방사선·저비용이지만 술자의 공간 인지 부담이 극단적으로 크다. 간 종양 소작에서 바늘 끝을 초음파 평면 안에 유지하는 것은 숙련자도 실패한다. 이 '평면 밖 바늘' 문제는 장비 성능이 아니라 인간 인지의 문제였기 때문에, 영상 품질 개선으로는 해결되지 않고 표현 방식의 변경(AR)을 요구했다.

연구는 고전이 됐고 상용화도 성공했으나 규모는 작다. 발표(1992)에서 FDA 클리어런스(2009)까지 17년이 걸렸다. 초기 시스템은 지연시간·추적 정확도·HMD 무게가 모두 임상 부적합이었고, 실제로 팔린 제품은 HMD를 버리고 모니터 기반 3D 장면으로 후퇴한 형태였다.

### MIT Grimson — 표면 기반 자동 정합, AR을 임상 워크플로에 얹은 수학
| 항목 | 내용 |
| --- | --- |
| 주체 | W. Eric L. Grimson, G.J. Ettinger, S.J. White, T. Lozano-Pérez, W.M. Wells III, R. Kikinis — MIT AI Lab + Brigham and Women's Hospital |
| 연도 | 1994 (CVPR) / 1996 (IEEE TMI) |
| 수치 | IEEE Transactions on Medical Imaging, 1996. Crossref 피인용 211회(DOI 10.1109/42.491415). CVPR-94 선행판 피인용 52회. 동시대 비교치: 마커+랜드마크 혼합 정합의 평균 시스템 정확도 1.81mm (Ganslandt 2002). |
| 출처 | Grimson WEL, Ettinger GJ, White SJ, Lozano-Pérez T, Wells WM, Kikinis R. "An automatic registration method for frameless stereotaxy, image guided surgery, and enhanced reality visualization." IEEE Trans Med Imaging, 1996. DOI 10.1109/42.491415, Crossref 피인용 211. |

환자 머리 표면을 레이저로 스캔해 얻은 점군과 MRI에서 추출한 피부 표면을 자동으로 맞추는(surface matching) 정합 알고리즘이다. 이전까지 정합은 두피에 마커(fiducial)를 붙이거나 해부학적 랜드마크를 사람이 클릭해야 했다. 논문 제목에 'enhanced reality visualization'이라는 표현이 직접 등장하며, 정합된 MRI 구조를 수술 현미경 시야나 비디오 영상에 겹치는 데까지 나아갔다.

1990년대 초 내비게이션의 실제 병목은 하드웨어가 아니라 '정합에 걸리는 시간과 사람의 손'이었다. 마커를 미리 붙이고 CT를 다시 찍는 워크플로는 응급수술에 쓸 수 없고, 마커가 피부와 함께 움직이면 오차가 생긴다. 수술실 시간이 분당 비용으로 환산되는 환경에서 '자동·무마커 정합'은 임상 채택의 전제조건이었다.

성공. 표면 정합은 오늘날 거의 모든 상용 신경외과 내비게이션의 표준 옵션이 됐다. 다만 '표면'을 맞춘다는 접근은 뇌 내부의 변형(brain shift)에는 원리적으로 무력해, 다음 20년의 핵심 난제를 그대로 남겼다.

### 수술 내비게이션의 상용화 — Brainlab, StealthStation, Mazor
| 항목 | 내용 |
| --- | --- |
| 주체 | Brainlab AG (Stefan Vilsmeier, 뮌헨), Medtronic Navigation(구 Surgical Navigation Technologies) StealthStation, Mazor Robotics (Moshe Shoham, Eli Zehavi, 2001 창업) |
| 연도 | Brainlab 창업 1989 / Mazor SpineAssist FDA 2004 / Medtronic의 Mazor 인수 2018 |
| 수치 | Mazor SpineAssist: 2004년 FDA 승인, 최초의 FDA 클리어 척추 수술 로봇. Renaissance(2011) 공표 정확도 1.5mm. Medtronic의 Mazor 인수: 2018년, 약 $1.7B(위키피디아 기재; 2018-09 발표 당시 보도는 $1.64B). 임상 정합 정확도 기준선: 초음파-MRI 공정합 오차 2mm 이내(Keles 2003), 기준점+표면 정합 평균 1.81mm(Ganslandt 2002). |
| 출처 | Wikipedia: Mazor Robotics (창업 2001, SpineAssist FDA 2004, Renaissance 1.5mm, Medtronic 인수 2018 $1.7B). Keles GE et al., Neurosurgery 2003. Ganslandt O et al., Neurol India 2002. |

AR이 아직 연구 단계일 때 '정합 + 추적 + 화면'이라는 골격만 떼어낸 내비게이션은 먼저 산업이 됐다. 광학 추적 카메라가 환자에 고정된 기준 프레임과 수술 기구의 마커를 동시에 보고, 술전 CT/MRI 좌표계로 변환해 모니터 위 3개 단면에 기구 끝 위치를 그린다. AR과의 차이는 단 하나 — 술자가 환자에서 눈을 떼고 모니터를 봐야 한다는 것. 이 '시선 이탈(attention shift)'이 훗날 AR HMD가 공략하는 정확한 틈이 된다. Mazor는 여기에 로봇 팔을 더해 궤적을 물리적으로 고정하는 쪽으로 갔다.

척추 유합술에서 척추경 나사(pedicle screw)를 넣을 때 척추경 내벽을 4mm 이상 뚫으면 신경근·척수 손상이 발생한다. 자유수기(free-hand)는 술자 경험에 전적으로 의존했고, 투시(fluoroscopy) 의존은 환자와 술자 모두에게 누적 방사선을 안겼다. 정량화된 안전 기준(Gertzbein-Robbins 등급)이 있는 몇 안 되는 수술이었기에, '정확도'가 곧 판매 논리가 될 수 있었다.

성공했고, 그것이 AR의 진입 장벽이 됐다. 내비게이션이 이미 '충분히 좋은' 해답으로 자리잡았기 때문에, AR은 정확도로 이기는 것이 아니라 '시선을 떼지 않는다'는 인간공학적 가치로만 차별화할 수 있게 됐다. 이 구도가 2019년 이후 AR 제품 포지셔닝을 결정한다.

### 정합의 근본 한계 — 장기는 움직인다 (brain shift와 연부조직 변형)
| 항목 | 내용 |
| --- | --- |
| 주체 | Christopher Nimsky, Rudolf Fahlbusch 등 (Erlangen) / Gian Andrea Prevost, Eigl B, Paolucci I 등 (Bern) / Egidijus Pelanis, Teatini A 등 (Oslo, HoloCare) |
| 연도 | 2000 (brain shift 정량화) / 2020~2021 (간 복강경 AR 실패 확인) |
| 수치 | 피질 이동 최대 24mm, 심부 종양 경계 3mm 초과 이동이 전체 증례의 66% (Nimsky, Neurosurgery 2000). 간 복강경: FRE 14.0mm → 9.2mm, 정합 소요 중앙값 8분 50초, 증례 10건 (Prevost, J Gastrointest Surg 2020). HoloCare: 병변 부근 TRE 3.78±1.89mm, 절제연 정확도 중앙값 4.44mm(최대 9.75mm) (Pelanis, Med Image Anal 2021). 간 팬텀 AR 조준 오차 29.4±17.1mm(복강경 축) (Ribeiro, J Surg Res 2024). |
| 출처 | Nimsky C, Ganslandt O, Cerny S, Hastreiter P, Greiner G, Fahlbusch R. Neurosurgery, 2000. Prevost GA et al., J Gastrointest Surg, 2020. Pelanis E, Teatini A, Eigl B et al., Medical Image Analysis, 2021. Ribeiro M, Espinel Y, Rabbani N et al., J Surg Res, 2024. |

AR은 술전 영상이 술중 실제 해부와 같다고 가정한다. 이 가정은 뼈에서만 성립한다. Nimsky는 술중 MRI로 개두 후 뇌 표면이 최대 24mm 이동하고, 심부 종양 경계도 66%의 증례에서 3mm를 넘게 움직인다는 것을 정량화했다. 간에서는 기복(pneumoperitoneum)으로 인한 형상 변화가 더 크다. Prevost의 3D 복강경 간절제 AR 시스템은 초기 기준점 정합 오차(FRE) 14.0mm(SD 5.0), 보정 후에도 9.2mm(SD 2.8)에 그쳤고, 저자들은 절제 안내용으로는 '일관되게 너무 부정확하다'고 결론지었다. Oslo의 주입형 기준점 방식은 병변 근처 목표 정합 오차(TRE) 3.78±1.89mm까지 좁혔으나 돼지 모델 전임상 단계였다.

1990년대 후반 신경외과는 이미 내비게이션을 도입했고, 그 다음에 필연적으로 '내비게이션이 가리키는 위치가 진짜인가'를 검증해야 했다. 술중 MRI(iMRI)라는 검증 도구가 등장한 시점이 정확히 이 문제를 측정 가능하게 만들었다. 복부외과는 10년 늦게 같은 질문에 도달했고, 답은 더 나빴다.

실패 — 그러나 생산적인 실패. 기술적 원인: 강체 정합(rigid registration)은 변형체에 대해 원리적으로 틀렸다. 경제적 원인: 비강체 정합에 필요한 술중 3D 영상(iMRI·iCT)은 수술실 개조비가 수백만 달러 규모여서, 정확도 이득이 비용을 정당화하지 못했다. 결과적으로 AR은 뼈(척추·관절·두개골)로 후퇴했고, 간·폐·유방 AR은 2026년 현재도 연구 단계다.

### 연구실을 나오지 못한 2000년대 AR — Varioscope AR과 CAMC
| 항목 | 내용 |
| --- | --- |
| 주체 | Wolfgang Birkfellner, Michael Figl (Vienna Medical University, Varioscope AR) / Nassir Navab, Sandro Michael Heining, Joerg Traub (TU München + LMU 외상외과, Camera Augmented Mobile C-arm) |
| 연도 | Varioscope AR 2002 / CAMC 정확도 논문 2010, 임상 43례 2012 |
| 수치 | Varioscope AR: 평균 보정 오차 1.24±0.38 픽셀(0.12±0.05mm), 최대 3.33±1.04 픽셀(0.33±0.12mm); 프로브 위치 변환 오차 <1mm가 56%, 나머지는 <2mm (Birkfellner, IEEE TMI 2002). 후속 광학투과형 자동보정: 중첩 오차 0.14~0.91mm, 지연 0.1초로 인한 공간 편차 최대 1.1~2.8mm (Figl, IEEE TMI 2005). 입체시 중첩의 과제 성공률 87.5% vs 단안 66.6% (Birkfellner, Phys Med Biol 2003). CAMC: 중첩 정확도 <1mm, 사체 43례 검증, 임상 적용 43례 (Navab, IEEE TMI 2010; Weidert, Unfallchirurg 2012). |
| 출처 | Birkfellner W, Figl M, Huber K et al. IEEE Trans Med Imaging, 2002 (PMID 12472271). Figl M, Ede C, Hummel J et al. IEEE Trans Med Imaging, 2005 (PMID 16279085). Birkfellner W, Figl M, Matula C et al. Phys Med Biol, 2003 (PMID 12608617). Navab N, Heining SM, Traub J. IEEE Trans Med Imaging, 2010 (PMID 20659830). Weidert S et al. Unfallchirurg, 2012 (PMID 22406917). |

Varioscope AR은 상용 헤드마운트 수술 확대경(Life Optics Varioscope)에 마이크로디스플레이를 끼워 광학 투과형 AR을 만든 것으로, 두개악안면외과를 겨냥했다. CAMC는 전혀 다른 발상이다 — 이동형 C-arm의 X선 원점에 거울로 광축을 일치시킨 비디오 카메라를 달아, 단 한 장의 X선 영상과 실시간 비디오를 하드웨어적으로 정합시켰다. 소프트웨어 정합이 아예 필요 없으므로 정합 오차의 상당 부분이 구조적으로 제거된다.

외상외과(trauma)의 고유 문제는 방사선이다. 골절 정복과 나사 삽입 시 투시를 반복하면 술자 손이 1차 빔에 근접한 채 누적 피폭을 받는다. 내비게이션은 기준 프레임을 뼈에 박아야 해서 응급 외상에 부적합했다. CAMC는 '기준 프레임 없이, X선 1장으로'를 노렸다. Varioscope AR은 두개악안면 수술에서 모니터를 볼 수 없는 자세 문제를 겨냥했다.

기술적으로는 성공, 상업적으로는 소멸. 두 시스템 모두 정확도 목표(<1mm)를 달성했고 사체·임상 검증까지 마쳤으나 제품이 되지 못했다. 경제적 원인: CAMC는 C-arm 제조사가 기존 제품군을 개조해야 했고 규제 재승인 비용과 시장 규모가 맞지 않았다. 기술적 원인: Varioscope AR 계열은 지연시간 0.1초만으로도 최대 2.8mm의 공간 편차가 생겨, 술자가 머리를 움직이는 실제 수술에서 정확도 보증이 불가능했다. 이 '지연=오차' 관계가 2010년대 후반 저지연 HMD가 나오기 전까지 광학투과형 AR 전체의 발목을 잡았다.

### Google Glass 의료 붐과 붕괴 — 2년 반의 열광
| 항목 | 내용 |
| --- | --- |
| 주체 | Google X / 초기 채택 외과의들 (Rafael Grossmann, Pierre Theodore, Oliver Muensterer 등), 이후 다수 학술 그룹 |
| 연도 | 2013 (첫 수술 스트리밍) ~ 2015-01 (Explorer 프로그램 종료) |
| 수치 | PubMed 'Google Glass' + surgery 검색 결과 총 82건(대부분 2014~2016). 배터리: 연속 촬영 시 1시간 미만(GoPro는 2시간 초과). 해상도: 720p 동영상 / 5MP 사진(GoPro 1080p / 12MP). 첫 성형수술 적용일 2013-10-29. 레지던트 술후 디브리핑 만족도 3.75 → 4.42 (5점 척도, p<.05, Sahyouni 2017). |
| 출처 | Chang JY, Tsui LY, Yeung KS, Yip SW, Leung GK. Surgical Innovation, 2016 (PMID 27146972). Davis CR, Rosenfield LK. Plast Reconstr Surg, 2015 (PMID 25719707). Muensterer OJ, Lacher M, Zoeller C, Bronstein M, Kübler J. Int J Surg, 2014 (PMID 24534776). Paro JA et al. Ann Plast Surg, 2015 (PMID 25664407). Sahyouni R et al. Surg Neurol Int, 2017 (PMID 28540134). |

단안 프리즘 디스플레이가 달린 경량 안경형 기기로, 술자 시점 1인칭 영상 스트리밍·핸즈프리 기록·음성 검색을 제공했다. 엄밀히 말해 정합 AR이 아니라 '시야 주변 정보 표시(HUD)'였으나, 의료계는 이를 AR로 받아들였다. 2013년 10월 29일 첫 성형수술(안검성형술)에 적용됐고, 이후 2년간 PubMed에 82편의 논문이 쏟아졌다.

수술실의 오래된 문제는 '멸균 상태에서 손을 쓸 수 없다'는 것이다. 술자는 영상을 다시 보려고 세척된 손을 쓸 수 없고, 매번 순회간호사에게 말해야 한다. Glass는 이 문제를 소비자 가격($1,500)으로 푸는 것처럼 보였고, 마침 원격 교육·수술 기록에 대한 수요가 커지던 시점이었다. 즉 의료가 Glass를 원한 이유는 AR이 아니라 '핸즈프리'였다.

소멸. 기술적 원인: 배터리 1시간 미만, 발열, 720p의 불충분한 화질, 수술용 루페(loupe)와 물리적 간섭, 화상회의 지연과 끊김. 경제적·제도적 원인: 환자 영상이 Google 클라우드를 경유하는 구조가 HIPAA 준수 검토를 통과하기 어려웠고, Google이 2015년 1월 Explorer 프로그램을 종료하면서 기기 공급 자체가 끊겼다. 남긴 교훈은 명확하다 — 의료 AR의 실패 원인 1순위는 알고리즘이 아니라 하드웨어 수명주기와 데이터 거버넌스다.

### Novarad OpenSight — HoloLens 기반 최초의 미국 의료 AR 510(k)
| 항목 | 내용 |
| --- | --- |
| 주체 | Novarad Corporation (Utah, American Fork) — 기존 PACS 업체 |
| 연도 | 2018-09-21 (FDA 클리어런스) |
| 수치 | 510(k) K172418, 결정일 2018-09-21, 제품코드 LLZ, 규정 892.2050. 동일 업체 후속 제품 VisAR: 510(k) K220146, 결정일 2022-05-27, 제품코드 OLO. 참고 하드웨어: HoloLens 2는 2019-11-07 출시, $3,500, 대각 시야각 52°(초대 HoloLens 34°). |
| 출처 | openFDA 510(k) API: K172418 (Novarad Corporation, OpenSight, 2018-09-21, LLZ), K220146 (VisAR, 2022-05-27, OLO), K061920/K132853 (NovaPACS). Wikipedia: HoloLens 2 사양·가격. |

Microsoft HoloLens에서 환자의 CT/MRI 3D 재구성을 실제 환자 몸 위에 정합해 보여주는 술전 계획·표시 도구다. 환자 위에 붙인 기준 마커로 볼륨을 정합하고, 술자는 절개 위치와 심부 구조를 피부 위에서 직접 확인한다. 중요한 것은 규제 경로다 — Novarad는 자사 PACS 제품(NovaPACS, K061920 등)과 같은 제품코드 LLZ('System, Image Processing, Radiological')로 신청해, AR을 '새로운 수술기구'가 아니라 '영상 표시 방법의 변형'으로 프레이밍했다. 이 전략이 통했다.

2016~2018년은 HoloLens(2016 출시)가 처음으로 '실용적 정확도의 광학투과형 HMD'를 대량 생산품으로 제공한 시점이다. 그 전까지 의료 AR은 기기를 직접 만들어야 했고(Varioscope AR), 그래서 제품이 되지 못했다. 동시에 미국 병원은 CT 3D 재구성을 이미 일상적으로 만들고 있었으나 그것을 수술실로 가져갈 방법이 모니터뿐이었다.

성공 — 다만 '문을 연' 성공이다. 시장 점유는 크지 않았으나 FDA가 HoloLens 기반 AR을 기존 영상처리 제품코드로 통과시킬 수 있음을 입증해, 이후 모든 의료 AR 제조사의 규제 전략 템플릿이 됐다. 2022년의 VisAR에서 별도 제품코드(OLO)로 옮겨간 것은 FDA가 AR을 독립 범주로 인식하기 시작했다는 신호다.

### Augmedics xvision — FDA가 새 제품코드를 만든 척추 AR HMD
| 항목 | 내용 |
| --- | --- |
| 주체 | Augmedics, Ltd. (이스라엘 Yokneam / 미국 Chicago) — 임상 검증은 Camilo A. Molina, Daniel M. Sciubba, Timothy Witham (Johns Hopkins) |
| 연도 | 2019-12-20 (FDA 510(k) K190929) / 2020 첫 인체 적용 |
| 수치 | 510(k) K190929, 결정일 2019-12-20, 제품코드 SBF. 이후 재클리어런스 6건(K211188 2021-07-19, K220905 2022-11-17, K241481 2024-10-16, K250255 2025-03-13, K251639 2025-10-03, K261854 2026-07-31). 첫 인체 적용 결과: Gertzbein-Robbins 임상 정확도 100%, 선형 편차 평균 2.07mm, 각도 편차 2.41°, 사체 벤치마크와 유의차 없음(P>.05) (Molina 2021, Oper Neurosurg, PMID 33377137, 피인용 77). 메타분석: AR 척추 기구 삽입 정확도 97.2%(95% CI 96.2~98.1%, p<0.001), 8개 연구·163명·나사 1,2 |
| 출처 | openFDA 510(k) API (applicant: Augmedics, Ltd.; product_code SBF). Molina CA, Sciubba DM, Greenberg JK, Khan M, Witham T. Oper Neurosurg, 2021, DOI 10.1093/ons/opaa398, PMID 33377137, Europe PMC citedByCount 77. Pahwa B, Azad TD, Liu J et al. J Clin Med, 2023, PMID 37959207. openFDA classification API: product code SBF. |

투명 디스플레이가 달린 전용 헤드셋을 술자가 쓰면, 환자 척추의 3D 재구성과 계획된 나사 궤적이 환부 위에 겹쳐 보인다. 별도 광학 카메라 없이 헤드셋 자체가 환자에 부착된 마커를 추적한다. 기존 내비게이션 대비 유일하면서 결정적인 차이는 술자가 모니터를 보려고 고개를 돌리지 않는다는 것 — 즉 손과 눈이 같은 곳에 머문다. Johns Hopkins의 첫 인체 적용(78세 여성, L4-S1 감압 및 나사·로드 고정)이 2020년에 이뤄졌다.

척추경 나사 삽입은 의료에서 AR이 성립할 수 있는 거의 유일한 조건을 갖춘 수술이다. (1) 대상이 뼈라 변형되지 않아 강체 정합이 유효하다. (2) 안전 기준이 mm 단위로 정량화돼 있다(Gertzbein-Robbins 등급: A=천공 없음, B=<2mm, C=2~4mm, D=4~6mm). (3) 연간 시술 건수가 크고 임플란트 매출과 묶여 경제성이 있다. (4) 자유수기 대비 개선 여지가 통계적으로 입증 가능하다. 다른 어떤 수술도 이 네 조건을 동시에 만족하지 않는다.

성공. AR 수술 내비게이션 최초의 명확한 상업·규제 성공 사례다. 결정적 증거는 FDA가 이 기기를 위해 제품코드 SBF('Orthopedic Augmented Reality', 규정 882.4560, Class II)를 신설했고, K190929가 그 코드의 첫 번째 항목이라는 사실이다. 이후 모든 정형외과 AR이 이 predicate를 따라 들어왔다. 다만 주의 — 메타분석의 97.2%는 자유수기 대조군 대비 우월성을 직접 입증한 수치가 아니며, 기존 로봇/내비게이션도 유사한 정확도를 보고한다.

### Philips ClarifEye / Karolinska ARSN — HMD를 버린 AR (하이브리드 수술실 방식)
| 항목 | 내용 |
| --- | --- |
| 주체 | Adrian Elmi-Terander, Gustav Burström, Erik Edström, Rami Nachabe (Karolinska Institutet + Philips Healthcare) |
| 연도 | 2016~2020 임상 연구 / 2021-02-23 FDA 510(k) K201743 |
| 수치 | 2019년 임상 결과: 흉요천추 나사 253개, 전체 정확도 94.1%, Gertzbein 2등급(2~4mm 천공) 5.9%(15개), 3등급(중증 오배치) 0개, 나사당 평균 5.2±4.1분 (Spine 2019, Crossref 피인용 204). 2018년 사체 최소침습 연구: 나사 18개 중 16개 완벽 배치(89%), 내비게이션 시간 90±53초, 평균 오차각 0.9°±0.8° (Spine 2018, 피인용 123). 변형교정 비교: ARSN 나사 밀도 86.3%±14.6% vs 자유수기 74.7%±13.9%, 수술시간 차이 없음(431분 vs 417분) (Spine 2020). FDA: K201743 ClarifEye R1.0, 2021-02-23, 제품코드 OWB. 메타분석에서 Allura AR  |
| 출처 | Elmi-Terander A, Burström G, Nachabe R et al. "Pedicle Screw Placement Using Augmented Reality Surgical Navigation With Intraoperative 3D Imaging." Spine, 2019, DOI 10.1097/brs.0000000000002876, Crossref 피인용 204. Elmi-Terander A et al. Spine, 2018, 피인용 123. Edström E, Burström G, Persson O et al. Spine, 2020. openFDA 510(k): K201743. Pahwa 2023 메타분석. |

HMD를 쓰지 않는 AR이다. 하이브리드 수술실 천장의 C-arm에 4개의 비디오 카메라를 내장해, 술중 콘빔 CT로 얻은 3D 척추 영상을 환자 피부 표면의 비디오 영상에 정합해 모니터에 겹쳐 보여준다. 술자는 환자 피부 위에 그려진 나사 궤적을 보며 진입점과 각도를 잡는다. 피부에 붙이는 접착식 마커만 쓰고 뼈에 기준 프레임을 박지 않는다. 헤드셋의 지연·무게·시야각 문제를 아예 회피한 설계다.

2010년대 중반 유럽 대형 병원은 혈관내 시술용 하이브리드 수술실에 이미 수백만 유로를 투자해둔 상태였다. 그 장비(천장 C-arm + 술중 3D 영상)를 척추수술에 재활용할 수 있다면 한계 비용이 낮다. 동시에 최소침습 척추수술(MIS)의 확산으로, 작은 절개로는 해부 랜드마크를 촉지할 수 없어 영상 의존도가 급등했다. HMD가 아직 신뢰할 수 없던 시점에 '기존 수술실 인프라를 AR화'하는 것이 합리적 선택이었다.

성공. 그러나 xvision과 다른 성공이다 — ClarifEye는 하이브리드 수술실을 이미 보유한 병원에만 팔 수 있어 설치 기반이 제한적이다. 주목할 점은 메타분석에서 xvision(HMD)과 Allura AR(비HMD)의 정확도 차이가 통계적으로 유의하지 않았다는 것(p=0.092)이다. 즉 HMD가 정확도에 기여한다는 증거는 아직 없고, HMD의 가치 주장은 여전히 인간공학과 작업흐름에 머물러 있다.

### 제품코드 SBF의 개방 — 정형외과 AR 35건 클리어런스 (2019~2025)
| 항목 | 내용 |
| --- | --- |
| 주체 | Medacta International (NextAR), Pixee Medical (Knee+), Zimmer Biomet/Orthosoft (OptiVu ROSA MxR), Surgalign (ARAI, HOLO Portal), Surgical Theater (SpineAR SNAP / SyncAR), Onpoint Surgical, Brainlab (Mixed Reality Spine Navigation), Globus Medical (ExcelsiusXR), Kico (ARVIS), Polarisar (STELLAR Knee), Taiwan Main Orthopaedic (Caduceus S) |
| 연도 | 2019-12-20 첫 클리어런스 ~ 2025-07-31 (조회 시점 기준 35건) |
| 수치 | SBF 제품코드 510(k) 35건 (2019-12-20 K190929 ~ 2025-07-31 K250477). 주요 최초 진입: Medacta NextAR TKA K193559 2020-07-10; Pixee Medical Knee+ K202750 2021-04-21; Medacta NextAR Spine K210859 2021-11-05; Zimmer OptiVu ROSA MxR K220733 2022-07-29; Surgical Theater SpineAR SNAP K213034 2022-09-29; Onpoint AR Spine K231284 2023-09-08; Brainlab Mixed Reality Spine Navigation K242569 2025-05-16; Globus ExcelsiusX |
| 출처 | openFDA 510(k) API, product_code=SBF, 전체 목록 (조회 2026-09). openFDA classification API, product code SBF 정의. Ma Y, Wu J, Dong Y, Tang H, Ma X. Orthop Surg, 2025 (PMID 39815419). Kurosaka K et al. Clin Orthop Relat Res, 2023 (PMID 36862072). |

xvision이 뚫은 SBF 제품코드로 6년간 35건의 510(k)가 통과했다. 의미심장한 것은 분포다 — 척추뿐 아니라 인공슬관절(TKA), 인공견관절(TSA/RSA), 인공고관절로 빠르게 퍼졌다. Medacta NextAR는 2020년 7월 TKA로 시작해 견관절·척추로 확장했고, Pixee Medical의 Knee+는 스마트글래스에 QR 유사 마커를 붙여 대형 내비게이션 장비 없이 절삭 가이드 각도를 표시하는 저가 접근을 택했다. Brainlab이 2025년에야 SBF로 들어온 것은 기존 내비게이션 강자가 AR을 늦게 방어적으로 채택했음을 보여준다.

인공관절 치환술이 AR을 받아들인 이유는 척추와 다르다. TKA에서 대퇴·경골 절삭면의 각도 오차 몇 도가 임플란트 수명과 재치환율을 좌우하는데, 기존 해법은 (a) 기계식 가이드(부정확) 또는 (b) 로봇/내비게이션(대당 수억 원, 수술실 공간 점유, 등록 시간 추가)뿐이었다. AR 글래스는 '로봇의 정확도에 근접하면서 로봇의 자본지출이 없는' 중간 가격대를 열었다. 즉 정형외과가 AR을 택한 이유는 정확도가 아니라 자본 효율이다.

규제·상업적으로는 성공, 임상 근거는 아직 얇다. 35건의 클리어런스는 모두 '기존 기기와 실질적 동등(substantially equivalent)' 판정이지, 우월성 입증이 아니다. THA 무작위시험처럼 통계적 유의성은 얻었으나 저자 스스로 임상적 의의를 부정한 사례가 나오는 중이다. 정형외과 AR의 진짜 시험대는 정확도가 아니라 재치환율·기능점수 같은 장기 결과인데, 그 데이터는 2026년 현재 존재하지 않는다.

### HoloAnatomy — 시신 없는 해부학 교육
| 항목 | 내용 |
| --- | --- |
| 주체 | Case Western Reserve University Interactive Commons (Mark Griswold, Susanne Wish-Baratz) + Cleveland Clinic Lerner College of Medicine; 현재 AlensiaXR가 배포 |
| 연도 | 2015 개발 시작 / 2019~2020 비교효과 연구 발표 / 2019 Case Western 신교육과정 전면 도입 |
| 수치 | 비교효과 연구: 학생 64명, 시신 실기시험 평균 73.8%±12.3 vs 혼합현실 실기시험 평균 74.2%±13.0, 유의차 없음(p>0.05), 두 시험 간 상관 r=0.74(p<0.01), 대조군 33명 (Stojanovska M et al., Medical Science Educator, 2019, PMID 34457656). 학습 파지(retention) 예비연구: 1학년 38명 참여, 2부에서 참가자 22명과 동급생 129명 비교, 혼합현실군 유의하게 높은 점수(p<.009) (Baratz G, Sridharan PS, Yong V et al., Int J Med Educ, 2022). 제조사 주장: '전통 해부 대비 최대 2배 빠른 학습' — 제조사 홈페이지 문구로, 위 동등성 연구와 직접 대응 |
| 출처 | Stojanovska M, Tingle G, Tan L et al. "Mixed Reality Anatomy Using Microsoft HoloLens and Cadaveric Dissection: A Comparative Effectiveness Study." Medical Science Educator, 2019/2020, PMID 34457656. Baratz G, Sridharan PS, Yong V et al. Int J Med Educ, 2022 (PMID 35506483). case.edu/holoanatomy (제조사·대학 공식 페이지, '2배' 주장 출처). |

HoloLens로 인체 전신의 3D 홀로그램을 여러 학생이 동시에 같은 공간에서 보며 층별로 벗겨내고 회전시키는 해부학 교육 플랫폼이다. 수술 AR과 달리 정합 정확도 요구가 없다 — 환자가 없으므로 오차가 해를 끼치지 않는다. 이 점이 의료 AR 중 교육 분야가 가장 먼저, 가장 널리 실용화된 이유다. Case Western의 Health Education Campus(2019년 개관)는 해부학 실습실을 전통 시신 해부와 병행 설계했다.

미국 의과대학의 구조적 문제가 배경이다. (1) 시신 기증 감소와 보관·처리 비용(시신 1구당 수천 달러, 전용 환기·방부 시설 필요), (2) 의학교육과정 압축으로 해부학 시수 자체가 줄어드는 추세, (3) 원격·분산 캠퍼스 확대. 여기에 COVID-19(2020)가 실습실 접근을 물리적으로 차단하면서 대체재 수요가 급증했다. 즉 교육 AR은 '더 잘 가르치기 위해'가 아니라 '시신을 구할 수 없어서' 채택됐다.

성공, 단 '우월'이 아니라 '동등'으로서의 성공. 핵심 결과는 혼합현실 학습군이 시신 시험에서 더 잘한 것이 아니라 '차이가 없었다'는 것이다. 시신 확보가 불가능하거나 비용이 과도한 기관에서 이는 충분한 도입 근거가 된다. 주의할 점: 제조사가 홍보하는 '2배 빠른 학습'은 위 동등성 논문이 뒷받침하지 않으며 별도 출처 확인이 필요하다.

### 원격 AR 멘토링 — STAR와 전장·오지 수술 지원
| 항목 | 내용 |
| --- | --- |
| 주체 | Edgar Rojas-Muñoz, Chengyuan Lin, Natalia Sanchez-Tamayo, Juan P. Wachs 등 (Purdue University, System for Telementoring with Augmented Reality) |
| 연도 | 2020 (무작위 교차시험 발표) |
| 수치 | 윤상갑상막절개술 무작위 교차시험: STAR 원격 안내가 음성 전용 대비 시술 점수와 시술 안전성에서 통계적으로 우월 (Rojas-Muñoz E et al., npj Digital Medicine, 2020, PMID 32509972). 최소침습수술 원격멘토링 동적 AR 큐 범위검토: 논문 21편, 손동작 큐 10편, 수술기구 큐 10편, 술기평가 13편 (Hamza H, Aboumarzouk OM, Al-Ansari A, Navkar NV, J Med Internet Res, 2025, PMID 39899360). |
| 출처 | Rojas-Muñoz E, Lin C, Sanchez-Tamayo N et al. "Evaluation of an augmented reality platform for austere surgical telementoring: a randomized controlled crossover study in cricothyroidotomies." npj Digital Medicine, 2020, PMID 32509972. Hamza H, Aboumarzouk OM, Al-Ansari A, Navkar NV. J Med Internet Res, 2025, PMID 39899360. |

원격지의 전문의가 현장 술자의 시야 영상 위에 절개선·기구 방향을 직접 그리면, 그 주석이 현장 술자의 투명 디스플레이(환자 위에 배치된 반투과 화면)에 환부와 정합돼 표시된다. 음성만으로 '조금 더 왼쪽'이라고 말하는 대신 위치를 지시할 수 있다. 무작위 교차 설계로 음성 전용 멘토링과 직접 비교했다는 점에서, 대부분 사례보고에 그치는 원격 AR 연구 중 근거 수준이 높다.

원격 수술 지원의 근본 문제는 언어의 공간 표현 한계다. 전문의는 무엇을 하라고 정확히 알지만, 음성으로는 '어디를' 전달할 수 없다. 이 문제가 극단화되는 곳이 전투 현장·재난 지역·군함·오지로, 숙련도가 낮은 시술자가 윤상갑상막절개술(cricothyroidotomy) 같은 시간 제약 술기를 수행해야 한다. 미 국방부와 NASA가 이 분야 연구를 후원한 이유가 여기 있다. AR은 '전문가를 보낼 수 없을 때 전문가의 손가락만 보내는' 수단이었다.

연구 단계 — 규제 승인 제품 없음. 기술적 원인: 대역폭과 지연이 통제되지 않는 환경(위성·전술망)이 바로 그 기술이 가장 필요한 환경이다. Google Glass가 겪은 '지연과 끊김'이 그대로 재현된다. 경제적·제도적 원인: 원격 술기 지도에 대한 의료과실 책임 소재와 주(州)·국경 간 면허 문제가 해결되지 않았고, 수가(reimbursement) 코드가 없어 병원이 도입할 재무적 유인이 없다. 상업적으로는 Proximie·Help Lightning 같은 비정합 원격 협업 도구가 자리를 차지했으나, 이들은 영상 위 주석 수준으로 AR 정합은 아니다.

### 하드웨어 공급 붕괴 — 의료 AR의 가장 큰 단일 위험
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft (HoloLens 2), Magic Leap, 그리고 이들 위에 제품을 올린 의료 소프트웨어 업체 전부 |
| 연도 | 2024 (HoloLens 2 단종 발표) / 2024-12-31 (Magic Leap One 서비스 종료) |
| 수치 | HoloLens 2: 2019-11-07 출시, $3,500(기업형 월 $125 / 개발자 월 $99), 대각 시야각 52°. 단종 후 소프트웨어 업데이트는 2027-12-31까지. Magic Leap: 누적 조달액 최소 $3.5B(사우디 PIF $750M 포함), Magic Leap One 2018-08-08 출시 $2,295, 2020-04-22 인력 약 50% 감원, 2020-05 $350M 추가 조달, Magic Leap 2 2022-09-30 출시, 2024-07 약 75명 추가 감원(영업·마케팅 부문 전체), Magic Leap One 2024-12-31 서비스 종료·작동 정지. |
| 출처 | Wikipedia: HoloLens 2 (출시일·가격·시야각·단종·업데이트 종료일 2027-12-31, IVAS 계약). Wikipedia: Magic Leap (조달 $3.5B, Magic Leap One 2018-08-08 $2,295, 2020-04-22 감원, 2022-09-30 ML2, 2024-07 감원, 2024-12-31 EOL·작동 정지). |

2018~2024년 의료 AR 제품의 절대다수는 자체 하드웨어가 아니라 HoloLens 2 또는 Magic Leap 위에 얹힌 소프트웨어였다. Novarad OpenSight/VisAR, HoloAnatomy, Surgical Theater SpineAR, 다수의 대학 연구 시스템이 여기 해당한다. 그 기반이 2024년에 동시에 무너졌다. Microsoft는 HoloLens 2를 단종했고(소프트웨어 업데이트만 2027-12-31까지 보증), Magic Leap One은 2024-12-31 클라우드 서비스 종료와 함께 기기가 작동을 멈췄다 — 구매한 하드웨어가 문자 그대로 벽돌이 됐다.

의료기기 규제는 하드웨어 수명을 가정한다. 510(k)로 클리어된 기기는 predicate와 동일한 하드웨어 구성을 전제하므로, 헤드셋이 단종되면 제조사는 새 헤드셋으로 재신청해야 한다(Augmedics의 반복 재클리어런스가 부분적으로 이 성격이다). 반면 소비자 AR 하드웨어의 제품 주기는 3~5년이고, 군용 IVAS 계약 같은 외부 요인으로 방향이 바뀐다. 즉 의료(10~15년 기기 수명 기대)와 소비자 전자(3~5년)의 시간 척도가 애초에 맞지 않았다.

실패 — 기술이 아니라 공급망의 실패다. 상업적으로 성공한 의료 AR 제품(Augmedics xvision, Medacta NextAR, Philips ClarifEye)의 공통점은 전용 하드웨어를 직접 만들거나 기존 의료장비(C-arm)에 얹었다는 것이고, 실패하거나 위태로운 제품의 공통점은 소비자 헤드셋 의존이다. 이것이 의료 AR 30년사에서 가장 반복적으로 확인된 교훈이다 — Google Glass(2015)에서 Magic Leap One(2024)까지 같은 실패가 9년 간격으로 되풀이됐다.

#### 검증에서 잡힌 정정
- [핵심 오류] 'FDA ... 2025년까지 35건이 그 코드로 통과했다' 및 'SBF 제품코드 510(k) 35건(2019-12-20 K190929 ~ 2025-07-31 K250477), 조회 2026-09' — 틀림. openFDA(product_code=SBF)는 2026-09-29 현재 총 43건을 반환하며 최신 결정일은 2026-07-31이다. 35건은 오직 2025-07-31 컷오프에서만 맞는 수이고, 서사가 명시한 조회 시점(2026-09)과 맞지 않는다. 또한 '2025년까지'도 틀렸다 — 2025년에만 13건(2025-08-08, 09-04, 09-10, 09-29, 10-03 포함)이 나와 2025년 말 누계는 40건이다. 올바른 표기: '2025년 말까지 40건, 2026-09 조회 시점 43건'.
- [자기모순] 위 '35건 / ~2025-07-31' 창과 같은 문서의 Augmedics 항목이 충돌한다. 그 항목은 재클리어런스로 K251639(2025-10-03)와 K261854(2026-07-31)를 정확히 싣고 있는데(openFDA로 둘 다 확인됨, 제품코드 SBF), 이 둘은 문서가 주장하는 SBF 집계 창 밖에 있다. 같은 문서의 두 수치가 서로를 반박한다.
- [분석군 혼동 + 없는 p값] 'AR 내비게이션 척추경 나사 우수/양호율 99.1% vs 대조군 91.7%(p<0.0001), 150명·699개 나사 (Ma 2025)' — 수치 짝짓기가 틀렸다. 실제 초록(PMID 39815419): 1차 분석인 FAS 민감도 분석에서 실험군 98.0%(344/351) vs 대조군 91.7%(319/348), 차이 6.3%[3.0~9.8%], p=0.0003. 99.1% vs 91.7%는 ATS(actual treatment set)에서만 나오며 그 차이는 7.3%[4.1~10.6%]다. PPS의 p는 정확히 0.0001. 즉 초록에 'p<0.0001'은 존재하지 않고, ATS 정확도 값에 FAS/PPS 계열 p값을 붙인 것은 분석군 혼합이다. 150명·699개(351+348)는 맞다. 올바른 표기: 'FAS 98.0% vs 91.7%, 차이 6.3%, p=0.0003(ATS 기준으로는 99.1% vs 91.7%)'.
- [출처 귀속 오류 + 연도 불가능] 'PubMed Google Glass + surgery 검색 결과 총 82건(대부분 2014~2016)' — 틀림. 82는 PubMed 검색 건수가 아니라 Davis CR & Rosenfield LK, Plast Reconstr Surg 2015(PMID 25719707)의 체계적 문헌고찰 스크리닝 수다. 초록 원문: 'Eighty-two publications were identified, with 21 included for review.' 검색어는 'Google'과 'Glass'였고 대상은 성형외과 관련 문헌, DB는 PubMed/Ovid MEDLINE/Cochrane이다. 게다가 2015년 발표 논문이 '2014~2016년' 문헌을 담을 수 없으므로 연도 서술 자체가 불가능하다. 포함 논문은 82편이 아니라 21편(정식 논문 3, 사설/논평 7, 학회초록 1, 뉴스 3, 온라인 7).
- [중복 계수] 'CAMC: 중첩 정확도 <1mm, 사체 43례 검증, 임상 적용 43례 (Navab, IEEE TMI 2010; Weidert, Unfallchirurg 2012)' — '사체 43례'가 근거 없다. Navab 2010(PMID 20659830) 초록은 'cadaver studies conducted by trauma surgeons'와 '<1 mm' 정확도만 보고하고 사체 증례 수를 제시하지 않는다. 43이라는 수는 Weidert 2012(PMID 22406917)의 'The clinical application of the device in 43 cases'에서만 나온다. 같은 43을 사체와 임상 양쪽에 중복 기재한 오류다.
- [문헌 성격 오기재] 'HoloCare: 병변 부근 TRE 3.78±1.89mm, 절제연 정확도 중앙값 4.44mm(최대 9.75mm) (Pelanis, Med Image Anal 2021)' — 숫자 3개는 모두 정확하나(PMID 33454603 확인) 근거의 성격이 틀리게 제시됐다. 해당 논문 제목은 'Evaluation of a novel navigation platform for laparoscopic liver surgery with organ deformation compensation using injected fiducials'이고, 검증은 인체가 아니라 '돼지 4마리 전임상 시험(four porcine models)'이다. 시스템은 HoloLens류 HMD가 아니라 로봇 C-arm 기반이며, HoloCare 제품이라는 근거가 논문에 없다. 또한 저자 결론은 'accurate enough to be potentially clinically beneficial'로, 이 
- [연도 오기] 'Stojanovska M et al., Medical Science Educator, 2019, PMID 34457656' — Europe PMC 기준 해당 논문의 발행연도는 2020이다(Med Sci Educ, pubYear 2020). 항목 헤더의 '2019~2020 비교효과 연구 발표'는 모호하게 빠져나가지만 수치 줄의 '2019'는 틀렸다. 내용 수치(64명, 73.8%±12.3 vs 74.2%±13.0, p>0.05, r=0.74 p<0.01, 대조군 33명)는 전부 정확하다.
- [미검증 수치] 'Magic Leap 누적 조달액 최소 $3.5B(사우디 PIF $750M 포함)' — 총액 $3.5B는 인용된 Wikipedia 문서에서 확인된다('By August 2024, Magic Leap had raised at least $3.5 billion'). 그러나 'PIF $750M'이라는 구체 수치는 인용 출처에서 확인되지 않는다. 공개 보도상 PIF 투자는 별개 라운드(2021년 약 $450M, 2023년 약 $590M)로 알려져 있어 $750M은 출처 대조가 필요하다.
- [서사 주장 과장] '의료는 AR을 가장 먼저 받아들인 분야였다' — 성립하지 않는다. 'augmented reality'라는 용어 자체가 Caudell & Mizell(Boeing)이 1990년에 만들고 1992년 1월 HICSS에서 발표한 것으로, 대상은 의료가 아니라 항공기 배선 하네스 조립(제조업)이었다. 광학 시스루 HMD의 원형은 Sutherland 1968, 정합된 중첩 정보 표시는 1950~60년대 항공 HUD까지 거슬러 간다. Roberts 1986이 '수술 AR 최초'인 것은 맞지만, '분야 중 의료가 최초'는 틀렸다. 같은 이유로 1992년 Bajura를 두고 'AR이라는 용어가 정착하기도 전에'라고 한 것도 부정확하다 — 용어는 1990년에 이미 만들어졌고 SIGGRAPH '92(7월)보다 앞선 1992년 1월에 활자화됐다.
- [분류 오해 소지] 'FDA는 이를 위해 Orthopedic Augmented Reality(제품코드 SBF)를 신설했고 ... 규정 882.4560' — 규정 번호·클래스·정의 원문은 모두 정확히 확인된다. 다만 openFDA classification에서 SBF의 medical_specialty_description은 'Orthopedic'이 아니라 'Neurology'이며, 882.4560은 정형외과 규정(888.xxxx)이 아니라 기존 신경외과 정위기구(stereotaxic instrument) 규정이다. 즉 FDA가 만든 것은 '새 분류 규정'이 아니라 '기존 신경과 규정 아래의 새 제품코드'다. 또한 K190929는 De Novo가 아니라 'Substantially Equivalent' 판정 510(k)다.
- [출처 간 불일치 고지 누락] 'Roberts 1986 피인용 656회(Semantic Scholar)' — Semantic Scholar 조회값과 정확히 일치함을 확인했다(citationCount 656). 다만 같은 논문의 피인용은 DB마다 크게 갈린다: Crossref 519회, Europe PMC 299회. 서사가 DB를 명시한 점은 적절하나, 2.2배 편차가 나는 지표를 단일 권위 수치처럼 본문('656회 인용')에 노출한 것은 오해를 부른다.
- 제품코드 SBF 클리어런스 '35건'은 틀렸다. openFDA 조회 결과 SBF 총계는 43건이다(2019-12-20 K190929 ~ 2026-07-31 K261854). 2025년 말 기준으로도 40건이다. 조사가 누락한 8건: K252054(Surgical Theater SpineAR SNAP, 2025-09-29), K252530·K252170·K250108(Mr Surgical Solutions OptiVu Shoulder, 2025-09-10/08-08/07-09), K251737(Medacta NextAR Shoulder, 2025-09-04), K251639(Augmedics, 2025-10-03), K252847(Medacta NextAR Hip, 2026-01-09), K253805(Pixee Knee+, 2026-04-24), K261854(Augmedics, 2026-07-31).
- 내부 모순: SBF 항목은 '조회 2026-09' 기준 '2019-12-20 ~ 2025-07-31 K250477 총 35건'이라고 적었으나, 같은 문서의 Augmedics 항목은 K251639(2025-10-03)와 K261854(2026-07-31)를 SBF 클리어런스로 나열한다. 2026-09 조회라면 종점이 2025-07-31일 수 없다. 35라는 수는 2025년 8월경 스냅샷이며 '2025년까지'라는 서술과도 맞지 않는다.
- CAMC '사체 43례 검증'은 근거 없는 수치다. Navab 2010(IEEE TMI, PMID 20659830) 원문은 사체 연구를 언급하되 43이라는 수를 제시하지 않는다. 43은 Weidert 2012(Unfallchirurg, PMID 22406917)의 임상 적용 증례 수다. 같은 43이 사체와 임상 양쪽에 중복 기재됐다.
- '2013~2015년 Google Glass 열풍은 … 소멸했다'는 틀렸다. 2015-01-15에 종료된 것은 Explorer 프로토타입 생산이고, 이후 Glass Enterprise Edition 1(2017년 기업 공개)과 Enterprise Edition 2(2019년 5월, 8MP 카메라)가 이어졌으며 Google이 Glass 생산·판매를 완전히 중단한 것은 2023-03-15다. 의료 Glass 연구도 EE2로 계속됐다. '2년 반의 열광 뒤 소멸'은 10년 궤적을 2년으로 압축한 오류다.
- 'AR이라는 용어가 정착하기도 전에 그 개념을 실증했다'(Bajura 1992)는 순서가 반대다. 'augmented reality'는 1992년 1월 HICSS-25에서 Caudell & Mizell이 Boeing 항공기 배선 공정용으로 명명했고(DOI 10.1109/HICSS.1992.183317, 피인용 852), SIGGRAPH '92는 그해 7월이다.
- '전환점은 2018년 Novarad OpenSight' + '최초의 미국 의료 AR 510(k)' 프레이밍은 성립하지 않는다. openFDA 확인 결과 OpenSight(K172418, 2018-09-21)의 제품코드는 LLZ(영상처리 시스템)로, FDA는 이를 AR 범주로 취급하지 않았다. 또한 같은 문서가 인용한 InnerOptic InVision(K083728, 2009-08-12)이 9년 앞선 AR 510(k)다. 따라서 '이후 모든 의료 AR 제조사의 규제 전략 템플릿'이라는 주장은 검증되지 않으며, 실제로 범주를 연 것은 SBF(Augmedics)다.
- '간 복강경 AR의 정합 오차는 14.0mm'는 최악값만 인용한 것이다. Prevost 2020(J Gastrointest Surg, PMID 31621024) 원문은 '첫 정합 시도 평균 FRE 14.0mm(SD 5.0) → 마지막 시도 9.2mm(SD 2.8)'이다. 또한 '수술 안내에는 너무 부정확'은 측정 판정이 아니라 설문 응답(절제 유도 한정)이며, 같은 논문은 '워크플로 영향은 작고', '사라지는 병변 탐지 이득은 크다'고 결론짓는다.
- Ribeiro 2024(J Surg Res, PMID 38354617)의 '29.4±17.1mm'만 인용한 것은 선택 인용이다. 원문은 복강경 축 29.4±17.1mm와 함께 술자 포트 축 9.2±5.1mm를 병기한다. 유리한 쪽을 빼고 3배 큰 값만 제시했다.
- Ma 2025(Orthop Surg, PMID 39815419)의 '99.1% vs 91.7%, p<0.0001'은 세 가지 분석 집합 중 가장 유리한 ATS(actual treatment set) 결과다. FAS 민감도 분석은 98.0%(344/351) vs 91.7%(319/348), p=0.0003이며 우월성 검정의 주 결과는 차이 6.3%[3.0–9.8%]다.
- Molina 2021(Oper Neurosurg, PMID 33377137)의 '임상 정확도 100%'는 환자 1명·나사 6개의 first-in-human 결과다. 표본 크기를 밝히지 않고 100%를 'AR 수술 내비게이션의 결정적 증거'로 제시한 것은 증거 강도의 과장이다.
- Pahwa 2023(J Clin Med, PMID 37959207)의 97.2%(95% CI 96.2–98.1)는 대조군 없는 단일군 8편·163명 풀링이며 Europe PMC 피인용은 3회다. 우월성 근거가 아니다. 같은 문서가 인용한 Kurosaka 2023(CORR, PMID 36862072)은 '광범위 도입 비권고'를 명시하고, SBF 43건은 전부 substantially equivalent 판정이다.
- 피인용 수치가 서로 다른 DB에서 혼용돼 비교 불가능하다. Roberts 1986은 Semantic Scholar 656이 맞지만 Crossref는 519이고, Elmi-Terander 2019는 Crossref 204·Europe PMC 164다. 단일 기준 없이 '656회', '278회', '211회', '204회'를 나란히 놓으면 상대적 영향력 비교가 왜곡된다.
- '하드웨어 공급 붕괴 = 의료 AR의 가장 큰 단일 위험'은 이 문서 자신의 증거와 충돌한다. HoloLens 2는 단종 후에도 2027-12-31까지 소프트웨어 업데이트가 유지되고 Magic Leap 2(2022-09-30 출시)는 존속하며, 문서가 꼽은 상업적 성공작(xvision, NextAR, ClarifEye)은 애초에 그 플랫폼에 의존하지 않는다. 또한 Magic Leap One은 '작동 정지'가 아니라 2024-12-31 클라우드 서비스 종료·핵심 기능 EOL이다.
- '움직이지 않는 뼈에서만 AR이 성립한다'는 반례로 반박된다. InnerOptic은 연부조직 초음파 AR로 2009·2012년 FDA 클리어런스를 받았고(K083728, K121479, 제품코드 IYO), Adballah 2022(Surg Endosc, PMID 34734305)는 ex-vivo 간에서 AR이 표준 초음파 내비게이션보다 절제연이 더 정확했다고 보고한다.
- 'HoloAnatomy 2019년 Case Western 신교육과정 전면 도입', 'AlensiaXR 배포', 'PubMed Google Glass+surgery 82건', 'Google Glass 첫 성형수술 적용일 2013-10-29'는 이번 대조에서 1차 출처로 확인되지 않았다. 특히 '전통 해부 대비 최대 2배 빠른 학습'은 제조사·대학 홍보 문구이며 독립 검증이 없다 — Stojanovska 2020(PMID 34457656) 원문은 시신 73.8%±12.3 vs 혼합현실 74.2%±13.0으로 '차이 없음(p>0.05)'이 결론이다.
- SBF 제품코드 클리어런스 '2025년까지 35건'은 틀렸다. openFDA(마지막 갱신 2026-09-21) 기준 SBF 총 43건이며, 2025-12-31 기준으로는 40건이다. 35건은 2025-07-31(K250477)까지 자른 값이다. 게다가 같은 문서가 Augmedics K261854(2026-07-31)를 인용하고 출처란에 '조회 2026-09'라고 적어, 자기 데이터로 자기 수치를 반증한다. 누락된 8건: K252170(2025-08-08), K251737(2025-09-04), K252530(2025-09-10), K252054(2025-09-29), K251639(2025-10-03), K252847(2026-01-09), K253805(2026-04-24), K261854(2026-07-31).
- Pelanis 2021(Med Image Anal, PMID 33454603)을 '간 복강경 AR 실패 확인' 근거로 분류한 것은 원문 오독이다. 이 연구는 인간 임상이 아니라 돼지 4마리(four porcine models) 전임상시험이고, 저자 결론은 'The presented solution is accurate enough to be potentially clinically beneficial for surgical guidance in laparoscopic liver surgery' 즉 긍정이다. 또한 이 플랫폼은 로봇 C-arm + 투시영상 기반 내비게이션으로, 'HoloCare'(HoloLens 계열 스핀오프) 제품으로 귀속한 것도 부정확하다. TRE 3.78±1.89mm, 절제연 중앙값 4.44mm(최대 9.75mm) 수치 자체는 맞다.
- Navab CAMC의 '사체 43례 검증'은 존재하지 않는 수치다. Navab 2010(IEEE TMI, PMID 20659830) 초록은 cadaver studies를 언급할 뿐 43이라는 숫자를 제시하지 않는다. 43은 Weidert 2012(Unfallchirurg, PMID 22406917)의 '임상 적용 43례'이며, 같은 숫자를 사체 검증에 중복 적용했다.
- Ma 2025(Orthop Surg, PMID 39815419)의 '99.1% vs 91.7%(p<0.0001)'는 1차 분석 결과가 아니라 ATS(actual treatment set) 결과다. 사전 규정된 FAS(full analysis set) 민감도 분석은 98.0%(344/351) vs 91.7%(319/348), 차이 6.3%[2.9-9.8]이고 FAS 우월성 검정 p=0.0003이다. 여러 분석집합 중 가장 큰 차이(ATS 7.3%)를 골라 인용했다. 또 '699개 나사'는 실제 삽입 수가 아니라 계획 수(351+348)다.
- (외 11건)

## industry — 제조·산업·물류 분야의 증강현실 전개 (1990~2026)
항목 14개 · 검증 정정 지적 59건

> 산업 AR의 출발점은 소비자 욕구가 아니라 보잉의 배선(wire harness) 공장이었다. 1990~1992년 톰 카우델과 데이비드 미젤은 항공기 한 대에 수백 종씩 필요한 배선 조립 합판(formboard)을 매번 다시 그려야 하는 비용 문제를 풀려고 "augmented reality"라는 말을 지어냈다. 목표는 몰입이 아니라 도면 폐기였다. 1993년 파이너의 KARMA가 정비로, 1999~2003년 독일 ARVIKA 컨소시엄과 ARTESAS가 자동차·항공 정비로 이 계보를 넓혔다. 2010년대 초 스마트폰 센서와 SLAM이 싸지면서 2차 물결이 왔다. 구글 글래스는 소비자에서 참패(2015-01 단종)한 뒤 2017년 Glass Enterprise Edition으로 공장에 재취업했고, DHL은 2015년 vision picking 시범으로 물류 피킹을 열었다. 2015~2018년은 자본의 전성기였다. PTC가 퀄컴에서 Vuforia를 6,480만 달러에 샀고(2015-11-03), 매직리프는 35억 달러를, DAQRI는 2억 7,500만 달러를 모았다. 그러나 수익은 오지 않았다. DAQRI(2019-09)·Meta Company(2019-01)·ODG가 연쇄 도산했고, 마이크로소프트는 IVAS 최대 218.8억 달러 계약을 따고도 2023년 국방부 시험에서 "현 장비가 더 낫다"는 평가를 받았다. 2020년대는 정리의 시대다. TeamViewer가 Ubimax·Upskill·Viscopic을 흡수해 산업 AR 소프트웨어를 원격지원 한 줄로 압축했고, 구글은 2023-03-15 Glass Enterprise를 끝냈으며, PTC는 2024년 10-K에서 AR을 5대 핵심에서 빼 "부수 기술"로 강등했다. 마이크로소프트는 2025-10-14에 Dynamics 365 Guides·Remote Assist의 2026-12-31 지원 종료를 공지했다. 34년간 산업 AR은 사라지지 않았지만, 산업을 바꾸지도 못했다.


### 보잉 배선 하네스 AR — 'augmented reality'라는 말이 태어난 곳
| 항목 | 내용 |
| --- | --- |
| 주체 | Thomas P. Caudell, David W. Mizell — Boeing Computer Services, Research & Technology (시애틀) |
| 연도 | 1990(사내 프로젝트 시작) / 1992(HICSS-25 논문 발표) / 실용화 안 됨 |
| 수치 | 논문 인용수 1,398회(Semantic Scholar, 2026-09 조회). 발표지: Proceedings of the Twenty-Fifth Hawaii International Conference on System Sciences(HICSS-25), 1992. |
| 출처 | T. Caudell & D. Mizell, "Augmented reality: an application of heads-up display technology to manual manufacturing processes," HICSS-25, 1992 — 인용수는 Semantic Scholar Graph API(api.semanticscholar.org) 2026-09-29 조회. 배경은 https://en.wikipedia.org/wiki/Industrial_augmented_reality |

보잉 항공기 한 대에는 수 킬로미터의 전선 다발이 들어가고, 이를 조립하려면 기종·옵션마다 실물 크기 배선 도면을 합판(formboard)에 인쇄해 벽에 세워야 했다. 기종이 바뀔 때마다 이 합판을 새로 제작·보관·폐기해야 하는 것이 비용의 핵심이었다. 카우델과 미젤은 작업자에게 시스루 HMD를 씌우고 배선 경로를 실물 합판 위에 직접 겹쳐 그리면 물리적 도면 자체를 없앨 수 있다고 봤다. 이들이 이 기법을 부르려고 만든 용어가 'augmented reality'다. 논문 제목이 말해주듯 출발점은 '가상현실'이 아니라 'heads-up display 기술의 수작업 제조공정 적용'이었다.

AR을 부른 것은 그래픽 기술이 아니라 '다품종 소량 항공기 조립에서 도면 자체가 재고이자 비용'이라는 보잉 고유의 문제였다. VR처럼 세계를 대체할 이유는 없었고, 현실 위에 선 몇 개만 얹으면 충분했다.

용어와 개념은 학계 전체의 출발점이 됐지만, 프로젝트 자체는 생산 라인 표준으로 정착하지 못했다. 당시 HMD 무게·해상도·정합(registration) 정밀도가 실제 조립 허용오차를 못 따라갔다. 보잉은 이후 20년 넘게 AR 시범을 반복하게 된다.

### KARMA — 정비(maintenance)로 넘어간 AR
| 항목 | 내용 |
| --- | --- |
| 주체 | Steven K. Feiner, Blair MacIntyre, Dorée Seligmann — Columbia University |
| 연도 | 1993 |
| 수치 | 발표: Communications of the ACM, Vol.36 No.7, 1993, pp.53-62. |
| 출처 | https://en.wikipedia.org/wiki/Industrial_augmented_reality (세부 서지는 Feiner, MacIntyre, Seligmann, CACM 1993 — 인용수는 이번 조사에서 API 한도로 재확인 실패) |

KARMA(Knowledge-based Augmented Reality for Maintenance Assistance)는 레이저 프린터 정비를 대상으로 한 시스템이었다. 핵심은 하드웨어가 아니라 '무엇을 언제 보여줄지'를 규칙 기반 지식시스템(IBIS)이 자동 생성한다는 점이었다. 즉 AR을 '그래픽 문제'가 아니라 '설명 생성 문제'로 다룬 최초의 산업형 접근이다. 조립이 아니라 정비를 택한 것은, 정비가 숙련도 편차가 크고 매뉴얼이 두꺼워 비용이 큰 영역이었기 때문이다.

제조 현장에서 조립은 라인화·표준화로 비용을 줄일 수 있지만, 정비는 고장이 비정형이라 표준화가 안 된다. AR이 가장 먼저 붙을 자리는 그래서 정비였다.

상용화되지 않았으나 30년 뒤 Microsoft Dynamics 365 Guides, PTC Vuforia Expert Capture 등 '단계별 작업지시' 제품군이 모두 이 구조를 반복했다. 학술 계보로는 성공, 제품으로는 미발생.

### ARVIKA / ARTESAS / STAR — 독일이 국가 예산으로 산업 AR을 밀다
| 항목 | 내용 |
| --- | --- |
| 주체 | 독일 연방교육연구부(BMBF) 주관, Siemens 주도. 참여: Volkswagen, BMW, DaimlerChrysler, Audi, EADS(현 Airbus), Ford 유럽 등 20여 개 기관 |
| 연도 | ARVIKA 1999~2003 / ARTESAS 2004~2006 |
| 수치 | ARVIKA 참여기관 20여 곳(보고마다 상이). 총 예산 규모는 이번 조사에서 확인 실패. |
| 출처 | https://en.wikipedia.org/wiki/Industrial_augmented_reality |

ARVIKA는 '개발·생산·서비스에서의 증강현실'을 표방한 당시 세계 최대의 산업 AR 컨소시엄이었다. 자동차 차체 설계 검토, 엔진 조립 가이드, 정비 지원을 실제 공장에서 시험했다. 후속 ARTESAS는 자동차·항공 정비에 집중했다. 같은 시기 유럽-미국 공동의 STAR(Service and Training through Augmented Reality), 스웨덴·호주·일본의 유사 프로그램이 나왔다. 이 시기의 특징은 민간 수요가 아니라 산업정책이 AR을 끌고 갔다는 점이다.

독일 자동차·항공 산업은 1990년대 말 모델 다양화(플랫폼 공유·옵션 폭증)로 조립 지시서와 정비 매뉴얼이 폭증하는 문제를 안고 있었다. AR은 '종이 문서의 폭증'에 대한 답으로 제시됐다.

기술적 성과는 방대했으나 어느 프로그램도 양산 라인 상시 운용으로 이어지지 않았다. 당시 HMD는 무겁고, 추적(tracking)은 공장의 금속 반사·조명 변화에 취약했으며, 무엇보다 CAD 데이터를 현장에 실시간으로 내려보낼 IT 인프라가 없었다. 실패 원인은 광학보다 데이터 파이프라인 쪽이 컸다.

### 구글 글래스 — 소비자 참패 후 공장으로 재취업
| 항목 | 내용 |
| --- | --- |
| 주체 | Google X → Google(Glass at Work 프로그램). 산업 고객: AGCO(농기계), GE Aviation, Deutsche Post DHL Group, Sutter Health, H.B. Fuller, Boeing |
| 연도 | 2012-06-27 개발자판($1,500) / 2014-04-15 일반 판매 / 2015-01-15 소비자 단종 / 2017-07 Enterprise Edition / 2019-05-20 EE2 / 2023-03-15 생산·판매 종료 / 2023-09-15 지원 종료 |
| 수치 | Explorer Edition $1,500. 소비자 판매 기간 약 7개월(2014-04-15~2015-01-15). EE2 출시 2019-05-20, Snapdragon XR1 탑재. 생산 종료 2023-03-15, 지원 종료 2023-09-15. 구글 공식 블로그는 '생산시간 단축·품질 향상·비용 절감'을 언급했을 뿐 구체 수치는 제시하지 않음. |
| 출처 | https://en.wikipedia.org/wiki/Google_Glass ; https://blog.google/products/devices-services/glass-enterprise-edition-2/ |

구글 글래스는 소비자 시장에서 가격($1,500)과 프라이버시 반발로 공개 판매 7개월 만에 접혔다. 그런데 같은 하드웨어가 공장에서는 팔렸다. 2017년 Glass Enterprise Edition, 2019년 Snapdragon XR1 기반 EE2로 이어지며 조립 지시, 품질 검사, 창고 피킹에 투입됐다. 흥미로운 점은 산업용 전환의 이유가 기술이 아니라 맥락이었다는 것이다. 공장 작업자는 이미 보안경·헬멧을 쓰고 있어 '이상한 안경'이라는 사회적 비용이 0이었고, 한 대당 생산성 향상이 곧바로 원가로 환산됐다. 그럼에도 2023년 3월 구글은 이 제품군도 끝냈다.

AGCO 같은 다품종 소량 조립 업체는 작업자가 태블릿을 들었다 놨다 하는 시간 자체가 손실이었다. '핸즈프리'가 AR의 3D 그래픽보다 훨씬 강한 구매 동기였다. 실제로 Glass EE는 3D 정합조차 안 하는 단안 HUD였는데도 팔렸다.

실패. 기술적 이유보다 경제적 이유가 컸다. 단안 800×640급 HUD는 수백 달러 스마트폰으로 대체 가능한 기능이었고, 구글 입장에서 수천~수만 대 규모 기업 시장은 유지비를 정당화하지 못했다. 2023년 구글은 산업용 AR을 완전히 접고 Project Iris/AI 안경 쪽으로 이동했다.

### DHL vision picking — 'pick-by-vision'이 물류에 들어오다
| 항목 | 내용 |
| --- | --- |
| 주체 | DHL Supply Chain, 파트너 Ricoh·Ubimax(xPick), 하드웨어 Google Glass·Vuzix M100 계열 |
| 연도 | 2014(개념 보고서) / 2015(네덜란드 시범) / 2017(2차 확대) / 2019(다국 상용 배치) |
| 수치 | DHL이 공개적으로 반복 인용한 수치는 네덜란드 시범의 '효율 25% 향상'과 이후 배치의 '생산성 약 15% 향상'이다. ※ 이번 조사에서 dhl.com 원문 접근이 차단되어 두 수치 모두 1차 출처로 재확인하지 못했다(uncertain 참조). 시범 규모(작업자 10명, 3주, 약 2만 개 품목/9천 건 주문)로 널리 보도되나 역시 미확인. |
| 출처 | DHL Trend Research, "Augmented Reality in Logistics" (2014) 및 DHL 보도자료 — ※ 본 조사에서 원문 미확보. 관련 하드웨어·소프트웨어는 https://en.wikipedia.org/wiki/TeamViewer_(company) (Ubimax 인수 기록) |

창고 피킹에서 작업자는 종이 리스트나 핸드헬드 스캐너를 들고 통로를 걷는다. 한 손이 묶이고, 시선이 화면과 선반을 왕복한다. vision picking은 안경에 '몇 번 통로, 몇 번 칸, 몇 개'만 띄우고 바코드는 안경 카메라가 읽게 해 두 손을 자유롭게 만든다. DHL은 2014년 트렌드 리포트로 개념을 제시하고 2015년 네덜란드 창고에서 시범한 뒤, 2019년 여러 국가·사업장으로 확대했다. 여기서 AR은 3D 홀로그램이 아니라 사실상 '시야 안의 텍스트 한 줄'이며, 그것이 정확히 성공 요인이었다.

전자상거래 확산으로 주문 단위가 '팔레트'에서 '낱개 1개'로 바뀌면서 창고 인건비의 55~65%가 피킹에 몰렸고, 계절 성수기마다 단기 인력을 대량 투입해야 했다. 신입이 2주 걸려 익히던 동선을 안경이 대신 알려주면 교육기간이 사라진다 — 이것이 AR이 아니라 '교육비 절감'으로서의 구매 동기였다.

부분 성공. 산업 AR 중 가장 오래 살아남은 용례이지만, 같은 문제를 음성 피킹(voice picking, 1990년대부터 존재)과 손목형 스캐너가 더 싸게 풀 수 있었고, 아마존은 아예 로봇(Kiva, 2012 인수 $775M)으로 사람 동선 자체를 없앴다. AR 피킹은 '자동화가 경제성이 안 나오는 중간 규모 창고'라는 틈새에 남았다.

### 에어버스 MiRA / SART — 항공 조립 검사에 AR
| 항목 | 내용 |
| --- | --- |
| 주체 | Airbus (툴루즈), Testia(에어버스 자회사) |
| 연도 | 2011(MiRA 도입) / 2015(SART 발표) |
| 수치 | 널리 인용되는 수치는 'A380 동체 섹션의 브래킷 약 8만 개 검사를 3주에서 3일로 단축'이다. ※ 이번 조사에서 airbus.com 원문 페이지가 404/접근불가여서 1차 확인 실패(uncertain 참조). |
| 출처 | Airbus 보도자료 및 Testia 자료 — ※ 본 조사에서 원문 미확보(도메인 404). 수치는 2차 보도 기준. |

MiRA(Mixed Reality Application)는 태블릿을 A380 동체 내부에 비추면 3D 디지털목업(DMU)과 실물의 차이를 겹쳐 보여주는 검사 도구다. SART(Smart Augmented Reality Tool)는 조립 위치 마킹 등에 쓰였다. 핵심은 HMD가 아니라 태블릿이었다는 점 — 정합 정밀도가 중요한 검사 작업에서는 손에 든 화면이 오히려 실용적이었다. 항공기 동체 한 섹션에 수만 개의 브래킷이 있고, 각각이 도면대로 붙었는지 사람 눈으로 대조하는 것이 병목이었다.

항공기는 인증(certification) 산업이다. '도면대로 만들었다'는 증거를 남기는 비용이 제조 비용의 상당 부분을 차지한다. AR은 조립을 빠르게 한 게 아니라 '검사 기록을 자동으로 남기는' 역할로 들어갔다. 다른 산업에서 AR이 자주 실패한 이유가 여기서 드러난다 — 규제 증빙이 없는 산업에서는 AR의 ROI 계산이 훨씬 어렵다.

제한적 성공. 검사·마킹 등 좁은 작업에서는 정착했으나, 조립 라인 전반의 작업지시 수단으로 확산되지는 않았다. 태블릿 기반이어서 '핸즈프리'라는 AR의 대표 편익을 포기한 것이 역설적으로 생존 이유였다.

### DAQRI — 2억 7,500만 달러를 태우고 사라진 스마트 헬멧
| 항목 | 내용 |
| --- | --- |
| 주체 | DAQRI(로스앤젤레스), 공동창업 Brian Mullins·Gaia Dempsey. 투자 Tarsadia Investments 주도 |
| 연도 | 2010 설립 / 2014 Smart Helmet 발표 / 2017 Smart Glasses / 2019-09-09 자산매각·폐업 발표 |
| 수치 | 누적 조달 2억 7,500만 달러(2017-07 기준). 2013-06 시리즈A 1,500만 달러. 최대 직원 140명. 더블린(2015)·비엔나(2016) 사무소. 2017-10 직원 약 1/4 감원 및 공동창업자 사임. 2019-09-09 폐업 발표, 그달 안에 정리. |
| 출처 | https://en.wikipedia.org/wiki/Daqri |

DAQRI는 건설·석유화학·중공업 현장의 안전모를 그대로 AR 기기로 만들자는 접근이었다. Intel Core m7을 넣은 Smart Helmet은 3D 매핑, 열화상, 실시간 경보, 시각적 작업지시를 제공했다. 2017년에는 무겁다는 비판에 대응해 경량 Smart Glasses를 냈다. 회사는 Melon(EEG), ARToolworks(초기 AR 툴킷), 1066 Labs(디스플레이)까지 인수하며 수직계열화를 시도했다.

중공업 현장은 '기존 보호장구에 기능을 얹는다'는 논리가 통하는 유일한 곳이었다. 안전모는 어차피 써야 하니 추가 착용 저항이 0이라는 판단이었다.

완전 실패. 기술적으로는 헬멧이 무겁고(1kg 이상) 배터리가 짧았으며, 경제적으로는 대당 수천 달러 하드웨어를 팔면서 소프트웨어 생태계가 없어 반복 매출이 생기지 않았다. 하드웨어 자체 제조라는 선택이 치명적이었다 — 같은 시기 살아남은 회사들은 모두 소프트웨어였다.

### Meta Company와 ODG — 2019년 한 해에 무너진 AR 하드웨어 중간지대
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta Company — Meron Gribetz(컬럼비아대 재학 중 창업). 투자: Horizons Ventures, Tim Draper, Lenovo, Tencent |
| 연도 | Meta: 2012 설립 / 2016-03 Meta 2 발표($949) / 2018-09 직원 2/3 무급휴직 / 2019-01 채권자 압류·자산매각. ODG: 2018~2019 감원·자산경매 |
| 수치 | Meta: 킥스타터 $194,444(2013), 시리즈A $2,300만(2015), 추가 $5,000만(2016, Lenovo·Tencent 등). 직원 약 100명 중 2/3 무급휴직(2018-09). 2019-01 주채권자 압류 후 전 자산 매각, IP는 Meta View(현 Campfire)가 2019-05 인수. |
| 출처 | https://en.wikipedia.org/wiki/Meta_(augmented_reality_company) (ODG는 별도 위키 문서 부재 — uncertain 참조) |

Meta 2는 HoloLens($3,000)의 1/3 가격($949)에 더 넓은 시야각을 내세운 개발자용 AR 헤드셋이었다. 대신 PC에 유선으로 물려야 했다. Osterhout Design Group(ODG)은 군용 디스플레이 기술로 시작해 R-7/R-8/R-9 산업용 AR 안경을 냈고, 2017년 마이크로소프트에 특허 일부를 매각해 자금을 댔다. 둘 다 '소비자보다는 싸고 산업용으로는 쓸 만한' 중간지대를 노렸다.

2016년 전후는 'HoloLens가 너무 비싸다'는 인식이 산업계에 퍼진 시점이었다. 가격을 낮추면 공장 도입이 폭발하리라는 가설이 있었다.

실패. 그리고 가설이 틀렸음을 증명했다. 문제는 가격이 아니라 '한 대당 연간 절감액을 회계적으로 증명하기 어렵다'는 것이었다. 기업은 $3,000이 비싸서 안 산 게 아니라, 1,000대를 깔았을 때 무엇이 좋아지는지 계산이 안 돼서 안 샀다. 2019년 DAQRI·Meta·ODG가 같은 해 무너진 것은 우연이 아니다.

### PTC Vuforia — 세계 최대 AR SDK의 매출이 '무의미(immaterial)'했다
| 항목 | 내용 |
| --- | --- |
| 주체 | PTC Inc.(매사추세츠 니덤) ← Qualcomm Connected Experiences |
| 연도 | 2015-11-03 PTC가 퀄컴에서 인수 / 2021 성장 핵심축 / 2024 '부수 기술'로 강등 |
| 수치 | 인수가 $64.8M 현금(현금 인수분 $4.5M 제외 순액). 이 중 인수 무형기술 $41.2M, 영업권 $23.3M, 기술 상각 내용연수 6년. 인수 자금 중 $50.0M은 신용한도 차입. 인수 시점 직원 약 80명. 인수 직전 PTC의 IoT 부문 매출 $52.9M(FY2015) → $80.3M(FY2016). |
| 출처 | PTC Inc. Form 10-K, FY2016 (SEC accession 0000857005-16-000071), FY2021 (0001564590-21-057806), FY2024 (0000950170-24-127231) — SEC EDGAR 원문 직접 확인 |

Vuforia는 2010년대 초 가장 널리 쓰인 AR SDK였다. 그런데 PTC의 SEC 공시는 인수 시점 Vuforia의 '과거 연환산 매출이 재무적으로 무의미(immaterial)'했다고 명시한다. 즉 개발자 점유율 1위 AR 플랫폼이 돈을 벌지 못하고 있었다. PTC는 이를 CAD·PLM·IoT와 묶어 '작업자에게 3D 조립지시를 띄우는' 산업용 제품(Vuforia Studio, Expert Capture)으로 재포장했다. 2021년 10-K에서 PTC는 'IIoT와 AR 솔루션에서 더 큰 시장 성장 기회를 본다'고 썼다. 그러나 2024년 10-K에서 AR은 5대 핵심 솔루션(PLM·ALM·SLM·CAD·SaaS) 목록에서 빠지고, SaaS·AI·IoT와 함께 '가능화 기술(enabling technologies)'로 내려갔다.

PTC는 CAD·PLM 회사다. 이미 고객사의 3D 모델을 다 갖고 있으니, 그 모델을 현장 작업자 시야에 띄우는 것이 자연스러운 확장이라고 봤다. AR을 '새 시장'이 아니라 '기존 CAD 데이터의 마지막 배송 구간'으로 정의한 것이다.

제품은 살아남았으나 전략적 지위는 강등됐다. 2021년 '성장축' → 2024년 '부수 기술'로의 이동은 산업 AR 소프트웨어 최대 사업자의 판단이 바뀌었다는 가장 명확한 공시 증거다. 같은 자리를 AI가 가져갔다.

### 마이크로소프트 HoloLens와 IVAS — 218.8억 달러 계약, 그리고 '기존 장비가 더 낫다'
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft, 미 육군(US Army), Anduril Industries |
| 연도 | 2015-01 HoloLens 발표 / 2016-03-30 개발자판 $3,000 / 2019-02-24 HoloLens 2 발표 $3,500 / 2021-03-26 IVAS 양산계약 최대 $21.88B / 2023-01 DOT&E 부정 평가 / 2025-02 Anduril로 이관 |
| 수치 | IVAS 양산계약 최대 $21.88B(2021-03-26), 대상 근접전투부대 12만 명 이상. 2020-12 의회가 $1.1B 요구에서 $230M 삭감. 2022-03 시험 완료 전까지 약 $400M 집행 보류. 2022-09 초기 5,000대 인수 개시(당초 2021년 4만 대 목표에서 하향). 2023-09 차기 개발단계에 $95M 추가(시제 280대 포함). 2025-02 Anduril이 생산·개발·납기 관리 인수. |
| 출처 | https://en.wikipedia.org/wiki/Integrated_Visual_Augmentation_System ; https://en.wikipedia.org/wiki/HoloLens_2 ; https://learn.microsoft.com/en-us/hololens/hololens2-support (Azure Remote Rendering·WMR 폐기 공지) |

HoloLens 2는 산업 AR의 사실상 기준기가 됐다. 조립·정비·원격지원 소프트웨어들이 모두 이 기기 위에 지어졌다. 매출의 큰 축은 군이었다 — IVAS(Integrated Visual Augmentation System)는 보병 12만 명 이상에게 야시·조준·상황인식을 통합한 HMD를 보급하는 사업으로, 최대 218.8억 달러 규모였다. 그러나 2023년 1월 국방부 시험평가국(DOT&E) 보고서는 병사들이 두통·눈피로·메스꺼움 등 광범위한 신체 장애를 겪었고, '병사들은 IVAS보다 기존 장비로 임무를 더 잘 수행했다'고 결론지었다. 기기 발광이 수백 미터 밖에서 보인다는 지적까지 나왔다.

군은 AR의 ROI를 '생산성'이 아니라 '생존율'로 계산할 수 있는 거의 유일한 고객이었고, 예산 규모가 민간 산업 AR 시장 전체보다 컸다. 마이크로소프트가 HoloLens를 계속 만든 이유의 상당 부분이 이 계약이었다.

기술적 실패가 명확하게 문서화된 드문 사례다. 시야각·무게·발광·멀미는 모두 광학과 인체공학의 문제였지 소프트웨어 문제가 아니었다. HoloLens 2는 단종됐고(소프트웨어 업데이트만 2027-12-31까지), Windows Mixed Reality는 폐기됐으며, Azure Remote Rendering은 2025-09-30 서비스 종료됐다.

### TeamViewer의 산업 AR 싹쓸이 — Ubimax·Upskill·Viscopic
| 항목 | 내용 |
| --- | --- |
| 주체 | TeamViewer SE(독일 괴핑엔). 인수 대상: Ubimax(독일, xPick·xAssist), Upskill(미국, Skylight — 보잉 배선 사례의 그 회사), Viscopic(독일) |
| 연도 | 2020(Ubimax) / 2021(Upskill, Viscopic) |
| 수치 | 인수 시점: Ubimax 2020년, Upskill 2021년, Viscopic 2021년. ※ 인수 금액은 이번 조사에서 1차 출처 확인 실패(Ubimax는 약 €1.3억대로 보도됨 — uncertain 참조). |
| 출처 | https://en.wikipedia.org/wiki/TeamViewer_(company) |

2019년 상장한 원격제어 소프트웨어 회사 TeamViewer가 2020~2021년 산업 AR 소프트웨어 주요 업체를 연달아 사들여 'TeamViewer Frontline'으로 통합했다. 주목할 점은 인수자가 AR 회사도, 제조 소프트웨어 회사도 아닌 '원격 데스크톱 회사'였다는 것이다. 이는 산업 AR의 실제 킬러앱이 3D 조립지시가 아니라 '원격 전문가가 현장 화면을 보며 화살표를 그리는 것'으로 수렴했음을 보여준다. Ubimax의 xPick은 DHL vision picking의 소프트웨어이기도 했다.

코로나19가 결정적이었다. 2020년 국경이 닫히면서 장비 제조사의 서비스 엔지니어가 고객 공장에 못 갔다. '전문가를 비행기 태우는 비용'이라는 아주 구체적인 숫자가 갑자기 눈에 보였고, 원격지원 AR은 그 비용을 직접 대체했다. AR이 팔린 이유는 증강이 아니라 출장 금지였다.

산업 AR 소프트웨어 시장이 독립 시장으로 존속하지 못하고 원격지원 SaaS의 한 기능으로 흡수된 사건. 개별 회사로는 정상적 엑시트지만, 산업 AR이라는 카테고리로는 소멸에 가깝다.

### Vuzix — 산업용 스마트글라스 순수 사업자의 재무 실체
| 항목 | 내용 |
| --- | --- |
| 주체 | Vuzix Corporation(뉴욕 로체스터), 창업자 Paul Travers. 나스닥 VUZI |
| 연도 | 1997 설립 / 2013 M100 / 2017 M300 / 2019 Blade / 2021 매출 정점 / 2024 매출 반토막 |
| 수치 | 연매출(10-K 기준): 2016 $2.13M → 2018 $8.09M → 2020 $11.58M → 2021 $13.16M(정점) → 2022 $11.84M → 2023 $12.13M → 2024 $5.75M → 2025 $6.28M. 순손실: 2019 -$26.5M / 2021 -$40.4M / 2022 -$40.8M / 2023 -$50.1M / 2024 -$73.5M / 2025 -$32.3M. 2015-01 인텔 $25M 투자로 지분 30%(이후 10%로 희석). 직원 약 90명. |
| 출처 | Vuzix Corporation, SEC XBRL companyfacts (CIK 0001463972), us-gaap:Revenues / us-gaap:NetIncomeLoss, 10-K 연간 값 — data.sec.gov 직접 조회(2026-09-29). 회사 연혁은 https://en.wikipedia.org/wiki/Vuzix |

Vuzix는 DHL·아마존·의료 현장에 쓰인 산업용 단안 스마트글라스의 대표 공급사다. 2015년 1월 인텔이 2,500만 달러를 투자해 지분 30%를 확보하며 주목받았다. 그런데 SEC 제출 재무제표는 산업 AR 하드웨어 시장의 실제 크기를 잔인할 만큼 정확히 보여준다. 10년 넘게 '산업 현장 도입 사례'가 계속 보도됐지만, 이 회사의 연매출은 단 한 번도 1,320만 달러를 넘지 못했고 손실은 매년 매출의 3~13배였다.

2020~2021년 매출 증가는 코로나 원격지원 수요였다. 2024년 반토막은 그 수요가 사라졌음을 뜻한다. 즉 산업 AR 하드웨어의 수요는 산업 구조가 아니라 팬데믹이라는 일시적 조건에 얹혀 있었다.

생존했으나 확장 실패. 2016~2025년 누적 순손실 약 3억 5천만 달러에 대해 누적 매출은 약 8천만 달러다. '산업 AR이 도입되고 있다'는 서사와 실제 지불 규모 사이의 격차를 보여주는 가장 냉정한 숫자다.

### 매직리프의 기업용 선회 — 35억 달러의 방향 전환
| 항목 | 내용 |
| --- | --- |
| 주체 | Magic Leap(플로리다 플랜테이션). 투자: Google, Alibaba, Qualcomm, a16z, AT&T, NTT Docomo, 사우디 공공투자기금(PIF) |
| 연도 | 2014-10 구글 $540M 투자 / 2018-08-08 Magic Leap One $2,295 / 2020-04 직원 절반 감원·기업용 전환 / 2022-09-30 Magic Leap 2 / 2024-12-31 Magic Leap One 지원 종료 |
| 수치 | 누적 조달 최소 $3.5B(2024-08 기준). 구글 초기 $540M(2014-10), 시리즈C $827M(2015-12), 2016-02 약 $800M, 시리즈D $461M(2018-03), NTT Docomo $280M(2019-04), 2020-05 $350M, 사우디 PIF 누적 $750M. 기업가치: 2016-12 $4.5B → 2019 $6.4B → 2020-09 $450M(93% 하락) → 2021-10 $2B. Magic Leap One $2,295, 지원 종료 2024-12-31. |
| 출처 | https://en.wikipedia.org/wiki/Magic_Leap |

매직리프는 소비자·엔터테인먼트 AR을 표방하며 역대 AR 기업 최대 자금을 모았다. Magic Leap One은 2018년 AT&T를 통해 $2,295에 나왔으나 판매는 참담했다. 2020년 4월 코로나를 계기로 직원 약 절반을 감원하고 CEO를 교체하며 기업용(의료·제조·방산)으로 전면 선회했다. 2022년 Magic Leap 2는 처음부터 기업 전용으로 출시됐다. 사우디 PIF가 최대 주주가 되면서 회사는 사실상 국부펀드가 유지하는 조직이 됐다.

2020년 선회의 표면 이유는 코로나였지만 실질 이유는 소비자 판매 실패였다. 기업용은 '단가가 높고 수량이 적어도 되는' 시장이라 하드웨어 원가가 높은 회사에게 유일하게 남은 출구였다. 산업 AR로 넘어온 회사 상당수가 같은 경로를 밟았다 — 자발적 선택이 아니라 후퇴였다.

생존 중이나 자립 실패. 2024년 매직리프는 구글과 광학·기술 파트너십을 맺으며 사실상 부품·광학 공급자로 재정의됐다. 35억 달러를 쓰고 산업 AR 시장에서 독립 제품 회사로 자리잡지 못한 것은, 이 시장의 총 지불 규모 자체가 작다는 방증이다.

### 마이크로소프트의 철수 — Dynamics 365 Guides·Remote Assist 2026-12-31 종료
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft |
| 연도 | 2018 Remote Assist·2019 Guides 출시 / 2025-03-25 Remote Assist mobile 폐기 / 2025-10-14 종료 공지 / 2025-11-01 신규·갱신 구매 중단 / 2026-12-31 지원 종료 |
| 수치 | 지원 종료 2026-12-31. 구독 구매·갱신 가능 시한 2025-11-01(공지 후 불과 2주여서 사실상 즉시 중단). 공지일 2025-10-14. Remote Assist mobile 폐기 2025-03-25. Azure Remote Rendering 종료 2025-09-30. Windows Mixed Reality는 Windows 11 24H2에서 제거, SteamVR 연동은 2026-11까지. HoloLens 2 소프트웨어 업데이트는 2027-12-31까지. |
| 출처 | https://learn.microsoft.com/en-us/lifecycle/announcements/dynamics-365-guides-remote-assist-end-of-support (공지일 2025-10-14, 원문 직접 확인) ; https://learn.microsoft.com/en-us/dynamics365/mixed-reality/remote-assist/ra-overview ; https://learn.microsoft.com/en-us/hololens/hololens2-support |

Dynamics 365 Guides는 HoloLens용 홀로그래픽 작업지시 앱이고 Remote Assist는 원격 전문가 지원 앱이다. 이 둘은 지난 7~8년간 '산업 AR의 표준 제품'으로 불렸고, 전 세계 파트너사 수십 곳(PTC, Trimble, DXC, Taqtile, Kognitiv Spark 등)이 이 위에 사업을 세웠다. 마이크로소프트는 2025년 10월 14일 두 제품의 2026년 12월 31일 지원 종료를 공지했다. 종료 이후 앱은 작동하지 않으며 데이터만 Dataverse에 남는다. 대체재로는 '마켓플레이스의 다양한 혼합현실 솔루션'과 'Teams 모바일의 공간 주석 기능'을 제시했다 — 즉 직접적 후속 제품이 없다.

철수의 이유는 AR이 작동하지 않아서가 아니라, 같은 엔지니어링 자원을 Copilot/AI에 투입하는 편이 수익률이 압도적으로 높았기 때문이다. 산업 AR의 총 유효시장(TAM)이 마이크로소프트 규모 회사의 최소 사업 단위에 못 미쳤다는 것이 핵심이다.

산업 AR 소프트웨어 표준 플랫폼의 소멸. 2026년 말 이후 HoloLens 위에 구축된 수많은 기업 도입 사례가 마이그레이션 대상이 된다. 지난 10년간의 '산업 AR 도입 사례'들이 플랫폼과 함께 증발하는 셈이며, 이것이 기술 도입을 벤더 플랫폼에 의존할 때의 구조적 위험을 보여준다.

#### 검증에서 잡힌 정정
- 구글 글래스 '소비자 판매 기간 약 7개월(2014-04-15~2015-01-15)' — 산술 오류. 해당 구간은 정확히 9개월이다.
- 구글 글래스 '2012-06-27 개발자판($1,500)' — 2012-06-27은 Google I/O 발표 및 Glass Explorer 예약판매 개시일이고, 실제 Explorer Edition 기기 배포는 2013-04-16에 시작됐다(en.wikipedia.org/wiki/Google_Glass). 발표일을 출시일처럼 제시했다. 또한 2014-04-15는 '일반 판매' 개시가 아니라 재고가 하루 만에 소진된 1일 한정 판매였고, 상시 공개 판매는 2014-05-14부터다.
- 매직리프 '2014-10 구글 $540M 투자' / '구글 초기 $540M' — 구글 단독 투자가 아니다. 위키피디아는 'over $540 million from Google, Qualcomm, Andreessen Horowitz, and Kleiner Perkins'로 기재한다. 구글이 주도한 약 $542M 라운드 총액을 구글 한 곳의 투자액으로 귀속시켰다.
- 매직리프 조달 내역의 이중계상 및 자체 모순 — 카드가 나열한 개별 금액을 합하면 540+827+800+461+280+350+750 ≈ $4.0B로, 같은 카드가 명시한 '누적 조달 최소 $3.5B(2024-08 기준)'를 약 5억 달러 초과한다. 원인은 (a) '시리즈D $461M(2018-03)'이 이미 사우디 PIF 자금인데 'PIF 누적 $750M'로 다시 계상됐고, (b) '시리즈C $827M(2015-12)'와 '2016-02 약 $800M'이 동일한 시리즈C의 중복 기재로 보이기 때문이다(실제 시리즈C 공표액은 $793.5M, 2016-02-02).
- ARVIKA·ARTESAS 연도 모순 — 서사 본문은 '1999~2003년 독일 ARVIKA 컨소시엄과 ARTESAS가 자동차·항공 정비로 이 계보를 넓혔다'고 두 사업을 같은 기간으로 묶었으나, 같은 조사의 카드는 ARTESAS를 2004~2006으로 적었다. 같은 문서 안에서 충돌한다.
- ARVIKA/ARTESAS 카드의 출처-주장 불일치 — 유일한 인용처 en.wikipedia.org/wiki/Industrial_augmented_reality에는 ARVIKA 1999~2003, ARTESAS 2004~2006, 'Siemens 주도', '참여기관 20여 곳', 'Volkswagen·BMW·DaimlerChrysler·Audi·EADS·Ford 유럽' 중 어느 것도 없다. 해당 문서는 ARVIKA를 'BMBF가 후원한 최대 컨소시엄', ARTESAS를 'ARVIKA에서 파생'이라고만 서술하고 연도 범위도 참여사 명단도 제시하지 않는다. ARVIKA 단독 위키 문서는 존재하지 않는다(de.wikipedia.org/wiki/ARVIKA는 404).
- KARMA 카드의 출처-주장 불일치 — 인용된 URL(Industrial_augmented_reality)에는 공저자 Blair MacIntyre·Dorée Seligmann도, 'CACM Vol.36 No.7, 1993, pp.53-62'라는 서지도 없다. 해당 문서는 'Steven K. Feiner와 동료들이 1993년 레이저 프린터 정비 응용을 제안했다'고만 적는다. 서지 자체는 실재하지만 제시된 출처가 그것을 뒷받침하지 못한다.
- IVAS '최대 218.8억 달러 계약을 따고도' — $21.88B는 10년 생산계약의 상한(ceiling)이지 수령·확정 금액이 아니다. 같은 카드가 인용한 실제 집행 기록은 2020-12 의회 $230M 삭감, 2022-03 약 $400M 보류, 2023-09 $95M 추가로 두 자릿수 억 달러 수준이다. 상한을 실적처럼 읽히게 한 과장이다.
- IVAS '2023년 국방부 시험에서 현 장비가 더 낫다는 평가' — 시험 시점 오기. 해당 초기 운용시험(IOT&E)은 2022년 5~6월에 수행됐고, 2023-01 DOT&E 연례보고서가 그 결과를 'accomplished their missions better with their current equipment than with IVAS'로 평가한 것이다. 2023년에 시험이 있었던 것이 아니다.
- 매직리프 '35억 달러'를 2015~2018 자본 전성기에 배치 — 시대착오. $3.5B는 2024-08 기준 누적치로 2019 NTT Docomo $280M, 2020 $350M, 2021 $500M, 2023 PIF 라운드가 모두 포함된다. 서사가 지목한 창구(2015~2018)에 조달된 금액이 아니다.
- Vuzix 매출 추이의 선택적 생략 — '2016 $2.13M → 2018 $8.09M → 2020 $11.58M'으로 단조 상승처럼 제시했으나, SEC XBRL 실제값은 2019년 $6,670,604로 2018년 $8,094,368 대비 약 18% 하락했다. 하락 연도를 건너뛴 배열이다.
- Vuzix 누적 손익 반올림 — '2016~2025년 누적 순손실 약 3억 5천만 달러'는 SEC 10-K 실제 합계 $342.3M보다 약 8백만 달러 과대, '누적 매출 약 8천만 달러'는 실제 $83.2M보다 과소다. 둘 다 서사가 강조하려는 격차를 키우는 방향으로 어긋난다.
- DHL vision picking '효율 25% 향상'·'생산성 약 15% 향상' — 독립 검증 없음. DHL/Ubimax의 자체 마케팅 수치이며, 동료심사 논문이나 제3자 감사 근거를 찾지 못했다. 카드 스스로 'dhl.com 원문 접근 차단으로 1차 출처 재확인 실패'를 인정했음에도 서사 본문은 'DHL은 2015년 vision picking 시범으로 물류 피킹을 열었다'며 확정 사실처럼 서술한다. 시범 규모(작업자 10명·3주·2만 품목·9천 건)도 미확인이다.
- 에어버스 MiRA 'A380 브래킷 약 8만 개 검사를 3주에서 3일로 단축' — 독립 검증 없음. 카드 스스로 airbus.com 원문이 404여서 1차 확인에 실패했고 '2차 보도 기준'이라고 적었다. 에어버스 자체 홍보 수치가 인용 연쇄를 통해 순환 재생산된 전형적 사례로, 검증된 성과로 제시해서는 안 된다.
- 구글 글래스 기업 성과 — 카드 자신이 '구글 공식 블로그는 생산시간 단축·품질 향상·비용 절감을 언급했을 뿐 구체 수치는 제시하지 않음'이라 적었고, blog.google의 2019-05-20 EE2 포스트를 직접 확인한 결과도 동일하다(수치 0건). 즉 산업 AR 성과 주장 전반에 계량 근거가 부재하다.
- DAQRI '2014 Smart Helmet 발표' — 2년 오차. 위키피디아는 2014년을 개발 착수로, 실제 공개는 2016-01 CES로 기재한다.
- DAQRI '공동창업 Brian Mullins·Gaia Dempsey' — 창업자 누락. 위키피디아는 Philip Tolk을 공동창업자로 함께 명시한다.
- DAQRI '최대 직원 140명' — 성격 오기. 위키피디아의 140명은 '해산 시점' 인원이지 최대 인원이 아니다. '헬멧이 무겁고(1kg 이상)'라는 중량 수치도 인용된 위키 문서에 없는 미출처 값이다.
- HoloLens 2 'HoloLens 2 소프트웨어 업데이트는 2027-12-31까지' — 출처 불일치. 인용된 learn.microsoft.com/en-us/hololens/hololens2-support 페이지에는 그 날짜가 없다. 해당 페이지가 명시하는 것은 Azure Remote Rendering 2025-09-30 종료, Windows Mixed Reality의 Windows 11 24H2 제거, SteamVR 2026-11까지뿐이다.
- PTC Vuforia '6,480만 달러에 샀고' — 총 인수대가는 $69.2M이다. $64.8M은 인수한 현금 $4.5M을 차감한 순액이며, 10-K의 매입가 배분 총액은 $69,243K다. 서사 본문은 이 구분 없이 지급액인 것처럼 서술한다. 또한 '인수 자금 중 $50.0M은 신용한도 차입'은 FY2016 10-K 인수 주석(R51/R53)에서 확인되지 않는다.
- TeamViewer 'Upskill(미국, Skylight — 보잉 배선 사례의 그 회사)' — 오도. Upskill(구 APX Labs)은 2016년경 보잉 배선 조립 파일럿의 소프트웨어 공급사이지, 1990년 카우델·미젤의 보잉 프로젝트와는 무관하다. 같은 서사 안에 나란히 놓여 30년을 건너뛴 동일시가 발생한다. 인수 시점도 위키 기준 Ubimax 2020-07-15, Upskill 2021-03-02이며 인수가는 어느 쪽도 공시되지 않았다(Ubimax 약 €1.3억은 보도 추정치).
- 보잉 '항공기 한 대에 수백 종씩 필요한 배선 조립 합판(formboard)' — 미출처 수치. 인용된 어느 출처에도 '수백 종'이라는 값이 없다.
- [존재하지 않는 인용] PTC 항목 표제 '세계 최대 AR SDK의 매출이 "무의미(immaterial)"했다' — PTC FY2021·FY2024 10-K 전문을 추출해 확인한 결과 'immaterial'이 Vuforia나 AR 매출과 연결된 서술은 **없다**. 두 문서 모두 'Vuforia'는 정확히 1회 등장하며 매출 수치 자체가 공시되지 않는다. 실제 문구는 FY2016 10-K의 'At the time of the acquisition, Vuforia had approximately 80 employees and its historical annualized revenues were not material' — **퀄컴 소유 시절(2015) 인수 직전** 상태 서술이지 PTC의 10년 AR 실적 평가가 아니다. 출처: https://www.sec.gov/Archives/edgar/data/857005/000085700516000071/ptc9-30x1610xk.htm
- [인용 문서와 정면 모순] '같은 자리를 AI가 가져갔다' — PTC FY2024 10-K 원문은 AI를 Vuforia와 **동일한 'enabling technologies' 범주**에 넣는다: '...artificial intelligence software, our ThingWorx Internet of Things software, and our Vuforia augmented reality software.' 5대 solution은 PLM·ALM·SLM·CAD·SaaS이며 AI도 여기 없다. AI가 AR 자리를 대체했다는 서술은 근거 문서가 반박한다.
- [전제 오류] 'AR을 5대 핵심에서 뺐다' — FY2021 10-K에 'AR이 5대 핵심'인 목록은 존재하지 않는다. FY2021은 CAD·PLM·IIoT·AR의 **4대 시장**을 서술하고, FY2024의 5대 solution(PLM/ALM/SLM/CAD/SaaS)은 다른 분류 체계다. 또한 IoT(ThingWorx)도 AR과 동일하게 enabling technology로 내려갔으므로 'AR만의 강등'은 성립하지 않는다.
- [기원 왜곡] '산업 AR의 출발점은 보잉' — 조사가 인용한 위키피디아 AR 문서 자체가 1968년 Sutherland 광학 시스루 HMD, 1975년 Krueger Videoplace를 앞에 두고, **최초 작동 몰입형 AR 시스템은 1992년 미 공군 Armstrong Labs의 Louis Rosenberg 'Virtual Fixtures'**라고 명시한다('the first immersive augmented reality system ever built'). 카우델·미젤 논문 제목도 'an application of **heads-up display technology**' — 군용 항전 HUD의 응용임을 스스로 밝힌다. 보잉이 만든 것은 필드가 아니라 용어다.
- [숫자 오류] 구글 글래스 '소비자 판매 기간 약 7개월(2014-04-15~2015-01-15)' — Explorer Edition은 **2013-04-16부터** 최종 사용자에게 배송·판매됐다(위키피디아 Google Glass: 'Google Glass was launched in 2013 but pulled in 2015'). 실제 기간은 약 **21개월**이지 7개월이 아니다. 2014-04-15는 1일 한정 일반 판매일일 뿐 판매 시작일이 아니다.
- [인과 역전] '소비자에서 참패(2015-01 단종)한 뒤 2017년 Glass Enterprise Edition으로 공장에 재취업했다' — 구글의 기업 트랙('Glass at Work' 인증 파트너 프로그램)은 **2014년**에 이미 가동됐고, DHL의 Glass 기반 vision picking 시범도 소비자 Glass가 아직 판매 중이던 2014~2015년에 진행됐다. 기업 용도는 소비자 실패의 *결과*가 아니라 **병행**이었다. '실패 후 전환'이라는 인과 고리는 만들어진 것이다.
- [시점 오류 ~5~7년] '2010년대 초 스마트폰 센서와 SLAM이 싸지면서 2차 물결이 왔다' — 모바일 AR 2차 물결은 2008~2009년 GPS·나침반 기반 POI 브라우저(Wikitude World Browser 2008-10, Layar 2009)와 마커 추적(ARToolKit 1999)으로 시작했고 **SLAM과는 무관**했다. SLAM이 상품화된 것은 훨씬 뒤로, Wikitude가 자사 SLAM을 출시한 해가 **2017년**, ARKit 발표가 **2017-06-05**다. 원인으로 지목한 기술이 결과보다 8년 늦다.
- [선행연구 무시] 'DHL은 2015년 vision picking 시범으로 물류 피킹을 열었다' — pick-by-vision은 DHL보다 6년 앞서 학술·실환경 검증이 끝나 있었다. Reif & Günthner, 'Pick-by-vision: augmented reality supported order picking', The Visual Computer, **2009**(피인용 98); Reif, Günthner & Schwerdtfeger, 'Pick-by-Vision comes on age: evaluation of an augmented reality supported picking system in a **real storage environment**', 2009(피인용 42); Schwerdtfeger, 'Pick-by-vision: bringing HMD-based augmented reality into the warehouse', 2012 — 모두 TU Münch
- (외 29건)

## education
항목 15개 · 검증 정정 지적 47건

> 교육에서의 AR은 기술이 준비돼서가 아니라 "눈에 보이지 않는 3차원을 가르칠 방법이 없다"는 오래된 곤란에서 출발했다. 1999년 가토 히로카즈의 ARToolKit이 웹캠과 종이 마커만으로 정합 문제를 공짜로 풀어주자 예산 없는 교실 연구가 가능해졌다. 2000~2003년 빈 공대의 Construct3D는 입체기하의 공간지각 문제를, 2001년 HIT Lab NZ의 MagicBook은 "책에서 3D로 넘어가는 전이(transitional) 인터페이스"를 제시했고, 2002년 셸턴·헤들리는 지구-태양 관계 오개념을 겨냥했다. 그러나 2006년 커라월라의 초등 과학 실험은 AR을 쓴 아이들이 전통 교구를 쓴 아이들보다 오히려 덜 몰입했다고 보고했다 — 이 분야 최초의 신뢰할 만한 음(陰)의 결과다. 2007~2009년 MIT·하버드의 핸드헬드 AR 시뮬레이션은 무대를 야외 탐구로 옮겼지만 인지부하와 기기 관리라는 한계를 스스로 기록했다. 2013~2014년 Wu와 Radu의 종합 리뷰가 의제를 정리하자 2014년 이후 메타분석이 쏟아졌다. 값은 0.56에서 0.90까지 흩어졌고, 표본은 대개 100명 미만·1회성·연구자 자작 시험지였다. 2016년 포켓몬 GO가 AR을 대중화했지만 BMJ 연구는 늘어난 걸음 수가 6주 만에 사라졌음을 보여줬다 — 신기효과 감쇠를 가장 깨끗하게 계량한 자료다. 2015~2021년 Junaio·HP Reveal·Google Expeditions가 차례로 죽으며 교사들이 만든 콘텐츠도 함께 사라졌고, HoloLens 기반 해부학 RCT는 시신 해부와 "차이 없음"을 보고했다. 남은 것은 값싸고 지루한 도구와, 효과크기 대신 설계와 지속성을 묻는 질문이다.


### ARToolKit — 교육 AR의 물적 토대
| 항목 | 내용 |
| --- | --- |
| 주체 | 가토 히로카즈(Hirokazu Kato, 나라선단과학기술대학원대), 마크 빌링허스트(Mark Billinghurst, 워싱턴대 HIT Lab) |
| 연도 | 1999(논문) / 2001(오픈소스 v1.0) / 2015-05-13(DAQRI v5.2 재공개) |
| 수치 | Kato & Billinghurst(1999) IWAR 논문 Crossref 피인용 1,086회(2026-09-29 기준). 오픈소스 v1.0은 2001년, DAQRI 인수 후 v5.2 재공개는 2015-05-13. |
| 출처 | Kato H., Billinghurst M., "Marker tracking and HMD calibration for a video-based augmented reality conferencing system", Proc. 2nd IEEE/ACM IWAR, 1999, DOI 10.1109/IWAR.1999.803809 (Crossref 피인용 1,086) / Wikipedia "ARToolKit" |

흑백 사각 마커를 단일 웹캠으로 인식해 카메라의 6자유도 자세를 실시간 추정하는 C/C++ 라이브러리다. 원래는 원격 화상회의용 AR 시스템의 마커 추적·HMD 캘리브레이션 기법으로 발표됐다. 2001년 워싱턴대 HIT Lab이 오픈소스로 공개하면서 사실상 표준이 됐고, Symbian(2005)·iPhone 3G(2008)·Android(2010)로 이식됐다. 2010년대 초까지 AR 교육 연구 논문의 대다수가 이 라이브러리 위에 만들어졌다.

교육 연구자에게는 1990년대 AR의 전제조건(HMD, 자기식/광학식 트래커, 워크스테이션)을 살 예산이 없었다. ARToolKit은 프린터로 뽑은 종이 마커와 저가 웹캠만으로 '정합(registration)' 문제를 무료로 해결했다. 즉 교육이 AR을 받아들인 첫 이유는 교육학이 아니라 '공짜'였다.

성공했지만 주인이 사라졌다. DAQRI가 인수해 v5.2를 오픈소스로 재공개했으나 DAQRI가 2019년 9월 폐업하면서 유지보수 주체가 소멸했고, 커뮤니티 포크(artoolkitX)와 마커리스 SDK(Vuforia·ARKit·ARCore)로 흡수됐다.

### Construct3D — 입체기하 교육용 AR
| 항목 | 내용 |
| --- | --- |
| 주체 | 한네스 카우프만(Hannes Kaufmann), 디터 슈말슈티크(Dieter Schmalstieg), 미하엘 바그너(Michael Wagner) — 빈 공과대학교 |
| 연도 | 2000(EAIT 논문) / 2002(SIGGRAPH) / 2003(Computers & Graphics 평가 논문) |
| 수치 | Kaufmann, Schmalstieg & Wagner(2000) Education and Information Technologies 5(4) Crossref 피인용 202회. Kaufmann & Schmalstieg(2003) Computers & Graphics 27(3):339-345 Crossref 피인용 338회(2026-09-29 기준). |
| 출처 | Kaufmann H. et al., "Construct3D: A Virtual Reality Application for Mathematics and Geometry Education", Education and Information Technologies, 2000, DOI 10.1023/A:1012049406877 / Kaufmann & Schmalstieg, "Mathematics and geometry education with collaborative augmented reality", Computers & Graphics 27(3), 2003, DOI 10.1016/S0097-8493(03)00028-1 |

Studierstube 플랫폼 위에 만든 시스루 HMD 기반 3D 기하 작도 시스템이다. 학생 여러 명이 같은 공간에서 같은 입체 도형을 보며 점·선·면·회전체를 직접 손으로 작도한다. 종이 위의 2D 투상도를 머릿속에서 3D로 복원해야 하는 단계를 아예 건너뛰게 만드는 것이 설계 의도였다. 오스트리아 고등학교 '기술도학(Darstellende Geometrie)' 과목과 대학 기하 수업에서 반복 평가됐다.

기술도학·입체기하는 공간지각 능력이 낮은 학생을 대량으로 탈락시키는 과목이었다. 교사들은 '학생이 투상도를 3D로 못 읽는다'는 문제를 수십 년간 안고 있었고, AR은 그 변환 단계를 없애는 유일한 후보였다. 기술 성숙이 아니라 이 특정 병목이 채택 이유였다.

학문적으로는 성공(AR 교육 연구의 표준 인용 사례)했지만 보급은 실패했다. HMD·트래커 세트가 학급 단위로는 감당 불가능한 가격이었고, Studierstube는 연구용 플랫폼이라 학교 IT 환경에 이식되지 않았다. 평가 표본도 수십 명 규모에 그쳤다.

### MagicBook — 전이 인터페이스
| 항목 | 내용 |
| --- | --- |
| 주체 | 마크 빌링허스트, 가토 히로카즈, 이반 포퍄레프(Ivan Poupyrev) — 워싱턴대/캔터베리대 HIT Lab, ATR |
| 연도 | 2001(Computers & Graphics 논문, CHI'01 Extended Abstracts, SIGGRAPH 2001 Emerging Technologies) |
| 수치 | Computers & Graphics 25(5):745-753, Crossref 피인용 356회. CHI'01 Extended Abstracts pp.25-26, Crossref 피인용 113회(2026-09-29 기준). Google Scholar 기준 값은 이보다 훨씬 크다. |
| 출처 | Billinghurst M., Kato H., Poupyrev I., "The MagicBook: a transitional AR interface", Computers & Graphics 25(5), 2001, DOI 10.1016/S0097-8493(01)00117-0 |

실제 종이책에 마커를 인쇄하고, 학습자가 핸드헬드 디스플레이로 페이지를 보면 그림 위에 3D 장면이 솟아오르는 장치다. 핵심은 '전이(transitional)'라는 개념 — 현실(책 읽기) → AR(책 위의 3D) → 몰입형 VR(장면 안으로 들어가기)로 스위치 하나로 연속 이동한다. 여러 사람이 같은 책을 동시에 보며 누구는 AR 관찰자로, 누구는 VR 내부 참가자로 존재할 수 있다. 교육용 제품이 아니라 인터페이스 연구 데모였지만, 이후 20년간 'AR 교과서'라는 상상의 원형이 됐다.

2000년 전후 VR 교육은 '몰입은 되는데 교실·교사·교재와 단절된다'는 벽에 부딪혀 있었다. MagicBook은 기존 인쇄 교재를 버리지 않고 증강한다는 타협안을 제시했고, 이것이 교육계에 먹혔다. 즉 AR이 교육에 들어온 논리는 '더 좋은 몰입'이 아니라 '기존 교재와의 연속성'이었다.

개념적으로는 대성공, 제품으로는 미출현. 'AR 팝업북'은 2010년대 내내 상업적으로 반복 시도됐으나(Popar, Disney, ColAR/Quiver 등) 콘텐츠 제작비와 앱 수명 문제로 대부분 단명했다.

### 셸턴·헤들리의 지구-태양 관계 실험 — 과학 오개념 교정
| 항목 | 내용 |
| --- | --- |
| 주체 | 브렛 셸턴(Brett E. Shelton), 닉 헤들리(Nicholas R. Hedley) — 워싱턴대 |
| 연도 | 2002 |
| 수치 | IEEE ART'02(The First IEEE International Augmented Reality Toolkit Workshop) 게재, Crossref 피인용 176회(2026-09-29 기준). |
| 출처 | Shelton B.E., Hedley N.R., "Using augmented reality for teaching Earth-Sun relationships to undergraduate geography students", IEEE ART 2002, DOI 10.1109/ART.2002.1106948 |

학부 지리학 수강생에게 ARToolKit 기반으로 지구·태양·자전축을 손에 든 마커 위에 띄워 계절·주야·황도 개념을 가르친 준실험이다. 사전·사후 검사로 오개념 변화를 측정했고, AR 조작 후 계절 발생 원인에 대한 오답이 줄었다고 보고했다. 표본이 작고 통제집단 설계가 약해 인과 주장은 제한적이다. 그럼에도 '천문 오개념'이라는 구체적 교육 문제에 AR을 겨눈 최초의 정량 연구로 계속 인용된다.

계절·달의 위상 같은 천문 개념은 관찰자가 시스템 바깥에서 볼 수 없다는 구조적 이유로 세계 어디서나 오개념률이 높았다. 교과서 삽화는 시점을 고정하고, 실물 모형은 크기·움직임을 왜곡한다. AR은 '학습자가 시점을 들고 돌릴 수 있다'는 점에서 이 문제에 정확히 대응했다.

부분적 성공. 이후 천체 AR은 SkyView·Star Walk 같은 소비자 앱으로 대중화됐지만, 정규 교육과정 안에서의 오개념 교정 효과는 후속 메타분석에서도 일관되게 재현되지 않았다.

### 커라월라의 "Making it real" — 최초의 명확한 음의 결과
| 항목 | 내용 |
| --- | --- |
| 주체 | 루신다 커라월라(Lucinda Kerawalla), 로즈메리 러킨(Rosemary Luckin), 시몬 셀리에플로트(Simon Seljeflot), 애덤 울라드(Adam Woolard) — 런던대/서식스대 |
| 연도 | 2006 |
| 수치 | Virtual Reality 10(3-4), Crossref 피인용 380회 / Semantic Scholar 600회(2026-09-29 기준). 실험 대상 10세 아동. |
| 출처 | Kerawalla L., Luckin R., Seljeflot S., Woolard A., "'Making it real': exploring the potential of augmented reality for teaching primary school science", Virtual Reality 10(3-4), 2006, DOI 10.1007/s10055-006-0036-4 |

10세 아동을 대상으로 AR '가상 거울' 인터페이스와 전통적 과학 교구를 비교한 교실 연구다. 교사-아동 대화를 담화 분석해 참여도와 학습 기회를 측정했다. 결과는 예상과 반대였다 — AR을 쓴 아이들이 전통 교구를 쓴 아이들보다 덜 몰입했다. 저자들은 교사가 내용을 수정할 수 없는 고정 콘텐츠, 탐색 안내 부재, 제한된 수업 시간, 교육과정 요건 불일치를 네 가지 설계 요구사항으로 정리했다.

2000년대 중반은 AR 교육이 데모 단계에서 실제 교실로 넘어가던 시점이었고, 영국 학교는 이미 교육용 CD-ROM 실패를 겪은 뒤였다(같은 저자가 2005년에 가정용 교육 소프트웨어 사용시간이 주당 10~25분으로 급락한다는 연구를 낸 바 있다). 즉 이 연구는 'AR이 효과 있나'가 아니라 '왜 교실 기술은 늘 실패하나'라는 물음의 연속선에 있었다.

실패 사례로서 가장 값진 결과. 기술적 이유(정합 오류·조작 난이도)와 제도적 이유(교사가 콘텐츠를 못 고침, 교육과정과 불일치)를 분리해 지목했고, 후자가 결정적이라고 봤다. 이 지적은 20년 뒤 HP Reveal·Google Expeditions 종료로 다시 입증된다.

### 핸드헬드 참여형 AR 시뮬레이션 — Environmental Detectives / Alien Contact!
| 항목 | 내용 |
| --- | --- |
| 주체 | 에릭 클롭퍼(Eric Klopfer)·커트 스콰이어(Kurt Squire) — MIT Teacher Education Program / 매트 던리비(Matt Dunleavy)·크리스 디디(Chris Dede)·레베카 미첼 — 래드퍼드대·하버드 교육대학원 |
| 연도 | 2007(Klopfer & Squire, ETR&D) / 2008-2009(Dunleavy·Dede·Mitchell, JOST) |
| 수치 | Klopfer & Squire, ETR&D, Crossref 피인용 614회. Squire & Klopfer, Journal of the Learning Sciences, 312회. Dunleavy, Dede & Mitchell, Journal of Science Education and Technology, 1,044회(2026-09-29 기준). |
| 출처 | Klopfer E., Squire K., "Environmental Detectives — the development of an augmented reality platform for environmental simulations", ETR&D, DOI 10.1007/s11423-007-9037-6 / Dunleavy M., Dede C., Mitchell R., "Affordances and Limitations of Immersive Participatory Augmented Reality Simulations for Teaching and Learning", JOST, DOI 10.1007/s10956-008-9119-1 |

GPS와 PDA(뒤에 스마트폰)를 이용해 학교 운동장·캠퍼스 자체를 무대로 삼은 위치기반 AR 시뮬레이션이다. Environmental Detectives는 학생이 가상의 화학물질 유출 사건을 현장에서 조사하게 하고, Alien Contact!는 수학·과학·언어 데이터를 현장 단서로 흩뿌린다. 학생은 역할(화학자·기자 등)을 나눠 맡고 각자에게 다른 정보가 주어져 협업이 강제된다. 두 연구 모두 참여도 상승을 보고하는 동시에 한계를 명시했다 — 인지 과부하, 기기 관리 부담, GPS 오차와 배터리 같은 기술적 실패.

과학교육은 '진짜 탐구(authentic inquiry)'를 원했지만 실제 오염 사고 현장에 학생을 데려갈 수 없었다. 동시에 2000년대 중반 미국 학교에는 PDA와 무선망이 막 보급돼 있었다. 즉 AR은 '위험하거나 존재하지 않는 현장을 학교 부지에 겹쳐놓는' 값싼 방법으로 채택됐다.

영향력은 컸으나 확산은 실패. 던리비 논문은 Crossref 피인용 1,044회로 이 분야 최상위권이지만, 기기 배포·GPS 정확도·교사 훈련 비용 때문에 연구 프로젝트 밖으로 나가지 못했다. 위치기반 교육 AR의 실질적 대중화는 2016년 포켓몬 GO가 소비자 쪽에서 해냈다.

### 종합 리뷰의 등장 — Wu(2013)와 Radu(2014)
| 항목 | 내용 |
| --- | --- |
| 주체 | 우 흐시우-핑(Hsin-Kai Wu) 외 — 대만사범대 / 율리안 라두(Iulian Radu) — 조지아공대 |
| 연도 | 2013 / 2014 |
| 수치 | Wu et al.(2013) Computers & Education 62:41-49, Crossref 피인용 1,832회. Radu(2014) Personal and Ubiquitous Computing 18(6), Crossref 686회 / Semantic Scholar 860회. Radu가 분석한 비교 연구 26편(2026-09-29 기준). |
| 출처 | Wu H-K., Lee S.W-Y., Chang H-Y., Liang J-C., "Current status, opportunities and challenges of augmented reality in education", Computers & Education, 2013, DOI 10.1016/j.compedu.2012.10.024 / Radu I., "Augmented reality in education: a meta-review and cross-media analysis", 2014, DOI 10.1007/s00779-013-0747-y |

Wu 외(2013)는 Computers & Education에 AR 교육의 현황·기회·도전을 정리해 이 분야의 의제를 설정했다. Radu(2014)는 AR과 비AR을 비교한 26편의 선행 연구를 메타리뷰해 긍정 효과와 부정 효과를 나란히 목록화했다. 부정 효과로는 주의 터널링(attention tunneling), 사용성 난이도, 인지 과부하, 교실 통합의 어려움을 꼽았다. 두 논문 모두 개별 실험의 효과크기 통합이 아니라 '무엇이 효과를 만드는가'의 요인 분해를 시도했다는 점이 중요하다.

2010년대 초 스마트폰 보급으로 AR 교육 논문이 폭증했지만, 서로 다른 기기·과목·측정도구를 쓴 소규모 연구들이라 비교가 불가능했다. 정리 없이는 연구비 심사도 교육정책 판단도 할 수 없는 상태였다.

성공. 이 두 편이 기준점을 만든 뒤 2014년부터 메타분석이 쏟아졌다. 다만 Radu가 지적한 부정 효과 목록은 이후 메타분석들이 평균값을 보고하는 과정에서 대체로 묻혔다.

### 1세대 메타분석 — 효과크기 0.56~0.68
| 항목 | 내용 |
| --- | --- |
| 주체 | 마크 산토스(Marc Ericson C. Santos) 외 — NAIST / 하칸 테케데레·하니페 괴케르 — 터키 / 무자페르 외즈데미르 외 — 터키 / 후안 가르손·후안 아세베도 — 콜롬비아 |
| 연도 | 2014(Santos) / 2016(Tekedere & Göker) / 2018(Özdemir) / 2019(Garzón & Acevedo) |
| 수치 | Santos(2014): 87편 검토 → 43편 사용자 연구 → 7편 효과크기 계산, 평균 ES=0.56. Tekedere & Göker(2016): 171편 중 15편(2005-2015), ES=0.677. Özdemir 외(2018): SSCI 16편(2007-2017). Garzón & Acevedo(2019): 64편, N=4,705(2010-2018), d=0.68, p<.001, Semantic Scholar 피인용 432회. |
| 출처 | Santos M.E.C. et al., IEEE Trans. Learning Technologies 7(1), 2014, DOI 10.1109/TLT.2013.37 / Tekedere H., Göker H., Int. J. of Environmental and Science Education 11(16), 2016 (ERIC) / Özdemir M. et al., Eurasian Journal of Educational Research, 2018 (ERIC) / Garzón J., Acevedo J., Educational Research Review 27, 2019, DOI 10.1016/j.edurev.2019.04.001 |

AR 교육 효과를 처음으로 수치화한 네 편의 메타분석이다. Santos(2014)는 87편의 논문 중 사용자 연구가 있는 43편, 그중 효과크기 계산이 가능한 7편만으로 평균 0.56을 얻었고 범위가 '작은 음의 효과부터 큰 효과까지' 흩어진다고 명시했다. Tekedere & Göker(2016)는 171편 중 15편으로 ES=0.677. Özdemir 외(2018)는 SSCI 등재 16편(2007-2017)을 분석해 모바일 기기에서 효과크기가 가장 컸고 웹캠 기반에서 가장 작았으며, 학년 수준에 따른 차이는 유의하지 않다고 보고했다. Garzón & Acevedo(2019)가 64편·학습자 4,705명으로 d=0.68을 내놓으며 이 세대의 표준 인용값이 됐다.

2014년 무렵 '교육용 AR이 정말 효과가 있느냐'는 질문이 연구비·교육청 조달 결정과 직결되기 시작했다. 개별 실험은 표본 30~80명짜리가 대부분이라 근거가 되지 못했고, 메타분석이 유일한 답변 형식이었다.

수치는 얻었지만 신뢰도는 취약하다. Santos의 경우 87편 중 효과크기를 뽑을 수 있었던 논문이 7편뿐이라는 사실 자체가 이 분야의 보고 관행이 얼마나 허술했는지를 보여준다. Garzón & Acevedo의 64편·4,705명은 연구당 평균 약 74명 — Cheung & Slavin이 효과크기를 2배로 부풀린다고 지목한 '소규모 시행'의 전형이다.

### 2세대 메타분석 — 0.38(인지부하 감소)부터 0.93(언어)까지의 분산
| 항목 | 내용 |
| --- | --- |
| 주체 | 후안 가르손 외(Educational Research Review 2020) / 잉 차이·즈룽 판·민 류(JCAL 2022) / 장신이(Hsin-Yi Chang) 외(Computers & Education 2022) / 거거 리·헝 뤄·디 천(Education Sciences 2024) / 주슈치 외(Smart Learning Environments 2026) |
| 연도 | 2019~2026 |
| 수치 | Garzón 외(2020): 46편, Crossref 피인용 232회. Cai 외(2022): 21편(2008-2020), 언어 이득 0.93 / 동기 0.42, RVE 추정. Chang 외(2022): 134편(2012-2021), Crossref 263회. Li 외(2024): 237편 검토 중 실험 60편, g=0.896, 95% CI [0.685, 1.107]. 이을마즈 & 바트드(2021) 과학 24편 g=0.602. 주 외(2026): 27편, 인지부하 g=-0.383, 95% CI [-0.740, -0.027], I²=92.7%, Egger p=0.072. |
| 출처 | Garzón J. et al., Educational Research Review 31, 2020, DOI 10.1016/j.edurev.2020.100334 / Cai Y., Pan Z., Liu M., Journal of Computer Assisted Learning, 2022 (ERIC) / Chang H-Y. et al., Computers & Education 191, 2022, DOI 10.1016/j.compedu.2022.104641 / Li G., Luo H., Chen D., Education Sciences, 2024 / Zhu X., Peng K., Yu S., Smart Learning Environments, 2026 (ERIC) |

2세대 메타분석은 '평균이 얼마냐'에서 '무엇이 조절하느냐'로 질문을 바꿨다. Garzón 외(2020)는 46편을 학습이론별로 나눠 협력학습(collaborative) 설계에서 효과가 가장 컸다고 보고했다 — 기술이 아니라 교수설계가 변수라는 것. Cai 외(2022)는 언어 학습 21편에서 학습 이득 0.93, 학습 동기는 0.42로 '성적은 크게 오르고 동기는 별로'라는 비대칭을 드러냈다. Chang 외(2022)는 10년치 134편을 훑어 처치 기간이 유의한 조절변수이고 3D 시각화가 자동으로 좋은 게 아니라고 경고했다. Li 외(2024)는 고등교육 60편에서 g=0.896으로 매우 큰 값을 냈고, 주 외(2026)는 인지부하가 g=-0.383만큼 줄지만 이질성이 I²=92.7%로 극단적이라고 보고했다.

1세대가 내놓은 0.5~0.7이라는 값이 정책 문서에 인용되기 시작했지만, 같은 기술로 왜 어떤 수업은 되고 어떤 수업은 안 되는지 설명하지 못했다. 조달 담당자에게 필요한 것은 평균이 아니라 조건이었다.

조절변수는 밝혀졌지만 분산 문제는 해결되지 않았다. 동일 기술에 대해 0.38에서 0.90까지 값이 흩어지고 이질성 I²가 90%를 넘는다는 것은 통합 평균 자체가 해석 가치를 잃었다는 뜻이다. 교과·설계·기간이 다르면 AR은 같은 개입이 아니다.

### 포켓몬 GO — 대중화와 신기효과 감쇠의 자연실험
| 항목 | 내용 |
| --- | --- |
| 주체 | 나이앤틱(Niantic, 구글 사내 스타트업에서 2015년 분사), 포켓몬 컴퍼니, 닌텐도 |
| 연도 | 2016-07-06(출시) |
| 수치 | 출시 2016-07-06. 다운로드 1억(2016-07-31), 5억(2016-09), 10억(2019-02). 미국 일일 활성 사용자 2,100만 명(2016-07-12)으로 종전 캔디크러시 기록 2,000만 경신, 이후 2016년 9월 중순까지 미국 플레이어 79% 이탈. 2016년 매출 9억 5천만 달러, 2020년까지 누적 64억 6천만 달러. Howe 외(2016) BMJ 355:i6270 — 응답자 중 560명(47.4%)이 플레이, 첫 주 +955보/일, 6주 후 소멸, Crossref 피인용 144회. |
| 출처 | Wikipedia "Pokémon Go" (다운로드·매출·사용자 수치) / Howe K.B., Suharlim C., Ueda P., Howe D., Kawachi I., Rimm E.B., "Gotta catch'em all! Pokémon GO and physical activity among young adults: difference in differences study", BMJ 2016;355:i6270, DOI 10.1136/bmj.i6270 |

GPS 기반 위치 게임에 카메라 오버레이를 얹은 모바일 AR 게임이다. 교육용으로 설계된 적이 없지만, 출시 몇 주 만에 '증강현실'이라는 단어를 전 세계 교사·사서·박물관 담당자의 어휘로 만들었다. 도서관과 박물관이 포켓스톱을 방문 유도에 활용했고, 언어학습·현장학습 설계 연구가 잇따라 나왔다. 무엇보다 이 게임은 AR의 행동 변화 효과를 대규모로 측정할 수 있는 자연실험을 제공했다.

교육 AR은 2016년까지도 '기기가 없다'는 벽에 막혀 있었다. 포켓몬 GO는 이미 모든 학생 주머니에 있는 스마트폰만으로 AR이 성립함을 증명했고, 애플(ARKit, 2017)과 구글(ARCore, 2017)이 곧바로 OS 수준 AR 프레임워크를 내놓는 계기가 됐다. 교육이 AR을 다시 본 이유는 교육학적 발견이 아니라 설치 기반의 갑작스러운 확보였다.

대중화는 대성공, 교육적 지속성은 실패. BMJ에 실린 하우 외(2016)의 차분의 차분(difference-in-differences) 연구는 설치 첫 주 일평균 걸음 수가 955보 증가했으나(95% CI 697~1,213) 6주 후에는 통계적 유의성이 사라졌음을 보였다. 미국 사용자 수도 2016년 7월 정점 이후 9월 중순까지 79%가 이탈했다. 이것이 교육 AR 문헌이 말하는 '신기효과'의 가장 깨끗한 계량 증거다.

### Merge Cube와 저가 도구 계열
| 항목 | 내용 |
| --- | --- |
| 주체 | Merge Labs, Inc.(미국 샌안토니오) |
| 연도 | 2017(출시) / 2026-06(서비스 존속 확인) |
| 수치 | Merge EDU 개인 구독 월 9.99달러(최대 3대), Explorer 시뮬레이션 100종 이상. 학교/교육구는 별도 견적. 2026-06-13 기준 mergeedu.com 정상 운영(웨이백 머신 캡처로 확인). |
| 출처 | mergeedu.com 및 mergeedu.com/pricing 아카이브 캡처(web.archive.org, 2026-06-13 / 2020년대 가격 페이지) / Merge Cube 관련 교육연구 예: IEEE Access, "Merge Cube as a New Teaching Tool for Augmented Reality", 2023, DOI 10.1109/ACCESS.2023.3301399 |

손바닥만 한 폼 재질 정육면체 표면에 마커 패턴을 인쇄한 물건이다. 스마트폰 카메라로 보면 큐브 위에 심장·화산·행성 같은 3D 객체가 올라오고, 학생이 손으로 돌리면 객체가 따라 돈다. 촉각과 시각을 결합한다는 점, 그리고 학생 1인당 비용이 헤드셋의 100분의 1 수준이라는 점이 핵심이다. 현재는 Merge EDU 앱군(Explorer 시뮬레이션 100종 이상, Object Viewer, HoloGlobe)과 구독 모델로 운영된다.

2016~2017년 HoloLens(개발자 에디션 3,000달러)와 Magic Leap One(2,295달러)이 보여준 것은 '학급 30명에게 헤드셋을 주는 시나리오는 영원히 불가능하다'는 사실이었다. Merge Cube는 반대 방향을 택했다 — 기기를 싸게 만드는 대신 기기를 아예 없애고 이미 있는 스마트폰·태블릿에 종속시켰다.

드물게 살아남은 사례. 2026년 6월 기준 서비스가 정상 운영 중이며, 개인 구독 월 9.99달러, 학교·교육청은 견적 기반이다. 다만 학술적으로는 여전히 소규모 사례연구 위주이고, 엄밀한 효과 검증은 빈약하다(IEEE Access 2023 등 일부).

### 플랫폼 사망 — Junaio, HP Reveal, Google Expeditions
| 항목 | 내용 |
| --- | --- |
| 주체 | Metaio GmbH(2003년 뮌헨공대 스핀오프, 2015년 애플 인수) / Autonomy→HP(Aurasma, 2011) / 구글 |
| 연도 | 2015-05(Metaio/Junaio) / 2020-02(HP Reveal) / 2021-06-30(Google Expeditions) |
| 수치 | Metaio 애플 인수 2015년 5월(공개 보도 5월 28일), 제품 판매 즉시 중단. Aurasma 2011-05-05 출시 → 2011년 10월 HP 인수 → HP Reveal 서비스 종료 2020년 2월. Google Expeditions 2015년 9월 출시, 2016년 5월까지 학생 100만 명 이상, 600종 이상 답사, 교실 키트=카드보드 30개+교사용 태블릿, 종료 2021-06-30. DAQRI: 2010년 설립, 누적 조달 2억 7,500만 달러(2017-07), 2019년 9월 폐업. |
| 출처 | Wikipedia "Metaio", "Aurasma", "Google Expeditions", "DAQRI" (각 항목의 인수·종료 일자) |

세 플랫폼 모두 교사가 코딩 없이 AR 콘텐츠를 만들 수 있게 해준 도구였고, 세 개 모두 사라졌다. Junaio는 2010년대 초 대표적 AR 브라우저로 학교 프로젝트에 널리 쓰였으나 애플 인수 직후 제품 판매와 서비스가 중단됐다. Aurasma/HP Reveal은 교사들이 교실 게시물·워크시트에 영상을 붙이는 용도로 대규모로 채택됐다가 2020년 2월 서비스가 종료됐다. Google Expeditions는 교사용 태블릿과 학생용 카드보드 30개 세트로 600종 이상의 가상 답사를 제공했고 2017년 가을 Tango 기반 AR 모드를 추가했지만 2021년 6월 30일 종료되어 Arts & Culture로 흡수됐다.

교사가 콘텐츠를 만들 수 없다는 커라월라(2006)의 지적에 대한 업계의 답이 바로 이 '무코딩 저작 도구'들이었다. 실제로 이 도구들이 나오자 교육 AR 채택이 급증했다. 문제는 수익 모델이 없었다는 것이다.

세 건 모두 실패이며, 실패 원인은 기술이 아니라 경제다. Junaio는 인수 합병으로, HP Reveal은 사업 정리로, Expeditions는 구글의 제품 정리로 죽었다. 공통 결과는 동일하다 — 교사가 몇 년간 축적한 콘텐츠가 서버 종료와 함께 소멸했고, 이 학습된 무력감이 학교의 AR 재도입을 구조적으로 어렵게 만들었다. 같은 시기 DAQRI(2010년 설립, 2017년 7월까지 누적 조달 2억 7,500만 달러)가 2019년 9월 폐업하며 ARToolKit 유지보수도 함께 끊겼다.

### 고가 헤드셋 훈련의 경제학 — HoloLens, Magic Leap, IVAS
| 항목 | 내용 |
| --- | --- |
| 주체 | 마이크로소프트, 매직리프, 미 육군, Anduril Industries |
| 연도 | 2016(HoloLens 개발자 에디션) / 2018-08-08(Magic Leap One) / 2021-03(IVAS 계약) / 2025-02(Anduril 이관) |
| 수치 | Magic Leap: 누적 조달 35억 달러 이상(2024-08 기준, 사우디 PIF 7억 5천만 달러 포함), Magic Leap One 2018-08-08 AT&T 통해 2,295달러, 2020-04-22 인력 50% 감원, Magic Leap 2 출시 2022-09-30(기업용). IVAS: 2021년 3월 최대 218억 8천만 달러, 12만 명분, 헤드셋 무게 3.4파운드(약 1.54kg), 의회 삭감 2억 3천만 달러(2020)·유보 약 4억 달러(2022), 2025-02 Anduril 이관. |
| 출처 | Wikipedia "Magic Leap", "Integrated Visual Augmentation System" (계약액·감원·시험 결과) |

직업훈련·군사훈련은 '실패 비용이 큰 절차를 반복 연습시켜야 한다'는 이유로 AR의 가장 유력한 시장으로 지목됐다. 마이크로소프트 HoloLens는 정비·의료·군사 훈련에서 표준 장비가 됐고, 미 육군의 IVAS는 HoloLens 2를 기반으로 12만 대 규모, 최대 218억 8천만 달러 계약으로 이어졌다. 매직리프는 35억 달러 이상을 조달하고 2,295달러짜리 Magic Leap One을 내놓았다. 세 시도 모두 훈련 효과가 아니라 착용성·비용·조직 도입 문제에서 무너졌다.

2016~2021년 기업과 군은 '숙련공 은퇴로 인한 암묵지 소실'과 '훈련용 실물 장비의 가동 중단 비용'이라는 구체적 문제를 안고 있었다. AR 작업지시서는 이 두 가지를 동시에 겨눈 해법으로 보였고, 학교와 달리 군·기업은 대당 수천 달러를 지불할 능력이 있었다.

대체로 실패. 매직리프는 2020년 4월 22일 인력의 절반을 감원하고 기업용으로 선회했으며 2024년 7월 영업·마케팅 조직 전체를 포함해 약 75명을 추가 감원했다. IVAS는 2022년 11월 시험에서 병사들이 두통·눈의 피로·구역을 호소했고, 국방부 감찰관실은 초기형 IVAS보다 기존 장비로 임무 수행이 더 나았다고 평가했으며, 의회는 2020년 2억 3천만 달러를 삭감하고 2022년 약 4억 달러를 유보했다. 2025년 2월 Anduril이 생산·개발을 넘겨받았다. 교육 현장에는 이 계열의 장비가 사실상 도달하지 못했다.

### 의료·직업 훈련의 실증 — HoloAnatomy RCT와 조립 작업 실험
| 항목 | 내용 |
| --- | --- |
| 주체 | 아서 탱·찰스 오언·프랭크 비오카·메이 모우 — 미시간주립대 / 마리나 스토야놉스카 외 15인 — 케이스웨스턴리저브대 Interactive Commons·해부학교실 |
| 연도 | 2003(Tang 외, CHI) / 2019-2020(Stojanovska 외, Medical Science Educator) |
| 수치 | Stojanovska 외: 2개 코호트 총 64명 + 후행 대조군 33명, 시신 시험 73.8%±12.3 / MR 시험 74.2%±13.0, p>0.05, r=0.74(p<0.01), Medical Science Educator 30(1):173-178, Crossref 피인용 67회. Tang 외(2003) CHI 논문 Crossref 피인용 448회 / Semantic Scholar 687회. 지구과학 쪽 저가 사례로 UC Davis KeckCAVES의 AR Sandbox(2012 공개, 오픈소스)를 쓴 Woods 외(2016) Journal of Geoscience Education 파일럿 연구 피인용 81회. |
| 출처 | Stojanovska M. et al., "Mixed Reality Anatomy Using Microsoft HoloLens and Cadaveric Dissection: A Comparative Effectiveness Study", Medical Science Educator 30(1), 2020, DOI 10.1007/s40670-019-00834-x (PubMed PMID 34457656 초록 전문 확인) / Tang A., Owen C., Biocca F., Mou W., CHI 2003, DOI 10.1145/642611.642626 / Woods T.L. et al., Journal of Geoscience Education, 2016, DOI 10.5408/15-135.1 |

탱 외(2003)는 AR로 조립 지시를 공간에 직접 겹쳐 보여줄 때 인쇄물·모니터 대비 오류와 정신적 작업부하가 줄어드는지 비교한 초기 통제실험이다. 스토야놉스카 외(2019)는 의대생을 대상으로 HoloLens 기반 혼합현실 해부학 수업과 전통적 시신 해부를 무작위 배정해 비교한 무작위대조시험이다. 후자가 중요한 이유는 결과가 '우위'가 아니라 '동등'이었기 때문이다 — 시신 시험 평균 73.8%±12.3, MR 시험 평균 74.2%±13.0, 통계적 차이 없음(p>0.05). 두 시험 점수의 상관은 r=0.74(p<0.01)였다.

의학교육은 교과 내용이 폭증하면서 해부 실습에 배정할 시간이 줄어드는 구조적 압박을 받고 있었다(논문 서두가 이를 명시한다). 동시에 시신 확보·보존·시설 비용은 계속 오른다. AR은 '해부학을 더 잘 가르치는 법'이 아니라 '해부학을 더 싸고 빠르게 가르치는 법'으로 요청됐다.

부분 성공. '차이 없음'은 마케팅에는 실망스럽지만 정책적으로는 강력하다 — 시신 없이도 동등한 성취가 가능하다면 비용·윤리·공간 제약이 있는 기관에서 대체재가 된다. 다만 표본 64명(+대조군 33명)의 단일 기관 연구이며, 장기 파지나 임상 수행으로의 전이는 측정되지 않았다.

### 과대평가 비판 — 신기효과, 출판편향, 그리고 매체 논쟁의 재연
| 항목 | 내용 |
| --- | --- |
| 주체 | 리처드 클라크(Richard E. Clark, 남캘리포니아대) / 앨런 청·로버트 슬래빈(존스홉킨스대) / 귀도 마크란스키 외(코펜하겐대) / 이네스 미겔-알론소 외(부르고스대), 주미 리 외 |
| 연도 | 1983(Clark) / 2016(Cheung & Slavin) / 2019(Makransky 외) / 2024-2025(신기효과 실측) |
| 수치 | Clark(1983) Review of Educational Research 53(4), Crossref 피인용 1,412회. Cheung & Slavin(2016) Educational Researcher, 12개 리뷰 645편 분석, Crossref 408회. Makransky, Terkildsen & Mayer(2019) Learning and Instruction 60:225-236, Crossref 1,293회. Miguel-Alonso 외(2024) Virtual Reality, 학부생 86명(통제/처치), Semantic Scholar 153회. Lee 외(2025) IEEE TVCG, 3주 3파 종단설계(2026-09-29 기준 피인용). |
| 출처 | Clark R.E., "Reconsidering Research on Learning from Media", RER 53(4), 1983, DOI 10.3102/00346543053004445 / Cheung A.C.K., Slavin R.E., "How Methodological Features Affect Effect Sizes in Education", Educational Researcher, 2016, DOI 10.3102/0013189X16656615 (ERIC 초록) / Makransky G., Terkildsen T.S., Mayer R.E., Learning and Instruction, 2019, DOI 10.1016/j.learninstruc.2017.12.007 / Miguel-Alon |

AR 교육 효과크기 문헌 전체에 대한 세 갈래 비판이 있다. 첫째, 클라크(1983)의 고전적 논변 — 매체 자체는 학습에 영향을 주지 않으며 효과로 보이는 것의 상당 부분은 교수설계 차이와 신기효과다. 둘째, 청과 슬래빈(2016)이 교육 분야 645편을 분석해 찾아낸 방법론적 부풀림 — 출판된 논문, 소규모 시행, 연구자 자작 측정도구를 쓴 연구의 효과크기가 각각 미출판·대규모·독립 측정도구 대비 약 2배였고, 준실험이 무작위실험보다 유의하게 컸다. AR 교육 메타분석에 들어간 연구는 거의 전부가 '출판됨 + 소규모 + 연구자 자작 시험지 + 준실험'이라는 네 조건을 동시에 만족한다. 셋째, 몰입 자체가 학습을 방해할 수 있다는 실증 — 마크란스키 외(2019)는 몰입형 VR이 현존감은 높이지만 학습은 떨어뜨린다고 보고했다.

2019년 이후 AR 효과크기가 교육청 조달과 에듀테크 마케팅에 직접 인용되기 시작하면서, 수치의 생성 조건을 따지는 작업이 실무적으로 시급해졌다. 특히 g=0.9 같은 값이 하티(Hattie)의 통상 기준선 0.40의 두 배를 넘는다는 점이 오히려 의심의 근거가 됐다.

비판은 옳았지만 시장을 멈추지는 못했다. 신기효과를 직접 측정한 최근 연구들은 그것이 실재하며 방향이 부정적일 수 있음을 보인다 — 미겔-알론소 외(2024)는 학부생 86명 대상 실험에서 신기효과가 초기 학습 성과를 떨어뜨리는 요인이며 사전 튜토리얼로 완화된다고 보고했고, 이 외(2025)의 3주 3회차 종단 연구는 초기 신기함이 학습을 방해하다가 환경에 익숙해질수록 부호화가 개선된다고 보고했다. 포켓몬 GO의 6주 감쇠와 합치면 결론은 일관된다 — AR의 단발성 효과크기는 지속성 검증 없이는 의미가 없다.

#### 검증에서 잡힌 정정
- 가토 히로카즈의 1999년 소속이 틀렸다. 조사는 '가토 히로카즈(Hirokazu Kato, 나라선단과학기술대학원대)'라고 적었으나, IWAR'99 논문 원문 표제면(hitl.washington.edu/artoolkit/Papers/IWAR99.kato.pdf)에는 'Hirokazu Kato¹ ... ¹Faculty of Information Sciences, Hiroshima City University, kato@sys.im.hiroshima-cu.ac.jp'로 인쇄돼 있다. 즉 1999년 소속은 히로시마시립대학이며, NAIST는 그가 2007년 이후 옮긴 곳이다(영문 위키백과 'ARToolKit' 항목의 오류가 그대로 전파된 것으로 보인다). 빌링허스트의 워싱턴대 HIT Lab 소속만 맞다.
- Li·Luo·Chen 논문의 발행연도가 1년 틀렸다. 조사는 '거거 리·헝 뤄·디 천(Education Sciences 2024)', 'Li 외(2024)'라고 두 번 적었으나 실제는 'Augmented Reality in Higher Education: A Systematic Review and Meta-Analysis of the Literature from 2000 to 2023', Education Sciences 15(6):678, DOI 10.3390/educsci15060678, 온라인 게재 2025-05-29이다(Crossref issued/published-online 모두 2025-05-29). 2024년 날짜가 붙은 것은 INPLASY 프로토콜 등록(10.37766/inplasy2024.3.0062, 2024-03-15)뿐이다. 저자도 6인(Gege Li, Heng Luo, Di Chen, Peiyu Wang, Xin Yin, Jiakai Zhang)이다. 237
- 위 Li 외 연구의 적용 범위가 누락됐다. 이 메타분석은 '고등교육(higher education)' 한정이며 g=0.896은 대학생 표본만의 추정치다. 조사는 이를 교육 일반의 최댓값처럼 '값은 0.56에서 0.90까지 흩어졌고'라는 서사에 투입했다. 초·중등을 포함한 전체 교육 AR의 상한으로 읽히면 안 된다.
- MagicBook을 'HIT Lab NZ'에 귀속시킨 것은 시대착오다. 서사는 '2001년 HIT Lab NZ의 MagicBook'이라고 썼으나, HIT Lab NZ 공식 소개(hitlabnz.org/index.php/about)는 'Operating since 2002'라고 명시한다. 2001년 MagicBook은 워싱턴대 HIT Lab과 ATR의 성과다(Billinghurst·Kato·Poupyrev). 조사 항목 본문의 '워싱턴대/캔터베리대 HIT Lab'과 서사가 서로 모순된다.
- Junaio의 사망 시점이 틀렸다. 항목 제목은 '플랫폼 사망 — Junaio ... (2015-05(Metaio/Junaio))'로 2015년 5월을 사망일로 제시하지만, 영문 위키백과 'Junaio'는 'Junaio and all Junaio channels were deactivated on 15 December 2015'라고 적는다(출시는 2009-11-11). 2015년 5월은 애플 인수 보도(5/28)와 메타이오의 제품 판매 중단 시점일 뿐, 서비스 종료는 2015-12-15다. 조사가 인용한 위키백과 'Metaio'만 보고 'Junaio'를 보지 않은 결과다.
- 효과크기 범위 제시가 범주 오류다. 항목 제목 '2세대 메타분석 — 0.38(인지부하 감소)부터 0.93(언어)까지의 분산'과 서사 '값은 0.56에서 0.90까지 흩어졌고'는 서로 다른 구성개념을 한 수직선에 올려놓았다. Zhu 외(2026)의 값은 g=-0.383(음수)이며 '학습 성취'가 아니라 '인지부하 감소량'이다(부호가 음수일수록 바람직). 성취 효과크기(0.56~0.896)와 같은 척도가 아니므로 '0.38에서 0.90까지의 분산'이라는 서술은 성립하지 않는다. 또한 서사가 제시한 '0.56~0.90' 범위는 본문의 0.93(Cai 언어), 0.602(Yılmaz&Batdı), 0.677(Tekedere&Göker)와도 어긋난다.
- '이질성 I²가 90%를 넘는다'는 일반화가 근거를 넘어선다. 조사가 제시한 I² 값은 Zhu 외(2026)의 92.7% 단 하나뿐이며, Garzón(2019/2020)·Cai(2022)·Chang(2022)·Li(2025)에 대해서는 I²가 전혀 제시되지 않았다. 인지부하 메타 1편의 이질성으로 2세대 메타분석 전체가 I²>90%라고 결론 내릴 수 없다.
- ARToolKit이 1999년에 '공짜로' 교실 연구를 가능하게 했다는 서사는 조사 자신의 자료와 충돌한다. 서사는 '1999년 ... ARToolKit이 웹캠과 종이 마커만으로 정합 문제를 공짜로 풀어주자 예산 없는 교실 연구가 가능해졌다'고 쓰지만, 같은 조사의 항목이 '오픈소스 v1.0은 2001년'이라고 적고 있다. 1999년 IWAR 논문의 시스템은 비디오 시스루 HMD 기반 화상회의 장치이지 웹캠+종이 마커 교실 키트가 아니다. 무상 배포의 기점은 1999년이 아니라 2001년이다.
- Stojanovska 외 연구의 설계 해석이 과하다. 초록이 'randomized controlled trial'이라 칭하는 것은 사실이나, 실제 설계는 64명을 두 코호트로 교차 배정해 전원이 시신 실기시험과 MR 실기시험을 '둘 다' 치른 개인 내 비교이고, 33명 대조군은 6회 세션이 끝난 뒤 사후 모집돼 무작위 배정되지 않았다('a third cohort of 33 students ... was recruited to participate in the final practical exams'). 즉 73.8% vs 74.2%, p>0.05는 '두 시험 형식'의 동등성이지 '두 교수법'의 무작위 비교 결과가 아니다. 논문 제목 자체도 'A Comparative Effectiveness Study'다. 따라서 '시신 없이도 동등한 성취가 가능하다'는 정책적 결론은 이 설계가 지지하는 범위를 넘는다.
- Merge EDU의 '월 9.99달러(최대 3대)' 가격은 인용된 2026-06-13 캡처로 확인되지 않는다. 웨이백 CDX 조회 결과 2026-06-13 캡처(20260613220925, mergeedu.com, HTTP 200)는 실재하고 사이트 정상 운영도 확인되며 2026년 /pricing/edu 페이지의 'over 100 interactive AR/VR experiences'도 확인된다. 그러나 해당 2026년 가격 페이지는 금액을 JavaScript로 주입해 캡처 본문에는 'Loading pricing information...'만 남아 있고, 요금제 구조도 Individual/Teacher/Homeschool/School 4단으로 바뀌어 있다. 9.99달러는 2020년경 캡처에서 온 구가격이며 '2026년 기준 가격'으로 제시하면 안 된다.
- Cai 외(2022)와 Zhu 외(2026)의 출처 표기가 틀렸다. Cai, Pan & Liu는 ERIC 수록물이 아니라 Wiley의 Journal of Computer Assisted Learning 논문으로 DOI 10.1111/jcal.12661이며, 게다가 '언어학습 한정' 메타분석이라 0.93은 AR 일반의 값이 아니다. Zhu 외도 'ERIC'이 아니라 SpringerOpen의 Smart Learning Environments 13(1), DOI 10.1186/s40561-025-00429-7이고 공저자는 4인(Xiuqi Zhu, Kuan Peng, Shuyu Yu, Guohua Wang)이다.
- 부차적 연도·귀속 오류 3건. (a) Klopfer & Squire의 ETR&D 논문은 '2007'이 아니라 ETR&D 56(2):203-228, 2008년 게재다(2007-04-05는 온라인 선공개일). (b) Metaio를 '2003년 뮌헨공대 스핀오프'라고만 적었으나 인용된 위키백과 'Metaio'는 'grew out of an internal project within Volkswagen'이라고 병기한다 — 폭스바겐 내부 프로젝트 기원이 빠졌다. (c) IVAS의 '3.4파운드'는 위키백과가 version 1.2에 붙인 수치인데 조사는 2021년 계약 맥락에 배치했다. 또한 신기효과 반증 근거로 든 Makransky 외(2019)와 Miguel-Alonso 외(2024)는 모두 몰입형 VR 연구이지 AR 연구가 아니며, Miguel-Alonso의 연구 목적은 '신기효과를 튜토리얼로 완화할 수 있는가'였다(86명 통제/처치 구성은 정확).
- 가토 히로카즈의 1999년 소속이 '나라선단과학기술대학원대(NAIST)'로 적혀 있으나 틀렸다. 1999 IWAR 원논문 PDF(hitl.washington.edu/artoolkit/Papers/IWAR99.kato.pdf)의 각주 1은 'Faculty of Information Sciences, Hiroshima City University'이고 이메일도 kato@sys.im.hiroshima-cu.ac.jp다. 가토는 2007년에야 NAIST로 옮겼다. 위키백과 ARToolKit 문서의 오류('Hirokazu Kato of Nara Institute of Science and Technology in 1999')를 원문 대조 없이 승계했다.
- 서사 문장 '1999년 ... ARToolKit이 웹캠과 종이 마커만으로 정합 문제를 공짜로 풀어주자'는 원논문과 불일치한다. 1999 IWAR 논문은 'video-based augmented reality conferencing system'과 'HMD calibration'을 다루는 광학 HMD 회의 시스템 논문이다(초록 원문 확인). 또한 오픈소스 v1.0 배포는 2001년이고(연구의 자기 데이터 행도 2001년이라 적음), 같은 2001년 ARToolworks가 설립되어 상용 라이선스를 병행 판매했으므로 '공짜'는 비상업 용도 한정이다. 1999년을 교실 확산의 기점으로 삼는 인과 연결은 2년 이르다.
- '2001년 HIT Lab NZ의 MagicBook'은 시대착오다. HIT Lab NZ는 2002년 캔터베리대·워싱턴대·CDC 합작으로 설립됐고 빌링허스트가 2002~2015년 소장을 맡았다(위키백과 HIT Lab NZ). 2001년 MagicBook은 워싱턴대 HIT Lab 성과이며, 가토는 히로시마시립대, 포퍄레프는 ATR 소속이었다. 데이터 행의 '워싱턴대/캔터베리대 HIT Lab, ATR'이라는 병기도 같은 혼동을 반복한다.
- 커라월라 논문 공저자 이름이 '애덤 울라드(Adam Woolard)'로 되어 있으나 실제로는 Adrian Woolard다(Crossref 저자 레코드 및 Semantic Scholar 'A. Woolard', Virtual Reality 10(3-4) 저자란).
- 'Li G., Luo H., Chen D., Education Sciences, 2024'는 연도·범위·저자 수가 틀렸다. 실제 논문은 Li Gege, Luo Heng, Chen Di, Wang Peiyu, Yin Xin, Zhang Jiakai, 'Augmented Reality in Higher **Education**: A Systematic Review and Meta-Analysis of the Literature from 2000 to **2023**', Education Sciences 15(6):678, **2025-05-29** 출판, DOI 10.3390/educsci15060678 — 저자 6인이다. 237편/60편/g=0.896/95% CI[0.685,1.107] 수치는 정확하나 이는 **고등교육 한정** 결과이며, 이를 교육 AR 일반의 효과크기 분산 논거로 쓰면 범위를 넘는다. '2024'는 INPLASY 프로토콜 등록(10.37766/inplasy2024.
- 'HoloLens 기반 해부학 RCT는 시신 해부와 차이 없음을 보고했다' 및 '시신 없이도 동등한 성취가 가능하다면 대체재가 된다'는 원 결과의 오독이다. Stojanovska 외(2020) 초록 원문상 73.8%±12.3와 74.2%±13.0은 *같은 학생들*이 치른 시신 실기시험과 MR 실기시험 점수이며(‘All 64 students completed two practical exams with equivalent content, one in the cadaver lab and one using MR’), 코호트1·2는 상지/하지를 교차해 두 교수법을 모두 받았다. 33명 대조군은 6회 세션이 끝난 뒤 최종 실기시험에만 사후 모집됐다. 논문 결론도 'regardless of the study modality, performed similarly on the MR and the cadaver practical exams' — 시험 형식 등가성이지 교수법 등가성이 아니다. 따라서 
- Stojanovska 논문 저자 수가 '외 15인'(=16인)으로 적혀 있으나 실제 저자는 15인이다(Stojanovska M, Tingle G, Tan L, Ulrey L, Simonson-Shick S, Mlakar J, Eastman H, Gotschall R, Boscia A, Enterline R, Henninger E, Herrmann KA, Simpson SW, Griswold MA, Wish-Baratz S). '외 14인'이 맞다.
- '신기효과를 직접 측정한 최근 연구'로 제시된 세 편이 모두 AR이 아니라 VR 연구다. Makransky/Terkildsen/Mayer(2019)는 VR 과학실험실 시뮬레이션, Miguel-Alonso 외(2024)는 제목 'Evaluation of the novelty effect in **immersive Virtual Reality** learning experiences'(Virtual Reality 28(1), DOI 10.1007/s10055-023-00926-5), Lee/Chen/Basu(2025)는 제목 'From Novelty to Knowledge: A Longitudinal Investigation of the Novelty Effect on Learning Outcomes in **Virtual Reality**'(IEEE TVCG 31(5):3204-3212, DOI 10.1109/tvcg.2025.3549897)이다. AR 교육의 신기효과 감쇠 논증에 i
- '미겔-알론소 외(2024)는 학부생 86명 대상 실험에서 신기효과가 [학습을 저해함을 보였다]'는 연구 설계와 다르다. 초록 원문상 86명은 튜토리얼 미제공(Control)과 튜토리얼 수행(Treatment)으로 나뉘었고, 연구 목적은 'to measure the effectiveness of a **tutorial at mitigating** the novelty effect'다. 보고된 결과는 튜토리얼이 만족도를 유의하게 높이고, iVR 조작 학습시간을 줄이고, 이해·평가 수준을 향상시켰다는 것이다. 신기효과의 크기를 직접 계량한 연구가 아니며 보고 방향도 양(+)이다.
- Merge EDU의 '개인 구독 월 9.99달러(최대 3대)'와 '2026-06-13 기준 mergeedu.com 정상 운영'은 현재 시점(2026-09-29) 기준으로 낡았다. mergeedu.com은 merge3d.ai로 302 리다이렉트되며, merge3d.ai/pricing의 현행 요금은 Merge3D Platform 번들 기준 Individual $17/월(연 $207), Teacher $28/월(연 $331), Classroom $0/월, School $0/월이다. $9.99/월·3대 플랜은 현행 가격 페이지에 없다. 3개월 전 웨이백 캡처로 '정상 운영'과 가격을 현재형 단언한 절차 자체가 결함이다.
- 'Junaio·HP Reveal·Google Expeditions ... 공통 결과는 동일하다 — 교사가 몇 년간 [만든 콘텐츠가 사라졌다]'는 Expeditions에 대해 성립하지 않는다. 위키백과 Google Expeditions: 'The platform was discontinued on June 30, 2021, and **was merged into Google Arts & Culture**' — 600종 답사 콘텐츠는 이관됐고, 애초에 구글·출판 파트너 제작물이지 교사 자작물이 아니다. 교사 제작 콘텐츠 소실은 Aurasma/HP Reveal의 사용자 제작 aura에 해당하는 이야기다.
- ARToolKit 항목의 '유지보수 주체가 소멸했다'는 같은 행이 스스로 언급한 사실과 모순된다. 위키백과 ARToolKit: DAQRI 철수 후 ARToolworks 전 CEO Ben Vaughan과 전 CTO Phil Lamb가 artoolkitX를 만들어 'to ensure that the software is developed and maintained'했고 초기에는 Realmax Inc가 지원했다. 유지보수 주체는 교체됐지 소멸하지 않았다.
- '동일 기술에 대해 0.38에서 0.90까지 값이 흩어지고 이질성 I²가 90%를 넘는다'는 서로 다른 구인을 한 축에 올린 범주 오류다. Zhu 외(2026) g=−0.383은 **인지부하** 효과(음수=감소=이득, Smart Learning Environments, DOI 10.1186/s40561-025-00429-7, 27편)이고, Cai/Pan/Liu 0.93은 **언어 학습 이득 한정**(JCAL, DOI 10.1111/jcal.12661, 21편, 2008-2020, RVE), Li 외 0.896은 **고등교육 성취 한정**이다. I²=92.7%도 인지부하 합성의 값이지 성취 문헌의 값이 아니다. 결과지표 간 이질성을 단일 추정량의 불안정성으로 제시했다.
- '커라월라 ... 이 분야 최초의 신뢰할 만한 음(陰)의 결과'는 두 겹으로 과장이다. (a) 초록 원문은 'Analysis of **teacher–child dialogue** in a comparative study'로, 검정력을 갖춘 성과 실험이 아니라 질적 대화 분석이고 측정된 것은 학습 성취가 아니라 몰입(engagement)이다('the children using AR were **less engaged**'). (b) Santos 외(2014) 초록은 효과크기 산출이 가능했던 7편이 'from a **small negative effect** to a large effect'로 흩어졌다고 보고하므로, 음의 결과는 2006년 이전·이후에 산재했다. '최초의 신뢰할 만한'이라는 우선권 주장은 근거가 없다.
- 'BMJ 연구 ... 신기효과 감쇠를 가장 깨끗하게 계량한 자료다'는 설계에 비해 과한 평가다. Howe 외(2016)는 BMJ 초록상 'cohort study using online survey data' — Amazon Mechanical Turk로 모집한 18~35세 미국인 1,182명이 플레이 여부를 **자기보고**하고 iPhone Health 앱 걸음 수를 읽어온 자기선택 코호트다. 결과변수는 학습이 아니라 **신체활동**이며, 6주는 관찰 종료 시점이지 측정된 감쇠 상수가 아니다(6주차 130보, 95% CI −593~853). 교육 AR의 신기효과 준거로 쓰기에는 외적 타당도가 좁다.
- Özdemir 외(2018)를 1세대 메타분석 근거로 인용하면서 그 초록이 자가당착이라는 점을 짚지 않았다. EJER 74(2018):165-186 원문 초록은 'AR applications **increase** students' academic achievement in the learning process compared to traditional methods'라고 쓴 직후 'It was concluded that AR applications **do not show significant differences** in academic success in the learning process'라고 쓴다. '보고 관행이 허술했다'는 서사 자신의 논점을 강화할 증거인데 누락됐다.
- Li·Luo·Chen 메타분석의 연도가 틀렸다. '거거 리·헝 뤄·디 천(Education Sciences 2024)'이라 했으나 실제는 2025년이다 — 'Augmented Reality in Higher Education: A Systematic Review and Meta-Analysis of the Literature from 2000 to 2023', Education Sciences 15(6):678, DOI 10.3390/educsci15060678, 게재일 2025-05-29(OpenAlex·Crossref 확인). 2024는 INPLASY 프로토콜 등록(DOI 10.37766/inplasy2024.3.0062)의 연도다. 저자도 3인이 아니라 6인(Li, Luo, Chen, Wang, Yin, Zhang)이고, 범위는 교육 일반이 아니라 '고등교육(2000-2023)'이다. g=0.896, 95% CI [0.685-1.107], 237편 검토→실험 60편은 정확하다.
- Merge EDU 가격이 현재가 아니다. '개인 구독 월 9.99달러(최대 3대)'라 했으나, 2026-09-30 현재 mergeedu.com은 merge3d.ai로 302 리다이렉트되고 라이브 요금표는 Individual 월 17달러(연간 결제, 연 207달러), Teacher 월 28달러(연 331달러), Classroom·School은 0달러다. 근거로 든 것이 2026-06-13 웨이백 캡처여서 아카이브 스냅샷을 '2026-06 서비스 존속 확인'이라는 현재 상태 주장으로 제시했다. 또한 브랜드가 Merge3D로 바뀌고 AI 3D 생성 제품(Merge Creator)으로 축을 옮긴 사실이 빠졌다.
- (외 17건)

## consumer
항목 15개 · 검증 정정 지적 55건

> 소비자 AR의 역사는 기술사가 아니라 마찰의 역사다. 1999년 가토 히로카즈의 ARToolKit이 흑백 사각 마커로 카메라 자세를 역산하는 값싼 방법을 내놓았고, 2009년 Flash 포팅으로 웹캠 달린 PC가 모두 AR 단말이 됐다. 그래서 첫 소비자 AR은 광고였다. 2008년 11월 MINI는 독일 자동차 잡지 지면에 마커를 인쇄했고, 2009년 11월 Esquire는 표지에서 로버트 다우니 주니어가 걸어나오게 했다. 둘 다 반복되지 않았다 — 잡지를 웹캠에 들어올리는 동작이 일상이 아니었기 때문이다. 2009~2011년 Layar·Wikitude·junaio 같은 'AR 브라우저'는 GPS와 나침반만으로 도시 위에 정보를 겹치려 했으나 도심 GPS 오차와 갱신되지 않는 콘텐츠로 무너졌고, 셋 다 소비자 앱을 버리고 B2B SDK로 피신한 끝에 퀄컴과 애플에 흡수됐다. 광고형 AR의 정점이자 종점은 Blippar였다. 2016년 스스로 15억 달러라 말하던 회사는 1억 3,170만 달러를 태우고 2018년 12월 18일 잔고 6만 5천 달러로 법정관리에 들어갔다. 이미지 인식이 애플·구글의 무료 기능이 되어 해자가 사라졌고, 캠페인마다 콘텐츠를 새로 만드는 원가구조에는 규모의 경제가 없었다. 같은 시기 구글 글래스는 기술이 아니라 사회적 이유로 죽었다. 2016년은 전환점처럼 보였다. 포켓몬 고는 한 달 만에 1억 다운로드, 첫해 9억 5천만 달러를 벌었지만 기술적으로는 카메라와 자이로스코프로 그림을 겹친 것이 전부였고 다수는 배터리 때문에 AR을 껐다. 실제로 살아남은 소비자 AR은 스냅챗 렌즈 — 세계가 아니라 얼굴만 이해하는 AR이었다. 2017년 ARKit·ARCore가 마커를 없애자 IKEA Place가 나왔고, 반품 비용을 가진 유통이 가장 진지한 고객이 됐다. 그러나 2018년 3월 ARKit 전용 앱 누적 다운로드는 1,300만에 그쳤다. 2024~2025년 메타는 Spark를 닫고 나이앤틱은 게임을 팔았다. 소비자 AR은 산업이 아니라 OS의 한 기능으로 정착했다.


### ARToolKit과 FLARToolKit — 마커 AR이라는 값싼 토대
| 항목 | 내용 |
| --- | --- |
| 주체 | 가토 히로카즈(加藤博一, 나라첨단과학기술대학원대학)가 개발, 워싱턴대 HIT Lab이 배포. 2001년 ARToolworks 설립, 이후 DAQRI 인수, 현재 artoolkitX가 유지 |
| 연도 | 1999년 개발 / 2001년 오픈소스 v1.0 / 2009년 Flash 포팅 / 2015년 5월 13일 DAQRI가 v5.2로 재공개 |
| 수치 | 개발 1999년, 오픈소스 v1.0 2001년, DAQRI 재공개 v5.2 2015-05-13, 최신 안정판 1.1.22(2024년 12월) |
| 출처 | Wikipedia, 'ARToolKit'(Kato 1999, NAIST/HIT Lab; ARToolworks 2001; DAQRI v5.2 2015-05-13) / Wikipedia, 'Augmented reality' 연표: '2009: ARToolkit ported to Adobe Flash (FLARToolkit)' |

흑백 사각 마커의 네 꼭짓점을 검출해 실물 카메라의 위치와 자세를 실시간으로 역산하는 라이브러리다. 환경의 3차원 지도를 만들지 않고 마커 하나만 풀기 때문에 계산량이 극히 작다. 이 가벼움 덕에 Symbian(2005), iPhone 3G(2008), Android(2010)로 차례로 이식되며 최초의 모바일 AR SDK 가운데 하나가 됐다. 2009년 Adobe Flash로 포팅된 FLARToolKit은 플러그인 설치 없이 웹브라우저와 웹캠만으로 AR을 돌릴 수 있게 만들었다. 소비자 AR의 1세대 전체가 이 한 줄기 위에 서 있다.

광고·출판이 필요했던 것은 정밀도가 아니라 '인쇄물에서 웹으로 사람을 끌어오는 후크'였다. 마커 AR은 특수 하드웨어 없이 웹캠만으로 작동해 캠페인 단가에 맞았다.

기술로는 성공, 제품으로는 소멸. 마커를 인쇄하고 카메라 앞에 들어올려야 한다는 제약 자체가 소비자 AR의 천장이었고, 2017년 평면 검출(ARKit/ARCore)이 나오자 사실상 용도 폐기됐다.

### MINI Cabrio 웹캠 AR 광고 — 최초의 대량 소비자 노출
| 항목 | 내용 |
| --- | --- |
| 주체 | BMW 그룹 MINI 독일법인. 추적 기술은 뮌헨의 Metaio |
| 연도 | 2008년 11~12월 |
| 수치 | 2008년 11월 캠페인 개시, 게재 매체 3종 이상(Auto Motor und Sport·Autobild·Werben & Verkaufen). IAB의 AR 마케팅 플레이북도 2008년을 기점으로 인용 |
| 출처 | BMW Group PressClub 보도사진 'The new MINI Cabrio – launch campaign with augmented reality technology'(11/2008) / Hackaday 2008-12-13 'MINI's Augmented Reality Ad' / Geekologie 2008-12 |

독일 자동차 잡지 지면에 인쇄한 마커를 PC 웹캠에 비추면 화면에 MINI Cabrio의 3D 모델이 떠오르고, 종이를 돌리면 차도 함께 돌았다. 전용 URL에 접속한 뒤 브라우저(당시 Internet Explorer)와 웹캠만 있으면 됐다. 게재지는 Auto Motor und Sport, Autobild, Werben & Verkaufen. 지면 광고를 '클릭 가능한 매체'로 바꾼 최초의 대규모 시도로 기록된다.

자동차 광고에는 '실물 크기와 존재감을 지면으로 전달할 수 없다'는 고유한 문제가 있었다. 동시에 인쇄 광고는 효과 측정이 불가능했는데, AR은 독자가 URL에 접속하는 추적 가능한 행동을 만들어냈다.

화제성은 컸으나 반복되지 않았다. 잡지를 웹캠 앞에 들어올리는 동작이 일상 행동이 아니었고, 캠페인 1회당 3D 모델과 전용 사이트를 새로 제작해야 해 단가가 높았다.

### Esquire 증강현실 특집호 — 잡지산업의 마지막 반격
| 항목 | 내용 |
| --- | --- |
| 주체 | Esquire(Hearst), 편집장 David Granger. 제작은 The Barbarian Group과 애니메이션 스튜디오 Psyop. 표지 모델 Robert Downey Jr. |
| 연도 | 2009년 (2009년 11월 10일 발매, 12월호) |
| 수치 | 발매 2009-11-10, 제작비는 '6자리 달러(six figures)'로 보도 |
| 출처 | Engadget 2009-11-10 'Esquire's Augmented Reality issue goes on sale' / Observer 2009-11-09 / Fast Company, 'Esquire's Six-Figure Augmented Reality Issue' |

표지와 내지 여러 면에 마커를 인쇄하고, 독자가 PC에 전용 소프트웨어를 설치한 뒤 잡지를 웹캠에 비추면 그린스크린으로 촬영한 로버트 다우니 주니어가 표지에서 걸어나와 말을 걸었다. 표지 문구가 그의 뒤로 날아가는 연출까지 넣었다. 잡지 한 권 전체를 AR 인터페이스로 설계한 최초의 사례다.

2009년은 미국 잡지 광고면이 급감하던 해다. 인쇄물이 '디지털이 하지 못하는 것'을 증명해야 한다는 압박이 편집국 차원의 실험을 낳았다.

1회성으로 끝났다. 전용 소프트웨어를 다운로드·설치해야 한다는 마찰이 치명적이었고 후속호는 없었다. 이 실패는 'AR의 성패는 렌더링 품질이 아니라 진입 단계 수'라는 법칙을 처음 드러냈다.

### Layar — AR 브라우저의 등장과 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | Raimo van der Klein, Claire Boonstra, Maarten Lens-FitzGerald (네덜란드 암스테르담) |
| 연도 | 2009년 6월 설립 / 2014년 6월 Blippar에 인수 / 2016년 암스테르담 사무소 폐쇄 |
| 수치 | 레이어 수 2010년 7월 1,000개 → 2011년 9월 2,993개. 창업 2009년 6월, 인수 2014년 6월, 사무소 폐쇄 2016년, 2019년 1월 공동창업자 2인이 IP 재매입 검토 |
| 출처 | Wikipedia, 'Layar' / MixedRealityLab, 'Handheld Augmented Reality Browsers' 정량·정성 조사 / Communications of the ACM, 'Augmented Reality Browsers' / Cornell CS, 'No Escape From Reality: Security and Privacy of Augmented Reality Browsers'(WWW 2015) |

카메라 화면 위에 GPS·나침반·가속도계만으로 주변 정보를 겹쳐 보여준 세계 최초급 모바일 AR 브라우저다. 콘텐츠는 서드파티가 '레이어(layer)'로 등록했다 — 부동산 매물, 지하철역, 위키백과 항목, 트윗 등. 지도라는 2D 은유를 버리고 '고개를 돌리면 정보가 보인다'는 은유를 처음 상품화했다. 2010년 9월 1일 세계경제포럼이 'Technology Pioneer for 2011'로 선정했다.

2009년에 스마트폰이 GPS·디지털 나침반·가속도계를 동시에 탑재하기 시작했다. 위치기반 서비스 업계는 지도 위 핀이라는 표현의 한계를 넘고 싶어 했고, Layar는 센서만으로 그것을 구현할 수 있었다.

실패. 기술적 이유는 도심 GPS 오차(수십 m)와 나침반 흔들림이라 대상이 엉뚱한 방향에 떠 있었다는 것, 경제적 이유는 콘텐츠 제공자가 레이어를 계속 갱신할 수익 유인이 없어 콘텐츠가 빠르게 죽었다는 것이다. 학술 조사도 '빈약한 콘텐츠, UI 설계, 시스템 성능'을 얼리어답터의 지속 사용을 막은 3대 요인으로 지목했다.

### Wikitude와 junaio/Metaio — 소비자 앱을 버리고 SDK로 피신하다
| 항목 | 내용 |
| --- | --- |
| 주체 | Wikitude(오스트리아 잘츠부르크) / Metaio(독일 뮌헨, 창업자 Günter Greiner·Peter Meier·Thomas Alt, 폭스바겐 사내 프로젝트에서 분사) |
| 연도 | Wikitude 2008년 10월 20일 출시 → 2012년 SDK 피벗 → 2021년 9월 퀄컴 인수 → 2024년 9월 21일 서비스 종료 / Metaio 2003년 설립 → 2015년 5월 애플 인수 |
| 수치 | Wikitude: 2008년 Android Developer Challenge Top-50, 2010년 World Summit Award·Galileo Master·Navteq Challenge Global Champion, 2017년 AWE 최우수 개발자 도구. 신규 구독 중단 2023-09-21, 서비스 전면 종료 2024-09-21. Metaio: 애플이 2015년 5월 21~22일 인수 완료, AR 특허출원 100건 이상 이전 |
| 출처 | Wikipedia, 'Wikitude' / Wikipedia, 'Metaio' / Wikipedia, 'ARKit'(2015년 5월 Metaio 인수와 100건 이상 특허출원 명시) |

둘 다 소비자용 AR 브라우저(Wikitude World Browser, junaio)로 출발했다가 소비자 앱으로는 수익이 나지 않자 B2B SDK 사업으로 갈아탔다. Wikitude는 2012년 SDK로 제품 구조를 재편했고, Metaio는 인쇄물과 위치 양쪽을 다루는 junaio로 유럽 캠페인 시장을 잡았다. 결말은 둘 다 플랫폼 기업에 흡수되는 것이었고, 두 브라우저 앱은 모두 사라졌다. Metaio의 SLAM·컴퓨터비전 기술과 100건이 넘는 AR 특허출원은 그대로 애플로 넘어가 ARKit의 토대가 됐다.

2008년 안드로이드 마켓은 사실상 비어 있었고, 센서만으로 만든 앱도 최상위에 오를 수 있었다. 유럽 브랜드들은 미국 플랫폼에 의존하지 않는 AR 공급자를 원했다.

소비자 제품은 전멸, 기술과 인력은 플랫폼 기업이 흡수. 이 패턴(소비자 AR 스타트업 → SDK 피벗 → 대기업 인수 → 소멸)은 이후 10년간 반복되는 표준 경로가 됐다.

### Blippar의 붕괴 — 광고형 AR 유니콘의 최후
| 항목 | 내용 |
| --- | --- |
| 주체 | Ambarish Mitra, Omar Tayeb, Steve Spencer, Jessica Butcher(런던). 투자자 Khazanah Nasional(말레이시아 국부펀드), Qualcomm Ventures, Candy Ventures |
| 연도 | 2011년 설립 / 2018년 12월 18일 법정관리 / 2019년 초 IP 매각 |
| 수치 | 2016년 초 직원 300명·14개국 사무소. Series D 5,400만 달러(2016). 총 조달 1억 3,170만 달러(4개 라운드, ZDNET/Crunchbase 기준, 보도에 따라 1억 3,200만~1억 4,000만 달러). 자칭 기업가치 15억 달러(2016). 2018년 12월 18일 법정관리, 2019년 2월 보도 기준 파산 시 잔고 약 6만 5,000달러. 2021년 재기 시도로 프리-시리즈A 500만 달러(€360만) |
| 출처 | CNBC 2018-12-18 'UK AR startup Blippar collapses into administration' / Engadget 2018-12-18 / Marketing Dive 2018-12-18(가치 15억 달러 언급) / ZDNET(조달 1억 3,170만 달러) / Business Insider 2020-11-22 '…a failed sale to Snap, and an investor fight' / Yahoo Finance 2019-02-22(잔고 6만 5,000달러) / Wikipedia, 'Blippar' |

제품 포장이나 인쇄 광고를 앱으로 스캔하면 콘텐츠가 뜨는 'blipp' 서비스를 광고주에게 캠페인 단위로 팔았다. 2011년 8월 캐드버리와 함께 iOS·안드로이드에 출시했고, 2014년 6월에는 Layar를 인수해 AR 브라우저 자산까지 흡수했다. 한때 AR 광고 시장을 대표하는 회사였다.

브랜드는 포장과 인쇄물이라는 '죽은 매체'를 측정 가능한 디지털 접점으로 바꾸고 싶어 했다. 2011~2015년에는 그 기능을 파는 회사가 따로 필요했다.

붕괴. 기술적 이유는 이미지 인식 자체가 상품화되어(애플·구글·페이스북이 무료 SDK로 제공) 해자가 사라진 것, 경제적 이유는 캠페인마다 3D 콘텐츠를 새로 제작해야 하는 에이전시형 원가구조여서 매출이 늘어도 마진이 붙지 않은 것이다. Snap에 매각을 시도했으나 무산됐고, 주주 Khazanah와의 분쟁으로 구제 증자가 막히면서 현금이 소진됐다.

### Google Glass 소비자판 — 기술이 아니라 사회가 거부한 실패
| 항목 | 내용 |
| --- | --- |
| 주체 | Google X, Sergey Brin |
| 연도 | 2012년 4월 공개 / 2013년 4월 16일 Explorer 배포 / 2014년 4월 15일 일반 판매 / 2015년 1월 15일 Explorer 프로그램 종료 |
| 수치 | 가격 1,500달러(영국 £1,000). Explorer 1차 배포 약 8,000명, 2013년 말 누적 약 1만 대로 추정(구글은 판매량을 끝까지 공개하지 않음). 사전 예약 2012-06-27 개시, Explorer 종료 2015-01-15, 기업용 판매 중단 2023-03-15 |
| 출처 | Wikipedia, 'Google Glass'(날짜·금지 조치·사건 기록) / CIO, 'How Many People Actually Own Google Glass?'(판매량 미공개와 추정치 논쟁) |

안경테 오른쪽에 프리즘 디스플레이와 전방 카메라를 단 웨어러블로, 음성 명령('OK Glass')과 관자놀이 터치패드로 조작하며 시야 한쪽에 알림과 길안내를 띄웠다. 스마트폰을 주머니에서 꺼내는 동작을 없애겠다는 발상이었다. 2013년 '#ifihadglass' 공모로 선발된 Explorer들에게 먼저 배포했고, 2014년 4월 15일과 5월 14일 이틀간 미국에서 일반 판매를 열었는데 재고가 하루 만에 소진됐다. 영국은 2014년 6월 £1,000에 출시.

'폰을 꺼내 보는 동작'을 없애려는 시도였다. 문제는 그 불편이 소비자에게 절박하지 않았다는 것이다 — 기업 현장(손이 자유로워야 하는 작업)과 달리, 소비자에게는 해결할 고통이 없었다.

실패, 그리고 그 원인이 기술이 아니었다는 점이 중요하다. 착용자가 아니라 주변 사람의 프라이버시를 침해하는 최초의 대중 기기였고 'Glasshole'이라는 낙인이 생겼다. 2014년 2월 샌프란시스코 바에서 착용자가 촬영 우려로 폭행당한 사건, 라스베이거스 카지노들의 착용 금지(네바다 도박규정), 2014년 10월 29일 MPAA와 전미극장주협회의 영화관 금지, 2013년 10월 캘리포니아의 운전 중 착용 딱지(작동 증거 부족으로 기각) 등이 이어졌다. 이후 Glass는 기업용으로만 살아남았다.

### Snapchat 렌즈와 Looksery — 얼굴 AR, 소비자 AR의 유일한 대량 성공
| 항목 | 내용 |
| --- | --- |
| 주체 | Snap Inc. / Looksery(Victor Shaburov, Yurii Monastyrshin, 2013년 설립, 우크라이나·샌프란시스코) |
| 연도 | 2015년 9월 Looksery 인수·Lenses 출시 / 2016년 12월 Cimagine 인수 / 2017년 4월 World Lenses |
| 수치 | Looksery 인수가 1억 5,000만 달러(2015년 9월, 당시 우크라이나 기술기업 최대 인수). Looksery는 2014년 6월 킥스타터에서 3만 달러 목표를 초과 달성. Cimagine 인수 3,000만~4,000만 달러(2016년 12월). 2022년 4월 CEO Evan Spiegel: '매일 2억 5,000만 명 이상이 AR 기능을 사용'(같은 분기 DAU 3억 3,200만 명 → 약 75%). 크리에이터 25만 명이 렌즈 250만 개 제작. 2023년 3월 투자자의 날: 지난 1년간 2억 5,000만 명이 AR 쇼핑 렌즈 사용 |
| 출처 | Wikipedia, 'Looksery' / Wikipedia, 'Snapchat' / Wikipedia, 'Snap Inc.' / Moneycontrol 2022-04-22(Spiegel 발언) / AR Insider 2023-03-14 'Snapchat Shopping Lenses: 5 Billion Served'(Snap Investor Day) |

얼굴 랜드마크를 실시간 추적해 얼굴 위에 텍스처·왜곡·3D 오브젝트를 입힌다. 공간을 이해하지 않고 얼굴만 이해하기 때문에 저사양 단말에서도 30fps가 나왔다 — 이 기술적 '얕음'이 곧 보급의 조건이었다. 2015년 '무지개 토하기' 렌즈가 사회 현상이 됐고, 브랜드는 스폰서드 렌즈를 사는 방식으로 광고에 들어왔다. 2017년 4월 World Lenses로 카메라 후면에도 3D 오브젝트를 놓기 시작했다.

소셜 앱에는 '보낼 것이 없는 날'이라는 문제가 있었다. 렌즈는 아무 일도 일어나지 않은 하루에도 보낼 거리를 만들어줬다. 이것은 기술 문제가 아니라 콘텐츠 공급 문제였다.

성공. 그러나 주의해야 할 성공이다 — 이것은 '현실 위에 정보를 겹치는' AR이 아니라 '얼굴을 바꾸는' AR이다. 공간 정합도, 측정도, 영속성도 필요 없다. 소비자 AR에서 규모를 낸 유일한 형태가 AR의 원래 정의에서 가장 먼 형태였다는 사실이 이 분야의 핵심 아이러니다.

### Pokémon Go — 분수령이자 오해의 출발점
| 항목 | 내용 |
| --- | --- |
| 주체 | Niantic(John Hanke, 2010년 구글 사내 스타트업, 2015년 10월 독립), 닌텐도, 포켓몬컴퍼니 |
| 연도 | 2016년 7월 6일 (호주·뉴질랜드·미국) |
| 수치 | 다운로드: 이틀 만에 미국 안드로이드 500만+, 1주 1,000만, 7월 13일 1,500만, 7월 31일 1억, 2016년 9월 5억, 2017년 2월 6억 5,000만, 2018년 5월 8억, 2019년 2월 10억. 매출: 2016년 9억 5,000만 달러, 2017년 8억 9,000만, 2018년 13억, 2019년 14억, 2020년 19억 2,000만 → 2020년까지 누적 64억 6,000만 달러. 이용: 미국 일일 이용 정점 2016-07-15, 2016년 9월 중순까지 미국 플레이어의 79% 이탈, 2017년 6월 활성 6,000만, 2018년 5월 MAU 1억 4,700만. 배터리: 고사양 Nexus 6에서 완충 배터리가 2~4시간에 소진(Mobile Enerlytics 측정), 배터리  |
| 출처 | Wikipedia, 'Pokémon Go'(다운로드·매출·이탈률·AR 모드 기술 서술) / Wikipedia, 'Niantic, Inc.' / CNET 2016-07-15 'How to save your battery while playing Pokemon Go'(AR 끄기 권고) / Mobile Enerlytics, 'A First Inside Look at Pokémon GO Battery Drain' |

기술적으로는 지극히 단순하다. 위치는 GPS, 화면 정합은 자이로스코프와 카메라 영상 합성이 전부다 — 공간을 인식하지도, 평면을 찾지도, 가림(occlusion)을 처리하지도 않는다. 위키백과의 서술 그대로 'AR 모드는 플레이어 기기의 카메라와 자이로스코프를 사용해 포켓몬이 현실에 있는 것처럼 표시한다'. 포켓스톱과 체육관 좌표는 전작 Ingress에서 이용자들이 등록한 포털 데이터를 그대로 재활용했다. 2017년 12월 ARKit 기반 AR+ 모드가 추가됐지만 어디까지나 선택 기능이었다.

엔터테인먼트 산업에는 '실내에 갇힌 플레이어를 밖으로 내보낼 이유'가 없었다. 위치기반 게임은 2012년부터 존재했지만 사람을 걷게 할 만큼 강한 IP가 없었다. 포켓몬은 애초에 '밖에 나가서 잡는다'는 서사를 가진 20년 된 IP였다 — 게임 메커닉과 IP 서사가 일치한 드문 사례다.

분수령이자 오해의 출발점. 'AR이 대중화됐다'는 서사를 만들었지만 실제로 팔린 것은 AR이 아니라 위치기반 수집 게임이었고, 당시 언론과 공략은 배터리를 아끼려면 AR을 끄라고 권고했다. 2025년 3월 12일 Niantic은 게임 사업을 Scopely에 35억 달러에 매각(5월 29일 완료)하고 지리공간 사업만 Niantic Spatial로 남겼다.

### Ingress 대 Pokémon Go — IP가 기술을 이긴 대조실험
| 항목 | 내용 |
| --- | --- |
| 주체 | Niantic(당시 구글 사내), John Hanke |
| 연도 | 2012년 11월 15일 안드로이드 비공개 베타 / 2013년 12월 14일 공개 / 2014년 7월 14일 iOS |
| 수치 | 활성 이용자 2013년 5월 약 50만 명, 2014년 2월 200만 명. 누적 다운로드 2013년 8월 100만, 2015년 1월 800만, 2018년 11월 2,000만. 2016년 7월까지 커뮤니티가 포털 1,500만 건을 신청해 그중 500만 건이 게임에 반영. 같은 시점 Pokémon Go 누적 다운로드는 10억(2019년) — 약 50배 차이 |
| 출처 | Wikipedia, 'Ingress (video game)' / Wikipedia, 'Pokémon Go' |

같은 회사, 같은 엔진, 거의 같은 수준의 AR(카메라 영상 위 오버레이), 같은 위치기반 메커닉이다. 다른 것은 IP 하나뿐이었다. Ingress는 이용자가 실세계의 조형물·표지판을 '포털'로 신청하게 해 지리 데이터베이스를 크라우드소싱했고, 그 데이터가 그대로 Pokémon Go의 포켓스톱과 체육관이 됐다.

2012년에 구글은 지도 데이터의 '사람이 실제로 서는 지점'을 알 방법이 없었다. Ingress는 게임을 대가로 그 데이터를 수집하는 장치였다 — AR은 목적이 아니라 수집의 구실이었다.

제품으로는 소규모 성공, 데이터 파이프라인으로는 완전한 성공. 2,000만 대 10억이라는 격차는 소비자 AR 대중화의 변수가 기술이 아니라 브랜드였음을 보여주는 가장 깨끗한 대조군이다.

### ARKit·ARCore의 등장과 Project Tango의 폐기 — 그리고 나타나지 않은 수요
| 항목 | 내용 |
| --- | --- |
| 주체 | Google ATAP(Tango), Google(ARCore), Apple(ARKit, 2015년 5월 Metaio 인수로 기술 확보) |
| 연도 | Tango 2014년 6월 5일 발표 → 2018년 3월 1일 지원 종료 / ARKit 2017년 6월(iOS 11) / ARCore 2017년 8월 발표, 2018년 2월 23일 1.0 |
| 수치 | Tango: 개발자용 Yellowstone 태블릿 2015년 6월까지 3,000대 판매, 상용 단말은 Lenovo Phab 2 Pro(2016년 11월 미국 출시, 목표가 500달러 미만)와 Asus ZenFone AR(CES 2017) 단 2종, 지원 종료 2018-03-01. ARKit: A9 이상 프로세서 필요. Sensor Tower 집계(2018년 4월): ARKit 전용 앱 누적 다운로드가 2018년 3월 1,300만 건으로 6개월 전의 4배 이상, App Store의 AR 대응 앱 2,000개 돌파, 다운로드 구성은 게임 47%·유틸리티 14%·라이프스타일 11% |
| 출처 | Wikipedia, 'Tango (platform)' / Wikipedia, 'ARCore' / Wikipedia, 'ARKit' / Marketing Dive 2018-04-06 'Ikea Place ranks as No. 2 free ARKit app'(Sensor Tower 데이터 인용) |

Tango는 적외선 깊이 센서를 단말에 넣어 정확한 3D를 얻으려 했고, ARKit과 ARCore는 일반 카메라와 IMU만 쓰는 시각관성주행거리계(VIO)로 정확도를 포기하는 대신 기존 단말 전부를 대상으로 삼았다. 구글은 자사 전략을 2년 만에 뒤집고 Tango를 죽였다. 결과적으로 마커 없이 바닥을 찾아 물체를 놓는 일이 수억 대 단말의 기본 기능이 됐다.

전용 하드웨어를 요구하면 설치기반이 만들어지지 않는다는 것이 Tango의 교훈이다. 플랫폼 기업들은 정확도보다 보급률을 택했다.

플랫폼 문제는 해결됐는데 수요는 나타나지 않았다. 수억 대 단말이 AR을 지원하게 된 시점에도 AR 전용 앱 누적 다운로드는 1,300만 건에 그쳤다. 기대와 실제 사용의 격차를 보여주는 가장 단단한 수치이며, 이후 AR은 독립 앱이 아니라 기존 앱의 한 기능으로만 살아남는다.

### IKEA — 카탈로그 AR(2013)에서 IKEA Place(2017)로
| 항목 | 내용 |
| --- | --- |
| 주체 | IKEA(Inter IKEA Systems). IKEA Place는 Apple ARKit·iOS 11 출시에 맞춰 공개 |
| 연도 | 2013년 카탈로그 AR / 2017년 9월 IKEA Place / 2020년 12월 카탈로그 폐간 발표 |
| 수치 | 카탈로그 발행부수: 1951년 초판 28만 5,000부 → 2013년 약 2억 800만 부 → 2016년 2억 부(69개 판·32개 언어·50여 개국) → 2021년 최종판 4,000만 부. IKEA Place 초기 수록 제품 약 2,000점, 축척 정확도 98% 주장(IKEA 자체 발표). 2018년 4월 기준 ARKit 무료 앱 다운로드 2위(Sensor Tower) |
| 출처 | Wikipedia, 'IKEA Catalogue'(발행부수·AR 도입·폐간) / Wikipedia, 'IKEA' / IKEA Newsroom, 'IKEA Place, a furniture-placement app with AR tech'(98% 정확도) / TechCrunch 2017-09-14 / Marketing Dive 2018-04-06 |

2013년판 카탈로그는 지면의 심벌을 스캔하면 가구 내부를 들여다보는 'X-ray' 뷰와 영상이 뜨는 마커 AR이었다. 2014년판부터는 카탈로그 책자 자체를 바닥에 놓아 축척 기준점으로 삼고 방 사진 위에 가구를 합성했다 — 인쇄물 2억 부가 곧 전 세계에 배포된 마커였던 셈이다. 2017년 IKEA Place는 ARKit의 평면 검출을 써서 마커를 완전히 없앴고, 조명과 그림자, 직물 질감까지 렌더링했다.

가구는 반품 비용이 가장 비싼 상품군이다 — 부피, 배송, 조립이 모두 되돌려져야 한다. '치수는 맞는데 막상 놓으면 커 보인다'는 공간 불확실성이 온라인 구매를 막는 구체적 장애였고, AR은 정확히 그 불확실성만 겨냥했다.

AR은 남고 카탈로그는 죽었다. 2020년 12월 IKEA는 70년 된 카탈로그의 폐간을 발표하며 '고객과 연결되는 새로운 방식' 때문에 카탈로그의 중요성이 줄었다고 밝혔다. AR이 인쇄물을 보조하러 들어왔다가 인쇄물을 대체한 사례다.

### 전자상거래 AR의 '반품 감소' 주장과 그 근거의 격차
| 항목 | 내용 |
| --- | --- |
| 주체 | 주장 측: Shopify, Loop Returns, SeekXR, Build.com, Gunner Kennels, Rebecca Minkoff 등 벤더·브랜드 사례연구 / 학술 측: Tan Yong-Chin·Chandukala·Reddy(2021), Heller·Chylinski·de Ruyter·Mahr(2019) |
| 연도 | 2017~2026 |
| 수치 | 벤더 주장: Shopify 사례 반품 40% 감소, SeekXR 25% 감소, Build.com 'AR 이용 고객이 22% 덜 반품', Gunner Kennels 반품률 5% 감소, Rebecca Minkoff 3D 모델 조작 후 장바구니 담기 44%↑·주문 27%↑·AR 상품페이지 구매 65%↑. 학술: Tan Yong-Chin, Chandukala, Reddy, 'Augmented Reality in Retail and Its Impact on Sales', Journal of Marketing, 2021, DOI 10.1177/0022242921995449, 피인용 285회(Crossref 기준). Heller 외, 'Touching the Untouchable: Exploring Multi-Senso |
| 출처 | Shopify Blog, 'AR shopping'(Rebecca Minkoff·Gunner Kennels 사례) / Loop Returns 2022-01-18 'Using AR technology to lower your ecommerce return rate'(Shopify 40%·SeekXR 25%·Build.com 22%) / Crossref: DOI 10.1177/0022242921995449, DOI 10.1016/j.jretai.2019.10.008 |

AR 도입 근거로 가장 많이 인용되는 '반품 감소' 수치는 거의 전부 AR 공급자 또는 도입 브랜드가 스스로 낸 사례연구이며, 대조군·관측 기간·반품의 조작적 정의가 공개되지 않는다. 반면 실제 거래 데이터를 분석한 연구는 훨씬 조건부의 결론을 낸다. Tan 외(2021)는 국제 화장품 리테일러의 모바일 앱 데이터로, AR 사용이 매출을 올리는 것은 '제품 불확실성이 높을 때'뿐임을 보였다 — 덜 알려진 브랜드, 취향이 갈리는 제품, 비싼 제품, 그리고 해당 채널이나 카테고리를 처음 쓰는 고객에서만 효과가 나타났다. 즉 AR은 평균 전환율을 올리는 장치가 아니라 불확실성을 깎는 장치다.

온라인 의류·가구 반품률이 수익을 잠식하는 수준에 이르자 리테일러는 '만져보지 못함'을 대체할 장치가 필요했다. 반품은 매출과 달리 회계장부에 직접 찍히는 비용이라 AR 투자 결재를 통과시키기 쉬운 명분이었다.

주장과 근거 사이의 격차가 지금도 남아 있다. AR의 효과는 존재하지만 '모든 상품에서 반품이 줄어든다'가 아니라 '불확실성이 큰 곳에서만 줄어든다'가 학술적으로 지지되는 범위다. 어느 분야에서든 AR의 ROI를 인용할 때는 누가 측정했는지를 먼저 확인해야 한다.

### Snap Spectacles — 소비자 AR 안경의 두 번째 실패
| 항목 | 내용 |
| --- | --- |
| 주체 | Snap Inc. |
| 연도 | 2016년 11월 10일 1세대 / 2018년 4월 26일 2세대 / 2019년 11월 3세대 / 2021년 5월 4세대(첫 AR 디스플레이) / 2024년 9월 17일 5세대 |
| 수치 | 2017년 말 미판매 재고·미사용 부품 4,000만 달러 상각. 2018년 5월까지 누적 판매 22만 대(목표에 크게 미달). 3세대 가격 380달러. 4세대: 대각 시야각 26.3도, Snapdragon XR1, 듀얼 3D 도파관. 5세대: 대각 시야각 46도, 37 PPD, 카메라 4개, 완전 독립 구동, Snap OS. 참고로 Snap의 2017년 3월 2일 IPO 시가총액은 약 240억 달러 |
| 출처 | Wikipedia, 'Spectacles (product)'(세대별 날짜·시야각·4,000만 달러 상각·22만 대) / Wikipedia, 'Snap Inc.' |

1세대는 엄밀히 AR이 아니라 원형 영상을 찍는 카메라 안경이었다. 자판기 'Snapbot'을 게릴라식으로 배치해 희소성 마케팅을 했고 초기에는 줄이 섰지만 수요가 곧 증발했다. 실제 AR 디스플레이가 들어간 것은 2021년 4세대부터인데, 이때부터 Snap은 일반 판매를 포기하고 개발자에게만 배포하는 전략으로 전환했다.

Snap은 렌즈로 얼굴 AR을 이미 장악했으므로, 그 AR을 얼굴에서 세계로 옮길 자체 하드웨어가 필요했다. 폰 카메라에 머무는 한 애플·구글의 플랫폼 정책에 종속되기 때문이다.

실패. 경제적으로는 수요 예측 실패(22만 대 판매, 4,000만 달러 상각), 기술적으로는 시야각(26도→46도)과 배터리·발열이 소비자 제품 기준에 못 미쳤다. Google Glass 이후에도 같은 벽이 그대로였다는 점이 요지다 — 소비자 AR 안경의 제약은 소프트웨어가 아니라 광학과 전력이다.

### 정리기 — Meta Spark 종료, Niantic 매각, Vision Pro
| 항목 | 내용 |
| --- | --- |
| 주체 | Meta, Niantic/Scopely, Apple, Magic Leap |
| 연도 | 2024~2026 |
| 수치 | Meta Spark AR Studio 2019년 출시 → 2025년 1월 종료. Niantic: 2025년 3월 12일 Scopely에 게임 사업 35억 달러 매각(5월 29일 완료), 감원 2023년 6월 230명·2025년 4월 68명, 지리공간 부문은 Niantic Spatial로 분사. Apple Vision Pro: 2023년 6월 5일 발표, 2024년 2월 2일 출시, 3,499달러(2026년 6월 25일 3,699달러로 인상), 2024년 1월 19일 예약 18분 만에 매진, 예약 2주간 약 20만 대, 초기 출하 추정 6만~8만 대. Magic Leap: 총 조달 35억 달러 이상, 기업가치 2016년 12월 45억 달러 → 2020년 9월 4억 5,000만 달러(6개월 만에 93% 하락), |
| 출처 | Wikipedia, 'Spark AR Studio' / Wikipedia, 'Niantic, Inc.'(Scopely 35억 달러, 감원) / Wikipedia, 'Apple Vision Pro'(가격·예약·출하 추정) / Wikipedia, 'Magic Leap'(조달·기업가치·감원) |

2024~2025년에 소비자 AR의 두 축이 동시에 정리됐다. 플랫폼 기업은 서드파티 AR 저작 도구를 닫았고(Meta의 Spark AR Studio), AR 게임의 상징이던 회사는 게임 사업을 팔고 지도·지리공간 데이터 회사로 남았다(Niantic). 하드웨어 쪽에서는 애플이 3,499달러짜리 Vision Pro로 다시 시도했으나 초기 출하량은 소비자 제품이라기보다 개발자 키트에 가까운 규모였다. Magic Leap은 소비자 시장을 이미 2020년에 포기했다.

광고 예산이 AI로 이동했고, 렌즈·필터는 이미 각 플랫폼의 기본 기능으로 흡수되어 별도의 크리에이터 생태계를 유지할 경제적 이유가 사라졌다.

소비자 AR은 '독립 산업'에서 'OS의 한 기능'으로 격하됐다. 산업으로서는 축소됐지만 기능으로서는 편재화됐다 — 오늘날 AR은 별도의 앱이 아니라 카메라 앱, 지도 앱, 쇼핑 앱 안의 버튼 하나로 존재한다.

#### 검증에서 잡힌 정정
- [수치 오류·출처 모순] Pokémon Go '배터리 절약 모드의 절감폭은 19%에 그침'. 인용 출처인 Mobile Enerlytics 'A First Inside Look at Pokémon GO Battery Drain' 원문을 직접 확인한 결과, 절약 모드의 플레이 시간 연장 폭은 화면 밝기 30%/50%/80%에서 각각 23%, 30%, 40%로 명시돼 있다. 19%라는 숫자는 해당 출처에 존재하지 않는다. (나머지 '완충 2~4시간', 'Nexus 6', 'AR 캡처 시 1.95시간'은 일치)
- [대상 misattribution + 표현 오류] Tango '개발자용 Yellowstone 태블릿 2015년 6월까지 3,000대 판매'. Wikipedia 'Tango (platform)' 원문은 2015년 6월까지 Peanut 폰과 Yellowstone 태블릿을 **합쳐** 3,000대 **이상**(more than 3,000)이 판매됐다고 서술한다. 태블릿 단독 3,000대가 아니며 '3,000대'로 상한처럼 못박은 것도 틀렸다.
- [연도 오류] Tango '2014년 6월 5일 발표'. 6월 5일은 Wikipedia 인포박스의 initial release(개발자 키트 출시일)이고, Project Tango가 Google ATAP에 의해 공개 발표된 것은 2014년 2월 20일이다. '발표'로 쓰면 4개월 오차. (지원 종료 2018-03-01, Lenovo Phab 2 Pro 2016-11 미국 출시·$500 미만 목표가는 일치)
- [연도·기준 혼동] Magic Leap '기업가치 2016년 12월 45억 달러 → 2020년 9월 4억 5,000만 달러(6개월 만에 93% 하락)'. Wikipedia 'Magic Leap' 원문은 2019년 64억 달러 → 2020년 **6월** 4억 5,000만 달러로 6개월 만에 93% 하락이라고 서술한다. 즉 (1) 하락 시점은 9월이 아니라 6월, (2) 93%의 기준은 2016년 12월 45억 달러(Forbes 추정)가 아니라 2019년 64억 달러다. 45억→4.5억은 90% 하락이며 6개월이 아니라 3년 반에 걸친 변화다. 두 개의 서로 다른 평가액을 하나의 문장으로 접합한 오류.
- [사실관계 오류] 서사 '(Layar·Wikitude·junaio) 셋 다 소비자 앱을 버리고 B2B SDK로 피신한 끝에 퀄컴과 애플에 흡수됐다'. Layar는 퀄컴도 애플도 아닌 영국 Blippar에 2014년 6월 인수됐고(Wikipedia 'Layar'로 확인), Blippar 붕괴 후 2019년 1월 공동창업자들이 IP 재매입을 검토했다. 퀄컴(Wikitude)·애플(Metaio)에 흡수된 것은 3사 중 2사뿐이다.
- [인과·연대 오류] 서사 '2009년 Flash 포팅으로 웹캠 달린 PC가 모두 AR 단말이 됐다. 그래서 첫 소비자 AR은 광고였다. 2008년 11월 MINI는…'. 결과(2008년 11~12월 MINI 광고)가 원인(2009년 FLARToolKit)보다 앞선다. 더욱이 인용 출처인 Hackaday 2008-12-13 원문을 확인한 결과 MINI 광고는 Flash/FLARToolKit이 아니라 뮌헨 Metaio의 **Unifeye SDK**로 구동됐고, Internet Explorer와 **ActiveX**를 요구해 크로스플랫폼 지원조차 없었다. Flash 포팅이 MINI 광고를 가능하게 했다는 서사는 성립하지 않는다.
- [근거 없는 성과 주장 — 독립 검증 전무] 전자상거래 AR 반품 감소 수치 전부. Shopify 'AR shopping' 블로그 원문을 직접 확인한 결과 **40% 반품 감소 주장은 이 페이지에 존재하지 않는다**. Loop Returns(2022-01-18) 원문에는 'Shopify 40%', 'SeekXR 25%', 'Build.com 22%'가 실려 있으나 세 수치 모두 해당 기업의 자체 발표를 재인용한 것이고 원자료·표본·측정방법·대조군이 공개돼 있지 않다. Rebecca Minkoff 44%/27%/65%와 Gunner Kennels 5%도 Shopify 자사 case-studies 내부 링크만 있을 뿐 외부 출처가 없다. 함께 유통되는 '전환율 94% 증가'도 무출처. 즉 전부 벤더 마케팅 자료의 순환 인용이며 독립 검증된 것은 하나도 없다.
- [학술 근거의 오적용] 위 반품 감소 주장의 '학술 측' 근거로 제시된 Tan·Chandukala·Reddy(2021)는 Crossref에서 제목이 문자 그대로 'Augmented Reality in Retail and Its Impact on **Sales**'로 확인된다 — 매출·구매행동 연구이지 **반품률을 측정한 연구가 아니다**. Heller 외(2019) 'Touching the Untouchable'도 다감각 AR의 심리적 효과 연구로 반품률 측정이 아니다. 따라서 '학술적으로 지지되는 범위는 불확실성이 큰 곳에서만 반품이 줄어든다'는 정리는 이 두 논문으로 뒷받침되지 않는다. (DOI·연도·저널·피인용 285회/237회 자체는 Crossref API에서 정확히 일치)
- [저자 누락] Heller 외 2019 저자를 'Heller, Chylinski, de Ruyter, Mahr' 4인으로 적었으나 Crossref 기록상 저자는 Jonas Heller, Mathew Chylinski, Ko de Ruyter, Dominik Mahr, **Debbie I. Keeling** 5인이다.
- [연도 오류] 'Meta Spark AR Studio 2019년 출시'. Wikipedia 'Spark AR Studio' 문서가 2019년으로 적고 있으나(해당 문서는 출처 부실), 이 도구는 2017년 4월 F8에서 'AR Studio'로 공개돼 2017년 12월 개방됐고 2019년은 'Spark AR'로 **개명**한 해다. 또한 종료는 '2025년 1월'이 아니라 2025년 1월 14일로 특정 가능하다.
- [근거 없는 날짜 특정] Metaio '애플이 2015년 5월 21~22일 인수 완료'. Wikipedia 'Metaio'와 'ARKit' 모두 'May 2015'까지만 기술하며 21~22일이라는 날짜는 어느 인용 출처에도 없다. 인수 사실이 보도된 것은 2015년 5월 하순(5월 28일 전후)이다. 일 단위 특정은 출처를 초과한 서술.
- [출처 확인 불가 + 날짜 의심] Esquire AR호 '발매 2009-11-10'. 인용된 Engadget 2009-11-10 기사 URL은 현재 조회되지 않으며(404), Wikipedia 'Esquire (magazine)' 문서에는 AR호 관련 서술이 아예 없다. 2009년 12월호의 실제 가판 발매일은 2009년 11월 16일로 보도된 사례가 다수이고 11월 9~10일은 사전 공개/시연 시점이다. 발매일과 공개일의 혼동 가능성이 높으며 현 상태로는 무검증.
- [출처 URL 사망 + 수치 해석 오류] 'Sensor Tower 집계(2018년 4월): ARKit 전용 앱 누적 다운로드가 2018년 3월 1,300만 건으로 6개월 전의 4배 이상'. 인용된 Marketing Dive 2018-04-06 URL은 404다. 또한 ARKit은 2017년 9월 출시로 '6개월 전'이면 출시 시점 자체여서 '4배 이상'이라는 비교 기준이 성립하지 않는다(원 보도는 '출시 후 6개월간 누적 1,300만' 프레이밍). 나아가 이 1,300만은 **ARKit 전용 앱**만 집계한 값이어서, Snapchat·Pokémon Go·IKEA 등 기존 앱 내부의 AR 사용을 배제한다. 이를 근거로 '수요가 나타나지 않았다'고 단정하는 것은 지표의 범위를 넘어선 해석이다.
- [추정치를 수치처럼 제시] Google Glass '2013년 말 누적 약 1만 대'. Wikipedia가 확인해 주는 것은 #IfIHadGlass 선발 8,000명뿐이고, 1만 대는 구글이 판매량을 공개하지 않은 상태에서 언론이 낸 추정치다. 본문이 '추정'이라 덧붙인 점은 타당하나 확정 수치와 나란히 배치돼 있어 오독을 유발한다.
- [시점 압축] Blippar '2018년 12월 18일 잔고 6만 5천 달러로 법정관리에 들어갔다'(서사 부분). 6만 5,000달러는 본문 각주가 스스로 밝히듯 2019년 2월 관리인 보고 기준 수치이지 2018-12-18 시점의 잔고로 확인된 값이 아니다. 또한 총 조달 1억 3,170만 달러와 자칭 기업가치 15억 달러는 Wikipedia 'Blippar' 본문에 없고(직접 확인), ZDNET/Crunchbase·Marketing Dive 재인용에만 의존한다.
- [연대 부정확] 서사 '2009~2011년 Layar·Wikitude·junaio 같은 AR 브라우저'. Wikitude World Browser는 2008년 10월 20일 출시로 2009년보다 앞선다(Wikipedia 'Wikitude'). 본문 각주는 2008-10-20을 정확히 적고 있어 서사와 각주가 불일치한다.
- Magic Leap 기업가치 하락 — 기준점과 날짜가 모두 틀렸다. 연구: '2016년 12월 45억 달러 → 2020년 9월 4억 5,000만 달러(6개월 만에 93% 하락)'. 실제(위키백과 원문): The Information이 2020년 9월에 '2019년 64억 달러 → 2020년 6월 4억 5,000만 달러, 6개월간 93% 하락'이라고 보도했다. 즉 93%·6개월의 기준은 2019년 64억 달러이지 2016년 45억 달러가 아니며, 4억 5,000만 달러는 2020년 6월 값이고 9월은 보도 시점이다. 45억→4.5억은 3년 반에 걸친 90% 하락으로 '6개월 93%'와 무관하다.
- Magic Leap 회복 누락 — 2021년 10월 VentureBeat 보도 기준 미상의 투자자로부터 5억 달러를 조달해 기업가치가 20억 달러로 회복됐고 2022년 Magic Leap 2를 출시했다. 연구는 이 반전을 통째로 빼고 '4억 5,000만 달러'에서 서사를 끝내 붕괴 서사를 과장했다.
- Pokémon Go 배터리 절약 모드 '19%' — 출처 수치와 불일치. 연구가 인용한 Mobile Enerlytics 'A First Inside Look at Pokémon GO Battery Drain'의 실제 측정값은 화면 밝기 30%에서 23%, 50%에서 30%, 80%에서 40% 절감이다. 19%라는 값은 해당 출처에 없다. 또 같은 연구의 핵심 발견은 'AR 모드를 끄면 포획 시 배터리 수명이 거의 두 배가 된다(카메라가 총 전력의 약 56% 소비)'인데, 연구는 절감폭을 축소한 숫자만 취해 '절약 모드는 소용없었다'는 인상을 만들었다.
- Layar의 인수 주체 — 서사 단락의 'Layar·Wikitude·junaio 셋 다 … 퀄컴과 애플에 흡수됐다'는 틀렸다. Layar는 2014년 6월 영국 Blippar에 인수됐고(위키백과 'Layar' 확인), 퀄컴·애플과 무관하다. 퀄컴=Wikitude(2021년 9월), 애플=Metaio/junaio(2015년 5월)뿐이다. 연구의 세부 항목은 Blippar 인수를 정확히 적어놓고 서사에서 스스로 부정했다.
- FLARToolKit → MINI 인과 역전 — 서사는 '2009년 Flash 포팅으로 … 그래서 첫 소비자 AR은 광고였다'며 2008년 11월 MINI를 사례로 든다. MINI(2008년 11~12월)는 FLARToolKit(2009년)보다 앞서므로 인과가 불가능하다. Hackaday(2008-12-13)는 MINI 광고가 Metaio Unifeye SDK 기반이며 Internet Explorer의 ActiveX를 요구해 타 브라우저·OS에서는 작동하지 않았다고 기록한다 — Flash 기반이 아니다.
- Blippar '자칭 기업가치 15억 달러(2016)' — 성격과 연도가 어긋난다. VentureBeat(2018-12-18, 위키백과가 인용하는 원 보도)에 따르면 15억 달러는 2015년 익명 기업이 제시했다고 전해지는 인수 제안액이지 Blippar가 2016년에 자칭한 기업가치가 아니다. 같은 보도는 이후 Snap이 약 2억 달러를 제안했다고 전한다. '스스로 15억 달러라 말하던 회사'라는 서사적 표현은 인용 보도로 뒷받침되지 않는다.
- Blippar 법정관리 날짜 — 연구는 '2018년 12월 18일'을 단정한다. 동시대 1차 보도인 VentureBeat는 발표를 12월 17일로 적고 기사 자체가 12월 18일자다(CNBC·Engadget도 18일자 보도). 18일은 보도일이지 법정관리 개시 확정일로 단정할 근거가 제시되지 않았다.
- Blippar 항목의 출처 오귀속 — 연구는 '총 조달 1억 3,170만 달러', '자칭 기업가치 15억 달러', '2018년 12월 18일 법정관리', '잔고 약 6만 5,000달러'의 출처 목록에 Wikipedia 'Blippar'를 포함했다. 해당 문서 원문(wikitext)을 직접 확인한 결과 이 네 수치 중 어느 것도 들어 있지 않다. 위키백과는 Series D 5,400만 달러, 직원 300명/14개 사무소, 2019년 초 Nick Candy 투자사에 IP 매각, 2021년 500만 달러만 기재한다.
- Tan·Chandukala·Reddy 논문 연도 — Crossref 기준 Journal of Marketing 2022년, 제86권 1호 48~66쪽(온라인 선공개 2021-06-16)이다. 연구는 '2021년'으로만 적어 게재 연도를 잘못 표기했다.
- 같은 논문의 주제 오적용 — 'Augmented Reality in Retail and Its Impact on Sales'는 제목 그대로 국제 화장품 소매업체 데이터로 AR이 '매출'에 미치는 영향을 측정한 연구이며, 반품률(returns)은 다루지 않는다. 연구는 이 논문을 '반품 감소 주장'에 대한 학술적 반증으로 세웠으나 측정 대상이 다르다. 논문의 실제 결론은 '인지도 낮은 브랜드·수요층이 좁은 상품·고가 상품에서 효과가 크고 신규 고객에서 가장 강하다'이다.
- Heller 외 논문 저자 누락 — Crossref 기준 저자는 Jonas Heller, Mathew Chylinski, Ko de Ruyter, Dominik Mahr, **Debbie I. Keeling** 5인이다. 연구는 4인만 적어 제5저자를 빠뜨렸다.
- 반품 감소 수치의 독립 검증 부재 — Shopify 40%, SeekXR 25%, Build.com 22%, Gunner Kennels 5%, Rebecca Minkoff 44%/27%/65%는 모두 Loop Returns(반품관리 SaaS 벤더)의 자사 블로그 사례를 단일 경로로 하는 마케팅 수치다. 표본 크기·측정 기간·대조군·상품군·선택편향이 전혀 공개돼 있지 않으며 동료심사도 독립 재현도 없다. 출처를 제공한 Loop Returns 자체가 해당 주장으로 이익을 얻는 당사자라는 점이 명시되지 않았다.
- Snap '매일 2억 5,000만 명 AR 사용' — Snap의 자사 투자자 발표(2022년 4월 Spiegel 발언, 2023년 3월 투자자의 날)이며 독립 감사나 제3자 계측이 없다. 위키백과 'Snapchat'·'Snap Inc.' 문서에는 이 수치가 실려 있지 않다(World Lenses 2017년 4월, 2022년 7월 DAU 3억 4,700만만 확인됨). 'AR 기능 사용'의 정의가 렌즈·필터 1회 탭까지 포함하는 광의여서 공간정합 AR 사용률로 읽으면 과대해석이다. '크리에이터 25만 명·렌즈 250만 개'도 동일하게 자사 집계다.
- IKEA Place '축척 정확도 98%' — IKEA 자체 보도자료 수치이며 측정 방법·조건·오차 정의가 공개된 적이 없고 독립 검증도 존재하지 않는다. 연구가 '(IKEA 자체 발표)'라고 병기한 점은 타당하나, 이 수치는 검증된 성능이 아니라 마케팅 주장으로 취급되어야 한다.
- (외 25건)

## heritage_arch — 문화유산·건축·도시 분야의 증강현실 전개
항목 15개 · 검증 정정 지적 46건

> 1997년 컬럼비아대의 Touring Machine이 배낭 컴퓨터·차등GPS·시스루 HMD로 캠퍼스 건물 위에 이름표를 띄우면서, AR은 실내 마커를 떠나 '측량되지 않은 도시'와 정면으로 마주쳤다. 1999년 Azuma는 이를 「야외에서 AR을 작동시키는 것의 난제」로 정식화했다 — 정합 오차, 센서 드리프트, 햇빛 아래의 대비, 전력, 그리고 통제할 수 없는 환경. 같은 해 Höllerer의 Situated Documentaries가 장소에 서사를 묶었고, 2000년 남호주대 ARQuake는 50cm급 측량용 DGPS에만 약 4천 달러, 전체 1만 달러가 넘는 장비 목록으로 야외 AR의 경제성을 숫자로 드러냈다. 2000~2002년 EU의 ARCHEOGUIDE(총 485만 유로, EU 분담 260만 유로)는 올림피아 유적에 헤라 신전 복원을 겹쳤지만, GPS만으로는 기둥 하나에 맞출 수 없어 사전 촬영한 기준영상과의 영상 대조로 보정해야 했고, 프로젝트 종료와 함께 현장에서 사라졌다. 2006년 Reitmayr–Drummond의 모델 기반 야외 추적이 기술적 돌파를 냈지만 '3D 도시 모델이 미리 있어야 한다'는 전제는 남았다. 2008~2014년 Layar·Wikitude의 지오브라우저 세대는 스마트폰으로 진입장벽을 없앴으나, GPS·나침반 오차 탓에 결국 '떠다니는 아이콘'에 머물렀고 인수·소멸했다. 이후 문화유산 AR은 정합이 쉬운 실내 박물관으로 후퇴했다. 건설은 반대 방향으로 갔다 — 2019년 Trimble XR10+HoloLens 2가 BIM 모델을 현장에 1:1로 겹쳤으나, 헤드셋 자체가 단종 수순을 밟았다. 지하 매설물 X-ray vision은 2009년 이래 '킬러앱'으로 반복 거론되지만, 근본 문제가 AR이 아니라 '도면이 틀린다'(ASCE 38 QL-D)는 데이터 품질이어서 정착하지 못했다. 2022년 ARCore Geospatial API가 스트리트뷰 기반 VPS로 정합을 인프라로 옮기면서, 야외 AR은 비로소 '장비'가 아니라 '지도'의 문제가 되었다.


### Touring Machine — 야외 모바일 AR의 원형
| 항목 | 내용 |
| --- | --- |
| 주체 | Steven Feiner, Blair MacIntyre, Tobias Höllerer, Anthony Webster — Columbia University, Computer Graphics and User Interfaces Lab |
| 연도 | 1996 연구 시작 / 1997 발표(ISWC'97 및 Personal Technologies 저널판) / 상용화 없음 |
| 수치 | 피인용 248(ISWC'97, Crossref) / 304(Personal Technologies, Crossref); 연구 시작 1996; ONR 계약 N00014-97-1-0838, NSF CDA-92-23009 |
| 출처 | Feiner S., MacIntyre B., Höllerer T., Webster A. (1997) "A touring machine: prototyping 3D mobile augmented reality systems for exploring the urban environment", ISWC'97, doi:10.1109/iswc.1997.629922 / Personal Technologies, doi:10.1007/bf01682023; Columbia MARS 프로젝트 페이지 https://graphics.cs.columbia.edu/projects/mars/ |

배낭에 3D 그래픽 가속 컴퓨터, 차등 GPS(DGPS), 방위 추적기가 달린 광학 시스루 HMD, 무선 네트워크를 지고 컬럼비아 캠퍼스를 걸으면 건물 위에 이름표와 메뉴가 겹쳐 떴다. 손에 든 스타일러스 펜 컴퓨터가 HMD에 뜬 내용을 조작하는 2화면(head-worn + hand-held) 구조였는데, 이 하이브리드 UI 자체가 논문의 핵심 기여였다. 라벨은 시야 중심에 가까울수록 밝아지고, 건물을 일정 시간 응시하면 선택되어 그 건물의 학과 목록이 건물 주위에 3D로 배열됐다. 선택 결과는 동시에 손에 든 컴퓨터의 웹 브라우저에 URL로 전달됐다. 이후 시스템은 DGPS에서 실시간 이동측위(RTK) GPS+GLONASS로, 컬럼비아 자체 개발 대역확산 무선에서 IEEE 802.11a/b로 갱신됐다.

1990년대 중반까지 AR은 보잉의 배선 조립, 의료 영상 중첩처럼 실내·통제 환경에 머물렀다. 반면 건축·도시 정보는 본질적으로 '현장에 붙어 있는' 정보인데, 그것을 현장에서 볼 수단이 종이 지도와 안내판뿐이었다. 캠퍼스라는 좁고 미리 측량된 공간, 그리고 차등 GPS로 '건물 단위 식별'은 가능해졌다는 판단이 야외 시도를 촉발했다. 즉 기술이 무르익어서가 아니라, 정보와 장소의 분리라는 건축·도시 고유의 문제가 먼저 있었다.

연구로는 성공, 제품으로는 부재. Crossref 기준 ISWC판 피인용 248회, Personal Technologies 저널판 304회로 이후 모든 야외 AR 가이드의 조상이 됐다. 그러나 배낭 규모를 벗어난 적이 없고 상용 제품으로 이어지지 않았다. 실패라기보다 '하드웨어가 20년 뒤에야 따라온 설계'에 가깝다.

### Azuma의 야외 AR 난제 정식화 — 문제를 이름 붙인 문서
| 항목 | 내용 |
| --- | --- |
| 주체 | Ronald Azuma — HRL Laboratories |
| 연도 | 1997(AR 서베이) / 1999(야외 난제 章) / 2001(Recent Advances 후속) |
| 수치 | 「A Survey of AR」 Presence 6(4), 1997, 피인용 6,839(Crossref); 「The Challenge of Making AR Work Outdoors」 1999, 피인용 75(Crossref) |
| 출처 | Azuma R. (1997) Presence: Teleoperators and Virtual Environments, doi:10.1162/pres.1997.6.4.355; Azuma R. (1999) in Mixed Reality, doi:10.1007/978-3-642-87512-0_21 |

1997년 Presence에 실린 「A Survey of Augmented Reality」가 AR을 (1) 실재와 가상의 결합, (2) 실시간 상호작용, (3) 3차원 정합이라는 세 조건으로 정의했다. 여기서 세 번째 조건인 '정합(registration)'이 AR을 VR과 갈라놓는 지점이자, 야외에서 무너지는 지점이다. 1999년 Azuma는 「The Challenge of Making Augmented Reality Work Outdoors」에서 실내와 야외를 명시적으로 분리했다. 실내는 환경을 준비할 수 있다 — 마커를 붙이고, 조명을 고정하고, 추적 장비를 천장에 달 수 있다. 야외는 그 어느 것도 할 수 없으며, 대신 GPS 오차·자기 나침반 왜곡·자이로 드리프트·직사광 아래 디스플레이 대비·전력이라는 다섯 개의 독립적 제약을 동시에 받는다. 그의 결론은 단일 센서로는 불가능하고 '하이브리드 추적'이 필수라는 것이었다.

1997~1999년은 Touring Machine, ARQuake, 초기 군용 야외 AR이 동시에 등장하면서 '왜 야외에서만 유독 어긋나는가'가 각 연구실의 공통 좌절이 된 시점이다. 문제가 개별 구현의 버그가 아니라 구조적임을 밝힐 문서가 필요했다. 이 문서 이후 야외 AR 논문의 표준 서론이 '야외는 다르다'로 시작하게 된다.

성공 — 다만 해결이 아니라 정의로서. 1997년 서베이는 Crossref 피인용 6,839회로 AR 분야 최다 인용 문헌 중 하나다. 1999년 야외 章은 피인용 75회로 적지만, 그가 지목한 다섯 제약은 25년이 지난 2020년대에도 그대로 살아 있다. 즉 이 문서의 가치는 '풀렸다'가 아니라 '무엇이 안 풀리는지 목록이 바뀌지 않았다'는 데 있다.

### Situated Documentaries — 장소에 서사를 묶다
| 항목 | 내용 |
| --- | --- |
| 주체 | Tobias Höllerer, Steven Feiner, John Pavlik(컬럼비아 저널리즘 스쿨) — Columbia University |
| 연도 | 1999(ISWC'99 발표); Mobile Journalist's Workstation 및 MARS Authoring Tool로 2000년대 초까지 이어짐 |
| 수치 | 피인용 63(Crossref); 제작 다큐멘터리 3편(1968 학생시위, 지하 터널, 캠퍼스 초기사) |
| 출처 | Höllerer T., Feiner S., Pavlik J. (1999) "Situated documentaries: embedding multimedia presentations in the real world", ISWC'99, doi:10.1109/iswc.1999.806664; Columbia MARS 프로젝트 페이지 |

Touring Machine을 이름표 띄우기에서 '현장 기반 다큐멘터리'로 확장했다. 캠퍼스를 걸으면 그 자리에서 실제로 일어난 사건의 사운드·텍스트·이미지·비디오가 공간에 배치되어 재생된다. 실제 제작된 편은 1968년 컬럼비아 학생 시위, 캠퍼스 지하 터널 시스템, 캠퍼스 초기 역사 세 가지였다. 이 중 지하 터널 편은 AR로 '보이지 않는 것'을 보이게 하는 X-ray vision 발상의 초기 사례다. 이후 MARS Authoring Tool을 만들어 프로그래머가 아닌 사람도 3D 하이퍼미디어 서사를 저작할 수 있게 했는데, 이는 '누가 콘텐츠를 만드는가'라는 AR의 지속가능성 문제를 처음 건드린 작업이다.

저널리즘 스쿨이 공동 저자로 들어간 것이 핵심이다. 기술 연구실이 '무엇을 보여줄 것인가'를 스스로 대답할 수 없었고, 장소 기반 서사에 이미 전문성을 가진 분야가 필요했다. 문화유산·도시 해설 분야의 고유 문제는 '설명할 대상은 눈앞에 있는데 설명할 시간과 층위는 눈에 보이지 않는다'는 것이었고, AR은 그 시간 축을 공간에 되돌려 놓는 도구로 채택됐다.

개념적으로 성공, 시스템으로는 소멸. Crossref 피인용 63회. 오늘날 모든 '위치 기반 오디오 투어'와 문화유산 AR 앱의 개념적 원형이지만, 당시 시스템은 배낭 장비를 벗어나지 못해 실제 방문객에게 배포된 적이 없다. 콘텐츠 저작 도구를 만들었다는 점은 선견지명이었으나, 저작 비용 문제는 이후 20년간 문화유산 AR을 계속 죽이는 원인이 된다.

### ARQuake / Tinmith — 야외 AR의 비용과 한계를 숫자로 노출
| 항목 | 내용 |
| --- | --- |
| 주체 | Bruce Thomas, Wayne Piekarski 외 — University of South Australia, Wearable Computer Lab |
| 연도 | 1998~2006(프로젝트 기간); ARQuake 2000(ISWC) → 2002(저널판·CACM); Tinmith-Metro 2001 |
| 수치 | 측량급 DGPS 50cm @10Hz vs 일반 GPS 5m @1Hz; GPS 장비 약 $4,000, 주요 구성품 합계 $10,000 초과; 피인용 — ISWC 2000판 114, Personal and Ubiquitous Computing 2002판 109, CACM 2002판 223, Tinmith-Metro 2001 67(모두 Crossref) |
| 출처 | Thomas B. 외 (2000) ISWC, doi:10.1109/iswc.2000.888480; Thomas B. 외 (2002) Personal and Ubiquitous Computing, doi:10.1007/s007790200007; Piekarski W., Thomas B. (2002) CACM, doi:10.1145/502269.502291; Piekarski W., Thomas B. (2001) Tinmith-Metro, doi:10.1109/iswc.2001.962093; 프로젝트 페이지 https://www.tinmith.net/arquake/ |

1인칭 슈팅게임 Quake를 실제 대학 캠퍼스 위에 겹친 야외 AR 게임이다. 학부 우등생 5명, 지도교수 1명, 박사과정 1명의 소규모 팀이 만들었다. 하드웨어는 반투명 AR 고글, 노트북, Trimble Ag132 GPS 수신기, InterSense IS-300 자기·자이로 방위 센서, 디지털 나침반과 경사계를 커스텀 배낭에 담은 구성이었다. 같은 팀의 Tinmith는 이 플랫폼을 게임에서 '현장 3D 모델링'으로 돌려, 걸어 다니며 건물 형상을 구성하는 Tinmith-Metro(2001)를 내놓았다 — 건축·측량 영역으로의 첫 전용 사례다.

게임은 문화유산이나 건설과 달리 '틀려도 아무도 다치지 않는' 도메인이다. 그래서 야외 AR의 한계를 자유롭게 밀어붙이고 공개적으로 기록할 수 있었다. 실제로 이 프로젝트가 남긴 가장 큰 가치는 게임이 아니라 실패 목록이다. 연구팀은 가상/실제 정렬 불일치, 야외 조명 아래 콘텐츠 가독성 문제, 자기 왜곡에 의한 센서 드리프트, 그리고 야외 보행자가 마우스 쓰는 실내 플레이어보다 느려 게임 균형이 깨진다는 인간공학적 문제까지 명시했다.

연구 성과로는 큰 성공(CACM 2002판 피인용 223회), 제품으로는 애초에 목표가 아니었다. 결정적인 숫자는 비용이다 — 50cm 정밀도를 10Hz로 내는 측량급 차등 GPS 장비 하나에 약 4,000달러, 주요 구성품 합계 10,000달러 초과. 당시 일반 GPS는 5m 정밀도에 1Hz였다. 즉 2000년 시점에서 '건물 모서리에 맞는 야외 AR'은 기술적으로 가능했지만 1인당 1만 달러였고, 이것이 야외 AR이 연구실을 못 벗어난 경제적 이유다.

### ARCHEOGUIDE — 문화유산 AR의 첫 대규모 공공 투자
| 항목 | 내용 |
| --- | --- |
| 주체 | 조정기관 INTRACOM S.A.(그리스). 파트너 6곳 — Fraunhofer IGD(독일), ZGDV(독일), CCG/ZGDV(포르투갈), A&C 2000 S.R.L.(이탈리아), 그리스 문화부, Post Reality S.A.(그리스). 주요 저자 Vlahakis V., Ioannidis M., Karigiannis J., Tsotros M., Gounaris M., Stricker D., Gleue T., Dähne P. |
| 연도 | 2000-01-01 ~ 2002-06-30(EU FP5-IST, 과제번호 IST-1999-11306); 주요 논문 2001~2002; 상시 운영 서비스로의 전환 없음 |
| 수치 | 총사업비 €4,851,991, EU 분담 €2,600,000; 기간 2000-01-01~2002-06-30(30개월); 파트너 7개 기관 4개국; 피인용 — IEEE CG&A 2002판 266, VAST 2001판 163, 기기 설계 논문 77, ISMAR 2002 아키텍처 논문 40(모두 Crossref) |
| 출처 | CORDIS 과제 IST-1999-11306 https://cordis.europa.eu/project/id/IST-1999-11306; Vlahakis V. 외 (2002) IEEE Computer Graphics and Applications, doi:10.1109/mcg.2002.1028726; Vlahakis V. 외 (2001) VAST, doi:10.1145/584993.585015; Gleue T., Dähne P. (2001) doi:10.1145/584993.585018; Dähne P., Karigiannis J. (2002) ISMAR, doi:10.1109/ismar.2002.1115103 |

고대 올림피아 유적을 시험장으로, 방문객이 현장에 서면 폐허 위에 복원된 신전과 고대 경기 장면이 겹쳐 보이게 하는 야외 AR 가이드다. 단일 기기가 아니라 성능·가격이 다른 3단 구성(배낭형 노트북+HMD, 펜 컴퓨터, PDA)을 제공해 '누가 무엇을 볼 수 있는가'를 등급화한 점이 특징이다. 위치는 DGPS와 디지털 나침반으로 대략 잡고, 그 자세를 사전에 촬영해 둔 기준 영상들과 대조하는 영상 기반 보정으로 다듬는 하이브리드 방식을 썼다. 즉 순수 GPS로는 신전 기둥 하나에 정렬할 수 없다는 것을 프로젝트 초기에 인정하고, 유적 전체를 미리 촬영해 '시각적 측량 기준점'을 깔아 두는 쪽을 택했다. 서버-클라이언트 구조로 무거운 렌더링과 데이터베이스를 현장 서버에 두고 무선으로 전송했다.

고고 유적의 고유 문제는 '남아 있는 것이 전체의 극히 일부'라는 점이다. 올림피아에서 관람객이 보는 것은 무너진 기둥 드럼들이고, 그것이 무엇이었는지는 안내판의 작은 복원 삽화로만 전달된다. 동시에 유적은 물리적 복원이 윤리적·법적으로 제한된다(원형 훼손 금지). 물리적으로 복원할 수 없는 것을 시각적으로만 복원한다는 AR의 성질이, 문화유산 보존 원칙과 정확히 맞물렸다. EU가 FP5 '이용자 친화적 정보사회' 프로그램에서 이 조합에 돈을 댄 이유다.

학술적으로는 대성공, 서비스로는 실패. IEEE Computer Graphics and Applications 2002년 논문은 Crossref 피인용 266회로 문화유산 AR의 표준 인용 문헌이 됐고, VAST 2001 논문 163회, 기기 설계 논문 77회, ISMAR 2002 시스템 아키텍처 논문 40회가 뒤따랐다. 그러나 프로젝트가 2002년 6월 종료되자 올림피아에서 상시 서비스로 전환되지 않았다. 실패 원인은 기술과 경제로 나뉜다 — 기술적으로는 유적 전체에 기준 영상을 깔고 계절·시간·날씨에 따라 갱신해야 하는 유지 부담, 그리고 장비 무게·배터리·직사광 아래 HMD 가독성. 경제적으로는 연구비가 끝나면 장비 대여·정비·콘텐츠 갱신 비용을 댈 주체가 없었다는 점이다. 이것이 이후 20년간 문화유산 AR이 반복하는 전형적 소멸 패턴의 원형이다.

### LIFEPLUS / 고대 폼페이 — 유적에 '사람'을 되살리려는 시도
| 항목 | 내용 |
| --- | --- |
| 주체 | George Papagiannakis, Nadia Magnenat-Thalmann — MIRALab, University of Geneva 외 유럽 컨소시엄 |
| 연도 | 2002~2004(EU IST 프로젝트 LIFEPLUS); 주요 논문 2007 |
| 수치 | IJAC 5(2), 2007, 피인용 22(Crossref); EU IST 프로젝트 |
| 출처 | Papagiannakis G., Magnenat-Thalmann N. (2007) "Mobile Augmented Heritage: Enabling Human Life in Ancient Pompeii", International Journal of Architectural Computing 5(2):396-415, doi:10.1260/1478-0771.5.2.396 |

ARCHEOGUIDE가 건물을 복원했다면 LIFEPLUS는 사람을 복원하려 했다. 폼페이의 실제 주택 유적에 옷 시뮬레이션과 피부 렌더링을 갖춘 가상 인물들이 걸어 다니고 대화하는 장면을 실시간으로 겹쳤다. 기술적 초점이 정합에서 '실시간 가상 인물 렌더링'으로 이동한 것이 특징이다 — 즉 야외 정합 문제를 정면으로 풀기보다, 폼페이 주택처럼 벽으로 둘러싸여 상대적으로 통제 가능한 실내·반실내 공간을 골라 정합 난이도를 낮추고 그 대신 콘텐츠 품질을 밀어붙였다. 마커 없는 실시간 카메라 추적과 사전 제작된 인물 애니메이션을 결합했다.

2000년대 초 문화유산 AR 현장의 자각은 '건물 껍데기를 복원해도 관람객의 몰입이 얕다'는 것이었다. 유적 해설의 진짜 공백은 형태가 아니라 생활이었다. 동시에 야외 정합 문제가 풀리지 않자, 연구 전선이 '어디서나 정합'에서 '정합하기 쉬운 곳에서 최고 품질'로 우회했다. LIFEPLUS는 그 우회의 대표 사례다.

제한적 성공 후 소멸. International Journal of Architectural Computing 2007년 논문 기준 피인용 22회로 ARCHEOGUIDE에 크게 못 미친다. 시연 수준을 넘어 상시 서비스가 되지 못한 이유는 명확히 경제적이다 — 고증된 의상·행위·언어를 갖춘 가상 인물 한 장면의 제작비가 유적 한 곳의 연간 해설 예산을 초과했고, 재사용도 불가능했다(폼페이용 인물은 올림피아에서 쓸 수 없다). 콘텐츠 단가가 정합 정확도보다 먼저 프로젝트를 죽인 사례다.

### 모델 기반 야외 추적(Reitmayr–Drummond) — 기술적 돌파와 그 전제
| 항목 | 내용 |
| --- | --- |
| 주체 | Gerhard Reitmayr, Tom Drummond — University of Cambridge |
| 연도 | 2006(ISMAR 2006); 산업 적용은 2010년대 중반 이후 |
| 수치 | ISMAR 2006, 피인용 237(Crossref); 관련 계보 — Behringer 외 2002 피인용 14, Jiang·Neumann·You 2004 하이브리드 추적 피인용 50(Crossref) |
| 출처 | Reitmayr G., Drummond T. (2006) "Going out: robust model-based tracking for outdoor augmented reality", ISMAR 2006, doi:10.1109/ismar.2006.297801 |

GPS와 나침반을 보조로 밀어내고, 카메라가 보는 영상을 미리 준비된 도시의 3D 텍스처 모델과 직접 맞춰 자세를 구하는 방식이다. 건물 외곽선·모서리 같은 기하 특징을 추적하고, 관성 센서로 빠른 움직임을 메우며, 프레임마다 모델과 재정합해 드리프트를 제거한다. 이로써 방위 오차가 시간에 따라 누적되지 않는다. 야외 AR 정합 정밀도를 '건물 단위'에서 '건물 모서리 단위'로 끌어올린 전환점으로 평가된다.

2000년대 중반 건축·도시 분야에는 이미 사진측량과 항공 라이다로 만든 3D 도시 모델이 쌓이기 시작했다. 즉 '미리 만들어진 환경 모델'이라는 전제가 처음으로 현실적이 됐다. 동시에 문화유산·건설 쪽 요구가 '건물이 어디 있는지 알려 달라'에서 '설계한 벽이 실제 벽과 몇 센티 어긋나는지 보여 달라'로 올라가면서, GPS 수준 정밀도로는 쓸모가 없어졌다.

기술적 성공, 그러나 전제가 병목으로 남았다. Crossref 피인용 237회. 이 접근은 오늘날 VPS(시각 측위)의 직계 조상이다. 한계는 분명하다 — 최신 3D 모델이 없으면 작동하지 않고, 공사 중인 현장이나 계절에 따라 형상이 변하는 식생 많은 공간에서는 모델과 실제가 어긋난다. 결국 '정합 문제를 해결한다'가 아니라 '정합 문제를 지도 제작 문제로 옮긴다'가 이 계보의 성격이다.

### 지오브라우저 세대 — Layar와 Wikitude의 부상과 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | Layar — Raimo van der Klein, Claire Boonstra, Maarten Lens-FitzGerald(네덜란드). Wikitude — 오스트리아 잘츠부르크 |
| 연도 | Wikitude World Browser 2008 / Layar 창업 2009-06(암스테르담) → Blippar 인수 2014-06, 암스테르담 사무소 2016 폐쇄 / Wikitude → Qualcomm 인수 2021-09, 2023-09-21 신규 구독 중단, 2024-09-21 서비스 완전 종료 |
| 수치 | Layar 창업 2009-06 암스테르담, 창업자 3인, 2010-09-01 WEF 2011 Technology Pioneer 선정, 2014-06 Blippar 인수(금액 미공개), 2016 사무소 폐쇄; Wikitude 2008 창업, 2012 SDK 전환, 2017 SLAM 도입, 2021-09 Qualcomm 인수, 2023-09-21 신규 구독 중단, 2024-09-21 전 서비스 종료 |
| 출처 | Wikipedia "Layar" https://en.wikipedia.org/wiki/Layar; Wikipedia "Wikitude" https://en.wikipedia.org/wiki/Wikitude |

스마트폰 카메라 화면 위에 주변 정보(부동산 매물, 관광 명소, 지하철역, 도시계획 정보)를 GPS·나침반·가속도계만으로 겹쳐 띄우는 '증강현실 브라우저'다. 누구나 자기 데이터를 '레이어'로 올릴 수 있는 개방형 플랫폼 구조여서, 문화유산 단체나 지자체가 코드를 몰라도 위치 콘텐츠를 발행할 수 있었다. 이것이 야외 AR을 처음으로 배낭에서 주머니로 옮겼다. Wikitude는 2012년 SDK로 전환하고 2017년 SLAM 기반 마커리스 추적을 넣으며 순수 지오브라우저 모델을 스스로 폐기했다.

2008~2009년 iPhone 3GS와 초기 Android가 GPS·디지털 나침반·카메라를 한 몸에 담으면서, ARQuake가 1만 달러로 하던 일의 조악한 버전을 600달러 기기가 하게 됐다. 도시·부동산·관광 분야는 '정보는 데이터베이스에 있고 사용자는 현장에 있다'는 간극을 오래 안고 있었기에, 정확도가 낮아도 즉시 채택했다.

명백한 실패이며, 그 원인 분석이 이 축에서 가장 교훈적이다. 기술적 원인 — 스마트폰 GPS 수평 오차가 도심에서 통상 수 미터에서 수십 미터에 이르고(도시 협곡의 다중경로), 자기 나침반은 철골 구조물과 차량 근처에서 수십 도씩 틀어진다. 결과적으로 겹쳐진 아이콘이 엉뚱한 건물 위에 떠 있었고, 사용자는 '증강'이 아니라 '대충 맞는 목록'을 보게 됐다. 경제적 원인 — 레이어를 만들 유인이 약했다. 정확도가 낮으니 사용자가 안 쓰고, 사용자가 없으니 콘텐츠 제공자가 갱신을 멈추고, 죽은 레이어가 쌓이며 플랫폼 신뢰가 무너졌다. Layar는 2014년 Blippar에 인수된 뒤 사실상 소멸했고(인수가 미공개), Wikitude는 2021년 Qualcomm에 인수된 뒤 2024년 9월 21일 서비스를 완전히 종료했다. 15년간 가장 널리 배포된 야외 AR 플랫폼 두 개가 모두 사라졌다.

### 박물관 AR — 실내로의 전략적 후퇴
| 항목 | 내용 |
| --- | --- |
| 주체 | Cleveland Museum of Art(ARTLENS, 후원 Swagelok Company), 스미스소니언 국립자연사박물관(Skin and Bones, 2015) 등 |
| 연도 | 2010년대 초 본격화; Cleveland Museum of Art ARTLENS 계열 2013년 Gallery One 개관 이후 계속 갱신 |
| 수치 | ARTLENS — iBeacon 240개 이상, 작품 영상 1,500편 이상, iOS 16.4+/Android 15+ 지원, 무료; Gallery One 개관 2013 |
| 출처 | Cleveland Museum of Art ARTLENS App https://www.clevelandart.org/artlens-gallery/artlens-app; 관련 리뷰 문헌은 Crossref 검색 기준 다수이나 인용수가 낮아 개별 지목 생략 |

문화유산 AR의 무게중심이 야외 유적에서 실내 전시장으로 이동했다. 실내에서는 조명이 고정되고, 작품 표면 자체가 자연 특징 마커가 되며, 비콘·Wi-Fi로 실내 측위를 보조할 수 있다. 클리블랜드미술관 ARTLENS 앱은 240개 이상의 iBeacon으로 실내 위치를 잡고, 소장품 전체 검색·길찾기·1,500편 이상의 작품 영상을 제공하며 ARTLENS Wall 등 전시장 설치물과 연동된다. 스미스소니언의 Skin and Bones는 골격 표본에 살과 움직임을 겹쳐 보여주는 방식으로, '표본은 있으나 생태는 보이지 않는다'는 자연사 전시의 고유 공백을 겨냥했다.

야외 정합이 풀리지 않는 동안, 박물관에는 다른 압박이 왔다 — 관람객 체류 시간 감소와 스마트폰으로의 주의 이탈이다. 실내는 정합 난이도가 낮고 유지 주체(박물관)가 분명하며 예산이 연간 편성된다. 즉 ARCHEOGUIDE를 죽인 두 조건(정합 불가, 운영 주체 부재)이 실내에서는 동시에 완화된다. 이것이 문화유산 AR이 실내로 후퇴한 구조적 이유다.

부분적 성공이되 중요한 단서가 붙는다. ARTLENS는 10년 이상 유지·갱신되며 살아남은 드문 사례이고, 그 비결은 AR이 앱의 일부일 뿐이고 길찾기·검색·영상이라는 실용 기능이 본체라는 점이다. 반대로 'AR만 하는' 단발성 전시 앱은 OS 갱신 한두 번에 작동을 멈추고 조용히 스토어에서 내려간다. 기술적 실패가 아니라 소프트웨어 유지보수 예산 구조의 실패다. 또한 이 후퇴는 야외 난제를 해결하지 않고 회피한 것이어서, 유적·정원·도시 같은 야외 문화유산은 계속 공백으로 남았다.

### 건설 현장 AR — BIM 모델을 현장에 1:1로 겹치기
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft, Trimble Inc.(측량·건설 계측 기업) |
| 연도 | HoloLens 1 개발자판 2016-03-30($3,000) / HoloLens 2 발표 2019-02-24(MWC 바르셀로나), 출시 2019-11-07($3,500) / Trimble XR10 동시 발표 2019, 2019년 하반기 출하 / HoloLens 2 단종, 소프트웨어 지원은 2027-12-31까지 |
| 수치 | HoloLens 1 — 2016-03-30 개발자판 $3,000, 시야각 약 30°×17.5°; HoloLens 2 — 발표 2019-02-24, 출시 2019-11-07, $3,500(기업 구독 $125/월, 개발자 $99/월), 시야각 대각 52°, 무게 566g, Snapdragon 850, 지원 종료 2027-12-31; IVAS — 2021-03 최대 $21.88B / 12만 명분, 2022-09 초기 5,000대 인수, 의회 삭감 $230M(FY2020) 및 보류 약 $400M(2022), 2025-02 Anduril 이관; AEC 분야 연구 의제 논문(Delgado 외 2020) 피인용 416(Semantic Scholar) |
| 출처 | Wikipedia "HoloLens 2" https://en.wikipedia.org/wiki/HoloLens_2; Wikipedia "Microsoft HoloLens"; Wikipedia "Integrated Visual Augmentation System"; Trimble Building Construction Field Systems https://www.trimble.com/en/products/building-construction-field-systems; Delgado J.M.D. 외 (2020) Advanced Engineering Informatics, doi:10.1016/j.aei.2020.101122 |

Trimble XR10은 HoloLens 2를 안전모에 통합한 기기다. 건설 현장은 안전모 착용이 법적 의무이므로, 안전모를 벗고 별도 헤드셋을 쓰는 방식은 애초에 불가능했다 — 이 규제 제약을 하드웨어 설계로 흡수한 것이 XR10의 존재 이유다. 작업자는 Trimble Connect로 올린 BIM 모델을 현장 실공간에 1:1 축척으로 겹쳐 보며, 배관·덕트가 들어갈 자리, 슬리브 위치, 시공 오차를 눈으로 확인한다. Trimble은 별도로 태블릿 기반 SiteVision을 두어, GNSS 수신기와 결합하면 야외에서 측량급 정밀도로 모델을 현장에 놓는 경로도 제공한다.

건설의 고유 문제는 '설계는 3D인데 현장은 2D 도면으로 지어진다'는 번역 손실이다. 2010년대에 BIM이 의무화 흐름을 타면서(영국 2016년 공공공사 BIM Level 2 의무화 등) 정밀한 3D 모델이 이미 존재하게 됐고, 그 모델을 현장에서 확인할 마지막 한 걸음만 비어 있었다. 또 하나는 재시공 비용이다. 설비 간섭을 시공 후에 발견하면 철거·재시공이 필요하고, 그 비용이 헤드셋 몇 대 값을 즉시 넘는다. 문화유산과 달리 건설에서는 AR의 투자 회수 계산이 성립한다.

혼합 — 워크플로는 살아남고 기기는 죽었다. HoloLens 2는 시야각을 1세대의 대각 34도에서 52도로 넓히고 무게 566g, $3,500에 출시됐으나 단종됐고 소프트웨어 지원만 2027년 말까지 유지된다. 실패 원인은 건설이 아니라 모기업 쪽 사정이 컸다 — 미 육군 IVAS 계약(2021년 3월, 최대 218.8억 달러, 12만 명분)이 착용자 두통·안구 피로·구토, 수백 미터 밖에서 보이는 발광, 좁은 주변시 문제로 무너졌고, 의회가 2020년 11억 달러 요청 중 2.3억 달러를 삭감, 2022년 약 4억 달러를 보류했다. 2025년 2월 Anduril이 인수·운영을 넘겨받았다. 현장 쪽 기술적 한계도 분명했다 — 광학 시스루 디스플레이는 직사광 아래 대비가 무너지고, 현장의 반복적 회색 벽면과 계속 바뀌는 형상은 SLAM 정합을 흔들며, 배터리 수명이 교대 근무 시간에 못 미친다. 결과적으로 현장 AR의 주류는 헤드셋에서 태블릿·전화기로, 즉 SiteVision류로 이동했다.

### Daqri Smart Helmet — 건설 AR의 가장 비싼 실패
| 항목 | 내용 |
| --- | --- |
| 주체 | Daqri(미국 로스앤젤레스). 공동창업자 Brian Mullins, Gaia Dempsey. 주요 투자 Tarsadia Investments |
| 연도 | 창업 2010 / Smart Helmet 공개 2016(CES) / 사업 종료 발표 2019-09-09 |
| 수치 | 창업 2010; 시리즈 A $15M(2013-06); 누적 조달 $275M(2017-07 기준); Smart Helmet 공개 CES 2016, Intel 6세대 Core m7; 2017 약 25% 감원; 종료 발표 2019-09-09; ARToolKit 인수 2015, 오픈소스 재공개 v5.2 2015-05-13 |
| 출처 | Wikipedia "Daqri" https://en.wikipedia.org/wiki/Daqri; Wikipedia "ARToolKit" https://en.wikipedia.org/wiki/ARToolKit |

안드로이드 기반 산업용 스마트 안전모다. 인텔 6세대 Core m7 프로세서와 다수의 카메라·센서를 안전모에 통합해, 건설·플랜트 작업자에게 설비 정보와 작업 지시를 시야에 겹쳐 보여주는 것을 목표로 했다. Trimble XR10보다 3년 앞서 '안전모 = AR 플랫폼'이라는 같은 통찰에 도달했다. Daqri는 2015년 ARToolKit을 인수해 오픈소스로 재공개(v5.2, 2015-05-13)하며 AR 생태계 전체에 대한 지배력을 노렸다.

2015~2016년은 산업용 AR에 대한 기대가 정점이던 시기다. 건설·중공업의 고유 문제 — 숙련공 고령화, 절차 문서의 현장 접근성 부재, 안전 규정 준수 확인 — 가 모두 '눈앞에 정보를 띄운다'로 해결될 것처럼 보였다. 대형 투자자들이 이 서사에 자금을 쏟았다.

완전한 실패. 2017년 7월 기준 누적 조달액 2억 7,500만 달러(2013년 6월 시리즈 A 1,500만 달러 포함). 2017년 직원 약 4분의 1 감원과 공동창업자 Mullins 퇴진, 두 달 뒤 Dempsey 퇴사. 2019년 9월 9일 자산 매각 및 클라우드·스마트글라스 하드웨어 사업 종료를 이메일로 통보했다. 실패 원인은 기술과 경제 양쪽이다 — 기술적으로 헬멧이 무겁고 열이 나며 배터리가 교대 시간을 못 버텼고, 현장 정합 정밀도가 실제 시공 허용오차(수 밀리미터~수 센티미터)에 못 미쳐 '정보 표시기' 이상이 되지 못했다. 경제적으로는 하드웨어·OS·SDK·콘텐츠를 모두 자체 구축하려다 비용이 폭증했고, 같은 기간 Microsoft가 HoloLens로 플랫폼 층을 장악해 수직통합 전략의 근거가 사라졌다. 2억 7,500만 달러를 태우고 남긴 유산은 ARToolKit의 오픈소스 재공개뿐이다.

### 지하 매설물 X-ray vision — 반복 거론되는 '킬러앱'이 정착하지 못한 이유
| 항목 | 내용 |
| --- | --- |
| 주체 | Vineet Kamat, Amir Behzadan, Sanat Talmaki, Suyang Dong(University of Michigan); Benjamin Avery, Christian Sandor, Bruce Thomas(University of South Australia); Mark Livingston 외(US Naval Research Laboratory); 상용 vGIS/vSite(캐나다) |
| 연도 | 1999(Situated Documentaries의 캠퍼스 터널 편이 사실상 최초) → 2009~2010 Kamat 연구실의 본격 체계화 → 2019~2025 vGIS/vSite 등 상용화 시도 → 현재까지 표준 실무 아님 |
| 수치 | ASCE 38-02 발행 2003, 품질 등급 QL-A/B/C/D 4단계; 피인용 — Avery·Sandor·Thomas(2009) IEEE VR 94, Livingston 외(2009) IEEE VR 66, Talmaki·Dong·Kamat(2010) 59, Behzadan·Kamat(2009) 42(Semantic Scholar)/14(Crossref), Hansen 외(2025) 덴마크 사례 2(Crossref); vSite — 측량급 최대 1cm 표방, 1만 건 이상 유틸리티 프로젝트 |
| 출처 | Avery B., Sandor C., Thomas B. (2009) IEEE VR, doi:10.1109/vr.2009.4811002; Livingston M. 외 (2009) IEEE VR, doi:10.1109/vr.2009.4810999; Behzadan A., Kamat V. (2009) CRC, doi:10.1061/41020(339)123; Hansen L., Wyke S., Bodum L. (2025) Innovative Infrastructure Solutions, doi:10.1007/s41062-025-02372-5; Wikipedia "Subsurface utility engineering"; vSite 제품 페이지 https://www.vgis.io/ |

지면을 투시해 매설된 상수도·가스·전력·통신관을 실제 위치에 겹쳐 보여주는 기능이다. 굴착 전 작업자가 삽을 넣을 자리에 무엇이 있는지 바로 보는 그림은 AR의 가장 직관적인 정당화이며, 그래서 20년 넘게 '킬러앱'으로 지목됐다. 기술적으로는 두 문제가 겹친다. 첫째, 정합 — 지하 3m의 관을 지표 좌표계에 몇 센티 오차로 놓아야 한다. 둘째, 깊이 지각 — 벽 뒤나 땅속에 그린 물체는 사람의 시각계가 자동으로 '표면 위에 떠 있다'고 해석해 버린다. Avery·Sandor·Thomas(2009)와 Livingston 외(2009)가 이 지각 문제를 정면으로 다뤄, 가장자리 보존·격자 마스크·터널 절개 같은 시각 단서를 넣어야 비로소 '뒤에 있다'고 읽힌다는 것을 실험으로 보였다.

굴착 사고는 굴착 산업의 최대 단일 손실 원인이다. 그런데 그 원인은 작업자가 도면을 안 봐서가 아니라, 도면과 현실이 다르기 때문이다. 미국토목학회 ASCE 38-02(2003년 발행)는 지하 매설물 정보를 네 등급으로 나눈다 — QL-D는 기존 기록이나 기억에 의존, QL-C는 지상 노출부를 측량해 기록과 대조, QL-B는 물리탐사로 수평 위치 확인, QL-A는 실제 굴착 노출로 위치·종류·크기·재질·상태 확인. 현장의 압도적 다수는 QL-D 또는 QL-C다. 이 등급 체계의 존재 자체가 '기록은 못 믿는다'는 업계의 공식 자백이다.

기술적으로는 계속 진전, 실무 정착은 실패. 핵심 이유는 냉정하다 — AR은 표시 문제를 풀지 데이터 품질 문제를 풀지 못한다. QL-D 도면을 밀리미터 정밀도로 정합해 보여주면 '정확해 보이는 틀린 그림'이 되고, 이는 종이 도면보다 위험하다. 작업자가 화면을 믿고 삽을 넣으면 책임 소재가 모호해지므로, 어느 유틸리티 사업자도 AR 표시를 굴착 승인 근거로 인정하지 않는다. 즉 장벽은 광학이 아니라 법적 책임과 데이터 등급이다. 상용 제품(vGIS/vSite)은 호환 GNSS·측위 장비와 결합 시 최대 1cm 측량급 정밀도를 표방하며 토론토시·LA수도전력국·AECOM·PCL 등을 고객으로 1만 건 이상의 유틸리티 프로젝트에 쓰였다고 밝히지만, 이는 측위 정밀도이지 매설물 위치 정확도가 아니다. 2025년 덴마크 굴착 손상 방지 사례 연구는 이 간극을 다시 확인했다. 결론적으로 X-ray vision은 '실패한 아이디어'가 아니라 '선행 조건이 충족되지 않은 아이디어'다 — 전제는 AR 기술이 아니라 QL-A/B 수준의 지하 데이터베이스 구축이며, 그것은 도시 단위 공공 투자 문제다.

### 도시계획 참여에서의 AR — 정합 정밀도보다 '누가 보는가'가 중요한 영역
| 항목 | 내용 |
| --- | --- |
| 주체 | Mark Billinghurst 계열의 Holger Regenbrecht 외(University of Otago, 2011); Hesam Imottesjo, Jaan-Henrik Kain(Chalmers, Urban CoBuilder, 2018); Kai Reaver(오슬로, 2023) |
| 연도 | 2011(Allen 외, 스마트폰 기반 공공참여) → 2018(Urban CoBuilder) → 2020~2021 오슬로 워크숍, 2023 논문 발표 |
| 수치 | 오슬로 — 워크숍 5회(각 1주), 2020~2021년 8월, 참여자 약 50~70명, 오슬로 8개 구역, 배치 총 약 8,000건 중 나무 약 5,000건, iPad Pro + ARKit/Unity(Udaru); 피인용 — Reaver(2023) 19, Allen 외(2011) 55, Imottesjo·Kain(2018) 50(모두 Crossref) |
| 출처 | Reaver K. (2023) "Augmented reality as a participation tool for youth in urban planning processes: Case study in Oslo, Norway", Frontiers in Virtual Reality, doi:10.3389/frvir.2023.1055930; Allen M., Regenbrecht H., Abbott M. (2011) OzCHI, doi:10.1145/2071536.2071538; Imottesjo H., Kain J. (2018) Computers, Environment and Urban Systems, doi:10.1016/j.compenvurbsys.2018.05.003 |

도시계획 참여 AR은 주민이 현장에 서서 제안된 건물·가로수·시설물을 실제 스케일로 보고, 나아가 직접 배치해 보는 방식이다. Reaver의 오슬로 사례가 실증 규모가 가장 크다 — 2020년과 2021년 8월에 걸쳐 5차례의 1주일 워크숍을 열고 오슬로 8개 구역에서 약 50~70명의 청소년이 iPad Pro와 ARKit 기반 자체 소프트웨어(Udaru, Unity 제작)로 도시 요소를 배치했다. 총 약 8,000건의 배치 중 약 5,000건이 나무 배치였다. Arnstein의 참여 사다리 framework로 평가했고, 일부 제안은 실제로 오슬로시가 채택했다.

도시계획 참여의 고질적 문제는 '평면도와 조감도를 읽을 수 있는 사람만 의견을 낼 수 있다'는 표상 장벽이다. 이는 기술 문제가 아니라 형평성 문제이며, 특히 청소년·비전문가·비모국어 화자를 체계적으로 배제한다. AR은 표상 해독 능력 없이도 '여기 이렇게 생긴 게 선다'를 즉각 전달한다. 결정적으로, 이 영역은 정합 오차가 수십 센티미터여도 목적을 달성한다 — 나무를 어디쯤 심을지 논의하는 데 밀리미터가 필요하지 않다. 야외 AR의 최대 난제가 이 도메인에서만은 치명적이지 않다는 점이 채택 이유다.

제한적이되 실질적 성공. Reaver(2023) 논문은 Crossref 피인용 19회, Allen 외(2011) 55회, Imottesjo·Kain(2018) 50회다. 참여자 거의 전원이 참여·도시계획·설계에 대한 이해가 늘었다고 보고됐고 일부 제안이 실제 채택됐다. 그러나 한계도 명확히 기록됐다 — 지오로케이션 추적이 부정확해 AR에서 배치한 좌표를 GIS로 직접 옮길 수 없었고, 워크숍 후 수작업 재배치가 필요했다. 즉 '의견 수렴 도구'로는 작동했지만 '설계 데이터 입력 도구'로는 작동하지 않았다. 또 하나의 한계는 내용 쪽이다 — 청소년 참여자는 수종·토양·장기 환경 영향에 대한 지식이 없어 전문가 검증이 반드시 필요했다.

### VPS 시대 — 야외 정합을 기기에서 지도 인프라로 옮기다
| 항목 | 내용 |
| --- | --- |
| 주체 | Google(ARCore, Street View), Niantic / Niantic Spatial Inc. |
| 연도 | Pokémon Go 2016-07-06 / Niantic Lightship SDK 공개 2021-11 / Google ARCore Geospatial API 2022 / Niantic 게임 부문 매각 2025-03-12 확정, 2025-05-29 완료, 지리공간 부문 Niantic Spatial로 분사 |
| 수치 | Pokémon Go — 출시 2016-07-06, 5억 다운로드(2016-09), 10억 돌파(2019 초), 누적 매출 $6.46B(2020년까지); Niantic — Lightship SDK 2021-11 공개, Coatue $300M 투자 시 기업가치 $9B, Scopely 매각 $3.5B(2025-03-12 확정, 2025-05-29 완료), Niantic Spatial 분사; ARCore Geospatial API — 스트리트뷰 15년 이상 영상 기반, 스트리트뷰 커버리지 지역 전역 |
| 출처 | Google ARCore Geospatial 개발자 문서 https://developers.google.com/ar/develop/geospatial; Wikipedia "Niantic, Inc."; Wikipedia "Pokémon Go" |

시각 측위 시스템(VPS)은 기기가 보는 영상을 클라우드에 축적된 전역 시각 지도와 대조해 위치와 방향을 구한다. Google의 ARCore Geospatial API는 15년 이상 축적된 스트리트뷰 영상에 심층신경망을 적용해, 오랜 기간 변하지 않을 특징들만 골라 기술한 뒤 수십억 장에서 전역 3D 점군을 만든다. 사용자의 카메라 픽셀에서 같은 종류의 특징을 뽑아 이 모델과 대조해 GPS보다 훨씬 정밀한 자세를 낸다. 스트리트뷰가 있는 거의 모든 국가에서 작동하며, WGS84·지형·옥상 세 종류의 앵커를 제공한다. 이는 Reitmayr–Drummond(2006)의 모델 기반 추적을, 연구실 한 블록이 아니라 지구 규모로 산업화한 것이다.

2020년대 들어 문화유산·건축·도시 AR의 모든 시도가 같은 벽에 반복해 부딪혔음이 명확해졌다 — 개별 프로젝트가 자기 현장의 정합 기준(ARCHEOGUIDE의 기준 영상, Reitmayr의 3D 모델)을 매번 새로 만들어야 했고, 그 비용이 프로젝트를 죽였다. 정합을 각 앱의 문제에서 공용 인프라로 끌어올리는 것만이 구조적 해법이었다. Google은 스트리트뷰라는 이미 지불된 자산을 갖고 있었기에 이 전환을 할 수 있었다.

진행 중이며 판정 유보. 기술적으로는 야외 AR 30년 난제의 가장 유력한 해법이다. 그러나 세 가지가 남는다. 첫째, 커버리지 — 스트리트뷰 차량이 다니지 않는 곳, 즉 유적 내부·공원 보행로·건설 현장 안쪽은 비어 있다. 둘째, 변화 — 계절에 따라 형상이 바뀌는 식생 많은 공간과 공사 중 현장은 시각 지도와 어긋난다. 셋째, 종속 — 문화유산 기관이나 지자체가 정합을 특정 민간 플랫폼에 의존하게 된다. Niantic의 궤적이 시사적이다. Pokémon Go는 2016년 7월 출시 후 2016년 9월까지 5억 다운로드, 2019년 초 10억 돌파, 2020년까지 누적 매출 64억 6천만 달러를 올렸지만, 정작 AR 모드는 선택 기능이고 많은 플레이어가 꺼 놓는다 — 대중적 성공은 AR 때문이 아니었다. Niantic은 2021년 Coatue에서 3억 달러를 유치하며 90억 달러 가치를 인정받았으나, 2025년 게임 부문을 Scopely에 35억 달러에 매각하고 지리공간 사업만 Niantic Spatial로 분사했다. '현실 세계 메타버스'라는 서사는 접혔고, 남은 것은 지도 자산이다.

### 야외·대규모 환경 공통 난제의 기술적 정리
| 항목 | 내용 |
| --- | --- |
| 주체 | 해당 없음 — 이 축 전체의 횡단 정리 |
| 연도 | 1997(문제 등장) ~ 현재(부분 해결) |
| 수치 | 일반 GPS 5m@1Hz vs 측량급 DGPS 0.5m@10Hz(2000년, 장비 약 $4,000); 방위 1도 오차 → 100m 거리에서 약 1.7m 편차; HoloLens 시야각 34°(1세대 대각)→52°(2세대 대각); ASCE 38 지하 데이터 4등급 |
| 출처 | Azuma R. (1999) doi:10.1007/978-3-642-87512-0_21; Reitmayr G., Drummond T. (2006) doi:10.1109/ismar.2006.297801; Livingston M. 외 (2009) doi:10.1109/vr.2009.4810999; Avery B. 외 (2009) doi:10.1109/vr.2009.4811002; 각 항목별 출처는 위 항목들 참조 |

야외 문화유산·건축·도시 AR이 30년간 반복해 부딪힌 제약을 여섯 층으로 나눌 수 있다. (1) 위치 정합 — GPS 단독으로는 부족하다. 일반 GPS는 5m·1Hz 수준이고 도심 협곡에서는 다중경로로 더 나빠진다. 측량급 RTK는 센티미터를 내지만 2000년 기준 장비만 4,000달러였다. (2) 자세 정합 — 자기 나침반은 철골·차량·전력선 근처에서 수십 도 틀어지고, 자이로는 드리프트가 누적된다. 위치가 1cm여도 방위가 1도 틀리면 100m 앞 대상은 1.7m 어긋난다. 이것이 야외 AR에서 자세가 위치보다 치명적인 이유다. (3) 지각 — 사람의 시각계는 겹쳐 그려진 물체를 자동으로 '표면 앞'으로 해석하므로, 지하 매설물이나 벽 뒤 구조는 별도의 폐색 단서 없이는 '뒤에 있다'로 읽히지 않는다. (4) 광학 — 광학 시스루 디스플레이는 직사광 아래 대비가 무너진다. 가상 영상은 실제 빛에 더해질 뿐 뺄 수 없어, 밝은 배경 위에 어두운 물체를 그릴 수 없다. 이는 소프트웨어로 해결 불가능한 물리적 제약이다. (5) 사전 지식 — 정합을 잘 하려면 미리 만든 3D 모델이나 기준 영상이 필요한데, 그 제작·갱신 비용이 개별 프로젝트 예산을 넘는다. (6) 운영 — 콘텐츠 제작 단가, OS 갱신에 따른 앱 수명, 장비 대여·충전·정비 인력. 앞의 네 개는 기술 문제이고, 뒤의 두 개는 경제 문제다. 그리고 이 축의 사례들을 죽인 것은 대부분 뒤의 두 개였다.

이 목록이 중요한 이유는 각 시대가 '이번에는 다르다'고 주장했으나 실제로 바뀐 항목이 하나씩뿐이었기 때문이다. 스마트폰은 (6)의 장비 비용만 낮췄고 (1)(2)를 오히려 악화시켰다. HoloLens는 (2)를 SLAM으로 크게 개선했으나 (4)를 전혀 못 건드렸다. VPS는 (1)(2)(5)를 한꺼번에 공략한 최초의 접근이며, 그래서 이번에는 실제로 다를 가능성이 있다. 다만 (4)와 (6)은 여전히 열려 있다.

부분 해결. 2025년 기준 (1)(2)(5)는 VPS와 SLAM으로 도심에서 실용 수준에 도달했고, (3)은 20년의 지각 연구로 설계 가이드라인이 확립됐다. (4)는 광학의 근본 제약으로 남아 있으며, 밝은 야외에서의 해법은 광학 시스루를 포기하고 비디오 시스루(카메라 영상에 합성) 또는 태블릿으로 가는 것이다 — 실제 산업 현장 AR이 헤드셋에서 태블릿으로 회귀한 이유가 이것이다. (6)은 전혀 해결되지 않았고, 오히려 이 축 사례들의 사망 원인 1위다.

#### 검증에서 잡힌 정정
- [확정 오류] Touring Machine의 NSF 과제번호가 틀렸다. 조사는 'ONR 계약 N00014-97-1-0838, NSF CDA-92-23009'라고 적었으나, ISWC'97 논문(http://www.cs.columbia.edu/graphics/publications.newer/iswc97.pdf) 원문 PDF 6절 Acknowledgments를 추출한 결과 실제 문구는 다음과 같다: "This work was supported in part by the Office of Naval Research under Contracts N00014-94-1-0564 and N00014-97-1-0838, the Columbia Center for Telecommunications Research under NSF Grant ECD-88-11111, a Columbia University Provost's Strategic Initiative Fund Award, and a gift
- [확정 오류] 오슬로 사례의 8,000건/5,000건 수치를 잘못 읽었다. 조사는 '배치 총 약 8,000건 중 나무 약 5,000건'이라고 적어 나무가 아닌 배치가 약 3,000건 있었던 것처럼 서술했다. Reaver(2023, Frontiers in Virtual Reality) 원문은 'approximately 8,000 trees were placed by AR during the workshops'이며, 중복 제안을 통합하면 'approximately 5,000 original tree placements'가 된다고 밝힌다. 즉 8,000과 5,000은 둘 다 나무 수치이며 각각 '원시 배치수'와 '중복 제거 후 고유 배치수'다. '8,000건 중 5,000건이 나무'라는 구성은 원문에 없는 비(非)수목 배치 약 3,000건을 만들어낸다.
- [확정 오류] 오슬로 참여자 수 '약 50~70명'은 출처에 없는 수치다. Reaver(2023)는 워크숍당 9~18명의 청소년 그룹 5개라고만 밝히므로 산술 범위는 약 45~90명이다. 논문은 총 참여자 수를 단일 수치나 '50~70' 범위로 제시하지 않는다. 범위 자체를 좁혀 인용한 것으로, 출처 미지지 수치다.
- [확정 오류] IVAS 의회 삭감액 $230M의 회계연도 표기가 틀렸다. 조사는 '의회 삭감 $230M(FY2020)'이라 적었으나, 이 삭감은 2020년 12월 통과된 세출법에서 육군의 **FY2021** IVAS 요구액 약 $1.1B을 $230M 줄인 것이다. 삭감이 이루어진 시점(2020년 12월)과 대상 회계연도(FY2021)를 혼동한 표기다. 같은 항목의 '보류 약 $400M(2022)'는 2022년 3월로 정확하다.
- [부정확한 귀속] LIFEPLUS의 주관기관 표기가 사실과 다르다. 조사는 'George Papagiannakis, Nadia Magnenat-Thalmann — MIRALab, University of Geneva 외 유럽 컨소시엄'으로 적어 MIRALab을 주도 기관처럼 제시했으나, CORDIS(과제 IST-2001-34545)상 LIFEPLUS의 조정기관(coordinator)은 그리스 FORTH(Foundation for Research and Technology Hellas)이고 참여기관은 10곳이다. MIRALab은 참여 파트너이자 인용 논문의 저자 소속일 뿐이다. 아울러 조사가 '2002~2004'로 적은 기간의 정확한 값은 2002-03-01~2004-10-31이며, 조사가 언급하지 않은 사업비는 총 €3,250,140 / EU 분담 €1,452,000이다(ARCHEOGUIDE를 '문화유산 AR의 첫 대규모 공공 투자'로 부르는 서사 자체는 금액·시기상 유지된다).
- [서사-데이터 불일치, 경미] 축 서사가 지오브라우저 세대를 '2008~2014년'으로 묶고 '인수·소멸했다'고 맺지만, 조사 자신의 항목 데이터가 Wikitude의 서비스 완전 종료를 2024-09-21로 적고 있다. 2014년은 Layar의 Blippar 피인수 시점일 뿐이며, Wikitude는 그 뒤 10년을 더 운영(2017 SLAM 도입, 2021 Qualcomm 피인수)했다. 연도 구간 표기가 자기 데이터와 어긋난다.
- [검증 한계 — 오류 아님, 주의] 조사가 근거로 삼은 피인용수는 전부 Crossref 기준인데, Crossref는 2000년 이전 문헌의 인용을 심하게 과소집계한다. 예컨대 Touring Machine의 Personal Technologies 판은 Crossref 304회지만 OpenAlex 기준 951회다. 조사가 출처를 'Crossref'로 명시한 점은 정직하나, '피인용 248/304로 야외 AR 가이드의 조상이 됐다'는 식으로 영향력을 논증할 때 실제 영향력을 약 3배 과소평가하게 된다. 수치 자체는 정확하므로 오류로 계상하지는 않는다.
- [미검증 — 오류 아님, 확인 실패] Trimble XR10의 '2019 동시 발표, 2019년 하반기 출하'는 1차 출처로 확인하지 못했다. 조사가 인용한 Trimble 제품 페이지(trimble.com/en/products/building-construction-field-systems)에는 현재 XR10 언급이 전혀 없고, 과거 XR10 전용 URL은 이 일반 페이지로 301 리다이렉트된다(제품 단종 정황과는 부합). 반증은 없으나 근거도 확인되지 않았으므로 별도 출처 보강이 필요하다.
- NSF 과제번호 오류: Touring Machine ISWC'97 논문의 감사문은 ONR 계약 N00014-94-1-0564와 N00014-97-1-0838, 그리고 NSF Grant ECD-88-11111(Columbia Center for Telecommunications Research), Provost's Strategic Initiative Fund, Microsoft 기부를 명시한다. 축이 적은 'NSF CDA-92-23009'는 이 논문에 등장하지 않으며, ONR 계약도 2건 중 1건만 적었다.
- Azuma 1999의 제약 개수 오류: 원문은 'This section analyzes these three problem areas'라고 명시하고 §3.1 크기·무게·전력, §3.2 디스플레이, §3.3 추적 세 가지만 다룬다. 축이 말한 '다섯 제약'(정합 오차·센서 드리프트·햇빛 대비·전력·통제불가 환경)은 Azuma가 제시한 목록이 아니며, 횡단 정리의 '(1)(2)(5) 해결 / (4) 미해결' 채점은 존재하지 않는 번호 체계를 근거로 삼는다.
- GPS 수치의 출처 오귀속: 횡단 정리는 '일반 GPS 5m@1Hz'의 근거로 Azuma 1999를 인용하지만, Azuma 1999 원문은 일반 GPS 약 30m, 차등 GPS 약 3m라고 적는다. 5m@1Hz/$200과 50cm@10Hz/$4,000은 tinmith.net ARQuake FAQ의 수치다.
- 오슬로 나무 수치 오독: Reaver(2023) 원문은 워크숍 중 AR로 약 8,000그루의 '나무'가 배치됐고, 중복·겹침을 통합하면 약 5,000건의 고유 나무 배치로 추정된다고 적는다. 즉 5,000은 8,000에서 중복을 제거한 부분집합이다. 축의 '배치 총 약 8,000건 중 나무 약 5,000건'은 8,000을 나무 아닌 것을 포함한 총계로 잘못 읽었다.
- 오슬로 참여자 수 미근거: 원문은 5개 그룹, 각 그룹 9~18명이라고만 적어 총 45~90명 범위가 나온다. 축의 '약 50~70명'은 논문이 뒷받침하지 않는 좁힌 수치다.
- 오슬로 워크숍 시점 압축: 원문은 '다섯 개의 개별 워크숍, 각 1주일, 2020년 8월'에 수행한 뒤 2021년에 이어졌다고 적는다. 축의 '워크숍 5회(각 1주), 2020~2021년 8월'은 2020년 8월에 집중된 5회와 이후 속행을 뭉뚱그렸다.
- IVAS 의회 삭감의 회계연도 오류: $1.1B 요구액에서 $230M을 삭감한 결정은 2020년 12월에 이뤄져 FY2021 예산 건이다. 축은 이를 'FY2020'으로 표기했다.
- LIFEPLUS 논문 면수 오류: Crossref 기준 International Journal of Architectural Computing 5(2)의 해당 논문은 395-415쪽이다. 축은 396-415로 적었다.
- HoloLens 1 시야각의 지위 오류: '약 30°×17.5°'는 Microsoft 공식 사양이 아니라 시연 기기를 본 참관자 1인의 추정치로 기록된 값이다. 축은 이를 하드웨어 제원처럼 제시했다.
- ARCHEOGUIDE 파트너 수 자체모순: 같은 항목 안에서 '파트너 6곳'과 '파트너 7개 기관'을 함께 적었다(조정기관 INTRACOM + 파트너 6곳 = 7개 기관으로 해석해야 일관됨).
- Daqri 인수 대상 표기 오류: Daqri가 2015년 5월 인수한 것은 오픈소스 라이브러리 'ARToolKit'이 아니라 이를 상용 배포하던 회사 ARToolworks다.
- ARToolKit 연대 착오에 기반한 서사: 축은 1997년 Touring Machine이 'AR이 실내 마커를 떠난' 사건이라고 하지만, 마커 AR의 정본 ARToolKit은 Hirokazu Kato가 1999년에 개발했다. 1997년에는 떠날 마커 패러다임이 아직 없었다.
- Azuma의 '야외 난제 정식화' 시점 오류: Azuma 본인의 논문 목록에 따르면 최초 정식화는 1998년 11월 1일 First Int'l Workshop on Augmented Reality 발표 'Making Augmented Reality Work Outdoors Requires Hybrid Tracking'(pp.219-224)이다. 1999년 章은 ISMR'99 초청강연에 딸린 확장판이다.
- Trimble의 건설 AR 시점 오류: Trimble SketchUp Viewer는 HoloLens 1(2016)에서 '최초의 상용 HoloLens 애플리케이션'이었다. 축의 '2019년 Trimble XR10+HoloLens 2가 BIM 모델을 현장에 1:1로 겹쳤다'는 서술은 3년 앞선 선행 상용화를 누락한다.
- Daqri 성격 규정 오류: '건설 AR의 가장 비싼 실패'라 했으나 Daqri는 2011년 QR 기반 AR 퍼블리싱 플랫폼으로 출발했고 2014년에야 하드웨어에 진입했으며, 2017년 말 스마트헬멧을 주력에서 제외하고 스마트글라스로 선회했다. 누적 $275M은 Melon(EEG 헤드밴드)·Two Trees Photonics·1066 Labs·ARToolworks 인수를 포함한 전사 조달액으로, 건설용 헬멧에 투입된 금액이 아니다.
- Wikitude 사인(死因) 오류: Wikitude는 2012년 SDK 전환으로 지오브라우징을 떠났고 2017년 SLAM을 도입했으며 2021년 Qualcomm에 인수됐다. 2024년 서비스 종료는 지오브라우저 중단 12년 뒤의 인수 후 제품 정리로, 'GPS·나침반 오차 탓에 떠다니는 아이콘에 머물러 소멸'이라는 인과는 Layar에는 몰라도 Wikitude에는 성립하지 않는다.
- Regenbrecht 계보 허위: 'Mark Billinghurst 계열의 Holger Regenbrecht'라고 했으나 Billinghurst는 Allen·Regenbrecht·Abbott(2011) 저자가 아니며(Crossref 저자 3인), Regenbrecht는 University of Otago 소속으로 Billinghurst의 HIT Lab NZ 계보로 분류할 근거가 제시되지 않았다.
- vSite 업체 주장 무검증 인용: '측량급 최대 1cm', '1만 건 이상 유틸리티 프로젝트'는 vgis.io 제품 페이지의 자사 주장이며 독립 검증 출처가 붙어 있지 않다. 축은 이를 수치 항목에 그대로 실었다.
- ASCE 38 판본 미갱신: ASCE 38-02(2003년 발행)는 2022년 ASCE 38-22로 개정되어 대체됐다. 축은 현행 규범처럼 38-02만 제시한다.
- 피인용 데이터베이스 혼용: Delgado 외(2020)를 'Semantic Scholar 416'으로만 적었으나 Crossref는 370이다. 축은 다른 항목에서는 'Semantic Scholar/Crossref' 병기를 하면서 이 항목만 단일 출처를 써서 비교 불가능한 수치를 같은 표에 섞었다.
- ARQuake 비용 수치의 연도 귀속: $4,000/$10,000 수치는 ISWC 2000 논문이 아니라 1998~2006년을 포괄하며 '2006년 최신 시스템'을 함께 안내하는 tinmith.net 프로젝트 FAQ 페이지에서 나온다. 축은 이를 '2000년'의 경제성 논증으로 제시한다.
- ARCHEOGUIDE '현장에서 사라졌다'의 근거 부재: CORDIS 기록은 30개월 고정 기간의 FP5 과제가 정상 종료된 사실만 보여준다. 기한 만료는 기술적 실패의 증거가 아니며, 축은 2002년 이후 올림피아 현장에 관한 출처를 제시하지 않았다.
- (외 16건)

\newpage

# 기반 — 시지각·수학·센서·지연·AI·플랫폼·인간요인

## vision
항목 16개 · 검증 정정 지적 60건


### 망막 광수용체의 불균등 분포 — 1억 개 센서, 100만 가닥 출력
| 항목 | 내용 |
| --- | --- |
| 수치 | 원뿔세포 약 460만 개(개인별 범위 약 440만~530만), 간상세포 약 9200만 개(범위 약 7800만~1억 700만). 중심와 피크 원뿔 밀도 약 199,000개/mm²(개인 간 변이 약 100,000~324,000개/mm²). 간상세포 피크는 중심에서 약 18~20도(망막상 4.5mm) 고리에서 약 150,000~160,000개/mm². 간상세포가 전혀 없는 영역(rod-free zone) 직경 약 0.35mm. 시신경 축삭 약 100만~120만 가닥. 맹점(시신경유두)은 코 쪽 약 15도, 크기 약 5도×7도. 중심와 원뿔 안절 직경 약 1.5마이크로미터, 주변부 원뿔 약 6마이크로미터, 간상 약 2마이크로미터. |
| 출처 | Curcio CA, Sloan KR, Kalina RE, Hendrickson AE (1990) "Human photoreceptor topography", Journal of Comparative Neurology 292(4):497–523 (1차 출처, 실측 8안). 원조 계수는 Østerberg G (1935) Acta Ophthalmologica Suppl. 6. 세포 치수·시냅스 수는 Kolb H, "Photoreceptors", Webvision (webvision.pitt.edu, University of Pittsburgh). |

사람의 눈은 카메라처럼 균일한 센서를 갖고 있지 않다. 빛을 받는 세포는 두 종류로, 밝은 곳에서 색을 보는 원뿔세포와 어두운 곳에서 명암만 보는 간상세포다. 원뿔세포는 망막 중앙의 아주 좁은 구덩이에 극단적으로 몰려 있고, 간상세포는 그 중앙을 완전히 비운 채 주변에 고리 모양으로 퍼져 있다. 이렇게 배치된 이유는 물리적 병목 때문이다. 망막에는 약 1억 개의 광수용체가 있지만, 눈에서 뇌로 나가는 시신경 축삭은 약 100만 가닥뿐이다. 평균 100대 1로 압축해야 하는데, 눈은 이 압축률을 균일하게 나누지 않고 중앙에만 몰아주는 쪽을 택했다. 중심와에서는 원뿔세포 하나가 자기 전용 신경절세포 두 개(밝아짐 담당·어두워짐 담당)를 갖지만, 주변부에서는 수백 개의 간상세포가 신경절세포 하나를 공유한다. 그 대가로 중앙은 해상도를, 주변은 감도와 움직임 검출을 얻는다. 즉 눈은 '전체를 적당히'가 아니라 '한 점만 극단적으로, 나머지는 포기'라는 설계를 선택했다.

### 중심와의 크기 — 고해상도가 필요한 영역은 시야의 0.1%
| 항목 | 내용 |
| --- | --- |
| 수치 | 중심오목(foveola) 직경 0.35mm ≈ 시야 약 1도. 중심와(fovea) 직경 1.5mm ≈ 약 5도. 방중심와(parafovea) 외경 2.5mm ≈ 약 8도. 망막 환산 배율: 눈의 후절점 기준 시야 1도 ≈ 망막 약 288~291마이크로미터. 시선 이동 빈도 초당 2~3회(즉 고정 지속 시간 평균 200~330밀리초). 양안 시야 약 200도×135도 중 중심 5도 원의 입체각 비중 약 0.1%. |
| 출처 | Wandell BA, "Foundations of Vision" (Sinauer, 1995), 5장 '눈의 광학과 망막 표본화'. 각도-망막 환산은 Drasdo N & Fowler CW (1974) British Journal of Ophthalmology 58:709–714. 중심와 구역 정의는 Polyak SL, "The Retina" (1941) 이래의 표준 구분. |

중심와는 생각보다 훨씬 작다. 가장 해상도가 높은 중심오목(foveola)은 망막에서 지름 0.35밀리미터, 각도로는 약 1도에 불과하다. 팔을 뻗었을 때 엄지손톱이 가리는 각도가 약 1.5~2도이니, 우리가 '선명하게 본다'고 느끼는 영역은 팔 끝 엄지손톱보다도 작다. 그런데 주관적으로는 시야 전체가 선명해 보인다. 이것은 착각이며, 뇌가 초당 두세 번 시선을 옮겨 필요한 곳마다 중심와를 갖다 대고, 그 결과를 하나의 안정된 장면으로 합성하기 때문에 생기는 인상이다. 즉 우리가 보는 '선명한 세계'는 한 번에 찍힌 사진이 아니라 시간에 걸친 표본들의 재구성이다. 이 사실이 중요한 이유는, 렌더링 자원을 어디에 써야 하는지를 면적 기준이 아니라 시선 위치 기준으로 판단해야 한다는 뜻이기 때문이다. 양안 시야 200도×135도 안에서 중심 5도 원의 면적 비중은 0.1% 수준이다.

### 이심률 의존 시력 — 2도에서 절반, 30도에서 16분의 1
| 항목 | 내용 |
| --- | --- |
| 수치 | 중심와 최소분해각 약 0.5~1.0 분각(시력 1.0 = 1분각, 시력 2.0 = 0.5분각). 이심률별 시력 비율: 2도에서 중심의 약 1/2, 4도에서 1/3, 6도에서 1/4, 30도에서 1/16이며 30도를 넘으면 더 가파르게 하락. 시력의 E2 ≈ 2.5도(연구에 따라 1.5~3도). 피질 확대율: 중심와 부근 V1에서 시야 1도당 약 15~20mm, 20도 이심률에서는 1mm/도 미만. 중심 2도 시야가 V1 표면적의 약 8~10%를 차지. |
| 출처 | Levi DM, Klein SA, Aitsebaomo AP (1985) "Vernier acuity, crowding and cortical magnification", Vision Research 25:963–977 (E2 모델의 1차 출처). 피질 확대율은 Horton JC & Hoyt WF (1991) Archives of Ophthalmology 109:816–824. 이심률별 시력 비율 요약은 Strasburger H, Rentschler I, Jüttner M (2011) "Peripheral vision and pattern recognition: a review", Journal of Vision 11(5):13. |

시력은 중심에서 벗어날수록 떨어지는데, 그 떨어지는 방식에 단순한 규칙이 있다. 분해할 수 있는 최소 각도(MAR)는 이심률에 대해 거의 직선으로 커진다. 수식으로는 MAR = M0 × (1 + E/E2)이고, 여기서 E는 중심에서 떨어진 각도, E2는 '중심 값의 두 배가 되는 이심률'이다. 시력의 경우 E2가 약 2.5도이므로, 2.5도만 벗어나도 최소분해각이 두 배가 된다. 왜 이런 형태인가 하면, 망막의 광수용체 간격과 신경절세포 간격이 이심률에 대해 대략 선형으로 벌어지기 때문이고, 더 근본적으로는 대뇌 시각피질에서 시야 1도에 배정되는 피질 면적(피질 확대율)이 이심률에 반비례해 줄기 때문이다. 다시 말해 시력 저하는 눈의 광학 흐림이 아니라 표본 간격과 뇌 자원 배분의 문제다. 실제로 주변시에 흐린 이미지를 넣어도 사용자는 잘 모르지만, 그 이유는 '흐려서'가 아니라 '애초에 그 정도밖에 표본화되지 않아서'다.

### 시야각의 실제 크기 — 단안 100도, 양안 200도
| 항목 | 내용 |
| --- | --- |
| 수치 | 단안 시야(고정점 기준): 코 쪽 약 60도, 위 약 60도, 아래 약 70~75도, 귀 쪽 약 100~110도. 양안 합산 수평 약 200~220도, 수직 약 130~135도. 양안 중첩(입체시 가능) 영역 약 114~120도. 근주변시/중간주변시 경계 약 30도, 원주변시 약 60도 이상. 참고 기기값: Meta Quest 3 수평 약 110도, Apple Vision Pro 수평 약 100~110도, Varjo XR-4 수평 약 120도(제조사 공표치, 측정 조건 상이). |
| 출처 | 시야 각도는 Spector RH, "Visual Fields", in Walker HK et al., "Clinical Methods: The History, Physical, and Laboratory Examinations" 3rd ed. (Butterworths, 1990), 116장. 주변시 구역 정의와 기능은 Strasburger H et al. (2011) Journal of Vision 11(5):13. 기기 수치는 제조사 공표 사양(측정 방법 비표준). |

사람의 시야는 좌우 비대칭이다. 코가 가로막기 때문에 한쪽 눈은 코 쪽으로 약 60도밖에 못 보지만 귀 쪽으로는 100도가 넘게 본다. 위쪽은 눈썹과 눈두덩이 가려 약 60도, 아래쪽은 뺨 각도 덕에 70~75도로 더 넓다. 두 눈을 합치면 수평 200~220도가 되는데, 이 중 가운데 약 114~120도만 두 눈이 겹쳐 입체시가 가능하고, 양 끝 각 40도쯤은 한쪽 눈만 보는 단안 영역이다. 이 바깥 영역은 해상도가 거의 없다시피 하지만 결코 쓸모없지 않다. 주변시는 움직임 검출, 자세 균형, 공간에 대한 '거기 있음'의 감각을 담당한다. 시야가 좁아지면 시력이 멀쩡해도 균형이 흔들리고 공간이 작게 느껴진다. 현행 증강현실·가상현실 기기는 수평 100~120도 수준으로, 자연 시야의 절반가량만 덮는다.

### 각해상도의 한계 — 도당 60화소와 회절의 우연한 일치
| 항목 | 내용 |
| --- | --- |
| 수치 | 시력 1.0 = 최소분해각 1분각 = 도당 30주기 → 필요 화소밀도 60 PPD. 최고 시력자(2.0) 기준 0.5분각 → 120 PPD. 중심와 원뿔 간격 약 2.0~2.5마이크로미터 ≈ 0.4~0.5분각. 회절 한계 θ = 1.22λ/D: λ=550nm, 동공 D=3mm일 때 2.24×10⁻⁴ rad = 46초각 ≈ 0.77분각. 전 시야(200도×135도)를 60 PPD로 채우면 한쪽 눈에 12,000×8,100 ≈ 9,720만 화소. 참고 기기값: Quest 3 약 25 PPD, Apple Vision Pro 중심 약 34 PPD, Varjo XR-4 중심 약 51 PPD(제조사·리뷰 측정치). |
| 출처 | 표본화와 원뿔 간격은 Williams DR (1985) "Aliasing in human foveal vision", Vision Research 25:195–205 (1차 출처). 회절 한계와 눈의 광학은 Charman WN, "Optics of the Eye", in Bass M (ed.) "Handbook of Optics" 3rd ed., Vol. III, 1장. 시력-주파수 환산은 Wandell, "Foundations of Vision" (1995), 5장. |

시력 1.0이라는 임상 기준은 1분각(1/60도) 떨어진 두 점을 구분한다는 뜻이다. 격자무늬로 바꾸면 도당 30주기를 분해한다는 말이고, 표본화 정리에 따라 이를 표시하려면 한 주기에 최소 두 화소, 즉 도당 60화소(60 PPD)가 필요하다. 흥미로운 것은 이 값이 세 가지 독립된 물리량과 거의 일치한다는 점이다. 첫째, 중심와 원뿔세포의 간격이 약 0.5분각으로 도당 120개, 즉 나이퀴스트 한계가 정확히 도당 60주기다. 둘째, 동공 3밀리미터에서 빛의 회절 한계는 약 0.77분각으로 원뿔 간격과 같은 크기다. 셋째, 대비 민감도 함수의 고주파 차단이 약 50~60주기/도다. 진화가 광학 한계에 맞춰 센서 간격을 정한 결과, 눈은 렌즈 성능을 낭비하지도 부족하게 쓰지도 않는 지점에 놓여 있다. 증강현실 디스플레이가 도당 60화소를 목표로 삼는 이유가 이것이다. 그 이상은 원리적으로 보이지 않는다.

### 대비 민감도 함수 — 눈은 밴드패스 필터다
| 항목 | 내용 |
| --- | --- |
| 수치 | 피크 공간주파수 2~5 주기/도, 피크 감도 100~500(역치 대비 0.2~1%). 고주파 차단 약 50~60 주기/도(고휘도·고대비 조건). 저주파 쪽은 0.5 주기/도 이하에서 감도 저하. Michelson 대비 = (Lmax−Lmin)/(Lmax+Lmin). 주변시에서는 차단 주파수가 이심률에 대략 반비례해 낮아짐. 시간주파수를 올리면(약 8Hz 깜박임) 저주파 감도가 상승하고 밴드패스가 로우패스로 변형. 참고 배경 휘도: 맑은 하늘 약 8,000 cd/m², 직사광 노면 3,000~10,000 cd/m², 실내 사무실 100~300 cd/m². |
| 출처 | Campbell FW & Robson JG (1968) "Application of Fourier analysis to the visibility of gratings", Journal of Physiology 197(3):551–566 (1차 출처). 시공간 결합 특성은 Robson JG (1966) Journal of the Optical Society of America 56:1141–1142. 측면 억제 기전은 Kuffler SW (1953) Journal of Neurophysiology 16:37–68. |

눈은 모든 크기의 무늬에 똑같이 민감하지 않다. 아주 굵은 줄무늬(저주파)도, 아주 가는 줄무늬(고주파)도 잘 못 보고, 중간 굵기에서 가장 민감하다. 이를 공간주파수 축으로 그린 것이 대비 민감도 함수이고, 모양은 가운데가 솟은 산 형태, 즉 밴드패스 필터다. 고주파 쪽이 떨어지는 이유는 눈의 광학 흐림과 원뿔세포 간격 때문이고, 저주파 쪽이 떨어지는 이유는 망막 신경 회로의 측면 억제 때문이다. 측면 억제는 주변보다 밝은지 어두운지의 '차이'만 전달하도록 신호를 가공하므로, 넓고 완만한 밝기 변화는 애초에 뽑아내지 않는다. 증강현실에서 이 함수가 결정적인 이유는, 광학 시스루 장치가 실제 세계 빛 위에 가상 빛을 '더하기'만 할 수 있기 때문이다. 배경 휘도가 L일 때 가상 물체의 대비는 ΔL/(ΔL+L)이므로, 배경이 밝을수록 같은 대비를 내는 데 필요한 디스플레이 휘도가 폭증하고, 원리적으로 검은색은 만들 수 없다.

### 휘도 적응 범위 — 14 로그 단위를 3 로그 창으로 훑는다
| 항목 | 내용 |
| --- | --- |
| 수치 | 지각 가능 휘도 범위 약 10⁻⁶ ~ 10⁸ cd/m², 약 14 로그 단위. 한 순간의 동시 대비 범위 약 3 로그 단위(1,000:1). 동공 직경 2~8mm → 면적비 16배(약 1.2 로그). 나머지 약 12~13 로그는 광화학·신경 이득. 참고: 별빛 밤 약 10⁻³ cd/m², 실내 조명 10~100 cd/m², 흐린 날 야외 1,000 cd/m², 맑은 날 야외 3,000~10,000 cd/m². |
| 출처 | Hood DC & Finkelstein MA, "Sensitivity to light", in Boff KR, Kaufman L, Thomas JP (eds.) "Handbook of Perception and Human Performance", Vol. 1 (Wiley, 1986), 5장. 동공 기여도는 Watson AB & Yellott JI (2012) "A unified formula for light-adapted pupil size", Journal of Vision 12(10):12. |

사람은 별빛 아래부터 눈 덮인 설원까지, 밝기 차이가 100조 배에 달하는 환경을 모두 본다. 그러나 이 넓은 범위를 한꺼번에 보는 것이 아니다. 어느 한 순간에 구분할 수 있는 밝기 범위는 대략 1,000배(3 로그 단위)에 불과하며, 이 좁은 창을 현재 환경 밝기에 맞춰 옮기는 것이 적응이다. 적응을 담당하는 기구는 세 층이다. 첫째는 동공으로, 지름이 8밀리미터에서 2밀리미터까지 변해 면적 기준 약 16배(1.2 로그)를 조절한다. 이것만으로는 턱없이 부족하므로, 둘째로 광수용체 안의 색소 농도와 세포 내 이득이 바뀌고, 셋째로 망막 신경 회로가 게인을 재조정한다. 동공은 전체 범위의 10%도 감당하지 못하므로, 흔한 통념과 달리 적응의 주역이 아니다. 증강현실에서 이 사실이 중요한 이유는, 사용자의 순응 상태를 모른 채 디스플레이 밝기를 정하면 어떤 값도 틀리기 때문이다.

### 암순응과 명순응 — 45분 대 5분의 비대칭
| 항목 | 내용 |
| --- | --- |
| 수치 | 원뿔 순응 완료 약 9~10분, 감도 상승 약 1~2 로그. 원뿔-간상 분기점 약 5~10분. 간상 순응 30~45분, 완전 순응까지 최대 약 2시간. 최종 감도 상승 10⁴~10⁶배. 로돕신 재생 반감기 약 5분(원뿔 색소는 약 90초~2분으로 훨씬 빠름). 명순응 약 수십 초~5분. 간상세포 최대 감도는 약 507nm(청록), 원뿔 기반 주간시 최대 감도는 555nm — 어두워지면 붉은색이 먼저 어두워지는 푸르키녜 이동의 원인. |
| 출처 | Hecht S, Haig C, Chase AM (1937) "The influence of light adaptation on subsequent dark adaptation of the eye", Journal of General Physiology 20:831–850 (고전 1차 출처). 색소 재생 동역학은 Lamb TD & Pugh EN (2004) "Dark adaptation and the retinoid cycle of vision", Progress in Retinal and Eye Research 23:307–380. |

어두운 곳에 들어가면 시력이 서서히 돌아오는데, 그 회복 곡선은 매끄러운 직선이 아니라 두 단계로 꺾인다. 처음 5~10분은 원뿔세포가 회복하는 구간으로, 감도가 10~100배 올라가다 멈춘다. 그 뒤 곡선이 한 번 꺾이며(원뿔-간상 분기점) 간상세포가 주도권을 가져가고, 30~45분에 걸쳐 감도가 최종적으로 1만~100만 배까지 올라간다. 이 느림의 원인은 화학이다. 밝은 빛에 표백된 시각 색소 로돕신을 다시 만들려면 비타민A 유도체가 색소상피를 오가는 순환이 필요하고, 그 재생 반감기가 약 5분이다. 반대로 어두운 곳에서 밝은 곳으로 나오는 명순응은 색소를 분해하는 방향이라 훨씬 빠르며, 수십 초에서 길어야 5분이면 끝난다. 이 비대칭 — 어두워지는 데 45분, 밝아지는 데 5분 — 이 증강현실 야간 사용의 핵심 제약이다.

### 시간 해상도와 임계융합주파수(CFF) — 60Hz는 절반의 진실
| 항목 | 내용 |
| --- | --- |
| 수치 | 간상 매개 CFF 포화 약 15Hz, 원뿔 매개 CFF 포화 약 60Hz(고휘도). 페리-포터 법칙: CFF = a·log₁₀L + b, 원뿔에서 기울기 약 10~12Hz/log 단위. 주변시 대면적·고휘도 조건에서 90Hz 이상 보고(Tyler CW의 주변시 측정). 안구 운동 중에는 최대 약 2,000Hz의 변조도 감지 가능(팬텀 어레이·'무지개 효과'), 일부 관찰자에서는 훨씬 높은 주파수까지. 참고 기기 리프레시: Quest 3 90/120Hz, Valve Index 최대 144Hz, Apple Vision Pro 90/96/100Hz. |
| 출처 | Ferry ES (1892) American Journal of Science 44:192–207 및 Porter TC (1902) Proceedings of the Royal Society A 70:313–329 (법칙의 1차 출처). 중심-주변 차이는 Tyler CW (1985) "Analysis of visual modulation sensitivity. II. Peripheral retina and the role of photoreceptor dimensions", JOSA A 2:393–398. 요약은 Kalloniatis M & Luu C, "Temporal Resolution", Webvision. |

깜박이는 빛은 어느 주파수를 넘으면 연속된 빛으로 보인다. 그 경계가 임계융합주파수(CFF)다. 흔히 '사람 눈은 60Hz까지'라고 하지만, 이 값은 고정 상수가 아니라 조건의 함수다. 첫째, 밝을수록 높아진다. 페리-포터 법칙에 따라 CFF는 휘도의 로그에 비례해 직선으로 올라가며, 휘도가 10배 오를 때마다 대략 10~12Hz씩 상승한다. 밝은 원뿔 조건에서 약 60Hz 근처에 포화하고, 어두운 간상 조건에서는 약 15Hz에서 멈춘다. 둘째, 자극이 클수록, 그리고 시야 주변일수록 CFF가 높아진다. 주변시는 큰 자극과 높은 휘도에서 중심시보다 뚜렷하게 높은 융합 주파수를 보인다. 왜 그런가 하면 주변 경로는 해상도를 포기하는 대신 시간 응답이 빠른 세포(마그노 계열)로 구성돼 있기 때문이다. 셋째, 안구가 움직이는 동안에는 빛의 시간 변조가 망막 위 공간 패턴으로 바뀌어, 훨씬 높은 주파수까지 감지된다.

### 지속성(persistence)과 망막 번짐 — 저지속성 구동이 발명된 이유
| 항목 | 내용 |
| --- | --- |
| 수치 | 시각 통합의 임계 지속(블로흐 법칙) 약 20~100밀리초, 저조도에서 더 김. 90Hz 프레임 시간 11.1밀리초. 머리 회전 100도/초 × 11.1ms = 1.11도 번짐 = 60 PPD 기준 약 67화소. 점등 2ms로 낮추면 0.2도 = 약 12화소. 듀티비 2/11.1 = 18% → 동일 평균 휘도에 필요한 순간 휘도 약 5.5배. 업계 목표 지속 시간 2밀리초 이하. 일상 머리 회전 속도 100~200도/초, 빠른 회전 시 최대 약 500도/초. |
| 출처 | 블로흐 법칙 원전은 Bloch AM (1885) Comptes Rendus de la Société de Biologie 37:493–495. 지속성-번짐 관계와 2밀리초 목표는 Abrash M (2013) "Down the VR Rabbit Hole: Fixing Judder" 및 (2012) "Why Virtual Isn't Real to Your Brain", Valve 개발자 기술 블로그 (업계 1차 기술 출처). 유지형 디스플레이의 운동 번짐 이론은 Klompenhouwer MA & Velthoven LJ (2004) SID Symposium Digest. |

눈은 빛을 순간적으로 읽지 않고 일정 시간 동안 모아서 읽는다. 블로흐 법칙에 따르면 어떤 임계 시간 이내에서는 밝기×시간의 곱만 중요하며, 그 임계 시간은 조건에 따라 20~100밀리초 수준이다. 여기서 증강현실의 고약한 문제가 생긴다. 사용자가 머리를 돌리면 전정안구반사가 시선을 세계에 고정하므로, 눈은 세계에 대해 정지해 있고 디스플레이 화면에 대해서는 움직인다. 그런데 화면이 한 프레임 내내 켜져 있으면(풀 지속성), 그 프레임 시간 동안 화면의 한 점이 망막 위를 쭉 긁고 지나가며 선을 그린다. 90Hz에서 프레임은 11.1밀리초이고, 머리 회전 속도가 100도/초라면 번짐은 1.1도, 도당 60화소 기준 약 66화소 길이가 된다. 해결책은 화면을 프레임 대부분 동안 꺼두고 아주 짧게만 켜는 것이다. 점등 시간을 2밀리초로 줄이면 번짐은 0.2도, 약 12화소로 줄어든다. 대가는 밝기다. 듀티비가 18%로 떨어지므로 같은 체감 밝기를 내려면 순간 휘도를 5.5배 올려야 한다.

### 단속운동(saccade) — 하루 20만 번의 순간이동
| 항목 | 내용 |
| --- | --- |
| 수치 | 빈도 초당 2~3회, 하루 약 15만~20만 회. 대부분의 진폭 15도 이하. 주계열 근사: 지속시간 D ≈ 2.2·A + 21 밀리초(A는 진폭, 도) → 10도에서 약 43ms, 20도에서 약 65ms. 최고 각속도: 10도에서 약 300도/초, 30도에서 약 500도/초, 최대 약 700도/초(원숭이는 1,000도/초). 잠복기 약 200밀리초(express saccade는 약 80~120밀리초). 미세단속운동 진폭 2~120 분각, 빈도 초당 약 1~2회. 고정 중 표류 약 20~40 분각/초, 떨림 약 20~100Hz·진폭 20~40 초각. |
| 출처 | Bahill AT, Clark MR, Stark L (1975) "The main sequence, a tool for studying human eye movements", Mathematical Biosciences 24:191–204 (주계열의 1차 출처). 고정 미세운동은 Martinez-Conde S, Macknik SL, Hubel DH (2004) "The role of fixational eye movements in visual perception", Nature Reviews Neuroscience 5:229–240. |

눈은 부드럽게 훑지 않는다. 한 곳에 200~330밀리초 머물렀다가 다음 곳으로 총알처럼 튀는 동작을 반복하며, 이를 단속운동이라 한다. 이 운동은 탄도적(ballistic)이어서 일단 발사되면 중간에 목표를 바꿀 수 없고, 그 대신 진폭과 속도·지속시간 사이에 일정한 관계(main sequence)가 성립한다. 진폭이 클수록 최고 속도가 올라가고 지속시간은 대략 선형으로 길어진다. 왜 탄도적인가 하면, 시각 피드백으로 궤적을 제어하려면 최소 60~100밀리초가 필요한데 단속운동 자체가 그보다 짧게 끝나기 때문이다. 뇌는 피드백 대신 미리 계산한 신호를 한 번에 쏜다. 시선을 고정하고 있을 때도 눈은 멈추지 않는다. 미세단속운동, 표류(drift), 떨림(tremor)이 계속되어 망막상은 끊임없이 흔들리며, 이 흔들림이 없으면 상은 몇 초 안에 사라진다(Troxler 소멸).

### 추적운동(smooth pursuit) — 느리지만 유일하게 부드러운 눈
| 항목 | 내용 |
| --- | --- |
| 수치 | 잠복기 90~150밀리초(단속운동의 자발적 잠복기 200~250밀리초 대비 빠름). 개루프 구간 약 100밀리초. 이득(눈 속도/목표 속도) 약 0.9 내외. 최대 유지 속도 약 30도/초, 이를 넘으면 따라잡기 단속운동 발생(훈련·최적 조건에서 100도/초까지 보고). 수직 방향, 특히 위쪽 추적이 수평보다 불리. 계산 예: 60Hz 풀 지속성 화면에서 30도/초 추적 시 망막 번짐 = 30 × (1/60) = 0.5도 ≈ 30화소(60 PPD 기준). |
| 출처 | Lisberger SG, Morris EJ, Tychsen L (1987) "Visual motion processing and sensory-motor integration for smooth pursuit eye movements", Annual Review of Neuroscience 10:97–129 (표준 1차 리뷰). 속도 한계와 따라잡기 단속운동은 Meyer CH, Lasker AG, Robinson DA (1985) Vision Research 25:561–563. |

움직이는 물체를 눈으로 따라갈 때만 눈은 진짜로 부드럽게 움직인다. 이 추적운동은 단속운동과 달리 시각 피드백 제어 루프로 동작한다. 목표의 망막상 속도 오차를 줄이는 방향으로 눈 속도를 조절하는 방식이라 잠복기가 90~150밀리초로 단속운동보다 짧고, 개루프 구간이 약 100밀리초 지속된 뒤 폐루프로 전환된다. 다만 이 루프에는 한계 속도가 있다. 목표가 약 30도/초를 넘으면 추적만으로 따라잡지 못해 중간중간 따라잡기 단속운동이 끼어들고, 시선은 부드러움을 잃는다. 또 추적운동은 대개 실제로 움직이는 시각 목표가 있어야 발동하며, 아무것도 없는 어둠 속에서 의지만으로 눈을 부드럽게 움직이기는 매우 어렵다. 증강현실에서 이 운동이 중요한 이유는, 사용자가 움직이는 가상 물체를 눈으로 따라갈 때 눈이 화면에 대해 미끄러지며 앞 항목과 똑같은 망막 번짐을 만들기 때문이다.

### 전정안구반사(VOR) — 증강현실 지연 예산 20밀리초의 진짜 이유
| 항목 | 내용 |
| --- | --- |
| 수치 | 지연 7~15밀리초(문헌에서 흔히 '10밀리초 미만'으로 인용). 이득 약 1.0(수평·수직), 유효 주파수 대역 약 0.5~15Hz(일부 조건에서 20Hz 이상). 비틀림(torsional) VOR은 이득이 낮음. 일상 머리 회전 100~200도/초, 빠른 회전 최대 약 500도/초. 오차 계산: 지연 20밀리초 × 회전 100도/초 = 2도 어긋남 → 팔 길이(60cm)에서 약 2.1cm 위치 오차. 지연 50밀리초 × 200도/초 = 10도. 지연 지각 역치: 헤드마운트 조건에서 대략 10~20밀리초, 최적 조건의 시스루 증강현실에서는 수 밀리초까지 낮게 보고된 사례 있음. |
| 출처 | 3-뉴런 호와 반사 특성은 Leigh RJ & Zee DS, "The Neurology of Eye Movements" 5th ed. (Oxford University Press, 2015), 2장. 증강현실 지연 지각은 Ellis SR, Mania K, Adelstein BD, Hill MI (2004) "Generalizeability of latency detection in a variety of virtual environments", Proceedings of the Human Factors and Ergonomics Society 48:2632–2636 및 Adelstein BD, Lee TG, Ellis SR (2003) HFES Proceedings 47:2083–2087. |

머리를 돌려도 세상이 흔들려 보이지 않는 것은 눈이 머리와 반대 방향으로 정확히 같은 각도만큼 돌기 때문이다. 이 보상을 담당하는 것이 전정안구반사이며, 사람 몸에서 가장 빠른 반사 중 하나다. 빠른 이유는 회로가 극도로 짧기 때문이다. 속귀의 반고리관에서 전정핵을 거쳐 외안근 운동신경핵까지, 신경세포 셋만 건너면 끝난다(3-뉴런 호). 결정적으로 이 반사는 시각을 쓰지 않는다. 눈이 얼마나 어긋났는지 보고 고치는 피드백 방식이 아니라, 머리의 각속도를 관성 센서로 직접 재서 앞먹임으로 눈을 미는 개루프 방식이다. 그래서 시각 피드백에 의존하는 추적운동보다 10배 이상 빠르다. 바로 이 지점이 증강현실 지연 목표의 근원이다. 머리를 돌리면 사용자의 눈은 10밀리초 안에 세계의 한 점에 고정된다. 그런데 디스플레이가 50밀리초 뒤에 갱신되면, 눈이 이미 고정한 그 점에 가상 물체가 아직 도착하지 않은 상태가 되고, 가상 물체는 실제 세계 위에서 미끄러지는 것처럼 보인다.

### 단속운동 억제(saccadic suppression) — 하루 중 10%의 공짜 창
| 항목 | 내용 |
| --- | --- |
| 수치 | 대비 역치 상승 최대 약 0.5~1 로그 단위(2~10배). 저공간주파수(약 1주기/도 이하)에 선택적, 고공간주파수는 거의 영향 없음. 시작 시점 단속운동 개시 약 50~75밀리초 전, 종료 후 약 50밀리초까지 지속 → 총 창 길이 약 100~200밀리초. 하루 단속운동 15만~20만 회 × 창 100밀리초 = 깨어 있는 16시간의 약 10% 이상. 응용: 단속운동 중 리다이렉티드 워킹의 회전 이득은 감지되지 않고 최대 약 12.6~14도/초까지 적용 가능하다는 보고(Steinicke 등 2010년경 실험, 조건 의존). |
| 출처 | Burr DC, Morrone MC, Ross J (1994) "Selective suppression of the magnocellular visual pathway during saccadic eye movements", Nature 371:511–513 (선택적 억제의 1차 출처). 시점과 기전 리뷰는 Ross J, Morrone MC, Goldberg ME, Burr DC (2001) "Changes in visual perception at the time of saccades", Trends in Neurosciences 24:113–121. 응용은 Sun Q et al. (2018) "Towards virtual reality infinite walking: dynamic saccadic red |

눈이 700도/초로 튈 때 망막에는 엄청난 번짐이 지나가야 정상이다. 그런데 우리는 그 번짐을 보지 못한다. 뇌가 단속운동 전후로 시각 감도를 능동적으로 낮추기 때문이다. 이 억제에는 두 가지 기전이 함께 작용한다. 하나는 능동적 억제로, 운동 명령을 내리는 회로가 그 사본(원심성 복사)을 시각 경로에 보내 미리 감도를 떨어뜨린다. 그 증거가 억제 시작 시점이다. 억제는 눈이 실제로 움직이기 50~75밀리초 전에 이미 시작된다 — 즉 망막에서 일어난 일의 결과가 아니다. 다른 하나는 마스킹으로, 단속운동 직전과 직후의 선명한 상이 그 사이의 번짐을 앞뒤에서 덮어버린다. 중요한 단서는 이 억제가 선택적이라는 점이다. 굵은 무늬(저공간주파수)는 강하게 억제되지만, 가는 무늬(고공간주파수)는 거의 억제되지 않는다. 마그노 경로만 골라 끄기 때문으로 해석된다.

### 입체시와 이접-조절 충돌 — 2초각의 정밀도가 만든 함정
| 항목 | 내용 |
| --- | --- |
| 수치 | 입체시력 역치 최고 약 2~6초각(최적 실험 조건), 임상 정상 20~40초각. 동공간거리(IPD) 성인 평균 약 63mm, 범위 약 52~78mm. 파눔 융합 영역: 중심와에서 약 ±5~10분각, 이심률 10도에서 ±30~40분각까지 확대. 편안한 이접-조절 불일치 영역 약 ±0.4디옵터(Shibata 등 2011). 눈의 초점 심도 약 ±0.3디옵터(동공 3~4mm). 계산 예: 초점면 2m(0.5D) 디스플레이에 30cm(3.33D) 물체를 시차로 배치 → 충돌 2.83D, 편안한 영역의 약 7배. 다초점면 방식의 권장 면 간격 약 0.6~0.9디옵터. 성인의 약 3~5%는 입체시가 약하거나 없음. |
| 출처 | Shibata T, Kim J, Hoffman DM, Banks MS (2011) "The zone of comfort: Predicting visual discomfort with stereo displays", Journal of Vision 11(8):11 (편안한 영역의 1차 출처). 기전과 다초점면 해법은 Hoffman DM, Girshick AR, Akeley K, Banks MS (2008) "Vergence–accommodation conflicts hinder visual performance and cause visual fatigue", Journal of Vision 8(3):33. 파눔 영역은 Howard IP & Rogers BJ, "Binocular Vision and Stereo |

두 눈은 약 6.3센티미터 떨어져 있어 같은 물체를 조금 다른 각도에서 본다. 뇌는 이 차이(양안 시차)를 거리로 환산하는데, 그 정밀도가 놀랍다. 최적 조건에서 2~6초각, 즉 1도의 1,000분의 1 수준의 시차까지 구분한다. 자연 시야에서는 이 시차 신호와 초점 신호가 항상 일치한다. 가까운 것을 볼 때 두 눈이 안으로 모이고(이접), 동시에 수정체가 두꺼워져 초점을 당긴다(조절). 두 반응은 신경학적으로 서로 연결돼 자동으로 함께 움직인다. 그런데 대부분의 헤드마운트 디스플레이는 화면이 고정된 한 거리에 맺히므로, 초점은 항상 그 거리에 있는데 시차는 물체 거리를 말한다. 두 신호가 어긋나고, 이를 이접-조절 충돌이라 한다. 눈의 초점 심도가 ±0.3디옵터 정도로 좁아 이 어긋남을 흡수하지 못하며, 대략 ±0.4디옵터를 넘으면 피로·두통·복시 경향이 나타난다. 문제가 가장 심한 구간은 역설적으로 증강현실에서 가장 쓸모 있는 구간, 즉 손이 닿는 거리다.

### 주변시 군집화(crowding)와 유용시야 — 주변은 흐린 것이 아니라 뒤섞인 것
| 항목 | 내용 |
| --- | --- |
| 수치 | 부마 법칙: 임계 간격 ≈ 0.5 × 이심률(계수는 과제에 따라 0.3~0.5). 예: 이심률 10도 → 임계 간격 약 5도. 군집화의 E2는 약 0.5~1도로, 시력의 E2(약 2.5도)보다 훨씬 작아 군집화가 더 빠르게 악화. 유용시야(UFOV)는 이중 과제 조건에서 유효 반경이 유의하게 축소(고령·고부하에서 감소폭 큼). 무주의 맹시 고전 실험에서 예상 밖 자극 미검출률 약 46~50%(Simons & Chabris 1999). |
| 출처 | Bouma H (1970) "Interaction effects in parafoveal letter recognition", Nature 226:177–178 (1차 출처). 종합 리뷰는 Whitney D & Levi DM (2011) "Visual crowding: a fundamental limit on conscious perception and object recognition", Trends in Cognitive Sciences 15:160–168. 유용시야는 Ball KK, Beard BL, Roenker DL et al. (1988) JOSA A 5:2210–2219. 무주의 맹시는 Simons DJ & Chabris CF (1999) Perception 28:1059–1074. |

주변시의 한계를 해상도로만 설명하면 절반을 놓친다. 주변에 글자 하나만 놓으면 놀랄 만큼 잘 읽히지만, 그 글자 좌우에 다른 글자를 붙이는 순간 가운데 글자를 알아볼 수 없게 된다. 시력이 떨어져서가 아니다. 대상 자체는 여전히 분해되는데, 주변 요소들의 특징이 뒤섞여 하나의 텍스처로 뭉개지기 때문이다. 이를 군집화(crowding)라 한다. 방해를 일으키는 임계 간격에는 간단한 규칙이 있다. 부마 법칙에 따르면 임계 간격은 대략 이심률의 절반이다. 중심에서 10도 떨어진 곳이라면 좌우 5도 안에 다른 요소가 있으면 안 된다는 뜻이다. 이 값은 시력 저하보다 훨씬 빠르게 커지므로, 주변시의 실질적 한계는 해상도가 아니라 군집화가 정한다. 여기에 인지 부하가 겹치면 유용시야가 더 줄어든다. 중심 과제가 어려울수록 주변에서 실제로 처리되는 범위가 좁아지고, 눈에 똑똑히 들어온 것도 알아차리지 못하는 무주의 맹시가 나타난다.

#### 검증에서 잡힌 정정
- 맹점 방향 오류: '맹점(시신경유두)은 코 쪽 약 15도'. 시신경유두는 망막에서 코 쪽이지만, 시야 좌표에서 맹점은 귀 쪽(temporal) 12~15도, 수평선보다 약 1.5도 아래에 나타난다. 같은 항목의 다른 수치가 모두 시야 각도이므로 좌표계가 뒤섞였다. 크기는 약 5.5도(폭)×7.5도(높이)이므로 '5도×7도'는 폭·높이 순서만 주의하면 허용 범위. (출처: Wikipedia Blind spot — 'about 12–15° temporally and 1.5° below the horizontal', 'roughly 7.5° high and 5.5° wide')
- 간상 피크 위치의 단위 자기모순: '간상세포 피크는 중심에서 약 18~20도(망막상 4.5mm)'. 같은 문서가 채택한 환산(1도≈288~291µm)을 적용하면 4.5mm=15.6도이고, 18~20도=5.18~5.76mm다. 두 값이 동시에 성립할 수 없다. Curcio 1990은 간상 피크를 이심률 3~5mm의 타원형 고리로 보고한다(≈10~17도). Webvision(Kolb)이 'about 4.5 mm or 18 degrees'라고 느슨하게 쓴 문장을 그대로 옮긴 것으로 보이며, 1차 데이터와 환산식 중 하나에 맞춰 고쳐야 한다.
- 고정 지속시간 역수 오류: '시선 이동 빈도 초당 2~3회(즉 고정 지속 시간 평균 200~330밀리초)'. 2~3회/초의 역수는 333~500밀리초다. 200밀리초가 되려면 초당 5회여야 한다. 읽기 과제의 고정 시간(200~250ms)을 장면 관찰 빈도(2~3회/초)의 역수로 잘못 제시했다.
- 이심률 시력 계열과 E2의 자기모순: 제시된 비율(2도 1/2, 4도 1/3, 6도 1/4, 30도 1/16)을 MAR=M0(1+E/E2)에 대입하면 네 점 모두 정확히 E2=2.0도를 함의한다. 그런데 같은 항목은 'E2≈2.5도'라고 적었고, E2=2.5를 쓰면 6도에서 1/3.4, 30도에서 1/13이 되어 표에 적힌 1/4, 1/16과 불일치한다.
- V1 중심 2도 점유율 오류: '중심 2도 시야가 V1 표면적의 약 8~10%'. 인용한 Horton & Hoyt(1991)의 면적 확대율 m=(17.3mm/(ρ+0.75도))²를 시야에 걸쳐 적분하면 중심 2도는 V1의 약 15~17%(외곽 한계 60~90도 가정)다. 8%에 가까운 값은 중심 '1도'(7~8%)에 해당한다. 같은 적분은 중심 10도에서 약 45~51%를 주어 Horton & Hoyt의 '50~60%' 서술과 정합한다. (식 확인: PMC8378846 본문 인용)
- 전 시야 화소수의 이중 오류: '전 시야(200도×135도)를 60 PPD로 채우면 한쪽 눈에 12,000×8,100 ≈ 9,720만 화소'. (a) 200도는 양안 합산 수평 시야이며 같은 문서가 단안 수평을 약 160도(코 60 + 귀 100)로 적었으므로 '한쪽 눈'에 붙일 수 없다. (b) 구면 시야에 평면 격자를 곱해 입체각의 cos 항을 빠뜨렸다. 60 PPD는 1.18×10^7 화소/스테라디안이므로 양안 시야 6.450 sr → 7,620만 화소, 단안(160도×(상60·하75)) 5.116 sr → 6,050만 화소다. 9,720만은 약 28% 과대이며, 같은 문서가 바로 앞 항목에서 5도 원의 비중을 입체각으로 정확히(0.093%) 계산한 것과 방법이 불일치한다.
- 단속운동 억제 예산 산수 오류: '하루 단속운동 15만~20만 회 × 창 100밀리초 = 깨어 있는 16시간의 약 10% 이상'. 15만×0.1초=15,000초=4.17시간=16시간의 26.0%, 20만×0.1초=5.56시간=34.7%다. 제시된 곱셈에서 10%는 나오지 않으며(약 3배 차이), 창 길이를 문서가 말한 100~200밀리초 상한으로 잡으면 52~69%까지 간다. 소제목 '하루 중 10%의 공짜 창'도 함께 수정해야 한다.
- 로그-배율 환산 오류: '대비 역치 상승 최대 약 0.5~1 로그 단위(2~10배)'. 0.5 로그 단위는 10^0.5=3.16배이고 2배는 0.30 로그 단위다. 괄호 안 범위는 '약 3~10배'여야 한다.
- 리다이렉티드 워킹 수치의 차원·출처 오류: '단속운동 중 회전 이득은 감지되지 않고 최대 약 12.6~14도/초까지 적용 가능(Steinicke 등 2010년경)'. Steinicke 등 2010(IEEE TVCG 16(1):17-27, 초록 원문 대조)은 단속운동 억제 실험이 아니라 보행 중 재지향 실험이며, 결과는 전부 무차원 이득이다 — 물리 회전이 지각 회전보다 '49% 크게 또는 20% 작게', 거리 '14% 축소 / 26% 확대', 곡률 '반경 22m 이상'. 도/초 단위 값은 논문에 없다. 또한 '이득(무차원)'을 '도/초(각속도)'로 서술한 것 자체가 차원 오류이며, 단속운동 기반 재지향의 1차 출처는 Bolte & Lappe 2015(IEEE TVCG 21(4):545-552)와 같은 항목이 이미 인용한 Sun 등 2018이다.
- Shibata 2011의 결론 왜곡: '편안한 이접-조절 불일치 영역 약 ±0.4디옵터(Shibata 등 2011)'. 해당 논문(초록 원문 대조)의 핵심 결과는 편안한 영역이 대칭이 아니라는 것이다 — 같은 디옵터 값의 불일치가 원거리에서 더 불편하고, 음의 불일치(화면 뒤)는 원거리에서, 양의 불일치(화면 앞)는 근거리에서 더 불편하다. 단일 대칭 수치 ±0.4D는 원문에 없다. 따라서 뒤따르는 계산 '충돌 2.83D = 편안한 영역의 약 7배'도 분모가 무효여서 성립하지 않는다.
- 암순응 단계 순서 모순: '원뿔 순응 완료 약 9~10분' 다음에 '원뿔-간상 분기점 약 5~10분'이라고 적었다. 분기점은 원뿔이 정체한 뒤 간상이 주도권을 갖는 시점이므로 원뿔 완료보다 앞설 수 없다. 고전 표준값은 원뿔 정체 약 4~8분, 원뿔-간상 분기점 약 7~10분이다.
- 고정 미세운동 수치: 떨림(tremor) 대역을 '약 20~100Hz'로 적었으나 표준 보고는 40~100Hz(대표값 약 90Hz)이며 20~40Hz는 표류(drift) 대역이다. 표류 속도 '약 20~40 분각/초'도 인용된 Martinez-Conde 등 2004가 담는 고전값(진폭 약 1.5~4분각, 중위 속도 약 4분각/초)과 다르고, 자연 장면 자유관찰 조건의 약 50분각/초와도 다르다 — 측정 조건(머리 고정 여부, 저역 통과 차단 주파수)이 빠진 채 중간값만 제시되어 어느 문헌으로도 추적되지 않는다. 떨림 진폭도 최신 리뷰는 약 1분각(≈60초각)으로 적어 '20~40초각'보다 크다. (출처: PMC5082990, Rucci & Poletti)
- 원뿔세포 개인 범위: '약 440만~530만'. Curcio 등 1990이 보고한 범위는 4.08~5.29백만(408만~529만)으로, 같은 문장의 간상 범위(7,800만~1억 700만 = 77.9~107.3백만)가 원문과 정확히 일치하는 것을 보면 원뿔 하한만 전사 과정에서 올라간 것으로 보인다. 다만 이 세션에서는 검색 예산 소진으로 초록 원문을 축자 재확인하지 못했고(Crossref 요약에서 4.6백만·199,000/mm²·92백만·0.350mm만 확인) 범위 문구는 미확인이므로, 원문 초록 한 줄 대조로 확정할 것을 권한다.
- (소) 페리-포터 기울기 '원뿔에서 약 10~12Hz/로그 단위'는 보고값(중심와 약 12.5Hz/decade, 주변부 약 19Hz/decade)보다 낮고 좁게 잡혔다. 인용 출처로 든 Webvision 'Temporal Resolution' 문서에는 기울기 수치가 없으며, 오히려 '이심률이 커지면 기울기가 더 급해진다'고만 적혀 있어 단일 범위 제시의 근거가 되지 못한다.
- (소) '세 가지 독립된 값의 우연한 일치'라는 서술은 수치가 뒷받침하지 않는다: 회절 0.77분각, 원뿔 간격 0.4~0.5분각, 시력 1.0의 1분각은 2배 이상 흩어져 있다. 격자(공간주파수) 기준으로 맞추면 회절 차단은 D/λ=95주기/도, 원뿔 나이퀴스트 약 60주기/도, 행동 차단 30~60주기/도로, '일치'가 아니라 '같은 자릿수'가 정확한 표현이다.
- (소) 단안 시야 상·하 '위 약 60도, 아래 약 70~75도'는 출처 의존값이다. 다른 표준 임상 기준은 상 70도·하 80도를 쓴다(Wikipedia Visual field: 'temporally 107, nasally 60, 70 above, 80 below'). 단일 수치로 제시하지 말고 측정 기준(눈썹·뺨 차폐 포함 여부)을 명시해야 한다. 참고로 이 항목의 양안 합산(200~220도), 중첩(114~120도), 수직(135도)은 제시된 단안 값들과 산술적으로 정합한다.
- 원뿔세포 개인별 범위를 '약 440만~530만'으로 적었으나, 1차 출처 Curcio et al. 1990 초록의 값은 4.08~5.29 million이다. 하한이 4.4M이 아니라 4.08M이며, 실제 변이폭(1.21M)을 0.9M으로 25% 축소했다. (PMID 2324310 원문: 'The average human retina contains 4.6 million cones (4.08-5.29 million)')
- '맹점(시신경유두)은 코 쪽 약 15도' — 망막/시야 좌표를 혼동한 원리 오류. 시신경유두는 망막에서 코 쪽이지만, 그것이 만드는 맹점은 시야에서 **귀 쪽** 12~15도에 나타난다. 같은 항목의 다른 수치가 모두 시야각이므로 독자는 시야 코 쪽으로 읽게 된다. 또 표준값은 수평 경선 아래 약 1.5도라는 조건이 붙는다(맹점: 귀 쪽 12~15도, 수평 아래 1.5도, 7.5도 높이 × 5.5도 폭).
- 간상세포 피크 위치를 '중심에서 약 18~20도(망막상 4.5mm)'로 병기했으나 두 값이 서로 모순된다. 같은 문서가 채택한 환산율 288~291µm/도로 계산하면 4.5mm = 15.6도, 18~20도 = 5.2~5.8mm다. Webvision 원문은 '4.5mm 또는 18도'(photoreceptors 장)와 '5mm 또는 18도'(Facts and Figures 장)로 서로 다르게 적고 있고, Curcio 1990 초록은 수치 대신 '시신경유두와 같은 이심률의 타원형 고리'라고만 기술한다. 유두 중심 이심률은 약 15~16도이므로 '18~20도'는 상한을 과대하게 늘린 값이다.
- 간상 피크 밀도 '약 150,000~160,000개/mm²'를 Curcio et al. 1990을 1차 출처로 달았으나, 그 논문 초록에는 간상 피크 밀도의 수치가 없다(위치와 상대 변화만 기술). 160,000/mm²는 Webvision 'Facts and Figures concerning the human retina' 장의 값이다. 또 Curcio 초록이 보고한 '피크는 통상 상측 망막(5/6안)', '수평 경선 교차 지점에서 15~25% 감소'라는 구조가 단순 '고리'로 평탄화됐다.
- 이심률별 시력비 표(2도 1/2, 4도 1/3, 6도 1/4, 30도 1/16)가 같은 항목이 제시한 E2 ≈ 2.5도와 불일치한다. 시력비 = 1/(1+E/E2)에 대입하면 네 점 모두 정확히 E2 = 2.00도를 가리킨다. E2 = 2.5도라면 각각 1/1.80, 1/2.60, 1/3.40, 1/13.00이 되어야 한다.
- '30도를 넘으면 더 가파르게 하락' — 바로 앞에서 제시한 선형 MAR 법칙 MAR = M0(1+E/E2)과 모순되며, 근거로 든 30도 1/16이라는 값 자체가 그 선형 법칙 위에 정확히 놓인다(E2=2.0 기준). 제시된 데이터 범위 안에는 가속 하락의 증거가 없다.
- '시력의 E2 ≈ 2.5도'의 1차 출처로 Levi, Klein & Aitsebaomo (1985) Vision Research 25:963–977을 지정했으나, 그 논문은 **버니어 시력(vernier acuity)**과 군집화를 측정한 연구로(초록: 'Vernier acuity, crowding and cortical magnification' — 버니어 역치는 지각 하이퍼컬럼 크기의 약 1/40) 버니어 E2는 1도 미만이다. 격자/시표 시력의 E2 ≈ 2.5도는 Weymouth·Westheimer 계열 값이며 Strasburger et al. 2011 리뷰가 그 정리를 담당한다.
- '중심 2도 시야가 V1 표면적의 약 8~10%를 차지' — 인용한 Horton & Hoyt (1991) 자신의 확대율 함수 M = 17.3/(E+0.75) mm/도로 면적 적분하면 A(2도)/A(10도) = 33.0%이고, 같은 저자들의 '중심 10도가 V1의 최소 50~60%' 진술과 결합하면 중심 2도는 약 18%다(중심 5도 > 50% 기준으로는 약 25%). 8~10%는 **중심 1도**의 값이다(같은 계산으로 8.8%). 약 2배 과소평가.
- '도당 60화소와 회절의 우연한 일치'라는 삼중 일치 주장이 성립하지 않는다. 세 값을 같은 단위로 환산하면 — 시력 1.0 → 30 c/deg(60 PPD), 회절 Rayleigh 0.77분각 → 약 39 c/deg(비간섭 차단 D/λ = 3mm/550nm = 95 c/deg), 원뿔 간격 2.4µm → Nyquist 69 c/deg — 2배 이상 벌어진다. 특히 1차 출처로 든 Williams (1985) 초록은 '약 60~70 c/deg 이상에서 앨리어싱이 보인다'고 명시하는데, 이는 원뿔 모자이크를 표시하려면 120~140 PPD가 필요함을 뜻한다. 60 PPD는 세 한계의 수렴점이 아니라 임상 시력 관례 단독으로 정해진 값이며, 광학 한계와 광수용체 한계 양쪽보다 **낮다**.
- '전 시야(200도×135도)를 60 PPD로 채우면 **한쪽 눈에** 12,000×8,100 ≈ 9,720만 화소' — 200도×135도는 같은 문서가 앞 항목에서 정의한 **양안** 합산 시야다. 단안 수평 시야는 본문 자신의 값(코 쪽 60도 + 귀 쪽 100~110도)으로 160~170도이므로 단안 환산은 약 9,600×8,100 ≈ 7,800만 화소다. 양안 시야로 계산한 값에 '한쪽 눈' 라벨을 붙였다.
- '하루 단속운동 15만~20만 회 × 창 100밀리초 = 깨어 있는 16시간의 약 10% 이상' 및 절 제목 '하루 중 10%의 공짜 창' — 자체 산수가 맞지 않는다. 15만×0.1초 = 15,000초, 20만×0.1초 = 20,000초이고 16시간 = 57,600초이므로 26~35%다. 본문이 제시한 창 길이 상한(200ms)을 쓰면 52~69%까지 간다. 결론을 약 3배 축소했다.
- '단속운동 중 리다이렉티드 워킹의 회전 이득은 감지되지 않고 최대 약 12.6~14도/초까지 적용 가능하다는 보고(Steinicke 등 2010년경 실험)' — Steinicke et al. 2010 (IEEE TVCG 16:17–27, PMID 19910658)에는 °/s 단위 수치가 존재하지 않는다. 그 논문이 보고한 역치는 전부 무차원 이득과 반경이다: 지각된 가상 회전보다 물리적으로 약 49% 더 또는 20% 덜 회전, 거리 −14%/+26% 스케일, 반경 22m 초과 원호. 또 그 실험은 단속운동 게이팅이 아닌 통상 시야에서의 이득 역치다. °/s 단위 리다이렉션 속도는 같은 항목이 별도로 인용한 Sun et al. 2018(단속운동 리다이렉션) 계열 문헌의 값이다.
- '편안한 이접-조절 불일치 영역 약 ±0.4디옵터(Shibata 등 2011)' — 인용 논문의 핵심 결론과 반대다. Shibata et al. 2011 (J Vis 11(8):11) 초록: '같은 디옵터 값의 충돌이 근거리보다 원거리에서 덜 편안했다', '음의 충돌(화면 뒤 콘텐츠)은 원거리에서, 양의 충돌(화면 앞)은 근거리에서 덜 편안했다'. 즉 comfort zone은 **거리 의존적이고 부호에 대해 비대칭**이며 고정 대칭 상수가 아니다. 이어지는 '충돌 2.83D는 편안한 영역의 약 7배' 계산도 이 잘못된 상수에 의존한다.
- '최대 유지 속도 약 30도/초... (훈련·최적 조건에서 100도/초까지 보고)'의 근거로 Meyer, Lasker & Robinson (1985) Vision Research 25:561–563을 들었으나 인용 관계가 역전됐다. 그 논문 제목은 'The upper limit of human smooth pursuit velocity'이고 초록은 '5명 중 4명에서 목표속도 100 deg/sec까지 안구속도가 목표속도의 약 90%였다'고 보고한다. 100°/s는 훈련·최적 조건의 예외가 아니라 일반 피험자 다수의 통상 결과이며, 30°/s는 그 논문에 없는 수치다.
- (외 30건)

## depth
항목 16개 · 검증 정정 지적 62건


### 역투영 문제 — 왜 깊이는 보이는 것이 아니라 추론되는 것인가
| 항목 | 내용 |
| --- | --- |
| 수치 | 투영식 x = f·X/Z (f는 눈의 절점-망막 거리, 인간 약 17mm). 광수용체 약 1억 2천만 간상세포 + 약 600만 원추세포 → 시신경 축삭 약 100만 개, 정보 압축비 약 100:1. 중심와 원추세포 간격 약 2.5μm(시각 약 0.5분각). 정상 시력 분해 한계 1분각(60초각). 초시력(vernier alignment) 역치 약 5초각 — 수용체 간격보다 열 배 미세. |
| 출처 | George Berkeley, An Essay Towards a New Theory of Vision (1709), §2, §11. / David Marr, Vision (1982), ch.1. / Stephen E. Palmer, Vision Science: Photons to Phenomenology (1999), ch.5 "Perceiving Depth and Shape". |

망막은 곡면이지만 본질적으로 2차원 센서다. 3차원 공간의 점 (X, Y, Z)는 눈 속에서 (fX/Z, fY/Z)로 투영되며, 이 나눗셈에서 Z 자체는 사라진다. 한 점이 망막에 맺히면 그 점은 눈에서 뻗어 나간 시선 위의 무한히 많은 점들 가운데 어느 것이든 될 수 있다. 버클리는 1709년에 이 사정을 "거리는 그 자체로는 보이지 않는다. 거리를 나타내는 선은 눈의 바닥에 한 점으로 끝나기 때문이다"라고 적었다. 따라서 깊이 지각은 측정이 아니라 역문제 풀이다. 정보가 부족한 방정식을 풀기 위해 뇌는 두 가지를 동원한다. 하나는 여러 개의 부분적 단서(cue)이고, 다른 하나는 세상에 대한 사전 가정(빛은 위에서 온다, 물체는 강체다, 바닥은 평평하다)이다. 단서는 각각 불완전하고 조건부이며 거리대마다 유효성이 다르다. 증강현실이 가능한 이유가 정확히 여기에 있다. 뇌가 추론으로 깊이를 만든다면, 추론의 입력을 위조하면 존재하지 않는 깊이를 만들어 넣을 수 있다.

### 가림(occlusion, interposition) — 가장 강하지만 가장 인색한 단서
| 항목 | 내용 |
| --- | --- |
| 수치 | 유효 거리 범위: 0m ~ 무한대(접촉 가능한 최근거리부터 지평선까지 균일). 제공 정보: 순서만(ordinal). 판정 역치 \|Δz\|/z ≈ 0 — 겹치기만 하면 판정 성립. 윤곽 정렬 초시력 역치 약 5초각(최적 조건). 커팅·비시턴의 9단서 순위에서 개인공간·행동공간·조망공간 전부 1위. |
| 출처 | James E. Cutting & Peter M. Vishton (1995), "Perceiving layout and knowing distances," in W. Epstein & S. Rogers (eds.), Perception of Space and Motion (Handbook of Perception and Cognition, Vol.5), Academic Press, pp.69–117 (특히 pp.80–83 및 Figure 3–5). / Hermann von Helmholtz, Treatise on Physiological Optics, Vol.3, §26. / Ken Nakayama, Shinsuke Shimojo & Gerald H. Silverman (1989), Perception 18 |

한 물체의 윤곽이 다른 물체의 윤곽을 끊고 지나가면, 끊은 쪽이 앞이다. 이 판정의 시각적 서명은 T자 접합(T-junction)으로, 세로획의 임자가 뒤에 있는 물체다. 가림이 세 가지 이유로 모든 거리대에서 최강 단서가 된다. 첫째, 물리적으로 위배되기 어렵다. 불투명한 물체는 예외 없이 뒤를 가리며, 반례는 거울·유리·그림자 정도로 드물다. 둘째, 판정에 필요한 정밀도가 극히 낮다 — 두 윤곽이 만나는지 아닌지만 보면 되고, 인간의 윤곽 정렬 감도는 초시력 수준이다. 셋째, 성능이 거리에 무관하다. 다른 단서들은 거리 z 또는 z²에 비례해 무너지지만, 가림은 5센티미터 앞이든 5킬로미터 앞이든 똑같이 작동한다. 대가는 인색함이다. 가림은 순서(ordinal)만 알려주고 거리 차이의 양(metric)은 한 톨도 알려주지 않는다. 손가락이 달을 가린다는 사실에서 손가락이 달보다 38만 킬로미터 가깝다는 정보는 나오지 않는다.

### 양안시차(binocular disparity) — 6.3센티미터짜리 삼각측량기
| 항목 | 내용 |
| --- | --- |
| 수치 | 성인 평균 IPD 약 63mm(범위 약 50~75mm). 중심와 스테레오 역치 최적 조건 5~10초각, 임상 정상 20~40초각. 역치 10초각(4.85×10⁻⁵ rad), IPD 63mm 기준 판별 가능한 최소 깊이차: 0.5m에서 0.19mm / 2m에서 3.1mm / 10m에서 7.7cm / 30m에서 0.69m / 100m에서 7.7m. 파눔 융합역 중심와 약 6분각, 주변 10도에서는 수십 분각. 유효 범위: 개인공간에서 최강, 행동공간에서 상위, 수백 미터에서 실질 소멸. |
| 출처 | Cutting & Vishton (1995), pp.84–95. / Ian P. Howard & Brian J. Rogers, Perceiving in Depth, Vol.2: Stereoscopic Vision (Oxford, 2012), ch.18 "Stereoacuity". / Gerald Westheimer (1979), "Cooperative neural processes involved in stereoscopic acuity," Experimental Brain Research 36:585–597. |

두 눈이 좌우로 떨어져 있어 같은 장면을 조금 다른 각도에서 본다. 주시점과 같은 깊이에 있는 점들(호롭터)은 두 망막의 대응 지점에 맺히고, 그보다 앞이나 뒤의 점은 어긋난다. 이 어긋남이 시차다. 소각 근사에서 깊이차 Δz가 만드는 시차각은 η ≈ IPD·Δz/z²이다. 여기서 핵심은 분모의 z² — 거리가 두 배 멀어지면 같은 깊이차가 만드는 시차는 네 분의 일로 줄어든다. 감도가 거리 제곱으로 무너진다는 뜻이고, 이것이 스테레오시가 근거리 전문 단서인 이유다. 반대로 개인공간에서는 압도적으로 정밀하다. 또 하나의 한계는 융합이다. 시차가 파눔 융합역을 넘으면 두 상이 하나로 합쳐지지 않고 복시로 갈라지는데, 중심와의 융합역은 대략 6분각에 불과하다(주변부에서는 훨씬 넓어진다). 시차만으로는 절대 거리를 알 수 없고, 눈 사이 거리(IPD)와 수렴 각도를 알아야 비율이 거리로 환산된다.

### 수렴(vergence) — 절대 거리를 알려주는 드문 단서
| 항목 | 내용 |
| --- | --- |
| 수치 | IPD 63mm 기준 수렴각: 0.25m → 14.4도 / 0.5m → 7.2도 / 1m → 3.6도 / 2m → 1.8도 / 6m → 0.60도 / 무한대 → 0도. 유효 범위 약 0~2m(일부 연구는 1m 이내로 더 보수적). 감도 dθ/dz ∝ 1/z². 커팅·비시턴 순위에서 개인공간 중위권, 행동공간 이후 소멸. |
| 출처 | Cutting & Vishton (1995), pp.95–97. / James R. Tresilian, Mark Mon-Williams & Brian M. Kelly (1999), "Increasing confidence in vergence as a cue to distance," Proceedings of the Royal Society B 266:39–44. / Howard & Rogers, Perceiving in Depth, Vol.1, ch.25. |

가까운 것을 볼 때 두 눈은 안쪽으로 모이고 먼 것을 볼 때 평행해진다. 이 모임 각도 θ = 2·arctan(IPD/2z)는 망막 이미지가 아니라 안구 근육의 상태에서 나온다(외망막 정보, extraretinal). 그래서 이 단서는 드물게도 절대 거리를 준다 — 장면 안에 비교 대상이 없어도, 아는 물체가 없어도, 각도만으로 몇 미터인지 나온다. 문제는 감도다. dθ/dz가 1/z²에 비례하므로 멀어질수록 각도 변화가 급격히 사라진다. 1미터에서 2미터로 갈 때 수렴각은 3.6도에서 1.8도로 1.8도나 줄지만, 10미터에서 20미터로 갈 때는 0.36도에서 0.18도로 겨우 0.18도 줄어든다. 안구 위치 감각 자체의 잡음을 고려하면 실용 한계는 대략 2미터, 낙관적으로 잡아도 3~6미터다. 수렴과 조절은 신경적으로 교차 연결되어 있어(수렴성 조절 AC/A, 조절성 수렴 CA/C) 한쪽이 움직이면 다른 쪽이 따라간다.

### 조절(accommodation)과 흐림(blur) — 2미터에서 은퇴하는 단서
| 항목 | 내용 |
| --- | --- |
| 수치 | 초점심도 약 ±0.2~0.3D(동공 크기·판정 기준에 따라 변동). 유효 범위 약 0~2m. 디옵터 환산: 0.3m=3.33D, 0.5m=2.0D, 1m=1.0D, 2m=0.5D, 5m=0.2D, ∞=0D. 조절 진폭의 연령 감소(Duane 1912): 10세 약 14D, 20세 약 10D, 40세 약 4.5D, 50세 약 2D, 60세 약 1D 이하. 암소시 휴식 초점(dark focus) 약 1.5D(약 67cm). |
| 출처 | Alexander Duane (1912), "Normal values of the accommodation at all ages," JAMA 59:1010–1013. / Herschel W. Leibowitz & D. Alfred Owens (1975), "Anomalous myopias and the intermediate dark focus of accommodation," Science 189:646–648. / Robert T. Held, Emily A. Cooper & Martin S. Banks (2012), "Blur and disparity are complementary cues to depth," Current Biology 22:426–431. / Cutting & Vishton (199 |

수정체의 굴절력을 바꿔 상을 망막에 맺는 작용이 조절이고, 그 강도는 디옵터(D = 1/거리[m])로 잰다. 조절 상태는 수렴처럼 절대 거리 신호가 될 수 있지만 두 가지가 발목을 잡는다. 첫째는 초점심도다. 인간 눈의 초점심도는 대략 ±0.2~0.3디옵터로, 이 범위 안의 거리 차이는 흐림으로 전혀 구분되지 않는다. 그런데 디옵터는 거리의 역수이므로 먼 거리일수록 같은 디옵터 차이에 해당하는 거리 폭이 폭발적으로 넓어진다. 1미터(1.0D)와 2미터(0.5D)의 차이는 0.5디옵터지만, 2미터(0.5D)와 무한대(0D)의 차이도 0.5디옵터다. 다시 말해 2미터 너머는 조절에게 전부 같은 곳이다. 둘째는 노화다. 조절 진폭은 나이에 따라 거의 선형으로 붕괴해 50대에는 사실상 소진된다(노안). 흐림 자체는 부호가 모호해서 앞으로 틀렸는지 뒤로 틀렸는지 알려주지 않는데, 눈의 색수차와 비대칭 수차가 이 부호를 부분적으로 복원해 준다.

### 수렴-조절 충돌(VAC) — 증강현실이 몸에 남기는 청구서
| 항목 | 내용 |
| --- | --- |
| 수치 | 실용 요약치: 상면 기준 약 ±0.3디옵터 이내가 편안(원거리 시청일수록 여유가 넓고, 근거리일수록 좁으며 비대칭). 계산 예: 상면 2m(0.5D)에 ±0.3D를 적용하면 0.8D=1.25m ~ 0.2D=5m — 홀로렌즈의 권장 배치 범위와 정확히 일치한다. 같은 기기에서 30cm(3.33D) 앞에 물체를 띄우면 충돌이 2.83D에 달해 사용 불가 영역이다. 호프먼 등(2008)은 초점 단서를 올바르게 준 조건에서 스테레오 융합 시간이 단축되고 피로 보고가 감소함을 보였다. |
| 출처 | David M. Hoffman, Ahna R. Girshick, Kurt Akeley & Martin S. Banks (2008), "Vergence–accommodation conflicts hinder visual performance and cause visual fatigue," Journal of Vision 8(3):33. / Takashi Shibata, Joohwan Kim, David M. Hoffman & Martin S. Banks (2011), "The zone of comfort: Predicting visual discomfort with stereo displays," Journal of Vision 11(8):11. / Microsoft Mixed Reality 개발 문서(홀로렌 |

실세계에서는 수렴 거리와 조절 거리가 항상 같다. 손끝을 보면 눈은 손끝으로 모이고 초점도 손끝에 맞는다. 두 계통은 신경적으로 짝지어져 있어(AC/A, CA/C 교차 연결) 한쪽만 움직이는 일이 거의 없다. 스테레오 디스플레이는 이 짝을 강제로 분리한다. 수렴은 양안 시차가 지시하는 가상 거리를 따라가지만, 초점은 광학 상면 — 즉 하드웨어가 정한 고정 거리 — 에 묶인다. 두 회로가 서로 다른 값을 요구하며 싸우고, 그 대가가 눈 피로·두통·융합 지연·깊이 판단 왜곡이다. 중요한 점은 이 충돌의 크기를 미터가 아니라 디옵터로 재야 한다는 것이다. 초점면에서 멀어질수록 디옵터 차이가 비선형적으로 커지기 때문이다. 편안한 영역(zone of comfort)은 상면을 중심으로 한 디옵터 구간으로 정의되며, 그 바깥에 콘텐츠를 두면 사용 시간에 비례해 불편이 누적된다.

### 운동시차(motion parallax) — 한 눈으로도 깊이를 만드는 방법
| 항목 | 내용 |
| --- | --- |
| 수치 | 유효 범위: 0~30m에서 강함, 그 너머 급감(커팅·비시턴 기준 행동공간 상위권). 관찰자 측방 속도 1m/s일 때 각속도: 1m 거리 → 57도/s, 10m → 5.7도/s, 100m → 0.57도/s. 인간의 느린 움직임 검출 역치는 대략 0.1~0.3도/s. 정지 자세에서도 자연 체간 동요로 머리가 좌우 1~2cm 흔들리며, 이것만으로도 근거리 시차가 발생한다. |
| 출처 | Brian J. Rogers & Maureen Graham (1979), "Motion parallax as an independent cue for depth perception," Perception 8:125–134. / Mark Nawrot (2003), "Eye movements provide the extra-retinal signal required for the perception of depth from motion parallax," Vision Research 43:1553–1562. / Cutting & Vishton (1995), pp.86–90. |

관찰자가 옆으로 움직이면 가까운 물체는 빠르게, 먼 물체는 느리게 반대 방향으로 흐른다. 측방 이동 속도 v일 때 거리 z에 있는 점의 각속도는 대략 ω ≈ v/z이다. 기하학적으로 이것은 양안시차와 같은 삼각측량이되, 기선이 두 눈 사이 거리가 아니라 머리가 움직인 거리라는 점만 다르다. 그래서 잠재력이 더 크다 — 6.3센티미터만 움직여도 양안과 동등하고, 한 걸음 옆으로 가면 기선이 수십 센티미터가 되어 훨씬 먼 거리까지 유효해진다. 다만 조건이 붙는다. 망막 위 움직임만으로는 물체가 움직인 것인지 내가 움직인 것인지 알 수 없으므로, 자기 운동 정보(안구 운동의 원심성 복사, 전정 신호, 목 고유수용감각)가 결합되어야 부호와 절대 스케일이 확정된다. 로저스와 그레이엄은 시차 이외의 모든 단서를 제거한 자극에서도 사람이 양안시차에 필적하는 깊이를 본다는 것을 보였다.

### 시야 내 높이 / 각도 하강(height in the visual field, angular declination)
| 항목 | 내용 |
| --- | --- |
| 수치 | 눈높이 1.6m 기준 하강각: 2m → 38.7도 / 5m → 17.7도 / 10m → 9.1도 / 30m → 3.05도 / 100m → 0.92도. 감도 dγ/dd = −h/d². 유효 범위: 약 2m부터 지평선까지, 행동공간·조망공간에서 2위. 지면 접촉이 없으면 정보량 0. |
| 출처 | Teng Leng Ooi, Bing Wu & Zijiang J. He (2001), "Distance determined by the angular declination below the horizon," Nature 414:197–200. / H. A. Sedgwick (1986), "Space perception," in Boff, Kaufman & Thomas (eds.), Handbook of Perception and Human Performance, Vol.1, ch.21. / Cutting & Vishton (1995), pp.90–93. |

지면에 놓인 물체는 멀수록 시야에서 높은 곳, 즉 지평선에 가까운 곳에 보인다. 눈높이 h, 거리 d일 때 시선의 하강각은 γ = arctan(h/d)이다. 이 단서가 강력한 이유는 상수 h가 크기 때문이다 — 서 있는 사람의 눈높이 1.6미터는 양안 기선 6.3센티미터의 25배이므로, 같은 1/거리제곱 감도 저하를 겪더라도 절대 성능이 훨씬 오래 유지된다. 그래서 커팅·비시턴의 분석에서 행동공간과 조망공간 모두 가림 다음가는 2위를 차지한다. 또 이 단서는 절대 거리를 준다 — 눈높이를 알면 하강각에서 바로 미터가 나온다. 전제 조건은 두 가지다. 물체가 지면에 접촉해 있어야 하고, 관찰자가 자신의 눈높이와 시선 방향(따라서 지각된 눈 수준)을 알아야 한다. 우이·우·허는 프리즘으로 지각된 눈 수준을 조작하면 거리 판단이 예측대로 어긋남을 보여 이 메커니즘을 직접 입증했다.

### 상대 크기와 친숙한 크기(relative size, familiar size)
| 항목 | 내용 |
| --- | --- |
| 수치 | 크기 변별 웨버 비 약 2~3% → 거리 비를 약 2~3% 분해능으로 판별. 시각 환산: 키 1.7m 사람이 10m 앞 → 9.7도, 100m 앞 → 0.97도, 1km 앞 → 0.097도(약 5.8분각, 여전히 시력 한계 위). 유효 범위: 전 거리대, 조망공간에서 상대적 비중 상승(커팅·비시턴 순위 조망공간 3위). |
| 출처 | William H. Ittelson (1951), "Size as a cue to distance: Static localization," American Journal of Psychology 64:54–67. / Walter C. Gogel (1969), "The sensing of retinal size," Vision Research 9:1079–1094. / Cutting & Vishton (1995), pp.93–95. |

물체의 시각(視角)은 실제 크기 S와 거리 z에 대해 α ≈ S/z로 줄어든다. 같은 크기임을 알 수 있는 물체가 둘 있으면 시각의 비가 곧 거리 비의 역수가 되므로, 어느 쪽이 얼마나 더 먼지가 나온다 — 이것이 상대 크기다. 다만 상대적이어서 절대 거리는 나오지 않는다. 절대 거리를 얻으려면 물체의 실제 크기를 알아야 하고(친숙한 크기), 그러면 z = S/α로 거리가 확정된다. 이텔슨은 같은 각크기의 트럼프 카드를 크기만 바꿔 보여주면 지각 거리가 바뀐다는 고전적 실험으로 친숙한 크기의 효력을 보였다. 이 단서의 장점은 거리 의존성이 1/z로 완만하다는 것이고(시차·수렴의 1/z²보다 훨씬 느리게 무너진다), 단점은 세상 지식에 의존한다는 것이다. 처음 보는 물체에는 무력하고, 크기 가정이 틀리면 거리 판단이 그대로 틀린다. 크기-거리 불변 가설(S/z 일정)은 달 착시 같은 현상의 해석 틀이기도 하다.

### 결 기울기(texture gradient)
| 항목 | 내용 |
| --- | --- |
| 수치 | 지면 위 균질 타일 기준: 요소 가로 시각 ∝ 1/z, 세로 시각 ∝ 1/z², 종횡비 ∝ 1/z, 면밀도 ∝ 1/z². 경사각 판단은 체계적으로 실제보다 완만하게(혹은 특정 조건에서 과대하게) 편향되며 오차가 흔히 10도 이상. 유효 범위: 지면이 보이는 전 구간, 그러나 상대적 비중은 9단서 중 하위. |
| 출처 | James J. Gibson (1950), The Perception of the Visual World, Houghton Mifflin, ch.5–6. / James E. Cutting & Robert T. Millard (1984), "Three gradients and the perception of flat and curved surfaces," Journal of Experimental Psychology: General 113:198–216. / David C. Knill (1998), Vision Research 38:1683–1711. |

깁슨이 지각 이론의 중심에 놓았던 단서다. 자갈밭·잔디·타일처럼 통계적으로 균질한 표면을 비스듬히 보면 표면 요소의 상이 거리에 따라 체계적으로 변한다. 변화는 세 성분으로 분해된다. 첫째 크기 기울기 — 요소의 가로 시각이 1/z로 줄어든다. 둘째 밀도 기울기 — 단위 면적당 요소 수가 1/z²로 늘어난다. 셋째 압축(foreshortening) — 지면을 비스듬히 보므로 세로가 가로보다 더 줄어들어 요소의 종횡비가 1/z에 비례해 납작해진다. 이 세 성분은 원리상 독립적이며, 커팅과 밀러드는 이들을 분리해 제시하는 실험으로 사람이 평면 경사에는 압축을, 곡면 지각에는 크기 기울기를 주로 쓴다는 것을 밝혔다. 결 기울기의 약점은 정밀도다. 표면이 정말 균질하다는 가정에 의존하는데 현실의 표면은 대개 그렇지 않고, 결과적으로 경사 판단 오차가 크다. 커팅·비시턴의 순위에서도 하위권에 머문다.

### 선 원근(linear perspective)
| 항목 | 내용 |
| --- | --- |
| 수치 | 투영 기하: 화면 상 좌표 x = f·X/Z, 평행선 다발은 방향 벡터 d에 대해 소실점 f·d로 수렴. 지평선은 눈높이와 같은 높이의 상면 선. 인간 양안 수평 시야 약 200도, 고해상 중심시는 약 2도. 유효 범위: 직선 구조가 있는 모든 거리대. 렌더 시야각 불일치의 효과는 곧바로 깊이 왜곡으로 나타나며, 렌더 FOV가 실제보다 크면 장면이 앞뒤로 늘어나 보인다. |
| 출처 | Leon Battista Alberti, De pictura (1435) — 원근 작도법의 최초 체계화. / H. A. Sedgwick (1986), "Space perception," in Boff, Kaufman & Thomas (eds.), Handbook of Perception and Human Performance, Vol.1, ch.21. / Cutting & Vishton (1995), pp.99–101. |

실제로 평행한 직선들이 상에서는 한 소실점으로 수렴한다. 엄밀히 말해 선 원근은 독립 단서라기보다 결 기울기와 상대 크기가 장면에 직선 구조가 있을 때 취하는 특수한 형태다. 그러나 정보량은 크다. 소실점은 그 선들의 3차원 방향을 알려주고, 수평면의 소실선인 지평선은 관찰자의 눈높이를 알려주며, 지평선이 있으면 앞서 본 각도 하강 단서가 곧바로 작동한다. 대가는 가정 의존성이다. 선 원근을 쓰려면 "이 선들은 실제로 평행하다", "이 모서리는 직각이다"라는 강한 사전 가정을 넣어야 한다. 에임스 방(Ames room)은 바로 이 가정을 공격해 만든 착시로, 사다리꼴 방을 직육면체로 가정하는 순간 그 안의 사람 크기가 두 배로 달라 보인다. 사전 가정이 강한 단서는 잘 맞을 때는 강력하고 틀릴 때는 크게 틀린다.

### 대기 원근(aerial perspective) — 공기가 쓰는 거리계
| 항목 | 내용 |
| --- | --- |
| 수치 | 코슈미더: C = C₀·e^(−βd), V = 3.912/β(대비역치 2% 기준). 맑은 날 V=20km → β=1.96×10⁻⁴/m: 100m에서 대비 1.9% 감소, 1km에서 17.8%, 10km에서 85.9% 감소. 짙은 안개 V=200m → β=1.96×10⁻²/m: 50m에서 대비 62% 감소. 유효 범위: 실질적으로 수백 미터 이상, 조망공간에서 3~4위. |
| 출처 | Harald Koschmieder (1924), "Theorie der horizontalen Sichtweite," Beiträge zur Physik der freien Atmosphäre 12:33–53. / Glenn A. Fry, C. S. Bridgman & V. J. Ellerbrock (1949), "The effects of atmospheric scattering upon the appearance of a dark object," American Journal of Optometry 26:9–19. / Cutting & Vishton (1995), pp.101–103. |

대기 중 분자와 에어로졸이 빛을 산란시켜, 멀리 있는 물체일수록 대비가 낮고 밝으며 푸르스름해진다. 코슈미더의 법칙은 거리 d를 지난 물체의 대비가 C = C₀·e^(−βd)로 감쇠한다고 기술한다(β는 소광계수). 기상 시정 V는 대비가 인간의 역치 2퍼센트까지 떨어지는 거리로 정의되며 V = 3.912/β이다. 이 지수 법칙의 함의가 중요하다 — 맑은 날에는 β가 너무 작아서 수십 미터 안에서는 감쇠가 측정 불가 수준이다. 즉 대기 원근은 조망공간 전용 단서이며, 커팅·비시턴의 분석에서도 유일하게 멀어질수록 상대적 유용성이 올라가는 단서다. 반대로 안개나 미세먼지가 짙으면 β가 백 배 커져 근거리에서도 강력하게 작동하고, 이 때문에 안개 속에서 거리 판단이 체계적으로 왜곡된다(멀게 보임).

### 그림자와 음영(cast shadow, shading)
| 항목 | 내용 |
| --- | --- |
| 수치 | 태양의 각지름 약 0.53도(0.00925 rad) → 지면에서 1m 떠 있는 물체의 그림자 가장자리 번짐 폭 약 9.3mm, 10cm 떠 있으면 약 0.9mm. 커스틴 등의 자극에서 그림자 궤적 조작만으로 지각된 3차원 궤적이 수직 상승 대 후방 이동으로 전환. 그림자는 단서 강도로는 약한 편이지만, 공중에 뜬 물체처럼 지면 접촉 단서가 없는 경우 사실상 유일한 단서가 된다. |
| 출처 | Daniel Kersten, Pascal Mamassian & David C. Knill (1997), "Moving cast shadows induce apparent motion in depth," Perception 26:171–192. / Pascal Mamassian, David C. Knill & Daniel Kersten (1998), "The perception of cast shadows," Trends in Cognitive Sciences 2:288–295. / V. S. Ramachandran (1988), "Perception of shape from shading," Nature 331:163–166. |

물체가 지면에 드리우는 그림자는 물체와 지면의 접촉 여부, 그리고 접촉하지 않는다면 얼마나 떠 있는지를 알려준다. 커스틴 등의 이른바 "상자 속 공" 실험이 이 단서의 힘을 극적으로 보여준다 — 공의 상 자체는 전혀 건드리지 않고 그림자의 궤적만 대각선으로 바꾸면, 관찰자는 같은 영상에서 공이 수평으로 굴러가는 대신 위로 떠오르며 뒤로 물러나는 것을 본다. 즉 그림자가 물체의 크기·위치 단서를 이긴다. 음영(shading)은 별개로 표면의 곡률과 볼록·오목을 알려주지만 조명 방향이 모호해 그 자체로는 양의적이며, 뇌는 "빛은 위에서 온다"는 사전 가정으로 이 모호성을 해소한다(라마찬드란). 그림자의 가장자리 번짐(반그림자, penumbra)은 광원의 각크기와 물체-지면 간격의 곱이므로, 추가로 높이 정보를 담는다.

### 커팅·비시턴의 통합 지도 — 세 개의 공간과 단서 순위
| 항목 | 내용 |
| --- | --- |
| 수치 | 구역 경계: 개인공간 약 0~2m, 행동공간 약 2~30m, 조망공간 30m 이상. 구역별 순위 — 개인공간: 가림 > 양안시차 > 상대 크기 > 수렴·조절 > 운동시차. 행동공간: 가림 > 시야 내 높이 > 양안시차 > 운동시차 > 상대 크기. 조망공간: 가림 > 시야 내 높이 > 상대 크기 > 대기 원근. 조절·수렴은 약 2m에서 실질 소멸, 양안시차는 수백 미터까지 느리게 감쇠, 대기 원근은 수백 미터 이후에야 유의미해진다. |
| 출처 | James E. Cutting & Peter M. Vishton (1995), "Perceiving layout and knowing distances: The integration, relative potency, and contextual use of different information about depth," in W. Epstein & S. Rogers (eds.), Perception of Space and Motion (Handbook of Perception and Cognition, Vol.5), Academic Press, pp.69–117 — 특히 깊이 대비 정의와 Figures 3–5. / James E. Cutting (1997), "How the eye measures realit |

1995년 커팅과 비시턴의 기여는 새 단서를 발견한 것이 아니라 아홉 단서를 하나의 공통 척도로 비교 가능하게 만든 것이다. 그들은 각 단서에 대해 "깊이 대비(depth contrast)", 즉 그 단서만으로 판별 가능한 최소 상대 깊이차 \|Δz\|/z를 정의하고, 이를 관찰 거리에 대해 로그-로그 평면에 겹쳐 그렸다. 그러면 단서마다 다른 기울기의 직선이 나온다. 가림은 거의 수평선(거리와 무관), 양안시차·수렴·각도 하강은 1/z² 계열로 가파르게 악화, 상대 크기와 결 기울기는 1/z 계열로 완만하게 악화, 대기 원근은 홀로 오른쪽 아래로 향한다(멀수록 좋아진다). 이 직선들이 서로 교차하는 지점들이 자연스럽게 공간을 세 구역으로 나눈다. 개인공간은 팔이 닿는 약 2미터까지, 행동공간은 즉시 걸어가거나 물건을 던질 수 있는 약 30미터까지, 그 너머가 조망공간이다. 구역이 바뀌면 상위 단서의 순서가 바뀐다는 것이 결론이다.

### 단서 충돌의 해소 — 신뢰도 가중 평균이냐 거부(veto)냐
| 항목 | 내용 |
| --- | --- |
| 수치 | MLE 결합: 두 단서의 σ가 같으면 통합 σ는 1/√2 ≈ 0.71배(정밀도 약 41% 향상). 에른스트·뱅크스(2002)는 시각-촉각 크기 판단에서 실측 통합 분산이 MLE 예측과 일치함을 보였다. 힐리스 등(2002)은 시차-결 조합에서 단일 단서 정보가 강제 융합으로 소실됨을 보였다. 파눔 융합역(약 6분각)을 넘는 시차-가림 충돌에서는 평균이 아니라 기각 또는 지각 분열이 일어난다. |
| 출처 | Michael S. Landy, Laurence T. Maloney, Elizabeth B. Johnston & Mark Young (1995), "Measurement and modeling of depth cue combination: In defense of weak fusion," Vision Research 35:389–412. / Marc O. Ernst & Martin S. Banks (2002), "Humans integrate visual and haptic information in a statistically optimal fashion," Nature 415:429–433. / James M. Hillis, Marc O. Ernst, Martin S. Banks & Michael S.  |

여러 단서가 각기 다른 깊이를 주장할 때 뇌는 두 가지 방식 중 하나를 쓴다. 불일치가 작으면 신뢰도 가중 평균을 취한다. 각 단서의 추정치를 zᵢ, 그 분산을 σᵢ²라 할 때 통합 추정치는 ẑ = Σwᵢzᵢ이고 가중치는 wᵢ = (1/σᵢ²)/Σ(1/σⱼ²)이며, 통합 분산은 1/σ² = Σ1/σᵢ²로 줄어든다. 이것이 최대우도추정(MLE)이며, 단서가 늘수록 정밀도가 올라가는 이유다. 결정적으로 가중치는 고정된 것이 아니라 상황에 따라 재계산된다 — 거리가 멀어지면 시차의 σ가 커지므로 그 가중치가 자동으로 떨어진다. 그러나 불일치가 크면 평균이 깨지고 거부(veto)가 일어난다. 한 단서가 다른 단서를 완전히 기각해 버리는 것이다. 가림이 전형적인 거부 단서로, 시차가 가상 물체를 뒤에 놓으라고 말해도 가림이 앞이라고 말하면 대개 가림이 이긴다(때로는 두 해석이 모두 무너져 물체가 종잇장처럼 납작해 보이기도 한다). 한편 같은 감각 양상 안의 단서들(시차와 결)은 강제로 융합되어 개별 단서에 대한 접근 자체가 사라지지만, 감각 양상이 다르면(시각과 촉각) 개별 접근이 남는다.

### 증강현실에서 실제로 관측되는 것 — 거리 압축과 단서별 재현 난이도
| 항목 | 내용 |
| --- | --- |
| 수치 | 레너 등(2013) 메타 리뷰: 헤드셋 가상현실에서 지각 거리 = 의도 거리의 평균 약 74%(연구 간 대략 60~90% 분포). 지연 예산: 총 motion-to-photon 지연 20밀리초 이하가 통상 권장치이며, 사람의 지연 검출 역치는 연구에 따라 약 3~17밀리초로 보고된다. 정합 오차 환산: 머리 회전 100도/s에 지연 10밀리초 → 각오차 1.0도, 팔 길이 0.6m에서 약 10.5밀리미터 어긋남. 홀로렌즈 2 기준 권장 콘텐츠 배치 1.25~5m, 근접 클리핑 0.85m — 초점면 2m에 ±0.3디옵터 편안 영역을 적용한 값과 일치한다. |
| 출처 | Rebekka S. Renner, Boris M. Velichkovsky & Jens R. Helmert (2013), "The perception of egocentric distances in virtual environments — A review," ACM Computing Surveys 45(2), Article 23. / J. Edward Swan II, Adam Jones, Eric Kolstad, Mark A. Livingston & Harvey S. Smallman (2007), "Egocentric depth judgments in optical, see-through augmented reality," IEEE Transactions on Visualization and Computer  |

이론이 예측하는 왜곡은 실측으로 확인된다. 머리 착용 디스플레이에서 사람은 거리를 체계적으로 과소평가한다. 레너 등이 수십 편의 연구를 종합한 결과, 가상현실 헤드셋에서 판단된 거리는 의도한 거리의 평균 약 74퍼센트였다. 광학투과 증강현실에서는 실세계가 그대로 보이므로 압축이 덜하지만, 스완 등의 측정에서는 근거리(약 0.3~0.5m)에서 과대평가, 중거리에서 과소평가로 전환되는 비단조 패턴이 반복 관측되었다. 원인은 단일하지 않다 — 좁은 시야각(주변 시야의 광류·지면 단서 손실), 고정 초점면, 부정확한 IPD, 렌더 시야각과 광학 시야각의 불일치, 기기의 무게와 관성으로 인한 자세·머리 움직임 변화가 모두 기여한다. 이를 단서별 재현 난이도로 정리하면 세 등급이 나온다. 쉬움: 선 원근, 상대 크기, 결 기울기, 양안시차, 수렴 — 올바른 투영 행렬과 정확한 모델 스케일만 있으면 물리적으로 정확히 나온다. 중간: 운동시차(추적 정확도와 지연에 종속), 그림자(실세계 조명 추정 필요), 시야 내 높이(지면 평면 추정 필요). 어려움: 가림(광학투과에서는 원리적으로 불가에 가까움), 조절(광학 재설계 없이는 불가), 대기 원근의 대비 저하(가산 합성에서는 원리적으로 불가).

#### 검증에서 잡힌 정정
- [치명·원리 역전] VAC 항목 '원거리 시청일수록 여유가 넓고, 근거리일수록 좁으며 비대칭'은 인용한 Shibata et al.(2011)과 정반대. 논문 원문(PMC3369815, Discussion/Figure 17): "The slopes of the upper and lower lines are slightly greater than 1 and the zone is narrower at long distances (small dioptric values) than at short distances (large dioptric values)." 실험1 결과도 "a 1.2-D crossed disparity conflict is relatively more uncomfortable at far viewing distance than at near". 즉 디옵터 기준 편안 영역은 원거리에서 좁고 근거리에서 넓다(다만 근거리는 총 피로가 큼). 또한 논문의 추정치는 '±0.3D'가
- [치명·수치] '홀로렌즈 2 … 근접 클리핑 0.85m'는 마이크로소프트 공식 지침과 불일치. learn.microsoft.com/windows/mixed-reality/design/comfort 원문: "we recommend starting to fade out content at 40 cm and placing a rendering clipping plane at 30 cm", "we recommend against ever presenting holograms closer than 40 cm". 0.85m는 구 Windows Holographic API의 기본 근평면 값이지 편안성 권고치가 아니다. (같은 문서에서 '권장 배치 1.25~5m'와 '초점거리 약 2.0m'는 확인됨 — 단 이 문서는 1세대·2세대 공통 지침이며 1m 미만 콘텐츠도 'depth budget' 조건으로 허용하므로, '±0.3D와 정확히 일치'는 사후 합리화다.)
- [수치·지수 오류] 결 기울기 '면밀도 ∝ 1/z²'(본문 정의: 단위 면적당 요소 수)는 방향과 지수가 모두 틀렸다. 눈높이 h의 지면에서 거리 z의 면적요소가 만드는 입체각은 ≈ dA·h/z³ 이므로 요소 1개의 상 면적 ∝ 1/z³, 따라서 상에서의 요소 밀도 ∝ z³/h — 거리가 멀어질수록 '증가'한다(지평선 쪽으로 결이 촘촘해지는 현상 자체). 같은 항목이 제시한 가로 ∝1/z·세로 ∝1/z²와도 산술적으로 모순(면적=1/z³ ⇒ 밀도=z³).
- [단위·정의 오류] '두 단서의 σ가 같으면 통합 σ는 1/√2 ≈ 0.71배(정밀도 약 41% 향상)'. σ 계산은 맞지만 41%는 1/σ의 증가율이다. 인용된 MLE 문헌(Ernst & Banks 2002; Landy et al. 1995)은 정밀도·신뢰도를 1/σ²로 정의하므로 동일 단서 2개의 정밀도는 정확히 2배(+100%)이고, 표준편차는 29% 감소다. '정밀도 41% 향상'은 지표를 바꿔 쓴 오기.
- [기준 혼동] 대기 원근 '기상 시정 V는 대비가 인간의 역치 2퍼센트까지 떨어지는 거리로 정의되며 V=3.912/β'. 3.912=ln(1/0.02)는 코슈미더의 2% 시각 역치 규약이고, 기상 관측의 시정(WMO 기상광학거리 MOR)은 투과율 5% 기준이므로 V=ln(1/0.05)/β≈2.996/β다. 따라서 보도된 '맑은 날 시정 20km'에 3.912를 적용하면 β를 약 30% 과대추정(1.96×10⁻⁴ 대 1.50×10⁻⁴ /m)하고, 뒤따르는 대비감쇠 수치가 전부 과장된다(10km: 85.9% → 약 77.7%, 1km: 17.8% → 약 13.9%).
- [출처 권 번호] Renner, Velichkovsky & Helmert (2013)는 ACM Computing Surveys **46**(2), Article 23 (Crossref: v46 i2 p1-40; OpenAlex 동일). 본문의 '45(2)'는 틀림. 덧붙여 이 논문은 '메타 리뷰'가 아니라 서술형 문헌 개관이고, 74%는 초록 원문 "a mean estimation of egocentric distances in virtual environments of about 74% of the modeled distances" — 헤드셋 VR 한정이 아니라 가상환경 전반의 평균이다.
- [출처 제목·면수] Fry, Bridgman & Ellerbrock (1949)의 실제 제목은 "The effects of atmospheric scattering **on binocular depth perception**", Am. J. Optometry & Arch. AAO **26(1):9–15** (Crossref, 저자 3인 일치). 본문이 붙인 제목 '…upon the appearance of a dark object'는 Fry의 1947년 JOSA 논문(J. Opt. Soc. Am. 37(8):635, "…Against a Sky Background")의 것이고, 면수 '9–19'도 틀렸다(9–15).
- [출처 권·장 오류] 'Howard & Rogers, Perceiving in Depth, Vol.1, ch.25'는 존재하지 않는다. Crossref 장 레코드로 확인: Vol.1(Basic Mechanisms)은 총 10장(제9장 image formation and accommodation pp.435–474, 제10장 Vergence eye movements pp.475–548)뿐이고, 제25장 "Depth from accommodation and vergence"는 **Vol.3(Other Mechanisms of Depth Perception) pp.1–14**이다(Vol.2=제11~24장). 같은 근거로 'Vol.2 ch.18 Stereoacuity'는 맞다(Vol.2의 8번째 장 "Stereoscopic acuity" pp.287–362 = 제18장).
- [출처 장 제목 허위] Palmer, Vision Science: Photons to Phenomenology (1999)의 제5장 제목은 "**Perceiving Surfaces Oriented in Depth**"다(하버드 HOLLIS MARC 505 목차: … Processing image structure -- Perceiving surfaces oriented in depth -- Organizing objects and scenes …). 본문의 ch.5 "Perceiving Depth and Shape"라는 제목은 이 책에 없다.
- [출처 면수] Ellis & Menges (1998), Human Factors 40(3)은 **415–431**이다(PubMed 11536894). 본문의 '415–434'는 틀림.
- [출처 내용 오기] '커팅·비시턴의 9단서'에 결 기울기(texture gradient)와 선 원근(linear perspective)을 포함시키고 순위를 매긴 것은 오류. C&V(1995)의 9개는 occlusion, relative size, **relative density**, height in the visual field, aerial perspective, binocular disparity, **accommodation**, **convergence**, **motion perspective**이며(C&V를 인용한 Sci Rep 2021, PMC8277830의 요약과 일치), 결 기울기·선 원근은 상대 크기/상대 밀도의 특수형으로 흡수돼 별 항목이 아니다. 반대로 9단서에 실제로 포함된 '상대 밀도'가 본문 목록에서 빠졌고, '수렴·조절'을 한 항목으로 묶은 것도 원문(각각 1개)과 다르다. C&V의 용어도 motion parallax가 아니라 motion perspe
- [자기모순 산술] '초시력 역치 약 5초각 — 수용체 간격보다 열 배 미세'. 같은 문단이 제시한 중심와 원추 간격 0.5분각=30초각을 쓰면 30/5=6배다(열 배가 되려면 역치 3초각). vernier 역치 통상 보고치 5~10초각을 감안하면 배율은 3~6배.
- [근사식 오용] 시야 내 높이 '감도 dγ/dd = −h/d²'는 원거리 근사다. γ=arctan(h/d)의 정확한 미분은 −h/(d²+h²). 이 단서의 유효 하한으로 본문이 제시한 d=2m, h=1.6m에서 근사값 0.400 rad/m 대 정확값 0.244 rad/m — 감도를 64% 과대평가한다. 같은 항목의 각도 표는 정확한 arctan으로 계산돼 있어 내부 불일치.
- [공식·차원 오류] 선 원근 '평행선 다발은 방향 벡터 d에 대해 소실점 f·d로 수렴'. 방향 d=(dx,dy,dz)의 소실점은 상 좌표 (f·dx/dz, f·dy/dz)이며, dz로 나누는 사영이 빠지면 3차원 벡터에 f를 곱한 값이 되어 상 좌표가 아니다. 또 dz=0(상면에 평행한 방향)에서는 유한 소실점이 존재하지 않는다는 조건도 누락.
- [개념 오류] '광수용체 1억 2천만+600만 → 축삭 100만, 정보 압축비 약 100:1'. 본인 숫자로는 126:1이며(반올림은 무해), 더 큰 문제는 이 단일 비율을 같은 문단이 곧바로 인용하는 중심와에 적용할 수 없다는 점이다. 중심와에서는 원추 1개가 midget 신경절세포 약 2개로 이어져 사실상 1:2 '확장'이고, 100:1급 수렴은 간상세포·주변시의 성질이다. 따라서 '압축비 100:1'과 '중심와 0.5분각 표본화'를 인과로 연결하면 틀린 서술이 된다.
- [역치 혼동] '파눔 융합역(약 6분각)을 넘는 시차-가림 충돌에서는 평균이 아니라 기각 또는 지각 분열'. 파눔역은 이중상(diplopia) 한계이고 단서 충돌의 veto 기준이 아니다. 융합역을 넘어도 정성적(qualitative) 스테레옵시스는 수 도(degree) 단위 시차까지 유지되며, 파눔역 자체가 자극의 공간주파수·크기·노출시간에 따라 수 분각~수십 분각으로 변해 '약 6분각' 고정값으로 쓸 수 없다. Landy et al.(1995)의 robust fusion/veto 모형도 파눔역으로 매개변수화되지 않는다.
- [기하 조건 누락] 그림자 반영 폭 '1m 부양 → 약 9.3mm'는 태양이 천정에 있을 때(광선이 지면에 수직)만 성립한다. 태양 고도 ε에서 지면 위 반영 폭은 약 1/sin ε 배로 늘어나 ε=40°이면 약 14mm, ε=20°이면 약 27mm가 된다. 또 기준 거리는 '물체 높이'가 아니라 '물체 가장자리→그림자'까지의 광선 경로 길이다. 태양 각지름도 0.53°는 평균이고 근·원일점에서 0.524~0.542°로 변한다.
- [역치 모집단 혼용] 양안시차 표(0.5m 0.19mm / 2m 3.1mm / 10m 7.7cm / 30m 0.69m / 100m 7.7m)는 최적 실험실 조건 10초각을 쓴 값인데, 같은 항목이 두 줄 위에서 제시한 '임상 정상 20~40초각'을 넣으면 같은 식이 2~4배 나쁜 값을 준다(10m에서 15~31cm, 100m에서 15~31m). 즉 표의 값은 '판별 가능한 최소 깊이차'의 일반값이 아니라 상한 성능이며, 이 값을 그대로 쓰면 '양안시차는 수백 미터까지 느리게 감쇠'라는 같은 항목의 서술과도 충돌한다.
- [지표 오용] 가림 '판정 역치 \|Δz\|/z ≈ 0'. 가림은 순서(ordinal) 정보만 주므로 \|Δz\|/z라는 비율 역치가 정의되지 않는다. 커팅·비시턴의 깊이 대비 도표에서도 가림은 0이 아니라 '가정된 최소 순서 판별값'에서 전 거리대에 걸쳐 수평선으로 그려진다. 또 '유효 거리 범위 0m~무한대'의 하한 0m는 윤곽이 겹치는 두 물체가 상에 맺혀야 성립하는 단서의 조건상 의미가 없다.
- [값 대조 필요·의심] Duane(1912) 조절진폭의 '20세 약 10D, 40세 약 4.5D'는 통상 재현되는 Duane 평균곡선(10세 약 14D, 20세 약 11D, 30세 약 9D, 40세 약 6D, 50세 약 2D, 60세 약 1D)보다 낮아, 평균이 아니라 하한(최소) 곡선 값에 가깝다. 인용 서지 자체는 확인됨(Crossref: JAMA LIX(12):1010, 1912) — 원표의 평균/최대/최소 세 곡선 중 어느 것을 쓴 것인지 명시하거나 값을 교정해야 한다.
- [출처 절 번호 의심] 'Helmholtz, Treatise on Physiological Optics, Vol.3, §26'을 가림·T자 접합의 근거로 든 것은 절 지정이 어긋날 가능성이 높다. Southall 번역본 Vol.2가 §24 Contrast·§25 Various Subjective Phenomena로 끝나는 것을 원문(archive.org helmholtzs-treatise-on-physiological-optics-vol-2 전문)에서 확인했고, 따라서 Vol.3은 제3부 'The Perceptions of Vision'의 서론격인 §26(지각 일반론·무의식적 추론)으로 시작한다. 단안 깊이 단서로서의 가림 논의는 그 뒤의 깊이 지각 절에 있으므로 §26 지정은 재확인 필요.
- [서술 미지정] 선 원근 '렌더 FOV가 실제보다 크면 장면이 앞뒤로 늘어나 보인다'는 어느 FOV를 고정하는지, 관찰자의 부분 보정을 포함하는지에 따라 부호가 달라지는 서술이다. 실측 문헌은 축소(geometric FOV>display FOV) 조건에서 '지각 거리 증가'를 보고하는 쪽이며, '깊이 방향 순수 신축'으로 단정할 근거는 제시된 출처(Alberti 1435, Sedgwick 1986, C&V)에 없다.
- 결 기울기: '면밀도 ∝ 1/z²'는 틀렸다. 같은 문장의 가로 ∝1/z, 세로 ∝1/z²를 받으면 요소의 상 면적 ∝1/z³이므로 상에서의 요소 면밀도는 ∝z³(정면 평면은 ∝z²)로 거리와 함께 '증가'한다. 1/z²는 부호(추세)와 지수가 모두 틀렸고, 멀수록 결이 듬성해진다는 정반대 결론을 함의한다.
- 양안시차: '주시점과 같은 깊이에 있는 점들(호롭터)'은 호롭터의 정의가 아니다. 호롭터=대응 망막점에 맺히는 점들의 자취 = 이론적으로 주시점과 두 눈 절점을 지나는 비트-뮐러 원(+수직 Prévost–Burckhardt 선), 경험적으로는 근거리에서 더 편평(헤링-힐레브란트 편차), 편심 주시에서는 뒤틀린 3차 곡선. 주시점과 같은 깊이의 정면 평면은 0이 아닌 시차를 갖는다.
- 단서 충돌: '파눔 융합역(약 6분각)을 넘는 시차-가림 충돌에서는 기각 또는 지각 분열'은 원리 혼동. 파눔 융합역은 양안 단일시(이중상 개시) 한계로, 단서 간 가중평균/거부를 가르는 기준이 아니다. 시차는 파눔 영역을 넘어(이중상 상태, 수 도 단위까지) 정성적 깊이를 계속 제공하며, 인용된 Nakayama 등도 6분각 경계를 제시하지 않는다.
- 조절/흐림: '유효 범위 약 0~2m', '2미터에서 은퇴하는 단서'는 망막 흐림에까지 적용되지 않는다. 같은 항목이 인용한 Held, Cooper & Banks (2012, Current Biology 22:426–431)의 결론은 흐림과 시차가 상보적이며 시차가 약해지는 원거리·대규모 장면에서 흐림의 상대 기여가 커진다는 것이다. 외망막 조절 신호(≈2m 한계)와 망막 흐림 단서를 한 범주로 묶은 것이 오류.
- 증강현실: '홀로렌즈 2 기준 ... 근접 클리핑 0.85m'는 현행 마이크로소프트 지침과 다르다. Mixed Reality 'Comfort' 문서(HoloLens 1세대·2 공통)는 40cm에서 콘텐츠 페이드아웃 시작, 렌더링 클리핑 평면 30cm를 권고한다(디스플레이 고정 초점 약 2.0m, 최적 배치 1.25~5m는 일치). 0.85m는 홀로렌즈 1세대 시절의 구 클리핑 값. https://learn.microsoft.com/en-us/windows/mixed-reality/design/comfort
- 증강현실: '30cm(3.33D) 앞에 물체를 띄우면 ... 사용 불가 영역'은 과장이며 같은 근거 문서와 충돌한다. 마이크로소프트는 1m 미만 콘텐츠를 근거리 직접 상호작용용으로 조건부 허용하고(깊이 예산 예: 전체 시간의 25% 이내), 클리핑 평면 자체를 30cm에 두라고 명시한다. 문서의 표현은 '거리가 줄면 불편 가능성이 지수적으로 증가'이지 사용 불가가 아니다.
- 출처 오류: Renner, Velichkovsky & Helmert (2013) 'The perception of egocentric distances in virtual environments — A review'는 ACM Computing Surveys 45(2)가 아니라 46(2), Article 23 (2013)이다. (Crossref 확인: ACM Computing Surveys, vol.46, issue 2, 2013)
- 출처 오류: Stephen E. Palmer, Vision Science (1999)의 5장 제목은 'Perceiving Depth and Shape'가 아니라 'Perceiving Surfaces Oriented in Depth' (p.199부터; 5.1 The Problem of Depth ...)이다. (원서 전문 검색으로 확인)
- (외 32건)

## math
항목 16개 · 검증 정정 지적 48건


### 좌표계의 사슬 — 세계·기기·카메라·이미지·눈
| 항목 | 내용 |
| --- | --- |
| 수치 | 고리 4~5개. 세계→기기 6자유도(실시간, 30~60 Hz 갱신). 기기→카메라 6자유도(고정, 공장 보정). 카메라→이미지 3×3 행렬 K(4~5개 파라미터). 픽셀 하나가 차지하는 각크기 = 수평화각/가로해상도 = 68°/1920 ≈ 2.1 arcmin. 1도의 각오차는 1 m 거리에서 약 17.5 mm, 3 m에서 약 52 mm의 어긋남을 만든다. |
| 출처 | Hartley & Zisserman, 『Multiple View Geometry in Computer Vision』 2nd ed. (Cambridge, 2004), Ch.6 §6.1 'Finite cameras'; Szeliski, 『Computer Vision: Algorithms and Applications』 2nd ed. (2022), §2.1 |

증강현실의 수학은 결국 한 문장으로 요약된다. 실세계 안의 한 점을 디스플레이의 한 픽셀 자리로 옮겨라. 그런데 그 사이에는 최소 다섯 개의 좌표계가 끼어 있다. 방이 기준인 세계좌표계, 기기 본체가 기준인 기기좌표계, 렌즈 중심이 원점인 카메라좌표계, 센서 픽셀이 기준인 이미지좌표계, 그리고 광학 시스루 기기라면 사용자 눈이 원점인 눈좌표계다. 각 단계는 '어떻게 회전해 있고 얼마나 떨어져 있는가'를 담은 변환 하나로 이어진다. 중요한 성질은 이 변환들이 더해지는 것이 아니라 곱해진다는 점이다. 앞 단계에서 각도를 0.5도 잘못 알면, 뒤 단계에서 그 오차가 거리에 비례해 커진 채 전달된다. 그래서 AR에서 '어디가 틀렸는가'를 묻는 일은 언제나 '사슬의 어느 고리가 헐거운가'를 묻는 일이 된다. 세계→기기 변환만 실시간으로 계속 바뀌고(SLAM이 푸는 부분), 기기→카메라는 공장에서 한 번 재는 고정값이며, 기기→눈은 사용자마다 다르고 심지어 안경이 코 위에서 미끄러지면 바뀐다.

### 동차좌표(homogeneous coordinates) — 왜 차원을 하나 늘리는가
| 항목 | 내용 |
| --- | --- |
| 수치 | 강체 변환 = 4×4 행렬, 성분 16개 중 실제 자유도는 6개. 카메라 사영행렬 P = 3×4, 성분 12개, 스케일 불변이므로 자유도 11개. 무한원점은 네 번째 성분 w=0. 한 점 대응은 2개의 방정식을 주므로 P를 선형으로 풀려면 최소 6점(11 자유도 ≤ 12식). |
| 출처 | Hartley & Zisserman, 『Multiple View Geometry』 2nd ed. (2004), Ch.2 §2.2 'The 2D projective plane' 및 Ch.3; Szeliski 2nd ed. (2022), §2.1.1~2.1.4 |

유클리드 좌표에서 회전은 행렬 곱이지만 평행이동은 덧셈이다. 성질이 다른 두 연산이 섞이면 변환을 여러 번 합성할 때 식이 지저분해지고 한 덩어리로 다룰 수 없다. 좌표 (X,Y,Z)에 1을 덧붙여 (X,Y,Z,1)로 만들면, 회전과 이동을 4×4 행렬 하나로 묶을 수 있고 합성은 그냥 행렬 곱 한 번이 된다. 더 결정적인 이유는 원근 투영에 있다. 카메라가 만드는 영상은 x/Z, y/Z처럼 깊이로 나누는 연산인데 나눗셈은 선형 연산이 아니다. 동차좌표에서는 3×4 행렬을 곱해 (u', v', w')를 얻고 맨 마지막에 딱 한 번 w'로 나눈다. 즉 비선형인 나눗셈을 계산의 끝으로 미뤄, 중간 과정을 전부 선형대수로 만든다. 부수 효과도 크다. 마지막 성분이 0인 좌표 (X,Y,Z,0)은 '무한히 먼 점', 곧 방향을 뜻하므로, 철길이 지평선에서 만나는 소실점 같은 것을 무한대 기호 없이 유한한 숫자로 다룰 수 있다. 또 (X,Y,Z,W)와 그것을 λ배한 좌표는 같은 점이므로, 전체 스케일은 의미가 없다. 이 스케일 불변성 때문에 자유도를 셀 때 항상 1을 빼야 한다.

### 강체 변환 SE(3) — 자세를 담는 그릇
| 항목 | 내용 |
| --- | --- |
| 수치 | SE(3) 자유도 6 = 회전 3 + 이동 3. SO(3)는 9개 성분에 직교성·행렬식 조건 6개가 걸려 자유도 3. 대응하는 리대수 se(3)는 6차원 벡터(twist). 로드리게스 공식: R = I + sinθ[k]× + (1−cosθ)[k]×², 여기서 k는 회전축 단위벡터, θ는 회전각. |
| 출처 | Solà, Deray, Atchuthan, 「A micro Lie theory for state estimation in robotics」, arXiv:1812.01537 (2018); Murray, Li, Sastry, 『A Mathematical Introduction to Robotic Manipulation』 (CRC, 1994), Ch.2 |

회전하되 늘리거나 찌그러뜨리지 않는 변환, 거기에 평행이동을 더한 것이 강체 변환이고, 이들의 모임을 SE(3)라 부른다. 자유도는 정확히 6이다. 어느 쪽을 보는가(회전 3)와 어디에 있는가(이동 3). 이것이 군(group)을 이룬다는 말은 세 가지를 뜻한다. 두 변환을 이어 붙이면 여전히 강체 변환이고, 아무것도 하지 않는 항등변환이 있으며, 모든 변환에 역이 존재한다. 역변환은 공식이 간단해서 R의 전치와 −Rᵀt로 바로 얻는다. 합성은 교환법칙이 성립하지 않는다. '앞으로 1 m 간 뒤 90도 돌기'와 '90도 돈 뒤 앞으로 1 m 가기'는 다른 곳에 도착한다. 이것이 자세 계산에서 곱하는 순서를 틀리면 결과가 조용히 망가지는 이유다. 한편 SE(3)는 평평한 벡터공간이 아니라 굽은 다양체다. 그래서 두 자세를 더하거나 평균 내는 일이 그냥은 성립하지 않고, 최적화할 때는 현재 자세 주변의 '평평한 접평면'에서 6개 숫자만 흔든 뒤 지수사상으로 다시 다양체 위로 되돌리는 방식을 쓴다.

### 오일러각과 짐벌락 — 3개의 숫자로는 안 되는 이유
| 항목 | 내용 |
| --- | --- |
| 수치 | 축 선택 순서의 조합은 12가지(고유 오일러각 6 + 타이트-브라이언 6). 특이점은 가운데 각도 = ±90°. SO(3)는 3차원 다양체지만 위상적으로 3-파라미터 전역 차트가 불가능하다(Stuelpnagel 1964). 특이점 근처에서 각속도→오일러각 변환행렬의 조건수가 발산한다. |
| 출처 | Stuelpnagel, 「On the Parametrization of the Three-Dimensional Rotation Group」, SIAM Review 6(4):422–430 (1964); Diebel, 「Representing Attitude: Euler Angles, Unit Quaternions, and Rotation Vectors」, Stanford Univ. tech report (2006) |

회전을 세 축 주위의 각도 세 개로 적는 방식이 오일러각이다. 요·피치·롤처럼 사람이 직관적으로 읽을 수 있고 저장도 가볍다. 그런데 치명적인 결함이 있다. 가운데 축의 각도가 ±90도가 되는 순간 첫 번째 축과 세 번째 축이 물리적으로 같은 방향으로 겹쳐, 서로 다른 두 각도가 같은 효과를 낸다. 즉 자유도 하나를 잃는다. 이것이 짐벌락이다. 흔한 오해는 이것이 기계 장치의 결함이라는 것인데, 사실은 순수한 수학적 필연이다. 스투엘프나겔이 보인 대로, 3차원 회전군은 세 개의 실수로 전역적으로, 특이점 없이, 매끄럽게 덮을 수 없다. 즉 어떤 3-파라미터 표현을 고안하더라도 반드시 어딘가에 특이점이 생긴다. 실무에서 무서운 것은 각도가 갑자기 튀는 현상 자체가 아니라, 그 근처에서 야코비안(미분)의 값이 무한대로 발산해 칼만 필터나 최적화가 조용히 발산한다는 점이다. 아폴로 유도장치는 관성플랫폼이 3짐벌 구조여서 실제로 락 영역이 존재했고, 네 번째 짐벌을 추가하자는 제안은 무게와 비용 때문에 기각되어 우주비행사들이 회피 기동으로 대처했다.

### 회전행렬 SO(3) — 튼튼하지만 뚱뚱한 표현
| 항목 | 내용 |
| --- | --- |
| 수치 | 성분 9개, 제약 6개, 자유도 3. 3×3 행렬 곱 = 곱셈 27회 + 덧셈 18회. 벡터 하나 회전 = 곱셈 9회 + 덧셈 6회(쿼터니언 방식보다 빠름). 재직교화는 보통 수백~수천 회 누적 곱마다 한 번. |
| 출처 | Hartley & Zisserman, 『Multiple View Geometry』 2nd ed. (2004), Appendix 4 'Matrix properties and decompositions'; Diebel (2006) §5 |

회전을 3×3 행렬로 적는 방식이다. 조건은 두 가지다. 각 열이 서로 직교하는 단위벡터일 것, 그리고 행렬식이 +1일 것. 행렬식이 −1이면 회전이 아니라 거울상 뒤집기가 되어 오른손이 왼손으로 변한다. 장점은 명확하다. 점을 회전시키는 일이 행렬 곱 한 번이고, 회전을 이어 붙이는 것도 곱이며, 역회전은 전치라서 공짜다. 특이점도 없다. 단점은 두 가지다. 첫째, 자유도 3을 표현하는 데 숫자 9개를 쓴다. 둘째, 부동소수점 곱을 반복하면 반올림 오차가 쌓여 열들이 서서히 직교성을 잃는다. 그대로 두면 회전이 미세하게 물체를 늘리거나 찌그러뜨리기 시작하므로, 주기적으로 그람-슈미트나 SVD 기반 극분해로 가장 가까운 정규직교행렬로 되돌려야 한다. 또 하나 덜 알려진 약점은 보간이다. 두 회전행렬을 성분끼리 평균 내면 결과는 회전행렬이 아니다. 그래서 두 자세 사이를 부드럽게 잇는 작업에는 적합하지 않다.

### 쿼터니언 — 왜 반각인가, 왜 부호가 두 개인가
| 항목 | 내용 |
| --- | --- |
| 수치 | 성분 4개, 제약 1개(단위 노름), 자유도 3. 쿼터니언 곱 = 곱셈 16회 + 덧셈 12회(회전행렬 곱 27+18보다 저렴). 단위 쿼터니언 전체는 4차원 구 S³를 이루며, 이것이 SO(3)를 2:1로 덮는다. 정규화 비용은 제곱근 1회 + 나눗셈 4회. |
| 출처 | Shoemake, 「Animating Rotation with Quaternion Curves」, SIGGRAPH '85, Computer Graphics 19(3):245–254 (1985); Diebel (2006) §6 |

쿼터니언은 회전을 네 개의 숫자 (w, x, y, z)로 적되, 네 숫자의 제곱합이 1이 되도록 묶은 것이다. 실제 값은 회전축 단위벡터 k와 회전각 θ에 대해 w = cos(θ/2), (x,y,z) = k·sin(θ/2)이다. 왜 하필 절반 각인가. 쿼터니언으로 벡터를 회전시키는 연산은 q를 앞뒤로 두 번 곱하는 형태(q v q*)라서 각도가 두 배로 적용된다. 그래서 애초에 절반만 담아둔다. 이 구조에서 중요한 귀결이 나온다. q와 −q는 정확히 같은 회전을 나타낸다(이중 피복). 그래서 두 자세 사이를 보간하거나 여러 자세를 평균 낼 때 부호를 먼저 맞추지 않으면, 짧게 돌 수 있는 길을 두고 반대쪽으로 크게 도는 결과가 나온다. 장점은 명확하다. 특이점이 없고(짐벌락 없음), 숫자 4개만 쓰며, 정규화가 나눗셈 한 번으로 끝나 회전행렬의 재직교화보다 훨씬 싸고, 두 회전 사이를 일정한 각속도로 잇는 구면선형보간(SLERP)이 깔끔하게 정의된다. 단점은 사람이 값을 봐도 무슨 자세인지 직관적으로 읽히지 않는다는 것뿐이다.

### 핀홀 카메라 모델과 내부 파라미터(intrinsics)
| 항목 | 내용 |
| --- | --- |
| 수치 | K의 파라미터 4~5개(fx, fy, cx, cy, s). 현대 CMOS 센서는 s ≈ 0. 예: 가로 1920 px, 수평화각 68°면 fx = 960 / tan(34°) ≈ 1423 px. 픽셀 피치 1.0 µm 센서라면 실제 초점거리 ≈ 1.42 mm. 주점 편차는 보통 중심에서 수~수십 px. fx와 fy의 비(화소 종횡비)는 대개 1.000±0.005. |
| 출처 | Hartley & Zisserman, 『Multiple View Geometry』 2nd ed. (2004), §6.1 'Finite cameras'; Szeliski 2nd ed. (2022), §2.1.5 'Camera intrinsics' |

카메라가 하는 일을 가장 단순하게 적으면 이렇다. 공간의 점을 렌즈 중심과 잇는 직선을 그어, 그 직선이 센서 평면과 만나는 자리가 영상 위 위치다. 수식으로는 u = fx·X/Z + cx 꼴이 된다. 여기서 Z로 나누는 것이 바로 원근이다. 멀수록 작게 보이는 현상이 이 나눗셈 하나에서 나온다. 이 관계를 담은 3×3 행렬 K를 내부 파라미터라 부르고, 안에는 네다섯 개의 숫자가 들어간다. fx, fy는 초점거리를 픽셀 단위로 환산한 값이고, cx, cy는 주점(광축이 센서를 뚫는 자리)이며, s는 픽셀이 직각이 아닐 때의 기울기다. 주의할 점은 fx가 밀리미터가 아니라 픽셀이라는 것이다. 같은 렌즈라도 센서 픽셀이 작으면 fx 값은 커진다. 그리고 주점은 영상 정중앙이 '대략' 맞지만 정확히는 아니다. 조립 공차 때문에 보통 수 픽셀에서 수십 픽셀 벗어나 있으며, AR에서는 이 몇 픽셀이 곧 몇 밀리미터의 어긋남으로 보인다. 또 이 모델에서 초점거리와 물체까지의 거리는 곱으로만 나타나므로, 한 장의 사진만으로는 '작은 물체가 가까이'와 '큰 물체가 멀리'를 구별할 수 없다.

### 렌즈 왜곡 — 직선이 직선으로 보이지 않는다
| 항목 | 내용 |
| --- | --- |
| 수치 | 브라운-콘래디 계수 5개(k1, k2, k3, p1, p2). 일반 스마트폰 광각 카메라는 k1이 대략 −0.1 ~ −0.3 수준이고, 1080p 영상 모서리에서 보정 전후 차이가 10~30 px 정도 난다. 화각 120° 이상의 광각에서는 가장자리 변위가 100 px을 넘기도 한다. 어안(화각 180° 안팎)은 등거리 r = fθ, 등입체각 등 별도 모델 사용. |
| 출처 | D.C. Brown, 「Decentering Distortion of Lenses」, Photogrammetric Engineering 32(3):444–462 (1966); OpenCV calib3d 모듈 문서 'Camera Calibration and 3D Reconstruction' |

핀홀 모델은 거짓말을 조금 한다. 실제 렌즈를 통과한 빛은 정확히 직선 경로를 따르지 않아서, 세상의 곧은 직선이 영상에서 휘어 보인다. 주된 성분은 두 가지다. 하나는 반경 방향 왜곡으로, 영상 중심에서 멀어질수록 점이 안쪽으로 당겨지거나(배럴) 바깥으로 밀려난다(핀쿠션). 이것은 렌즈가 회전대칭이기 때문에 중심으로부터의 거리 r의 짝수 거듭제곱 급수 k1·r² + k2·r⁴ + k3·r⁶로 근사한다. 다른 하나는 접선 방향 왜곡으로, 렌즈와 센서가 완벽히 평행하게 조립되지 않았을 때 생기며 p1, p2 두 계수로 표현한다. 이 다섯 계수 모델을 브라운-콘래디 모델이라 부른다. 순서가 중요하다. 왜곡은 정규화된 좌표에서 먼저 적용되고, 그다음 K를 곱해 픽셀로 간다. 순서를 바꾸면 결과가 틀린다. 그리고 실무에서 성가신 점은 역변환이다. 왜곡된 픽셀에서 원래 방향을 되돌리는 닫힌 형태의 공식이 없어서 반복 계산이나 미리 만든 룩업테이블을 쓴다. 화각이 아주 넓은 어안 렌즈는 이 다항식 모델이 아예 발산하므로, r = f·θ 같은 별도의 투영 모델로 갈아타야 한다.

### 카메라 보정(calibration) — 체커보드 한 장이 하는 일
| 항목 | 내용 |
| --- | --- |
| 수치 | 최소 자세 수 3회(스큐를 0으로 가정하면 2회). 실무 권장 15~30장. 양호한 보정의 RMS 재투영 오차는 0.1~0.5 px. 서브픽셀 코너 검출 정밀도 약 0.02~0.1 px. 체커보드가 영상 면적의 30% 이상을 차지하고, 기울기 20~45° 범위를 골고루 포함하는 것이 권장된다. |
| 출처 | Z. Zhang, 「A Flexible New Technique for Camera Calibration」, IEEE TPAMI 22(11):1330–1334 (2000); Hartley & Zisserman 2nd ed. (2004), Ch.8 |

보정이란 K와 왜곡 계수를 실제로 재는 작업이다. 원리는 간단하다. 3차원 위치를 정확히 아는 점들과 그 점들이 영상에 찍힌 위치를 짝지어 놓고, 그 짝들을 가장 잘 설명하는 파라미터를 찾는다. 장의 체커보드가 표준이 된 이유는 평면이라서 만들기 쉽고 코너 위치를 서브픽셀 정밀도로 검출할 수 있기 때문이다. 장이 제안한 방법의 핵심은 이렇다. 평면 위의 점들과 영상 점들 사이에는 호모그래피 H가 성립하고, 이 H는 K와 회전의 두 열, 이동으로 분해된다. 회전행렬의 두 열이 서로 직교하고 길이가 같다는 조건이 자세마다 K에 두 개씩 제약을 준다. 따라서 자세를 세 번 이상 바꿔 찍으면 K의 다섯 파라미터를 결정할 수 있다. 먼저 닫힌 형태로 초기해를 구하고, 그다음 모든 코너의 재투영 오차 제곱합을 최소화하는 비선형 최적화로 다듬는다. 여기서 사람들이 가장 많이 실패하는 부분은 데이터 다양성이다. 체커보드를 정면으로만, 화면 가운데에만 놓고 찍으면 초점거리와 물체 거리가 서로 구별되지 않아 해가 미끄러진다. 판을 크게 기울이고, 화면 구석까지 채우고, 거리를 바꿔가며 찍어야 조건수가 좋아진다.

### PnP 문제 — 3D-2D 대응에서 자세를 되찾기
| 항목 | 내용 |
| --- | --- |
| 수치 | 최소 점 수 3(P3P), 해의 개수 최대 4개. 4번째 점으로 유일해 선별. 직접선형변환(DLT)으로 3×4 사영행렬을 풀려면 최소 6점. EPnP는 계산량이 O(n)이라 n = 1000에서도 수 밀리초 수준. 실무 수렴 판정은 평균 재투영 오차 1 px 이하. |
| 출처 | X.-S. Gao, X.-R. Hou, J. Tang, H.-F. Cheng, 「Complete Solution Classification for the Perspective-Three-Point Problem」, IEEE TPAMI 25(8):930–943 (2003); V. Lepetit, F. Moreno-Noguer, P. Fua, 「EPnP: An Accurate O(n) Solution to the PnP Problem」, IJCV 81(2):155–166 (2009) |

AR에서 매 프레임 푸는 핵심 방정식이 이것이다. 공간에서 위치를 아는 점 n개가 영상의 어디에 찍혔는지 알 때, 카메라가 어디에서 어느 방향으로 보고 있었는지를 역산하는 문제다. 미지수는 6개(회전 3, 이동 3)이고, 점 하나가 방정식 2개를 주므로 이론상 3점이면 충분하다. 그런데 3점만으로는 답이 하나로 정해지지 않는다. 식이 4차 다항식이 되어 최대 네 개의 실수 해가 나온다. 기하학적으로 보면 이해가 된다. 삼각형 하나만 보고는 그것이 앞으로 기울었는지 뒤로 기울었는지 구별되지 않는 배치가 존재한다. 그래서 실무에서는 네 번째 점을 하나 더 써서 후보들을 재투영해 보고 가장 잘 맞는 것을 고른다. 점이 많을 때는 다른 전략을 쓴다. EPnP는 모든 3D 점을 네 개의 가상 제어점의 가중합으로 다시 적어, 미지수를 제어점 네 개의 카메라 좌표(12개)로 줄인다. 그러면 점 개수에 선형인 시간으로 풀린다. 어느 방법을 쓰든 마지막에는 항상 비선형 정제를 붙인다. 초기해를 출발점으로 삼아 재투영 오차를 가우스-뉴턴이나 레벤버그-마쿼트로 줄이는 단계다. 초기해 없이 비선형 최적화만 돌리면 엉뚱한 국소최소로 빠진다.

### RANSAC — 틀린 데이터가 다수일 때
| 항목 | 내용 |
| --- | --- |
| 수치 | 반복 횟수 N = log(1−p) / log(1−(1−ε)^s). p = 0.99(성공확률), s = 4, ε = 0.5(이상치 50%)이면 N = 72회. 같은 조건에서 s = 8이면 1177회로 폭증. 내부점 판정 임계값은 보통 재투영 오차 1~3 px(측정 잡음 표준편차의 약 2배). 변형으로 MSAC, PROSAC, LO-RANSAC, GC-RANSAC. |
| 출처 | M.A. Fischler & R.C. Bolles, 「Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography」, Communications of the ACM 24(6):381–395 (1981); Hartley & Zisserman 2nd ed. (2004), §4.7 및 Table 4.3 |

최소제곱법은 모든 데이터가 조금씩만 틀렸다고 가정한다. 그 가정이 깨지면 무너진다. 아주 멀리 떨어진 이상치가 단 하나만 섞여도 최소제곱해는 그쪽으로 끌려간다. 통계 용어로 붕괴점이 0이다. 그런데 영상 특징점 매칭은 본질적으로 이상치 투성이다. 비슷하게 생긴 벽돌, 창틀, 반복 무늬는 엉뚱한 곳끼리 짝지어지고, 실제 현장에서 오대응 비율이 20~70%인 것은 전혀 이상한 일이 아니다. RANSAC의 발상은 데이터를 평균 내지 않고 투표하게 만드는 것이다. 모델을 정하는 데 필요한 최소 개수만 무작위로 뽑아 모델 하나를 만들고, 나머지 전체 데이터 중 그 모델에 일정 오차 안으로 들어오는 것을 센다. 이것을 여러 번 반복해 지지자가 가장 많은 모델을 채택하고, 마지막에 그 지지자들만으로 다시 정밀하게 푼다. 핵심 통찰은 계산량 공식에 있다. 필요한 반복 횟수는 이상치 비율에 대해서는 완만하지만 최소 표본 크기 s에 대해서는 지수적으로 커진다. 그래서 '최소 몇 점으로 풀 수 있는가'를 줄이는 연구, 곧 P3P 같은 최소 해법이 그토록 중요한 것이다.

### 번들 조정(bundle adjustment) — 전체를 한꺼번에 미세조정하기
| 항목 | 내용 |
| --- | --- |
| 수치 | 미지수 = 6m + 3n(카메라 m대, 점 n개). m=100, n=50,000 → 150,600개. 밀집 촐레스키 분해는 O(N³) ≈ 3.4×10¹⁵ 연산으로 현실적으로 불가능. 슈어 보수 후 축소 시스템은 6m × 6m = 600 × 600. 게이지 자유도 7개(회전 3 + 이동 3 + 스케일 1). 대표 구현: Ceres Solver, g2o, GTSAM. |
| 출처 | B. Triggs, P. McLauchlan, R. Hartley, A. Fitzgibbon, 「Bundle Adjustment — A Modern Synthesis」, Vision Algorithms '99, LNCS 1883:298–372 (Springer, 2000); S. Agarwal et al., 「Building Rome in a Day」, CACM 54(10):105–112 (2011) |

프레임마다 따로 자세를 풀면 오차가 쌓여 지도가 휘어진다. 번들 조정은 모든 카메라 자세와 모든 3D 점을 동시에 미지수로 놓고, 관측된 모든 영상점과 재투영된 점 사이의 거리 제곱합을 한꺼번에 최소화한다. 이름의 '번들'은 각 3D 점에서 여러 카메라로 뻗어 나가는 광선 다발을 뜻한다. 문제는 크기다. 카메라 100대, 점 5만 개면 미지수가 15만 개를 넘는다. 이것을 통째로 푸는 것은 불가능해 보이지만, 구조에 결정적인 성질이 있다. 어떤 3D 점은 그것이 실제로 보인 몇 대의 카메라하고만 연결되고 나머지와는 무관하다. 그래서 야코비안과 정규방정식 행렬이 극도로 희소한 블록 구조를 갖는다. 여기에 슈어 보수를 적용해 점 블록을 먼저 소거하면, 카메라 자세만 남은 훨씬 작은 연립방정식으로 줄어든다. 하나 더, 이 문제에는 게이지 자유도가 있다. 재구성 전체를 통째로 회전시키거나 옮기거나 확대해도 재투영 오차는 변하지 않는다. 그래서 7개의 자유도를 따로 고정하지 않으면 해가 유일하지 않다. 마지막으로 RANSAC이 놓친 잔여 이상치를 위해 후버나 코시 같은 로버스트 손실함수를 씌우는 것이 표준이다.

### 다양체 위의 최적화 — 회전은 더할 수 없다
| 항목 | 내용 |
| --- | --- |
| 수치 | 접평면 갱신 벡터 = 6차원(회전 3 + 이동 3). 소각 근사 sinθ ≈ θ의 상대오차는 θ = 5°에서 약 0.13%, θ = 30°에서 약 4.5%. 자세 공분산 6×6. 각 반복의 회전 갱신량은 통상 1° 이하로 유지. |
| 출처 | J. Solà, J. Deray, D. Atchuthan, 「A micro Lie theory for state estimation in robotics」, arXiv:1812.01537 (2018); C. Forster, L. Carlone, F. Dellaert, D. Scaramuzza, 「On-Manifold Preintegration for Real-Time Visual-Inertial Odometry」, IEEE Trans. Robotics 33(1):1–21 (2017) |

앞의 최적화들이 은근슬쩍 넘어간 문제가 있다. 최적화 알고리즘은 '현재 값에 작은 변화량을 더한다'를 반복하는데, 회전은 더할 수 있는 대상이 아니다. 두 회전행렬을 성분끼리 더하면 회전행렬이 아니고, 두 오일러각을 평균 내면 엉뚱한 자세가 나온다. 해법은 이렇다. 현재 추정된 회전 R 주변의 접평면에서 3차원 벡터 δ만큼 움직이고, 그 δ를 지수사상으로 회전으로 바꿔 R에 곱해 다시 회전 다양체 위로 돌려놓는다. 이동은 원래 벡터공간이니 그냥 더한다. 결과적으로 자세 하나당 정확히 6개의 숫자만 흔들게 되고, 자유도가 남거나 모자라지 않는다. 불확실성도 같은 논리를 따른다. 자세의 공분산은 접평면에서 정의된 6×6 행렬이다. 다만 이 선형화는 소각 가정 위에 서 있어, 한 번의 갱신량이 커지면 근사 오차가 급격히 커진다. 그래서 자세 갱신은 작은 스텝으로 여러 번 하는 것이 원칙이고, 이것이 레벤버그-마쿼트의 신뢰영역 개념과 자연스럽게 맞물린다.

### 센서 간 외부 보정 — 카메라와 관성센서는 같은 자리에 있지 않다
| 항목 | 내용 |
| --- | --- |
| 수치 | 카메라-IMU 거리(레버암)는 통상 2~10 cm. 각속도 200°/s(= 3.49 rad/s)에서 레버암 5 cm면 접선속도 0.175 m/s이고, 5 ms의 시간 오프셋은 약 0.87 mm의 위치 오차를 만든다. 같은 조건에서 회전 성분 오차는 1°이며, 이는 1 m 거리에서 약 17 mm의 어긋남에 해당해 위치 성분보다 20배 크다. 미지수: 외부 자세 6 + 시간 오프셋 1. |
| 출처 | R.Y. Tsai & R.K. Lenz, 「A New Technique for Fully Autonomous and Efficient 3D Robotics Hand/Eye Calibration」, IEEE Trans. Robotics and Automation 5(3):345–358 (1989); P. Furgale, J. Rehder, R. Siegwart, 「Unified Temporal and Spatial Calibration for Multi-Sensor Systems」, IROS 2013 (Kalibr); F.M. Mirzaei & S.I. Roumeliotis, 「A Kalman Filter-Based Algorithm for IMU-Camera Calibration」, IEEE Trans. R |

AR 기기 한 대 안에는 카메라, 관성센서(IMU), 디스플레이가 각각 다른 위치에 서로 다른 방향으로 붙어 있다. 이들 사이의 고정된 상대 자세를 모르면, 기기가 회전할 때마다 지렛대 효과로 위치 오차가 생긴다. 이 문제는 고전적으로 AX = XB 형태의 방정식으로 정식화된다. 두 센서가 같은 움직임을 각자의 좌표계에서 관측했을 때 성립하는 관계이며, 여기서 미지의 고정 변환 X를 푼다. 회전과 이동을 분리해 푸는 방법(차이-렌츠)과 동시에 푸는 방법이 있고, 후자가 일반적으로 정확하다. AR에서는 여기에 한 가지 미지수가 더 붙는다. 시간이다. 카메라와 IMU는 서로 다른 클럭과 서로 다른 지연을 갖기 때문에, 같은 순간을 서로 다른 타임스탬프로 기록한다. 이 시간 오프셋을 공간 외부 파라미터와 함께 미지수로 넣어 한꺼번에 푸는 것이 현재의 표준이다. 시간 오프셋이 특히 무서운 이유는 회전이 빠를수록 오차가 선형으로 커지기 때문이다. 느리게 움직일 때는 아무 문제가 없다가, 사용자가 고개를 홱 돌리는 순간에만 가상 물체가 튀는 증상이 바로 이것이다.

### 광학 시스루 HMD의 눈-디스플레이 보정(SPAAM)이 왜 어려운가
| 항목 | 내용 |
| --- | --- |
| 수치 | 3×4 투영행렬은 자유도 11개, 정렬 1회가 방정식 2개를 주므로 이론상 최소 6회, 실무에서는 20회 이상 권장. 성인 동공간거리(IPD) 평균 약 63.4 mm, 표준편차 약 3.8 mm(Dodgson 2004). 안구 회전중심은 각막 정점 뒤 약 13 mm, 입사동은 약 3 mm에 있어 레버암이 약 10 mm. 따라서 시선을 20° 돌리면 실효 시점이 약 3.4 mm 이동한다. 가상 상면 2 m, 실물 0.5 m, 눈 이동 5 mm인 경우 어긋남은 5 × (1 − 0.25) = 3.75 mm이고, 0.5 m 거리에서 각도로는 약 0.43°다. 참고로 인간의 최소 분간각은 약 1 arcmin(0.017°)이다. |
| 출처 | M. Tuceryan & N. Navab, 「Single Point Active Alignment Method (SPAAM) for Optical See-Through HMD Calibration for AR」, IEEE/ACM ISAR 2000, pp.149–158; J. Grubert, Y. Itoh, K. Moser, J.E. Swan II, 「A Survey of Calibration Methods for Optical See-Through Head-Mounted Displays」, IEEE TVCG 24(9):2649–2662 (2018); N.A. Dodgson, 「Variation and Extrema of Human Interpupillary Distance」, Proc. SPIE 5291 ( |

비디오 시스루 기기는 쉽다. 카메라가 찍은 영상 위에 가상 물체를 그리므로, 카메라의 투영 중심이 곧 사용자의 눈이다. 광학 시스루는 근본적으로 다르다. 사용자는 반투명 유리 너머로 실제 세계를 직접 보고, 그 위에 빛이 겹쳐진다. 그러므로 진짜 투영 중심은 사용자의 눈동자인데, 기기는 자기 사용자의 눈을 볼 수 없다. 측정할 수 없는 대상을 추정해야 하는 것이다. SPAAM의 발상은 사용자를 측정 장비로 쓰는 것이다. 디스플레이에 십자 표식을 띄우고, 사용자가 머리를 움직여 그 표식을 추적 중인 실제 세계의 한 점과 겹쳐 보이게 만든다. 겹친 순간 버튼을 누르면 '이 3D 세계점이 이 2D 디스플레이 좌표에 대응한다'는 한 쌍이 기록된다. 이런 쌍을 충분히 모으면 눈-디스플레이 사이의 3×4 투영행렬을 직접선형변환으로 풀 수 있다. 어려움은 네 겹이다. 첫째, 측정 장비가 사람이다. 머리 떨림, 조준 편향, 피로가 그대로 잡음이 된다. 둘째, 눈은 고정점이 아니다. 시선을 돌리면 안구가 회전하면서 실효 투영 중심이 밀리미터 단위로 움직인다. 셋째, HMD가 코 위에서 조금만 미끄러져도 애써 구한 보정이 무효가 된다. 넷째, 시차의 기하학 때문에 눈의 작은 이동이 곧바로 정합 오차로 증폭된다. 가상 상이 맺히는 거리 D와 실제 물체 거리 d가 다르면, 눈이 δ만큼 움직일 때 어긋남은 δ(1 − d/D)이 된다.

### 시간이라는 일곱 번째 좌표 — 지연, 예측, 잔여 오차
| 항목 | 내용 |
| --- | --- |
| 수치 | 사람 머리 회전 속도는 일상적으로 평균 50°/s 안팎, 급격한 동작에서 300~600°/s에 이른다. 100 ms 지연에 50°/s면 각오차 5°이고, 1 m 거리에서 약 87 mm 어긋난다. 홀로웨이의 경험칙은 팔 길이(약 0.7 m) 대상에서 지연 1 ms당 약 1 mm의 정합 오차다. 인간 시각의 최소 분간각 1 arcmin은 1 m 거리에서 약 0.29 mm에 해당한다. 현재 실용 목표는 motion-to-photon 20 ms 이하이며, 타임워프 계열 기법은 실효 지연을 한 프레임(60 Hz에서 16.7 ms) 수준까지 낮춘다. |
| 출처 | R. Azuma, 「A Survey of Augmented Reality」, Presence: Teleoperators and Virtual Environments 6(4):355–385 (1997); R. Holloway, 「Registration Error Analysis for Augmented Reality」, Presence 6(4):413–432 (1997); R. Azuma & G. Bishop, 「Improving Static and Dynamic Registration in an Optical See-through HMD」, SIGGRAPH '94, pp.197–204 |

앞의 모든 수학이 완벽해도 AR은 어긋날 수 있다. 계산에 쓰인 자세는 과거의 값이고, 그 결과로 그려진 그림은 미래에 눈에 도달하기 때문이다. 센서가 자세를 읽는 순간부터 그 결과가 빛이 되어 눈에 닿기까지의 시간을 motion-to-photon 지연이라 부른다. 그 사이에 머리가 움직였다면, 어긋남의 크기는 정확히 각속도 곱하기 지연 시간이다. 이 곱이 문제의 전부라는 사실이 중요하다. 지연을 절반으로 줄이면 오차도 절반이 된다. 대책은 세 갈래다. 첫째, 예측이다. 등속이나 등가속 모델, 또는 고속 IMU 적분으로 '표시될 시각의 자세'를 미리 계산한다. 다만 예측은 잡음도 함께 증폭하므로, 지연을 줄이면 화면이 떨리고 떨림을 줄이면 지연이 남는 맞바꿈이 생긴다. 둘째, 늦게 읽기(late latching)다. 렌더링 직전까지 자세 확정을 미룬다. 셋째, 재투영 또는 타임워프다. 이미 그린 화면을 최신 자세에 맞춰 2차원적으로 밀어 준다. 회전 성분은 깊이를 몰라도 거의 정확히 보정되지만, 평행이동 성분은 화소마다 깊이가 필요해 완전히 보정되지 않는다. 결국 시간은 좌표계 하나를 더 추가하는 셈이고, 이 축을 무시한 기하학은 정지 상태에서만 맞는다.

#### 검증에서 잡힌 정정
- [치명·자기모순] 「픽셀 하나가 차지하는 각크기 = 수평화각/가로해상도 = 68°/1920 ≈ 2.1 arcmin」 — 이 나눗셈은 항등식이 아니라 폭 전체의 평균에 불과하다. 핀홀 모델에서 픽셀의 각크기는 1/fx(광축)이고, 문서가 같은 조사 안에서 스스로 구한 fx=960/tan(34°)=1423.26 px를 쓰면 광축 픽셀은 1/1423.26 rad = 0.04026° = 2.42 arcmin(주장값보다 14% 큼), 영상 가장자리 픽셀은 1/fx/(1+(u/fx)²) = 1.66 arcmin(주장값보다 22% 작음)이다. 하나의 값 2.1 arcmin은 중심에서도 가장자리에서도 맞지 않으며, 같은 문서의 fx 수치와 모순된다.
- [치명·자기모순] 「스마트폰 광각은 k1 ≈ −0.1 ~ −0.3, 1080p 영상 모서리에서 보정 전후 차이가 10~30 px」 — 자릿수가 틀렸다. fx=1423 px, 1920×1080에서 모서리의 정규화 반경은 r=0.7739, r³=0.4635이므로 1차 반경왜곡 변위는 \|k1\|·r³·fx = k1=−0.1일 때 66.0 px, −0.2일 때 131.9 px, −0.3일 때 197.9 px다. 10~30 px가 되려면 k1 ≈ −0.015 ~ −0.045여야 한다. 더구나 바로 다음 문장의 「화각 120° 이상의 광각에서는 가장자리 변위가 100 px을 넘기도 한다」는 화각 68°·k1=−0.2에서 이미 132 px로 초과되어, 두 수치가 서로를 부정한다.
- [치명] 「축 선택 순서의 조합은 12가지(고유 오일러각 6 + 타이트-브라이언 6). 특이점은 가운데 각도 = ±90°」 — ±90°는 타이트-브라이언(비대칭, z-y-x 등) 6개 관례에만 해당한다. 같은 문장이 함께 센 고유 오일러각(대칭, z-x-z·z-y-z 등) 6개는 가운데 각도 β = 0° 또는 180°에서 짐벌락이 발생한다(Wikipedia Euler angles: z 축과 Z 축이 일치하면 β=0, 반대면 β=π). 즉 열거한 12개 관례 중 절반에 대해 명시한 특이점 위치가 틀렸다.
- [치명·차원오기] 「단위 쿼터니언 전체는 4차원 구 S³를 이루며, 이것이 SO(3)를 2:1로 덮는다」 — S³는 R⁴에 매장된 3차원 다양체(3-구)이지 '4차원 구'가 아니다. 이는 단순한 표기 문제가 아니라 같은 문장과 모순이다: SO(3)는 3차원이고 피복사상은 국소 미분동형이므로 덮는 쪽도 반드시 3차원이어야 한다. 또한 바로 앞의 「성분 4개, 제약 1개, 자유도 3」과도 어긋난다(4−1=3차원).
- [출처 내용 왜곡] 「홀로웨이의 경험칙은 팔 길이(약 0.7 m) 대상에서 지연 1 ms당 약 1 mm의 정합 오차다」 — 원문(Holloway, UNC TR 95-016, §6.3.2.3.2, p.131)은 대상 거리를 \|\|vS_P"\|\| = 500 mm로 잡고, 회전 성분 50°/s에서 bang_delay=436·Δt → 0.44 mm/ms, 병진 성분 500 mm/s에서 0.5 mm/ms를 **합산**해 'in the worst case, we get about 1 mm of registration error for every millisecond of delay'라고 적는다. 즉 (a) 거리가 0.7 m가 아니라 0.5 m, (b) 순수 회전 효과가 아니라 회전+병진 합산, (c) 일반 경험칙이 아니라 최악의 경우다. 같은 절이 제시한 평균 속도(20°/s·164 mm/s) 기준값은 약 0.33 mm/ms로 주장값의 1/3이다.
- [출처 내용 왜곡] 「사람 머리 회전 속도는 일상적으로 평균 50°/s 안팎」 — 인용된 Holloway/Azuma의 실측은 반대를 말한다. Holloway p.131: 'most of the head movements were slower than about 50 deg/s and 500 mm/s'로 50°/s는 보수적 상한이며, 같은 쪽에서 평균 계산에 쓴 값은 20 deg/s, Azuma 1995의 naive user 실측 첨두값도 120°/s다. 50°/s를 '평균'으로 놓았기 때문에 뒤따르는 「100 ms 지연에 50°/s면 5°, 1 m에서 87 mm」도 상한을 전형값으로 제시한 과대 추정이 된다(평균 20°/s면 2°, 약 35 mm).
- [원리 반대] 「타임워프 계열 기법은 실효 지연을 한 프레임(60 Hz에서 16.7 ms) 수준까지 낮춘다」 — 방향이 뒤집혔다. 타임워프/late-stage reprojection은 렌더가 끝난 뒤 스캔아웃 직전에 최신 자세로 영상을 재사영하는 기법이므로, 목적이 잔여(회전) 지연을 한 프레임 **아래**, 실무상 수 ms로 끌어내리는 것이다. Microsoft HoloLens 문서: 'HoloLens has hardware that adjusts the rendered image to account for the discrepancy between the predicted head position and the actual head position'이며, 같은 문서는 30 FPS로 떨어지면 '33.3 ms of extra latency'가 **추가**된다고 적는다. 즉 한 프레임(16.7 ms)은 타임워프가 제거하는 단위이지 도달 하한이 아니다.
- [단위 사슬 오류] 「픽셀 피치 1.0 µm 센서라면 실제 초점거리 ≈ 1.42 mm」 — 1423 px × 1.0 µm = 1.423 mm는 산술상 맞지만, 이 계산은 센서 폭이 1920 × 1.0 µm = 1.92 mm임을 전제한다. fx[px]는 출력 영상 픽셀이 아니라 센서의 실제 샘플링 피치에 묶인 양이고, 1080p 출력은 가로 4000 px 이상인 센서에서 다운스케일·비닝되어 나오므로 유효 피치가 물리 피치의 2~4배다. 실제 스마트폰 메인 카메라(화각 약 68°, 26 mm 환산)의 초점거리는 4~7 mm 대이며 1.42 mm 초점거리·1.92 mm 폭 센서를 쓰는 기종은 없다. 출력 해상도를 센서 화소수로 혼동한 단위 오류다.
- [수치 과소·근거 누락] 「세계→기기 6자유도(실시간, 30~60 Hz 갱신)」 — 30~60 Hz는 카메라 프레임률(시각 갱신)일 뿐 자세 출력률이 아니다. VIO는 IMU 전파로 수백 Hz~1 kHz로 자세를 내보내고, 현행 기기의 자세 질의·표시율은 HoloLens 2 120 Hz, Quest 3 90/120 Hz, Vision Pro 90~100 Hz다. HoloLens 1세대조차 Microsoft 문서 기준 'displays refresh 240 times a second, showing four separate color fields for each newly rendered image'이다. 2~20배 과소 표기이며, late-latching/타임워프가 성립하는 이유(자세 갱신률 ≫ 렌더 프레임률)를 설명 불가능하게 만든다.
- [경미·연산량 혼동] 「밀집 촐레스키 분해는 O(N³) ≈ 3.4×10¹⁵ 연산으로 현실적으로 불가능」 — N=150,600에서 N³=3.416×10¹⁵는 맞지만 촐레스키의 실제 연산량은 N³/3 ≈ 1.14×10¹⁵로 3배 작다(O(N³)의 상수를 1로 둔 혼동). 또 '불가능'의 근거가 틀렸다: 10¹¹~10¹² flop/s면 수 시간 규모로 느리긴 해도 불가능이 아니며, 진짜 장벽은 밀집 저장량 N²≈2.3×10¹⁰ 배정도(약 180 GB)다 — 문서는 이 결정적 수치를 언급하지 않는다.
- [경미·제약 오분류] 「SO(3)는 9개 성분에 직교성·행렬식 조건 6개가 걸려 자유도 3」 — 독립 제약 6개는 전부 RᵀR = I(대칭 3×3 → 6개)에서 나온다. det R = +1은 직교성에서 이미 det = ±1이 따라 나온 뒤 연결성분을 고르는 이산(0차원) 조건이므로 9−6=3의 차원 계산에 기여하지 않는다. 행렬식을 6개 제약의 일부로 센 것처럼 읽히는 서술이다.
- [경미·출처 귀속 오류] 「브라운-콘래디 계수 5개(k1, k2, k3, p1, p2)」의 출처로 D.C. Brown, 「Decentering Distortion of Lenses」, Photogrammetric Engineering 32(3):444–462 (1966)을 든 것 — 서지 자체는 실존하지만 이 1966년 논문은 제목대로 '탈중심(접선) 왜곡' 즉 p1, p2 항만 다룬다. k1·k2·k3의 반경 왜곡 다항식은 Conrady(1919)와 Brown의 1971년 「Close-Range Camera Calibration」(Photogrammetric Engineering 37(8):855–866) 계열이며, (k1,k2,p1,p2,k3) 5계수 묶음 자체는 OpenCV의 파라미터화 관례다. 실존 문헌을 잘못 귀속한 사례.
- [경미·통계 임계값] 「RANSAC 내부점 판정 임계값은 보통 재투영 오차 1~3 px(측정 잡음 표준편차의 약 2배)」 — Hartley & Zisserman의 표준 임계값은 자유도 2인 점 거리(재투영 오차)에 대해 t² = 5.99σ², 즉 t ≈ 2.45σ다. 약 2배(1.96σ)는 자유도 1(점-직선 거리) 경우의 값이므로 이 문맥에 맞지 않는다.
- [경미·범주 혼합] 센서 간 외부 보정 절의 「같은 조건에서 회전 성분 오차는 1°이며 ... 위치 성분보다 20배 크다」 — 두 항의 성격이 다르다. 0.87 mm는 레버암(5 cm)과 시간 오프셋이 곱해진 효과이지만, 1°(=200°/s × 5 ms)는 레버암과 무관한 순수 시간 정렬 오차이며 레버암이 0이어도 그대로 발생한다. 따라서 '레버암 효과'로 묶어 20배를 비교하는 것은 원인 범주가 섞인 비교이고, 20배 비율도 '기기 병진 오차(mm)'와 '1 m 거리 정합 오차(mm)'라는 서로 다른 계량을 암묵적으로 갈아 끼운 결과다.
- [경미·과대] 「서브픽셀 코너 검출 정밀도 약 0.02~0.1 px」 — 하한 0.02 px는 합성 영상·이상 조건의 값이고 실제 촬영 영상의 체커보드 코너 국소화 정밀도는 통상 0.05~0.1 px 수준이다. 또한 같은 항의 「양호한 보정의 RMS 재투영 오차 0.1~0.5 px」과 함께 두면, 코너 검출이 0.02 px 정밀도라는 전제에서 RMS 0.5 px는 거의 전부 모델 오차가 되어야 하는데 그 함의가 설명되지 않는다.
- 오일러각 특이점 — 「특이점은 가운데 각도 = ±90°」는 스스로 열거한 12가지 관례 중 절반에 대해 틀렸다. ±90°는 타이트-브라이언(비대칭, Z-Y-X 요·피치·롤 등) 6가지에만 해당한다. 고유 오일러각(대칭, Z-X-Z·Z-Y-Z·X-Y-X 등) 6가지의 축퇴는 가운데 각도 = 0° 또는 180°에서 일어나며(1·3축이 겹치는 지점), 그 관례에서 ±90°는 완전히 정상적인 자세다. Wikipedia Euler angles: 'uniquely determined except for the singular case that the xy and the XY planes are identical, i.e. when the z axis and the Z axis have the same or opposite directions' → β=0 또는 π. 12가지를 나열한 직후 단일 특이점 값을 단정한 것이므로 산술 오차가 아니라 원리 오류다.
- 픽셀 각크기 — 「픽셀 하나가 차지하는 각크기 = 수평화각/가로해상도」는 항등식이 아니다. 핀홀에서 픽셀당 각크기는 dθ/du = f/(f²+(u−cx)²)로, 주점에서 최대이고 주변으로 갈수록 작아진다. 카드 자신이 뒤에서 도출한 fx = 960/tan(34°) = 1423 px를 쓰면 중심 픽셀은 atan(1/1423) = 2.42 arcmin, 가장자리 픽셀(u−cx=960)은 1.66 arcmin으로 화면 내 편차가 45%다. 인용된 2.1 arcmin은 중심값도 주변값도 아닌 단순 평균이며 중심(최악)값을 13.7% 과소평가한다. 'Z로 나누는 것이 바로 원근'이라며 사영의 비선형성을 설명하는 절에서 정작 선형 나눗셈을 쓴 내부 모순이다.
- 홀로웨이 경험칙의 거리와 조건 — 「팔 길이(약 0.7 m) 대상에서 지연 1 ms당 약 1 mm」는 거리와 성격을 모두 틀렸다. 원문(UNC TR 95-016, p.131~132)의 계산 거리는 \|\|vS_P"\|\| = 500 mm이고, 결론은 최악값으로 명시된다: 'in the worst case, we get about 1 mm of registration error for every millisecond of delay.' 그 1 mm는 회전 0.44 mm/ms(50°/s×0.5m)와 병진 0.5 mm/ms(500 mm/s)의 합이며 절반이 병진 성분이다. 원문 측정 평균 속도(164 mm/s, 20°/s)를 넣으면 0.34 mm/ms로 3분의 1이다(논문 인쇄상의 '33 mm/ms'·'31 mm/ms'는 0.33/0.34의 단위 오타). 카드는 거리, 최악값 조건, 병진 기여를 모두 누락했다.
- 머리 회전 속도 평균 — 「일상적으로 평균 50°/s 안팎」은 상한을 평균으로 바꿔 쓴 것이다. 카드가 근거로 삼는 홀로웨이 원문의 3세션 약 10,000 샘플 측정: 'The mean linear velocity for these sessions was 164 mm/s and the mean angular velocity was 20 deg/s'이며, 50°/s는 'fairly conservative upper bounds'로 제시된 값이다. 즉 평균을 2.5배 부풀렸다. 따라서 이어지는 예시 「100 ms 지연에 50°/s면 각오차 5°, 1 m에서 약 87 mm」도 통상 동작 기준으로는 2°·약 35 mm가 맞다. 덧붙여 「급격한 동작에서 300~600°/s」는 인용된 AR 문헌 범위를 크게 벗어난다 — 같은 원문이 인용한 Azuma 1995의 순간 최대치는 120°/s다('the peak velocities did get as high as 120 deg/s in some c
- 비디오 시스루 — 「카메라가 찍은 영상 위에 가상 물체를 그리므로, 카메라의 투영 중심이 곧 사용자의 눈이다」는 거짓이다. 비디오 시스루/패스스루에서 카메라는 눈보다 수 cm 앞·바깥에 놓이므로 카메라 중심은 눈의 투영 중심이 아니다. 바로 이 눈-카메라 오프셋 때문에 패스스루 HMD는 촬영 영상을 눈 시점으로 재투영해야 하며, 고전적 orthoscopic 비디오 시스루 설계가 거울 폴딩으로 카메라를 광학적으로 눈 위치에 옮긴 이유도 이것이다. 비디오 시스루가 없애주는 것은 '눈 위치를 모른다'는 문제이고, 시점 오프셋 문제는 남는다. 카드가 OST에 대해 올바르게 지적한 것과 같은 종류의 오류를 VST에서 범했다.
- 카메라-IMU 외부 보정의 정식화 — 「이 문제는 고전적으로 AX = XB 형태의 방정식으로 정식화된다」는 IMU에 대해 틀렸다. AX = XB(Tsai & Lenz 1989)는 손-눈(hand/eye) 보정이며 두 장치가 모두 완전한 6자유도 자세를 준다는 전제 위에 있다. IMU는 각속도와 비력(specific force)을 주고 자세를 주지 않는다. 같은 카드가 함께 인용한 다른 두 문헌이 AX = XB를 쓰지 않는 이유가 바로 그것이다 — Mirzaei & Roumeliotis 2008은 관측성 분석을 동반한 EKF, Furgale et al. 2013(Kalibr)은 외부 자세와 시간 오프셋을 함께 추정하는 연속시간 배치 추정이다. 각속도 정렬로 회전 성분만 부분적으로 얻을 수 있고, 병진 성분은 충분한 운동 여기와 중력 관측이 있어야 관측 가능해진다.
- 다양체 최적화의 갱신량 — 「각 반복의 회전 갱신량은 통상 1° 이하로 유지」는 존재하지 않는 규칙이며, 온-매니폴드 최적화를 하는 이유를 거꾸로 설명한다. R ← R·exp([δ]×) 리트랙션은 δ 크기와 무관하게 정확하므로 증분을 작게 유지할 필요가 없다. 번들 조정의 스텝 크기를 제한하는 것은 신뢰영역/LM 감쇠이지 1° 상한이 아니다. 소각 근사(카드가 0.13%/4.5%로 옳게 계산한 부분)는 자코비안 유도에 들어가는 것이고 리트랙션 자체에는 들어가지 않는다. 즉 온-매니폴드 기법은 소각 근사를 '필요 없게 만드는' 장치인데, 카드는 소각 근사를 기법이 작동하는 근거로 제시했다.
- 촐레스키 연산량과 병목 — 「밀집 촐레스키 분해는 O(N³) ≈ 3.4×10¹⁵ 연산」에서 실제 연산량은 대칭 행렬 기준 약 N³/3 ≈ 1.14×10¹⁵ flops로 3배 과대 계상이다. 더 중요하게, 현실적 불가능의 실제 사유는 연산량이 아니라 메모리다: N = 150,600의 밀집 정규방정식 행렬은 150,600² × 8 B ≈ 181 GB로 애초에 적재되지 않는다. 슈어 보수·희소성을 쓰는 1차 동기는 flop 절감이 아니라 밀집 저장 회피이므로, 병목을 잘못 지목한 설명이다.
- S³의 차원 — 「단위 쿼터니언 전체는 4차원 구 S³를 이루며」에서 S³는 3차원 다양체(R⁴에 매장된 3-구)다. '4차원 구'는 S⁴를 가리키는 말이므로 같은 문장 안의 기호 S³와 모순된다. 이 구분은 카드 자신의 자유도 회계에 직결된다 — 성분 4개에 단위 노름 제약 1개를 걸어 3차원 대상을 얻고, 그것이 SO(3)의 자유도 3과 맞아떨어지는 것이 요점이기 때문이다.
- Szeliski 절 제목 오지정 — 「Szeliski 2nd ed. (2022), §2.1.5 'Camera intrinsics'」에서 §2.1.5의 제목은 'Camera intrinsics'가 아니라 '3D to 2D projections'이고 §2.1.6은 'Lens distortions'다(저자 공개 원고 목차에서 직접 확인: 2.1.1 Geometric primitives / 2.1.2 2D transformations / 2.1.3 3D transformations / 2.1.4 3D rotations / 2.1.5 3D to 2D projections / 2.1.6 Lens distortions). 'Camera intrinsics'는 §2.1.5 본문 안의 번호 없는 문단 표제다.
- H&Z 장 오지정 — 「카메라 보정(calibration) — 체커보드 한 장이 하는 일 … 출처 Hartley & Zisserman 2nd ed. (2004), Ch.8」은 잘못된 장을 지시한다. 공식 목차 확인 결과 Ch.8은 'More Single View Geometry'이고 그 보정 관련 내용은 §8.5 'Camera calibration and the image of the absolute conic', §8.6 소실점, §8.8 'Determining camera calibration K from a single view' — 즉 알려진 타깃 없이 하는 단일시점 보정이다. 3D 좌표를 아는 점들과 영상점을 짝지어 푸는 체커보드형 보정과 방사 왜곡 추정은 Ch.7 'Computation of the Camera Matrix P'(§7.1 Basic equations, §7.4 Radial distortion)다.
- RANSAC 내부점 임계값 — 「측정 잡음 표준편차의 약 2배」는 자유도를 틀렸다. 카드가 다루는 양은 재투영 오차, 즉 2자유도 점-점 거리이며 H&Z §4.7의 처방은 t² = 5.99σ²(χ² 95% 분위) → t = 2.45σ다. 약 1.96σ(≈2σ)는 t² = 3.84σ², 곧 1자유도 점-직선 거리 경우에 적용된다. 2σ를 쓰면 임계값이 약 20% 낮아져 참 내부점을 체계적으로 버리게 되므로, 자유도를 무시한 '약 2배'는 원리 설명으로서 부정확하다.
- 기기 자세 갱신율 — 「세계→기기 6자유도(실시간, 30~60 Hz 갱신)」은 한 자릿수 과소 서술이며 카드 자신의 지연 절과 충돌한다. 실제 AR 파이프라인은 IMU 속도(수백 Hz~약 1 kHz)로 자세를 전파하고 카메라 속도(30~60 Hz)로 시각 갱신을 반영하며, 디스플레이·후단 재투영은 60~120 Hz로 돈다. 자세 갱신이 정말 30~60 Hz에 묶이면 카드가 같은 문서에서 목표로 제시한 motion-to-photon 20 ms 이하, 나아가 타임워프의 프레임 이하 잔여 지연은 원리적으로 달성될 수 없다.
- 타임워프의 잔여 지연 — 「타임워프 계열 기법은 실효 지연을 한 프레임(60 Hz에서 16.7 ms) 수준까지 낮춘다」는 타임워프가 '제거하는 양'을 '도달하는 값'으로 바꿔 적었다. 후단 재투영(late-stage reprojection)은 스캔아웃 직전에 latch한 자세로 이미 렌더된 프레임을 재표본화하므로 잔여 회전 지연은 통상 한 자릿수 ms, 즉 한 프레임보다 훨씬 작다. 그리고 정작 짚어야 할 한계가 빠졌다 — 타임워프가 보정하는 것은 방향이고(깊이를 쓰더라도 병진은 근사에 그친다) 병진 지연과 디스오클루전은 남는다. 카드가 논의하는 근거리 정합에서 결정적인 성분이 바로 그 남는 쪽이다.
- 좌표계 사슬의 개수 — 「세계·기기·카메라·이미지·눈: 고리 4~5개」는 계수 근거가 맞지 않는다. 좌표계 5개를 나열하면 변환 고리는 4개다. 더욱이 '이미지'와 '눈'은 한 사슬에 연달아 오는 두 고리가 아니라 서로 배타적인 종단 — 비디오 시스루는 …→카메라→이미지, 광학 시스루는 …→기기→디스플레이/눈 — 이다. 카드가 뒤에서 두 방식의 근본적 차이를 옳게 구분하므로, 둘을 한 사슬에 직렬로 세운 도입부와 자체 충돌한다.
- (외 18건)

## sensors
항목 16개 · 검증 정정 지적 45건


### MEMS 가속도계 — 정전용량 방식
| 항목 | 내용 |
| --- | --- |
| 수치 | Bosch BMI270 기준: 측정범위 ±2 g(16384 LSB/g) ~ ±16 g(2048 LSB/g), 16비트 분해능. 노이즈 밀도 160 µg/√Hz. 제로-g 오프셋 ±20 mg(= 0.196 m/s²). 출력 데이터율(ODR) 12.5 Hz ~ 1.6 kHz. 동작온도 -40~+85°C. 증명질량은 통상 마이크로그램 수준, 변위는 나노미터 단위. |
| 출처 | Bosch Sensortec BMI270 제품 사양 (bosch-sensortec.com, 2026-09 확인). 원리 서술: Kaajakari, 'Practical MEMS' (2009), Ch.11 Accelerometers; Titterton & Weston, 'Strapdown Inertial Navigation Technology' 2nd ed., §6. |

가속도계는 가속도를 직접 재지 않는다. 아주 작은 질량(증명질량, proof mass)을 스프링으로 매달아 두고, 기기가 가속할 때 그 질량이 관성 때문에 뒤처지는 거리를 잰다. MEMS 방식에서는 이 '거리'를 빗살 모양으로 맞물린 전극 사이의 정전용량 변화로 읽는다. 전극 간격이 좁아지면 정전용량이 커지고, 이 변화는 펨토패럿(10⁻¹⁵ F) 단위여서 전용 증폭 회로가 칩 위에 함께 놓인다. 여기서 중요한 함정이 하나 있다. 아인슈타인의 등가원리 때문에 가속도계는 '가속'과 '중력'을 원리적으로 구별할 수 없다. 정지한 기기를 책상에 두면 가속도계는 0이 아니라 위쪽으로 9.81 m/s²를 출력한다. 따라서 가속도계 출력에서 이동에 의한 가속을 뽑아내려면 기기의 자세(어느 방향이 아래인가)를 먼저 알아야 하고, 그 자세는 자이로가 알려준다. 두 센서가 서로를 필요로 하는 구조가 여기서 시작된다.

### MEMS 자이로스코프 — 진동식 코리올리 원리
| 항목 | 내용 |
| --- | --- |
| 수치 | Bosch BMI270 기준: 범위 ±125 dps(262.1 LSB/dps) ~ ±2000 dps(16.4 LSB/dps). 노이즈 밀도 0.007 dps/√Hz(= 각도 랜덤워크 약 0.42 °/√hr). 제로-레이트 오프셋 ±0.5 dps. ODR 25 Hz ~ 6.4 kHz. 가속도계+자이로 합산 소비전류 685 µA(전 ODR 동작, 3.3V 기준 약 2.3 mW). 구동 진동 주파수는 통상 3~30 kHz, 감지 변위는 피코미터~나노미터. |
| 출처 | Bosch Sensortec BMI270 제품 사양 (2026-09 확인). 코리올리 원리: Titterton & Weston, 'Strapdown Inertial Navigation Technology' 2nd ed., §4.4 Vibratory gyroscopes; IEEE Std 952-2020 (Fiber Optic Gyro 용어지만 바이어스 정의 표준). |

MEMS 자이로에는 회전하는 팽이가 없다. 대신 증명질량을 한 방향으로 계속 진동시켜 둔다(구동 모드, 통상 수 kHz). 이 상태에서 칩 전체가 회전하면, 진동하는 질량에는 진동 방향과 회전축 모두에 수직인 코리올리 힘 F = -2m(ω × v)가 작용한다. 이 힘이 질량을 옆으로 아주 조금 흔들고(감지 모드), 그 옆흔들림의 크기가 회전 각속도 ω에 비례한다. 핵심은 이 센서가 '각도'가 아니라 '각속도'를 준다는 점이다. 각도를 얻으려면 적분해야 하고, 적분은 오차를 누적시킨다. 또한 구동 진동과 감지 진동이 완벽히 직교하지 않으면 회전이 없어도 감지 모드에 신호가 새어 들어오는데(구적 오차, quadrature error), 이것이 온도에 따라 변하는 것이 바이어스 드리프트의 주된 물리적 원인이다. 그래서 자이로 사양표에서 가장 중요한 숫자는 측정 범위가 아니라 제로-레이트 오프셋과 그 온도 계수다.

### 드리프트의 수학 — 바이어스가 t, t², t³로 자라는 이유
| 항목 | 내용 |
| --- | --- |
| 수치 | 보정 전 사양값으로 계산(BMI270 기준). 가속도계 b_a = 20 mg = 0.196 m/s² → 위치 오차 ½b_a t²: t=1초에 9.8 cm, t=10초에 9.8 m. 자이로 b_g = 0.5 dps = 8.73×10⁻³ rad/s → 각도 오차: t=10초에 5.0°, 위치 오차 (1/6)g·b_g·t³: t=1초에 1.4 cm, t=10초에 14.3 m, t=60초에 3.1 km. 온라인 보정 후 잔여 바이어스를 0.01 dps(≈36 °/hr)로 낮추면 t=10초에 28 cm로 줄어든다. 참고 실측 인용: 100 mg급 저가 가속도계는 약 10초 만에 50 m 정확도를 잃고, 10 µg급 최고급은 약 17분간 유지한다. |
| 출처 | 오차 전파 관계식: Titterton & Weston, 'Strapdown Inertial Navigation Technology' 2nd ed., §12 Error propagation / Groves, 'Principles of GNSS, Inertial and Multisensor Integrated Navigation Systems' 2nd ed., §5.7. 인용 문장 및 50 m 예시: Wikipedia 'Inertial measurement unit' (2026-09 확인) — "a constant error in attitude rate (gyro) results in a quadratic error growth in velocity and a cubic error growth in posit |

IMU만으로 위치를 추정하는 것을 관성항법(dead reckoning)이라 한다. 이때 오차가 자라는 방식에는 뚜렷한 위계가 있다. 첫째, 자이로에 상수 바이어스 b_g가 있으면 각속도를 한 번 적분해 얻는 자세 오차는 b_g·t로 시간에 비례해 자란다. 둘째, 가속도계 바이어스 b_a는 두 번 적분되어 위치 오차 ½·b_a·t²를 만든다 — 시간의 제곱이다. 셋째이자 가장 치명적인 것: 자세가 b_g·t만큼 틀어지면 기기는 중력 벡터의 방향을 잘못 알게 되고, 지구 중력 g의 일부(≈ g·b_g·t)가 '수평 가속'으로 잘못 해석된다. 이 가짜 가속을 두 번 적분하면 위치 오차는 (1/6)·g·b_g·t³, 즉 시간의 세제곱으로 폭발한다. 이것이 IMU 단독 추정이 수 초 이상 버틸 수 없는 근본 이유다. 중력이 오차 증폭기 노릇을 하는 것이다.

### 앨런 분산 — 센서 등급을 읽는 언어
| 항목 | 내용 |
| --- | --- |
| 수치 | 단위 변환: 노이즈 밀도 [°/s/√Hz] × 60 = 각도 랜덤워크 [°/√hr]. BMI270의 0.007 dps/√Hz → 약 0.42 °/√hr. 소비자급 MEMS 자이로의 바이어스 안정도는 통상 5~15 °/hr(0.0014~0.004 dps), 전술급 MEMS는 0.1~1 °/hr, 항법급 광섬유/링레이저 자이로는 0.001~0.01 °/hr. 가속도계 속도 랜덤워크(VRW)는 노이즈밀도 [µg/√Hz]로 표기되며 160 µg/√Hz ≈ 0.094 (m/s)/√hr. |
| 출처 | IEEE Std 647-2006 / IEEE Std 952-2020, Annex C — Allan variance 정의 및 기울기 해석. El-Sheimy, Hou & Niu, 'Analysis and Modeling of Inertial Sensors Using Allan Variance', IEEE Trans. Instrum. Meas. 57(1), 2008. 단위 변환 및 등급 구간은 위 표준과 산업 관행 종합(정확한 등급 경계는 문헌마다 다소 다름). |

센서 사양표의 '노이즈 밀도'와 '바이어스 안정도'는 같은 잡음의 서로 다른 시간대 얼굴이다. 앨런 분산은 정지된 센서를 몇 시간 켜놓고 출력을 기록한 뒤, 평균 구간 길이 τ를 바꿔가며 분산을 계산해 로그-로그 그래프로 그린 것이다. 짧은 τ에서는 그래프가 -1/2 기울기로 내려간다 — 백색잡음(각도 랜덤워크)이 지배하며, 오래 평균낼수록 좋아진다는 뜻이다. 그래프가 바닥을 치는 최저점이 '바이어스 안정도(bias instability)'로, 아무리 오래 평균내도 이보다 잘할 수 없는 한계다. 그 이후 τ가 더 커지면 그래프가 +1/2 기울기로 다시 올라간다 — 느린 온도 변화와 1/f 잡음이 지배하는 구간이다. AR에서 중요한 것은 최저점의 위치와 그때의 τ다. 만약 최저점이 τ=100초에 있다면, 그보다 짧은 시간 척도에서는 카메라가 계속 바이어스를 다시 추정해줘야 한다는 뜻이기 때문이다.

### 스테레오 깊이 — 두 눈의 삼각측량과 Z² 벽
| 항목 | 내용 |
| --- | --- |
| 수치 | 수치 예(f=800 px, B=6 cm, 시차 매칭 정밀도 Δd=0.2 px 가정): Z=1 m → ΔZ=4.2 mm; Z=3 m → ΔZ=3.8 cm; Z=5 m → ΔZ=10.4 cm; Z=10 m → ΔZ=42 cm. 상용 스테레오 모듈(예: Intel RealSense D435 계열) 공칭: B=50 mm, 깊이 오차 <2% at 2 m, 유효 범위 0.3~3 m(실내). 소비전력 통상 1.5~2.5 W(스테레오 + IR 프로젝터 포함). |
| 출처 | 삼각측량 및 오차 전파: Hartley & Zisserman, 'Multiple View Geometry in Computer Vision' 2nd ed., Ch.9-11; Szeliski, 'Computer Vision: Algorithms and Applications' 2nd ed., §12.1. 'displacement d = k/z, k = B·f' 및 무늬 없는 표면 실패: Wikipedia 'Computer stereo vision'(2026-09 확인). 수치 예는 본 조사에서 위 식으로 직접 계산. |

두 대의 카메라를 나란히 놓고 같은 장면을 찍으면, 가까운 물체일수록 두 영상에서 위치 차이(시차, disparity)가 크게 난다. 이 관계는 Z = f·B/d로 정확히 표현된다(Z는 거리, f는 초점거리 픽셀값, B는 두 카메라 간격인 베이스라인, d는 시차 픽셀값). 여기서 결정적인 것은 Z와 d가 반비례한다는 점이다. 이 식을 미분하면 깊이 오차 ΔZ = (Z²/(f·B))·Δd가 나온다 — 거리의 제곱에 비례해 오차가 커진다. 1 m에서 4 mm였던 오차가 10 m에서는 42 cm가 된다. 베이스라인 B를 늘리면 오차가 줄지만, 두 카메라의 공통 시야가 좁아지고 기기가 커진다. 안경형 기기에서 B는 사람 눈 간격인 6~7 cm를 넘기 어렵다. 또 하나의 근본 한계: 시차를 재려면 좌우 영상에서 '같은 점'을 찾아야 하는데, 흰 벽이나 잔잔한 물처럼 무늬 없는 표면에서는 대응점을 찾을 수 없어 깊이가 아예 나오지 않는다.

### 구조광(Structured Light) — 무늬를 던져 대응점을 만든다
| 항목 | 내용 |
| --- | --- |
| 수치 | 위상 이동 기법으로 줄 간격(stripe pitch)의 1/10 수준 표면 디테일 분해 가능, 보간으로 높이 분해능 픽셀의 1/50까지. Kinect v1(PrimeSense PS1080): 적외선 도트 패턴 약 30,000개, 깊이 출력 640×480 @ 30 Hz, 유효 범위 0.8~4.0 m, 무작위 오차가 거리의 제곱으로 증가해 최대 거리 5 m에서 약 4 cm. 파장 830~850 nm. 애플 TrueDepth(Face ID): 도트 프로젝터 약 30,000개 점, 유효 거리 약 25~50 cm. 실외 직사광(약 100,000 lux)에서는 대부분의 IR 구조광이 사실상 동작 불가. |
| 출처 | 원리·한계: Wikipedia 'Structured-light 3D scanner'(2026-09 확인) — 1/10 stripe pitch, 1/50 pixel, 반사면 한계 인용. Kinect v1 정확도 실측: Khoshelham & Elberink, 'Accuracy and Resolution of Kinect Depth Data for Indoor Mapping Applications', Sensors 12(2), 2012. Salvi et al., 'A state of the art in structured light patterns for surface profilometry', Pattern Recognition 43(8), 2010. |

스테레오의 치명적 약점은 무늬 없는 표면에서 대응점을 못 찾는 것이다. 구조광은 이 문제를 무식하고 확실하게 해결한다 — 없으면 만들어 던진다. 적외선 프로젝터가 알려진 패턴(점 뿌리기, 줄무늬, 그레이 코드)을 장면에 투사하고, 옆에 있는 적외선 카메라가 그 패턴이 물체 표면에서 얼마나 휘고 밀렸는지 본다. 프로젝터와 카메라의 기하가 이미 알려져 있으므로, 패턴 한 조각이 영상에서 어디로 이동했는지만 알면 삼각측량으로 그 지점의 거리가 나온다. 즉 구조광은 '프로젝터를 두 번째 카메라로 쓰는 스테레오'다. 정밀도를 높이는 표준 기법은 위상 이동(phase shift)으로, 줄무늬를 조금씩 밀어가며 여러 장 찍으면 줄 간격의 1/10 이하까지 분해할 수 있다. 한계도 분명하다. 강한 햇빛은 투사 패턴을 씻어버리고(적외선 성분이 태양광에 압도된다), 유리·금속 같은 반사면은 빛을 카메라 밖으로 튕기거나 반대로 과포화시키며, 여러 대가 같은 공간에 있으면 패턴이 서로 간섭한다.

### iToF(간접 비행시간) — 위상으로 거리를 재고, 그래서 접히는 거리
| 항목 | 내용 |
| --- | --- |
| 수치 | 모호거리 = c/(2·f_mod): 20 MHz → 7.5 m, 50 MHz → 3.0 m, 100 MHz → 1.5 m. 일반 정확도는 측정 거리의 약 1%. RF 변조 방식의 최대 범위 약 60 m, 프레임률 최대 160 fps. Kinect v2(Xbox One): 깊이 512×424 @ 30 Hz, 유효 범위 0.5~4.5 m, 시야각 70°×60°. 조명 소비전력이 지배적이며 모듈 전체로 통상 1~3 W(Kinect v2 급). 스마트폰용 소형 iToF 모듈은 수백 mW 수준. |
| 출처 | 원리·수식·한계: Wikipedia 'Time-of-flight camera'(2026-09 확인) — 4-tap 위상식, 모호거리, 1% 정확도, 60 m, 160 fps, 멀티패스 인용. Hansard, Lee, Choi & Horaud, 'Time-of-Flight Cameras: Principles, Methods and Applications', Springer 2013, Ch.1-2. Kinect v2 사양: Microsoft 공개 SDK 문서 및 Sarbolandi et al., 'Kinect Range Sensing: Structured-Light versus Time-of-Flight Kinect', CVIU 139, 2015. |

빛의 왕복 시간을 직접 재는 것은 어렵다. 그래서 간접 ToF는 다른 길을 택한다. 적외선 LED/VCSEL의 밝기를 수십 MHz의 사인파나 사각파로 계속 흔들어(변조) 장면에 뿌리고, 돌아온 빛이 원래 파형에 비해 얼마나 위상이 밀렸는지를 잰다. 위상 지연 φ는 왕복 거리에 비례하므로 d = (c/4πf_mod)·φ로 거리가 나온다. 픽셀마다 네 개의 시점(0°, 90°, 180°, 270°)에 전하를 나눠 받는 구조를 두고, 네 값 q1~q4로부터 arctan((q3-q4)/(q1-q2))를 계산해 위상을 얻는다. 여기에 원리적 함정이 있다. 위상은 360°에서 한 바퀴 돌아 0°가 되므로, 측정 거리는 모호거리 c/(2·f_mod)마다 접힌다. 20 MHz로 변조하면 7.5 m 밖 물체가 0 m처럼 보인다. 실무에서는 서로 다른 두세 개의 변조 주파수를 섞어 이 접힘을 풀어낸다(phase unwrapping). 두 번째 함정은 멀티패스다. iToF는 장면 전체를 한꺼번에 비추므로, 벽과 바닥에 두 번 튕겨 들어온 빛이 직접 들어온 빛과 한 픽셀에 섞여 평균 위상을 오염시킨다. 방 구석이 실제보다 둥글고 멀게 측정되는 전형적 오류가 여기서 나온다.

### dToF와 SPAD — 광자 한 알의 도착 시각을 세다
| 항목 | 내용 |
| --- | --- |
| 수치 | 빛의 왕복 시간: 1 cm당 66.7 ps, 1 m당 6.67 ns, 100 m당 667 ns. 따라서 타이밍 분해능 100 ps ≈ 거리 1.5 cm. SPAD 타이밍 지터는 통상 수십~수백 ps(고급 소자 20~50 ps), 사시간 수~수십 ns, 암계수율(DCR)은 화소당 수십~수천 cps(온도에 지수적으로 의존). dToF는 100 m 급 거리에서도 동작. iToF와 달리 모호거리가 펄스 반복 주기로 결정되어 훨씬 멀다. |
| 출처 | SPAD 동작 원리(가이거 모드, >3×10⁵ V/cm, 소광, 사시간, 피코초 지터, DCR, TCSPC 히스토그램): Wikipedia 'Single-photon avalanche diode'(2026-09 확인). Cova, Ghioni, Lacaita, Samori & Zappa, 'Avalanche photodiodes and quenching circuits for single-photon detection', Applied Optics 35(12), 1996. dToF 100 m/667 ns: Wikipedia 'Time-of-flight camera'(2026-09 확인). 왕복시간 수치는 c=2.998×10⁸ m/s로 직접 계산. |

직접 ToF는 정공법이다. 아주 짧은 레이저 펄스를 쏘고, 반사된 빛이 언제 돌아왔는지 그 시각을 직접 잰다. 문제는 척도다. 빛은 1 cm 왕복에 약 66.7 피코초밖에 안 걸린다. 1 cm 분해능을 원하면 66 ps를 구별해야 하고, 이건 보통 포토다이오드로는 불가능하다. 그래서 SPAD(단일광자 애벌랜치 다이오드)가 등장한다. SPAD는 항복전압보다 더 높은 역전압을 걸어 놓은 다이오드다(가이거 모드). 이 상태에서 광자 하나가 들어와 전자 하나를 만들면, 3×10⁵ V/cm를 넘는 강한 전기장이 그 전자를 가속해 충돌 이온화를 일으키고, 이것이 눈사태처럼 번져 측정 가능한 전류 펄스가 된다. 광자 하나가 수십억 개의 전하로 증폭되는 것이다. 이 사태는 스스로 멈추지 않으므로 소광(quench) 회로가 전압을 항복전압 아래로 끌어내려 꺼야 하고, 그동안(사시간, dead time) 새 광자를 못 받는다. 여기에 두 번째 아이디어가 붙는다. 단일 펄스의 반사광은 햇빛 잡음에 묻히므로, 같은 방향으로 수천~수만 번 쏘고 도착 시각을 히스토그램으로 쌓는다(TCSPC). 잡음은 시간축에 고르게 퍼지지만 진짜 신호는 같은 시간 칸에 반복해서 쌓이므로, 히스토그램의 봉우리가 곧 거리다. 이 통계적 누적이 dToF가 밝은 야외에서도 동작하는 비결이다.

### 아이폰 프로의 LiDAR Scanner — 실제로 들어있는 것
| 항목 | 내용 |
| --- | --- |
| 수치 | 애플 공식 표현으로 유효 작동 거리 약 5 m 이내. 파장 940 nm 대역 VCSEL. 널리 인용되는 분해점 수는 24×24 = 576점이지만 애플 공식 사양이 아니다(uncertain 참조). ARKit 깊이 API 출력은 256×192 @ 60 Hz의 깊이 맵(이는 라이다 원시 분해능이 아니라 융합 후 결과). 독립 평가에서 보고된 거리 오차는 근거리(1~2 m)에서 약 1 cm, 5 m 부근에서 수 cm~10 cm 수준. 실외 직사광에서 유효 거리가 크게 줄어든다. |
| 출처 | Apple, 'ARKit Depth API / Scene Reconstruction' 개발자 문서 및 iPad Pro(2020) 제품 페이지의 '최대 5미터' 표현. SystemPlus Consulting / TechInsights의 iPhone 12 Pro 라이다 분해 보고서(VCSEL+SPAD 구성 및 940 nm 확인). 정확도 실측: Luetzenburg, Kroon & Bjørk, 'Evaluation of the Apple iPhone 12 Pro LiDAR for an Application in Geosciences', Scientific Reports 11, 2021. ※ 576점 수치는 2차 보도 기반으로 1차 확인되지 않음. |

애플이 iPhone 12 Pro와 iPad Pro(2020)부터 넣은 'LiDAR Scanner'는 자동차용 회전식 라이다와 전혀 다르다. 움직이는 부품이 없는 고정형 플래시 dToF다. 940 nm 대역의 VCSEL 어레이가 회절광학소자(DOE)를 통과해 격자 형태의 적외선 점 패턴을 장면에 던지고, 그 반사광을 SPAD 어레이가 받아 각 점마다 광자 도착 시각 히스토그램을 쌓는다. 즉 구조광처럼 점을 뿌리되 삼각측량이 아니라 시간으로 거리를 푸는 방식이다. 출력은 조밀한 깊이 영상이 아니라 수백 개 수준의 희소한 거리 점이며, 이 희소 점군을 카메라 영상 및 VIO 추정과 융합해 조밀한 깊이 지도로 채워 올리는 것은 소프트웨어(ARKit의 Scene Reconstruction, Depth API)의 몫이다. 이 구조를 이해하면 실제 체감 성능이 설명된다 — 라이다는 평면의 위치와 스케일을 순간적으로 확정해주지만, 물체의 미세한 형태를 재현하는 것은 여전히 카메라 기반 추정이다.

### 이벤트 카메라 — 프레임을 버린 눈
| 항목 | 내용 |
| --- | --- |
| 수치 | 타임스탬프 분해능 마이크로초 단위. 실제 지연시간은 조건에 따라 수십 µs ~ 수 ms(신호 대비, 조도, 센서 설계에 의존). 다이내믹 레인지 120 dB(비교: Nikon D850 등 고급 DSLR 44.6 dB, 일반 CMOS 60~70 dB). 해상도 변천: 2014년 128×128급 → 2019년 640×480 → 현재 0.1~1 MP(Prophesee/Sony IMX636은 1280×720). 대비 임계값은 통상 10~25%. 소비전력은 이벤트 발생량에 비례해 변동하며 정적 장면에서 수 mW 수준까지 내려간다. |
| 출처 | 원리·사양(마이크로초 타임스탬프, 120 dB, 44.6 dB 비교, 해상도 변천, 임계값 기반 픽셀 회로): Wikipedia 'Event camera'(2026-09 확인). Gallego et al., 'Event-based Vision: A Survey', IEEE TPAMI 44(1), 2022 — 이 분야의 표준 서베이. Lichtsteiner, Posch & Delbruck, 'A 128×128 120 dB 15 µs Latency Asynchronous Temporal Contrast Vision Sensor', IEEE JSSC 43(2), 2008 — 원조 논문. |

일반 카메라는 초당 30번, 모든 픽셀을 한꺼번에 읽는다. 문제는 대부분의 픽셀이 이전 프레임과 거의 같다는 것 — 즉 대역폭과 전력의 대부분이 '변하지 않았다'는 정보를 전송하는 데 쓰인다. 이벤트 카메라(DVS, Dynamic Vision Sensor)는 이 전제를 뒤집는다. 각 픽셀이 독립적·비동기적으로 동작하며, 자기가 마지막으로 보고한 밝기를 기준값으로 저장해두고 현재 밝기와 계속 비교한다. 차이가 임계값을 넘는 순간에만 기준값을 갱신하고 '이벤트'를 내보낸다 — (x, y, 시각, 밝아짐/어두워짐) 네 값이 전부다. 결정적인 설계는 비교를 밝기의 로그값으로 한다는 점이다. 로그 차이는 곧 상대적 대비(몇 퍼센트 변했는가)이므로, 어두운 곳이든 눈부신 곳이든 같은 임계값이 통한다. 이것이 120 dB라는 비상식적 다이내믹 레인지의 원천이다. 프레임 노출 시간이라는 개념 자체가 없으므로 모션 블러도 원리적으로 존재하지 않는다. 대가도 있다. 텍스처가 있고 움직여야만 데이터가 나오므로 정지 장면에서는 아무것도 보이지 않고, 출력이 비동기 이벤트 스트림이라 기존 컴퓨터 비전 알고리즘을 그대로 쓸 수 없다.

### 자기장 센서 — 실내에서 나침반이 미치는 이유
| 항목 | 내용 |
| --- | --- |
| 수치 | 지구 자기장 총세기 약 20~80 µT(20,000~80,000 nT), 중위도 지표에서 대략 25~65 µT. 스마트폰 자력계의 전형적 분해능 약 0.1~0.6 µT, 측정범위 ±1,000~±4,900 µT(자석 근접 시 포화 방지), 출력률 10~100 Hz, 소비전류 수백 µA(연속 동작). 실내 철골 건물에서는 국소 왜곡이 수십 µT에 달해 헤딩 오차가 수십 도까지 발생하며, 같은 층에서 수 미터 이동만으로 방위가 20~30° 흔들리는 사례가 흔하다. 노트북·무선충전기 근처에서는 100 µT 이상의 오염도 발생한다. |
| 출처 | AMR 퍼멀로이 원리, 1 µs 이하 응답, 지구 자기장 20,000~80,000 nT: Wikipedia 'Magnetometer'(2026-09 확인). 하드아이언/소프트아이언 보정 모델: Renaudin, Afzal & Lachapelle, 'Complete Triaxis Magnetometer Calibration in the Magnetic Domain', Journal of Sensors, 2010. 실내 자기장 왜곡 실측: Li, Gallagher, Dempster & Rizos, 'How feasible is the use of magnetic field alone for indoor positioning?', IPIN 2012. ※ 개별 스마트폰 자력계 수치는 제조사별 편차가 크다. |

스마트폰의 자력계는 주로 이방성 자기저항(AMR) 소자나 홀 효과 소자를 쓴다. AMR은 퍼멀로이(니켈-철 합금) 박막의 전기저항이 자화 방향과 전류 방향의 각도에 따라 변하는 성질을 이용하며, 응답이 1 µs 이하로 빠르고 반도체 공정으로 대량생산할 수 있다. 자력계의 역할은 자이로가 알 수 없는 것 하나를 메우는 것이다 — 중력은 '아래'를 알려주지만 '북쪽'은 알려주지 못하므로, 요(yaw) 각의 절대 기준은 지자기밖에 없다. 문제는 지자기가 매우 약하고 쉽게 오염된다는 점이다. 왜곡은 두 종류로 나뉜다. 하드아이언 왜곡은 기기에 붙은 영구자석(스피커, 진동모터, 자석식 케이스)이 만드는 고정 오프셋으로, 측정값 구(球)의 중심을 원점에서 밀어낸다. 소프트아이언 왜곡은 주변 강자성체가 지자기를 굴절시켜 구를 타원체로 일그러뜨린다. 보정은 기기를 8자로 흔들어 측정점들을 모은 뒤, 그 점군에 타원체를 맞춰 중심(하드아이언)과 축비(소프트아이언)를 풀어내는 방식이다. 그러나 건물 철골, 엘리베이터, 배선의 전류가 만드는 왜곡은 위치에 따라 달라지므로 어떤 보정으로도 근본적으로 제거되지 않는다.

### GNSS — 야외 절대 위치의 미터 벽
| 항목 | 내용 |
| --- | --- |
| 수치 | 단일 주파수 L1 C/A 기준: 개활지 수평 정확도 약 3~5 m (95%), 도심 협곡에서는 10~50 m로 악화. 오차 예산(보정 전, 1σ 근사): 이온층 지연 최대 약 5 m(모델 보정 후 1~2 m), 대류권 약 0.5 m, 위성 시계·궤도 약 1 m, 수신기 잡음 0.3~1 m, 도심 멀티패스 수 m~수십 m. 이중주파수(L1+L5) 스마트폰은 양호한 조건에서 1~2 m. 위치 갱신률은 통상 1~10 Hz(관성 센서의 200~1000 Hz와 두 자릿수 차이). 소비전력 수신기 단독 20~50 mW 수준. L1 반송파 주파수 1575.42 MHz, 파장 19.03 cm. |
| 출처 | 오차 예산 및 DOP·UERE 구조: Kaplan & Hegarty, 'Understanding GPS/GNSS: Principles and Applications' 3rd ed., Ch.7 (Performance) 및 US DoD 'Global Positioning System Standard Positioning Service Performance Standard', 5th ed., 2020. 도심 멀티패스 및 스마트폰 이중주파수 성능: van Diggelen, 'End Game for Urban GNSS: Google's Use of 3D Building Models', GPS World / ION 자료. ※ 구체적 수치 범위는 문헌과 수신기에 따라 편차가 있어 대표값으로 제시. |

GNSS 수신기는 각 위성이 보낸 신호가 도착하기까지 걸린 시간에 빛의 속도를 곱해 거리를 구한다. 네 개 이상의 위성이 있으면 3차원 위치와 수신기 시계 오차를 동시에 풀 수 있다. 정확도를 결정하는 것은 두 가지의 곱이다. 하나는 거리 측정 오차(UERE)로, 여기엔 이온층 지연, 대류권 지연, 위성 시계·궤도 오차, 그리고 수신기 잡음과 멀티패스가 모두 들어간다. 다른 하나는 기하학적 희석(DOP)으로, 위성들이 하늘에 고르게 퍼져 있으면 작고 한쪽에 몰려 있으면 커진다. 도심에서 정확도가 급격히 나빠지는 이유가 여기 있다 — 건물이 하늘을 가려 DOP가 커지고, 동시에 신호가 벽에 반사되어 실제보다 긴 경로로 들어오는 멀티패스가 발생한다. 멀티패스는 보정 신호로도 제거되지 않는 국소 오차라 특히 고약하다. 최근 스마트폰이 L1과 L5 두 주파수를 함께 받게 되면서 이온층 지연을 직접 소거하고 L5의 넓은 대역폭으로 멀티패스를 억제할 수 있게 되어, 조건이 좋으면 1~2 m까지 내려간다.

### RTK — 반송파 위상으로 센티미터까지 내려가기
| 항목 | 내용 |
| --- | --- |
| 수치 | 단일 기준국 RTK 정확도: 수평 8 mm + 1 ppm, 수직 15 mm + 1 ppm. 여기서 1 ppm은 기선 10 km당 1 cm를 뜻한다. 유효 기선 거리 약 20 km 이내; 가장 가까운 기준국이 50 km를 넘으면 가상기준점(VRS) 방식을 쓴다. 모호정수 확정(fix) 수렴 시간은 조건에 따라 수 초~수십 초, 신호가 끊기면 재수렴이 필요하다. L1 파장 19.03 cm — 모호정수를 한 사이클 틀리면 오차가 그만큼 뛴다. 갱신률 1~20 Hz. 코드 기반 측정의 한계를 만드는 C/A 칩 길이는 약 293 m. |
| 출처 | 정확도 수치(8 mm + 1 ppm 수평, 15 mm + 1 ppm 수직), 20 km 기선, 50 km VRS, 19 cm 파장 오차: Wikipedia 'Real-time kinematic positioning'(2026-09 확인). 모호정수 해결 알고리즘: Teunissen, 'The least-squares ambiguity decorrelation adjustment: a method for fast GPS integer ambiguity estimation', Journal of Geodesy 70, 1995. 이론 전반: Hofmann-Wellenhof, Lichtenegger & Wasle, 'GNSS — Global Navigation Satellite Systems', Springer 2 |

일반 GNSS는 신호에 실린 코드(C/A)의 도착 시각을 재는데, 코드 한 칩의 길이가 약 293 m라 시각을 아무리 잘 재도 미터 단위가 한계다. RTK는 대신 반송파 자체의 위상을 잰다. L1 반송파의 파장은 19.03 cm이고 위상은 파장의 1/100까지도 읽을 수 있으므로 원리적으로 밀리미터 급 관측이 가능하다. 그런데 치명적 미지수가 있다 — 위성과 수신기 사이에 반송파가 정확히 몇 파장 들어있는지(정수 모호정수, integer ambiguity)를 모른다. 위상은 한 파장 안의 소수 부분만 알려주기 때문이다. 이 정수를 틀리면 오차는 곧바로 파장의 배수, 즉 19 cm 단위로 뛴다. RTK의 핵심은 두 가지다. 첫째, 위치를 정확히 아는 기준국(base)의 관측값을 이동국(rover)에 실시간으로 보내 차분을 취하면, 두 수신기가 공유하는 오차(이온층·대류권 지연, 위성 시계·궤도 오차)가 거의 상쇄된다. 둘째, 남은 정수 모호정수는 여러 위성·여러 시각의 관측을 모아 통계적으로 탐색해 확정한다(LAMBDA 알고리즘이 표준). 기준국과 멀어질수록 대기 오차가 더 이상 공통이 아니게 되어 정확도가 거리에 비례해 나빠진다 — 사양에 붙는 '1 ppm'이 바로 이 항이다.

### 센서 융합이 필요한 이유 — 주파수 영역에서 본 상보성
| 항목 | 내용 |
| --- | --- |
| 수치 | 전형적 주파수: IMU 200~1000 Hz, 카메라 30~60 Hz, GNSS 1~10 Hz, 자력계 10~100 Hz. 카메라 프레임 간격 30 Hz = 33.3 ms이며, 이 구간을 IMU가 메운다 — 앞의 t³ 계산으로 33 ms 동안의 위치 오차는 잔여 바이어스 0.01 dps 기준 약 0.01 mm 수준으로 무시할 만하다. 스케일 관측성을 얻으려면 일정 수준 이상의 가속 여기(excitation)가 필요하며, 등속 직선 운동만 하면 스케일이 다시 미관측 상태가 된다. 보고되는 VIO 이동거리 대비 누적 드리프트는 통상 0.1~1% 수준(환경과 시스템에 크게 의존, uncertain 참조). |
| 출처 | 상보성 및 스케일 관측성: Huang, 'Visual-Inertial Navigation: A Concise Review', ICRA 2019; Mourikis & Roumeliotis, 'A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation', ICRA 2007(MSCKF 원조). 관측성 해석: Kelly & Sukhatme, 'Visual-Inertial Sensor Fusion: Localization, Mapping and Sensor-to-Sensor Self-Calibration', IJRR 30(1), 2011. VIO 정의: Wikipedia 'Visual odometry'(2026-09 확인, 단 정량적 드리프 |

어떤 센서도 혼자서는 AR을 지탱하지 못한다. 그런데 왜 여럿을 합치면 되는가. 답은 각 센서의 오차가 서로 다른 시간 척도에 살고 있기 때문이다. IMU는 200~1000 Hz로 동작해 짧은 시간의 움직임을 훌륭히 잡아내지만, 오차가 t³로 자라 긴 시간에서는 쓸모없다 — 고주파에서 강하고 저주파에서 약하다. 카메라는 30~60 Hz로 느리고 모션 블러와 무늬 없는 벽에 취약하지만, 같은 특징점을 다시 보면 누적 오차가 리셋된다 — 저주파에서 강하고 고주파에서 약하다. 둘을 합치면 IMU가 프레임 사이 20~30 ms를 메우고 카메라가 주기적으로 IMU의 바이어스를 다시 추정해 붙잡아 준다. 여기에 결정적 보너스가 있다. 단안 카메라만으로는 장면의 절대 크기를 알 수 없다 — 작은 방을 가까이서 본 것인지 큰 방을 멀리서 본 것인지 구별 불가능하다(스케일 모호성). 그런데 가속도계는 m/s²라는 물리 단위로 측정하므로, 기기가 충분히 가속하기만 하면 스케일이 관측 가능해진다. 이것이 시각-관성 주행계(VIO)가 단안 카메라만으로도 미터 단위 지도를 만들 수 있는 이유이고, 동시에 '기기를 좌우로 조금 움직여 주세요'라는 AR 앱의 초기화 안내가 존재하는 이유다.

### 칼만 필터 — 불확실성의 크기로 믿음을 배분하는 장치
| 항목 | 내용 |
| --- | --- |
| 수치 | 칼만 이득 K_k = P_{k\|k-1}·H_kᵀ·S_k⁻¹, 여기서 S_k = H_k·P_{k\|k-1}·H_kᵀ + R_k(관측 잡음 공분산). 전형적 VIO 필터의 상태 벡터 차원: 자세(3) + 위치(3) + 속도(3) + 자이로 바이어스(3) + 가속도계 바이어스(3) = 15차원 기본형, MSCKF는 과거 카메라 자세들을 슬라이딩 윈도우로 유지해 수십~수백 차원. 필터는 IMU 속도(200~1000 Hz)로 예측하고 카메라 속도(30~60 Hz)로 갱신한다. 주목할 점: 자이로·가속도계 바이어스가 상태에 포함되어 실시간으로 추정·제거되며, 이것이 앞서 본 t³ 오차를 실용 수준으로 억누르는 메커니즘이다. |
| 출처 | 예측/갱신 구조, 칼만 이득 공식 및 불확실성 가중 해석: Wikipedia 'Kalman filter'(2026-09 확인). 원전: R.E. Kálmán, 'A New Approach to Linear Filtering and Prediction Problems', Journal of Basic Engineering 82(1), 1960. 오차상태 정식화: Sola, 'Quaternion kinematics for the error-state Kalman filter', arXiv:1711.02508, 2017 — 이 분야의 사실상 표준 참고문헌. 응용: Groves, 'Principles of GNSS, Inertial and Multisensor Integrated Navigation Systems' |

칼만 필터는 두 단계를 반복한다. 예측 단계에서는 물리 모델(IMU 적분)로 다음 시각의 상태를 추정하고, 동시에 그 추정이 얼마나 못 미더운지를 공분산 행렬 P로 함께 키운다. 갱신 단계에서는 실제 관측(카메라가 본 특징점)이 들어오면, 예측값과 관측값의 차이(혁신, innovation)를 계산해 상태를 수정한다. 핵심은 '얼마나 수정할 것인가'이고, 그 가중치가 칼만 이득 K = P·Hᵀ·S⁻¹다. 이 식이 말하는 바는 간단하다 — 예측의 불확실성 P가 크면 관측을 많이 믿고, 관측의 불확실성이 커서 S가 크면 예측을 유지한다. 두 정보원의 신뢰도에 반비례해 자동으로 저울질하는 것이며, 선형·가우시안 가정 아래서 이 배분이 최적임을 증명할 수 있다. 그런데 자세 추정은 본질적으로 비선형이다. 회전은 벡터 공간이 아니라 군(SO(3))에 살고, 쿼터니언은 단위 크기 제약을 가진다. 그래서 실무는 오차상태 칼만 필터(ESKF/MSCKF)를 쓴다 — 큰 상태(현재 자세와 위치)는 비선형 방정식으로 직접 적분하고, 필터는 '참값과 추정값의 작은 차이'만 다룬다. 이 오차는 항상 작으므로 소각 근사가 성립해 선형 필터의 최적성을 거의 그대로 누릴 수 있다. 이것이 거의 모든 AR 기기가 쓰는 구조다.

### 시간 동기화와 롤링 셔터 — 아무도 말하지 않는 마지막 오차
| 항목 | 내용 |
| --- | --- |
| 수치 | 타임스탬프 오차 1 ms × 각속도 1 rad/s = 0.057° 자세 오차 → 3 m 거리에서 3.0 mm 정합 오차. 5 rad/s에서는 15 mm. 롤링 셔터 판독 시간(readout/line scan time)은 스마트폰급 센서에서 통상 10~30 ms, 글로벌 셔터 센서는 0. AR 추적용 카메라가 글로벌 셔터를 채택하는 이유가 여기 있다. 사람이 인지하는 AR 정합 한계는 통상 모션-투-포톤 지연 20 ms 이하를 목표로 하며(움직임부터 화면 갱신까지 전체), 이 예산 안에서 센서 동기화 오차는 1 ms 이하로 관리되어야 한다. |
| 출처 | 시간 오프셋 온라인 추정: Li & Mourikis, 'Online temporal calibration for camera-IMU systems: Theory and algorithms', IJRR 33(7), 2014. 롤링 셔터 보정: Guo et al., 'Efficient Visual-Inertial Navigation using a Rolling-Shutter Camera with Inaccurate Timestamps', RSS 2014. 지연 인지 한계: Ellis, Breant, Manges, Jacoby & Adelstein, 'Factors influencing operator interaction with virtual objects viewed via head-mounted see-t |

여러 센서를 융합하려면 각 측정이 '언제' 일어났는지를 공통 시계로 알아야 한다. 이것이 생각보다 어렵다. 카메라의 타임스탬프는 노출 시작인가 끝인가 중앙인가, 센서 칩에서 나온 시각인가 운영체제가 받은 시각인가, 그 사이에 얼마나 지연됐는가. 이 불일치가 1 ms만 있어도 결과는 눈에 보인다 — 머리를 1 rad/s(초당 약 57°)로 돌리는 중이라면 1 ms의 어긋남은 0.057°의 자세 오차이고, 3 m 앞 가상 물체는 3 mm 흔들린다. 스포츠 동작처럼 5 rad/s로 돌리면 15 mm다. 이 때문에 진지한 AR 하드웨어는 IMU와 카메라를 같은 클록으로 하드웨어 트리거하거나, 소프트웨어로 시간 오프셋 자체를 필터의 상태 변수에 넣어 온라인 추정한다. 두 번째 문제는 롤링 셔터다. 대부분의 CMOS 센서는 한 프레임을 위에서 아래로 줄 단위로 순차 읽기 때문에, 한 장의 사진 안에서 맨 윗줄과 맨 아랫줄의 촬영 시각이 수 ms~수십 ms 차이 난다. 빠르게 움직이면 직선이 기울어지고 화면이 젤리처럼 출렁인다. 융합 관점에서 더 나쁜 것은, 한 프레임의 특징점들이 서로 다른 자세에서 관측됐는데 같은 시각으로 처리된다는 점이다. 그래서 정밀한 VIO는 각 특징점의 관측 시각을 줄 번호로부터 개별 보정한다.

#### 검증에서 잡힌 정정
- [치명적·단위 오류] '센서 융합' 항: "33 ms 동안의 위치 오차는 잔여 바이어스 0.01 dps 기준 약 0.01 mm 수준" — 본문이 제시한 (1/6)g·b_g·t³에 b_g=0.01 dps=1.7453×10⁻⁴ rad/s, t=0.0333 s를 대입하면 (1/6)(9.81)(1.7453e-4)(3.7037e-5)=1.06×10⁻⁸ m = 10.6 nm = 0.0106 µm. 즉 정답은 0.01 µm이고 본문 값은 약 946배(≈3자릿수) 과대. mm↔µm 단위 혼동.
- [단위 규약 혼용] '이벤트 카메라' 항: "다이내믹 레인지 120 dB(비교: Nikon D850 등 고급 DSLR 44.6 dB, 일반 CMOS 60~70 dB)" — 44.6 dB는 DxOMark의 D850 랜드스케이프 DR 14.8 EV를 전력규약 10·log₁₀(2^14.8)=44.55 dB로 환산한 값이고, 이벤트 카메라 120 dB는 진폭규약 20·log₁₀(=10⁶:1=20 stop, Lichtsteiner 2008 정의). 동일 규약이면 D850은 20·log₁₀(2^14.8)≈89 dB. 원 출처(위키백과 'Event camera' 표)가 이미 규약을 섞고 있고, 여기에 20log 기준 '일반 CMOS 60~70 dB'를 병기해 '최고급 DSLR(44.6) < 일반 CMOS(60~70)'라는 물리적으로 불가능한 서열이 만들어졌다. 44.6 dB를 그대로 받으면 D850이 7.4 stop짜리 센서라는 뜻이 된다.
- [전력 계산 오류] 'MEMS 자이로스코프' 항: "소비전류 685 µA(전 ODR 동작, 3.3V 기준 약 2.3 mW)" — BMI270 데이터시트(BST-BMI270-DS000-08) 전기특성표는 VDD typ 1.8 V(범위 1.71~3.6 V)이고 685 µA는 "A+G Normal Mode, VDD=1.8 V, TA=25°C, ODRmax" 조건값. 따라서 1.233 mW이며 3.3 V·2.3 mW는 약 1.83배 과대. 또한 원문 "at full ODR"은 '최대 ODR에서'의 뜻이므로 '전 ODR 동작'은 오역.
- [동작모드 불일치] 같은 문장에서 인용한 자이로 노이즈 밀도 0.007 dps/√Hz는 데이터시트상 nG,nd "Performance mode" 조건값이고, Performance mode 소비전류는 970 µA(=1.75 mW @1.8 V)다. 685 µA(Normal mode)와 0.007 dps/√Hz(Performance mode)를 한 묶음으로 제시한 것은 서로 다른 동작점을 합성한 사양이다.
- [범위 과소] 'MEMS 가속도계' 항: "출력 데이터율(ODR) 12.5 Hz ~ 1.6 kHz" — 이는 Normal mode 구간(ODRA,n 12.5~1600 Hz)뿐이다. 데이터시트 표제 사양은 "0.78 Hz … 1.6 kHz (accelerometer)"이고 Low-power mode는 ODRA,lpm 0.78~400 Hz. 하한이 16배 과대 표기.
- [조건 누락] 'MEMS 가속도계' 항: "노이즈 밀도 160 µg/√Hz"는 데이터시트상 nA,nd = 0.16 mg/√Hz "range = 8g" 조건값인데, 같은 문장이 ±2 g(16384 LSB/g)를 기준처럼 앞세워 조건을 누락했다. 또 "제로-g 오프셋 ±20 mg"은 OffA,life("soldered, over life time") 즉 수명 전체 누적 오프셋 규격이며 초기 typ 오프셋이 아니다.
- [1차 논문 오인용] '아이폰 프로의 LiDAR Scanner' 항: "독립 평가에서 보고된 거리 오차는 근거리(1~2 m)에서 약 1 cm, 5 m 부근에서 수 cm~10 cm 수준" — Luetzenburg, Kroon & Bjørk(Sci Rep 11, 2021) 초록의 실제 문장은 "accurate high-resolution models of small objects with a side length > 10 cm with an absolute accuracy of ± 1 cm"과 "3D models with the dimensions of up to 130 × 15 × 10 m of a coastal cliff with an absolute accuracy of ± 10 cm". 즉 ±1 cm는 '한 변 10 cm 이상 소형 물체 모델'의 정확도, ±10 cm는 '130 m 규모 절벽 모델 전체'의 절대정확도이며, '거리 1~2 m' / '거리 5 m'라는 측距 구간별 오
- [자기모순] '구조광' 항: Kinect v1의 "유효 범위 0.8~4.0 m"라 쓴 직후 "최대 거리 5 m에서 약 4 cm"라고 서술 — 최대거리가 4 m와 5 m로 동시에 주장된다. 4 cm/5 m는 Khoshelham & Elberink(2012)의 실측 최대거리 5 m 기준값이고, 위키백과 'Kinect'의 실사용 범위는 1.2~3.5 m(확장 0.7~6 m), FOV 57°×43°다. 범위 수치의 출처 기준을 통일해야 한다.
- [연도 오류] '이벤트 카메라' 항: "해상도 변천: 2014년 128×128급 → 2019년 640×480" — 128×128 DVS는 본 조사가 스스로 원조 논문으로 인용한 Lichtsteiner, Posch & Delbruck, IEEE JSSC 43(2), 2008이다. 위키백과 서술도 초기 프로토타입이 약 100 픽셀급이었고 640×480은 2019년이라는 것이어서, '2014년 128×128'은 6년 어긋난다.
- [오차예산 과소] 'GNSS' 항: "이온층 지연 최대 약 5 m(모델 보정 후 1~2 m)" — ±5 m는 고전 오차예산표의 1σ 항목값이지 최대치가 아니다. L1 천정방향 이온층 지연은 야간 1~3 m에서 주간·태양극대기 10~20 m까지 오르고, 저고도각 사선경로에서는 수십 m에 달한다. 또 같은 문장의 "위성 시계·궤도 약 1 m"는 동일 예산표의 ephemeris ±2.5 m / satellite clock ±2 m(RSS≈3.2 m)와 충돌한다.
- [출처 귀속 오류] 'iToF' 항: "RF 변조 방식의 최대 범위 약 60 m" — 위키백과 'Time-of-flight camera'는 60 m를 PMD 제품 계열에 한정해 서술하고("PMD ... can provide ranges up to 60 m"), 같은 문단의 SwissRanger는 5~10 m다. RF 변조 iToF의 일반 한계로 제시하면 과대 일반화다.
- [전력 과소·귀속 오류·중간 확신] 'iToF' 항: "모듈 전체로 통상 1~3 W(Kinect v2 급)" — 위키백과가 "about 1 watt"라 한 것은 조명 유닛(illumination unit) 단독 출력이다. Kinect v2 센서는 전용 12 V/2.67 A(≈32 W) 어댑터를 요구하며 실측 소비는 10 W대 중반으로 보고된다. 1~3 W를 'Kinect v2 급 모듈 전체'로 귀속한 것은 자릿수급 과소.
- [규범 오인용] 'MEMS 자이로스코프' 항 출처: "IEEE Std 952-2020 (Fiber Optic Gyro 용어지만 바이어스 정의 표준)" — 952는 단축 간섭형 광섬유자이로 규격이고, 코리올리 진동형 자이로(CVG)에는 전용 표준 IEEE Std 1431(Specification Format Guide and Test Procedure for Coriolis Vibratory Gyros)이 있다. 진동식 원리 항의 근거 표준으로는 1431을 인용해야 한다.
- [원리 서술 부정확] '자기장 센서' 항: "스마트폰의 자력계는 주로 AMR 소자나 홀 효과 소자를 쓴다" — 본 조사가 인용한 위키백과 'Magnetometer'는 홀 소자를 "used in applications where the magnetic field strength is relatively large"로 규정한다. 지구자기장 25~65 µT는 나 홀로의 홀 소자 감도 범위 밖이어서, 홀 기반 스마트폰 자력계(AKM 계열)는 자속집중기(magnetic concentrator)를 반드시 병용한다. 소자 종류를 병렬 대안처럼 쓴 것은 감도 척도를 생략한 서술이다.
- [검증 불가·정정 필요] Titterton & Weston 2nd ed. 절 번호 인용 3건(가속도계 §6, 진동형 자이로 §4.4, 오차전파 §12)은 IET/IEEE 목차 페이지 접근 차단(403/404)으로 확인하지 못했다. 동 판본은 자이로 기술이 3·4장, 가속도계·다중센서 기술이 5장, MEMS가 6장 구성으로 알려져 있어 '가속도계 §6'은 재확인이 필요하다. 절 단위 인용은 대조 전 확정 표기하지 말 것.
- [미출처 수치] 'GNSS' 항 "수신기 단독 소비전력 20~50 mW", '스테레오' 항 "D435 소비전력 1.5~2.5 W", '자이로' 항 "구동 진동 주파수 3~30 kHz"는 제시된 출처 목록 어디에서도 뒷받침되지 않는다(Intel 공식 도메인은 DNS 해석 실패로 대조 불가). 특히 상용 MEMS 자이로 구동 주파수는 통상 10~30 kHz대이며, 하한 3 kHz는 근거 제시가 필요하다.
- [치명·수치] 센서 융합 항목: "카메라 프레임 간격 33.3 ms … 잔여 바이어스 0.01 dps 기준 약 0.01 mm 수준" — 약 950배 과대. (1/6)·g·b_g·t³에 b_g=0.01 dps=1.745e-4 rad/s, t=0.0333 s를 넣으면 1.06e-8 m = 0.011 µm = 1.1e-5 mm다. 같은 조사가 제시한 t=10초 앵커(28 cm)에 (0.0333/10)³=3.7e-8을 곱해도 동일하게 1.06e-8 m이 나오므로, 자기 수치와도 어긋난다.
- [치명·원리] 위 항목의 기제 지목이 역전됨: "앞의 t³ 계산으로 33 ms 동안의 위치 오차는 … 무시할 만하다"고 하지만, 33 ms 구간의 지배항은 t³ 자이로항이 아니다. 가속도계 바이어스 t² 항이 미보정 20 mg에서 0.109 mm, 잔여 1 mg에서도 5.4 µm이고, 속도 랜덤워크(160 µg/√Hz)가 약 5.5 µm로, 둘 다 t³ 항(0.011 µm)보다 3~4자리 크다. 짧은 구간에서 t³가 무해한 이유는 t³가 작아서가 아니라 t²·√t 항이 지배하기 때문이며, 프레임 간극을 t³로 정당화한 논증이 성립하지 않는다.
- [치명·원리] MEMS 가속도계 원리요약이 비력(specific force / proper acceleration)과 중력 등가성을 누락: "기기가 가속할 때 그 질량이 관성 때문에 뒤처지는 거리를 잰다"는 서술은 정지 시 출력이 0임을 함의한다. 실제로 가속도계는 좌표가속도가 아닌 비력을 측정하므로 정지 상태에서 +1 g(9.81 m/s²)를 읽고 자유낙하에서 0을 읽으며, 중력과 가속을 원리적으로 구별할 수 없다. 이것이 관성항법의 출발점이고, 같은 조사의 위치오차식 (1/6)g·b_g·t³에 g가 들어가는 이유(자세 오차가 중력벡터를 잘못 투영) 자체가 이 성질이다. 원리요약과 수식이 서로 모순된다.
- [원리] 앨런 분산 항목: "평균 구간 길이 τ를 바꿔가며 **분산**을 계산해 로그-로그 그래프로 그린 것 … 짧은 τ에서는 그래프가 **-1/2 기울기**로 내려간다" — 기울기와 플롯 대상이 불일치. -1/2은 앨런 **편차** σ(τ)=√(앨런분산)의 기울기이고, 앨런 **분산** σ²(τ)는 같은 백색잡음 구간에서 τ⁻¹(기울기 -1)로 감소한다. IEEE Std 952 Annex C의 관행도 편차를 τ에 대해 플롯한다. 용어를 '앨런 편차(root Allan variance)'로 바꾸거나 기울기를 -1로 고쳐야 한다.
- [원리] 앨런 분산 항목: "'노이즈 밀도'와 '바이어스 안정도'는 같은 잡음의 서로 다른 시간대 얼굴이다" — 물리적으로 틀림. 두 값은 서로 다른 잡음 과정에서 나온다. -1/2 구간은 각속도에 실린 백색잡음(ARW), 평탄한 바닥(bias instability)은 플리커(1/f) 잡음이다. 동일한 잡음이라면 앨런 플롯에 기울기가 다른 두 구간이 생길 이유가 없고, 앨런 분산이 센서 등급 진단 도구가 되는 근거 자체가 사라진다. 또한 0.42 °/√hr(ARW)와 5~15 °/hr(바이어스 안정도)는 차원이 달라 직접 비교·등급 판정이 불가한데 본문은 같은 층위에 나열한다.
- [내부 모순] 이벤트 카메라: "다이내믹 레인지 120 dB(비교: Nikon D850 등 고급 DSLR 44.6 dB, 일반 CMOS 60~70 dB)" — 고급 DSLR이 범용 CMOS보다 DR이 낮다는 물리적으로 불가능한 대소관계. 44.6 dB는 약 7.4스톱에 불과하며, D850의 측정 DR은 약 14.8 EV ≈ 89 dB다. 44.6 dB 수치가 Wikipedia 'Event camera' 비교표에 실제로 존재함은 확인했으므로 인용은 충실하나, 교차검증 없이 옮겨 자기모순 문장을 만들었다. 100페이지 설명서에서는 비교 기준(측정 방식·SNR 정의)을 밝히거나 삭제해야 한다.
- [원리·불완전] 센서 융합: "등속 직선 운동만 하면 스케일이 다시 미관측 상태가 된다" — 퇴화 조건을 너무 좁게 잡음. 단안 관성 융합의 정설(Martinelli; Kelly & Sukhatme IJRR 2011)은 **등가속(constant acceleration)** 운동에서 스케일이 미관측이 된다는 것이고, 등속 직선운동(a=0)은 그 특수경우다. 즉 0이 아닌 일정 가속으로 움직여도 스케일이 풀리지 않는데, 본문 서술은 이 실제 실패모드를 놓친다. 순수 회전 시 병진·스케일 미관측 또한 누락됐다.
- [수치 조건 오류] BMI270 소비전력: "685 µA(전 ODR 동작, 3.3V 기준 약 2.3 mW)" — 685 µA는 정확하나(Bosch 제품 페이지 확인) 이 전류는 데이터시트 스펙 조건 VDD=1.8 V에서의 값이다. 제품 VDD 범위는 1.7~3.6 V이며, 실제 동작점 기준 전력은 약 1.2 mW다. 3.3 V를 곱한 2.3 mW는 실측 조건과 무관하게 약 2배 과대하며, 전력예산 비교(다른 항목의 mW/W 수치들과 나란히 제시됨)를 왜곡한다.
- [출처 귀속 오류] dToF/SPAD 항목이 "사시간 수~수십 ns"와 "DCR 화소당 수십~수천 cps"를 Wikipedia 'Single-photon avalanche diode'에 귀속시키지만, 해당 문서는 최신 소자 기준 "dead times of 1–2 ns"와 "DCRs < 10 Hz"를 말한다(직접 확인). 본문 수치는 dToF용 CMOS SPAD 이미징 어레이에는 타당하지만 인용된 출처가 이를 지지하지 않으므로, 출처를 어레이 문헌으로 교체하거나 '개별 소자 대 어레이'를 구분해야 한다. (>3×10⁵ V/cm, 피코초 지터, 소광, TCSPC 히스토그램은 해당 문서에서 확인됨.)
- [출처 귀속 오류] 스테레오 항목이 "'displacement d = k/z, k = B·f' 및 **무늬 없는 표면 실패**"를 함께 Wikipedia 'Computer stereo vision'에 귀속시키지만, 해당 문서는 d=k/z 관계만 제시하고 무텍스처 표면에서의 대응점 탐색 실패를 명시하지 않는다(smoothness 절의 일반 서술만 존재). 주장 자체는 참이므로 출처를 Hartley & Zisserman / Szeliski 또는 Scharstein & Szeliski 벤치마크 문헌으로 옮겨야 한다.
- [내부 불일치] 구조광 항목: Kinect v1 "유효 범위 0.8~4.0 m"라고 적은 직후 같은 문장에서 "**최대 거리 5 m**에서 약 4 cm"라고 한다. Khoshelham & Elberink(2012)가 5 m를 최대 거리로 다루므로 인용은 정확하지만, 본문이 앞서 선언한 유효범위와 충돌한다. 두 수치의 정의(공칭 동작범위 대 논문 측정 최대거리)를 구분해야 한다.
- [원리 과장] RTK 항목: "코드 한 칩의 길이가 약 293 m라 **시각을 아무리 잘 재도** 미터 단위가 한계다" — 칩 길이는 경성 하한이 아니다. 코드 상관 추적은 통상 칩 길이의 0.5~1%(약 1.5~3 m)까지 분해하며, 미터급 한계는 칩 길이와 추적 정밀도(및 멀티패스)의 곱에서 나온다. 같은 조사가 반송파에 대해서는 "파장의 1/100까지 읽을 수 있다"는 동일 논리를 적용하면서 코드에만 '아무리 잘 재도'를 적용해 비대칭적이다.
- [수치] GNSS 오차 예산: "이온층 지연 **최대** 약 5 m" — 5 m는 천정 방향 전형값에 가깝고, 저고도각·태양활동 극대기에는 수십 m(30 m 이상)까지 커진다. '최대'라는 한정이 부적절하다. 아울러 "위성 시계·궤도 약 1 m"도 고전 GPS 오차예산표(각 약 2.1 m, 1σ)보다 낙관적이어서, 현대 방송궤도력 기준임을 명시하지 않으면 합산 UERE가 과소 추정된다.
- Kaajakari, 'Practical MEMS'(2009) Ch.11은 'Accelerometers'가 아니다. 저자 공식 목차(kaajakari.net/PracticalMEMS/book_toc.shtml)에 따르면 Ch.3 'Accelerometers'(p.33), Ch.11 'Sensor specifications'(p.167), Ch.22 'Gyroscopes'(p.343)다. 가속도계 원리 인용은 Ch.3로 가야 한다.
- (외 15건)

## latency
항목 16개 · 검증 정정 지적 43건


### motion-to-photon 지연의 정의 — 무엇을 어디서부터 어디까지 재는가
| 항목 | 내용 |
| --- | --- |
| 수치 | 목표치: 20ms 이하(Carmack: "약 20밀리초 미만이면 일반적으로 지각되지 않는다"), 50ms는 "반응은 좋지만 미묘하게 늦게 느껴진다". XR 산업 표준 문헌에서 통용되는 예산도 20ms 미만. 단일 값이 아니라 프레임 내 위치별·프레임별로 분포하며, 60Hz 화면에서는 같은 프레임 안에서도 위아래가 16.7ms 차이가 난다. |
| 출처 | John Carmack, "Latency Mitigation Strategies" (2013), Oculus/AltDevBlogADay — 미러본 https://danluu.com/latency-mitigation/ ; Stauffert, Niebling & Latoschik, "Latency and Cybersickness: Impact, Causes, and Measures. A Review", Frontiers in Virtual Reality 1:582204 (2020) |

motion-to-photon(MTP) 지연은 사용자의 머리(또는 손)가 물리적으로 움직인 순간부터, 그 움직임을 반영한 빛이 눈에 도달하는 순간까지의 시간이다. 정의의 핵심은 양 끝점을 모두 '물리 세계'에 두었다는 점이다. 시작점을 '센서가 데이터를 출력한 시각'으로 잡으면 센서 내부 지연이 통째로 숨고, 끝점을 '프레임버퍼에 다 그린 시각'으로 잡으면 스캔아웃과 화소 응답이 숨는다. 증강현실에서 이 숫자가 결정적인 이유는, 사용자가 비교 대상을 손에 쥐고 있기 때문이다. 가상 물체가 늦게 그려지면 그 뒤에 있는 실제 세계가 '정답지' 역할을 해서 어긋남이 즉시 드러난다. 순수 가상현실에서는 비교 대상이 없어 전체가 함께 늦어도 덜 눈에 띄지만, 증강현실에서는 1mm의 어긋남도 보인다. 그래서 VR 업계의 '20ms' 목표는 AR에서는 출발선일 뿐이며, 실제로는 '얼마나 정확히 겹치는가'라는 각도 오차 문제로 다시 번역되어야 한다. 또 하나 중요한 것은 MTP가 단일 숫자가 아니라 분포라는 사실이다. 같은 기기에서도 화면 위쪽 픽셀과 아래쪽 픽셀은 서로 다른 지연을 가지며, 프레임마다 값이 흔들린다.

### 1단계: 센서 샘플링과 전송 — 지연의 첫 번째 관문
| 항목 | 내용 |
| --- | --- |
| 수치 | USB HID 표준 장치: 초당 125 샘플 → 최대 8ms 지터. 일부 USB 하드웨어는 초당 1000회 갱신 가능 → 1ms. 운영체제가 메시지 도착부터 사용자 모드 처리까지 추가로 '최대 수 밀리초'의 무작위 지연을 더한다. 참고: 1995년 당시 최고 성능 자기식 트래커 Polhemus Fastrak의 사양 지연은 4ms, UNC 광학식 트래커는 15~30ms였다. |
| 출처 | John Carmack, "Latency Mitigation Strategies" (2013), 'Sensors' 절 ; Ronald Azuma, "Predictive Tracking for Augmented Reality", UNC-Chapel Hill 박사학위논문 TR95-007 (1995), §5 ; Richard Holloway, "Registration Errors in Augmented Reality Systems", UNC TR95-016 (1995), §6.3.2.3 |

머리의 움직임은 먼저 관성측정장치(IMU)의 자이로스코프·가속도계로 측정된다. 여기서 지연은 두 갈래로 생긴다. 하나는 '샘플링 주기'다. 센서가 초당 125회 값을 내보낸다면, 움직임이 일어난 순간과 그것이 샘플에 잡히는 순간 사이에 최대 8밀리초의 무작위 간격이 생긴다. 이것은 평균 4ms의 지연이자 동시에 0~8ms의 지터(흔들림)다. 다른 하나는 '전송'이다. USB HID 같은 범용 인터페이스는 폴링 기반이라 장치가 준비되어 있어도 호스트가 물어볼 때까지 기다린다. 여기에 운영체제가 메시지를 커널에서 사용자 프로그램으로 넘기는 데 다시 수 밀리초의 예측 불가능한 지연이 붙는다. 그래서 해법은 두 방향이다. 샘플링 주파수를 올려 주기 자체를 줄이거나(1000Hz면 1ms), 타임스탬프를 센서 쪽에서 찍어 '언제 측정된 값인지'를 정확히 알리는 것이다. 후자가 더 중요한데, 지연의 절대값은 예측으로 보상할 수 있지만 '얼마나 늦었는지 모르는 지연'은 보상할 방법이 없기 때문이다. 현대 헤드셋이 IMU를 SoC에 직결하고 하드웨어 타임스탬프를 쓰는 이유가 이것이다.

### 2단계: 센서 융합 — 정확도를 사려고 시간을 지불한다
| 항목 | 내용 |
| --- | --- |
| 수치 | Azuma의 1995년 시스템 실측: 전체 70ms 지연 중 트래커 15~30ms(약 43%), 예측기 계산 약 12ms, 렌더링 16.67ms, 나머지는 통신·동기화 대기. 현대 헤드셋의 IMU는 통상 500~1000Hz(주기 1~2ms), 추적 카메라는 30~90Hz(주기 11~33ms) 수준이다. |
| 출처 | Ronald Azuma, "Predictive Tracking for Augmented Reality", UNC TR95-007 (1995), §5.11 및 §5.3 ; 현대 IMU/카메라 주파수는 업계 통용 범위(개별 기기 사양은 uncertain 참조) |

IMU만으로는 위치를 알 수 없다. 가속도를 두 번 적분하면 오차가 시간의 제곱으로 누적되어 수 초 만에 수 미터가 어긋난다. 그래서 카메라 기반 추적(SLAM)이 절대 기준을 잡아 주고, IMU가 그 사이를 빠르게 메운다. 문제는 두 센서의 시간 상수가 정반대라는 점이다. IMU는 빠르지만(1000Hz) 드리프트하고, 카메라는 정확하지만 느리다(30~90Hz에 노출 시간과 리드아웃 시간이 더해지고, 특징점 추출과 최적화에 다시 수 밀리초가 든다). 칼만 필터류의 융합기는 이 둘을 가중 평균하는데, 카메라 결과가 도착했을 때 그 관측은 이미 과거의 것이므로 '과거 시점으로 되돌아가 상태를 수정하고 현재까지 다시 적분하는' 작업이 필요하다. 이 구조 때문에 융합 단계는 단순한 계산 지연 외에 '관측 지연'이라는 고유한 지연을 갖는다. 실용적 타협은 명확하다. 화면에 내보내는 자세는 IMU가 주도하는 고주파 추정치를 쓰고, 카메라는 천천히 드리프트를 잡아당기게 한다. 그래서 헤드셋은 빠르게 돌릴 때는 매끄럽지만, 가만히 있으면 물체가 아주 천천히 미끄러지는 현상을 보인다.

### 3단계: 애플리케이션과 렌더링 — 파이프라이닝이 만드는 숨은 프레임
| 항목 | 내용 |
| --- | --- |
| 수치 | Carmack이 측정·정리한 전략별 지연: 동기식 렌더링 16~32ms / 파이프라인 이중 CPU 48~64ms / 늦은 프레임 스케줄링 18~34ms / 뷰 바이패스 16~32ms / 타임워프 2~18ms / 연속 타임워프 2~3ms(센서 500Hz 기준). 90Hz = 프레임 간격 약 11ms, 60Hz = 16.6ms. HoloLens 1: 60fps 미달 시 게임·렌더 스레드가 30fps로 떨어지면 추가 33.3ms 지연. |
| 출처 | John Carmack, "Latency Mitigation Strategies" (2013), 'Latency Reduction Strategies' 절 ; Microsoft Learn, "Hologram stability" (Windows Mixed Reality 개발자 문서, Frame rate 절) |

게임 엔진은 보통 CPU가 장면을 준비하고 GPU가 그리는 2단 파이프라인으로 돌아간다. 처리량(초당 프레임 수)은 올라가지만, 대가로 지연이 프레임 단위로 쌓인다. CPU가 n번째 프레임을 준비하는 동안 GPU는 n-1번째를 그리고, 화면은 n-2번째를 보여 준다. 90Hz에서 프레임 하나가 11.1ms이므로, 이 구조만으로 22ms가 붙는다. 동기식으로 돌리면 파이프라인 지연은 사라지지만 프레임률이 절반으로 떨어진다. Carmack이 정리한 여러 전략의 지연 차이가 바로 이 교환 관계를 보여 준다. 더 중요한 함정은 '프레임을 놓쳤을 때'다. 60Hz 목표에서 30Hz로 떨어지면 단순히 느려지는 게 아니라, 같은 그림이 두 번 표시되면서 두 번째 표시분은 16.6ms 더 늙은 그림이 된다. 즉 지연의 평균이 아니라 분산이 커지고, 이것이 저더(judder)와 멀미의 직접적 원인이다. Microsoft가 HoloLens 개발자에게 '30fps로 일정하게 도는 앱이 60fps와 30fps를 오가는 앱보다 낫다'고 못 박는 이유가 이것이다.

### 4단계: 스캔아웃 — 화면의 위와 아래는 같은 시각이 아니다
| 항목 | 내용 |
| --- | --- |
| 수치 | 60Hz 순차 주사: 아래쪽이 위쪽보다 약 16~17ms 늦게 표시. NTSC 인터레이스에서는 마지막 픽셀이 첫 픽셀보다 33ms 이상 늦음. Mine & Bishop 계산: 카메라(머리) 회전 200°/s, 60필드/s, 수평 시야 60°에 600픽셀 → 한 필드 동안 3.3°의 회전 = 33픽셀의 정합 오차. 반대로 스캔라인 단위로 재계산하면 0.013° = 0.13픽셀로 떨어진다(1픽셀 미만). |
| 출처 | Mark Mine & Gary Bishop, "Just-In-Time Pixels", UNC-Chapel Hill 기술보고서 TR93-005 (1993), §1~§2 및 §4.2 ; John Carmack (2013), 'Displays' 절 |

디스플레이는 이미지 전체를 한꺼번에 켜지 않는다. 대부분의 패널은 맨 윗줄부터 아랫줄까지 순차적으로 화소를 갱신한다. 60Hz 화면이라면 맨 아랫줄은 맨 윗줄보다 약 16밀리초 늦게 바뀐다. 그런데 렌더링은 보통 '한 순간의 시점'으로 화면 전체를 계산한다. 즉 화면 전체가 동일 시각의 표본이라고 가정하고 그린 그림을, 시간이 세로로 번지는 장치에 내보내는 것이다. 이 불일치가 기하학적 왜곡으로 나타난다. 머리를 좌우로 돌리는 동안 세로 직선은 진행 방향으로 기울어 보이고, 정지해 있어야 할 물체는 위아래가 어긋난 채로 흔들린다. Mine과 Bishop이 1993년에 제안한 해법 'Just-In-Time Pixels'는 급진적이지만 개념적으로 옳다 — 각 픽셀을 '그 픽셀이 실제로 표시될 시각'의 세계 상태로 계산하라는 것이다. 정지 화면으로 보면 왜곡된 그림이지만, 순차 주사 디스플레이에서 보면 오히려 왜곡이 없다. 현대의 스캔라인 단위 타임워프와 '빔 레이싱'은 이 아이디어의 실용적 근사다.

### 5단계: 화소 응답과 잔상(persistence) — 켜는 시간이 곧 번짐의 길이다
| 항목 | 내용 |
| --- | --- |
| 수치 | 응답 시간: 일반 LCD 패널 약 10ms, 게이밍/3D용 최적화 패널 5ms 미만, OLED 1ms 미만(Carmack 2013). 실측 잔상 시간: Valve Index 0.33ms, Oculus Rift 2ms — Rift의 경우 11.1ms 프레임 중 9.1ms는 화면이 꺼져 있고 마지막 2ms만 켜진다(Warburton et al. 2022). 계산 예(머리 100°/s, 세계 고정 물체 응시): 전체 잔상 11.1ms → 번짐 1.11°(67각분) / 2ms → 0.2°(12각분) / 0.33ms → 0.033°(2각분). 사람 시력의 분해 한계가 약 1각분이므로 0.33ms에서도 겨우 그 두 배 수준이다. |
| 출처 | John Carmack (2013), 'Displays' 절 ; Warburton, M. et al., "Measuring motion-to-photon latency for sensorimotor experiments with virtual reality systems", Behavior Research Methods (2022), doi:10.3758/s13428-022-01983-5, Methods 절(잔상 실측값) ; 번짐 각도는 홀드형 블러 = 속도×홀드시간 관계에서 저자 계산 |

화소가 명령을 받고 실제로 밝기를 바꾸는 데 걸리는 시간이 응답 시간이다. 액정(LCD)은 분자를 물리적으로 회전시켜야 해서 느리고, 유기발광다이오드(OLED)는 전류를 흘리면 바로 빛나므로 압도적으로 빠르다. 그런데 증강현실에서 더 중요한 것은 응답 시간이 아니라 '얼마나 오래 켜져 있는가', 즉 잔상 시간(persistence)이다. 이유는 눈이 움직이기 때문이다. 세계에 고정된 물체를 바라보며 머리를 돌리면, 전정안반사가 눈을 반대 방향으로 회전시켜 시선을 그 물체에 고정한다. 그런데 화면의 그림은 한 프레임 동안 패널 위의 같은 자리에 그대로 켜져 있다. 그 결과 그림은 회전하는 망막 위를 미끄러지고, 켜져 있던 시간만큼 길게 번진다. 번짐의 각도 = 망막 미끄러짐 각속도 × 잔상 시간. 해법은 화소를 프레임 끝에 아주 짧게만 번쩍이는 것이다. 이것이 저잔상(low persistence)이며, 대가는 휘도 손실이다. 같은 밝기를 내려면 켜져 있는 짧은 순간에 훨씬 강하게 발광해야 한다.

### 사람은 언제 지연을 알아채는가 — 연구별 역치
| 항목 | 내용 |
| --- | --- |
| 수치 | Carmack(2013): 약 20ms 미만은 일반적으로 지각되지 않음, 50ms는 반응은 좋으나 미묘하게 늦게 느껴짐. Ellis et al.(1999, 2004) 및 Adelstein et al.(2003): 17ms 이하의 지연도 탐지 가능. Jerald(2010): 최소 지각 역치로 한 참가자에게서 3.2ms 보고. Attig et al.(2017, HMD 아닌 일반 HCI): 100ms 이하에서는 사용성에 영향 없음. Davis et al.(2015): 사람은 최대 500Hz 수준의 시각적 변동도 검출 가능. 이 폭(3.2ms~100ms)이 바로 '과제 의존성'의 크기다. |
| 출처 | Stauffert, Niebling & Latoschik, "Latency and Cybersickness: Impact, Causes, and Measures. A Review", Frontiers in Virtual Reality 1:582204 (2020) — Ellis et al. 1999/2004, Adelstein et al. 2003, Jerald 2010, Attig et al. 2017, Davis et al. 2015를 정리한 표 ; John Carmack (2013) |

'몇 밀리초부터 보이는가'에 대한 답이 연구마다 20ms에서 3.2ms까지 벌어지는 데에는 이유가 있다. 첫째, 무엇을 묻느냐가 다르다. '늦다고 느끼는가'(탐지), '두 조건 중 어느 쪽이 더 늦은가'(변별), '불편한가'(불쾌), '수행이 나빠지는가'(성능)는 서로 다른 네 개의 역치이고, 보통 이 순서대로 숫자가 커진다. 둘째, 자극이 다르다. 고대비의 선명한 모서리가 있는 장면에서 머리를 빠르게 돌리면 미세한 어긋남도 '움직임'으로 보이지만, 흐릿하고 대비가 낮은 장면에서는 같은 지연이 숨는다. 셋째, 개인차가 크다. 훈련된 관찰자는 훨씬 낮은 역치를 보인다. 원리적으로 사람이 지연에 민감한 것은 절대 시간을 재기 때문이 아니라, 지연이 '장면이 스스로 움직이는 것'으로 변환되어 운동 지각 체계에 잡히기 때문이다. 그래서 역치는 밀리초가 아니라 실제로는 '장면 운동 속도(°/s)'의 역치이며, 머리를 빨리 돌릴수록 더 작은 지연이 보인다. 이 점이 이 분야에서 가장 자주 오해되는 부분이다.

### 왜 이렇게 민감한가 — 전정안반사(VOR)라는 상대
| 항목 | 내용 |
| --- | --- |
| 수치 | 각(회전) VOR의 잠복기는 통상 7~15ms로 보고된다(3-뉴런 궁). 비교: 시각 추종(smooth pursuit)의 잠복기는 약 100~130ms, 자발적 반응(버튼 누르기)은 200ms 이상. 즉 VOR은 시각계 자체보다 10배 이상 빠르다. 머리 회전 대역폭은 대부분 2Hz 이하(Azuma 1995 실측 파워스펙트럼)이나, 그 안에서의 순간 각속도는 수백 °/s에 이른다. |
| 출처 | R. John Leigh & David S. Zee, 『The Neurology of Eye Movements』, 5판(Oxford University Press, 2015), 3장 전정안반사 — VOR 잠복기 및 3-뉴런 궁 ; Ronald Azuma, UNC TR95-007 (1995), §3.6 머리 운동 주파수 분석(2Hz 이하) — 정확한 쪽수는 uncertain 참조 |

사람의 눈은 머리가 돌면 자동으로 반대 방향으로 돈다. 귓속의 반고리관이 각속도를 감지해 세 개의 시냅스만 거쳐 눈 근육으로 보내는 이 회로가 전정안반사(VOR)다. 시냅스를 최소로 거치도록 진화한 덕에 이 반사의 지연은 10밀리초 안팎으로, 인체의 어떤 자발적 반응보다도 빠르다. 여기에 증강현실이 처한 곤경의 본질이 있다. 우리는 반응 속도 10ms짜리 생물학적 안정화 장치와 경쟁하고 있는 것이다. 머리가 돌면 눈은 즉시 보정되어 시선이 목표에 고정되는데, 화면 속 가상 물체는 파이프라인 지연만큼 늦게 따라온다. 그 차이가 망막 위의 '미끄러짐'으로 나타나고, 시각계는 이것을 '물체가 스스로 움직였다'고 해석한다. 정지해 있어야 할 물체가 머리 움직임에 맞춰 헤엄치는 현상(swim)이 이렇게 생긴다. 더 나쁜 것은, 시각이 보고하는 움직임과 전정기관이 보고하는 움직임이 불일치하면 뇌가 이를 중독 신호로 해석한다는 감각 갈등 이론이다. 멀미가 단순한 불쾌가 아니라 진화적으로 설계된 경보인 이유다.

### 핵심 계산: 지연 → 각도 오차 → 실제 거리 오차
| 항목 | 내용 |
| --- | --- |
| 수치 | 【계산 1】 ω=50°/s(온건한 회전), Δt=100ms → 오차 5°. 팔 길이 68cm에서 약 60mm 어긋남 — 당시 정적 정합 오차 13mm의 4.5배(Azuma). 【계산 2】 ω=50°/s, Δt=10ms → 0.5°. 1m 앞 물체에서 약 9mm(Azuma). 【계산 3】 ω=100°/s, Δt=20ms → 2.0°. 1m 앞에서 약 35mm. 【계산 4】 ω=300°/s(급격한 회전 최대치), Δt=20ms → 6°. 1m 앞에서 약 105mm. 【Holloway의 경험칙】 최대 머리 속도 500mm/s·50°/s, 물체 거리 500mm 조건에서 회전 기여 0.44mm/ms + 병진 기여 0.5mm/ms ≈ 지연 1ms당 정합 오차 1mm. 평균 속도(164mm/s, 20°/s)에서는 약 0 |
| 출처 | Richard Holloway, "Registration Errors in Augmented Reality Systems", UNC TR95-016 (1995), §6.3.2.3, pp.131-132 (식 6.3.2.3.1, 6.3.2.3.2 및 1mm/ms 경험칙) ; Ronald Azuma, UNC TR95-007 (1995), §1.4, pp.12-13 및 §5.6 |

이 장의 모든 논의가 하나의 식으로 수렴한다. 각도 오차 = 머리 각속도 × 지연. 이 식이 성립하는 이유는 간단하다. 시스템이 Δt 전의 머리 자세로 그림을 그렸다면, 그 그림은 머리가 Δt 동안 돈 각도만큼 틀어진 자리에 놓인다. 각속도가 ω일 때 틀어진 각도는 정확히 ω·Δt다. 이 각도 오차를 눈에 보이는 거리 오차로 바꾸려면 물체까지의 거리를 곱한다(작은 각도에서 오차 ≈ 거리 × 각도(라디안)). 여기서 두 가지 성질이 드러난다. 첫째, 각도 오차는 거리와 무관하다 — 멀리 있든 가까이 있든 똑같이 틀어진다. 둘째, 물리적 거리 오차는 거리에 비례한다 — 그래서 멀리 있는 물체일수록 같은 지연에서 더 크게 어긋난다. 병진 운동도 마찬가지 방식으로 더해진다. 머리가 초속 v로 움직이면 Δt 동안 v·Δt만큼 위치가 어긋나고, 이것은 거리와 무관한 절대 오차다. Holloway는 이 둘을 합친 모델로 회전 성분과 병진 성분이 대략 같은 크기로 기여함을 보였다.

### 머리는 얼마나 빨리 움직이는가 — 각속도의 실측 분포
| 항목 | 내용 |
| --- | --- |
| 수치 | Azuma 실측(HMD 착용, 데모 응용): 느린 시퀀스 최대 70°/s, 빠른 시퀀스 최대 120°/s. 값의 약 절반이 10°/s 이하. 빠른 시퀀스에서 상위 10%가 40~120°/s 구간. Holloway 실측(수술 계획 과제): 평균 각속도 20~26°/s, 대부분 50°/s 및 500mm/s 이하, 보수적 상한으로 50°/s·500mm/s 채택. List(1983, 비행 시뮬레이터, 표적 응시): 최대 각속도 76~240°/s. Smith(1984, CAE 시뮬레이터): 최대 300°/s. Mine & Bishop이 인용한 전형적 머리 운동 최대치 370°/s. 주파수: 신호 에너지 거의 전부가 2Hz 이하(Azuma, So 1992와 일치). |
| 출처 | Ronald Azuma, UNC TR95-007 (1995), §1.4 Figures 1.7~1.9, pp.12-13 및 §3.6 ; Richard Holloway, UNC TR95-016 (1995), §6.3.2.3 p.131 및 §7.2.2 ; List (1983), Smith (1984) — Azuma/Mine & Bishop을 통한 2차 인용 |

지연을 오차로 환산하려면 머리가 실제로 얼마나 빨리 도는지를 알아야 한다. 이것은 추정이 아니라 측정된 값이다. 놀라운 사실은 분포가 극단적으로 비대칭이라는 점이다. 사용자는 대부분의 시간을 매우 느리게 움직이며 보내고, 아주 짧은 순간에만 빠르게 돈다. 그런데 '빠르게 도는 그 짧은 순간'이 바로 지연 오차가 가장 크게 드러나는 순간이다. 평균 각속도로 시스템을 설계하면 평소에는 괜찮지만 결정적 순간에 무너진다. 또 한 가지 중요한 사실은 머리 운동의 주파수 대역폭이 좁다는 것이다. 머리와 목은 관성이 있고 근육의 출력에 한계가 있어서, 신호 에너지의 거의 전부가 2Hz 이하에 있다. 이것이 예측(prediction)이 원리적으로 가능한 근거다 — 2Hz 이하로 대역이 제한된 신호는 짧은 구간이라면 외삽할 수 있다. 반대로 이 사실은 예측의 한계도 정해 준다. 2Hz 신호는 10초 안에 여러 번 방향을 바꾸므로 긴 예측은 원리적으로 불가능하다.

### 완화 기법 1: 예측(prediction) — 미래의 머리 자세를 그린다
| 항목 | 내용 |
| --- | --- |
| 수치 | Azuma 실측: 관성센서를 쓴 예측은 예측 없음 대비 평균 5~10배, 관성센서 없는 예측 대비 2~3배 정확. 실효 한계는 예측 구간 약 80ms 이하. 예측 구간을 25ms에서 200ms까지 늘리면 무예측 곡선은 선형으로, 예측 곡선은 그보다 빠르게 증가 — 500ms 지점에서는 두 예측 방식 모두 무예측보다 나빠진다. 예측 구간 추정 오차 10ms → 50°/s에서 0.5° 오차 → 1m 거리에서 약 9mm. Azuma의 최종 시스템은 온건한 머리 속도에서 4~5mm의 동적 정합을 달성. |
| 출처 | Ronald Azuma, "Predictive Tracking for Augmented Reality", UNC TR95-007 (1995) — 초록(2~3배/5~10배/80ms), §4.5 Figure 4.36(예측 구간 대 오차), §5.11(예측 구간 추정 오차 10ms → 0.5°), §6.5 |

지연을 없앨 수 없다면 미리 그리면 된다. 트래커가 읽은 '현재' 자세 대신, 그림이 실제로 표시될 시점의 자세를 추정해 그리는 것이다. 원리는 외삽이다. 현재 각도·각속도·각가속도를 알면 Δt 뒤의 각도를 테일러 전개로 추정할 수 있다. 여기서 관성센서가 결정적인 이유가 드러난다. 위치 트래커만 있으면 속도와 가속도를 수치 미분해야 하는데, 미분은 잡음을 증폭한다. 자이로는 각속도를 직접 측정하므로 미분 한 번을 건너뛴다. Azuma는 이 차이가 2~3배의 정확도 향상으로 나타남을 실측했다. 그러나 예측에는 냉혹한 대가가 있다. 주파수 영역에서 보면 예측기는 신호를 '각주파수의 제곱 × 예측 구간'에 비례해 증폭한다. 즉 예측 오차는 예측 구간의 제곱에 가깝게 커진다. 그래서 예측은 짧은 구간에서만 이득이고, 어느 지점을 넘으면 예측하지 않는 것보다 나빠진다. 결정적 함정이 하나 더 있다 — 시스템은 '얼마나 앞을 예측해야 하는지'(즉 남은 지연)를 정확히 알아야 한다. 이 값이 프레임마다 흔들리는데, 10ms만 잘못 잡아도 50°/s에서 0.5°가 어긋난다. 예측이 효과를 보려면 먼저 지연이 짧고 예측 가능해야 한다는, 얼핏 역설적인 결론이 여기서 나온다.

### 완화 기법 2: 타임워프와 재투영 — 다 그린 그림을 마지막 순간에 비튼다
| 항목 | 내용 |
| --- | --- |
| 수치 | Carmack 측정: 타임워프 적용 시 지연 2~18ms, 스캔라인을 따라가는 연속 타임워프는 센서 500Hz 기준 2~3ms. ATW 구현 요건: 90Hz에서 프레임 간격 약 11ms이므로 GPU가 메인 렌더링을 선점(preemption)해야 하며, 실용적으로는 2ms 이하의 선점 granularity가 필요 — 당시 GPU/드라이버로는 어려운 요구였다. ATW는 표시 주사율의 정수 분의 1로 떨어뜨려야 함(90Hz → 45Hz는 안정적 이중상, 65Hz 같은 중간값은 망막 위 상의 개수와 위치가 계속 변해 더 나쁨). Asynchronous Spacewarp(2016)는 장면 내 움직임까지 외삽해 CPU/GPU 부담을 거의 절반으로 줄이지만, 표시 주사율의 절반 미만으로는 잘 확장되지 않는다. HoloL |
| 출처 | John Carmack (2013), 'Time Warping' 절 ; Michael Antonov, "Asynchronous Timewarp Examined", Oculus/Meta 개발자 블로그 (2015-03-02) ; Dean Beeler, Ed Hutchins, Paul Pedriana, "Asynchronous Spacewarp", Oculus 블로그 (2016-11-10) ; Microsoft Learn, "Hologram stability", Reprojection 절 |

타임워프는 발상의 전환이다. 장면을 다시 그리는 대신, 이미 렌더링이 끝난 이미지를 화면에 내보내기 직전에 최신 머리 자세에 맞춰 2차원적으로 비틀어 넣는다. 회전만 보정하는 경우 이 변환은 단순한 이미지 워프이므로 계산 비용이 거의 들지 않고, 렌즈 왜곡 보정 패스와 합칠 수도 있다. 효과는 극적이다. 지연이 '렌더링이 끝난 시각부터 표시 시각까지'로 줄어들기 때문이다. 비동기 타임워프(ATW)는 이것을 별도 스레드에서 수행해, 게임이 프레임을 놓쳐도 화면은 항상 최신 자세로 갱신되게 한다. 그러나 타임워프가 만능이 아닌 이유가 명확히 있다. 회전만 보정하면 머리의 '이동'은 반영되지 않으므로 가까운 물체에서 이중상 저더가 남는다. 깊이를 함께 써서 위치까지 보정하면(깊이 재투영) 이번엔 가려졌던 영역에 데이터가 없어 구멍이 생긴다. 또 장면 안에서 스스로 움직이는 물체는 워프된 프레임에서 시간이 얼어붙고, 시선 방향에 의존하는 반사·스페큘러 하이라이트는 틀린 값으로 남는다. 그래서 Meta는 타임워프를 '만능 해법이 아니라 도로의 구멍을 메우는 보험'으로 규정한다.

### 완화 기법 3: 저잔상 디스플레이 — 지연이 아니라 '번짐'을 잡는 기술
| 항목 | 내용 |
| --- | --- |
| 수치 | 실측 잔상 시간: Valve Index 0.33ms, HTC Vive·Rift S 계열은 0.5~2ms 범위, Oculus Rift 2ms. Rift 기준 11.1ms 프레임 중 9.1ms 소등 + 2ms 점등(듀티비 약 18%). Index의 0.33ms는 144Hz 프레임(6.94ms)에서 듀티비 약 4.8%. 번짐 계산(머리 100°/s): 전체 잔상 11.1ms → 1.11° / 2ms → 0.2° / 0.33ms → 0.033°. HoloLens 1은 색순차 방식으로 R-G-B-G를 60Hz로 순환시키며, 개별 색 필드는 240Hz로 표시된다 — 이 구조 때문에 빠르게 움직이는 물체에서 색분리(무지개 테두리)가 나타나며, 시선으로 추적될 물체는 5°/s 이하로 움직이도록 권고된다. |
| 출처 | Warburton, M. et al., Behavior Research Methods (2022), doi:10.3758/s13428-022-01983-5, Methods 절 — 실측 잔상값 및 듀티 구조 ; Microsoft Learn, "Hologram stability", Color separation 절(240Hz 색필드, 5°/s 권고) ; 번짐 각도는 저자 계산 |

저잔상은 지연을 줄이지 않는다. 그런데도 체감 품질을 극적으로 올린다. 이유는 앞서 본 홀드형 번짐 때문이다. 화면이 프레임 내내 켜져 있으면, 그 시간 동안 눈이 회전하면서 상이 망막 위를 미끄러져 길게 뭉개진다. 화소를 프레임 끝에 짧게만 번쩍이면 번짐은 그 짧은 시간만큼으로 줄어든다. 여기에 대가가 따른다. 첫째, 밝기다. 듀티비가 1/33로 줄면 같은 평균 휘도를 내기 위해 순간 휘도를 33배 올려야 한다. 광학 시스루 장치에서는 밝은 실외 환경과 경쟁해야 하므로 이 제약이 특히 가혹하다. 둘째, 플리커다. 켜짐-꺼짐이 반복되면 주사율이 낮을 때 깜빡임이 지각되므로, 저잔상은 90Hz 이상의 높은 주사율과 짝을 이뤄야만 성립한다. 셋째, 프레임을 놓쳤을 때의 저더가 오히려 더 선명해진다. 번짐이 없으니 두 개의 상이 또렷하게 분리되어 보인다. 즉 저잔상은 '흐릿한 하나의 상'을 '선명한 두 개의 상'으로 바꾸는 거래이며, 프레임률을 지키는 것을 전제로만 이득이다.

### 완화 기법 4: 롤링 셔터 보정 — 카메라와 디스플레이, 두 개의 기울어짐
| 항목 | 내용 |
| --- | --- |
| 수치 | 카메라 롤링 셔터 리드아웃이 10ms일 때 머리 회전 100°/s → 첫 행과 마지막 행 사이 1.0°의 전단(shear). 디스플레이 쪽: 60Hz 주사에서 위아래 16.7ms 차이, 90Hz에서 11.1ms 차이 → 100°/s 회전 시 각각 1.67°, 1.11°의 전단. Mine & Bishop 계산으로는 NTSC 60필드/s, 200°/s 회전에서 한 필드당 3.3° = 600픽셀 시야에서 33픽셀. 스캔라인 단위로 재계산하면 0.13픽셀로 떨어진다. Carmack의 연속 타임워프(스캔라인 추종)는 센서 500Hz 기준 2~3ms 지연을 달성. |
| 출처 | Mark Mine & Gary Bishop, "Just-In-Time Pixels", UNC TR93-005 (1993), §1~§2 및 §4.2 Beam Racing ; John Carmack (2013), 'Continuous Time Warping' 절 ; 전단 각도는 저자 계산 |

증강현실 장치에는 시간이 세로로 번지는 장치가 둘 있다. 카메라의 롤링 셔터와 디스플레이의 순차 주사다. 둘은 방향만 반대일 뿐 같은 문제다. 롤링 셔터 카메라는 센서의 행을 위에서 아래로 차례로 읽어 낸다. 읽는 동안 카메라(머리)가 돌면, 맨 윗행과 맨 아랫행은 서로 다른 시각의 세계를 담는다. 그 결과 직선은 기울고 사각형은 평행사변형이 된다. 이것이 추적에 미치는 영향은 심각하다. 특징점의 위치가 왜곡되면 자세 추정 자체가 틀어지고, 그 오차는 지연 오차와 구별되지 않은 채 정합 오차로 나타난다. 보정 원리는 명확하다. 각 행에 독립된 타임스탬프를 부여하고, 그 시각의 IMU 자세를 써서 행마다 다른 변환을 적용하는 것이다. 즉 '하나의 이미지 = 하나의 자세'라는 가정을 버리고 '하나의 행 = 하나의 자세'로 내려간다. 디스플레이 쪽도 대칭적이다. 스캔라인 단위로 타임워프를 적용하거나(빔 레이싱), 프레임 전체를 동시에 발광시키는 글로벌 조명 방식으로 문제 자체를 없앤다. 근본 해법인 글로벌 셔터 센서는 화소마다 저장 소자를 두어야 해서 감도와 해상도를 희생한다.

### 광학 시스루와 비디오 시스루 — 지연 구조가 근본적으로 다른 이유
| 항목 | 내용 |
| --- | --- |
| 수치 | 광학 시스루: 현실 측 지연 ≈ 0(광학 경로), 가상 측은 전체 MTP. 비디오 시스루: 카메라 노출(통상 1~10ms) + 센서 리드아웃(롤링 시 5~15ms) + ISP + 합성 + 렌더 + 주사가 현실 영상에도 더해짐. Apple은 Vision Pro의 R1 칩이 "12밀리초 안에 새 이미지를 디스플레이로 스트리밍한다 — 눈 깜빡임보다 8배 빠르다"고 공표했다. Holloway(1995)의 결론: 광학 시스루에서는 온건한 머리 속도에서도 시스템 지연이 다른 모든 오차원의 합보다 큰 정합 오차를 만든다. 또한 광학 왜곡을 그래픽 파이프라인에서 계산으로 보정하면, 그 계산이 유발하는 지연 오차가 원래의 왜곡 오차보다 커지는 경우가 흔하다. |
| 출처 | Richard Holloway, "Registration Errors in Augmented Reality Systems", UNC TR95-016 (1995), 초록 및 §8.4(비디오 시스루의 현실 영상 지연 옵션, Bajura & Neumann 1995 인용) ; Michael Bajura & Ulrich Neumann, "Dynamic Registration Correction in Video-Based Augmented Reality Systems", IEEE Computer Graphics & Applications 15(5) (1995) ; Apple Newsroom, "Introducing Apple Vision Pro" (2023-06-05) |

두 방식의 차이는 '현실을 늦출 수 있는가'라는 한 가지 질문으로 요약된다. 광학 시스루에서는 실제 세계의 빛이 반투명 광학계를 통해 곧바로 눈에 들어온다. 지연은 사실상 0이다. 반면 가상 물체는 파이프라인 전체를 통과해 늦게 도착한다. 따라서 오차가 '상대적'으로 드러난다 — 현실이라는 완벽한 기준선 위에서 가상만 헤엄친다. 그리고 이 오차를 줄일 방법은 오직 하나, 가상 쪽 지연을 실제로 줄이는 것뿐이다. 비디오 시스루에서는 현실도 카메라를 통과한다. 노출, 리드아웃, 이미지 신호 처리, 합성, 렌더링, 주사를 모두 거친다. 결정적 이점이 여기서 생긴다. 현실과 가상이 같은 파이프라인을 지나므로, 둘을 같은 시각으로 정렬하면 상대 정합은 원리적으로 완벽해질 수 있다. Bajura와 Neumann이 1995년에 이미 지적했듯, 비디오 방식은 '실제 영상을 일부러 지연시켜 가상과 맞추는' 선택지를 갖는다. 광학 방식에는 없는 선택지다. 대신 비용이 있다. 이제 세계 전체가 전정기관보다 늦는다. 시각과 전정 감각의 불일치는 정합 오차보다 더 근원적인 불편을 만들고, 손을 뻗어 물건을 집는 것 같은 감각운동 과제의 수행이 떨어진다. 그래서 두 방식은 같은 '지연' 문제를 푸는 것이 아니라, 서로 다른 최적화 문제를 푼다. 광학은 '가상의 지연'을, 비디오는 '세계 전체의 지연'을 줄이는 싸움이다. 실무적으로 비디오 시스루는 카메라 영상 자체에도 타임워프를 적용해, 카메라의 긴 파이프라인 지연을 머리 움직임에 대한 응답 지연으로부터 분리한다.

### 실측 — 현대 기기의 지연은 실제로 얼마이며, 어떻게 재는가
| 항목 | 내용 |
| --- | --- |
| 수치 | Warburton et al.(2022) 실측, 240fps 카메라법, 7개 구성(HTC Vive 90Hz, Oculus Rift 90Hz, Rift S 80Hz, Valve Index 80/90/120/144Hz): 급작스러운 움직임 시작 시 평균 지연 21~42ms(최저 Oculus Rift, 최고 Valve Index 80Hz). 매끄러운 구간(예측 작동) 2~13ms. 예측이 이 낮은 값에 도달하는 데 걸리는 시간은 움직임 시작 후 25~58ms. 측정 재현성: 영상 간 표준편차 최대 1.75ms(Rift S). 측정 불확실도: 단일 값에 대해 약 ±4.2ms(Feldstein & Ellis 2020), 240fps 카메라의 빈 폭 4.17ms, 평균적으로 약 2.1ms 과대 보고. 선행 문헌 범위: |
| 출처 | Warburton, M., Mon-Williams, M., Mushtaq, F., Morehead, J.R., "Measuring motion-to-photon latency for sensorimotor experiments with virtual reality systems", Behavior Research Methods (2022), doi:10.3758/s13428-022-01983-5 (프리프린트 bioRxiv 2022.06.24.497509) — 초록, Methods, Results ; Stauffert et al., Frontiers in Virtual Reality 1:582204 (2020), Table 1·Table 2(측정 기법 25종 이상) ; Feldstein & Ellis (202 |

지연 측정의 어려움은 양 끝점이 서로 다른 물리 도메인에 있다는 데 있다. 시작점은 기계적 움직임이고 끝점은 빛이다. 그래서 표준 방법은 두 가지다. 하나는 고속 카메라로 실제 물체와 화면 속 대응물을 한 프레임에 함께 찍어 프레임 수를 세는 것이다. 단순하고 검증 가능하지만, 시간 분해능이 카메라 프레임률에 묶인다. 다른 하나는 광다이오드로 화면의 밝기 변화를 재고 물리적 스위치·가속도계와 시간차를 재는 것이다. 시간 분해능은 훨씬 높지만 한 점의 밝기만 측정한다. 여기서 이 장의 가장 중요한 실무적 발견이 나온다 — 지연은 단일 값이 아니며, 언제 재느냐에 따라 5배 이상 달라진다. Warburton 등은 움직임이 '갑자기' 시작되는 순간과 움직임이 '매끄럽게 진행 중'인 순간을 나누어 측정했다. 갑작스러운 시작에서는 예측 알고리즘이 무력하므로 시스템의 진짜 파이프라인 지연이 드러나고(21~42ms), 매끄러운 구간에서는 예측이 작동해 실효 지연이 2~13ms로 떨어진다. 제조사가 광고하는 낮은 숫자는 대개 후자이고, 사용자가 불편을 느끼는 순간은 대개 전자다. 가속이 급격한 순간, 즉 움직임의 시작과 정지와 방향 전환이 바로 지연이 폭로되는 지점이다.

#### 검증에서 잡힌 정정
- [확정 오류 · 정적↔동적 혼동] "Azuma의 최종 시스템은 온건한 머리 속도에서 4~5mm의 동적 정합을 달성" — 틀렸다. ±4~5mm는 Azuma의 **정적(static) 정합** 수치다. 학위논문 p.17: "The static errors are usually within ±5 mm from most viewpoints (0.42 degrees for a 68 cm arm length), which is less than the ±13 mm shown in previous work." SIGGRAPH94판도 "±4 mm for the red and green bars and ±5 mm for the blue bar"를 정적 정합으로 제시한다. Azuma는 어디서도 동적 정합을 mm로 보고하지 않는다. 게다가 이 조사 결과 자신의 식(오차=ω·Δt)과 모순된다: 50°/s·60ms=3°→68cm에서 약 36mm이고, 5~10배 개선을 적용해도 3.6~7mm가 상한이다.
- [확정 오류 · 범위를 단일값으로 압축] "전체 70ms 지연 중 트래커 15~30ms(약 43%)" — Azuma 원문은 "The end-to-end system delay typically varies from **50-70 ms**"(학위논문 §5, SIGGRAPH94 동일)다. 70ms라는 단일 총량은 없다. 15~30ms를 50~70ms로 나누면 점유율은 **21%~60%** 구간이며, "약 43%"는 최악의 트래커(30ms)와 최악의 총량(70ms)만 짝지어 만든 수치로 근거가 없다. 또한 같은 논문 §1.4는 일반 시스템에 대해 "On our systems, end-to-end delays typically exceed 100 ms"라고 적어, 50~70ms가 '실측 일반값'이 아니라 저지연 최적화 구성의 값임을 드러낸다.
- [확정 오류 · 같은 출처 상충 미조정] List(1983)를 두 개의 양립 불가능한 값으로 인용했다. 한 항목은 "List(1983, 비행 시뮬레이터, 표적 응시): 최대 각속도 76~240°/s"(Azuma 학위논문 p.13 "Uwe List reports peak angular velocities ranging from 76 to 240 degrees per second" — 정확)이고, 다른 항목은 "Mine & Bishop이 인용한 전형적 머리 운동 최대치 370°/s"인데 Mine & Bishop TR93-005 원문은 "peak velocities of 370 degrees/second during typical head motion - see [List 83]"로 **같은 List 1983을 출처로 명시**한다. 동일 1차 출처의 최대치가 240°/s와 370°/s로 갈리는데 조사 결과는 이를 조정하지 않았다. 한쪽은 반드시 틀렸다(2차 인용 오류 가능성이 높음).
- [확정 오류 · 출처에 없는 수치] "HTC Vive·Rift S 계열은 0.5~2ms 범위" — Warburton et al.(2022)에는 없다. 원문은 기기별 값이 아니라 전체 봉투값만 제시한다: "low pixel persistence where the screen is only illuminated for a short period at the end of each frame (0.33ms for the Valve Index – 2ms for the Oculus Rift)". Vive와 Rift S의 잔상 시간은 그 논문에 보고되지 않았으므로 "0.5~2ms"는 창작된 구간이다.
- [확정 오류 · 단위 정의] "60Hz 화면에서는 같은 프레임 안에서도 위아래가 16.7ms 차이가 난다" 및 "60Hz 주사에서 위아래 16.7ms 차이, 90Hz에서 11.1ms 차이" — 인용한 Carmack(2013) 원문은 **16 ms**다: "the bottom of the screen changes 16 milliseconds later than the top of the screen on a 60 fps display". 16.7ms는 프레임 **주기**이고 실제 주사(active scanout)는 수직 소거기간을 제외한다(예: 1080p60 CEA 타이밍은 총 1125행 중 1080행 활성 → 16.0ms). 90Hz도 11.1ms가 아니라 약 10.7ms다. 이 4% 과대치가 전단 각도 계산에 그대로 전파되어 1.67°→약 1.6°, 1.11°→약 1.07°로 내려간다. 또 다수 HMD 패널은 세로가 아니라 가로 방향으로 주사되어 '위아래'라는 서술 자체가 기기 
- [확정 오류 · 내부 산술 모순] "VOR 잠복기 7~15ms" + "시각 추종 100~130ms"를 놓고 "VOR은 시각계 자체보다 10배 이상 빠르다"고 단정했다. 제시된 범위로 비율을 계산하면 100/15≈6.7배 ~ 130/7≈18.6배이므로 하한에서 '10배 이상'은 성립하지 않는다. 각VOR 잠복기를 통상 인용값인 ~7~10ms로 좁히거나 "10배 이상"을 버려야 한다. (Leigh & Zee 5판 3장은 유료 도서로 원문 대조 불가 — 문헌값 자체는 미검증으로 남긴다.)
- [확정 오류 · 기기 세대 혼동] "HoloLens는 ... 깊이 재투영/평면 재투영/자동 평면 재투영의 **세 방식**을 제공한다" — MS Learn "Hologram stability"는 "There are **four** main types of reprojection"으로 Depth / Planar / Automatic Planar / **None**을 열거하고, Depth Reprojection에 대해 "This option is only available on **HoloLens 2 and Immersive Headsets**"라고 명시한다. 즉 같은 항목이 서술 대상으로 삼은 HoloLens 1(색순차·240Hz 색필드·5°/s 권고)에서는 깊이 재투영을 쓸 수 없고 Automatic Planar/Planar 두 가지뿐이다. 또 이 문서는 'Late Stage Reprojection'이라는 용어를 쓰지 않는다(다른 문서의 용어를 이 출처에 귀속시킴).
- [단위 비교 오류 · apples-to-oranges] "Polhemus Fastrak의 사양 지연은 4ms, UNC 광학식 트래커는 15~30ms였다"를 나란히 놓은 비교. Holloway TR95-016 p.133 원문은 "a specified latency of 4 ms (**Mine's number was somewhat higher but includes transmission time to the host**)"라고 단서를 달았다. 4ms는 호스트 전송을 제외한 벤더 **사양치**이고 15~30ms는 Azuma 시스템에서 측정된 **서브시스템 기여분**이므로 측정 경계가 다르다. 같은 축의 '정의의 핵심은 양 끝점' 원칙을 스스로 위반한 비교다.
- [기준거리 불일치 · 자체 산출을 출처로 귀속] "예측 구간 추정 오차 10ms → 50°/s에서 0.5° 오차 → **1m 거리에서 약 9mm**"(출처: Azuma §5.11). Azuma 원문은 "50 degrees per second, 10 ms of unaccounted delay yields 0.5 degrees"까지만 말하며 mm 환산이 없다. 그리고 Azuma가 문서 전체에서 쓰는 기준거리는 **68cm 팔 길이**이므로 같은 0.5°는 5.9mm가 되어야 한다. 같은 문서 안에서 【계산 1】은 68cm, 【계산 2~4】와 이 항목은 1m, Holloway 경험칙은 500mm를 기준으로 삼아 mm 값들이 서로 비교 불가능하다(같은 각오차가 5.9 / 8.7 / 4.4mm로 갈림).
- [범위·단위 혼입] '사람은 언제 지연을 알아채는가' 항목의 "이 폭(3.2ms~100ms)" 안에 Davis et al.(2015)의 500Hz를 함께 넣었다. Stauffert et al. 원문은 이를 "Humans can detect visual variations at 500 Hz"로 **깜빡임(flicker) 검출** 결과로 제시하며, 차원이 Hz(시간주파수 민감도)이지 ms(지연 역치)가 아니다. 논문 제목 자체가 "Humans perceive flicker artefacts at 500 Hz"로, 안구운동 중 나타나는 아티팩트 가시성이다. ms 역치 목록에 섞으면 단위가 뒤섞인다.
- [출처 문구 과장] "운영체제가 ... 추가로 '최대 **수 밀리초**'의 무작위 지연을 더한다" — Carmack 원문은 "an additional random delay of up to **a couple** milliseconds"로 약 2ms 수준을 뜻한다. '수 밀리초'(several ms)는 상한을 부풀린 번역이다.
- [표 라벨 드리프트 · 항목 누락] "Carmack이 **측정**·정리한 전략별 지연: 동기식 렌더링 16~32ms / 파이프라인 이중 CPU 48~64ms ..." — (a) 이 값들은 측정치가 아니라 기사 내 파이프라인 타임라인 도해에서 산출한 추정 예산이다. (b) 16~32ms의 원문 라벨은 "Ample performance, vsync"이며 '동기식 렌더링'이 아니다. (c) Carmack의 목록에 있는 "Prevent GPU buffering .... latency **32 – 48 milliseconds**" 한 단계가 표에서 빠져, 48~64ms에서 18~34ms로 건너뛰는 것처럼 보인다.
- [범위 대표성] "Index의 0.33ms는 144Hz 프레임(6.94ms)에서 듀티비 약 4.8%" — 산술은 맞지만 Warburton은 Index를 80/90/120/144Hz에서 측정했고 잔상 0.33ms는 고정 점등시간이다. 80Hz(12.5ms)에서는 듀티비가 2.6%로 절반 가까이 달라지므로 4.8%를 Index의 대표값처럼 제시하면 오독을 유발한다.
- [출처 범위 초과 · 벤더 수치의 성격] Apple R1 "12밀리초"를 motion-to-photon 절 안에 배치했다. Apple Newsroom 원문은 "R1 streams new images to the displays within 12 milliseconds"로 **카메라→디스플레이 스트리밍** 구간이며, 머리 움직임(물리)에서 시작하는 MTP 정의의 양 끝점과 일치하지 않는다. 덧붙여 "8x faster than the blink of an eye"는 깜빡임을 96ms로 환산한 셈인데, 사람 눈 깜빡임 지속은 통상 100~400ms로 벤더 마케팅 정규화값이다. 검증 가능한 지연 예산으로 취급할 수 없다.
- [역치 성격 혼동] 첫 항목의 "목표치: 20ms 이하(Carmack: 약 20밀리초 미만이면 일반적으로 지각되지 않는다)"에서 두 성격을 겹쳐 썼다. Carmack 원문의 20ms는 (i) '절대(absolute) 지연'에 대한 일반 감각 서술이고 직전 문장이 "Human sensory systems can detect very small **relative** delays"로 상대지연은 훨씬 작게 검출된다고 못박는다. (ii) Stauffert et al.은 같은 문장을 "should be below 50 ms to feel responsive and **recommends** less than 20 ms"로 **권고치**로 정리한다. 이 조사 결과 자신이 뒤에서 Jerald의 3.2ms를 인용하므로, 20ms를 '지각 역치'로 제시하면 문서 내부에서 충돌한다. '권고 예산'과 '지각 역치'를 분리 표기해야 한다.
- [그래프 밖 외삽의 출처 표기] "예측 구간을 25ms에서 200ms까지 늘리면 ... 500ms 지점에서는 두 예측 방식 모두 무예측보다 나빠진다"의 사실 자체는 옳다(학위논문 p.118 "By the 500 ms mark, both types of predictions would be less accurate than doing no prediction at all"). 다만 Figure 4.36의 실측 범위는 25~200ms이고 500ms는 곡선 형태(무예측=선형, 예측=초선형)로부터의 **본문 외삽**이다. 출처를 'Figure 4.36(예측 구간 대 오차)'으로만 달면 500ms가 측정점인 것처럼 읽힌다. 또 같은 문단의 "실효 한계는 예측 구간 약 80ms 이하"는, Azuma가 문맥에 따라 "keep prediction intervals short, below ~80 ms"(p.≈20)와 "keep system delays to ~80 ms or [less]"(p.≈12
- Carmack 전략표 오항목: '파이프라인 이중 CPU 48~64ms'는 틀렸다. Carmack 원문에서 48–64ms는 'Alternate Frame Rendering dual GPU'(이중 GPU 교대 프레임 렌더링) 항목의 값이며, CPU 파이프라인과 무관하다. 파이프라이닝에 해당하는 실제 항목은 'Prevent GPU buffering / Run GPU with minimal buffering: 32 – 48 milliseconds'인데 축의 목록에서 누락됐다. 'Ample performance, unsynchronized: 5 – 8 milliseconds at ~200 frames per second' 항목도 누락. (즉 '지연=48~64ms의 원인이 CPU 2단 파이프라인'이라는 원리 서술 자체가 출처와 어긋난다.)
- 'Azuma의 최종 시스템은 온건한 머리 속도에서 4~5mm의 동적 정합을 달성'(출처: Azuma TR95-007 초록·§6.5) — Azuma 학위논문에는 이 문장이 없다. Azuma 본인의 결론(7장 p.228)은 'This demonstration is supported by static registration that is usually within ±5 mm'로, ±4~5mm는 전부 '정적(static)' 정합 수치다(p.58 '±4 mm for the red and green bars and ±5 mm for the blue bar'). Azuma는 오히려 '동적 오차는 쉽게 100mm를 넘을 수 있다(dynamic errors can easily exceed 100 mm in magnitude, or about 8.3 degrees of arc for a 68 cm arm length)'고 명시한다. '4-5 mm 동적'이라는 표현은 Azuma가 아니라 Holloway
- Azuma §6.5는 'Exploring prediction parameter space'(pp.209~221)로 주파수영역 파라미터 탐색이며, mm 단위 정합 정확도 결과가 실려 있지 않다. 위 4~5mm 주장의 근거 절로 부적합.
- 'Azuma TR95-007 §5.11'은 존재하지 않는 절이다. Azuma 5장은 §5.1(System details)·§5.2(Timing details)·§5.3(Prediction method details)뿐이다. 축이 §5.11로 돌린 두 내용은 모두 §5.2에 있다 — (a) 지연 내역 'The optoelectronic tracker uses 15-30 ms, the predictor consumes ~12 ms, and Pixel-Planes 5 requires 16.67 ms ... At 30 ms, the tracker accounts for about 43% of a 70 ms total delay'는 §5.2, p.139; (b) '10 ms of unaccounted delay yields 0.5 degrees of error, which produces almost 9 mm of error for an object one meter away'는 §5.2, 
- '트래커 15~30ms(약 43%)' — 43%는 15~30ms 구간 전체의 비율이 아니다. 원문은 'At 30 ms, the tracker accounts for about 43% of a 70 ms total delay'로 30ms 끝점에 한정된 값이다(15ms이면 약 21%). 또 Azuma의 실측 전체 지연은 단일 70ms가 아니라 'The end-to-end system delay typically varies from 50-70 ms'이므로 '전체 70ms 지연'이라는 단정도 부정확하다.
- 'Azuma TR95-007 §3.6 머리 운동 주파수 분석(2Hz 이하)' — 절 지정이 틀렸다. Azuma §3.6은 'Evaluation'(정적 정합 평가, p.56)이다. 2Hz 결과('virtually all the signal energy in each of the four graphs exists at frequencies under 2 Hz, which corroborates similar data collected by [So92]')는 4장 §4.1, p.70(Figures 4.9~4.12)에 있고, 주파수분석 기법 자체는 §6.2·§6.6.3이다.
- 'Holloway TR95-016 §8.4(비디오 시스루의 현실 영상 지연 옵션, Bajura & Neumann 1995 인용)' — §8.4는 존재하지 않는다. Holloway 8장은 §8.1(Forecast for future systems, p.207)·§8.2(Future work, p.212)·§8.3(Conclusion, p.215)뿐이다. 해당 내용('In their video STHMD, they have the option of delaying the real-world imagery (not an option with optical STHMDs) to match the delay in displaying the virtual scene')은 §8.2, p.213에 있다.
- 'HoloLens는 ... 깊이 재투영/평면 재투영/자동 평면 재투영의 세 방식을 제공한다' — 개수가 틀렸다. 인용한 Microsoft Learn 'Hologram stability' 원문은 'There are four main types of reprojection'이라 명시하며 Depth / Planar / Automatic Planar / None 넷을 열거한다.
- '실측 잔상 시간: Valve Index 0.33ms, HTC Vive·Rift S 계열은 0.5~2ms 범위, Oculus Rift 2ms' — 중간값이 출처에 없다. Warburton et al.은 전체 시험 기기에 걸친 두 끝점만 제시한다: 'All the tested HMDs feature low pixel persistence where the screen is only illuminated for a short period at the end of each frame to reduce motion blur (0.33ms for the Valve Index – 2ms for the Oculus Rift).' HTC Vive·Rift S의 개별 잔상값이나 0.5ms라는 수치는 논문에 없으며 '0.5~2ms 범위'는 근거 없는 구체화다. 덧붙여 이 값들은 저자들이 측정한 것이 아니라 패널 특성 서술이므로 '실측 잔상 시간'·'Methods 절(잔상 실측값)'이라는 귀속도 과장이
- 'Index의 0.33ms는 144Hz 프레임(6.94ms)에서 듀티비 약 4.8%' — 산술은 맞지만 전제가 출처에 없다. Warburton은 0.33ms를 Valve Index의 값으로 제시했을 뿐 144Hz 조건에서의 측정치라고 명시하지 않았다(Index는 80/90/120/144Hz로 시험됨). 특정 주사율과 결합한 듀티비는 축의 추론이며 출처 표기가 필요하다.
- Azuma 쪽수: '§1.4 Figures 1.7~1.9, pp.12-13' — 70°/s·120°/s 피크 진술은 p.11에 있다(pp.11~13에 걸침). p.12~13으로 한정하면 핵심 문장을 놓친다.
- Holloway 절 지정: Polhemus Fastrak '사양 지연 4ms'를 '§6.3.2.3.2'로 돌렸으나, §6.3.2.3.2는 소각 근사식(bang_delay ≈ \|Ø̇head∆t\|·\|\|vS_P"\|\|)이다. 4ms 사양은 §6.3.2.3 본문 p.133('The Polhemus Fastrak has the lowest latency of the magnetic trackers (for tracking one object) with a specified latency of 4 ms')에 있다.
- 'HoloLens 1: 60fps 미달 시 게임·렌더 스레드가 30fps로 떨어지면 추가 33.3ms 지연' — 원문의 조건절이 빠졌다. Microsoft는 'In an engine with a game and a render thread running in lockstep, running at 30FPS can add 33.3 ms of extra latency'로 '두 스레드가 록스텝으로 도는 엔진'을 전제한다. 또 이 문서는 HoloLens 1 전용이 아니라 HoloLens 1·2·이머시브 헤드셋을 함께 다루므로 'HoloLens 1'로 한정한 것도 부정확하다.
- 용어: 인용한 Microsoft 'Hologram stability' 페이지는 'a sophisticated hardware-assisted holographic stabilization technique known as reprojection'이라고만 쓰고 'Late Stage Reprojection(LSR)'이라는 용어를 쓰지 않는다. 그 페이지를 근거로 'Late Stage Reprojection'을 괄호 병기하면 출처와 어긋난다(LSR은 다른 MS 문서의 용어).
- (외 13건)

## ai3d
항목 16개 · 검증 정정 지적 47건


### NeRF — 장면을 하나의 연속 함수로 적는다
| 항목 | 내용 |
| --- | --- |
| 수치 | MLP 8층 × 256채널(5층에 스킵 연결) + 128채널 1층. 광선당 샘플 수: 성긴 단계 Nc=64, 정밀 단계 Nf=128(합 256). 배치 4,096 광선. 100,000~300,000 반복. 입력 5D → 출력 4D(σ, RGB). |
| 출처 | Mildenhall, Srinivasan, Tancik, Barron, Ramamoorthi, Ng, "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis", ECCV 2020 (oral), arXiv:2003.08934 — 초록 및 Sec. 5.3 Implementation details |

NeRF는 장면을 폴리곤이나 점의 모음이 아니라 '함수'로 표현한다. 입력은 5차원이다. 공간의 한 점 (x, y, z)과 그 점을 바라보는 시선 방향 (θ, φ). 출력은 두 가지, 그 점의 밀도 σ(빛을 얼마나 막는가)와 그 방향에서 보이는 색 c다. 밀도는 방향과 무관하게 정해지고 색만 방향에 따라 달라지도록 설계했는데, 이 비대칭이 물체의 형태를 일관되게 유지하면서 금속의 하이라이트 같은 방향 의존 반사를 담는 장치다. 화면의 한 픽셀 값은 그 픽셀을 지나는 광선 위에서 색을 밀도로 가중 적분해 얻는다 — 고전 볼륨 렌더링 공식 그대로다. 핵심은 이 적분 전체가 미분 가능하다는 점이다. 그래서 '렌더링한 결과가 원본 사진과 다르다'는 오차를 광선을 거슬러 신경망 가중치까지 밀어 보낼 수 있고, 필요한 입력은 오직 사진들과 그 촬영 위치뿐이다. 3D 모델링도, 깊이 센서도, 메시도 필요 없다. 장면 하나에 신경망 하나를 통째로 과적합시키는 것이 학습의 전부다.

### 위치 인코딩 — 신경망이 디테일을 배우지 못하는 이유와 그 해법
| 항목 | 내용 |
| --- | --- |
| 수치 | 위치 γ(x): L=10 → 3차원 좌표가 60차원으로. 방향 γ(d): L=4 → 3차원이 24차원으로. 주파수는 2⁰부터 2^(L-1)까지 옥타브로 상승. |
| 출처 | Mildenhall et al., NeRF, ECCV 2020, Sec. 5.1 "Positional encoding"; 배경 이론은 Tancik et al., "Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains", NeurIPS 2020 (arXiv:2006.10739) |

좌표 (x, y, z)를 그대로 MLP에 넣으면 결과가 흐릿하게 나온다. 일반적인 신경망은 입력에 대해 저주파(완만한 변화) 함수를 먼저, 훨씬 쉽게 학습한다 — 스펙트럴 바이어스라 부르는 성질이다. 그래서 NeRF는 좌표를 넣기 전에 사인·코사인의 사다리를 통과시킨다. sin(2⁰πp), cos(2⁰πp), sin(2¹πp), … 식으로 주파수를 두 배씩 올린 값을 나란히 늘어놓아 저차원 좌표를 고차원 벡터로 부풀린다. 이렇게 하면 공간적으로 아주 가까운 두 점도 인코딩 후에는 뚜렷이 다른 벡터가 되고, 신경망은 그 차이를 근거로 미세한 경계를 표현할 수 있게 된다. 위치에는 L=10, 시선 방향에는 L=4를 쓰는데, 방향에 낮은 주파수를 쓰는 이유는 방향 의존 효과가 본래 완만하기 때문이다. 이 장치 하나를 빼면 같은 신경망, 같은 데이터로도 결과가 눈에 띄게 뭉개진다.

### NeRF의 계산 청구서 — 왜 2020년에는 AR에 쓸 수 없었나
| 항목 | 내용 |
| --- | --- |
| 수치 | 학습: NVIDIA V100 1장에서 장면당 약 1~2일. 렌더링: V100에서 프레임당 약 30초. 이미지 한 장당 신경망 질의 1.5~2억 회. 대조군 — AR 실시간 예산: 60 Hz에서 16.7 ms/프레임, 90 Hz에서 11.1 ms/프레임. |
| 출처 | Mildenhall et al., NeRF, ECCV 2020, Sec. 5.3 및 Sec. 6 ("approximately 1–2 days" on a single NVIDIA V100; "approximately 30 seconds per frame") |

NeRF의 아름다움은 전부 반복 계산으로 지불된다. 한 픽셀을 만들려면 광선 위 256개 지점에서 MLP를 각각 한 번씩 실행해야 한다. 800×800 이미지 한 장이면 신경망 호출이 1.5~2억 회다. 학습은 이 렌더링을 수십만 번 반복하는 일이므로, 장면 하나에 고성능 GPU 하루에서 이틀이 걸렸다. 렌더링 역시 프레임당 30초 수준이었다. 증강현실이 요구하는 예산과 비교해 보면 간극의 크기가 드러난다 — 60 Hz 디스플레이는 프레임당 16.7 ms, 90 Hz 헤드셋은 11.1 ms 안에 모든 계산을 끝내야 한다. 30초와 11 ms의 차이는 약 2,700배이고, 학습까지 포함하면 간극은 더 벌어진다. 이 숫자가 2020~2023년 연구의 방향을 정했다. '품질은 이미 증명됐다, 이제 세 자릿수 이상의 가속이 필요하다'가 문제 정의였고, Instant-NGP와 3D Gaussian Splatting은 각각 학습과 렌더링 쪽에서 이 청구서를 깎은 결과물이다.

### Instant-NGP — 신경망을 줄이고 학습되는 '표'를 늘리다
| 항목 | 내용 |
| --- | --- |
| 수치 | 학습 시간: 수 일 → '수 초' 단위. 복잡한 실촬영 장면도 5분 이내. 렌더링: 1920×1080에서 수십 밀리초. 해시 테이블 T=2^14(약 1.6만 엔트리)일 때 같은 파라미터 수의 주파수 인코딩보다 8배 이상 빠른 학습. T=2^19 구성은 신경망 1만 파라미터 + 인코딩 1,260만 파라미터로 1분 45초 학습. 종합 가속 '수 자릿수(several orders of magnitude)'. |
| 출처 | Müller, Evans, Schied, Keller, "Instant Neural Graphics Primitives with a Multiresolution Hash Encoding", ACM Transactions on Graphics 41(4) (SIGGRAPH 2022), arXiv:2201.05989; 프로젝트 페이지 nvlabs.github.io/instant-ngp |

Instant-NGP의 발상은 역설적이다. 신경망이 느리다면 신경망을 작게 만들고, 대신 학습 가능한 조회표(lookup table)에 정보를 지게 하자는 것이다. 공간을 여러 해상도의 격자로 동시에 덮고(거친 격자부터 촘촘한 격자까지), 각 격자의 꼭짓점마다 짧은 특징 벡터를 저장한다. 어떤 좌표를 질의하면 각 해상도에서 주변 꼭짓점 값을 보간해 가져와 전부 이어 붙이고, 그 벡터를 아주 작은 MLP에 통과시킨다. 문제는 촘촘한 격자의 꼭짓점 수가 폭발한다는 것이다. 여기서 해시 함수가 등장한다 — 꼭짓점 좌표를 고정 크기 해시 테이블의 인덱스로 바꿔 버린다. 당연히 충돌이 생기지만, 이들은 충돌을 별도로 해결하지 않고 그냥 둔다. 밀도가 있는(중요한) 지점의 그래디언트가 빈 공간의 그래디언트를 압도하므로, 최적화 과정이 알아서 중요한 쪽에 맞춰 표를 채운다. 게다가 이 구조는 조건 분기가 없어 GPU에서 완전히 병렬화되고, 저자들은 인코딩·MLP·렌더링을 하나의 CUDA 커널로 융합(fully-fused)해 메모리 대역폭 병목까지 제거했다.

### 3D Gaussian Splatting — 신경망을 버리고 알갱이를 뿌린다
| 항목 | 내용 |
| --- | --- |
| 수치 | 1080p에서 실시간 — 논문 초록 기준 30 FPS 이상, 저자 프로젝트 페이지 기준 100 FPS 이상. 실제 측정 134~160 FPS (NVIDIA A6000). 전형적 장면당 가우시안 100만~500만 개. 가우시안 1개의 파라미터: 위치 3 + 스케일 3 + 회전 4 + 불투명도 1 + 색(구면조화 3차) 48 = 59개. |
| 출처 | Kerbl, Kopanas, Leimkühler, Drettakis, "3D Gaussian Splatting for Real-Time Radiance Field Rendering", ACM Transactions on Graphics 42(4) (SIGGRAPH 2023), arXiv:2308.04079; 프로젝트 페이지 repo-sam.inria.fr/fungraph/3d-gaussian-splatting |

3DGS는 방향을 완전히 바꾼다. 장면을 함수로 두고 광선마다 샘플링하는 대신, 수백만 개의 반투명한 3차원 타원체(가우시안)를 공간에 배치한다. 각 가우시안은 중심 위치, 3×3 공분산(이방성 — 즉 방향에 따라 늘어난 타원 모양), 불투명도, 그리고 구면조화 계수(보는 방향에 따라 달라지는 색)를 갖는다. 공분산은 그대로 최적화하면 물리적으로 불가능한 값이 되기 쉬우므로, 회전(쿼터니언)과 축별 크기(스케일 벡터)로 분해해 최적화한다. 렌더링은 레이 마칭이 아니라 래스터화다 — 각 가우시안을 화면에 투영하면 2D 타원이 되고(이것이 'splat'), 이들을 깊이 순으로 알파 합성하면 그림이 완성된다. 래스터화는 GPU가 30년간 최적화해 온 바로 그 연산이므로 속도의 차원이 다르다. 결정적으로 이 투영·합성 과정도 전부 미분 가능해서, NeRF와 똑같이 '사진과의 오차'만으로 수백만 개 가우시안의 위치·모양·색을 동시에 학습시킬 수 있다. 시작점은 SfM이 부산물로 내놓는 성긴 점군이다.

### 적응적 밀도 제어와 타일 래스터화 — 3DGS를 실제로 작동시키는 두 장치
| 항목 | 내용 |
| --- | --- |
| 수치 | 밀도 제어 주기: 100 반복마다. 불투명도 리셋: 3,000 반복마다. 타일 크기 16×16 픽셀. 학습 총 30,000 반복(7,000 반복만으로도 실용 품질). 정렬은 타일당 1회(픽셀당 아님). |
| 출처 | Kerbl et al., 3D Gaussian Splatting, ACM TOG 42(4), 2023 — Sec. 5 "Optimization with Adaptive Density Control" 및 Sec. 6 "Fast Differentiable Rasterizer" |

가우시안을 흩뿌리는 발상만으로는 작동하지 않는다. 몇 개를 어디에 둘지 사람이 정할 수 없기 때문이다. 3DGS는 최적화 도중 주기적으로 개수를 스스로 조절한다. 위치 그래디언트가 큰 가우시안 — 즉 '자기가 맡은 영역을 제대로 못 그리고 있다'고 신호를 보내는 가우시안 — 을 찾아, 그것이 작으면 복제(clone)해 빈 곳을 메우고, 지나치게 크면 둘로 쪼개(split) 세부를 담게 한다. 반대로 불투명도가 임계값 아래로 떨어진 가우시안은 제거한다. 또 주기적으로 모든 불투명도를 0 근처로 리셋해, 카메라 근처에 쓸모없이 떠 있는 '떠다니는 얼룩(floater)'을 걸러낸다. 렌더링 쪽 장치는 타일 기반 래스터라이저다. 화면을 16×16 픽셀 타일로 나누고, 각 타일에 겹치는 가우시안만 모아 타일 단위로 한 번에 깊이 정렬한 뒤 앞에서 뒤로 합성한다. 픽셀마다 정렬하지 않으므로 정렬 비용이 급감하고, 역전파 때도 타일 단위로 알파 합성을 거꾸로 훑어 가우시안 개수에 제한 없는 그래디언트를 얻는다.

### 정면 비교 — Mip-NeRF 360 벤치마크 위의 숫자들
| 항목 | 내용 |
| --- | --- |
| 수치 | [학습 시간] 3DGS 30K 반복 약 41~45분 / 7K 반복 5~8분 · Instant-NGP(Base) 5~7분 · Plenoxels 25~27분 · Mip-NeRF 360 약 48시간. [렌더링] 3DGS 134~160 FPS · Instant-NGP(Base) 11.7 FPS, (Big) 9.43 FPS · Mip-NeRF 360 0.06~0.14 FPS(프레임당 약 7~17초). [모델 용량] 3DGS 523~734 MB · Instant-NGP(Base) 13 MB, (Big) 48 MB · Mip-NeRF 360 8.6 MB. 전부 NVIDIA A6000 단일 GPU. [품질] Mip-NeRF 360은 mip-NeRF 대비 MSE 57% 감소. |
| 출처 | Kerbl et al., 3D Gaussian Splatting, ACM TOG 42(4), 2023 — Table 1~3 (Mip-NeRF360, Tanks&Temples, Deep Blending, 총 13개 실장면 + Blender 합성); Barron, Mildenhall, Verbin, Srinivasan, Hedman, "Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields", CVPR 2022, arXiv:2111.12077 |

기술 세대의 전환은 같은 데이터, 같은 하드웨어에서 잰 숫자로 확인해야 한다. 표준 시험대는 Mip-NeRF 360 데이터셋이다 — 카메라가 대상 주위를 360도 도는 실외·실내 무한 장면들로, 배경이 무한히 멀어지고 중심 대상은 가깝다는 규모 불일치 때문에 초기 NeRF가 가장 취약했던 조건이다. Mip-NeRF 360 자체는 비선형 장면 파라미터화와 왜곡 정칙화로 이 문제를 풀어 품질 기준선을 세웠지만(mip-NeRF 대비 평균제곱오차 57% 감소), 그 대가로 학습 시간이 극단적으로 길어졌다. 세 방식을 같은 A6000 GPU에서 비교하면 트레이드오프의 구조가 드러난다. Mip-NeRF 360은 최고 품질·최악 속도·최소 용량, Instant-NGP는 최고 학습속도·중간 품질·최소 용량, 3DGS는 최고 속도·최고급 품질·최악 용량이다. 즉 3DGS가 지불한 대가는 계산이 아니라 저장 공간이다.

### 용량이라는 대가 — 3DGS 압축과 경량화
| 항목 | 내용 |
| --- | --- |
| 수치 | LightGaussian: 평균 15배 압축, 동시에 렌더링 속도 144 FPS → 237 FPS(약 64% 향상), 시각 품질 손실 최소. 대상 데이터셋 Mip-NeRF 360, Tanks & Temples. 원본 3DGS 장면 용량 523~734 MB → 대략 35~50 MB 수준. |
| 출처 | Fan, Wang, Yu, Kong, Zhang, Wang, "LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS", NeurIPS 2024, arXiv:2311.17245 |

3DGS가 빠른 이유가 곧 무거운 이유다. 장면 하나가 수백만 개의 독립적인 가우시안이고, 각각이 59개 실수를 들고 있다. 한 장면에 수백 메가바이트, 큰 장면이면 기가바이트가 나온다. 모바일 AR에는 그대로는 못 쓴다. 압축은 세 방향에서 이뤄진다. 첫째 가지치기 — 각 가우시안이 최종 화면에 실제로 얼마나 기여했는지(보이는 횟수, 투영 면적, 불투명도를 종합한 '전역 중요도')를 재서 하위를 제거하고, 남은 것들을 짧게 재학습해 품질을 회복한다. 둘째 구면조화 차수 낮추기 — 색의 방향 의존성을 담는 48개 계수가 파라미터의 대부분인데, 고차 계수를 지식 증류(원본 모델이 만든 가짜 시점 영상을 교사로 삼아)로 저차에 흡수시킨다. 셋째 벡터 양자화 — 중요도가 낮은 가우시안일수록 더 거친 코드북으로 표현해 비트 폭을 줄인다. 핵심 통찰은 가우시안들의 기여도가 극도로 불균등하다는 것이다. 그래서 '균일하게 줄이기'가 아니라 '중요도에 비례해 차등 압축'이 정답이 된다.

### 신경 SLAM — 위치추정과 지도작성이 같은 표현을 공유할 때
| 항목 | 내용 |
| --- | --- |
| 수치 | SplaTAM: 단안 unposed RGB-D 입력, 카메라 자세 추정·지도 구축·새 시점 합성에서 기존 방식 대비 최대 2배 성능(CVPR 2024). MonoGS: 단안 RGB만으로 3 FPS 동작, 3DGS를 유일한 표현으로 사용, SfM 초기화 불필요, 투명 물체와 미세 구조까지 복원(CVPR 2024 Highlight). |
| 출처 | Keetha, Karhade, Jatavallabhula, Yang, Scherer, Ramanan, Luiten, "SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM", CVPR 2024, arXiv:2312.02126; Matsuki, Murai, Kelly, Davison, "Gaussian Splatting SLAM", CVPR 2024 (Highlight), arXiv:2312.06741; 계보로 Sucar et al. "iMAP" ICCV 2021, Zhu et al. "NICE-SLAM" CVPR 2022 |

SLAM은 카메라가 '내가 지금 어디 있는가'(추적)와 '주변이 어떻게 생겼는가'(지도작성)를 동시에 푸는 문제다. 전통적 SLAM의 지도는 성긴 특징점이나 부호거리장(TSDF) 복셀이었다. 전자는 너무 듬성하고, 후자는 메모리를 먹으면서도 관측하지 않은 영역을 비워 둔다. 신경 표현은 여기에 두 가지를 준다. 첫째 완결성 — 학습된 사전 지식이 빈틈을 자연스럽게 메운다. 둘째 사진 수준의 렌더링 — 지도가 곧 볼 수 있는 장면이다. 2021년 iMAP은 하나의 MLP를 실시간으로 학습시키는 첫 시도였고, NICE-SLAM은 이를 계층적 특징 격자로 바꿔 대형 실내에 확장했다. 전환점은 가우시안이었다. SplaTAM은 명시적 가우시안을 지도로 삼아, 렌더링이 빠르다는 성질을 추적에도 그대로 쓴다 — 현재 카메라 자세로 지도를 렌더링해 실제 프레임과 비교하고, 그 오차를 자세 파라미터로 역전파해 자세를 직접 최적화한다. 여기에 실루엣 마스크를 두어 '이 픽셀은 아직 관측된 적이 없다'를 명시적으로 구분하고, 미탐색 영역에는 가우시안을 새로 추가해 지도를 구조적으로 확장한다. MonoGS는 깊이 센서 없이 단안 RGB만으로 같은 일을 해냈다.

### DUSt3R — 카메라를 모르고도 3차원을 얻다
| 항목 | 내용 |
| --- | --- |
| 수치 | 입력 2장부터 동작, 카메라 내부/외부 파라미터 사전 지식 불필요. 출력은 픽셀 정렬된 3D 포인트맵. 하나의 네트워크로 5개 이상의 고전 기하 과제를 통합. |
| 출처 | Wang, Leroy, Cabon, Chidlovskii, Revaud, "DUSt3R: Geometric 3D Vision Made Easy", CVPR 2024, arXiv:2312.14132 (Naver Labs Europe); 후속 MASt3R (ECCV 2024) |

지금까지의 모든 재구성에는 숨은 전제가 있었다. 각 사진을 어디서 어떤 렌즈로 찍었는지(외부·내부 파라미터)를 먼저 알아야 한다는 것이다. 보통 COLMAP 같은 SfM 도구로 얻는데, 이 단계는 느리고 잘 실패한다 — 사진 수가 적거나, 시점 차이가 크거나, 질감 없는 벽이 많으면 그냥 안 된다. DUSt3R는 이 전제 자체를 없앤다. 두 장의 사진을 입력받아, 각 픽셀에 대응하는 3차원 좌표를 담은 '포인트맵'을 곧바로 회귀(regression)한다. 두 포인트맵을 모두 첫 번째 카메라의 좌표계로 출력하게 하는 것이 핵심 설계다 — 이렇게 하면 두 사진 사이의 상대 자세가 포인트맵 대응에서 자동으로 따라 나온다. 즉 투영 기하학의 제약을 방정식으로 푸는 대신 학습으로 흡수한 것이다. 세 장 이상은 쌍별 결과를 전역 정렬로 묶는다. 그 결과 단안 깊이 추정, 다시점 스테레오, 픽셀 대응, 상대 자세 추정, 카메라 내부 파라미터 복원이 전부 하나의 모델에서 나온다. 구조는 표준 트랜스포머(ViT 인코더 + 교차 주의 디코더)이고 사전학습 가중치를 그대로 쓴다.

### MiDaS — 한 장의 사진에서 깊이를 배우는 법과 그 한계
| 항목 | 내용 |
| --- | --- |
| 수치 | 학습에 5개의 상보적 데이터셋 혼합(3D 영화 소스 포함). 평가는 학습에 쓰지 않은 데이터셋에 대한 제로샷 전이. 출력은 스케일·시프트 불변의 상대 역깊이. |
| 출처 | Ranftl, Lasinger, Hafner, Schindler, Koltun, "Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer", IEEE TPAMI(2020년 8월 게재 승인, arXiv:1907.01341); 후속 DPT (Ranftl et al., ICCV 2021) |

사람은 한 눈을 감아도 어느 것이 가까운지 안다. 단안 깊이 추정은 그 능력을 학습으로 재현한다. 문제는 데이터다. 실내 RGB-D 스캔, 실외 라이다, 스테레오 영화, 웹 사진에서 SfM으로 뽑은 깊이 — 이들은 단위도 다르고(미터 vs 상대값), 원점도 다르고(역깊이 vs 깊이), 정확도도 다르다. 그래서 단순히 합쳐 학습시키면 서로 충돌해 망가진다. MiDaS의 해법은 손실 함수 쪽에 있다. 예측과 정답을 각각 정규화해 스케일(배율)과 시프트(오프셋)를 제거한 뒤 비교하는 것이다. 그러면 '전체가 2배 멀다' 또는 '전체가 1미터씩 밀렸다'는 차이는 벌점을 받지 않고, 오직 '상대적인 앞뒤 관계'만 학습된다. 서로 호환되지 않던 데이터셋들이 이 손실 아래에서는 함께 쓰일 수 있게 된다. 여기에 데이터셋별 가중치를 다루는 다목적 학습과, 관련 과제로 인코더를 사전학습하는 전략이 더해진다. 검증은 학습에 쓰지 않은 데이터셋으로만 평가하는 제로샷 교차 데이터셋 전이로 한다. 남는 한계가 결정적이다 — 결과가 상대 깊이다. 무엇이 앞인지는 알지만 몇 미터인지는 모른다.

### Depth Anything — 라벨이 없는 6,200만 장으로 기초 모델을 만들다
| 항목 | 내용 |
| --- | --- |
| 수치 | V1: 라벨 없는 사진 약 6,200만 장 수집·자동 주석, 6개 공개 데이터셋 제로샷 평가, CVPR 2024. V2: 모델 규모 2,500만~13억 파라미터, Stable Diffusion 기반 깊이 모델 대비 10배 이상 빠르고 더 정확, 미터 단위 라벨로 미세조정한 메트릭 버전 별도 제공. |
| 출처 | Yang, Kang, Huang, Xu, Feng, Zhao, "Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data", CVPR 2024, arXiv:2401.10891; Yang et al., "Depth Anything V2", NeurIPS 2024, arXiv:2406.09414 |

MiDaS 계열의 병목은 라벨된 깊이 데이터의 양이었다. 깊이 정답을 얻으려면 라이다나 RGB-D 센서가 필요하고, 그렇게 모을 수 있는 장면의 다양성에는 한계가 있다. Depth Anything의 답은 라벨 없는 일반 사진을 대규모로 끌어들이는 '데이터 엔진'이다. 먼저 라벨된 데이터로 교사 모델을 학습시키고, 그 교사로 6,200만 장의 라벨 없는 사진에 의사 라벨(pseudo-label)을 붙여 학생 모델을 학습시킨다. 그냥 따라 하게만 하면 학생은 교사를 넘지 못한다. 그래서 두 장치를 넣는다. 첫째, 학생에게는 강한 데이터 증강(색 왜곡, 컷믹스)을 걸어 훨씬 어려운 조건에서 교사의 답을 맞히게 한다 — 쉬운 지름길을 막아 더 견고한 표현을 강제하는 것이다. 둘째, DINOv2 같은 사전학습 인코더의 특징을 따라가도록 보조 손실을 걸어 의미론적 사전지식을 물려받게 한다. V2에서는 한 걸음 더 나간다 — 라벨된 실사진을 전부 합성 이미지로 교체했다. 실사 깊이 라벨은 센서 노이즈와 경계 번짐이 있어 오히려 디테일을 망치는데, 합성 데이터는 완벽하게 날카로운 정답을 준다. 합성으로 강한 교사를 만들고, 그 교사가 대규모 실사진에 의사 라벨을 붙여 도메인 격차를 메우는 구조다.

### Depth Pro — 미터 단위 깊이를, 카메라 정보 없이, 0.3초에
| 항목 | 내용 |
| --- | --- |
| 수치 | 225만 화소(1536×1536) 깊이맵을 표준 GPU에서 0.3초에 생성. 카메라 내부 파라미터 불필요(초점거리를 이미지에서 추정). 미터 단위 절대 깊이(zero-shot metric). ICLR 2025. |
| 출처 | Bochkovskii, Delaunoy, Germain, Santos, Zhou, Richter, Koltun, "Depth Pro: Sharp Monocular Metric Depth in Less Than a Second", ICLR 2025, arXiv:2410.02073 (Apple) |

AR에서 상대 깊이는 절반의 답이다. 가상 소파를 거실에 놓으려면 '저 벽이 3.4미터'라는 절대값이 필요하다. 그런데 사진 한 장에서 절대 거리를 추정하려면 원리적으로 초점거리를 알아야 한다 — 같은 사진이 '가까운 작은 물체'일 수도 '먼 큰 물체'일 수도 있는 모호성이 초점거리로만 해소되기 때문이다. 문제는 웹에서 구한 사진의 EXIF가 없거나 틀린 경우가 태반이라는 것이다. Depth Pro는 초점거리 자체를 이미지에서 추정하는 별도 헤드를 두어, 카메라 내부 파라미터 없이 미터 단위 깊이를 내놓는다. 해상도 문제도 정면으로 다룬다. 고해상도 트랜스포머는 계산량이 폭발하므로, 입력을 여러 스케일로 나누어 겹치는 패치로 자르고 같은 ViT 백본을 패치들에 병렬 적용한 뒤 합치는 다중스케일 구조를 쓴다. 덕분에 머리카락·털·식물 잎맥 같은 경계가 살아난다. 학습은 실사와 합성을 섞고, 평가 지표도 기존의 평균 오차 대신 경계 정확도를 따로 측정하는 지표를 새로 도입했다 — 무엇을 재느냐가 무엇이 좋아지느냐를 결정하기 때문이다.

### 가림(occlusion)을 푸는 두 갈래 — 깊이맵과 의미분할
| 항목 | 내용 |
| --- | --- |
| 수치 | ARCore 깊이 API: 0~65 m 범위에서 깊이 추정, 가장 정확한 구간은 기기로부터 0.5~5 m. 깊이는 사용자가 기기를 움직인 이후에만 유효. ToF 센서 탑재 기기에서는 모든 가용 소스를 자동 융합. Segment Anything: 1,100만 장 이미지에 10억 개 이상 마스크(SA-1B)로 학습, 제로샷 성능이 지도학습 기법과 대등하거나 우수(ICCV 2023). |
| 출처 | Google, "Depth adds realism — ARCore Depth API" 개발자 문서(developers.google.com/ar/develop/depth); Du, Turner, Dzitsiuk, Prasso, Duarte, Dourgarian et al., "DepthLab: Real-time 3D Interaction with Depth Maps for Mobile Augmented Reality", UIST 2020; Kirillov, Mintun, Ravi, Mao, Rolland, Gustafson, Xiao, Whitehead, Berg, Lo, Dollár, Girshick, "Segment Anything", ICCV 2023, arXiv:2304.02643 |

증강현실이 '합성'이 아니라 '현실'로 보이는 결정적 단서는 가림이다. 가상 캐릭터가 실제 기둥 뒤로 사라져야 하고, 손을 뻗으면 손가락이 가상 버튼 앞에 와야 한다. 첫 번째 갈래는 깊이다. ARCore의 깊이 API는 전용 센서 없이 '움직임으로부터의 깊이'를 쓴다 — 사용자가 기기를 움직이는 동안 서로 다른 각도에서 찍힌 프레임들을 비교해 픽셀마다 시차를 재고 거리로 환산한다. 스테레오 카메라 두 대를 시간으로 대체한 셈이다. 그래서 사용자가 움직이기 전에는 깊이가 없고, 흰 벽처럼 특징이 없는 면에서는 부정확하다. ToF 센서가 있으면 그 값을 융합해 두 약점을 보완한다. 두 번째 갈래는 의미분할이다. 깊이만으로는 경계가 흐려 머리카락 같은 미세 구조에서 반드시 실패하는데, '이 픽셀은 사람이다'라는 의미 정보는 깊이와 독립적인 단서를 준다. Segment Anything 같은 프롬프트 기반 분할 기초 모델은 학습 때 보지 못한 물체까지 잘라 내므로, AR 장면의 임의 물체에 대해 마스크를 즉석에서 얻을 수 있다. 실무에서는 둘을 결합한다 — 깊이로 대략의 앞뒤를 정하고, 의미 마스크로 경계를 다듬는다.

### 생성형 3D — 촬영하지 않은 것을 만들어 내다
| 항목 | 내용 |
| --- | --- |
| 수치 | DreamFusion(ICLR 2023): 3D 학습 데이터 0, 사전학습 2D 확산 모델만 사용, 물체당 수천 회 최적화. LRM(ICLR 2024): 파라미터 5억 개, 학습 데이터 약 100만 객체(Objaverse 합성 렌더링 + MVImgNet 실촬영), 단일 이미지 → 3D 5초. TRELLIS(2024/2025): 파라미터 20억 개, 다양한 3D 객체 50만 개로 학습, 텍스트·이미지 조건부, 출력 = 래디언스 필드 / 3D 가우시안 / 메시. |
| 출처 | Poole, Jain, Barron, Mildenhall, "DreamFusion: Text-to-3D using 2D Diffusion", ICLR 2023, arXiv:2209.14988; Hong, Zhang, Gu, Bi, Zhou, Liu, Liu, Sunkavalli, Bui, Tan, "LRM: Large Reconstruction Model for Single Image to 3D", ICLR 2024, arXiv:2311.04400; Xiang et al., "Structured 3D Latents for Scalable and Versatile 3D Generation (TRELLIS)", arXiv:2412.01506 (Microsoft Research) |

재구성이 '있는 것을 옮기는 일'이라면 생성은 '없는 것을 만드는 일'이다. 3D 생성의 근본 난점은 데이터다. 텍스트-이미지 모델은 수십억 쌍으로 학습했지만, 라벨된 3D 데이터는 그 근처에도 못 간다. 세 세대의 답이 있었다. 1세대 DreamFusion은 3D 데이터를 아예 포기하고, 이미 학습된 2D 확산 모델을 심판으로 쓴다 — 무작위로 초기화한 NeRF를 임의 각도에서 렌더링하고, '이 그림이 해당 텍스트의 그럴듯한 이미지인가'를 2D 모델에게 물어 그 판단을 확률밀도 증류(SDS) 손실로 NeRF에 역전파한다. 3D 데이터 없이 3D가 나오지만, 물체 하나마다 수천 번의 최적화가 필요해 느리다. 2세대 LRM은 발상을 뒤집어, 대규모 3D·다시점 데이터로 트랜스포머를 한 번 크게 학습시켜 두고 추론은 한 번의 전방 통과로 끝낸다 — 사진 한 장을 넣으면 5초 만에 3D가 나온다. 3세대 TRELLIS는 출력 표현의 문제를 푼다. 구조화된 잠재표현(SLAT)을 하나 만들고 거기서 래디언스 필드, 3D 가우시안, 메시를 모두 디코딩할 수 있게 해, 같은 자산을 용도에 따라 다른 형식으로 꺼내 쓰고 국소 편집까지 가능하게 했다.

### 제작 비용의 재계산 — 5년간 실제로 바뀐 것과 바뀌지 않은 것
| 항목 | 내용 |
| --- | --- |
| 수치 | [재구성 시간] 1~2일(NeRF, V100) → 5분 이내(Instant-NGP) → 5~8분(3DGS 7K 반복, A6000) / 41~45분(3DGS 30K 반복). [렌더링] 30초/프레임 → 134~160 FPS, 약 4,000배. [자산 생성] 단일 이미지 → 3D 5초(LRM). [배포 용량] 523~734 MB → 15배 압축 후 35~50 MB(LightGaussian). [전제 조건 제거] 카메라 파라미터 불필요(DUSt3R), 깊이 센서 불필요(Depth Pro, 0.3초/2.25 MP). |
| 출처 | 본 항목의 수치는 앞선 항목들의 1차 출처를 종합한 것이다 — Mildenhall et al. ECCV 2020; Müller et al. SIGGRAPH 2022; Kerbl et al. SIGGRAPH 2023 Table 1~3; Fan et al. NeurIPS 2024; Hong et al. ICLR 2024; Bochkovskii et al. ICLR 2025 |

비용 변화를 감상이 아니라 숫자로 정리하면 네 축이 보인다. 첫째 계산 시간 — 장면 하나를 재구성하는 데 2020년에는 고성능 GPU로 1~2일, 2022년에는 5분 이내, 2023년 이후로는 실용 품질 기준 5~8분이다. 대략 200~500배의 단축이다. 둘째 렌더링 — 프레임당 30초에서 초당 130프레임 이상으로 약 4,000배 빨라졌고, 이 전환이 '뷰어에서 돌려 보는 결과물'을 '실시간 상호작용 콘텐츠'로 바꿨다. 셋째 입력 조건 — 정밀한 카메라 캘리브레이션과 SfM 성공이라는 전제가 포즈프리 모델로 완화되었고, 깊이 센서 요구는 단안 깊이 모델로 대체 가능해졌다. 넷째 자산 생산 — 사진 한 장에서 5초 만에 3D가 나온다. 반대로 바뀌지 않은 것도 정직하게 적어야 한다. 3DGS 장면은 편집이 어렵다 — 수백만 개 가우시안에서 '이 의자만 옮기기'는 메시에서만큼 자명하지 않다. 재조명(relighting)도 미해결이다. 원본 촬영의 그림자와 반사가 표현에 구워져 있어 새 조명 아래로 옮기면 어색해진다. 물리 시뮬레이션, 충돌 판정, 품질 검수, 그리고 촬영 자체의 인건비는 그대로다. 즉 싸진 것은 '계산'이고, 여전히 비싼 것은 '사람이 판단해야 하는 부분'이다.

#### 검증에서 잡힌 정정
- NeRF 샘플 수 '합 256'이 틀렸다. 64+128=192이다. NeRF 부록 0.A 원문: 'we sample 64 points per ray through the coarse network and 64+128=192 points per ray through the fine network, for a total of 256 network queries per ray.' 즉 256은 샘플 개수의 합이 아니라 광선당 MLP 질의 횟수(성긴망 64 + 정밀망 192)다. 샘플 개수와 질의 횟수라는 서로 다른 단위를 합산했다.
- '정면 비교 ... 전부 NVIDIA A6000 단일 GPU'가 틀렸다. 3DGS 논문은 'All results are reported running on an A6000 GPU, except for the Mip-NeRF360 method'라고 명시하고, 각주로 'We trained Mip-NeRF360 on a 4-GPU A100 node for 12 hours, equivalent to 48 hours on a single GPU. Note that A100's are faster than A6000 GPUs.'라고 적는다. 따라서 '48시간'은 A6000 벽시계 시간이 아니라 4×A100×12h를 환산한 GPU·시간이며, 하드웨어도 A6000이 아니다(h와 GPU·h의 단위 혼동).
- Mip-NeRF 360의 학습 비용을 '약 48시간'으로 제시한 것은 원 논문의 수치가 아니다. Mip-NeRF 360(CVPR 2022) 본문은 250k 반복을 '32코어 TPU v2'에서 학습했고 장면당 약 7시간 수준(구성별 6.2~8.8시간)으로 보고한다. 48시간은 3DGS 저자들의 A100 재학습 환산치이므로, 이를 Mip-NeRF 360의 학습 시간으로 쓰면 하드웨어와 단위가 함께 바뀐다.
- '3DGS 30K 반복 약 41~45분'이 틀렸다. 3DGS Table 1 실측: Mip-NeRF360 41m33s, Tanks&Temples 26m54s, Deep Blending 36m2s. 상한 '45분'은 표에 존재하지 않는 값이고, 실제 하한 약 27분이 누락되어 범위가 위로 밀렸다.
- '3DGS 7K 반복 5~8분'이 틀렸다. 실측은 Mip-NeRF360 6m25s, Tanks&Temples 6m55s, Deep Blending 4m35s다. 하한은 5분 미만(4분 35초)이고 상한 8분에 해당하는 값은 없다.
- '3DGS 실제 측정 134~160 FPS'가 틀렸다. 134/154/137 FPS는 30K 모델, 160/197/172 FPS는 7K 모델 값으로 서로 다른 학습 길이를 한 범위로 합성했다. 실장면 표의 최댓값은 197 FPS(7K, Tanks&Temples)이고, 논문은 합성(Blender) 장면이 180~300 FPS로 렌더링된다고 따로 보고한다. 상한 160은 표의 최댓값을 놓쳤다.
- '3DGS 모델 용량 523~734 MB'가 틀렸다. 523 MB는 Mip-NeRF360의 7K 모델, 734 MB는 같은 데이터셋의 30K 모델이다. 30K 모델의 실제 범위는 411 MB(Tanks&Temples)~734 MB, 7K 모델은 270~523 MB다. 두 설정의 값을 한 모델의 용량 범위로 제시했다.
- 3DGS FPS의 측정 조건 표기가 틀렸다. 논문은 렌더 해상도를 'kept the native input resolution for all renders'라고 밝혀 데이터셋별 원본 해상도에서 측정했다. 따라서 134~197 FPS를 초록의 '1080p에서 ≥30 fps' 및 프로젝트 페이지의 '≥100 fps at 1080p'와 같은 축에 놓고 비교할 수 없다.
- Instant-NGP 'T=2^19 구성 ... 1분 45초 학습'이 틀렸다. Figure 2 (f) T=2^19의 표기 시간은 1:47이고 (e) T=2^14는 1:48이다. 더 중요한 것은 이 시간이 수렴 시간이 아니라 '11 000 steps' 고정 학습 시간이라는 점이다. 즉 T=2^14와 T=2^19의 학습 시간은 1:48 대 1:47로 사실상 동일하고 차이는 PSNR(22.61 대 24.58)에 나타난다 — '표를 키우면 학습이 1분 45초'라는 서술은 비교 축을 잘못 짚었다.
- Instant-NGP '8배 이상 빠른 학습'은 논문 캡션 문구('trains over 8x faster')를 그대로 옮긴 것이지만, 같은 캡션의 실측치로는 재현되지 않는다. 비교 대상 (b) 주파수 인코딩 12:45(765초) 대 (e) T=2^14 1:48(108초)이므로 약 7.1배다. 요약이 논문의 자기모순을 검증 없이 통과시켰다.
- Instant-NGP '렌더링: 1920×1080에서 수십 밀리초'와 같은 문서의 '정면 비교' 수치가 서로 모순된다. INGP-Base 11.7 FPS는 프레임당 약 85 ms이고, 3DGS Table 1의 Deep Blending에서는 INGP-Base 3.26 FPS(약 307 ms), INGP-Big 2.79 FPS(약 358 ms)로 '수십 밀리초'와 한 자리 수 이상 어긋난다. 또 11.7/9.43 FPS는 Mip-NeRF360 데이터셋 한정 값이며 Tanks&Temples에서는 17.1/14.4 FPS다.
- '정렬은 타일당 1회(픽셀당 아님)'가 틀렸다. 3DGS의 빠른 래스터라이저는 (타일 ID, 깊이) 키에 대해 프레임 전체를 한 번에 정렬한다 — 'sort Gaussians ... using a single fast GPU Radix sort', 즉 프레임당 정렬 1회다. 타일 개수만큼 정렬을 수행하는 것이 아니므로 '타일당 1회'는 정렬 횟수의 단위를 잘못 적은 것이다(옳은 대조는 '프레임당 1회 대 픽셀당 정렬 없음').
- DreamFusion '물체당 수천 회 최적화'가 자릿수에서 틀렸다. 논문은 물체당 15,000 최적화 스텝을 수행하며, TPUv4 4칩에서 생성 1건당 약 1.5시간이 걸린다(시간은 NeRF 렌더링과 확산 모델 평가에 절반씩 소요). '수천 회'는 실제의 1/2~1/5 수준이고, 1.5시간이라는 생성 단가가 누락되어 3D 생성의 비용이 실제보다 싸게 읽힌다.
- Depth Pro '225만 화소(1536×1536)'가 단위에서 틀렸다. 1536×1536 = 2,359,296 화소, 즉 약 236만 화소다. 논문의 '2.25-megapixel'은 1 MP를 1024²(2^20)로 세는 이진 기준(1536/1024=1.5, 1.5²=2.25)이므로, 이를 10진 '225만 화소'로 번역하면 약 4.6% 낮게 표기된다.
- Depth Pro의 '0.3초'가 어떤 하드웨어인지 빠졌고, 그 결과가 오해를 만든다. 논문은 이 시간을 V100 GPU 기준으로 보고한다. 같은 문서가 NeRF의 '1~2일, 30초/프레임'을 V100으로 제시했으므로, '5년간 바뀐 것' 항목에서 Depth Pro를 신세대 성취로 대비시키면서 동일 세대 하드웨어라는 사실을 숨기게 된다.
- '렌더링 30초/프레임 → 134~160 FPS, 약 4,000배'의 배수가 부정확하고 조건이 불일치한다. 30초/프레임 = 0.0333 FPS이므로 134 FPS면 약 4,020배, 160 FPS면 약 4,800배다('약 4,000배'는 하한에만 성립). 게다가 분모는 V100·800×800 고정 해상도, 분자는 A6000·데이터셋 원본 해상도여서 배수 자체가 동일 조건 비교가 아니다.
- 문서가 스스로 세운 AR 실시간 예산과 제시한 해법의 수치가 모순된다. 기준은 60 Hz=16.7 ms, 90 Hz=11.1 ms인데, Depth Pro는 0.3초(300 ms, 60 Hz 예산의 약 18배), MonoGS는 3 FPS(약 333 ms, 약 20배)다. 두 결과를 AR 가림·재구성의 해답으로 배치하면서 예산 초과 배수를 계산하지 않았다.
- '용량이라는 대가' 항목의 '큰 장면이면 기가바이트가 나온다'는 인용된 출처로 뒷받침되지 않는다. 3DGS Table 1에서 GB급은 Plenoxels(2.1 GB / 2.3 GB / 2.7 GB)이고, 3DGS 자체의 최대 보고 용량은 734 MB다. 또 여기서도 '523~734 MB'는 7K와 30K 값을 섞은 범위다.
- DUSt3R '하나의 네트워크로 5개 이상의 고전 기하 과제를 통합'의 개수는 출처에 없다. 초록이 성능을 주장하는 과제는 단안 깊이 추정, 다시점 깊이 추정, 상대 자세 추정 3종이며, 나머지(픽셀 대응, 내부 파라미터 복원, 절대 자세/시각 위치추정)는 본문 downstream 응용 절에서 파생 활용으로 소개된다. '5개 이상'은 초록·표의 벤치마크 수와 본문 응용 수를 뒤섞은 집계다.
- NeRF 광선당 샘플 수 '성긴 Nc=64, 정밀 Nf=128(합 256)' — 산술·원리 모두 틀림. 논문 Sec.5.3은 'batch size of 4096 rays, each sampled at Nc=64 coordinates in the coarse volume and Nf=128 additional coordinates'이고 Sec.5.2는 정밀 망을 'the union of the first and second set of samples'(=Nc+Nf=192개 지점)에서 평가한다. 즉 광선당 지점은 192개, MLP 평가는 64(성긴)+192(정밀)=256회다. 256을 '샘플 수'로 적으면 64+128=192라는 덧셈 자체가 성립하지 않는다.
- NeRF 원리요약 '한 픽셀을 만들려면 광선 위 256개 지점에서 MLP를 각각 한 번씩 실행해야 한다' — 오류. 지점은 192개이고, 서로 다른 두 망(coarse/fine)이 존재하며 성긴 64개 지점은 두 망에서 각각 한 번씩 총 두 번 평가된다. '한 망이 256개 지점을 한 번씩'이라는 서술은 계층적 샘플링의 2단계 구조를 소거한다. (800×800×256=1.64억으로 부록의 'between 150 and 200 million network queries per rendered image'와 부합하는 것도 256이 지점 수가 아니라 질의 수임을 확인해 준다.)
- 정면 비교 항목의 '전부 NVIDIA A6000 단일 GPU' — 거짓. Kerbl et al. 표 각주는 'All results are reported running on an A6000 GPU, except for the Mip-NeRF360 method'이며, Mip-NeRF 360은 '4-GPU A100 node for 12 hours, equivalent to 48 hours on a single GPU'로 명시된다. 48시간은 A6000 단일 GPU 실측이 아니라 A100 클러스터의 GPU-시간 환산값이다.
- '3DGS 30K 반복 약 41~45분' — 45분은 어느 표에도 없다. 실제 30K 학습시간은 Mip-NeRF360 41m33s, Tanks&Temples 26m54s, Deep Blending 36m2s. 상한을 45분으로 늘리고 하한 26분대를 누락했다. 같은 오류가 마지막 '제작 비용의 재계산' 항목에 재등장한다.
- '3DGS 7K 반복 5~8분' — 실제는 4m35s(Deep Blending)~6m55s(Tanks&Temples), Mip-NeRF360은 6m25s. 하한(4분 35초)과 상한(6분 55초) 모두 틀렸고 '8분'에 해당하는 측정값은 없다.
- Instant-NGP 'T=2^19 구성은 신경망 1만 파라미터 + 인코딩 1,260만 파라미터로 1분 45초 학습' — 논문 Fig.2 (f)의 값은 10k + 12.6M / 1:47(PSNR 24.58)이다. 1분 45초가 아니라 1분 47초.
- Instant-NGP '해시 테이블 T=2^14일 때 같은 파라미터 수의 주파수 인코딩보다 8배 이상 빠른 학습' — 논문의 '8×' 주장 자체는 존재하나, 근거로 붙은 표값과 재현되지 않는다. Fig.2에서 (b) 주파수 인코딩 438k+0 / 12:45 대 (e) 해시 T=2^14 10k+494k / 1:48 → 벽시계 비율은 약 7.1배다. 또한 (b)의 438k는 전부 '신경망' 파라미터이고 (e)는 신경망 1만+인코딩 49.4만이므로 '같은 파라미터 수'는 총량 근사일 뿐 동종 비교가 아니다.
- Instant-NGP 원리요약 '각 격자의 꼭짓점마다 짧은 특징 벡터를 저장한다' — 방법의 핵심 기제를 잘못 서술. 격자 꼭짓점 수가 T 이하인 거친 레벨만 1:1 대응이고, 미세 레벨은 꼭짓점을 크기 T의 해시 테이블로 사상하며 충돌을 '해결하지 않는다'(논문: 다중해상도 구조와 MLP가 충돌을 암묵적으로 분해). '꼭짓점마다 저장'은 dense grid (c)/(d) 구성의 설명이며, 그것이 바로 해시 인코딩이 대체한 대상이다.
- 3DGS '정렬은 타일당 1회(픽셀당 아님)' — 정렬 단위 오기. 논문 Sec.6은 가우시안을 겹치는 타일 수만큼 인스턴스화해 (타일ID, 깊이) 키를 부여하고 'a single fast GPU Radix sort'로 프레임당 한 번 전역 정렬한다. '타일당 1회 정렬'이 아니라 '전역 1회 정렬 → 타일별 정렬 구간 획득'이며, 뒤이어 'there is no additional per-pixel ordering of points'가 성립한다.
- DreamFusion '물체당 수천 회 최적화' — 과소. 논문은 'We optimize for 15,000 iterations which takes around 1.5 hours' (TPUv4 4칩)라고 명시한다. 1만 5천 회는 '수천 회'가 아니며, 이 항목의 '1세대는 느리다'는 논지의 정량 근거가 절반 이하로 축소됐다. (덧붙여 최적화 중 NeRF 렌더 해상도가 64×64이고 Imagen 64×64 base 모델만 쓴다는 점이 SDS 비용 구조의 핵심인데 누락됐다.)
- NeRF 계산 청구서 항목의 출처 표기 'Sec. 5.3 및 Sec. 6 ("approximately 30 seconds per frame")' — 위치 오기. 1~2일/V100은 Sec.5.3이지만 '30 seconds per frame'은 본문이 아니라 부록(Appendix 0.A, Rendering details)에 있다. ECCV 2020 본문 Sec.6은 Results로 렌더 시간을 제시하지 않는다.
- (외 17건)

## platform
항목 16개 · 검증 정정 지적 46건


### OpenXR — 파편화를 끝내기 위한 표준
| 항목 | 내용 |
| --- | --- |
| 수치 | 발표 2017-02-27(GDC) / 프로비저널 0.90 2019-03-18 / 1.0 정식 2019-07-29(SIGGRAPH) / 1.1 2024-04-15. 라이선스 Apache 2.0, 로열티 없음. 적합(conformant) 런타임 최소 13곳: Acer·ByteDance·Canon·Collabora·Google·HTC·Magic Leap·Meta·Microsoft·Qualcomm·Sony·Valve·Varjo. 엔진 지원: Unreal 4.24+, Unity 2020.2+, Godot 4.0+, Blender 2.83 LTS+. SteamVR은 v1.16(2021-02)부터. |
| 출처 | Khronos Group, OpenXR 공식 페이지(khronos.org/openxr/); Wikipedia 'OpenXR' (발표·릴리스 일자); UploadVR, OpenXR 1.1 보도(2024-04-15) |

2017년 이전의 XR 개발은 기기마다 다른 SDK를 상대하는 일이었다. Oculus SDK, Valve의 OpenVR, Microsoft의 Windows Mixed Reality, 소니의 PSVR SDK가 각자 자기 방식으로 '머리 위치를 알려달라'와 '이 프레임을 화면에 띄워달라'를 요구했다. 앱 N개와 기기 M개가 있으면 N×M개의 통합 작업이 생긴다. OpenXR은 그 사이에 얇은 한 겹을 끼워 N+M으로 바꾸는 표준이다. 구조는 두 갈래인데, 위쪽은 앱이 호출하는 애플리케이션 인터페이스이고 아래쪽은 런타임이 하드웨어에 닿는 디바이스 플러그인 계층이다. 가장 영리한 설계는 입력 모델이다. 앱은 'A 버튼이 눌렸는가'를 묻지 않고 '집기(grab)라는 행위가 일어났는가'를 선언적으로 묻는다(action-based input). 실제 버튼과 행위의 연결은 런타임이 interaction profile로 바인딩한다. 그래서 2017년에 존재하지 않던 컨트롤러가 2024년에 출시돼도 예전에 만든 앱이 손을 대지 않고 동작한다. 로더(loader)가 시스템에 설치된 활성 런타임을 찾아 연결하고, 그 사이에 API 계층(디버깅·검증)을 끼워 넣을 수 있다는 점도 OpenGL/Vulkan에서 가져온 구조다.

### OpenXR 1.1 — 확장이 표준으로 승격되는 메커니즘
| 항목 | 내용 |
| --- | --- |
| 수치 | 1.1 릴리스 2024-04-15. 코어로 승격된 확장 5종: (1) Stereo with Foveated Inset(구 XR_VARJO_quad_views), (2) Local Floor(구 XR_EXT_local_floor), (3) Grip Surface(구 XR_EXT_palm_pose), (4) xrLocateSpaces(구 XR_KHR_locate_spaces), (5) XrUuid(구 XR_EXT_uuid). 신규 인터랙션 프로파일 13종 추가. 스타일러스·근접 감지·국소 햅틱·엄지 거치대 식별자 추가. 지지 표명: Meta·Pico·HTC·Valve·Varjo·Unity·Qualcomm·NVIDIA·XREAL·OPPO·Rokid — Apple은 불참. |
| 출처 | UploadVR, 'OpenXR 1.1' 기사(2024-04-15); Khronos OpenXR 페이지의 회원사 인용문 |

OpenXR은 코어 스펙을 작게 유지하고 새 기능은 확장(extension)으로 먼저 내보낸다. 접두사가 곧 신뢰도다. XR_VARJO_ 같은 벤더 접두사는 한 회사만 지원하고, XR_EXT_는 여러 회사가 합의했으며, XR_KHR_은 Khronos가 관리하고, 마지막으로 코어에 흡수되면 그 버전의 모든 런타임이 반드시 제공한다. 이 단계가 중요한 이유는 앱 코드의 모양이 달라지기 때문이다. 확장은 '있으면 쓰고 없으면 대체 경로'라는 분기를 강제하지만, 코어 기능은 분기 없이 호출하면 된다. 1.1은 이 승격이 실제로 작동함을 보여준 첫 사례다. Varjo가 만든 쿼드 뷰(포비티드 렌더링용 4개 뷰) 확장이 코어가 되면서, 눈동자를 추적해 보고 있는 곳만 고해상도로 그리는 최적화가 특정 벤더의 전유물에서 표준 기능으로 바뀌었다. local floor 공간의 승격도 실용적이다. 기존에는 바닥 높이를 아는 공간과 세션 시작점 기준 공간 둘뿐이라, '바닥은 알되 원점은 지금 내가 선 자리'라는 흔한 요구가 표준에 없었다.

### WebXR Device API — 설치 없는 AR
| 항목 | 내용 |
| --- | --- |
| 수치 | 표준 상태: W3C Candidate Recommendation Draft, 2026-06-09. 편집자 Brandon Jones(Google), Manish Goregaokar(Google), Rik Cabanier(Meta). 참조 공간 5종: viewer / local / local-floor / bounded-floor / unbounded. 별도 모듈 스펙으로 Hit Test, Anchors, Depth Sensing, Lighting Estimation, DOM Overlay, Hand Input 등이 분리 관리된다. |
| 출처 | W3C, 'WebXR Device API', Candidate Recommendation Draft 2026-06-09 (w3.org/TR/webxr/); immersiveweb.dev (세션 모드 설명) |

WebXR은 웹 페이지가 헤드셋과 카메라의 자세(pose) 정보를 받아 3D를 그리게 하는 브라우저 API다. 세션은 세 모드로 나뉜다. inline은 일반 페이지 안의 3D 뷰, immersive-vr은 헤드셋 전체 화면, immersive-ar은 현실 위에 겹치는 모드다. 핵심 개념은 참조 공간(reference space)인데, 이것은 '무엇을 흔들리지 않는 원점으로 삼을 것인가'를 고르는 일이다. viewer는 머리 자체가 원점이라 항상 눈앞에 붙어 있는 UI에 쓰고, local은 세션 시작 지점 고정, local-floor는 바닥이 높이 0, bounded-floor는 안전 경계 다각형이 정의된 방, unbounded는 광범위하게 이동할 수 있되 대신 시스템이 좌표계를 도중에 재조정할 수 있다. 원점 선택이 곧 드리프트를 어디로 밀어낼지의 선택이라는 점이 핵심이다. 렌더링 루프도 특별하다. 일반 웹의 requestAnimationFrame이 아니라 XRSession.requestAnimationFrame을 써야 하는데, 브라우저 화면의 60 Hz가 아니라 헤드셋 디스플레이의 실제 프레임 타이밍(90 Hz, 120 Hz 등)에 정확히 물려야 하기 때문이다.

### WebXR의 현실 — 브라우저 지원의 비대칭
| 항목 | 내용 |
| --- | --- |
| 수치 | caniuse 기준 전역 지원 77.15%(부분 지원 포함). Chrome 79+ / Edge 79+(2020-01)부터 부분 지원. Samsung Internet 12.0+, Opera Mobile 80+. Firefox 77+ 기본 비활성. 데스크톱 Safari 3.1~27.2 모두 기본 비활성. iOS Safari 미지원. Apple Vision Pro: Safari 17.4 / visionOS 1.1에서 플래그 뒤 제공(WebKit 블로그 2024-03-19), 입력 모드 transient-pointer, targetRaySpace=시선 방향, gripSpace=핀치한 손가락 위치, 손 추적은 선택적 요청 기능. |
| 출처 | caniuse.com/webxr (지원표·전역 사용률); WebKit Blog, 'Introducing Natural Input for WebXR in Apple Vision Pro'(2024-03-19) |

표준이 존재하는 것과 쓸 수 있는 것은 다르다. WebXR은 Chromium 계열(Chrome, Edge, Samsung Internet, Meta Quest Browser)에서는 오래전부터 동작하지만 Safari와 Firefox에서는 기본 비활성이거나 미지원이다. 이 비대칭에는 이유가 있다. WebXR immersive-ar은 페이지에 실질적으로 '방의 형태'와 '사용자의 움직임'을 준다. 이는 핑거프린팅과 감시의 새로운 표면이라서 Apple은 신중하게 접근했다. Apple이 Vision Pro에서 WebXR을 열 때 새 입력 모델을 발명한 것이 그 태도를 잘 보여준다. 기존 WebXR 입력은 컨트롤러(tracked-pointer)나 화면 터치(screen)를 가정했는데, Vision Pro는 '눈으로 보고 손가락을 맞대는' 방식이다. 시선 데이터를 웹 페이지에 넘기면 사용자가 무엇에 관심 있는지가 그대로 새어나가므로, Apple은 핀치하는 순간에만 잠깐 존재하는 transient-pointer 입력 소스를 만들었다. 페이지는 '사용자가 어디를 보고 있었는가'가 아니라 '사용자가 방금 무엇을 골랐는가'만 알게 된다.

### ARKit 기능 계보 — 평면에서 지구까지
| 항목 | 내용 |
| --- | --- |
| 수치 | ARKit 1 / iOS 11(2017-09): 월드 트래킹, 수평 평면, 광 추정. 1.5 / iOS 11.3(2018-03): 수직 평면, 이미지 인식. ARKit 2 / iOS 12(2018): ARWorldMap 영속·공유, 3D 객체 인식, 환경 텍스처링, USDZ + Quick Look. ARKit 3 / iOS 13(2019): People Occlusion, Motion Capture(골격 추적), 전·후면 카메라 동시 사용, 협업 세션. ARKit 3.5 / iPadOS 13.4(2020-03): Scene Geometry(iPad Pro LiDAR). ARKit 4 / iOS 14(2020): Location Anchors, Depth API. ARKit 5 / iOS 15(2021). A |
| 출처 | Apple 개발자 문서 'ARKit'(developer.apple.com/documentation/arkit/) 및 해당 연도 WWDC 세션. 버전-기능 대응은 아래 uncertain 참조. |

ARKit의 8년은 '세상을 무엇으로 근사하는가'의 확장사로 읽힌다. 1세대(2017)는 세상을 몇 장의 무한 수평 평면으로 근사했다. 카메라 영상의 특징점과 IMU를 융합하는 VIO(Visual-Inertial Odometry)로 자기 위치를 풀고, 같은 높이에 모인 특징점들을 평면으로 묶었다. 이어 수직 평면과 이미지 인식(1.5), 지도 저장·공유와 3D 객체 인식(2)이 붙었다. 3세대(2019)의 People Occlusion이 질적 도약이었는데, 매 프레임 신경망으로 '사람 형태 마스크'와 '사람까지의 대략적 깊이'를 추정해, 사람이 가상 물체보다 앞에 있으면 그 픽셀을 지운다. 가상 물체가 진짜로 그 공간에 있다는 느낌의 상당 부분이 여기서 나온다. 4세대(2020)는 LiDAR로 접근 방식을 바꿨다. 두 시점의 시차를 계산하는 대신 빛의 비행시간을 직접 재기 때문에, 특징점이 없는 흰 벽이나 어두운 방에서도 깊이가 나온다. 같은 해의 Location Anchor는 GPS로 못 하는 일을 한다 — 도심에서 GPS 수평 오차는 전파 반사 때문에 수십 미터까지 벌어지지만, 카메라가 본 건물 파사드를 Apple Maps의 Look Around 이미지와 대조하면 훨씬 좁게 수렴한다.

### visionOS의 ARKit — 카메라를 주지 않는 AR
| 항목 | 내용 |
| --- | --- |
| 수치 | visionOS 1.0 출시 2024-02-02(미국). visionOS 1 ARKit 제공 기능: 평면 감지, 씬 재구성(메시), 손 추적, 이미지 추적, 월드 앵커. visionOS 2(2024): 객체 추적, 룸 앵커, 전 방향 평면 감지 추가. Apple은 OpenXR 워킹그룹에 참여하지 않으며 ARKit/RealityKit 독자 스택을 유지한다. |
| 출처 | Apple 개발자 문서 'ARKit in visionOS'; UploadVR의 OpenXR 1.1 기사(Apple 불참 언급) |

visionOS의 ARKit은 이름만 같을 뿐 iOS의 그것과 권한 모델이 근본적으로 다르다. iOS에서는 앱이 카메라 프레임을 직접 받아 원하는 컴퓨터 비전을 돌릴 수 있지만, visionOS에서는 일반 앱이 패스스루 카메라의 원본 영상을 받지 못한다. 시스템이 먼저 세상을 해석하고, 앱에는 해석 결과만 — 평면, 재구성된 메시, 손 관절 좌표, 월드 앵커 — 넘긴다. 이유는 상시 착용 기기의 특성에 있다. 안경을 쓴 사람이 방에 들어가면 카메라 원본에는 그 방의 모든 사람 얼굴과 책상 위 서류가 담긴다. 이걸 앱에 주면 사용자가 아니라 주변 사람들의 프라이버시가 앱 개발자에게 위임된다. 그래서 공간 사용 모드에 따라 제공 데이터가 달라진다. 여러 앱이 창처럼 떠 있는 Shared Space에서는 ARKit 데이터가 제한되고, 앱 하나가 시야를 독점하는 Full Space에서 명시적 사용자 허가를 받아야 전체 데이터가 나온다. 개발자에게 이는 제약인 동시에 선물이다 — 손 추적 품질을 직접 손볼 수 없지만, 직접 만들지 않아도 된다.

### ARCore — 파편화된 안드로이드에서 AR을 성립시키는 법
| 항목 | 내용 |
| --- | --- |
| 수치 | ARCore 1.0 출시 2018-02-23. 안정 버전 예시 1.45(2024-08-14). 인증 요건: 카메라 품질, 모션 센서, 하드웨어 설계와 통합된 충분한 CPU 성능, Google Play 탑재. 앱 요건: AR Required는 minSdkVersion 24(Android 7.0) 이상, AR Optional은 19 이상. 일부 기기는 Android 8/9/10/13 이상 요구. 2026년 5월 기준 활성 기기의 88% 이상이 Depth API 지원. iOS에서는 iOS 12.0 이상 ARKit 호환 기기 전부에서 Cloud Anchors·Augmented Faces 사용 가능. |
| 출처 | Google, 'ARCore supported devices'(developers.google.com/ar/devices); Wikipedia 'ARCore'(출시일·인증 요건) |

ARCore가 푸는 문제는 ARKit과 다르다. Apple은 자기가 만든 열몇 종의 기기만 상대하므로 카메라 내부 파라미터(초점거리, 왜곡 계수)와 IMU의 시간 지연을 공장 단계에서 알고 있다. Google은 수백 종의 기기를 상대해야 하는데, VIO는 이 값들이 정확해야 성립한다. 카메라 노출 시각과 IMU 샘플 시각이 몇 밀리초만 어긋나도 위치 추정이 발산한다. 그래서 Google은 화이트리스트 방식을 택했다 — 제조사가 기기를 제출하면 Google이 카메라 품질·모션 센서·CPU 성능을 검증하고 캘리브레이션 프로파일을 만들어야 그 모델이 '지원 기기'가 된다. 여기에 Google Play 탑재라는 조건이 붙어 중국 내수 기기는 별도 목록으로 관리된다. Depth API의 설계도 같은 제약의 산물이다. 전용 깊이 센서를 요구할 수 없으므로, 사용자가 기기를 조금 움직일 때 생기는 프레임 간 시차로 깊이를 추정한다(depth-from-motion). 그래서 별도 하드웨어 없이 대부분의 기기에서 되지만, 사용자가 가만히 서 있으면 깊이가 채워지지 않는다.

### Geospatial API와 VPS — 지구 규모의 좌표계
| 항목 | 내용 |
| --- | --- |
| 수치 | VPS 학습 데이터: 15년 이상 축적된 스트리트뷰 이미지 기반 3D 점군. 커버리지: '거의 모든 국가'(nearly all countries). 앵커 3종: WGS84 앵커(타원체 기준 고도), Terrain 앵커(지면 기준 고도), Rooftop 앵커(옥상 기준 고도). 기기별 지원 편차 있음 — 일부 기기는 'Does not support Geospatial API'로 명시. 구 Cloud Anchor 엔드포인트는 2023-08-31 지원 종료. |
| 출처 | Google, 'ARCore Geospatial API'(developers.google.com/ar/develop/geospatial); Google, 'Cloud Anchors'(developers.google.com/ar/develop/cloud-anchors) |

GPS는 위성 전파의 도달 시간을 재는 방식이라 도심 협곡에서 치명적으로 흔들린다. 건물에 반사된 신호가 직진 신호보다 늦게 도착하는 멀티패스 때문에 오차가 수십 미터까지 벌어지고, 방향(heading)은 자기 나침반에 의존하므로 철골 구조물 옆에서는 더 나쁘다. VPS는 반대 방향으로 접근한다. 카메라가 지금 보는 픽셀에서 특징점을 뽑아, 15년 넘게 수집한 스트리트뷰 이미지로 만든 전 지구 3D 점군에 신경망으로 정합한다. 건물 파사드의 모양은 반사되지도 흔들리지도 않으므로 훨씬 안정적이다. 문제는 데이터 크기다. 전 세계 점군을 기기에 넣을 수 없으니, 먼저 GPS로 후보 지역을 좁히고(수십 미터 오차면 충분하다) 그 지역의 국소 모델만 받아 정합한다. 앵커 종류가 세 가지인 것도 실무적 이유가 있다. 개발자는 콘텐츠를 놓을 지점의 정확한 해발고도를 대개 모르기 때문에, 'WGS84 타원체 기준 절대 고도'뿐 아니라 '땅 위에 놓아라'(Terrain), '건물 옥상에 놓아라'(Rooftop)라는 상대 지정이 필요하다.

### 공간 앵커와 클라우드 앵커 — 좌표가 아니라 약속
| 항목 | 내용 |
| --- | --- |
| 수치 | ARCore Cloud Anchors: Android/iOS 교차 지원, 인터넷 연결 필수, 룸 스케일 권장, 구 엔드포인트 2023-08-31 종료. Meta Shared Spatial Anchors: Quest 2 / Quest Pro / Quest 3 / Quest 3S, Meta XR Core SDK v71 이상, v71+에서는 개별 사용자 ID 대신 임의의 그룹 UUID 기반 공유 권장, Enhanced Spatial Services 활성화 필요, 저장 앵커가 많으면 '설정 > 개인정보 > 물리 공간 기록 지우기' 안내. API 흐름: SaveAnchorAsync → ShareAsync → UUID 브로드캐스트 → LoadUnboundSharedAnchorsAsync. |
| 출처 | Google, 'Cloud Anchors' 문서; Meta, 'Shared Spatial Anchors (Unity)'(developers.meta.com/horizon/documentation/unity/unity-shared-spatial-anchors/) |

앵커를 '저장된 좌표'로 이해하면 왜 앵커가 필요한지 설명되지 않는다. AR 좌표계는 세션마다 원점이 다르고, 시간이 지나면 누적 오차로 드리프트한다. 어제 (1.2, 0, 3.4)에 놓은 물건을 오늘 같은 숫자로 불러오면 엉뚱한 데 나타난다. 앵커는 숫자가 아니라 '이 특징점 뭉치 옆'이라는 상대적 약속이고, 시스템은 매 프레임 그 약속을 다시 풀어 현재 좌표계상의 위치를 갱신한다. 물리적 세계 쪽이 기준이므로 드리프트가 물건을 끌고 다니지 않는다. 클라우드 앵커는 그 약속을 다른 사람에게 전달하는 기능이다. 여기서 결정적인 사실은 전달되는 것이 좌표가 아니라 점군(특징 지도)이라는 점이다. 앵커를 호스팅하려면 기기가 그 주변을 여러 각도에서 촬영해 3D 특징 맵을 만들어 서버에 올려야 하고, 다른 기기가 같은 장소를 비추면 서버가 특징을 대조해 상대 자세를 복원해 준다. 그래서 공유 앵커는 본질적으로 '남의 집 거실 구조를 서버에 업로드하는 일'이고, 여기서 저장 비용·프라이버시·수익화 문제가 동시에 발생한다. 앵커 서비스들이 줄줄이 문을 닫은 이유가 이것이다.

### glTF — 3D의 JPEG, 전송을 위한 형식
| 항목 | 내용 |
| --- | --- |
| 수치 | 착안 2012(COLLADA 워킹그룹) / 1.0 2015-10-19 / 2.0 2017-06 / 2.0.1 2021-10-11. ISO/IEC 12113:2022 국제표준(2022-07). 확장자 .gltf(JSON) / .glb(바이너리, 2.0부터 본 스펙 포함). 주요 확장: Draco(메시 압축), KTX 2.0 + Basis Universal(텍스처), meshopt, PBR 확장군(clearcoat, transmission, volume 등). 채택: Microsoft 2017-03-03(Paint 3D·3D Viewer·Babylon.js·Office), Smithsonian 2020-02 280만 점 공개. |
| 출처 | Khronos Group, glTF 개요 페이지(khronos.org/gltf/); Wikipedia 'glTF'(연혁·ISO 번호·채택 사례) |

glTF의 설계 목표는 단 하나, 'GPU가 바로 먹을 수 있는 상태로 저장한다'이다. 정점 데이터를 buffer(원시 바이트 덩어리) → bufferView(그 안의 구간) → accessor(구간을 어떤 타입으로 읽을지) 세 층으로 나눈 것이 핵심인데, 이 구조 덕분에 파일에서 읽은 바이트를 변환 없이 GPU 버퍼로 그대로 복사할 수 있다. 웹과 모바일에서는 파싱 시간이 곧 로딩 시간이므로 이 차이가 결정적이다. 두 번째 설계 결정은 재질 모델의 고정이다. glTF 1.0은 WebGL 셰이더 코드를 파일에 담았는데, 결과적으로 WebGL이 아닌 렌더러로는 이식이 안 되는 실패를 낳았다. 2.0은 이를 버리고 PBR metallic-roughness라는 물리 기반 재질 모델 하나로 통일했다. 금속성과 거칠기 두 숫자로 재질을 기술하니 어느 렌더러에서 열어도 비슷한 그림이 나온다. 압축은 코어가 아니라 확장으로 뺐다 — Draco는 메시를, KTX2/Basis Universal은 텍스처를 담당한다. 텍스처 압축이 특히 중요한데, GPU마다 지원하는 압축 포맷이 다르므로 Basis Universal은 중간 형태로 저장했다가 기기에서 그 기기가 지원하는 포맷으로 빠르게 변환한다.

### USD / USDZ — 협업과 합성을 위한 형식
| 항목 | 내용 |
| --- | --- |
| 수치 | Pixar 오픈소스 공개 2016(수정 Apache 라이선스). Alliance for OpenUSD(AOUSD) 창립 2023-08-01 — Pixar·Adobe·Apple·Autodesk·NVIDIA, Linux Foundation 산하 Joint Development Foundation과 공동. 확장자: .usd(ASCII 또는 바이너리) / .usda(ASCII) / .usdc(바이너리) / .usdz(패키지). USDZ 구성: 무압축·무암호 zip 아카이브, 내부에 USD + PNG/JPEG + M4A/MP3/WAV. Apple은 iOS 12(2018)부터 AR Quick Look의 형식으로 USDZ를 채택. |
| 출처 | Wikipedia 'Universal Scene Description'(오픈소스 시기·USDZ 구조·AOUSD 창립일·회원사) |

USD의 본체는 파일 포맷이 아니라 합성(composition) 규칙이다. 한 장면이 여러 레이어로 쪼개져 있고, 각 레이어는 같은 객체에 대해 '의견(opinion)'을 낸다. 어떤 의견이 이기는지를 정하는 강한 우선순위 체계가 있어서(sublayer, inherit, variantSet, reference, payload, specialize — 통칭 LIVRPS), 조명 담당과 모델링 담당이 같은 장면을 동시에, 서로의 파일을 건드리지 않고 편집해도 결과가 결정론적으로 합쳐진다. 이것은 수백 명이 한 영화의 한 장면을 만드는 픽사의 파이프라인에서 나온 요구다. payload가 특히 중요한데, 참조만 걸어두고 실제 데이터는 필요할 때만 읽는 지연 로딩이라 도시 한 채 규모의 장면도 열 수 있다. USDZ는 이 USD를 배포용으로 묶은 것인데, '무압축 zip'이라는 이상한 선택에 이유가 있다. 압축하면 파일 하나를 꺼내려고 전체를 풀어야 하지만, 압축하지 않고 각 파일의 시작 위치를 정렬해 두면 메모리 매핑으로 필요한 텍스처만 직접 읽을 수 있다. 다운로드가 끝나기 전에 보이는 부분부터 표시하는 것이 가능해진다.

### glTF와 USD는 왜 경쟁하는가
| 항목 | 내용 |
| --- | --- |
| 수치 | USDZ가 iOS AR Quick Look의 형식으로 고정된 시점: iOS 12(2018). glTF의 ISO/IEC 12113:2022 표준화: 2022-07. AOUSD 창립: 2023-08-01(Apple 창립 멤버). OpenXR 워킹그룹에는 Apple 불참 — 형식·런타임 양쪽에서 Apple이 별도 스택을 유지하는 구도. |
| 출처 | Wikipedia 'glTF' 및 'Universal Scene Description'; Khronos glTF 개요 페이지. 두 진영의 상호운용 작업 진행 상황은 아래 uncertain 참조. |

두 형식은 원래 층이 다르다. USD는 저작·합성·협업(쓰기 최적화), glTF는 전송·런타임(읽기 최적화)이므로, 이론적으로는 'USD로 만들고 glTF로 내보낸다'로 공존해야 한다. 실제로 충돌하는 이유는 세 가지다. 첫째, 재질 모델이 1:1로 대응하지 않는다. USD 쪽은 UsdPreviewSurface와 MaterialX 노드 그래프를, glTF는 metallic-roughness 코어에 확장을 얹는 방식을 쓰는데, 두 체계의 파라미터가 정확히 겹치지 않아 왕복 변환에서 재질이 깨진다. 실무자가 가장 자주 겪는 손실 지점이 여기다. 둘째, 정치적 요인이 있다. Apple이 2018년 AR Quick Look의 유일한 형식으로 USDZ를 못 박으면서, iOS에 AR 콘텐츠를 올리려면 USDZ 외에 선택지가 없어졌다. Khronos 진영은 그 사이 glTF를 웹과 안드로이드 쪽에 정착시켰다. 셋째, 구현 규모가 다르다. OpenUSD의 참조 구현은 C++ 수십 MB 규모라 웹 페이지가 통째로 싣기 어렵고, glTF 로더는 수십 KB로도 만들어진다. 결국 현장은 두 형식을 모두 유지하고 변환 파이프라인을 관리하는 쪽으로 수렴했다.

### Unity의 XR 스택 — 추상층을 한 겹 더
| 항목 | 내용 |
| --- | --- |
| 수치 | Unity OpenXR Plugin: OpenXR-SDK 1.1.36 링크, Unity Editor 2021.3 LTS 이상 호환. 지원 대상 예시 — Windows Mixed Reality(Windows 64-bit, DX11), Meta Quest(Android arm64, Vulkan), Magic Leap 2(Android x64, Vulkan), HoloLens 2(UWP arm64, DX11), SteamVR 및 기타 적합 런타임(Windows 64-bit, DX11). 입력·상호작용은 XR Interaction Toolkit 권장. |
| 출처 | Unity, 'OpenXR Plugin' 매뉴얼(docs.unity3d.com/Packages/com.unity.xr.openxr@1.14/manual/index.html) |

Unity는 세 층으로 XR을 다룬다. 맨 아래는 제공자 플러그인(OpenXR, ARCore XR Plugin, ARKit XR Plugin)이고, 가운데는 어느 제공자를 활성화할지 고르는 XR Plugin Management, 맨 위는 플랫폼 중립 API인 AR Foundation이다. 여기서 흔한 오해가 하나 있다. AR Foundation은 스스로 AR을 하지 않는다. ARPlaneManager 같은 컴포넌트는 '평면을 달라'는 주문서일 뿐이고, 실제 평면 검출은 아래의 ARCore 또는 ARKit 서브시스템이 수행한다. 그래서 AR Foundation이 제공하는 것은 두 플랫폼의 교집합에 가깝고, 한쪽에만 있는 기능은 반드시 조건 분기가 필요하다. 이 구조가 실무에 주는 함의는 '한 번 작성하면 어디서나 돈다'가 아니라 '한 번 작성하되 기능 가용성을 매번 질의해야 한다'는 것이다. AR Foundation은 각 기능마다 descriptor를 통해 '현재 플랫폼이 이걸 지원하는가'를 묻는 API를 제공하는데, 이 질의를 생략한 코드가 다른 기기에서 조용히 아무것도 하지 않는 것이 가장 흔한 버그다.

### Unreal의 XR 스택 — OpenXR 단일 경로
| 항목 | 내용 |
| --- | --- |
| 수치 | Unreal Engine 5.x 기준. 문서 명시: 'OpenXR in Unreal Engine only supports head-mounted devices.' OpenXR 지원은 Unreal 4.24부터 도입. XR 분류는 AR / VR / MR 세 범주. |
| 출처 | Epic Games, 'Developing for XR Experiences in Unreal Engine'(dev.epicgames.com/documentation/en-us/unreal-engine/); Wikipedia 'OpenXR'(Unreal 4.24+ 지원 시점) |

Unreal은 Unity와 다른 길을 택했다. 벤더별 플러그인을 각각 유지하는 대신 OpenXR을 헤드 마운트 기기의 단일 경로로 삼고, 벤더 고유 기능은 OpenXR 확장을 노출하는 보조 플러그인 형태로 얹는다. 추상층을 하나 덜 쓰는 셈이라 장단점이 명확하다. 장점은 벤더가 새 확장을 내면 엔진 코어 업데이트를 기다리지 않고 바로 쓸 수 있다는 것이고, 단점은 앱 코드가 확장 존재 여부를 직접 확인해야 하므로 Unity의 AR Foundation처럼 깔끔한 공통 API가 없다는 것이다. 주의할 제약이 하나 있는데, Unreal의 OpenXR 경로는 머리에 쓰는 기기만 지원한다. 핸드헬드 AR(휴대폰 AR)은 OpenXR 범위 밖이라 별도 경로를 써야 한다. 이는 OpenXR 표준 자체가 초기에 HMD 중심으로 설계된 역사와 관련이 있다.

### 지원 종료의 역사 — 플랫폼은 어떻게 죽는가
| 항목 | 내용 |
| --- | --- |
| 수치 | Google Glass: Explorer $1,500(2013-02 개발자, 2014-04-15 일반 판매), Explorer 프로그램 종료 2015-01-15, Enterprise Edition 1 2017-07, EE2 2019-05, 판매 중단 2023-03-15, 지원 종료 2023-09-15. Windows Mixed Reality: 2017-10 출시, 2023-12-21 사용 중단 발표, Windows 11 빌드 26052(2024-02-08) / 24H2에서 제거. Microsoft는 2023-01 HoloLens·VR·MR 개발팀을 해체. HoloLens 2: 2019-02-24 발표, $3,500, 대각 FOV 52°(1세대 34°), 1440×936/눈, 약 20 PPD, 생산 종료 20 |
| 출처 | Wikipedia 'Google Glass', 'Windows Mixed Reality', 'HoloLens 2', 'Magic Leap', 'Niantic, Inc.'; Google ARCore Cloud Anchors 문서 |

AR 플랫폼의 죽음에는 반복되는 패턴이 있다. 첫 번째 패턴은 3단계 소멸이다. 판매 중단 → 클라우드 서비스 종료 → 기기 무력화. 치명적인 것은 2단계인데, 기기의 핵심 기능이 클라우드에 의존하면 회사의 결정 하나로 사용자 손의 하드웨어가 벽돌이 된다. Magic Leap 1이 정확히 이 경로로 죽었다. 두 번째 패턴은 OS 업데이트에 묻히는 소멸이다. Windows Mixed Reality는 별도의 종료 공지 없이 Windows 11 업데이트에서 컴포넌트가 제거되면서, 사용자가 업데이트를 받는 순간 헤드셋이 인식되지 않게 됐다. 세 번째 패턴은 조용한 사업부 해체다 — 발표보다 인력 감축이 먼저 온다. 여기서 도출되는 실무 원칙이 있다. 표준(OpenXR, glTF)에 붙은 자산은 벤더가 사라져도 살아남고, 벤더 SDK와 벤더 클라우드에 붙은 자산은 같이 죽는다. AR 프로젝트의 수명 설계는 어떤 기능이 멋진가의 문제가 아니라, 이 의존성 그래프에서 어느 노드가 남의 사업 판단에 달려 있는가의 문제다.

### 플랫폼이 걸어놓은 성능 기준선 — 왜 12 밀리초인가
| 항목 | 내용 |
| --- | --- |
| 수치 | Apple Vision Pro: 발표 2023-06-05, 출시 2024-02-02(미국), $3,499(2026-06-25 $3,699로 인상). R1 칩이 카메라 12개·센서 5개·마이크 6개 입력을 처리해 12밀리초 안에 디스플레이로 스트리밍 — Apple 표현으로 '눈 깜빡임보다 8배 빠르다'. 두 디스플레이 합계 2,300만 화소(각각 우표 크기), 눈당 약 3660×3200, 90/96/100 Hz(M5 탑재판 최대 120 Hz), 시야각 약 100°×73°. Meta Quest 3: 출시 2023-10-10, $499.99(128GB)/$649.99(512GB), 눈당 2064×2208 RGB 스트라이프 LCD, 90–120 Hz, 컬러 패스스루용 400만 화소 RGB 카메라 2개, IR 패턴  |
| 출처 | Apple Newsroom, 'Introducing Apple Vision Pro'(2023-06-05) — R1 12밀리초·2,300만 화소 원문; Wikipedia 'Apple Vision Pro', 'Meta Quest 3'(가격·해상도·센서 구성). 20밀리초 전정 임계치는 아래 uncertain 참조. |

패스스루 방식 AR에서는 사용자가 보는 현실조차 카메라를 거친 영상이다. 카메라 노출 → 전송 → 처리 → 합성 → 디스플레이 발광까지의 전 구간 지연(photon-to-photon latency)이 크면, 고개를 돌릴 때 세상이 한 박자 늦게 따라온다. 인간의 전정계(안쪽 귀의 균형 기관)는 머리 움직임을 즉시 감지하는데, 눈이 보는 움직임이 그와 어긋나면 뇌는 이를 중독 신호로 해석해 멀미와 두통을 만든다. 이 불일치 허용 한계가 대략 20밀리초 수준으로 알려져 있어, 플랫폼들은 지연 예산을 그 아래로 잡는다. Apple이 12밀리초라는 숫자를 마케팅 전면에 내건 것도, 그것을 위해 범용 프로세서(M2) 옆에 센서 전용 칩(R1)을 따로 얹은 것도 이 예산 때문이다. 같은 이유로 패스스루 카메라 해상도는 디스플레이 해상도보다 낮게 잡힌다 — 화소를 늘리면 읽고 옮기고 처리하는 시간이 같이 늘어나기 때문이다. Vision Pro의 패스스루가 실제보다 뿌옇게 보이는 것은 기술 부족이라기보다 지연 예산을 지키기 위해 치른 대가다.

#### 검증에서 잡힌 정정
- OpenXR '라이선스 Apache 2.0' — 틀렸다. OpenXR-Docs COPYING.adoc 원문: 스펙·레퍼런스 페이지·문서의 소스는 'Creative Commons Attribution 4.0 International (CC-BY-4.0)', Apache License 2.0은 '헤더 파일·스크립트·프로그램·XML·빌드 툴링'에 적용, XML 레지스트리/메인 헤더/로더는 'Apache-2.0 OR MIT' 이중 라이선스. 즉 스펙 본문에 Apache 2.0을 붙인 것은 Wikipedia 인포박스를 그대로 옮긴 오류다. ('로열티 없음'은 Khronos 원문대로 맞음.) 출처: raw.githubusercontent.com/KhronosGroup/OpenXR-Docs/main/COPYING.adoc
- '적합(conformant) 런타임 최소 13곳' — 과소집계이며 단위도 틀렸다. Khronos 공식 적합 제품 목록(khronos.org/conformance/adopters/conformant-products/openxr)에는 제출 회사가 15곳으로, 조사가 빠뜨린 NVIDIA(CloudXR Runtime)와 Nreal/XREAL(Nreal Light·X)이 포함된다. khronos.org/openxr 본문 인용도 XREAL을 포함해 14곳이다. 더구나 그 목록의 행 단위는 '회사'가 아니라 '제품'(Meta만 Quest 2/3/3S/Pro/XR Simulator 5건, Varjo XR-3/VR-3/Aero/XR-4, Sony ELF-SR1/SR2 등)이어서 '런타임 13곳'은 회사 수와 런타임 수를 혼동한 수치다. 조사 자체도 NVIDIA를 1.1 지지사로는 적고 적합 런타임에서는 빼 내부 모순이다.
- HoloLens 2 '1440×936/눈, 약 20 PPD' — 20 PPD는 플랫폼 스펙이 아니다. Wikipedia HoloLens 2 문서는 Microsoft 공식 주장이 '47 pixels per degree'이고, '20 PPD 미만'은 디스플레이 분석가 Karl Guttag의 반론임을 명시한다. 비평가의 유효해상도 추정을 제조사 공표 스펙으로 제시했다. 게다가 산술 모순: 52° 대각·3:2에서 수평 FOV는 약 43.3°이므로 1440px는 ≈33 PPD, Microsoft의 47 PPD는 수평 2048px(2K 광학엔진)를 전제한다. 1440×936과 20 PPD와 52°는 서로 양립하지 않는다. 출처: en.wikipedia.org/wiki/HoloLens_2
- 'Chrome 79+ / Edge 79+(2020-01)부터 부분 지원' — Chrome의 출하 시점이 틀렸다. WebXR Device API는 Chrome 79 안정판과 함께 2019-12-10에 출하되었다(developer.chrome.com/blog/new-in-chrome-79, 문서 날짜 2019-12-10, 'You can now create immersive experiences ... with the WebXR Device API'). 2020-01은 Edge 79(2020-01-15)에만 해당하므로, 두 브라우저를 한 괄호에 묶어 2020-01로 적은 것은 최초 출하를 5주 이상 늦춘 오기다.
- Google Glass 'Explorer $1,500(2013-02 개발자)' — 개발자 배포 개시일이 틀렸다. Wikipedia: 개발자 사전예약 발표는 2012-06(Google I/O), 실제 개발자 배포 개시는 2013-04-16. 2013-02는 #ifihadglass 공모 공고 시점일 뿐이다. 또 '2014-04-15 일반 판매'는 당일 매진된 1일 한정 판매이고 실제 2차 공개 판매는 2014-05-14인데 이 날짜가 누락됐다. 'Explorer 프로그램 종료 2015-01-15'도 발표일이며 판매 중단은 2015-01-19이다. 출처: en.wikipedia.org/wiki/Google_Glass
- Meta Quest 3 '$499.99(128GB)/$649.99(512GB)' — 2023-10 출시가를 2026년 기준선으로 제시한 stale 수치다. Wikipedia Meta Quest 3: 2024-09까지 128GB 모델은 $429.99로 인하된 뒤 단종되었고 512GB가 $499.99로 내려왔다. Vision Pro는 2026-06-25 인상($3,699)까지 반영했는데 Quest 3만 2년 전 가격을 쓴 것은 기준연도 불일치다.
- Vision Pro 'R1 ... 12밀리초 안에 디스플레이로 스트리밍'을 photon-to-photon 지연 기준선으로 쓴 것 — 정의역이 다르다. Apple Newsroom 원문은 'R1 streams new images to the displays within 12 milliseconds — 8x faster than the blink of an eye'로, R1의 이미지 스트리밍 구간을 말한다. 원리요약이 정의한 photon-to-photon(카메라 노출→리드아웃→처리→합성→디스플레이 발광) 전 구간 지연과 동일시할 수 없고, 12ms에는 센서 노출·디스플레이 발광 지속 시간이 포함되지 않는다. 또 '8배'는 눈 깜빡임을 약 100ms로 잡은 마케팅 환산치다.
- glTF 채택 근거 'Smithsonian 2020-02 280만 점 공개' — 단위 혼동이다. Wikipedia glTF 원문은 'approximately 2.8 million 2D images and 3D models'로, 280만은 2D 이미지가 압도적 다수인 공개 레코드 총수이며 glTF로 배포된 3D 모델 수가 아니다. 3D 포맷 채택 규모의 근거로 인용하면 자릿수가 오해를 낳는다.
- ARKit 6 '4K(3840×2160) 비디오 캡처' — 해상도는 맞지만 단위(프레임레이트)와 조건이 빠져 반쪽 수치다. WWDC22 'Discover ARKit 6' 원문: 3840×2160 16:9는 30fps 고정(HD는 60fps)이며 iPhone 11 이상 및 M1 iPad Pro 한정, HDR은 non-binned 포맷에서만 가능하고 성능 비용이 있다. AR 파이프라인 예산을 논하는 절에서 fps 없는 '4K'는 성립하지 않는다. 출처: developer.apple.com/videos/play/wwdc2022/10126/
- Vision Pro '시야각 약 100°×73°', '눈당 약 3660×3200' — Apple 공표 스펙이 아니다. Apple은 FOV와 패널 화소수를 공식 발표하지 않았고 두 값은 제3자 분해·광학 측정 추정치다(Wikipedia가 표에 싣고 있을 뿐). Apple 공식 수치(23M 화소, 12ms, 12카메라/5센서/6마이크, 90/96/100Hz)와 같은 문장에 섞어 '플랫폼이 걸어놓은 성능 기준선'으로 제시하면 출처 등급이 뒤섞인다.
- caniuse 인용 '데스크톱 Safari 3.1~27.2 모두 기본 비활성' — 행을 섞어 읽었다. 현재 caniuse/webxr에서 데스크톱 Safari 행의 상단은 27.1 TP(3.1~27.1 TP)이고, 27.2는 iOS Safari 행(3.2~27.2, 전 구간 미지원)의 상단 버전이다. 또 데스크톱 Safari는 'not supported'와 'disabled by default'가 혼재한 구간인데 '모두 기본 비활성'으로 단일화했다.
- 'Firefox 77+ 기본 비활성' — caniuse에서 확인되지 않는 경계값이다. 현재 caniuse/webxr의 Firefox 행은 2~159 전 구간이 미지원 또는 기본 비활성으로 표시되어 77이라는 분기점을 특정할 근거가 없다(전역 77.15%가 전부 부분지원이고 Firefox 기여분은 0%이다). 검증 불가 수치로 표기해야 한다.
- 'Opera Mobile 80+' 및 브라우저 목록 누락 — 출처 간 불일치가 해소되지 않았다. caniuse는 Opera Mobile 80만 부분 지원으로 표시하지만 Wikipedia 'WebXR'은 'Opera 66+, Opera Mobile 64+'로 기술한다. 두 수치가 충돌하므로 80+ 단정은 근거가 약하고, 데스크톱 Opera 66+와 Oculus/Meta Quest Browser가 지원 목록에서 빠졌다.
- Magic Leap 항목의 투자 수치 시점 — '$3.5B 이상, 사우디 PIF $7.5억'은 Wikipedia 기준 '2024년 8월 시점 누적' 값인데, 이를 'Magic Leap 2: 2022-09-30' 항목에 붙여 2022년 수치처럼 읽히게 했다. PIF의 단일 투자는 2018-03-07 Series D $4.61억이며 $7.5억은 누적액이다.
- ARCore '일부 기기는 Android 8/9/10/13 이상 요구' — 13은 확인되지 않는다. developers.google.com/ar/devices에서 확인되는 상향 요건은 Android 8.0·10.0 등이며(기본 요건은 7.0), Android 13 이상을 요구하는 항목은 근거를 제시하지 못한다. (AR Required minSdk 24 / AR Optional 19는 원문 일치, 단 원문은 'AR Optional은 API 19로 빌드 가능하나 AR 기능 실행 자체는 24 이상 필요'라는 조건을 명시하므로 이 조건절이 누락됐다.)
- HoloLens 2 '1440×936/눈, 약 20 PPD' — 스펙이 아니다. Microsoft 공식 하드웨어 문서는 'Holographic resolution: 2k 3:2 light engines'(눈당 2048×1080급), 'Holographic density: >2.5k radiants (light points per radian)'(라디안당 2,500 광점 ≈ 약 44 PPD)로 명시한다(learn.microsoft.com/en-us/hololens/hololens2-hardware). '약 20 PPD'는 Karl Guttag의 비판적 측정 추정치이고 '1440×936'은 위키백과의 무출처 수치 — 제조사 스펙과 외부 비판치를 같은 문장에서 스펙으로 제시한 오류. (52° 대각 FOV, 1세대 34°, $3,500, 2019-02-24, 생산종료 2024-10, 지원종료 2027-12-31은 정확.)
- 'Chrome 79+ / Edge 79+(2020-01)부터 부분 지원' — Chrome 79 stable은 2019-12-10이다(chromiumdash.appspot.com/fetch_milestone_schedule?mstone=79 → "2019-12-10T00:00:00"). 2020-01은 Edge 79(2020-01-15)에만 해당하며, WebXR Device API의 최초 정식 출하 시점을 한 달 뒤로 밀어 적었다.
- '데스크톱 Safari 3.1~27.2 모두 기본 비활성' — caniuse/webxr 실제 행은 다르다. 데스크톱 Safari는 3.1~12.1이 '미지원(구현 없음)', 13 이후가 '기본 비활성'이다. '3.2~27.2 전 구간 미지원'은 iOS Safari 행의 숫자다. 두 행을 합쳐 '구현 없음'과 '플래그 뒤 존재'를 같은 상태로 뭉갰다.
- visionOS WebXR 상태가 2년 낡았다 — 'Safari 17.4 / visionOS 1.1에서 플래그 뒤 제공'은 2024-03 시점 스냅샷이고, WebKit 공식 블로그 'WebKit features in Safari 18.0'은 "Safari 18.0 for visionOS 2 adds support for immersive-vr sessions with WebXR"로 정식 출하를 발표했으며 transient-pointer와 손추적 권한 요청도 기본 기능으로 기술한다. 더 중요한 원리적 오류: visionOS Safari에 추가된 것은 immersive-vr이고, 이 절의 제목인 '설치 없는 AR'의 근거인 immersive-ar 세션은 확인되지 않는다 — Vision Pro를 'WebXR=설치 없는 AR' 사례로 쓰면 안 된다.
- 'XR_VARJO_ 같은 벤더 접두사는 한 회사만 지원한다' — OpenXR 명명 규약에서 벤더 태그는 확장의 '저자' 표시이며 독점 구현을 뜻하지 않는다. 다른 런타임이 벤더 확장을 구현하는 것이 규약상 허용되고 실제로도 흔하다(Monado 등이 타사 벤더 접두사 확장 다수 구현). XR_VARJO_quad_views가 1.1 코어로 승격된 사실 자체가 단일 벤더 한정이 아니었음을 보여준다. 역방향으로 'XR_EXT_=여러 회사가 합의'도 반쪽 — EXT는 복수 벤더 '저작'을 뜻하지만 구현 런타임이 하나뿐인 EXT도 많다. 접두사는 신뢰도 지표가 아니라 저자·승인 경로 지표다.
- Unity 스택의 층위 서술 오류 — '맨 위는 플랫폼 중립 API인 AR Foundation'은 틀렸다. 같은 조사가 인용한 Unity OpenXR Plugin 1.14 매뉴얼은 OpenXR이 'action-based input'을 쓰며 입력·상호작용 상위 API로 XR Interaction Toolkit(및 Input System)을 권장한다고 명시한다. AR Foundation은 AR 서브시스템(평면·앵커·메시·이미지 추적)의 상위 API이고, HMD 컨트롤러·햅틱·포즈는 AR Foundation을 거치지 않는다. 'OpenXR/ARCore/ARKit 제공자 → XR Plugin Management → AR Foundation' 단일 피라미드는 존재하지 않는다.
- Unreal 서술 오류 — '벤더별 플러그인을 각각 유지하는 대신 OpenXR을 단일 경로로 삼고, 추상층을 하나 덜 쓴다'는 사실과 다르다. 인용된 Epic 문서의 'OpenXR in Unreal Engine only supports head-mounted devices'는 오히려 핸드헬드 AR(ARKit/ARCore)이 OpenXR이 아닌 별도 경로임을 뜻하고, 같은 문서가 ARKit 기반 Live Link Face 등 벤더 종속 경로를 함께 나열한다(실무에서도 Quest는 Meta XR 플러그인, PSVR2는 플랫폼 SDK 경로). 또한 UE는 IXRTrackingSystem/HeadMountedDisplay + Enhanced Input이라는 자체 추상층을 유지하므로 '추상층이 한 겹 적다'는 정리도 성립하지 않는다.
- 'R1이 12밀리초 안에 → photon-to-photon 전 구간 지연' 혼동 — Apple Newsroom 원문은 "R1 streams new images to the displays within 12 milliseconds — 8x faster than the blink of an eye"로, 센서 입력→디스플레이 스트리밍 구간에 대한 칩 파이프라인 수치다. 카메라 노출·판독 시간과 디스플레이 스캔아웃·발광 지속은 이 12ms에 포함되지 않으므로, 절 제목('왜 12밀리초인가')에서 이를 카메라 광자→눈 광자 전 구간(photon-to-photon) 값으로 읽으면 과소평가가 된다.
- '20밀리초 전정(vestibular) 임계치' — 생리학적 상수가 아니다. 이 20ms는 VR 프레젠스 확보를 위한 공학 목표치(Carmack/Abrash 계열 경험칙)이며, 지연 변별 임계는 과제·시야·움직임 속도에 따라 수 ms에서 수십 ms까지 보고된다(머리 추적 과제에서 한 자릿수 ms 검출 보고 존재). 전정계의 생리 잠시(VOR 반응 ~10ms 수준)와 '20ms 지연 임계'는 별개 개념 — 공학 관행을 생리 임계치로 바꿔 말한 원리 오류다(조사 본문도 uncertain 표기).
- glTF 원리의 자기모순 — 'GPU가 바로 먹을 수 있는 상태로 저장한다(읽어서 그대로 업로드)'와 '주요 확장: Draco(메시 압축), KTX 2.0+Basis Universal, meshopt'는 양립하지 않는다. Draco·meshopt·Basis는 런타임 디코드/트랜스코드 단계를 반드시 요구하므로 '제로 처리 업로드' 성질을 포기하고 전송량과 교환하는 확장이다. 비압축 경로에서도 sparse accessor·정규화 정수 타입 등은 직접 업로드 예외에 해당한다. buffer→bufferView→accessor 3층 설명 자체는 정확.
- Smithsonian '2020-02, 280만 점 공개'를 glTF 3D 공개 규모처럼 제시한 것은 과장 — 인용된 위키백과 원문은 '약 280만 점의 2D 이미지와 3D 모델을 퍼블릭 도메인으로 공개했고 그중 3D 모델에 glTF를 사용'이다. 절대다수는 2D 이미지이며 3D 모델 수는 이보다 3~4자리 적다.
- Google Glass 'Explorer $1,500(2013-02 개발자)' — 위키백과 연혁은 개발자 사전주문 2012-06-27(Google I/O), 실제 개발자 배포 시작 2013-04-16이다. 2013-02는 일반인 대상 #ifihadglass 공모 시점이며 개발자 배포일이 아니다. (2014-04-15 1일 일반 판매, Explorer 종료 2015-01-15, EE1 2017-07, EE2 2019-05는 정확.)
- visionOS '카메라를 주지 않는 AR'을 아키텍처 원리로 일반화한 것은 시점 오류 — visionOS 2(2024) 이후 Apple은 엔터프라이즈 API로 메인 카메라 접근 권한(entitlement)을 제공하고 이후 배포 조건이 완화됐다. '일반 앱은 원본 프레임을 못 받는다'는 visionOS 1의 기본 권한 상태이며, '시스템이 먼저 해석한다'는 설계 원리와 '카메라 프레임 접근 불가'라는 구현 사실은 분리해서 서술해야 한다. (주의: Apple 개발자 문서는 JS 렌더링으로 이번 대조에서 직접 인용 확인 불가 — 재확인 필요 항목.)
- OpenXR 1.1 '지지 표명' 명단 중 NVIDIA·XREAL·OPPO·Rokid는 인용된 두 출처에서 확인되지 않는다 — khronos.org/openxr/의 1.1 회원사 인용문은 Qualcomm·Meta·PICO·HTC·Valve·Varjo·Unity 7곳이고 UploadVR 기사도 Meta·Pico·HTC·Valve·Varjo·Unity를 든다. 네 회사는 별도 보도자료 근거를 붙이거나 명단에서 빼야 한다. (Apple 불참은 두 출처 모두 확인.)
- ARKit 1 '세상을 몇 장의 무한 수평 평면으로 근사했다' — ARKit 1의 ARPlaneAnchor는 처음부터 center+extent를 가진 유한(경계 있는) 사각 평면 추정이었고, iOS 11.3에서 임의 경계 폴리곤(boundary geometry)이 추가됐다. '무한 평면'은 레이캐스트 옵션(existing plane infinite)과 평면 표현을 뒤섞은 서술이다. 같은 절의 ARKit 3 People Occlusion·Motion Capture도 iOS 13 전체 기능이 아니라 A12 Bionic 이상 한정이라는 조건이 빠졌다.
- (외 16건)

## human
항목 17개 · 검증 정정 지적 48건


### 감각 충돌 이론 — 멀미의 표준 설명
| 항목 | 내용 |
| --- | --- |
| 수치 | 양측 전정 기능 소실 환자는 운동 멀미에 사실상 면역이라는 것이 고전적 임상 소견. 순응은 통상 수 회 노출에 걸쳐 진행되며, 연속 노출 간격이 길어지면 순응이 소실된다. |
| 출처 | Reason, J.T. & Brand, J.J., 《Motion Sickness》, Academic Press, 1975 (감각 충돌 이론의 정본). Oman, C.M., "Motion sickness: a synthesis and evaluation of the sensory conflict theory", Canadian Journal of Physiology and Pharmacology 68(2), 1990, pp.294-303 (신경 미스매치 모델). |

우리 뇌는 자기 움직임을 세 갈래로 추정한다. 눈으로 들어오는 광학 흐름, 속귀 전정기관의 가속도 신호, 근육과 관절의 고유수용감각이다. 평소에는 세 추정치가 일치하므로 뇌는 의심하지 않는다. 그런데 머리에 화면을 씌우면 눈은 '내가 앞으로 나아간다'고 보고하는데 전정기관은 '나는 의자에 가만히 앉아 있다'고 보고한다. Reason과 Brand는 이 불일치 자체가 멀미의 원인이라고 보았고, Oman은 여기에 한 단계를 더 얹었다. 단순한 불일치가 아니라, 뇌가 과거 경험으로 학습해 둔 '이렇게 움직이면 이런 신호가 올 것'이라는 내부 모델(신경 저장소)의 예측과 실제 입력이 어긋날 때 오류 신호가 누적된다는 것이다. 이 모델이 강한 이유는 예측력이 있기 때문이다. 반복 노출로 내부 모델이 갱신되면 멀미가 줄어드는 순응 현상, 전정기관이 없는 사람(양측 전정 소실)은 멀미를 겪지 않는다는 임상 관찰이 모두 이 이론과 맞아떨어진다. 약점도 분명하다. 불일치의 크기를 미리 수치로 정의할 방법이 없어서, 사후에 '불일치가 있었으므로 멀미했다'고 설명할 뿐 어느 콘텐츠가 얼마나 멀미를 일으킬지 예측하지 못한다.

### 자세 불안정 이론 — 경쟁 가설
| 항목 | 내용 |
| --- | --- |
| 수치 | 자세 동요는 힘판(force plate)으로 압력중심(COP) 이동 경로 길이·면적을 측정하며, 멀미 취약군의 사전 동요 증가는 통상 노출 전 수십 초~수 분 구간에서 관측된다고 보고된다. 구체 효과크기는 연구마다 편차가 크다. |
| 출처 | Riccio, G.E. & Stoffregen, T.A., "An ecological theory of motion sickness and postural instability", Ecological Psychology 3(3), 1991, pp.195-240. Stoffregen, T.A. & Smart, L.J., "Postural instability precedes motion sickness", Brain Research Bulletin 47(5), 1998, pp.437-448. |

Riccio와 Stoffregen은 순서를 뒤집었다. 멀미가 나서 몸이 흔들리는 것이 아니라, 몸을 안정적으로 세우는 제어 전략을 찾지 못한 상태가 길어질 때 그 부산물로 멀미가 온다는 것이다. 생태심리학의 관점으로, 인간에게 서 있기란 정적인 상태가 아니라 끊임없이 미세하게 넘어지고 되잡는 동적 제어 과정이다. 이 제어는 시각을 주된 기준으로 삼는데, 머리에 씌운 화면이 시각 기준을 통째로 바꿔 버리면 기존 제어 전략이 무효가 되고 몸은 새 전략을 탐색하며 흔들린다. 이 이론이 감각 충돌 이론보다 강한 점은 반증 가능한 예측을 내놓는다는 것이다. 멀미를 호소하기 '이전에' 자세 동요(postural sway)가 이미 증가해 있어야 한다. Stoffregen 진영은 실제로 멀미를 보고하게 될 사람들이 노출 시작 직후부터 무게중심 흔들림이 컸다는 데이터를 반복해서 제시했다. 다만 재현이 항상 성공한 것은 아니고, 앉아서 노출해도 멀미가 생긴다는 점은 이 이론이 설명하기 어려운 부분이다. 현재 학계의 실무적 입장은 두 이론이 배타적이지 않으며, 자세 동요는 멀미의 조기 객관 지표로 쓸 만하다는 쪽이다.

### 사이버 멀미의 발생률과 개인차
| 항목 | 내용 |
| --- | --- |
| 수치 | 연구 간 발생률 보고 범위는 대략 20~80%, 중도 이탈률은 대략 5~15% 수준으로 흩어진다. 노출 시간이 길수록 증상이 누적되며, 20분을 넘기면 증상이 급격히 올라간다는 보고가 반복된다. 노출 후 잔여 효과(시각 흐림, 균형 저하, 지연된 플래시백)는 수 시간까지 지속될 수 있어, 군용 시뮬레이터 운용 규정은 훈련 후 일정 시간 운전·비행을 금지해 왔다. |
| 출처 | Kennedy, R.S. & Fowlkes, J.E., "Simulator sickness is polygenic and polysymptomatic: Implications for research", International Journal of Aviation Psychology 2(1), 1992. 발생률 분포와 조절 변인에 대한 메타분석은 Saredakis, D. et al., "Factors associated with virtual reality sickness in head-mounted displays: A systematic review and meta-analysis", Frontiers in Human Neuroscience 14:96, 2020. |

"몇 퍼센트가 멀미하는가"라는 질문에 하나의 숫자를 대는 것은 정직하지 않다. 발생률은 콘텐츠가 사용자를 가상으로 이동시키는지, 노출이 5분인지 40분인지, 기기의 지연과 프레임률이 얼마인지, 참가자를 어떻게 모집했는지에 따라 몇 배씩 달라진다. 가상 이동이 없는 정적 콘텐츠를 10분 보여주면 유의한 증상이 거의 없고, 조이스틱으로 가상 비행을 30분 시키면 절반 이상이 증상을 호소하고 일부는 중도 포기한다. 개인차도 크다. 여성이 남성보다 취약하다는 보고가 많은데, 그 원인이 생리적인 것인지 아니면 기기의 동공간거리 조절 범위가 여성 평균에 덜 맞아 생긴 인공물인지는 아직 논쟁 중이다. 어린이와 고령자가 성인보다 취약하다는 보고, 편두통 병력이 위험 요인이라는 보고도 있다. 중요한 것은 취약성이 고정된 특성이 아니라는 점이다. 반복 노출로 순응이 일어나므로, 실험실에서 초심자를 대상으로 잰 발생률은 실사용 환경의 상한선에 가깝다.

### SSQ — 멀미를 재는 자와 그 함정
| 항목 | 내용 |
| --- | --- |
| 수치 | 16문항, 각 0~3점. 하위척도 환산 가중치는 메스꺼움 ×9.54, 눈운동 ×7.58, 방향감각 ×13.92이고, 총점은 세 하위 원점수 합에 ×3.74를 곱한다. 널리 인용되는 해석 관례는 총점 5 미만 무증상, 5~10 경미, 10~15 유의, 15~20 우려, 20 초과 심각이지만 이는 규범 기준이 아니라 경험칙이다. |
| 출처 | Kennedy, R.S., Lane, N.E., Berbaum, K.S. & Lilienthal, M.G., "Simulator Sickness Questionnaire: An enhanced method for quantifying simulator sickness", International Journal of Aviation Psychology 3(3), 1993, pp.203-220. 변형 척도는 Kim, H.K. et al., "Virtual reality sickness questionnaire (VRSQ)", Applied Ergonomics 69, 2018, pp.66-73. |

사이버 멀미를 재는 사실상의 표준 도구는 Kennedy 등이 1993년에 발표한 시뮬레이터 멀미 설문(SSQ)이다. 16개 증상 항목을 각각 0(없음)~3(심함)으로 답하게 하고, 이를 세 하위척도로 묶는다. 메스꺼움(N), 눈운동 계열(O: 눈피로·초점 곤란·두통), 방향감각 상실(D: 어지럼·현기)이다. 각 하위척도는 서로 다른 가중치를 곱해 점수화하는데, 이 가중치가 서로 다르다는 사실 자체가 중요한 정보다. 세 증상군이 독립적으로 움직이며 원인이 다르다는 뜻이기 때문이다. 총점만 보고하면 이 정보가 통째로 사라진다. 눈피로가 높고 메스꺼움이 낮은 결과는 광학 설계 문제를, 반대 패턴은 움직임·지연 문제를 가리키는데 총점은 둘을 구별하지 못한다. 또 하나의 함정은 SSQ가 원래 비행 시뮬레이터 조종사용으로 개발되었다는 것이다. 사전-사후 차분을 쓰지 않고 사후 점수만 보고하면, 원래 있던 두통까지 기기 탓으로 계상된다. 최근에는 머리 착용 디스플레이에 맞게 항목을 줄인 VRSQ, CSQ 같은 변형이 쓰인다.

### 증강현실이 가상현실보다 덜 어지러운 이유, 그리고 대신 생기는 문제
| 항목 | 내용 |
| --- | --- |
| 수치 | 보통 머리 회전 속도 50~60°/s에서 지연 20 ms면 정합 오차는 1.0~1.2°가 된다. 빠른 머리 회전(약 300°/s 이상도 가능)에서는 같은 지연이 6° 이상의 오차를 만든다. 팔 길이 60 cm에서 1°는 약 1 cm의 어긋남이다. 업계 관행상 모션-투-포톤 지연 20 ms 이하가 최소 기준이고, 증강현실 정합에는 한 자릿수 ms가 요구된다. 이를 위해 최종 렌더 직전 최신 자세로 화면을 다시 밀어주는 late-stage reprojection이 쓰인다. 참고 시야각: HoloLens 2 대각 약 52°, Magic Leap 2 약 70°. |
| 출처 | Azuma, R.T., "A Survey of Augmented Reality", Presence 6(4), 1997, pp.355-385 (정합 오차와 지연의 관계를 정식화한 고전). Vovk, A. et al., "Simulator Sickness in Augmented Reality Training Using the Microsoft HoloLens", CHI 2018. |

광학 투시형 증강현실은 실제 세계를 그대로 보여준 위에 빛을 더한다. 사용자의 시야 대부분은 진짜 방바닥과 진짜 벽이고, 이들이 움직이지 않는 시각 기준(rest frame)을 계속 공급한다. 뇌가 자기 움직임을 추정할 때 참조할 신뢰할 만한 기준이 살아 있으므로 감각 충돌이 근본적으로 작다. 실제로 HoloLens 계열 기기의 실내 작업 실험에서 SSQ 상승은 미미하게 보고된다. 그러나 증강현실에는 가상현실에 없는 고유한 문제가 있다. 정합(registration)이다. 가상 물체가 실제 책상 위에 놓여 있어야 하는데, 머리가 움직이는 동안 시스템이 그 위치를 갱신하는 데 시간이 걸리면 물체가 책상에서 미끄러진다. 이 오차는 산수로 계산된다. 오차 각도 = 머리 각속도 × 모션-투-포톤 지연이다. 결정적인 차이는, 가상현실에서는 전체 장면이 함께 늦으므로 사용자가 '세계가 늦다'고 느끼지만, 증강현실에서는 진짜 책상은 지연 없이 보이고 가상 물체만 늦으므로 오차가 직접 눈에 보인다는 점이다. 그래서 증강현실의 지연 요구는 가상현실보다 더 가혹하다.

### 폭주-조절 충돌 — 시각 피로의 광학적 뿌리
| 항목 | 내용 |
| --- | --- |
| 수치 | 대다수 사용자가 견디는 편안한 영역은 폭주-조절 불일치 약 0.4디옵터 이내(Shibata et al. 2011). HoloLens 2의 고정 초점면은 약 2 m(0.5디옵터). 이 경우 콘텐츠를 약 1.1 m~무한대 구간에 두면 0.4디옵터 이내에 든다. 반대로 40 cm(2.5디옵터) 거리에 UI를 띄우면 불일치가 2디옵터에 달해 편안한 영역을 5배 초과한다. Magic Leap One은 초점면 2개(약 0.75 m와 2 m 상당)를 두어 이 문제를 완화하려 했다. |
| 출처 | Shibata, T., Kim, J., Hoffman, D.M. & Banks, M.S., "The zone of comfort: Predicting visual discomfort with stereo displays", Journal of Vision 11(8):11, 2011. 초기 정식화는 Hoffman, D.M. et al., "Vergence-accommodation conflicts hinder visual performance and cause visual fatigue", Journal of Vision 8(3):33, 2008. |

사람이 가까운 물체를 볼 때 눈은 두 가지를 동시에 한다. 양쪽 눈을 안쪽으로 모으고(폭주, vergence), 수정체를 두껍게 해 초점을 당긴다(조절, accommodation). 이 둘은 신경학적으로 강하게 연결된 반사쌍이다 — 하나만 따로 하기 어렵게 배선되어 있다. 그런데 스테레오 디스플레이는 이 쌍을 강제로 분리한다. 좌우 눈에 다른 이미지를 보여 물체가 50 cm 앞에 있는 것처럼 폭주하게 만들면서, 실제 빛은 언제나 고정된 초점면(예: 2 m)에서 나오므로 초점은 2 m에 맞춰야 선명하다. 뇌는 서로 다른 거리를 요구하는 두 명령을 동시에 처리해야 하고, 이 갈등이 눈피로·두통·복시·초점 곤란으로 나타난다. 이것이 폭주-조절 충돌(VAC)이다. 충돌의 크기는 거리가 아니라 디옵터(거리의 역수) 차이로 재야 한다. 3 m와 5 m의 차이는 0.13디옵터로 사소하지만, 25 cm와 50 cm의 차이는 2디옵터로 심각하다. 즉 같은 거리 차이라도 가까울수록 훨씬 나쁘다. 해결책은 초점면을 여러 개 두거나(배리포컬·다중초점), 빛의 방향까지 재현하거나(라이트필드·홀로그래픽), 아니면 콘텐츠를 편안한 영역 안에 묶어 두는 것이다.

### 시각 피로의 나머지 원인 분해
| 항목 | 내용 |
| --- | --- |
| 수치 | 눈깜빡임은 대화 중 분당 약 15~22회에서 화면 집중 시 분당 약 5~7회로 감소한다고 보고된다(Tsubota & Nakamura, NEJM 1993). 성인 동공간거리는 ANSUR II(2012) 기준 여성 평균 61.7 mm(표준편차 3.6, 범위 51.0~74.5), 남성 평균 64.0 mm(표준편차 3.4, 범위 53.0~77.0). 상용 기기의 조절 범위는 대체로 58~72 mm 수준이라 분포의 양 끝을 못 담는다. 안경 착용을 허용하려면 아이릴리프가 통상 18~20 mm 이상 필요하다. 야외 주광 조도는 10,000~100,000 lux에 달해, 광학 투시형이 대비를 확보하려면 매우 높은 휘도가 요구된다. 권장 휴식은 20분마다 6 m(20피트) 밖을 20초 보는 '20-20-20' 규칙(미국안 |
| 출처 | ANSUR II (2012) 미 육군 인체측정 조사 — 동공간거리 통계. Tsubota, K. & Nakamura, K., "Dry eyes and video display terminals", New England Journal of Medicine 328, 1993, p.584. 디스플레이 시각 피로 요구사항은 ISO 9241-303 및 입체 영상 관련 ISO 9241-392. |

폭주-조절 충돌은 시각 피로의 가장 유명한 원인이지만 유일한 원인은 아니다. 최소 다섯 갈래가 더 있고, 각각 다른 처방을 요구한다. 첫째, 눈깜빡임 감소다. 집중해서 화면을 볼 때 깜빡임 횟수가 3분의 1 수준으로 떨어지고 눈물막이 마르면서 따가움과 흐릿함이 온다. 이는 기기 문제가 아니라 과제 몰입의 부산물이라 광학으로 못 고친다. 둘째, 양안 정렬 오차다. 좌우 렌즈의 광축이 미세하게 어긋나면 눈이 매 순간 이를 보정하느라 융합 근육을 쓴다. 특히 수직 방향 어긋남은 인간이 거의 보정하지 못해 소량으로도 두통을 만든다. 셋째, 동공간거리 미스핏이다. 기기의 렌즈 중심 간격이 내 눈 간격과 다르면 렌즈 주변부로 보게 되어 왜곡과 색수차가 늘고, 상이 뒤틀린다. 넷째, 아이릴리프 — 렌즈에서 눈까지의 거리 — 가 부족하면 안경을 쓸 수 없고, 억지로 쓰면 시야가 잘리거나 렌즈가 긁힌다. 다섯째, 휘도와 대비의 문제다. 광학 투시형은 밝은 실외에서 가상 영상이 묻히므로 휘도를 올려야 하는데, 이는 눈부심과 피로를 동시에 키운다.

### 인지 부하 — 주의는 유한 자원이다
| 항목 | 내용 |
| --- | --- |
| 수치 | 표준 측정 도구는 NASA-TLX(정신적·신체적·시간적 요구, 수행, 노력, 좌절 6차원을 0~100으로 평정하고 쌍대비교 가중치를 곱함, Hart & Staveland 1988). 부하가 높을 때 유효 시야는 상당폭 축소되며, 이를 '터널 시야'라 부른다. 휴대전화 통화 중 운전자의 제동 반응은 대조군 대비 유의하게 지연되며, Strayer 등은 그 성능 저하가 혈중알코올농도 0.08% 수준의 손상과 견줄 만하다고 보고했다. |
| 출처 | Wickens, C.D., "Multiple resources and mental workload", Human Factors 50(3), 2008, pp.449-455. Hart, S.G. & Staveland, L.E., "Development of NASA-TLX", in 《Human Mental Workload》, North-Holland, 1988. Strayer, D.L., Drews, F.A. & Crouch, D.J., "A comparison of the cell phone driver and the drunk driver", Human Factors 48(2), 2006, pp.381-391. |

증강현실의 약속은 '정보를 보던 곳에 그대로 얹어 준다'이다. 스마트폰을 꺼내 고개를 숙이는 전환 비용을 없애 준다는 논리다. 절반은 맞다. 그러나 Wickens의 다중 자원 이론이 말하는 바는, 주의가 하나의 통짜 자원이 아니라 채널별로 나뉜 자원 풀이라는 것이다. 시각과 청각은 어느 정도 병렬 처리되지만, 같은 시각 채널 안에서 두 과제를 하면 자원을 직접 나눠 쓴다. 증강현실은 정보를 바로 그 시각 채널에 밀어 넣는다. 운전자가 앞을 보면서 속도를 읽는 것은 물리적 시선 이동을 줄이지만, 속도를 '읽는' 인지 처리 자체는 도로를 '해석하는' 처리와 같은 자원을 놓고 경쟁한다. 그래서 시선 이동 시간이 줄었다는 측정치가 곧 안전 개선을 뜻하지 않는다. 더 나아가 인지 부하는 시각 처리와 무관해 보이는 활동으로도 올라간다. 대화, 계산, 음성 명령 구성 같은 것들이다. 부하가 올라가면 유효 시야(useful field of view)가 좁아지고 주변부 사건 탐지가 떨어진다. 시선은 여전히 도로를 향하지만 보지 못하는 상태가 된다.

### 부주의 맹시와 인지적 포획
| 항목 | 내용 |
| --- | --- |
| 수치 | Simons & Chabris(1999): 조건 통합 시 약 50%가 고릴라를 보고하지 못했고, 가장 어려운 조건에서는 미탐지율이 훨씬 높았다(탐지율 8%대까지 떨어진 변형 조건 보고). Most 등: 주의 대상과 같은 색의 예상치 못한 자극은 약 94%가 탐지, 대비되는 색은 약 6%만 탐지. Fischer, Haines & Price(1980): HUD 조건에서 활주로 침입 항공기를 탐지하지 못한 조종사가 다수 발생. |
| 출처 | Simons, D.J. & Chabris, C.F., "Gorillas in our midst: sustained inattentional blindness for dynamic events", Perception 28(9), 1999, pp.1059-1074. Most, S.B. et al., "How not to be seen: The contribution of similarity and selective ignoring to sustained inattentional blindness", Psychological Science 12(1), 2001, pp.9-17. Fischer, E., Haines, R.F. & Price, T.A., "Cognitive issues in head-up displa |

부주의 맹시는 시야 한가운데 있고 눈이 향해 있는데도 보지 못하는 현상이다. Simons와 Chabris의 고릴라 실험이 이를 대중에 각인시켰다. 농구 패스 횟수를 세라는 과제를 주면, 화면 한가운데로 고릴라 옷을 입은 사람이 9초 동안 걸어 들어와 가슴을 두드리고 나가도 관찰자의 절반가량이 알아채지 못한다. 핵심 기제는 '주의 집합(attentional set)'이다. 뇌는 과제에 맞는 특징으로 필터를 설정하고, 그 필터에 걸리지 않는 것은 망막에 맺혀도 의식에 도달하지 않는다. Most 등의 실험이 이를 깔끔히 보여준다. 흰 글자를 추적하는 과제에서 흰 십자가가 지나가면 대부분이 알아채지만, 검은 십자가가 지나가면 거의 아무도 못 본다. 증강현실에 이것이 치명적인 이유는 두 방향으로 작동하기 때문이다. 첫째, 겹쳐 놓은 경고가 사용자의 주의 집합에 맞지 않으면 안 보인다 — 띄웠다고 전달된 것이 아니다. 둘째, 더 위험하게는 증강 콘텐츠가 주의 집합을 장악해 실세계의 예기치 못한 사건을 가린다. 항공 분야에서 이를 인지적 포획(cognitive capture)이라 부른다. HUD를 쓴 조종사가 착륙 성능은 좋아졌는데 활주로 위에 서 있는 항공기를 못 보고 착륙을 이어 간 시뮬레이터 실험이 1980년에 이미 보고되었다.

### 운전 중 증강현실 — HUD 연구가 실제로 말하는 것
| 항목 | 내용 |
| --- | --- |
| 수치 | 시속 100 km ≈ 27.8 m/s이므로 지연 100 ms당 종방향 2.8 m 오차. 일반 차량 HUD의 가상 영상 거리는 약 2~3 m(0.33~0.5디옵터), 증강현실 HUD는 7~15 m급으로 설계되는 추세. 미국 교통안전 통계에서 주의분산 운전은 연간 사망자 수천 명 규모에 관여하는 요인으로 집계된다. 반응 시간 측면에서, 인지 부하가 높은 이차 과제는 제동 반응을 통상 수백 ms 지연시킨다. |
| 출처 | Gabbard, J.L., Fitch, G.M. & Kim, H., "Behind the Glass: Driver Challenges and Opportunities for AR Automotive Applications", Proceedings of the IEEE 102(2), 2014, pp.124-136. Kim, S. & Dey, A.K., "Simulated augmented reality windshield display as a cognitive mapping aid for elder driver navigation", CHI 2009. 항공 HUD의 원조 경고는 앞 항목의 NASA TP-1711. |

차량용 HUD는 상용화된 증강현실 중 가장 오래된 축이고, 따라서 실증 데이터가 가장 두텁다. 그림은 양면적이다. 이득 쪽은 명확하다. 속도나 내비게이션 지시를 앞유리에 띄우면 계기판을 보려고 고개와 시선을 내리는 시간이 줄고, 눈이 먼 곳에서 가까운 곳으로 다시 초점 맞추는 재조절 시간도 아낀다. 항공 HUD를 광학적으로 무한대에 맺히도록(collimation) 만드는 이유가 이것이다. 대가 쪽도 명확하다. 인지적 포획으로 예기치 못한 사건 탐지가 떨어지고, 정보를 더 얹을수록 시각 채널 경쟁이 심해진다. 여기에 증강현실 HUD 특유의 문제가 더해진다. 단순 속도 표시는 위치가 틀려도 무방하지만, 앞차에 테두리를 그리거나 차선 위에 화살표를 깔려면 정합이 맞아야 한다. 차량 HUD는 가상 영상 거리가 유한(보통 2~3 m, 증강현실형은 7~15 m)한데 실제 대상은 수십 미터 밖에 있으므로 시차(parallax)가 생기고, 운전자 머리 위치가 조금만 달라져도 어긋난다. 게다가 시속 100 km에서는 100 ms의 지연이 2.8 m의 위치 오차를 만든다. 잘못 정합된 강조 표시는 없느니만 못하다 — 엉뚱한 곳을 보게 만들기 때문이다.

### 보행 중 증강현실 — 포켓몬 GO라는 자연실험
| 항목 | 내용 |
| --- | --- |
| 수치 | 포켓몬 GO 출시일 2016년 7월 6일, 첫 달 다운로드 1억 건 이상. Faccio와 McConnell은 미국 한 카운티의 경찰 사고 기록을 분석해 포켓스톱 인근 사고 증가를 보고했고, 이를 전국으로 외삽해 출시 후 148일간 수십억 달러 규모의 사회적 비용을 추정했다(추정치 폭이 매우 넓음). 게임사는 이후 시속 일정 속도 이상에서 경고 및 기능 제한, '운전자입니다' 확인 절차를 도입했다. |
| 출처 | Faccio, M. & McConnell, J.J., "Death by Pokémon GO: The Economic and Human Cost of Using Apps While Driving", Journal of Risk and Insurance, 2020. 보행자 휴대기기 부상 추세는 Nasar, J.L. & Troyer, D., "Pedestrian injuries due to mobile phone use in public places", Accident Analysis & Prevention 57, 2013, pp.91-95. |

2016년 포켓몬 GO는 인간요인 연구자들에게 뜻밖의 선물이었다. 수억 명이 동시에, 같은 날짜에, 위치 기반 증강현실 게임을 시작했다. 개입 시점이 날카롭게 정의된 준실험 설계가 저절로 만들어진 것이다. 연구자들은 출시 전후의 교통사고·보행자 부상 기록을 비교했고, 게임 내 좌표(포켓스톱·체육관)와 사고 위치의 공간적 상관을 볼 수 있었다. 결과는 위험 증가 쪽으로 수렴했으나, 크기 추정치는 연구마다 크게 갈렸고 특히 전국 단위 비용 외삽은 가정에 민감했다. 기제는 앞 항목들의 조합이다. 보행자가 화면을 볼 때 걷기라는 자세 제어 과제는 시각 자원을 빼앗기고, 유효 시야가 좁아지며, 주의 집합이 게임 요소에 맞춰지면서 연석·자전거·차량이 부주의 맹시의 대상이 된다. 증강현실 특유의 문제도 있다. 게임은 본질적으로 사용자를 물리적 장소로 이동시키는데, 그 장소의 안전성은 게임이 통제하지 못한다. 선로, 절벽, 군사 시설, 사유지에 좌표가 찍힐 수 있다. 이것은 소프트웨어가 물리 공간의 위험을 소환하는 새로운 형태의 안전 문제다.

### 구글 글래스 — 기술이 아니라 사회적 계약에서 실패했다
| 항목 | 내용 |
| --- | --- |
| 수치 | Explorer 프로그램: 2013년 4월 16일 배포 개시, 가격 1,500달러. 2014년 4월 15일 일반 판매(하루 만에 재고 소진). 2015년 1월 15일 Explorer 프로그램 종료. Enterprise Edition은 2023년 3월 15일 판매 종료, 2023년 9월 15일 지원 종료. 시애틀의 한 술집이 2013년 3월 착용 금지를 공표한 것이 상징적 사건으로 인용된다. |
| 출처 | 구글 글래스 연표는 Google 공식 발표 및 보도(위키백과 Google Glass 문서 교차 확인). 방관자 태도 실증은 Denning, T., Dehlawi, Z. & Kohno, T., "In situ with bystanders of augmented reality glasses: Perspectives on recording and privacy-mediating technologies", CHI 2014. 용도에 따른 수용 차이는 Profita, H. et al., "The AT effect: How disability affects the perceived social acceptability of head-mounted display use", CHI 2016. |

구글 글래스를 '기술이 미숙해서 실패한 제품'으로 기억하는 것은 잘못된 교훈을 남긴다. 배터리와 시야각도 문제였지만, 치명상은 착용자가 아닌 주변 사람들에게서 왔다. 얼굴에 카메라를 달고 걷는 사람 앞에서, 상대는 자신이 촬영되고 있는지 알 수 없었다. 스마트폰은 촬영할 때 팔을 들어 화면을 상대에게 향하는 명백한 신체 신호를 낸다 — 이 신호가 사회적 계약의 핵심이었는데, 안경형 기기는 그것을 지웠다. 반응은 빨랐다. 술집과 카지노, 병원, 영화관, 탈의실이 착용을 금지했고, 'Glasshole'이라는 멸칭이 만들어졌으며, 구글 자신이 2014년에 착용자 에티켓 가이드를 발표해야 했다 — 회사가 사용자에게 '무례하게 굴지 말라'고 공지해야 하는 상황 자체가 수용 실패의 증거다. 여기서 뽑아야 할 원칙은 세 가지다. 첫째, 착용형 기기의 수용은 착용자 효용이 아니라 방관자 비용으로 결정된다. 둘째, 사회적 신호(무엇을 하는 중인지 밖에서 보이는가)는 부가 기능이 아니라 핵심 설계 요구다. 셋째, 용도가 수용을 바꾼다. 같은 형태의 기기라도 명확한 직무나 보조기기 맥락에서는 훨씬 잘 받아들여진다는 것이 이후 연구로 확인되었고, 구글 글래스 자체도 산업·의료용 Enterprise Edition으로 살아남았다.

### 방관자 문제 — 동의하지 않은 사람의 권리
| 항목 | 내용 |
| --- | --- |
| 수치 | 미국 일리노이주 생체정보 프라이버시법(BIPA, 740 ILCS 14, 2008)은 생체식별자 수집에 사전 서면 동의를 요구하고 사인의 소권을 인정해 대규모 배상 사례를 낳았다. 텍사스주 CUBI(2009), 워싱턴주법도 유사. EU GDPR 제9조는 신원 확인 목적의 생체정보를 특별 범주로 분류해 원칙적 처리 금지 후 예외를 열거한다. 제조사 대응 예: 카메라 동작 시 점등되는 표시등(끌 수 없도록 설계), 녹화 시작 시 음성·시각 알림. |
| 출처 | 740 ILCS 14 (Illinois Biometric Information Privacy Act). Regulation (EU) 2016/679 (GDPR) Art. 9. 방관자 관점 실증은 Denning et al., CHI 2014; Koelle, M., Kranz, M. & Möller, A., "Don't look at me that way! Understanding user attitudes towards data glasses usage", MobileHCI 2015. |

증강현실 기기의 프라이버시 논의는 대개 사용자 데이터를 어떻게 보호할 것인가로 흐른다. 그러나 구조적으로 더 어려운 문제는 사용자가 아닌 사람 쪽에 있다. 방관자는 계약을 맺지 않았고, 이용 약관에 동의한 적이 없으며, 기기를 끌 수도 없고, 애초에 기기가 켜져 있는지 알 방법이 제한적이다. 게다가 요즘 증강현실 기기는 '녹화'만 하는 것이 아니다. 공간 이해를 위해 상시 카메라와 깊이 센서로 주변을 스캔하고, 평면과 사물을 인식하며, 그 결과를 지도로 저장한다. 즉 명시적 촬영 버튼을 누르지 않아도 방관자의 신체·행동·공간이 센서를 통과한다. 여기에 얼굴 인식이 결합되면 문제의 성격이 달라진다 — 길에서 마주친 사람의 신원이 자동으로 뜨는 상황은 기술적으로 오래전부터 가능했고, 실제로 억제해 온 것은 기술 한계가 아니라 기업의 자제와 법적 위험이었다. 현재의 방어선은 세 겹이다. 하드웨어 신호(녹화 중 LED, 물리 셔터), 플랫폼 정책(얼굴 인식 API 차단), 법제(생체정보 사전 동의 요구). 세 겹 모두 취약하다. LED는 가릴 수 있고, 정책은 바뀌며, 법은 관할권마다 다르다.

### 시선 추적 프라이버시 — 눈은 거짓말을 못 한다
| 항목 | 내용 |
| --- | --- |
| 수치 | 연구용 시선 추적기는 30 Hz부터 240·350·1000~1250 Hz까지 쓰인다. 증강현실·가상현실 내장 추적기는 통상 수십~120 Hz대. 사람의 안구 도약(saccade)은 최대 각속도 수백 °/s에 달하고, 평균 응시(fixation)는 수백 ms 단위다. 1시간 사용이면 양안 120 Hz 기준 수십만 개의 시선 표본이 쌓인다. |
| 출처 | Kröger, J.L., Lutz, O.H.-M. & Müller, F., "What Does Your Gaze Reveal About You? On the Privacy Implications of Eye Tracking", in Privacy and Identity Management (IFIP AICT 576), Springer, 2020, pp.226-241. 시선 기반 재식별은 Eberz, S. et al., "Looks Like Eve: Exposing Insider Threats Using Eye Movement Biometrics", ACM TOPS, 2016. 차등 프라이버시 적용은 Steil, J. et al., "Privacy-Aware Eye Tracking Using Different |

시선 추적은 증강현실 기기의 핵심 기술이 되었다. 시선이 향한 곳만 고해상도로 렌더링해 연산을 아끼고(포비티드 렌더링), 시선으로 대상을 선택하며, 동공간거리를 자동 보정한다. 그런데 이 신호는 성능 데이터가 아니라 심층적인 개인 정보다. 이유는 두 가지다. 첫째, 시선은 대부분 수의적 통제 밖이다. 자극에 이끌린 순간적 응시, 동공 크기 변화, 미세 떨림, 자발적 눈깜빡임은 의도로 조절할 수 없다. 프라이버시 보호의 표준 수단인 '동의'와 '자제'가 여기서는 작동하지 않는다. 둘째, 그 신호에서 추론되는 것의 폭이 대단히 넓다. 기계학습 분석으로 나이·성별·인종적 배경·성격 특성·현재 인지 부하와 피로·전문성 수준·언어 능력·흥미와 욕구·약물과 알코올의 영향, 나아가 자폐 스펙트럼·ADHD·조현병·파킨슨병·알츠하이머 같은 신경·정신 질환의 단서까지 추정 가능하다고 보고된다. 여기에 더해 시선 운동 패턴 자체가 개인 식별자로 작동할 수 있다 — 익명화된 시선 로그가 재식별의 통로가 된다. 대응은 두 갈래다. 아키텍처적으로 시선 원신호를 앱에 아예 노출하지 않고 시스템 프로세스 안에 가두는 방식(사용자가 확정 입력을 한 순간의 결과만 앱에 전달), 그리고 수학적으로 시선 시계열에 차등 프라이버시 잡음을 넣는 방식이다.

### 접근성 — 색각이상, 저시력, 안경, 그리고 대비를 보장할 수 없다는 문제
| 항목 | 내용 |
| --- | --- |
| 수치 | 적록색각이상은 북유럽계 남성 약 8%, 여성 약 0.5%. WCAG 2.1 대비 기준은 일반 텍스트 4.5:1, 큰 텍스트 및 그래픽 구성요소 3:1. 근시 유병률은 동아시아에서 특히 높아, 서울 19세 남성 징병검사 표본에서 96.5%가 근시로 보고된 바 있다. 안경 착용을 수용하려면 아이릴리프 약 18~20 mm 이상이 필요하며, 상용 기기는 흔히 도수 인서트로 이를 대체한다. 야외 조도 최대 10만 lux에 대비하려면 매우 높은 디스플레이 휘도가 요구된다. |
| 출처 | WCAG 2.1 (W3C Recommendation, 2018) Success Criterion 1.4.3, 1.4.11. 색각이상 유병률은 Birch, J., "Worldwide prevalence of red-green color deficiency", JOSA A 29(3), 2012. 한국 근시 유병률은 Jung, S.K. et al., "Prevalence of myopia and its association with body stature and educational level in 19-year-old male conscripts in Seoul", IOVS 53(9), 2012. |

일반 화면의 접근성 지침은 배경을 설계자가 통제한다는 전제 위에 서 있다. 웹 접근성 지침이 텍스트와 배경의 명도 대비를 4.5:1 이상으로 요구할 수 있는 것은 배경색을 설계자가 정하기 때문이다. 광학 투시형 증강현실은 이 전제를 깨뜨린다. 배경은 사용자가 지금 바라보고 있는 실제 세계이고, 흰 벽일 수도 대낮의 아스팔트일 수도 나뭇잎 그늘일 수도 있다. 게다가 대부분의 광학 투시 디스플레이는 빛을 '더하기'만 할 수 있어 검은색을 표현하지 못한다 — 검게 지정한 픽셀은 그냥 투명해진다. 따라서 밝은 배경 위에 어두운 글씨라는 가장 읽기 좋은 조합을 원리적으로 쓸 수 없다. 여기에 통상적 접근성 문제가 겹친다. 색으로만 정보를 구분하면 적록색각이상 사용자가 놓치고, 저시력 사용자는 확대가 필요한데 증강 콘텐츠는 실세계와 크기가 연동되어 있어 단순 확대가 정합을 깨뜨린다. 안경 착용자는 기기가 아이릴리프를 충분히 확보하지 않으면 아예 쓸 수 없거나, 도수 인서트라는 별도 비용을 치른다. 역방향의 기회도 있다. 증강현실은 저시력 보조 도구로서 실세계를 확대·대비 강화·윤곽 강조해 보여줄 수 있고, 청각 장애인에게 화자 위에 실시간 자막을 띄울 수 있다.

### 아동 사용 안전 — 연령 기준과 그 근거의 빈약함
| 항목 | 내용 |
| --- | --- |
| 수치 | 제조사 연령 지침(변동 가능): Meta Quest는 2023년 이후 10세 이상 계정 허용(이전 13세), Apple Vision Pro는 13세 이상, PlayStation VR2는 12세 이상. 광과민성 발작은 인구 약 4,000명당 1명, 뇌전증 환자의 약 5%가 광과민성이며 여성과 젊은 층에서 더 흔하다. 1997년 일본 애니메이션 방영 사건에서 수백 명이 병원 이송되고 만 명 이상이 증상을 호소했다. 콘텐츠 규범: WCAG는 1초에 3회를 초과하는 번쩍임을 금지하고, ITU-R BT.1702가 방송 영상의 광과민성 위험 저감을 권고한다. 아동 동공간거리는 성인 하한(약 52~58 mm)을 밑도는 경우가 흔하다. |
| 출처 | 광과민성 뇌전증 유병률 및 지침: Harding, G. et al., "Photic- and pattern-induced seizures: Expert consensus of the Epilepsy Foundation of America Working Group", Epilepsia 46(9), 2005. ITU-R BT.1702. WCAG 2.1 SC 2.3.1. 연령 지침은 각 제조사 공식 안전 고지. 동공간거리 분포는 ANSUR II (2012). |

제조사들은 머리 착용 디스플레이에 연령 하한을 붙여 왔다. 그런데 이 숫자들의 과학적 근거는 흔히 생각하는 것보다 얇다. 우려의 근거로 제시되는 것은 대략 네 가지다. 첫째, 아동의 양안시와 조절 기능은 발달 중이며, 폭주-조절 충돌에 장기간 노출되는 것이 발달에 어떤 영향을 주는지에 대한 장기 추적 연구가 사실상 없다. 둘째, 물리적 미스핏이 확실하다. 아동의 동공간거리는 성인 기기의 조절 하한을 밑돌아, 아이가 쓰면 렌즈 중심이 눈 바깥쪽에 놓이고 상이 왜곡되며 부적절한 폭주 요구가 생긴다. 이는 추정이 아니라 측정 가능한 사실이다. 셋째, 무게와 목 부담이다. 아동의 머리 대비 목 근력 비율은 성인과 다르다. 넷째, 광과민성 발작 위험으로, 눈에서 몇 센티미터 떨어진 화면이 시야 대부분을 채우면 플래시 자극의 망막 면적 비율이 TV보다 훨씬 커진다. 여기에 인간요인 이외의 문제 — 실공간을 이동하게 만드는 콘텐츠의 물리적 안전, 상시 센서가 수집하는 아동 생체정보 — 가 겹친다. 정직한 결론은 이렇다. 단기 안전 문제(미스핏, 발작, 낙상)는 충분히 근거가 있고 대응책도 명확하지만, 장기 시각 발달 영향은 아직 데이터가 없다. 연령 하한은 예방 원칙에 따른 보수적 설정이지 실증된 임계값이 아니다.

### 잔여 효과와 노출 관리 — 벗은 다음에도 끝나지 않는다
| 항목 | 내용 |
| --- | --- |
| 수치 | 군용 시뮬레이터 운용에서 노출 후 조종 금지 시간은 통상 12~24시간 범위로 규정되어 왔다(기관·기종별 상이). 프리즘 적응 실험에서 시각 변형에 대한 적응과 그 해제(readaptation)는 수십 초~수 분 단위로 일어나지만, 강한 노출일수록 잔여가 길어진다. 카메라 투시형 기기에서 카메라가 눈보다 수 cm 앞·위에 있으면 그만큼의 시점 오프셋이 손 뻗기 오차로 나타난다. |
| 출처 | Kennedy, R.S., Stanney, K.M. & Dunlap, W.P., "Duration and exposure to virtual environments: sickness curves during and across sessions", Presence 9(5), 2000, pp.463-472. Stanney, K.M. et al., "What to expect from immersive virtual environment exposure: Influences of gender, body mass index, and past experience", Human Factors 45(3), 2003, pp.504-520. |

사이버 멀미 논의는 대개 착용 중의 증상에서 멈춘다. 그러나 시뮬레이터 인간요인 연구가 수십 년 전에 확립한 사실은, 증상의 상당 부분이 기기를 벗은 뒤에 나타나거나 지속된다는 것이다. 이를 잔여 효과(after-effect)라 부른다. 기제는 순응의 뒷면이다. 착용 중 뇌는 새로운 시각-전정 관계에 맞춰 내부 모델을 조정한다. 벗는 순간 세계는 원래대로 돌아왔는데 내부 모델은 조정된 상태로 남아 있고, 이제는 정상 세계가 어긋나 보인다. 나타나는 증상은 자세 불안정과 균형 저하, 손-눈 협응 오차, 시각 흐림과 잔상, 방향감각 혼란, 그리고 노출이 끝난 뒤 몇 시간 후에 예고 없이 찾아오는 어지럼의 재발(플래시백)이다. 마지막 것이 특히 문제인데, 본인은 이미 회복했다고 믿고 운전대를 잡은 뒤에 일어나기 때문이다. 미군 시뮬레이터 운용 규정이 훈련 후 일정 시간 비행·운전을 금지해 온 이유가 여기에 있다. 증강현실도 예외가 아니다. 특히 시야를 광학적으로 변형하는 기기(배율이 있거나 카메라 투시형이라 시점이 실제 눈 위치와 다른 경우)는 벗은 뒤 손 뻗기 오차를 남긴다.

#### 검증에서 잡힌 정정
- Magic Leap One 초점면 '약 0.75 m와 2 m 상당' — 단위 오류. Cercenelli et al. 2023(PMC10054537) Table 1의 직접 비교: Magic Leap 1 = 'Double fixed at 0.5 and 1.5 m'(2.0 D / 0.67 D), HoloLens 2 = 'Single fixed at 2 m'. 0.75는 미터가 아니라 디옵터로 보고된 값(0.75 D = 1.33 m)이며, 이를 미터로 옮겨 적었다. 같은 표에서 Magic Leap 1의 시야각도 50° 대각(40°H×30°V)으로, 본문이 인용한 Magic Leap 2의 70°와 혼동하지 않도록 구분이 필요하다.
- 'HoloLens 2의 고정 초점면 0.5디옵터 → 콘텐츠를 약 1.1 m~무한대 구간에 두면 0.4디옵터 이내에 든다' — 산술 오류. 0.5 D ± 0.4 D = 0.1~0.9 D이므로 실제 구간은 1.11 m ~ 10 m다. 무한대는 0 D이므로 불일치가 0.5 D로 0.4 D 한계를 넘는다. Microsoft 공식 지침(learn.microsoft.com mixed-reality/design/comfort)도 'the optimal zone for hologram placement is between 1.25 m and 5 m'이며 40 cm 페이드아웃·30 cm 클리핑을 권고한다. 상한을 무한대로 둔 것은 산술과 제조사 지침 양쪽에 어긋난다.
- '대다수 사용자가 견디는 편안한 영역은 폭주-조절 불일치 약 0.4디옵터 이내(Shibata et al. 2011)' — 해당 논문에 없는 수치이자 원리 왜곡. Shibata et al. 2011(J Vis 11(8):11, DOI 10.1167/11.8.11) 초록 원문: 'conflicts of a given dioptric value were slightly less comfortable at far than at near distance', 그리고 'negative conflicts (stereo content behind the screen) are less comfortable at far distances and that positive conflicts (content in front of screen) are less comfortable at near distances'. 즉 논문의 핵심 발견은 편안한 영역이 시청 거리와 불일치의 부호에 따라 비대칭적으로 변한다는 
- 'Fischer, Haines & Price(1980): HUD 조건에서 활주로 침입 항공기를 탐지하지 못한 조종사가 다수 발생' — 수량 과장. NASA TP-1711 원 초록(NTRS ID 19810005125): 조종사 8명이 고정형 727 시뮬레이터에서 HUD 18회·통상계기 13회 접근을 수행했고 'two of the pilots did not see the obstacle at all with the HUD' — 8명 중 2명(25%)으로 다수가 아니라 소수다. 또한 이 연구의 대표 수치는 미탐지 인원이 아니라 활주로 장애물에 대한 평균 반응시간 4.13초(HUD) 대 1.75초(HUD 없음)이며, 본문은 이 핵심 수치를 누락했다. 표본이 8명이라는 점도 함께 밝혀야 한다.
- 'Most 등: 주의 대상과 같은 색의 예상치 못한 자극은 약 94%가 탐지, 대비되는 색은 약 6%만 탐지' — 조작 변인 오기 및 원리 역전. Most et al. 2001(Psychol Sci 12(1):9-17) 초록 원문은 'The more similar an unexpected object is to the attended items, and the greater its difference from the ignored items, the more likely it is that people will notice it'로, 저탐지 조건은 '대비되는 색'이 아니라 '무시하도록 지시받은 집합과 같은 색'이다(논문 제목의 selective ignoring). 결정적으로 같은 논문 실험 3은 'nearly 30% of observers failed to notice a bright red cross move across the display, even though it had a
- 'Tsubota, K. & Nakamura, K., New England Journal of Medicine 328, 1993, p.584' — 저자명 오류. Europe PMC 및 인용 종설(PMC9790652) 참고문헌 원문 모두 'Tsubota K & Nakamori K (1993): Dry eyes and video display terminals. N Engl J Med 328: 584' — 제2저자는 Nakamura가 아니라 Nakamori K다(동일 저자쌍의 1995년 Arch Ophthalmol 113:155-158도 Nakamori).
- '눈깜빡임은 대화 중 분당 약 15~22회에서 화면 집중 시 분당 약 5~7회로 감소' 및 '깜빡임 횟수가 3분의 1 수준으로 떨어진다' — 인용 출처의 실측치와 불일치. Tsubota & Nakamori 1993의 보고치는 이완 22회/분, 독서 10회/분, VDT 7회/분으로 '대화' 조건이 없고 5회/분이라는 값도 없다. 문헌 표준 대조치는 Bentivoglio et al. 1997(Mov Disord 12:1028-1034)의 '대화 26회/분 → VDT 14.5회/분'이다(PMC9790652 본문 인용: 'Blink frequency has been shown to fall from 26 blinks/min in conversation to 14.5 blinks/min during VDT use'). 따라서 대화 기준치는 15~22가 아니라 약 26회/분이고, 화면 사용 시 감소폭은 3분의 1(-67%)이 아니라 약 45%다. -67%에 가까운 값은 화면이 아니라 '독서' 
- 'Stoffregen & Smart: 멀미 취약군의 사전 동요 증가는 통상 노출 전 수십 초~수 분 구간에서 관측된다' — 시점 오기. 인용 논문의 제목 자체가 'Postural instability precedes motion sickness'로, 자세 동요 증가가 앞서는 대상은 '노출'이 아니라 '멀미 증상 발현'이다. 측정은 광학 흐름 노출 중에 이뤄지며, 증상 보고 이전 구간에서 동요 증가가 관측된다. '노출 전'이라고 쓰면 노출이 시작되기도 전에 예측 지표가 나온다는 뜻이 되어 논문 설계와 맞지 않는다.
- '연구용 시선 추적기는 30 Hz부터 240·350·1000~1250 Hz까지 쓰인다' — 상한 과소. 연구용 상용기의 표본율 상한은 2000 Hz다(SR Research EyeLink 1000 Plus / Portable Duo 단안 2000 Hz). 1000~1250 Hz를 천장으로 제시하면 프라이버시 논거인 '표본 밀도'를 절반으로 축소하게 된다. 다만 이어지는 '1시간 양안 120 Hz → 수십만 표본'은 120×3600×2=864,000으로 계산이 맞다.
- 'Simons & Chabris(1999): 조건 통합 시 약 50%가 고릴라를 보고하지 못했고' — 수치 귀속 부정확. 논문 원문(Perception 28:1059-1074): 'Out of all 192 observers across all conditions, 54% noticed the unexpected event and 46% failed to notice' — 이 46%는 고릴라와 우산 여성 두 사건을 합친 값이고, 고릴라 단독 조건 통합 탐지율은 44%(미탐지 56%)다. 정확히 50% 미탐지가 나오는 것은 12명을 대상으로 한 가슴두드림 추가 조건뿐이다. 한편 '탐지율 8%대까지 떨어진 변형 조건'은 Table 1의 Transparent/Gorilla 셀 두 곳에서 8%로 정확하며, '9초' 지속도 원문('this action began after 35 s and lasted 9 s')과 일치한다.
- '상용 기기의 조절 범위는 대체로 58~72 mm 수준이라 분포의 양 끝을 못 담는다' — 구식 수치. 3자리 고정 슬라이더 세대(Quest 2: 58/63/68 mm)의 값이며, 이후 세대는 연속 조절로 범위가 넓어져 ANSUR II 분포의 1~99 백분위(여 53.5~70.5, 남 56.0~72.5)를 상당 부분 포괄한다. '못 담는다'는 결론을 유지하려면 기기 세대와 모델을 명시해야 한다.
- '40 cm(2.5디옵터) 거리에 UI를 띄우면 불일치가 2디옵터에 달해 편안한 영역을 5배 초과한다' — 표현상 수치 오류. 2.5-0.5=2.0 D는 맞지만, 2.0 D는 0.4 D 한계의 5'배'이고 '초과분'은 1.6 D로 한계의 4배다. '5배 초과'는 한계의 6배(2.4 D)를 뜻하게 되어 1.6배만큼 부풀려진 진술이다.
- [산수 오류·확인됨] '초점면 2 m(0.5 D)인 HoloLens 2에서 콘텐츠를 약 1.1 m~무한대 구간에 두면 0.4 D 이내에 든다' → 무한대는 0 D이므로 불일치가 0.5 D로 스스로 세운 0.4 D 기준을 넘는다. 0.5±0.4 D = 0.1~0.9 D이므로 실제 구간은 약 1.11 m~10 m다. 근거: Microsoft Learn 'Comfort - Mixed Reality' 공식 지침은 'HoloLens displays are fixed at an optical distance approximately 2.0 m'이며 'the optimal zone for hologram placement is between 1.25 m and 5 m', 40 cm 페이드아웃·30 cm 클리핑을 권고한다. 무한대는 권고 구간 밖이다.
- [오인용·확인됨] '대다수 사용자가 견디는 편안한 영역은 폭주-조절 불일치 약 0.4디옵터 이내(Shibata et al. 2011)' → Shibata et al. 2011은 단일 대칭 임계값 0.4 D를 제시한 논문이 아니다. 초록 원문: 'We found that conflicts of a given dioptric value were slightly less comfortable at far than at near distance' / 'negative conflicts (stereo content behind the screen) are less comfortable at far distances and positive conflicts (content in front of screen) are less comfortable at near distances.' 즉 이 논문의 두 주 결과는 (a) 같은 디옵터라도 원거리에서 더 불편하다는 거리 의존성, (b) 초점면 앞/뒤에 
- [과장·확인됨] 'Fischer, Haines & Price(1980): HUD 조건에서 활주로 침입 항공기를 탐지하지 못한 조종사가 다수 발생' → NASA TP-1711 원문은 상용 항공사 조종사 8명을 대상으로 했고 '두 명'만 장애물을 전혀 보지 못했다. 원문: 'Two of the pilots did not see the obstacle at all. Both of these runs were with HUD and were the pilots' first exposures to the obstruction.' 8명 중 2명(25%)은 '다수'가 아니며, 두 사례 모두 '첫 노출'이라는 결정적 조건이 붙는다. (부기: 저자는 Fischer, E. / Haines, R.F. / Price, T.A. 3인이 맞다.)
- [두 실험 혼합·확인됨] 'Simons & Chabris(1999): 조건 통합 시 약 50%가 고릴라를 보고하지 못했고 … 고릴라 옷을 입은 사람이 9초 동안 걸어 들어와 가슴을 두드리고 나가도 관찰자의 절반' → 원 논문상 본실험(n=192)의 예상치 못한 사건은 '5초'이고(‘the unexpected event lasted 5 s’), 전체 미탐지율은 46%(탐지 54%), 고릴라 조건만 보면 탐지 44%(미탐지 56%)다. '9초 + 가슴 두드림 + 50%'는 본실험이 아니라 관찰자 12명만 참여한 별도 추가 조건의 값이다(원문: 'this action began after 35 s and lasted 9 s in a stimulus tape 62 s long' / 'Twelve new observers … only 50% noticed the event'). 서로 다른 두 실험의 숫자를 한 문장에 합쳤다.
- [조건 오기·확인됨] '가장 어려운 조건에서는 미탐지율이 훨씬 높았다(탐지율 8%대까지 떨어진 변형 조건)' → 표 1에서 탐지율 8%가 나온 칸은 Transparent/Gorilla × 흰 팀 주의 조건이며, Easy 8%·Hard 8%로 과제 난이도와 무관했다. 8%를 만든 변인은 '난이도'가 아니라 반투명 중첩 표시 방식과 주의 대상 팀 색(흰색)과 고릴라 색(검정)의 불일치다. 실제로 논문은 검은 팀 주의 시 고릴라 탐지 58%, 흰 팀 주의 시 27%로 색 유사성 효과를 주 원인으로 지목한다.
- [이론 결손] 감각 충돌 이론을 '시각·전정·고유수용 세 추정치가 서로 어긋나면 멀미'로 서술 → Reason & Brand의 정식화와 Oman 1990(본문이 인용한 바로 그 문헌)의 핵심은 '현재 감각 입력 vs 내부 모델(과거 노출 경험 + 원심성 복사)이 예측한 입력'의 불일치, 즉 신경 미스매치다. '예상값' 항을 빼면 (a) 순응(예측 모형 갱신), (b) 프리즘 착용·영화 관람처럼 충돌이 있어도 멀미가 없는 사례, (c) 시각 입력이 전혀 없는 암흑 중 코리올리 자극이나 시각장애인의 멀미를 설명할 수 없다. 단순 3자 불일치 모델은 멀미를 과대예측한다는 것이 이 이론의 표준적 자기비판이며, 그 때문에 Bles 등의 주관적 수직 충돌 이론이 나왔다.
- [생리 기술 오류] '속귀 전정기관의 가속도 신호' → 전정기관은 단일 가속도계가 아니다. 반고리관은 각속도(회전율)를 전달하는 관성 적분기이고, 이석기관이 선형가속도와 중력(중력관성력)을 전달한다. HMD 멀미의 주 동인이 머리 '회전' 중 시각-전정 각속도 불일치이고 AR 정합 오차 산식(°/s × 지연)이 각속도 기반인 이상, 이 구분은 표현 문제가 아니라 원리의 핵심이다.
- [인용 시점 오류] '멀미 취약군의 사전 동요 증가는 통상 노출 전 수십 초~수 분 구간에서 관측된다 … Stoffregen & Smart(1998)' → 해당 논문 'Postural instability precedes motion sickness'의 설계는 움직이는 방 노출 '중' 자세 동요를 계측해, 증상 보고 이전에 이미 동요가 증가해 있음을 보인 것이다. '노출 전(베이스라인) 동요가 이후 멀미를 예측한다'는 별개 주장으로, Smart·Stoffregen·Bardy(2002) 및 후속 VR 연구들의 결과다. 두 주장을 같은 출처로 묶었다.
- [법제 오류] 'BIPA는 … 사인의 소권을 인정해 대규모 배상 사례를 낳았다. 텍사스주 CUBI(2009), 워싱턴주법도 유사' → 사인의 소권(private right of action)은 일리노이 BIPA에만 있다. 텍사스 CUBI(Tex. Bus. & Com. Code §503.001)와 워싱턴주법(RCW 19.375)은 주 법무장관 전속 집행이며 개인 소송이 불가능하다. 문장 전체의 논지가 '소권 → 대규모 배상'인데, 바로 그 결정적 차이를 '유사'로 지워버렸다. 미국 생체정보 소송이 일리노이에만 집중된 이유가 이 차이다.
- [기제 방향 오류] 'late-stage reprojection: 최종 렌더 직전 최신 자세로 화면을 다시 밀어주는' → LSR은 렌더가 끝난 뒤, 스캔아웃 직전에 이미 렌더된 프레임을 최신 자세로 워프(재투영)하는 기법이다. '렌더 직전'이면 그것은 그냥 자세 예측(late latching)이지 reprojection이 아니다. 렌더 이후 단계라는 점이 이 기법이 지연을 줄이는 원리 자체다.
- [수치 귀속 오류] '눈깜빡임은 대화 중 분당 약 15~22회에서 화면 집중 시 분당 약 5~7회로 감소한다고 보고된다(Tsubota & Nakamura, NEJM 1993)' → 해당 NEJM 1993 서한(328:584)이 보고한 조건은 '대화'가 아니라 안정(relaxed) 약 22회/분, 독서 약 10회/분, VDT 작업 약 7회/분이다. '대화 중 15~22회'라는 구간은 그 문헌의 조건이 아니며, 중간값인 독서 조건(약 10회/분)이 누락되어 감소폭이 실제보다 극적으로 보인다.
- [근거 논문의 대상 오기] '보행 중 증강현실 — 포켓몬 GO라는 자연실험 … 연구자들은 출시 전후의 교통사고·보행자 부상 기록을 비교' 절의 주 근거로 Faccio & McConnell(2020)을 들었으나, 이 논문의 제목과 분석 대상은 'The Economic and Human Cost of Using Apps While Driving' — 즉 운전 중 앱 사용으로 인한 차량 사고·부상·사망의 경제적 비용이다. 보행자 부상 연구가 아니며, 포켓스톱 근접 효과도 차량 사고 기록(경찰 조서)에서 추정한 것이다. 보행 중 위험을 논하는 절의 근거로 쓰면 인과 주체가 뒤바뀐다.
- [기제 서술 오류] 'Most 등: 주의 대상과 같은 색의 예상치 못한 자극은 약 94%가 탐지, 대비되는 색은 약 6%만 탐지' → Most et al.(2001)의 주장은 단순한 색 '대비'가 아니라 주의 세트(attentional set)와 '능동적 무시(selective ignoring)'다. 탐지가 붕괴하는 조건은 예상치 못한 자극이 '무시하도록 지시받은 집합과 같은 색'일 때이며, 논문 제목 자체가 'the contribution of similarity and selective ignoring'이다. 주의 집합·무시 집합 어느 쪽과도 다른 제3의 색은 중간 수준으로 탐지된다 — 이 점이 단순 대비 모델과 갈리는 지점이고, AR UI 설계 함의(무시 대상으로 분류된 색을 경고에 쓰면 안 된다)도 여기서 나온다.
- [용어·기제 오류] '부하가 높을 때 유효 시야는 상당폭 축소되며, 이를 터널 시야라 부른다' → 인지 부하로 줄어드는 것은 유효시야(UFOV)라는 주의적 개념이고, 통상 cognitive tunneling(주의 협소화)으로 부른다. 'tunnel vision'은 임상적으로 주변 시야의 물리적 결손을 가리키는 별개 용어다. 더 중요한 오류는 기제인데, 본문이 함께 인용한 Strayer 계열과 Simons&Chabris 계열 결과의 요지는 '응시점 위 물체도 놓친다(look but fail to see)'이므로, 동심원 시야 축소 모델로 환원할 수 없다.
- [현황 낙후] '상용 기기의 조절 범위는 대체로 58~72 mm 수준이라 분포의 양 끝을 못 담는다' → 이는 Quest 2의 3단 고정(58/63/68 mm) 시절 서술이다. 현행 기기는 Quest 3가 약 53~75 mm 연속 조절, Apple Vision Pro가 약 51~75 mm로, 본문이 함께 제시한 ANSUR II 범위(여 51.0~74.5 mm, 남 53.0~77.0 mm)를 사실상 포괄한다. 남성 상단(77 mm)만 남는데, 이는 '양 끝'이 아니라 한쪽 끝이다.
- 폭주-조절 '편안한 영역 약 0.4디옵터 이내(Shibata et al. 2011)' — 원문에 없는 수치다. Shibata 등은 단일 임계값을 제시하지 않았고, comfort zone 상대폭의 최대 0.8 D·최소 0.3 D를 '가정'한 뒤(0.3 D는 눈의 초점심도, Campbell 1957) 회귀로 경계선을 추정했다. 경계는 비대칭·거리의존적이다(m_near=1.035, T_near=-0.626; m_far=1.129, T_far=0.442). 저자들도 'the resulting estimate is arguable'라고 명기했다. 2 m 초점면(0.5 D)에 이 식을 대입하면 허용 불일치는 근거리측 0.59 D, 원거리측 0.45 D다.
- 'HoloLens 2의 2 m 초점면에서 콘텐츠를 약 1.1 m~무한대에 두면 0.4디옵터 이내에 든다' — 자체 모순이다. 무한대는 0 D이므로 0.5 m 초점면(0.5 D)과의 불일치가 0.5 D여서 스스로 세운 0.4 D 기준을 넘는다. 0.4 D 이내를 지키려면 약 1.11 m~10 m다. Shibata 식으로는 약 0.92 m~19.5 m, 마이크로소프트 공식 지침은 1.25 m~5 m(= 0.8 D~0.2 D, 초점면 기준 정확히 ±0.3 D 대칭)이며 40 cm 미만 배치 금지·30 cm 렌더 클리핑을 권고한다.
- '40 cm(2.5 D) UI는 불일치 2 D로 편안한 영역을 5배 초과' — 2.0 ÷ 0.4 = 정확히 5배이므로 '5배 초과'가 아니고 초과분은 4배다. 기준값 0.4 D 자체도 위 항목대로 출처 미확인이다.
- (외 18건)

\newpage

# 조경 — 해외 사례

## firms
항목 16개 · 검증 정정 지적 60건

> 조사 결과의 핵심은 단순하다. 지목된 해외 조경설계사무소 8곳(Sasaki·SWA·Field Operations·West 8·Snøhetta·Gustafson Porter+Bowman·MVVA·Turenscape) 중 증강현실을 실제 프로젝트에 쓴 곳은 확인되지 않았다. Sasaki 웹사이트 전체 검색에서 'augmented'는 0건이고 가상현실 글 두 편(2017·2018)만 남아 있다. 사내 도구 조직 'Sasaki Strategies'의 관심사도 VR이었다. SWA의 XL Lab은 VR·MR·파노라마·360도 영상을 평가한 연구 'Immersive Environments' 하나를 남겼는데, 성격이 '비판적·평가적'이라고 스스로 적어두었다. West 8은 2016년 1월 28일 HoloLens 체험 글을 올렸다가 지웠다 — 아카이브에도 본문이 남지 않았다. Snøhetta·GP+B·MVVA·Turenscape·Field Operations는 자체 사이트 검색과 Wayback 색인 모두 0건이었다.  건축·도시설계 쪽은 사정이 낫지만 여전히 얇다. 실제 프로젝트 소통에 AR을 쓴 확인 사례는 Gensler가 사실상 유일하다. 2023년 5월 구글 Geospatial Creator 출범 파트너로 이름을 올리고, Adobe Aero로 비영리 DignityMoves의 노숙인 임시주거 안을 주민에게 실규모로 보여줬다. 이것은 구글 개발자 블로그라는 1차 자료로 확인된다. Perkins+Will은 2017년 10월 AR 앱 'AX'를 먼저, 12월에 VR 앱 'VX'를 냈는데 지금 애플 앱스토어에 둘 다 없고 AX 보도자료 페이지마저 자사 사이트에서 사라졌다. Foster + Partners의 ARD는 사내 협업 도구 'Glaucon'이 VR·AR·모바일·웹으로 열린다고 적어놓았을 뿐, 적용 프로젝트를 밝히지 않는다.  가장 조심해야 할 함정은 용어였다. Arup은 2022년 ExperienceLab을 열었는데 'VR 헤드셋이 필요 없다'는 점을 장점으로 내세운 26채널 스피커·6m 곡면 스크린 CAVE다. ZHA의 ZHVR은 2022년 서울 DDP에서 'NEW WORLDS: 혼합현실 체험'을 전시했지만 관람객이 착용한 것은 HTC VIVE Pro 2, 즉 VR이다. HOK는 "VR과 AR 도구를 오래 써왔다"고 언론에 말하면서도 자사 사이트에 AR 프로젝트 페이지를 한 건도 올리지 않았다. KPF Urban Interface는 애초에 AR이 아닌 도시 데이터 분석 조직이었고 kpfui.com은 지금 죽었다. 결론: 설계사무소의 '디지털 랩' 발표와 납품물 사이의 거리가 크고, AR은 설계 도구가 아니라 대외 소통 도구로만 살아남았으며, 전용 앱 설치를 요구한 시도는 전부 접혔다.


### Gensler × DignityMoves — 구글 Geospatial Creator / Adobe Aero 기반 주민 설명용 실규모 AR
| 항목 | 내용 |
| --- | --- |
| 주체 | 설계: Gensler(주거 모델). AR 운용 주체: DignityMoves(캘리포니아 소재 501(c)(3) 비영리, EIN 87-1111468, 본부 2406 Bush Street, San Francisco). 플랫폼: Google(ARCore·Geospatial Creator), Adobe(Aero). |
| 도시·연도 | 미국 캘리포니아. 대표 이미지는 샌프란시스코. DignityMoves는 Alameda·Oakland·San Jose(Cherry Ave, Via del Oro)·San Luis Obispo·Santa Barbara·Modesto·Watsonville 등 다수 지구를 운영 중이며, 어느 지구에 AR을 적용했는지는 특정되지 않았다. 구글 발표 2023-05-10, Gensler 기고 2023-08-14. |
| 증거 수준 | 실제 납품 — 단, 납품물은 '조경·건축 설계'가 아니라 '주민 소통용 AR 콘텐츠'다. 구글의 1차 발표문과 Gensler 자사 기술이 서로를 뒷받침한다. |
| AR 여부 | AR 맞음. ARCore Geospatial API와 구글 지도 플랫폼의 Photorealistic 3D Tiles를 써서 실세계 위치를 실시간 측위(VPS)하고 그 좌표에 3D 모델을 정합해 겹친다. 구글은 이를 'world-anchored'·'real time localization and real world augmentation'으로 기술한다. |
| 규모 | 대상지 규모·참여 인원·기간·예산 모두 공개되지 않음 |
| 기술 | ARCore Geospatial API + Google Maps Platform Photorealistic 3D Tiles + Adobe Aero(저작). Rooftop anchor 지원. Android·iOS 교차 지원, QR/링크 공유, 앱 다운로드 불필요. |
| 출처 | 구글 개발자 블로그(1차) https://developers.googleblog.com/2023/05/create-world-scale-augmented-reality-experiences-in-minutes-with-google-geospatial-creator.html · Gensler https://www.gensler.com/blog/how-augmented-reality-can-drive-more-engaged-communities · https://dignitymoves.org/ |

Gensler가 설계한 노숙인 임시지원주거(interim supportive housing) 모델을 실제 대상지 좌표에 실물 크기로 겹쳐 보여주고, 주민·이해관계자가 스마트폰으로 제안을 확인하도록 한 것이다. 구글이 2023년 5월 10일 Geospatial Creator를 발표할 때 게임·리테일·지역탐색 분야 출범 파트너 명단에 Gap·Mattel·싱가포르관광청·TAITO와 함께 Gensler를 넣고, 'Gensler는 Adobe Aero의 Geospatial Creator를 써서 주민들이 노숙인을 위한 새 도시 프로젝트가 어떤 모습일지 쉽게 상상하게 도왔다'고 명시했다. Gensler 자체 블로그(2023년 8월 14일, Greg Gallimore·Collin Peters 공동집필)는 'DignityMoves가 폭넓은 이해관계자 집단에 제안 설계안을 공유하기 위해 증강현실을 쓴다'고 적었고, 대표 이미지 캡션을 '샌프란시스코 DignityMoves를 위한 시각화'로 달았다. 건축도면과 평면도에 익숙하지 않은 참여자에게 복잡한 문서 대신 전신 스케일 체험을 주는 것이 목적이었다. Adobe Aero로 만든 체험은 QR 스캔이나 링크로 공유되며 전용 앱 설치가 필요 없다 — 한국 사례에서 실패 원인으로 학습된 바로 그 문턱을 처음부터 피한 구조다. 다만 어느 단지에 몇 명이 몇 차례 썼는지, 설계 결정이 이 때문에 바뀐 적이 있는지는 공개되지 않았다.

구글 플랫폼은 유지되고 있고 DignityMoves는 캘리포니아 전역에서 계속 사업을 확대하고 있다. 그러나 DignityMoves 공식 웹사이트(2026년 9월 확인)에는 AR이나 Gensler 협업에 관한 언급이 없다 — 즉 AR은 특정 시점의 소통 수단이었고 조직의 상시 도구로 정착한 흔적은 확인되지 않는다. 설계 변경 반영 여부도 확인 불가.

### Perkins+Will 'AX'(Augmented Experience) 증강현실 앱 — 2017년 출시, 현재 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | Perkins+Will(현 Perkins&Will). 디지털 실무 책임자 Nick Cameron. 발주처 없음 — 사내 개발·자사 홍보 겸용. |
| 도시·연도 | 미국(시카고 본사). AX 2017-10-16 발표, VX 2017-12-21 발표. |
| 증거 수준 | 실제 납품(무료 배포 앱) — 그러나 회사 스스로 '초기 프로토타입/베타'로 규정했다. |
| AR 여부 | AR 맞음(단, 탁상형). Apple ARKit/iOS 11의 증강현실 기능을 썼고 실세계 평면 위에 축소 모형을 배치한다. 대상지 좌표에 실규모로 정합하는 방식은 아니다. |
| 규모 | 공개되지 않음. 다운로드 수·개발비·투입 인원 모두 미공개. 콘텐츠는 초기 2건(상하이자연사박물관, River Beech Tower)으로 언급됨. |
| 기술 | iOS 11 ARKit. AR 지원 iPhone/iPad 필요. 헤드셋 불필요. App Store 무료 배포. |
| 출처 | Wayback 보존 원문 https://web.archive.org/web/20171023034130id_/http://perkinswill.com/news/perkinswill-launches-augmented-reality-app-ax · 살아있는 VX 보도자료 https://perkinswill.com/news/perkinswill-adds-new-virtual-reality-app-to-growing-portfolio-of-digital-experience-tools/ · 앱스토어 검색 https://itunes.apple.com/search?term=perkins+will&entity=software (2026-09-30) |

설계사무소가 자기 이름으로 낸 AR 앱 중 가장 이른 사례에 속한다. 2017년 10월 16일 보도자료로 '증강현실 앱 AX 출시'를 발표했다. 회사는 이를 '초기 프로토타입'이라 못박고, '궁극적으로 설계자가 혼합된 실세계·가상 환경에서 자기 모델과 상호작용하게 할 것'이라고 썼다. 베타 단계 기능은 Perkins+Will이 설계한 공간을 3D 증강현실로 둘러보는 것 — 상하이자연사박물관이나 River Beech Tower의 축소 모형을 자기 거실·사무실·동네에 놓고 보고 소셜미디어로 공유하는 방식이었다. 후속 베타에서 매싱·유리·개구부 같은 설계 특성을 바꿔보는 도구를 넣겠다고 했다. 디지털 실무 책임자 Nick Cameron은 '이 새 기술의 가능성을 탐색하고 그 과정에서 재미도 보고 싶었다. AR을 둘러싼 지금의 흥분에 빨리 편승하고 싶어서 이번 첫 배포는 가능한 것의 표면만 긁었다'고 말했다. 두 달 뒤인 12월 21일 회사는 VR 앱 'VX'를 내놓으며 AX를 '두 달 전 베타 출시된 증강현실 앱'으로 회고했다. 중요한 점: 대상은 건물이고 탁상형 축소 모형이었다. 옥외 공간을 실제 대상지에 1:1로 정합한 것이 아니다.

접혔다. 2026년 9월 30일 애플 앱스토어 검색 API로 확인한 결과 'AX'도 'VX'도 Perkins&Will 명의 앱이 존재하지 않는다. 더 나아가 AX 출시 보도자료 페이지 자체가 자사 웹사이트에서 사라졌다(Wayback에만 남아 있다) — 반면 두 달 뒤의 VR 앱 VX 보도자료는 지금도 살아 있다. 즉 AR 쪽만 선택적으로 지워졌다. 회사가 종료 사유를 밝힌 기록은 찾지 못했다. 이후 회사의 공개 관심은 메타버스로 이동했다('Get a feel for life in the metaverse', 'The metaverse is coming').

### Foster + Partners ARD — 사내 협업 설계도구 'Glaucon'
| 항목 | 내용 |
| --- | --- |
| 주체 | Foster + Partners, Applied Research + Development(ARD) 그룹. 런던 본사. |
| 도시·연도 | 영국 런던. 연도 미상 — Wayback 스냅샷 기준 2022~2024년 사이에 페이지가 존재했다. |
| 증거 수준 | 사내 연구·도구(자사 기술). 납품물 아님. 외부 검증 자료 없음. |
| AR 여부 | 부분적. AR이 네 가지 출력 모드 중 하나로 명시되어 있으나, 실세계 정합 방식·기기·적용 사례가 전혀 공개되지 않아 '실세계에 겹쳤는지'를 검증할 수 없다. 함께 소개된 Sandbox VR은 명확히 VR이다. |
| 규모 | 공개되지 않음 |
| 기술 | 미공개. VR·AR·모바일·웹 다중 출력, 사실적 렌더링 환경, 사내 설계·시각화 워크플로 연동이라는 서술만 있음. |
| 출처 | https://web.archive.org/web/2024id_/https://www.fosterandpartners.com/expertise/applied-research-development/experience-and-interaction/ · 항목 목록 Wayback CDX(fosterandpartners.com/expertise/applied-research-development*) · 참고 https://aecmag.com/sustainability/cyclops-from-foster-partners-environmental-analysis/ |

Foster + Partners의 Applied Research + Development(ARD)가 개발한 협업 디지털 설계 도구다. 회사 설명은 이렇다. 'Glaucon은 ARD가 개발한 협업 디지털 설계 도구로, 여러 사용자가 VR·AR·모바일 또는 웹으로 경험할 수 있는 사실적 가상 환경에서 함께 작업하게 한다. 우리의 설계·시각화 워크플로와 통합되어, 어디에 있든 팀이 공유된 3D 환경에 들어가 설계 검토, 고객 프레젠테이션, 또는 실제 설계 작업 협업을 할 수 있다.' 같은 카테고리('Experience and interaction')에 'Sandbox VR'과 'XR history'가 함께 놓여 있다. Sandbox VR은 헤드마운트 디스플레이 전용 제스처로 모델을 잡고 손을 벌려 스케일을 바꾸는 방식이며, '다른 VR 이동 기법에서 흔한 멀미를 거의 완전히 피했다'고 적어놓았다. XR history 항목은 'ARD 구성원들은 20년 넘게 XR 시스템을 연구·구현해 왔다'고 주장한다. 다만 개별 페이지(glaucon, sandbox-vr, xr-history)에는 본문이 사실상 없고, 상위 카테고리 페이지의 요약문이 공개 정보의 전부다. 적용 프로젝트명·연도·사용 기기·정합 방식은 어디에도 없다.

확인 불가. Foster + Partners 웹사이트는 자바스크립트 렌더링이라 직접 본문 취득이 안 되고 Wayback 보존본에도 개별 항목 본문이 없다. ARD가 최근 공개적으로 내세우는 도구는 AR이 아니라 환경분석 도구 'Cyclops'(2025)와 AI 쪽이다.

### Gensler LA 대중교통 AR 플랫폼 — 개념 영상에서 멈춘 사례
| 항목 | 내용 |
| --- | --- |
| 주체 | 주도: Gensler(Stephanie Truong). 참여·의견제공: City of Los Angeles, LADOT, FAST, Metro OEI, The Bloc, CivicConnect. 발주처 없음. |
| 도시·연도 | 미국 로스앤젤레스. 대상지: The Bloc(복합시설)과 7th Street 지하철역. 2020년 11월 17일 공개. |
| 증거 수준 | 개념영상. 자사 블로그가 촬영 사실을 직접 서술한다. |
| AR 여부 | 설계 의도는 AR(실세계 역·상업시설에 정합된 길찾기·안내 레이어). 그러나 실제로 만들어진 것은 AR 인터페이스를 현장 영상 위에 합성한 시각화다. 실세계 정합이 작동한 증거는 없다. |
| 규모 | 비공개. 참여 기관 6곳 이상, 기능 6개. 예산·기간·인원 미공개. |
| 기술 | 미공개. 기기·SDK·정합 방식 언급 없음. '디지털 플랫폼'과 UI 설계 수준에 머문다. |
| 출처 | https://www.gensler.com/blog/integrating-mixed-augmented-reality-with-transit-hubs · 앱스토어 확인 https://itunes.apple.com/search?term=Gensler&entity=software |

로스앤젤레스 대중교통 이용 경험을 AR로 개선하는 구상이다. Gensler(Stephanie Truong 집필, 2020년 11월 17일)는 먼저 LA시, LADOT, FAST, Metro OEI, 복합시설 The Bloc, CivicConnect 등과 브레인스토밍·비저닝 세션을 열어 이용자 유형·현재 여정·통점·기회를 수집했다. 그 다음 The Bloc과 7th Street 지하철역에 통합되는 AR 플랫폼의 사용자 인터페이스를 설계했다. 핵심 여섯 기능을 뽑았다 — 여정계획·발권·교통정보, 이용자를 맞이하고 앱 기능을 안내하는 'AR 컨시어지', 길찾기와 행사 알림, 실시간 번역, 탑승 포인트를 저장하는 가상 아바타, 승객 간 소셜 플랫폼. 그리고 결정적인 문장이 나온다. '기능을 다듬은 뒤, 우리는 개념을 더 잘 보여주기 위해 The Bloc에서 우리 AR 인터페이스의 시각화를 촬영했다.' 즉 산출물은 작동하는 AR 시스템이 아니라 현장에서 찍은 시연 영상이다. 글은 '공공·민간 기관이 자기 자원을 어떻게 활용해 늘어나는 AR 통합 수요에 대응할지 교육받아야 한다'는 권고로 끝난다. 발주처가 아니라 Gensler가 주도한 자체 기획이라는 뜻이다.

접혔다고 보아야 한다. LA Metro가 이 플랫폼을 채택했다는 기록을 찾지 못했고, Gensler 명의로 앱스토어에 존재하는 앱은 'Gensler Meetings' 하나뿐이다(2026-09-30 확인). 글이 인용한 'AR 매출 2023년 274억 달러 전망'(2018년 19.6억 달러 대비)도 당시 업계 낙관을 그대로 옮긴 수치다.

### Gensler × Knight Foundation × Urban Periscope — 산호세 기후데이터 AR 렌즈
| 항목 | 내용 |
| --- | --- |
| 주체 | Knight Foundation(자금), Gensler(설계), Urban Periscope(구현). 각자의 정확한 역할 분담은 불명. |
| 도시·연도 | 미국 캘리포니아 산호세(시범 도시). 연도 미상 — Gensler 기고는 2023년 8월 14일. |
| 증거 수준 | 설계사무소 자사 서술 1건뿐. 1차 자료(재단 보조금 문서, 프로젝트 문서, 학회 발표) 확인 실패. 증거 수준을 '연구 프로토타입' 이하로 보아야 한다. |
| AR 여부 | 서술상 AR(도시 시설물 위에 사람 눈높이로 데이터 중첩). 그러나 기기·정합 방식이 전혀 공개되지 않아 독립 검증 불가. |
| 규모 | 전부 미공개 |
| 기술 | 'AR 렌즈' 외 정보 없음 |
| 출처 | https://www.gensler.com/blog/how-augmented-reality-can-drive-more-engaged-communities (유일 출처) · 도메인 확인 2026-09-30 |

Gensler 기고문에 따르면 'Knight Foundation이 Gensler와 협력해 Urban Periscope와 함께 증강현실 체험을 만들었고, 시민이 형평성과 회복력을 높이는 데이터를 이해하고 공유하도록 돕는다'. 캘리포니아 산호세를 시범 도시로 삼아 'AR 렌즈 도구가 실행 가능한 기후 데이터를 사람 눈높이 스케일로 도시 시설물 위에 겹친다'고 설명한다. 문제의식은 명확하다 — 도시의 자전거 공유, 도시 정원, 보행로 같은 자원 데이터가 접근하기 어려운 데이터베이스나 웹사이트에 갇혀 있어 시민이 알지 못한다는 것. 그래서 건축 도면을 단순화하는 데 쓰는 AR을 시민 데이터 민주화에도 쓴다는 논리다. 조경·공원 자원을 AR로 드러낸다는 점에서 이 축에서 가장 조경에 가까운 구상이지만, 확인 가능한 정보가 이 단락 하나뿐이다. urbanperiscope.com/.org 도메인은 2026년 9월 현재 응답하지 않으며, Knight Foundation 사이트 검색에서도 'Urban Periscope' 관련 게시물을 찾지 못했다.

확인 불가, 소멸 의심. urbanperiscope.com·urbanperiscope.org 모두 DNS 응답 없음(2026-09-30). Knight Foundation 웹사이트 검색에도 관련 게시물 없음. 결과물이 지금 접근 가능하다는 증거를 찾지 못했다.

### West 8 — 2016년 HoloLens 글, 이후 삭제
| 항목 | 내용 |
| --- | --- |
| 주체 | West 8 Urban Design & Landscape Architecture(네덜란드 로테르담, 대표 Adriaan Geuze) |
| 도시·연도 | 네덜란드. 2016년 1월 28일 발행. |
| 증거 수준 | 판정 불가 — 본문 소멸. 확인된 것은 URL과 발행일뿐이다. |
| AR 여부 | AR 기기(Microsoft HoloLens, 광학투과형 헤드마운트 디스플레이)에 관한 글인 것은 제목으로 확실하다. 다만 실제로 프로젝트에 정합해 써 본 것인지, 단순 체험기인지 판단할 근거가 없다. |
| 규모 | 알 수 없음 |
| 기술 | Microsoft HoloLens(제목 기준) |
| 출처 | Wayback CDX 색인 http://web.archive.org/cdx/search/cdx?url=west8.com&matchType=domain&filter=original:.*(augmented\|hololens).* → http://www.west8.com/index.php/2016/01/28/kijken-door-een-microsofts-hololens/ · 자사 검색 API https://www.west8.com/wp-json/wp/v2/search?search=HoloLens (0건) |

West 8(로테르담 기반 도시설계·조경설계사무소)은 2016년 1월 28일 자사 뉴스에 네덜란드어 제목 'Kijken door een Microsoft's HoloLens'(마이크로소프트 홀로렌즈로 들여다보기)라는 글을 올렸다. 마이크로소프트가 HoloLens 개발자 에디션을 발표하기 두 달 전, 조경사무소가 이 기기를 공개적으로 언급한 매우 이른 기록이다. 그러나 본문을 복구할 수 없었다. 현재 West 8 웹사이트에서 'HoloLens'·'Microsoft'·'augmented'로 검색하면 모두 0건이고, Wayback Machine이 이 URL에 대해 보유한 스냅샷은 2020년 7월과 9월 세 건뿐이며 그때 이미 본문이 사라진 껍데기(리다이렉트 스텁)였다. 2016년 2~3월 West 8 홈페이지·뉴스 목록 스냅샷에서도 'HoloLens' 문자열이 나오지 않는다. 즉 URL 흔적만 남고 내용은 소멸했다. 이 축에서 조경설계사무소가 AR 하드웨어를 언급한 유일한 자체 기록이 바로 지워진 글이라는 사실 자체가 결과다.

사라졌다. 자사 사이트에서 삭제되었고 아카이브에도 본문이 남지 않았다. 삭제 시점·사유 모두 불명. 그 뒤 West 8 사이트에는 AR 관련 게시물이 단 한 건도 없다('augmented' 검색 0건, 2026-09-30).

### Sasaki — 'augmented' 0건, VR만 두 편 (2017·2018)
| 항목 | 내용 |
| --- | --- |
| 주체 | Sasaki Associates(미국 매사추세츠 워터타운). TRG(Technical Resource Group) + Sasaki Strategies. Ken Goulding(프린시펄, Data and Design Tools 디렉터), Colin Booth. |
| 도시·연도 | 미국. Q&A 2017-08-21, 'Getting Real' 2018. |
| 증거 수준 | 사내 연구·홍보. 프로젝트 적용은 VR 설계검토 수준. |
| AR 여부 | 아님. 가상현실(헤드셋 기반 몰입)이다. AR은 개념적으로만 언급된다. |
| 규모 | VR 헤드셋 '여러 대', VR 전담 인턴 1명. 그 이상 미공개. |
| 기술 | VR 헤드셋(기종 미공개). 소프트웨어 미공개. 글은 Facebook·Google·HTC의 VR 투자를 배경으로만 언급. |
| 출처 | https://www.sasaki.com/voices/qa-better-design-through-virtual-reality/ · https://www.sasaki.com/voices/getting-real-about-virtual-reality/ · 자사 검색 API https://www.sasaki.com/wp-json/wp/v2/search?search=augmented (0건) · Wayback CDX(sasakistrategies.com) |

Sasaki는 이 축의 조경사무소 중 디지털 도구 담론이 가장 두꺼운 곳이지만, 자사 웹사이트 전체 검색에서 'augmented'는 0건, 'HoloLens' 0건, 'XR' 0건이다. 남아 있는 것은 가상현실 글 두 편이다. 2017년 8월 21일 'Q&A: Better Design through Virtual Reality'는 사내 연구 조직 TRG(Technical Resource Group)와 도구 개발 조직 'Sasaki Strategies'의 공동 작업으로, Sasaki Strategies 공동디렉터·프린시펄 Ken Goulding과 R&D 프로젝트 매니저 Colin Booth를 인터뷰했다. 당시 활동 내용은 'VR 헤드셋 여러 대 구입'과 'VR 전담 인턴 채용' 수준이었다. 2018년 'Getting Real About Virtual Reality'는 Purdue 대학교 신앙기반 기숙사의 채플과 Colby College 아이스하키 경기장을 사례로 들었다 — 둘 다 실내 건축이다. 글은 VR과 AR을 병렬 기술로 언급하지만('whether it is VR or AR'), AR 적용 사례는 제시하지 않는다. 오히려 경계가 기록되어 있다. '기술의 낭만이 아니다. 설계자로서 우리의 직관을 확인하기 위해 VR을 쓰는 것이다.' 그리고 VR이 설계에 덧붙는 시간 낭비로 인식된다는 점, 노출 덕트 같은 설비가 드러나 고객이 불편해한다는 점을 문제로 꼽았다.

'Sasaki Strategies'라는 이름의 별도 웹사이트 sasakistrategies.com은 2011년 개설되어 파노라마 투어(panos/MC-PANO-TOUR)를 호스팅했고, 2024년 아카이브 기록에서는 무관한 외부 도메인 파라미터가 붙은 스팸 URL이 대량으로 관측된다 — 도메인이 방치·탈취된 상태로 보인다. 현재 sasakistrategies.com·strategies.sasaki.com 모두 응답하지 않는다(2026-09-30). Sasaki의 도구 조직은 현재 sasaki.com 안의 'Data and Design Tools'로 흡수된 것으로 보인다.

### Sasaki × Virginia Tech 'Cyclorama' — 360도 곡면 스크린 공동 몰입 프레젠테이션
| 항목 | 내용 |
| --- | --- |
| 주체 | Sasaki(프린시펄 Greg Havens AIA·AICP, 프린시펄 겸 Data and Design Tools 디렉터 Ken Goulding). 발주처: Virginia Polytechnic Institute and State University. 시설: VT의 Cyclorama. |
| 도시·연도 | 미국 버지니아주 블랙스버그, 버지니아공대 캠퍼스. 2017년 가을(글 발행 2017-11-06). |
| 증거 수준 | 실제 납품(클라이언트 발표에 투입). 자사 기록. |
| AR 여부 | 아님. 실세계에 겹친 것이 아니라 실내 곡면 스크린에 가상 환경을 투사한 공유 몰입 환경이다. 흔히 CAVE 계열로 분류된다. |
| 규모 | 스크린 16ft × 40ft, 360도 랩어라운드. 현장 참여 관리자 30명. 나머지 구성원은 라이브스트림. 계획 기간 30년. |
| 기술 | VT 보유 Cyclorama(360도 곡면 투사 시설) + Sasaki가 이 발표를 위해 개발한 맞춤 소프트웨어(상세 미공개). |
| 출처 | https://www.sasaki.com/voices/fully-immersive-presentations-at-vt-2/ · https://www.sasaki.com/voices/fully-immersive-presentations-at-vt/ |

2017년 가을, Sasaki 팀은 버지니아공대 캠퍼스에서 향후 30년 캠퍼스 계획을 발표했다. 발표 형식이 특이했다. 16피트 × 40피트, 360도 둘러싸는 곡면 스크린('Cyclorama') 안에서, 관리자 30명을 한 공간에 들여놓고 미래를 함께 걸어보게 했다. 나머지 구성원에게는 라이브 스트리밍으로 개방했다. 프린시펄 Greg Havens(AIA, AICP)는 1992~1993년 같은 대학 계획을 컬러 레이저 프린터로 출력해 발표했던 경험과 이번을 대비시켰다. 이 발표용 기술 소프트웨어의 리드 개발자이자 Data and Design Tools 디렉터인 프린시펄 Ken Goulding의 말이 핵심이다. '이 실험은 경험이 공유될 때 몰입 환경이 갖는 힘을 보여줬다. 오늘날 가상현실의 한계는 그것이 거의 언제나 혼자 하는 경험이라는 점이다. 당신만 보고 상호작용한다. Cyclorama에서 우리는 서른 명을 한 공간에 들여놓고 실시간 대화에 참여하게 하는, 완전 몰입형 공유 경험을 시뮬레이션할 기회를 얻었다.' 즉 이들은 헤드셋 VR의 사회적 한계를 진단하고 의도적으로 다른 길을 갔다. 조경·캠퍼스 계획이라는 옥외 공간 대상이었고, 실제 클라이언트 의사결정 자리에 투입된 도구였다.

일회성 발표를 위한 '하이퍼 커스텀' 접근이었다고 자사가 기술했다. 상시 도구로 제품화되었다는 기록은 없다. 다만 '공유 몰입'이 헤드셋 단독 VR보다 설계 협의에 낫다는 진단은 이후 Arup ExperienceLab(2022)과 같은 방향이다.

### SWA Group XL Lab — 'Immersive Environments' 몰입기술 평가 연구
| 항목 | 내용 |
| --- | --- |
| 주체 | SWA Group, XL Lab. 공동연구책임자 Anya Domlesky, Emily Schlickman. 자금: SWA Patrick T. Curran Fellowship. |
| 도시·연도 | 미국. 연도 미확정 — Wayback이 이 페이지를 처음 보존한 시점이 2019년 8월 25일이므로 2018~2019년으로 추정된다. SWA 공식 펠로십 수상 목록에는 'Immersive Environments'라는 제목이 없고, 가장 가까운 항목은 2016년 George Kutnar의 'LArch VIS'(모션그래픽과 가상현실을 개념설계에 도입하는 방법 실험)다. |
| 증거 수준 | 연구 프로토타입(사내 펠로십 연구). 오픈소스로 공개했다고 밝힘. |
| AR 여부 | 부분적. 나열된 네 기술 중 '혼합현실(mixed reality)' 하나가 AR 계열에 걸치지만, 어떤 기기로 실세계에 어떻게 정합했는지 서술이 없다. 나머지 셋(VR·구면 파노라마·360도 영상)은 AR이 아니다. |
| 규모 | 미공개. 데모 데이 1회, 외부 행사 1회, 인터뷰 다수라는 서술만 있음. 예산·기간·인원 미공개. |
| 기술 | '하드웨어와 소프트웨어를 테스트했다'는 서술만 있고 기종·SDK는 공개되지 않음. |
| 출처 | https://www.swagroup.com/idea/immersive-environments/ · 펠로십 목록 https://www.swagroup.com/idea/fellowships/ · 자사 검색 https://www.swagroup.com/wp-json/wp/v2/search?search=augmented · 첫 아카이브 시점 Wayback CDX(swagroup.com/idea/immersive-environments/) |

SWA의 연구·혁신 조직 XL Lab이 수행한 시각화·시뮬레이션 연구다. 자사 설명은 이렇다. '이 시각화·시뮬레이션 프로젝트는 부상하는 "몰입" 기술 — 가상현실, 혼합현실, 구면 파노라마, 360도 영상 — 을 실험하여 설계·계획 과정에서의 현재 강점, 한계, 기회를 찾아냈다. 접근은 비판적·평가적이었으며, 이 새 도구들이 지금 가장 잘 쓰일 곳과 가까운 미래에 AEC 산업에서 맡을 역할을 이해하려는 의도였다.' 수행 내용은 하드웨어·소프트웨어 테스트, 설계자·계획가를 위한 데모 데이 개최, 고객과 이해관계자를 위한 외부 행사 개최, 업계 전문가 및 제품 엔지니어 인터뷰였다. 결과는 '조경설계와 인접 분야의 실험을 가속하기 위해 오픈소스 자원으로 공유'되었다. 공동연구책임자는 XL Lab의 Anya Domlesky와 Emily Schlickman이다. 자금원은 SWA의 Patrick T. Curran Fellowship. 주목할 점: 대상지도, 프로젝트도, 고객도 특정되지 않는다. 설계 납품이 아니라 도구 평가 연구다. 그리고 목록에서 AR은 독립 항목으로 등장하지 않는다 — '혼합현실'이 들어갔을 뿐이다.

오픈소스 자원의 현재 접근 경로를 확인하지 못했다. SWA 웹사이트 검색에서 'augmented'는 단 1건 걸리는데, 그것은 2024년 Curran Fellowship 행사 기록에서 'digital twins and augmented experiences'라는 수사적 표현으로 쓰인 것이고 AR 기술 내용이 아니다. XL Lab의 이후 공개 연구 방향은 산불(Playbook for the Pyrocene), 열, 탄소, 생물다양성, 감각도시(Urban Sensorium), 생성형 AI 식재계획 도구로 옮겨갔다 — AR은 후속이 없다.

### Zaha Hadid Architects ZHVR Group 'NEW WORLDS' — '혼합현실'로 홍보된 VR (서울 DDP)
| 항목 | 내용 |
| --- | --- |
| 주체 | Zaha Hadid Architects, ZHVR(Zaha Hadid Virtual Reality) Group. 파트너: L-Acoustics Creations, 아티스트 Halina Rice(런던 기반 전자음악·AV 작가), 디자이너 Jakob Macdonald. 전시 주최: DDP 디자인뮤지엄. |
| 도시·연도 | 대한민국 서울 DDP 디자인뮤지엄. 2022년 6월(발표 2022-06-16). LOOP 원형은 2019년 8월 발표. |
| 증거 수준 | 전시·시연. 공공 미술관 전시에 실제로 설치되었으나 설계 납품물이 아니다. |
| AR 여부 | 아님. 관람객이 착용한 기기는 HTC VIVE Pro 2로, 완전 몰입형 VR이다. 자사 서술도 '가상 공간으로 옮겨진다(transported into a virtual space)'고 명시한다. 'mixed reality'라는 명칭은 마케팅 용어일 뿐 실세계 정합이 없다. |
| 규모 | LOOP는 1인용 개인 오디토리엄, 24개 독립 오디오 채널. 관람객 수·예산·기간 미공개. |
| 기술 | HTC VIVE Pro 2 VR 헤드셋 + L-Acoustics L-ISA Immersive Hyperreal Sound 공간음향. ZHVR이 LOOP의 곡면 기하를 설계. |
| 출처 | Wayback 보존 원문 https://web.archive.org/web/2023id_/https://www.zaha-hadid.com/2022/06/16/new-worlds-a-mixed-reality-experience-featuring-loop-immersive-sound-lounge/ · https://www.zaha-hadid.com/2019/08/15/loop-immersive-sound-lounge-by-zhvr-for-l-acoustics-creations/ · https://www.zaha-hadid.com/2019/06/04/zhvr-launch-new-website/ · 관련 https://aecmag.com/vr-mr/patrik-schumacher-zha-the-metaverse-o |

2022년 6월 16일 ZHA는 '혼합현실 체험 NEW WORLDS'를 발표했다. 장소는 서울 DDP 디자인뮤지엄의 'Meta-Horizons: The Future Now' 전시다. 원래는 ZHVR(Zaha Hadid Virtual Reality) 그룹이 'LOOP 몰입형 사운드 라운지' 제품 테스트·개발을 위해 만든 설계 시뮬레이션이었고, 이 전시를 위해 ZHVR이 L-Acoustics Creations와 아티스트 Halina Rice와 함께 다듬고 확장했다. 그런데 자사 설명의 다음 문장이 결정적이다. '관람객은 HTC의 VIVE Pro 2 헤드셋으로 가상 공간에 옮겨져, Halina Rice의 몰입형 사운드스케이프를 경험한다.' VIVE Pro 2는 시야 차단형 VR 헤드셋이다. 실세계에 아무것도 겹치지 않는다. LOOP 자체는 2019년 시작된 L-Acoustics Creations와 ZHVR의 첫 협업으로, 24개 독립 채널로 L-ISA 공간음향을 재생하는 1인용 개인 오디토리엄이다. 시각 요소는 디자이너 Jakob Macdonald가 참여했다. 이 사례는 이 조사에서 가장 중요한 경고다 — 설계사무소의 '혼합현실' 발표를 AR로 받아들이면 안 된다.

ZHVR의 계보는 AR이 아니라 VR·메타버스로 계속 갔다. 2018년 3월 몬트리올 국제예술영화제(Le FIFA)에 ZHVR 영상 출품, 2019년 6월 ZHVR 자체 웹사이트 개설, 2019년 8월 LOOP 발표, 2022년 NEW WORLDS, 2023년 5월 시카고 싱크탱크 ArchAgenda와 함께 베네치아 건축비엔날레 병행행사로 'METROTOPIA' 메타버스 출범. 어느 단계에도 실세계 정합 AR은 없다. zaha-hadid.com은 zha.com으로 이전했고 구 도메인은 봇 접근을 차단한다.

### Arup ExperienceLab — 'VR 헤드셋이 필요 없다'를 장점으로 내세운 CAVE (AR 아님)
| 항목 | 내용 |
| --- | --- |
| 주체 | Arup(글로벌 엔지니어링·컨설팅). Ian Knowles(음향·AV·극장 컨설팅 디렉터). 발표: Lucy Chakaodza(UKIMEA 미디어, 런던). |
| 도시·연도 | 영국 런던. 2022년 3월 30일 발표. |
| 증거 수준 | 실제 납품(상시 운영 시설). 자사 발표. |
| AR 여부 | 아님. 실내 곡면 스크린 투사형 공유 몰입 시설(CAVE 계열)이다. 실세계에 겹치지 않는다. 오히려 헤드셋 착용 자체를 단점으로 규정하고 반대 방향을 택했다. |
| 규모 | 스피커 26대, 6m 곡면 스크린. 건설비·이용 건수 미공개. |
| 기술 | 헤드트래킹 스테레오 투사(입체영상), 캘리브레이션 몰입 음향, 데이터 시각화. VR 헤드셋 미사용. |
| 출처 | https://www.arup.com/news/arup-brings-design-to-life-with-industry-first-immersive-facility/ · https://www.arup.com/services/digital-solutions/soundlab/ · 사이트맵 전수 검색 https://www.arup.com/sitemap.xml (augmented/hololens/mixed reality 0건) |

2022년 3월 30일 Arup은 런던에 ExperienceLab을 열었다고 발표했다. 설계자·고객·이해관계자가 계획안의 가상 재현 안으로 들어가 돌아다니며, 자기 결정이 환경·공간·건물의 경험에 어떤 영향을 줄지 실행 전에 이해하게 하는 시설이다. 구성은 스피커 26대에 둘러싸이고 6미터 곡면 스크린을 마주하는 방이다. 헤드트래킹 스테레오 투사가 시야를 채우고 이용자 움직임에 반응하며, 정확한 피사계심도와 원근, 그리고 콘서트홀 실내음향부터 교통 소음까지 재현하는 캘리브레이션된 몰입 음향을 결합한다. 결정적 문장은 이것이다. '이런 종류의 협업형 몰입 시설은 건조환경 및 여타 전문서비스 부문에서 유일하며, 고립시키는 VR 헤드셋의 필요를 없애고 집단이 공간 안에서 함께 작업하며 해법과 변경을 논의하게 한다.' 데이터 시각화 기능도 있어 차량 통행 변화를 지도화하는 식으로 프로젝트가 주변 지역에 미칠 영향을 보여준다. 도시·마스터플랜 차원에서 소음·대기오염 저감안을 검증하거나 공간 이용을 복잡한 데이터 분석 대신 눈으로 보게 하는 용도다. 음향·AV·극장 컨설팅 디렉터 Ian Knowles의 말: 'Arup ExperienceLab은 인간 경험을 통해 우리가 건조환경을 설계하고 계획하는 방식을 진정으로 개선할 수 있는 디지털 시설이다.'

주목할 것은 Arup 웹사이트 전체 사이트맵(약 60만 바이트)을 훑었을 때 AR 관련 페이지가 단 한 건도 없다는 점이다. 몰입 관련 항목은 ExperienceLab과 SoundLab(디지털 솔루션), 'virtual-reality-soundbooths' 프로젝트가 전부이고, 나머지는 전부 디지털 트윈(프라이부르크, 헤이그 시청사, 파시그강 플라스틱 등)이다. 세계 최대 규모 엔지니어링 컨설턴시가 공개한 AR 프로젝트가 0건이라는 사실이 이 축에서 가장 의미 있는 부재다.

### HOK — 'AR을 오래 써왔다'는 주장과 0건의 공개 AR 프로젝트
| 항목 | 내용 |
| --- | --- |
| 주체 | HOK. Brian Jencek(샌프란시스코 기반 계획 디렉터), Jess Bayuk(인테리어·VR). |
| 도시·연도 | 미국. AEC Magazine 기고 2022년 3월 29일. |
| 증거 수준 | 사내 홍보·언론 기고. 납품물 증거 없음. |
| AR 여부 | 판정 불가에 가깝다. AR 사용을 주장하지만 구체 프로젝트·기기·정합 방식을 제시하지 않았고, 제시된 예시(뉴욕시 모델링, 관람석 시야)는 모두 화면·헤드셋 기반 가상 시각화다. |
| 규모 | 미공개 |
| 기술 | Blender, Unreal Engine, Unity, Twinmotion(자사 언급). AR 관련 SDK·기기 언급 없음. |
| 출처 | https://aecmag.com/vr-mr/hok-navigating-the-metaverse-for-architects/ · 자사 검색 API https://www.hok.com/wp-json/wp/v2/search?search=augmented%20reality · https://www.hok.com/news/2020-05/hoks-jess-bayuk-on-how-virtual-reality-is-changing-interior-design/ |

HOK는 언론 기고에서 AR 사용을 주장한다. AEC Magazine에 실린 2022년 3월 29일 기고 'HOK: navigating the metaverse for architects'에서 이렇게 말한다. 'HOK는 경기장, 병원, 사무실, 연구소가 되었든 제안된 공간에 고객을 몰입시키기 위해 가상현실(VR)과 증강현실(AR) 도구를 오래 써 왔다. 이 도구들은 건물 성능을 시뮬레이션하고 여러 시나리오를 재생할 수 있다. 예를 들어 뉴욕시를 모델링해 인구가 1천만 명 늘고 해수면이 6피트 상승하면 어떤 모습이 될지 보여줄 수 있다.' 샌프란시스코 기반 계획 디렉터 Brian Jencek은 '건물, 캠퍼스, 도시 등 우리가 설계하는 모든 것은 메타 공간으로 태어난다. 우리는 그것을 그냥 3D 모델이라 부른다. 우리는 이미 게임 디자이너가 쓰는 도구 — Blender, Unreal Engine, Unity, Twinmotion — 를 써서 사실적인 가상 환경을 만든다'고 말한다. 그런데 자사 웹사이트 전수 검색에서 AR 프로젝트는 한 건도 나오지 않는다. 사이트맵에 남은 몰입 관련 항목은 전부 VR이거나 메타버스 담론이다 — 'HOK의 Jess Bayuk: 가상현실이 인테리어 디자인을 바꾸는 방식'(2020-05), '완벽한 시야 만들기: HOK 건축가들이 말하는 관람석 설계'(2023-06), '인류와 메타버스'(행사), 'Gen Z·AI·메타버스 시대의 오피스 디자인'(2023-02). 주장과 공개 실적 사이의 간극이 이 항목의 내용이다.

HOK 웹사이트의 WordPress 검색 API로 'augmented reality'를 조회하면 결과 8건이 모두 VR·메타버스·경기장 설계 기사이며 AR 전용 항목이 없다. Wayback CDX에서도 hok.com 도메인에 'augmented'를 포함하는 URL이 0건이다. AR은 HOK에서 담론 수준에 머물렀다고 보아야 한다.

### KPF Urban Interface (KPFui) — AR이 아닌 도시 데이터 분석, 그리고 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | Kohn Pedersen Fox(KPF), KPF Urban Interface(KPFui). Luc Wilson. |
| 도시·연도 | 미국 뉴욕. 2016년 3월 23일 출범(보도 2016-03-25, The Real Deal). |
| 증거 수준 | 실제 납품(설계 의사결정 지원 도구, 학회 발표 있음) — 다만 AR 사례가 아니다. |
| AR 여부 | 아님. 도시 데이터 분석·시나리오 시뮬레이션·3D 시각화다. 실세계 정합 중첩이 아니다. |
| 규모 | '39년의 경험'이라는 수사 외 규모 수치 미공개 |
| 기술 | 도시 데이터 분석, 시나리오 분석, 3D 시각화. 대학·정부기관 연구 협업. |
| 출처 | Wayback 보존 원문 https://web.archive.org/web/2019id_/http://www.kpf.com/current/news/kpf-launches-kpf-urban-interface · https://www.kpf.com/current/news/luc-wilson-discusses-kpfs-urban-interface-tools-with-architectural-record · https://www.kpf.com/current/news/kpf-urban-interface-participates-in-simaud-2019 · 현재 404 확인 https://www.kpf.com/urban-interface |

이 축의 원 질문에 '옥외 공간을 다룬 도시설계' 조직으로 KPF Urban Interface가 포함되었으므로 성격을 분명히 해둘 필요가 있다. KPFui는 AR 조직이 아니다. 2016년 3월 23일 Kohn Pedersen Fox가 출범시킨 도시 데이터 분석 자원이다. 자사 발표문은 '수년간의 사내 개발을 거쳐, KPF Urban Interface는 39년의 경험과 도시 데이터 분석의 최근 발전을 결합해 건물과 도시 설계에서 정보에 기반한 의사결정을 위한 자원을 만든다'고 썼다. 근거로 든 문제의식은 2050년까지 도시 인구가 두 배가 되는 상황에서 정책결정자·설계자·개발자가 직면할 복잡성이며, 대응 수단으로 든 것은 도시 데이터 수집, 시나리오 분석, 3D 시각화다. 대학 및 정부기관과의 연구 협업을 함께 언급했다. 리더는 Luc Wilson으로, 2019년 SimAUD(Symposium on Simulation for Architecture and Urban Design)에 참가하고 Architectural Record와 인터뷰했다. 즉 성격은 시뮬레이션·분석이며, 증강현실과는 계보가 다르다.

브랜드가 접혔다. kpf.com의 'urban-interface' 페이지는 현재 404이며, 별도 도메인 kpfui.com은 응답만 하고 내용이 없는 껍데기다(2026-09-30 확인). KPF는 현재 이 기능을 'Applied Technology'라는 분야명 아래에 두고 있다. KPFui 관련 뉴스 페이지들은 Wayback에만 남아 있다.

### Snøhetta — AR 0건, 방향은 생성형 설계와 디지털 보존
| 항목 | 내용 |
| --- | --- |
| 주체 | Snøhetta(노르웨이 오슬로·미국 뉴욕 등). 조경 부문: 파트너 Michelle Delk(2026년 펜실베이니아대 실무교수 임명). |
| 도시·연도 | 노르웨이/미국 등. 확인 시점 2026-09-30. |
| 증거 수준 | 부재의 확인. 자사 사이트 검색 + 사이트맵 전수 + Wayback 색인 세 경로 모두 0건. |
| AR 여부 | 아님 — AR 활동 자체가 확인되지 않음. |
| 규모 | 해당 없음 |
| 기술 | 생성형 설계, 창의기술(creative technology), 디지털 아카이브. AR 기술 스택 없음. |
| 출처 | 자사 검색 https://www.snohetta.com/search?q=augmented (0건) · https://www.snohetta.com/perspectives/harnessing-generative-design-and-creative-technology · https://www.snohetta.com/perspectives/digital-design-in-the-age-of-sustainability · Wayback CDX(snohetta.com, augmented/hololens 0건) |

Snøhetta는 조경(파트너 Michelle Delk가 조경 부문을 이끈다)과 건축을 함께 다루며 기술 담론도 활발하지만, 증강현실은 없다. 자사 사이트 검색에서 'augmented'는 결과 0건이다(검색어 자체만 에코된다). 사이트맵 전수 조회에서도 AR 항목이 없고, Wayback CDX에서 snohetta.com 도메인에 'augmented' 또는 'hololens'를 포함하는 URL이 0건이다. 대신 남아 있는 기술 관련 게시물은 'Digital design in the age of sustainability', 'Harnessing generative design and creative technology', 'Open Archive: 건축의 디지털 보존과 확산'이며, 달력 항목은 ProptTech 행사, 파사드 설계 강연, '미래에 대비하는 건축가: 기술·새 비즈니스 모델·변화하는 임차인 수요를 위한 설계' 같은 것들이다. 'Harnessing generative design and creative technology' 본문에도 'augmented'·'immersive'·'reality' 중 어느 단어도 나오지 않는다. 즉 Snøhetta의 기술 투자는 생성형 설계와 아카이브 디지털화에 있고, 실세계 정합 중첩은 관심 영역이 아니다.

해당 없음 — 시작된 적이 없다.

### James Corner Field Operations · Michael Van Valkenburgh Associates · Gustafson Porter+Bowman · Turenscape · MVRDV — AR 실적 0건 확인
| 항목 | 내용 |
| --- | --- |
| 주체 | James Corner Field Operations(뉴욕), Michael Van Valkenburgh Associates(뉴욕·케임브리지), Gustafson Porter+Bowman(런던), Turenscape/土人景观(베이징), MVRDV(로테르담) |
| 도시·연도 | 확인 시점 2026-09-30 |
| 증거 수준 | 부재의 확인. 확인 경로를 사무소별로 명시했다. |
| AR 여부 | 아님 — 다섯 곳 모두 AR 활동 미확인. |
| 규모 | 해당 없음 |
| 기술 | 해당 없음 |
| 출처 | Wayback CDX(fieldoperations.net / mvvainc.com / gp-b.com 각 도메인, filter=augmented\|hololens\|mixed-reality → 0건) · https://www.gp-b.com/search?q=augmented&format=json · https://www.turenscape.com/sitemap.xml · Wayback CDX(mvrdv.com, filter=reality\|virtual\|immersive\|metaverse\|hololens) |

이 다섯 곳은 각기 다른 경로로 확인했고 결과는 모두 동일하다. 증강현실 관련 공개 활동이 없다. (1) James Corner Field Operations(fieldoperations.net): Wayback CDX에서 도메인 전체에 'augmented'·'hololens'·'mixed-reality'를 포함하는 URL 0건. (2) Michael Van Valkenburgh Associates(mvvainc.com): 같은 조건 0건. 자사 사이트는 봇 접근을 403으로 차단한다. (3) Gustafson Porter+Bowman(gp-b.com): Squarespace 사이트 검색 API로 'augmented'를 조회한 결과 실질 결과 0건(페이지 제목에 검색어가 에코된 것뿐), Wayback CDX도 0건. (4) Turenscape(turenscape.com): 사이트맵 전수 조회 및 영문 사이트 검색 모두 AR 관련 0건. (5) MVRDV(mvrdv.com): 자체 사이트가 Angular 단일페이지 앱이라 서버 측 검색이 불가능하지만, Wayback CDX로 도메인 전체 URL을 'reality\|virtual\|immersive\|metaverse\|hololens' 조건으로 조회했을 때 걸리는 것은 코로나 시기 온라인 강연('virtual forum', 'virtual festival of facades') 뿐이고 AR·MR 프로젝트는 없다. 즉 이 축이 가정한 '조경·도시설계 사무소의 AR 활용'은 대부분의 곳에서 아예 존재하지 않았다.

해당 없음. 단, MVRDV는 사이트 구조상 검증 신뢰도가 다른 넷보다 낮다(아래 uncertain 참조).

### 구글 Geospatial Creator (2023) — 설계사무소가 AR을 쓸 수 있게 만든 플랫폼 전환점
| 항목 | 내용 |
| --- | --- |
| 주체 | Google(ARCore 팀, Google Maps Platform). 저작 도구 파트너: Unity, Adobe(Aero). |
| 도시·연도 | 미국. 2023년 5월 10일 발표. ARCore Geospatial API 지원 87개국 이상. |
| 증거 수준 | 실제 납품(상용 플랫폼). 구글 개발자 블로그 1차 자료. |
| AR 여부 | AR 맞음. 실시간 측위(VPS)로 실세계 좌표를 확정하고 그 위에 콘텐츠를 정합해 겹친다. 구글 스스로 'world-anchored', 'real time localization and real world augmentation'으로 규정한다. |
| 규모 | 안드로이드 기기 14억 대 대상. 지원 국가 87개국 이상. iOS 교차 지원. |
| 기술 | ARCore Geospatial API + Photorealistic 3D Tiles(Google Maps Platform) + Rooftop anchors. 저작: Unity / Adobe Aero. 배포: QR·링크(앱 설치 불필요). Android·iOS 양쪽 지원. |
| 출처 | https://developers.googleblog.com/2023/05/create-world-scale-augmented-reality-experiences-in-minutes-with-google-geospatial-creator.html |

설계사무소 사례를 읽을 때 배경으로 알아야 할 플랫폼 변화다. 2023년 5월 10일 구글은 Geospatial Creator를 발표했다(작성 Stevan Silva, 선임 제품매니저). 핵심은 진입 장벽을 무너뜨린 것이다. Unity 또는 Adobe Aero 안에서, 실세계 어디에 디지털 콘텐츠를 놓을지 구글 어스나 스트리트뷰처럼 눈으로 보며 배치하고, 몇 분 만에 세계 규모 AR을 만들어 배포한다. 기반은 ARCore와 Google Maps Platform의 Photorealistic 3D Tiles이며, 건물 지붕에 콘텐츠를 고정하는 'Rooftop anchor' 같은 기능이 추가되었다. ARCore Geospatial API의 지원 범위는 발표 시점 기준 87개국 이상에서 확장되었고 안드로이드 기기 14억 대를 대상으로 한다. 특히 중요한 것은 Adobe Aero로 만든 체험이 QR 코드 스캔이나 링크로 공유되며 앱 전체 다운로드가 필요 없다는 점이다 — 전용 앱 설치가 AR 공공사업의 반복된 실패 원인이었음을 생각하면 결정적 변화다. 구글이 밝힌 출범 파트너에는 Gap, Mattel, Global Street Art, 싱가포르관광청, Gensler, TAITO가 있다. 설계 분야에서 유일하게 이름을 올린 것이 Gensler다.

플랫폼은 유지되고 있으며, 설계·도시 분야에서 AR을 쓰려면 사내 개발 없이 이 위에 올리는 것이 현재의 표준 경로다. Perkins+Will이 2017년 자체 앱(AX)으로 시도해 실패한 것과, Gensler가 2023년 플랫폼에 올려 성공한 것의 차이가 여기에 있다.

#### 검증에서 잡힌 정정
- 구글 항목 '지원 87개국 이상': 조사가 든 1차 출처(구글 개발자 블로그 2023-05-10)는 "we have extended coverage of the ARCore Geospatial API **from 87 countries to over 100 countries**"라고 87을 '이전 수치'로 못 박는다. 구글 현행 문서(developers.google.com/ar/geospatial-creator/adobe-aero)는 Geospatial Creator 저작 기반인 Photorealistic 3D Tiles를 "**49 countries**"로 적는다. '87개국 이상'은 두 출처 모두와 불일치.
- '구글의 1차 발표문과 Gensler 자사 기술이 서로를 뒷받침한다'(오판): 구글 블로그는 DignityMoves를 전혀 언급하지 않고 AR 주체를 "**Gensler** used Geospatial Creator in Adobe Aero"로 적는다. Gensler 블로그는 주체를 DignityMoves로 적고 Adobe Aero를 언급하지 않는다. 상호 보강이 아니라 상호 충돌.
- 'AR 운용 주체: DignityMoves'(구글 1차 자료와 충돌): 구글 발표문은 AR 제작·운용 주체를 Gensler로 명시한다.
- '플랫폼: Google(ARCore·Geospatial Creator), **Adobe(Aero)**' — DignityMoves 사례에 Aero를 붙인 근거는 Gensler 블로그에 없다(Aero 0회 언급). Aero는 구글 블로그 쪽 서술에만 나온다.
- "납품물은 '조경·건축 설계'가 아니라 '주민 소통용 AR 콘텐츠'다": Gensler 자사 프로젝트 페이지 'DignityMoves Cherry Avenue'는 "DignityMoves **engaged Gensler to design** a trauma-informed tiny home village"(San Jose, 136 private rooms, 'Completed in under a year', 'Every 5-Year, 10+ Community Partnerships With DignityMoves')라 적고, 샌프란시스코 건도 "$1.7 million village of tiny prefab homes, **designed by Gensler**"로 기재돼 있다. 설계 납품이 실재한다.
- '어느 지구에 AR을 적용했는지는 특정되지 않았다': 조사가 유일 출처로 든 Gensler 블로그의 이미지 캡션이 "A visualization for DignityMoves, **San Francisco**"라고 두 번 적고 있고, Gensler 프로젝트 기록에는 샌프란시스코의 옛 주차장 부지 tiny-cabin 커뮤니티가 명기돼 있다. 또 조사가 나열한 지구 목록(Alameda·Oakland·San Jose×2·San Luis Obispo·Santa Barbara·Modesto·Watsonville)에 정작 샌프란시스코가 빠져 있다.
- KPF Urban Interface '브랜드가 접혔다 / kpfui.com은 껍데기': 1차 보도자료 본문이 명시한 공식 주소는 **ui.kpf.com**이며 2026-09-30 현재 HTTP 200, Tools·Research·Case Studies·Blog 메뉴와 2022~2024년 채용 공고가 실린 온전한 사이트다. 조사는 보도자료에 없는 kpf.com/urban-interface(404)와 무관한 주차 도메인 kpfui.com만 확인했다.
- KPF 1차 보도자료를 'Wayback 보존 원문'으로만 제시: https://www.kpf.com/current/news/kpf-launches-kpf-urban-interface 는 현재도 HTTP 200으로 살아 있다.
- Sasaki Cyclorama '스크린 16ft × 40ft, **360도 랩어라운드**': 같은 글이 뒤에서 "rendered in a full 360-degree format for display within the presentation customized for the **180-degree Cyclorama screen**"이라고 스스로 정정한다. 360도는 렌더 포맷, 스크린은 180도다.
- Sasaki Cyclorama "일회성 발표를 위한 하이퍼 커스텀": 같은 글 마지막 문단에 "Havens gave the immersive presentation **once again to the VT board of trustees just last week**"이라고 적혀 있다(최소 2회 실사용). 또 렌더링은 외부 파트너 Design Distill이 7개 뷰를 제작했다는 서술이 있는데 조사는 이를 누락했다.
- SWA '공식 펠로십 목록에 Immersive Environments가 없고 가장 가까운 항목은 2016년 George Kutnar의 LArch VIS다': 공식 목록에는 "**Anya Domlesky, SWA and Emily Schlickman, SWA 'XL: Experiments in Landscape and Urbanism' 2016**"이 있다 — Immersive Environments의 공동연구책임자 2인과 동일 조합이며 XL Lab 명칭의 출처다. Kutnar는 그 프로젝트 페이지의 'THANKS TO' 협력자 명단에 있는 사람이다.
- SWA '규모 미공개 / 데모 데이 1회·외부 행사 1회·인터뷰 다수라는 서술만': 페이지는 게재 산출물 4건(Planning Magazine "Using Your Illusion", Mark Magazine Issue 68, Landscape Architecture Magazine "Thinking Ahead", Landscape Architecture Frontiers)과 외부 협력자(SF Dept. of Planning, Autodesk, County of Santa Clara, IrisVR, ESRI, Google, Municipal Art Society/Maker Park, Golden Triangle BID)를 명시한다.
- ZHA 'AR 활동 없음 / ZHVR의 계보는 AR이 아니라 VR·메타버스로 계속 갔다': 조사가 인용한 그 Wayback 페이지 뉴스 목록에 2019-08-28 "'Today at Apple' Design Lab with Zaha Hadid Architects: **Architecture in AR**"이 있다. 요약 원문 "Explore augmented reality in the design process with Zaha Hadid Architects, as part of Apple's 'Future of the City' series… **Then view your creation in AR.**"
- ZHA '전시 주최: DDP 디자인뮤지엄': ZHA 자사 발표(2022-05-26)는 "Zaha Hadid Architects (ZHA) **in collaboration with** Dongdaemun Design Plaza (DDP) in Seoul, Korea **presents** 'Meta-Horizons: The Future Now'"라 적는다. 공동 주최이며, NEW WORLDS는 그 'Meta-Horizons' 전시 내 콘텐츠다(모전시명 누락).
- Snøhetta 'Michelle Delk(2026년 펜실베이니아대 실무교수 임명)': Penn Weitzman의 그녀 인물 페이지는 Wayback에 **2024-07-02**부터 보존돼 있고, 그 2024년 스냅샷에 이미 직함이 **'Laurie Olin Professor of Practice in Landscape Architecture'**로 적혀 있다. 2026년 임명이 아니다. 또 Snøhetta 자사 people 디렉터리(2026-09-30)에는 'Delk' 0건이고 snohetta.com/people/michelle-delk는 404, 목록상 파트너는 Alan Gordon·Elaine Molinar 2명뿐이다 — '파트너'라는 현재 직함은 Snøhetta 자사 사이트로 확인되지 않고 Penn 약력에만 있다.
- HOK 항목 인물 'Jess Bayuk(인테리어·VR)': 조사의 근거인 AEC Magazine 기고(2022-03-29)에 Bayuk는 등장하지 않는다. 그 기사에 인용된 HOK 인물은 Brian Jencek("director of planning, HOK") 외 Sun·Schleusner·Weatherhead·Singaby다. Bayuk는 별개의 2020-05 HOK 자사 뉴스에만 나온다 — 두 출처를 한 항목에 섞었다.
- Foster + Partners 'Wayback 보존본에도 개별 항목 본문이 없다': 조사가 인용한 그 Wayback URL을 그대로 받으면 Sandbox VR과 Glaucon 본문이 모두 들어 있다("Glaucon is a collaborative digital design tool developed by ARD… experienced in VR, AR, mobile or through the web"). 라이브 페이지 실패 원인도 자바스크립트 렌더링이 아니라 HTTP 403(봇 차단)이다. 또 원문은 Glaucon을 "client presentation"에도 쓴다고 적어 '사내 협업 도구'로만 한정하기 어렵다.
- Perkins+Will AX 'Apple ARKit/iOS 11의 증강현실 기능을 썼고': 보도자료 원문은 "the augmented reality features in **Apple's latest operating system**… an AR-capable iPad or iPhone running **iOS 11**"이라고만 적고 ARKit이라는 명칭을 쓰지 않는다(출처에 없는 명칭).
- Arup '웹사이트 전체 사이트맵을 훑었을 때 AR 관련 페이지가 단 한 건도 없다': arup.com/sitemap.xml(604,814바이트)은 URL 목록만 담고 페이지 본문을 담지 않는다. URL 슬러그 스캔으로 본문 수준의 부재를 단정할 수 없다(방법론 결함). 단 슬러그상 immersive 계열 URL이 ExperienceLab 뉴스 1건뿐이라는 관찰 자체는 재현됨.
- 구글 Geospatial Creator 항목: '지원 국가 87개국 이상'·'ARCore Geospatial API 지원 87개국 이상'은 폐기된 수치다. 인용한 1차 자료 원문은 'we have extended coverage of the ARCore Geospatial API from 87 countries to OVER 100 COUNTRIES'라고 적는다. 87은 발표 시점에 이미 지나간 이전 값이고, 2023-05-10 기준 값은 100개국 이상이다. (1.4 billion Android devices는 정확.)
- Gensler×DignityMoves 항목: 'AR 운용 주체: DignityMoves / 설계: Gensler(주거 모델)'라는 역할 배분은 1차 자료와 반대다. 구글 개발자 블로그에는 'Gensler helps communities visualize new urban projects — Gensler used Geospatial Creator in Adobe Aero to help communities easily envision what new city projects might look like for the unhoused'라는 독립 절이 있고, DignityMoves라는 이름은 구글 발표문 전체에 0회 등장한다. Gensler를 운용 주체로 적은 것은 구글이고, DignityMoves를 운용 주체로 바꾼 것은 3개월 뒤 Gensler 자사 블로그다.
- 같은 항목: '구글의 1차 발표문과 Gensler 자사 기술이 서로를 뒷받침한다'는 거짓이다. 두 출처는 AR을 누가 운용했는지에서 정면 충돌한다. 또 'Adobe(Aero)'는 구글 발표문에만 나오고 Gensler 블로그 본문에는 Aero가 한 번도 나오지 않으므로, Aero를 DignityMoves 운용 스택으로 적을 근거가 없다.
- Foster + Partners Glaucon 항목: '연도 미상 — Wayback 스냅샷 기준 2022~2024년 사이에 페이지가 존재했다'는 틀렸다. CDX 실측 결과 최초 보존은 2021-07-29, 이어 2021-10-19·2021-10-24, 마지막이 2022-05-22다. 2024년 스냅샷은 존재하지 않는다. 조사가 인용한 URL(web/2024id_/)은 302로 재지향되며 응답 헤더가 'x-archive-redirect-reason: found capture at 20211024021540' — 즉 2021년 10월 스냅샷이다. 연도를 URL에 쓴 숫자로 오인했다.
- 같은 항목: 'Foster + Partners 웹사이트는 자바스크립트 렌더링이라 직접 본문 취득이 안 되고 Wayback 보존본에도 개별 항목 본문이 없다'는 사실과 다르다. Wayback 보존본에서 Glaucon 본문 전문이 취득된다: 'Glaucon is a collaborative digital design tool developed by ARD to allow multiple users to collaborate in photo realistic virtual environments that can be experienced in VR, AR, mobile or through the web.' 개별 항목 페이지 .../experience-and-interaction/glaucon/ 도 statuscode 200으로 4회 보존돼 있다. (참고로 원문이 'virtual environments'라고 쓰므로 AR 판정은 조사보다 더 낮춰야 한다.)
- HOK 항목: '제시된 예시(뉴욕시 모델링, 관람석 시야)' 중 '관람석 시야'는 인용된 AEC Magazine 기사에 없다. 기사 전문에서 seat·sightline·sight line·view from 모두 0건이다. 실제 예시는 (a)뉴욕 인구 1천만 증가·해수면 6피트 상승 모델링, (b)'a digital-only stadium where you were floating above the field' 두 개다.
- HOK 항목: 사람으로 적은 'Jess Bayuk(인테리어·VR)'는 인용된 AEC Magazine 기사에 등장하지 않는다(0건). 그 기사에서 실제로 발언한 HOK 기술 인물은 Brian Jencek(샌프란시스코 계획 디렉터), Chloe Sun(토론토 design technology specialist), Greg Schleusner(뉴욕 director of design technology), Rashed Singaby(캔자스시티 senior project designer)다. Bayuk는 별건 2020년 HOK 보도자료에만 있다.
- KPF Urban Interface 항목: '브랜드가 접혔다'와 '별도 도메인 kpfui.com은 응답만 하고 내용이 없는 껍데기다'는 둘 다 틀렸다. 조사가 인용한 KPF 보도자료 원문의 마지막 줄이 실제 주소 'ui.kpf.com'을 명시한다. ui.kpf.com은 HTTP 200·204,739바이트, 제목 'KPF Urban Interface', 메뉴 The Smart(er) City/Tools/Research/Case Studies/Blog, 뉴스 최신 게시물 2024-03-12 'Announcing Summer 2024 Internships'까지 살아 있다. kpfui.com(403, 150바이트)은 KPF의 주소가 아니며, 엉뚱한 도메인을 근거로 소멸을 선고했다.
- KPF 항목: 인물로 적은 'Luc Wilson'은 인용한 출범 보도자료(kpf-launches-kpf-urban-interface) 본문에 0건 등장한다. 그 보도자료는 사람 이름을 전혀 싣지 않는다. Wilson 귀속은 별건 Architectural Record 기사에서 온 것으로, 출처 표시가 어긋나 있다.
- Snøhetta 항목: '자사 사이트 검색 + 사이트맵 전수 + Wayback 색인 세 경로 모두 0건'에서 첫 경로가 무효다. snohetta.com/search?q=… 는 결과를 자바스크립트로 불러오므로 원시 HTTP 응답에는 어떤 질의에도 결과가 없다. 통제 질의로 확인: q=opera(오슬로 오페라하우스 설계사)도 q=augmented와 똑같이 빈 search-result-results 컨테이너를 반환하고 href="/projects/ 링크가 0개다. '0건'은 부재의 증거가 아니라 방법의 산물이므로 독립 경로 3개가 아니라 2개다.
- Gustafson Porter+Bowman 항목: 근거로 든 'https://www.gp-b.com/search?q=augmented&format=json'은 JSON을 반환하지 않는다. Squarespace HTML 페이지가 돌아오며, 통제 질의 q=garden도 동일한 HTML 껍데기를 반환한다. 이 인용은 0건을 입증하지 못한다.
- (외 30건)

## cityscope
항목 16개 · 검증 정정 지적 38건

> 실물모형+투영 방식은 조경·도시 분야에서 헤드셋 AR보다 훨씬 긴 계보와 두꺼운 증거를 갖는다. 1999년 MIT의 Urp(I/O Bulb)에서 시작해 2002년 Illuminating Clay(점토+천장 레이저스캐너+투영)와 SandScape로 갈라지고, 2002년 ISMAR 논문 'Augmented Urban Planning Workbench'로 학계가 스스로 이것을 AR로 분류했다. 2006년 Mitasova·Ratti·Ishii 공동논문이 MIT 장비를 GRASS GIS에 연결하면서 계보가 NCSU로 넘어가 TanGeoMS(2010)를 거쳐 Tangible Landscape(2013~)가 된다. 조경 분야의 핵심 사례는 분명히 Tangible Landscape다. 오픈소스이고, 부품표가 공개돼 있고(Kinect 50~200달러, 프로젝터 500~1000달러, 키네틱샌드 50달러 — 총 2~4천 달러), 2026년 6월까지 커밋이 이어지며 단종된 Kinect를 Orbbec Femto로 갈아타는 중이다. 2013~2024년 사이 19개 기관 설치가 문서화돼 있고 LSU 조경대학원, 노르웨이 NVE, 인도네시아 브라위자야대 등이 포함된다. 그러나 이 19곳은 거의 전부 교육·전시·연구였다. 유료 설계 용역에 납품돼 도면이 된 사례는 찾지 못했다. 오슬로 Mærradalsbekken 사례(2022)도 시가 이미 제시한 3개 대안을 대학이 검증한 연구다. 한편 CityScope 계열은 반대의 이야기다. 2016년 함부르크 FindingPlaces는 시장 지시로 34회·약 400명이 참여해 161개 후보지를 냈고 행정이 실제로 심사했다 — 그러나 최종 권고는 6곳, 약 750명분, 목표 2만 명의 약 4%였다. 그리고 함부르크가 제도화한 것은 레고 테이블이 아니라 2021년 DIPAS라는 평면 터치테이블+웹이었다. 프로젝트 사이트 findingplaces.hamburg는 2026년 9월 현재 응답하지 않는다. 2019년 함부르크 신도시 공모, 2020년 파리 ChampScope, 2023년 하르키우, 2026년 MineScope로 오면서 CityScope는 점점 웹 지도가 됐고, 탠저블 코드 저장소 CS_Brix는 2022년 8월 이후 멈춰 있다. 요약하면 실물모형+투영은 조경에서 살아남았지만 '연구실과 교실'에서였고, 공공 행정에서는 한 번의 강렬한 실증 뒤 화면으로 되돌아갔다.


### Urp / Luminous Planning Table / Augmented Urban Planning Workbench
| 항목 | 내용 |
| --- | --- |
| 주체 | MIT Media Lab Tangible Media Group (Hiroshi Ishii) + MIT 도시계획학과(Eran Ben-Joseph). John Underkoffler, Ben Piper, Luke Yeung, Dan Chak, Zahra Kanji. 발주처 없음 |
| 도시·연도 | 미국 케임브리지(MIT). Urp 1999, Luminous Planning Table 2001, Augmented Urban Planning Workbench 2002 |
| 증거 수준 | 연구 프로토타입 (+대학 스튜디오 교육·학회 시연) |
| AR 여부 | AR 맞음. 실제 물리적 모형 표면에 계산 결과를 정합해 투영하는 공간형(투영형) AR이며, 2002년 판본은 AR 전문 학회 ISMAR에 게재됐다. 단 정합 대상이 '실제 현장'이 아니라 '축소 실물모형'이라는 점은 구분해서 서술해야 한다. |
| 규모 | 탁상 규모 작업대. 참여 인원·예산 공개 없음 |
| 기술 | I/O Bulb(천장 설치 프로젝터+카메라), 광학 태그가 붙은 건축 모형 블록, 실시간 그림자/반사/풍환경 계산 |
| 출처 | https://doi.org/10.1145/302979.303114 (Urp, CHI'99) · https://doi.org/10.1177/0739456X0102100207 (JPER 21:196-203) · https://doi.org/10.1109/ISMAR.2002.1115090 (ISMAR 2002) |

MIT의 실물모형+투영 계보의 출발점이다. Underkoffler와 Ishii는 1999년 CHI에서 Urp를 발표했는데, 'I/O Bulb'라는 프로젝터-카메라 결합 장치를 천장에 달아 평범한 탁자 위의 건축 실물모형에 그림자·유리 파사드 반사·보행자 높이 풍환경 시뮬레이션을 실시간으로 투영해 겹쳤다. 하루 중 임의 시각의 정확한 그림자를 실제 모형에 덮어씌우는 것이 핵심 시연이었다. 2001년 Ben-Joseph(도시계획)과 Ishii(미디어랩)가 'Luminous Planning Table'로 이를 도시설계 교육·공공 커뮤니케이션 맥락에 옮겨 계획학 저널(JPER)에 실었다 — 설계 전문가의 프로세스와 시민과의 소통 프로세스를 동시에 겨냥한다는 주장이었다. 2002년에는 도면·실물모형·디지털 시뮬레이션을 한 작업대에서 겹치는 'Augmented Urban Planning Workbench'를 ISMAR(국제 혼합·증강현실 심포지엄)에 발표했다. 즉 이 계보는 AR 학계 스스로가 AR로 받아들인 출발점이다. 다만 실제 도시계획 용역에 납품된 기록은 없고, MIT 스튜디오와 연구 시연의 범위에 머물렀다.

Urp는 CHI 논문 기준 625회 피인용으로 탠저블 인터페이스 분야의 정전이 됐다. 그러나 장비 자체는 실무 도구로 상품화되지 않았고, MIT Tangible Media Group의 도시계획 라인은 2002년 이후 사실상 종료되어 계보가 CityScope(같은 MIT, 다른 그룹)와 NCSU로 갈라졌다.

### Illuminating Clay
| 항목 | 내용 |
| --- | --- |
| 주체 | MIT Media Lab Tangible Media Group. Ben Piper, Carlo Ratti, Hiroshi Ishii (CHI 논문 저자). 프로젝트 페이지에는 Yao Wang, Bo Zhu, Saro Getzoyan도 기재 |
| 도시·연도 | 미국 케임브리지(MIT). 2002 |
| 증거 수준 | 연구 프로토타입 (CHI 2002 논문) |
| AR 여부 | AR 맞음. 점토 모형의 3차원 표면 형상을 스캔해 그 표면에 계산 결과를 정합해 겹치는 투영형 AR. 정합 대상은 실제 지형이 아니라 점토 모형. |
| 규모 | 탁상 규모. 참여 인원·예산 미공개 |
| 기술 | 가변 점토 모형 + 천장 설치 레이저 스캐너(실시간 깊이 영상) + 프로젝터. 분석: 그림자, 침식, 가시권, 이동시간 |
| 출처 | https://doi.org/10.1145/503376.503439 (CHI 2002, pp.355-362) · https://tangible.media.mit.edu/project/illuminating-clay/ |

조경 분야 실물모형+투영의 직접적 조상이다. 사용자가 점토 지형모형을 손으로 깎으면 천장에 설치된 레이저 스캐너가 변형된 형상을 실시간으로 포착하고, 그 깊이 영상을 지형분석 함수 라이브러리에 입력해 결과를 다시 모형 표면에 정합해 투영한다. 계산 항목은 그림자 투사, 토양 침식, 가시권(visibility), 이동시간이었다 — 전부 조경·토목 설계의 판단 변수다. 논문 제목이 'a 3-D tangible interface for landscape analysis'이고 Ben Piper의 석사논문 제목이 'The Illuminated Design Environment: a 3D Tangible Interface for Landscape Analysis'였다는 점에서, 처음부터 조경을 겨냥한 장치였다. 물리 모형의 즉각성과 계산 시뮬레이션의 동역학을 결합한다는 것이 저자들의 주장이었다. 실제 대상지를 가진 프로젝트에 적용된 기록은 논문에 없다.

이 장치는 4년 뒤 Mitasova·Ratti·Ishii 공동논문(2006)에서 GRASS GIS에 연결되며 NCSU로 넘어가고, TanGeoMS(2010) → Tangible Landscape(2013~)로 이어진다. MIT 쪽의 원 장비는 후속 운용 기록 없음.

### SandScape
| 항목 | 내용 |
| --- | --- |
| 주체 | MIT Media Lab Tangible Media Group. Yao Wang, Assaf Biderman, Ben Piper, Carlo Ratti, Hiroshi Ishii |
| 도시·연도 | 미국 케임브리지 개발 / 오스트리아 린츠 전시. 2002년 9월부터 |
| 증거 수준 | 전시·시연 (아르스 일렉트로니카 센터 상설 전시) |
| AR 여부 | AR 맞음(투영형). 손으로 만든 모래 지형 표면에 계산 결과를 정합해 겹친다. 정합 대상은 모래 모형. |
| 규모 | 탁상 규모 모래상자. 관람 인원·예산 미공개 |
| 기술 | 모래 + 상향/하향 광학 센싱 + 프로젝터 투영. 모드: 표고·경사·등고선·그림자·배수·향 |
| 출처 | https://tangible.media.mit.edu/project/sandscape/ |

Illuminating Clay의 점토를 모래로 바꾼 자매 프로젝트다. 사용자가 모래로 지형을 만들면 그 지형을 나타내는 모래 표면에 시뮬레이션이 투영된다. 제공 모드는 표고, 경사, 등고선, 그림자, 배수(drainage), 향(aspect)으로, 조경·지형 분석의 기본 항목을 거의 그대로 담았다. 중요한 것은 이 프로젝트가 논문에 그치지 않고 공개 전시로 나갔다는 점이다. 2002년 9월부터 오스트리아 린츠의 아르스 일렉트로니카 센터 'Get in Touch' 전시에 설치됐다. 즉 이 계보에서 일반 대중이 실제로 손을 댄 최초의 사례에 해당한다. 다만 설계 의사결정에 쓰인 기록은 없고, 전시·시연의 범주다.

전시 종료 시점과 이후 행방은 확인하지 못했다. 그러나 '모래 + Kinect + 프로젝터'라는 이 조합은 10년 뒤 UC Davis의 AR Sandbox로 저비용 재구현되어 전 세계 수천 곳에 퍼졌다 — 원형은 MIT였지만 확산은 다른 팀이 만들었다.

### Mitasova·Ratti·Ishii 공동연구(2006) → TanGeoMS (NCSU, 2010)
| 항목 | 내용 |
| --- | --- |
| 주체 | 2006: Helena Mitasova, Lubos Mitas, Carlo Ratti, Hiroshi Ishii, Jason B. Alonso, Russell Harmon. 2010(TanGeoMS): Laura Tateosian, Helena Mitasova, Brendan Harmon, Brent Fogleman, Katherine Weaver, Russell Harmon — NCSU |
| 도시·연도 | 미국 노스캐롤라이나 롤리(NCSU) + 케임브리지(MIT). 2006, 2010 |
| 증거 수준 | 연구 프로토타입 (IEEE TVCG / IEEE CG&A 논문, 적용 시연 3건) |
| AR 여부 | AR 맞음(투영형). 실사 데이터를 물리 지형모형에 투영하고, 모형 변형을 스캔해 다시 투영하는 정합 루프. 정합 대상은 축소 모형. |
| 규모 | 유역·사주·훈련장 단위 축소모형. 참여 인원·예산 미공개 |
| 기술 | 천장 레이저 스캐너 + 프로젝터 + 가변 점토 3D 모형 + GRASS GIS. 시뮬레이션: 유출, 폭풍해일, 경관 복원 |
| 출처 | https://doi.org/10.1109/MCG.2006.87 (IEEE CG&A 26(4)) · https://doi.org/10.1109/TVCG.2010.202 (IEEE TVCG 16(6)) |

MIT의 예술적 프로토타입이 GIS 엔진에 연결되어 '분석 도구'가 되는 전환점이다. 2006년 IEEE Computer Graphics and Applications 논문은 Helena Mitasova·Lubos Mitas(NCSU)와 Carlo Ratti·Hiroshi Ishii(MIT)가 공저해, MIT의 탠저블 지형 장치를 오픈소스 GIS인 GRASS에 붙여 실시간 지형모형 상호작용을 구현했다. 2010년 NCSU는 이를 TanGeoMS로 정식화했다 — 레이저 스캐너, 프로젝터, 변형 가능한 물리 3차원 모형을 표준 GIS에 결합한 시스템이다. 사용자가 점토 표면을 고치거나 모형 위에 물체를 놓으면 천장 레이저 스캐너가 포착해 GIS로 불러와 실제 프로세스를 시뮬레이션하고 결과를 다시 모형 표면에 투영한다. 논문은 세 가지 적용을 시연했다: 유역 내 유출(runoff) 관리, 해안 사주(barrier island)에 대한 폭풍해일 영향 평가, 군 훈련장의 경관 복원. 조경·토목 실무 과제를 대상으로 삼은 최초의 본격적 사례군이다.

레이저 스캐너는 고가였고, 2013년 이후 Microsoft Kinect(깊이 카메라)로 대체되면서 시스템이 Tangible Landscape로 개명·재구축됐다. 즉 TanGeoMS는 폐기가 아니라 저비용화를 통해 계승됐다.

### Tangible Landscape (NCSU GeoForAll Lab) — 본체
| 항목 | 내용 |
| --- | --- |
| 주체 | NCSU Center for Geospatial Analytics / GeoForAll Lab. 교수진 Helena Mitasova, Lubos Mitas, Laura Tateosian, Ross K. Meentemeyer. 연구진 Anna Petrasova(주 개발·유지보수), Vaclav Petras, Corey White, Brendan Harmon, Payam Tabrizian. 발주처 없음(대학 자체 연구) |
| 도시·연도 | 미국 노스캐롤라이나 롤리. 최초 기록 2013-11-20, GitHub 저장소 개설 2014-08-19, 2026년 9월 현재 유지보수 중 |
| 증거 수준 | 연구 프로토타입 (단, 오픈소스로 다기관 채택·10년 이상 유지보수라는 점에서 단발 프로토타입과는 다르다) |
| AR 여부 | AR 맞음(투영형·공간형). 손으로 만든 3차원 지형 표면을 스캔해 그 표면에 GIS 연산 결과를 정합 투영한다. 헤드셋도, 카메라 패스스루도 쓰지 않는다. 정합 대상은 실제 현장이 아니라 축소 모형이므로 '현장 정합 AR'과는 구분해야 한다. |
| 규모 | 탁상 규모 지형모형. 하드웨어 총액 대략 2,300~4,000달러(공개 부품표 합산). 연구비 출처·금액은 확인 못함 |
| 기술 | 깊이 센서: Xbox One Kinect(50~200달러) + 어댑터(25~200달러) — 위키는 여전히 Kinect v2만 문서화하며 'Microsoft가 더 이상 생산하지 않는다'고 명시. 실제 코드는 2026년 5~6월 커밋에서 Orbbec Femto 센서 탐지·화이트밸런스 제어를 추가(PR #40). 프로젝터: Optoma ML750(500달러) / Epson PowerLite 1795F(950달러) / Optoma EH460ST(1000달러). 거치: Kupo C-스탠드 키트(120~200달러) + 베이비 월플레이트. 컴퓨터: System76 Oryx Pro(1500달러). 모형재: Waba Fun 키네틱샌드 11파운드(50달러). 소프트웨어: GRASS GIS + Blender + Python |
| 출처 | https://tangible-landscape.github.io/ · https://github.com/tangible-landscape/grass-tangible-landscape (커밋 이력) · https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Parts (부품·가격) · https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Physical-setup · 단행본 https://doi.org/10.1007/978-3-319-25775-4 및 https://doi.org/10.1007/978-3-319-89303-7 |

조경 분야 실물모형+투영의 사실상 표준 시스템이자, 이 축에서 유일하게 지금도 유지보수되는 코드베이스다. 물리 지형모형(키네틱 샌드 또는 폴리머)을 손으로 조각하면 깊이 센서가 스캔하고, 포인트클라우드 처리 → GRASS GIS 공간연산 → 프로젝터 투영 → Blender 3D 렌더링의 실시간 루프가 돌아간다. 지형을 깎으면 시뮬레이션 물길이 바뀌어 새 하천과 호수가 생긴다. 기능 목록에는 협업 모델링, 자유형상 조형, 객체 탐지·분류, 실시간 지리공간 분석, 시계열 분석, VR 연동이 있다. 적용 분야로는 정지·절성토, 우수관리, 침식 제어, 산책로 계획, 가시권, 태양광 잠재량, 지하 가시화, 도시성장, 병해·외래종 관리, 홍수·산불·해안 변화 대응, 공간 교육이 열거된다. 결정적으로 완전 오픈소스이며 부품표와 가격이 위키에 공개돼 있어, 누구나 2천~4천 달러 규모로 복제할 수 있다.

살아 있다. GitHub 저장소는 2026-09-21에도 푸시되었고 2026년 5~6월에 GRASS Tools API 리팩터링과 Femto 센서 지원이 들어갔다. 다만 스타 34개 규모의 소규모 연구 프로젝트이며, 단종된 Kinect 의존이 오래 병목이었다. 단행본 2권(Springer 2015 / 2018 2판)이 나왔다.

### Tangible Landscape 조경가 대상 검증 실험 (Harmon et al. 2018)
| 항목 | 내용 |
| --- | --- |
| 주체 | Brendan A. Harmon, Anna Petrasova, Vaclav Petras, Helena Mitasova, Ross Meentemeyer — NCSU |
| 도시·연도 | 미국 노스캐롤라이나 롤리(NCSU). 2018년 게재(실험 시기는 논문 본문 확인 필요) |
| 증거 수준 | 연구 프로토타입 (통제된 사용자 실험, 정량 평가 포함) |
| AR 여부 | AR 맞음(투영형). Tangible Landscape 본체와 동일한 정합 방식. |
| 규모 | 참가자 수를 초록에서 확인하지 못했다(비공개 저널). 'students, academics, and professionals' 세 집단이라는 구성만 확인 |
| 기술 | Kinect + 프로젝터 + 가변 지형모형 + GRASS GIS. 과제: 지형 조형, 절성토, 유출 시뮬레이션 |
| 출처 | https://doi.org/10.1177/1478077117749959 (IJAC 16(1):4-21) |

이 축에서 '조경 설계 도구로서' 효과를 정면으로 측정한 유일한 연구다. 조경학과 학생, 학계 연구자, 실무 조경가에게 조경 설계의 기본 과제 세 가지를 냈다 — 지형 모델링, 절성토(cut-and-fill) 분석, 물 흐름 모델링. 그리고 같은 과제를 (1) 탠저블 모델링, (2) 디지털(화면·마우스), (3) 아날로그 수작업 모형의 세 방식으로 수행시켜 비교했다. 평가는 인터뷰(정성)와 래스터 통계·형태계측(morphometric) 분석·지리공간 시뮬레이션(정량)을 함께 썼다. 결과는 탠저블 방식이 디지털도 아날로그 수작업도 이겼다는 것이다 — 참가자들은 더 정확한 모형을 만들었고, 지형의 형태적 특징(능선·계곡 같은 morphological features)을 더 잘 재현했다. 또 실시간 분석·시뮬레이션 피드백 덕분에 빠른 반복 과정으로 작업했고, 복잡한 지형 변화의 결과를 즉시 이해하고 조작할 수 있었다. 국제 건축컴퓨팅 저널(IJAC) 2018년 16권 1호 4~21쪽.

조경 분야에서 실물모형+투영의 설계 효용을 입증한 근거로 13회 피인용됐다. 그러나 이 결과가 조경 실무의 도구 채택으로 이어진 흔적은 없다 — 이후 확산은 설계사무소가 아니라 대학·박물관 쪽이었다.

### 급성참나무죽음 참여형 모델링 (Tonini 2017 캘리포니아 / Gaydos 2019 오리건)
| 항목 | 내용 |
| --- | --- |
| 주체 | 2017: Francesco Tonini, Douglas Shoemaker, Anna Petrasova, Brendan Harmon, Vaclav Petras, Richard C. Cobb, Helena Mitasova, Ross K. Meentemeyer. 2019: Gaydos 외 — NCSU Center for Geospatial Analytics 중심. 발주처 없음 |
| 도시·연도 | 미국 캘리포니아(2017 논문), 미국 오리건주 남서부(2019 논문) |
| 증거 수준 | 연구 프로토타입 (실제 이해관계자 참여 워크숍을 포함한 학술 연구) |
| AR 여부 | AR 맞음(투영형). Tangible Landscape 본체와 동일. |
| 규모 | 경관 규모(landscape-scale) 병해 확산 모델. 참여 이해관계자 수·회차·예산은 초록에서 확인 못함 |
| 기술 | Tangible Landscape + 확산 시뮬레이션 모델 + 출력 대시보드. 손 제스처로 방제 입력 제어 |
| 출처 | https://doi.org/10.1016/j.envsoft.2017.02.020 (EMS 92:176-188) · https://doi.org/10.1098/rstb.2018.0283 (Phil Trans R Soc B 374) |

Tangible Landscape가 실제 이해관계자를 모형 앞에 앉힌 두 건이다. 2017년 Environmental Modelling & Software 논문은 캘리포니아의 급성참나무죽음(sudden oak death, 병원체 Phytophthora ramorum) 관리 문제에 이 시스템을 적용했다. 목표가 서로 충돌하는 이해관계자 대표들이 지리적으로 사실적인 3차원 가시화 앞에 둘러서서 직관적인 손 제스처로 모델 시뮬레이션을 직접 조작하고, 출력 대시보드로 대안 전략을 비교했다. 저자들의 결론은 정보를 갖게 된 개인들이 상충(trade-off)을 스스로 다루기 시작했고 그것이 해법 구성으로 이어졌다는 것이다. 2019년 Philosophical Transactions of the Royal Society B 논문은 이를 오리건 남서부로 확장했다 — 새로운 EU1 계통이 유입되어 실질적 우려가 커진 지역에서 지역 이해관계자와 함께 경관 규모 방제 전략 평가용 대화형 예측 도구를 공동개발했다. 모델러와 이해관계자 사이의 권력관계를 재편한다는 참여형 모델링(PM)의 주장을 식물역학에 처음 들여온 사례다.

방제 정책에 실제로 반영됐는지는 확인하지 못했다. 논문은 '공동학습과 협력적 관리전략을 생성할 잠재력'을 탐색했다고 서술하며, 구속력 있는 결정으로 이어졌다고 주장하지 않는다. 피인용 15회(2017)·27회(2019).

### Tangible Landscape Immersive Extension (탠저블 테이블 + HMD)
| 항목 | 내용 |
| --- | --- |
| 주체 | Payam Tabrizian, Anna Petrasova, Brendan Harmon, Vaclav Petras, Helena Mitasova, Ross Meentemeyer — NCSU |
| 도시·연도 | 미국 노스캐롤라이나 롤리(NCSU). SIGSPATIAL 2016, ACADIA 2017(케임브리지 발표) |
| 증거 수준 | 연구 프로토타입 (사례연구 시연) |
| AR 여부 | 부분적. 테이블의 투영 부분은 AR이지만, HMD로 보는 부분은 몰입형 VR(가상 경관 안을 걷는 것)이다. 실세계 정합이 아니라 스캔된 모형 지형을 가상공간으로 옮겨 렌더링하는 방식이다. 논문도 'immersive virtual environment'라고 명시한다. |
| 규모 | 탁상 모형 + 1인용 HMD. 참여 인원·예산 미공개 |
| 기술 | Tangible Landscape(Kinect+프로젝터+GRASS GIS) + Blender 렌더링 + 헤드마운트 디스플레이. HMD 기종은 논문 초록에 없음 |
| 출처 | https://doi.org/10.1145/2996913.2996950 (ACM SIGSPATIAL 2016) · https://tangible-landscape.github.io/publications.html (ACADIA 2017) |

실물모형+투영의 한계를 시스템 설계자들이 직접 인정하고 헤드셋으로 보완한 사례이므로, '테이블 방식 대 헤드셋 AR' 논의의 핵심 증거다. 저자들의 문제의식은 명확하다 — Tangible Landscape는 조감(bird's-eye view)만 제공한다. 그래서 몰입형 가상환경을 결합해, 사용자가 만든 경관 안을 가상으로 걸어다니며 사람 눈높이(human-scale)로 볼 수 있게 했다. 이제 지형을 조형하고 수목을 그리고 시점을 정하고 산책 경로를 배치하면, 그 결과를 (1) 투영된 실물모형 위에서, (2) 화면에서, (3) 헤드마운트 디스플레이에서 동시에 볼 수 있다. 2016년 ACM SIGSPATIAL 논문이 물리 구성과 소프트웨어 구조를 기술하고 사례연구로 기능을 시연했다. 2017년에는 ACADIA(케임브리지)에서 'Tangible immersion for ecological design'으로 생태 설계 맥락에 적용했다. 즉 테이블의 강점은 공유·협업이고 약점은 시점이며, 헤드셋의 강점은 시점이고 약점은 공유다 — 이 대비가 같은 장비 안에서 실증됐다.

이 확장 기능은 Tangible Landscape 공식 기능 목록에 'Virtual Reality'로 남아 있다. 별도 제품이나 실무 납품으로 분리되지는 않았다.

### 오슬로 Mærradalsbekken 개천 복원 — 그린인프라 대안 검증 (Ortega & Zanusso 2022)
| 항목 | 내용 |
| --- | --- |
| 주체 | Rengifo Ortega, Enrico Zanusso. 소속 기관이 OpenAlex에 기재되어 있지 않아 확인 못함(노르웨이 소재 대학 추정). 대상 대안의 출처는 오슬로 시(municipality of Oslo) |
| 도시·연도 | 노르웨이 오슬로, Mærradal 계곡. 2022년 게재 |
| 증거 수준 | 연구 프로토타입 (지자체가 제시한 실제 대안을 대학이 검증. 지자체 발주 용역이라는 증거는 없음) |
| AR 여부 | AR 맞음(투영형). Tangible Landscape 본체와 동일. |
| 규모 | 밀집 시가지 내 개천 유역 규모. GI 대안 3안. 워크숍 회차·참여 인원·예산은 확인 못함 |
| 기술 | Tangible Landscape + GIS 기반 수문 시뮬레이션. GI 유형: 스웨일, 레인가든, 저류지 |
| 출처 | https://doi.org/10.18261/kp.115.4.5 (Kart og Plan 115(4)) |

Tangible Landscape가 실제 행정의 실제 대안을 다룬, 조경적으로 가장 구체적인 사례다. 노르웨이 오슬로 시가 Mærradal 계곡의 개천(Mærradalsbekken) 복개 해체·복원을 위해 제시한 그린인프라(GI) 대안 3안을 대상으로, 연구자들이 Tangible Landscape를 써서 설계하고 수문학적 성능을 평가했다. 논문의 논지는 밀집 시가지에 스웨일·레인가든·저류지 같은 GI를 놓으려면 도시 표면유출의 동역학과 복잡성을 잘 이해해야 하고, 도시 조직이 시간에 따라 바뀔 때 유출 패턴이 어떻게 달라지는지 다루려면 높은 유연성이 필요하며, 탠저블 방식이 GIS 지원하에 여러 시나리오를 준실시간으로 시뮬레이션·비교하게 해줌으로써 그 두 요구를 동시에 충족한다는 것이다. Tangible Landscape 공식 출판목록에서 유일하게 명시적 '케이스 스터디'로 분류되는 항목이다. 학술지 Kart og Plan 115권 4호.

검증 결과가 오슬로 시의 최종 설계 결정에 반영됐는지는 확인하지 못했다(유료 논문). 논문 자체는 '시가 제안한 3안을 평가했다'고만 서술한다.

### Tangible Landscape 설치 확산 — 문서화된 19개 기관 (2013~2024)
| 항목 | 내용 |
| --- | --- |
| 주체 | NCSU GeoForAll Lab이 배포·지원하고 각 기관이 자체 구축. 대표 기관: LSU 조경대학원, 노르웨이 NVE, 미국 NGA, 볼드헤드섬 보전협회, 브라위자야대 |
| 도시·연도 | 9개국 이상, 2013년 11월(NCSU 최초)~2024년 5월(파키스탄 NUST). 위키 기록 19건 |
| 증거 수준 | 혼합 — 대학 교육·연구실 설치(다수), 공공기관 전시 설치(NVE 알타 댐, NGA), 환경교육 상설 프로그램(볼드헤드섬). 유료 설계 용역 납품은 없음 |
| AR 여부 | AR 맞음(투영형). 전부 동일 시스템. |
| 규모 | 기관별 1대 규모. 기관당 예산·이용자 수는 기록 없음 |
| 기술 | Kinect + 프로젝터 + 모래/점토 모형 + GRASS GIS. 볼드헤드섬은 라즈베리파이로 스캐닝·애니메이션 구동, 표고 10배 과장 |
| 출처 | https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Community · https://github.com/tangible-landscape/grass-tangible-landscape/wiki/BHIC-Tangible-Landscape |

이 계보가 얼마나 퍼졌고 무엇에 쓰였는지를 가늠할 수 있는 1차 자료다. 공식 위키의 커뮤니티 페이지에 좌표·날짜·용도가 붙은 설치 기록 19건이 정리돼 있다. 조경에 직접 닿는 것은 미국 루이지애나주립대(LSU) Robert Reich School of Landscape Architecture의 오픈소스 지리공간 연구실(2017년 12월)로, 우수관리 설계 게임과 제방 축조 시뮬레이션에 썼다. 공공기관 설치로는 노르웨이 수자원·에너지청(NVE, 오슬로, 2017년 봄)이 'FUDT(디지털 지형모델의 동적 설계를 위한 물리적 사용자 인터페이스)' 사업으로 알타 댐 전시 디스플레이에 넣은 것이 있다. 미국 국가지리정보국(NGA, 포트벨보어, 2016년 1월)도 목록에 있다. 환경교육 쪽에서는 볼드헤드섬 보전협회(2016년 5월)가 2014년 실측 지형을 표고 10배 과장해 모래로 재현하고 폭풍해일 침수를 투영하는 '해안침수 게임'을 운영했다 — 참가자가 방호사구를 쌓아 '침수 건물 수'를 줄이는 방식이고, 스캐너와 소프트웨어는 라즈베리파이로 돌렸다. 그 밖에 인도네시아 브라위자야대(카르스트 수문·열대림 산불 확산, 2017), 체코 마사릭대·팔라츠키대, 슬로바키아 샤파리크대('Krajina na dotyk'), 남아공 세인트존스칼리지, 아르헨티나 UADER, 미국 조지아대, USDA-ARS, 중국지질조사국 우한센터(2020), 파키스탄 NUST(2024) 등이 있다.

확산의 성격이 결정적이다 — 19곳 중 대부분이 지리·지형 개념 교육, 학생 실습, 박물관·전시 데모였다. 설계사무소나 발주처가 설계 산출물을 만들기 위해 도입한 사례는 목록에 없다. 각 설치의 현재 가동 여부도 위키에 갱신돼 있지 않다(볼드헤드섬 페이지는 2018년 9월 이후 미수정). 기록 간격이 2020년→2024년으로 벌어진 점은 확산 둔화를 시사한다.

### AR Sandbox (UC Davis)
| 항목 | 내용 |
| --- | --- |
| 주체 | Oliver Kreylos(UC Davis DataLab / 前 KeckCAVES). 협력: UC Davis Tahoe Environmental Research Center, Lawrence Hall of Science, ECHO Leahy Center for Lake Champlain. 재원: 미국 NSF |
| 도시·연도 | 미국 캘리포니아 데이비스 개발. 소프트웨어 페이지 최종 갱신 표기 2012-05-06. 2026년 현재 'Active' |
| 증거 수준 | 실제 납품·상설 설치 (박물관·학교 전시물로서). 단 설계 용역 납품은 아님 |
| AR 여부 | AR 맞음(투영형). 실제 모래 표면의 3차원 형상을 Kinect로 스캔해 그 표면에 등고선·수체를 정합 투영한다. 이름 자체가 'Augmented Reality Sandbox'다. 정합 대상은 실제 지형이 아니라 모래 모형. |
| 규모 | '전 세계 수천 곳(thousands of locations)'에 설치 — 박물관, 대학, 중·고등학교. 백악관, USA Science and Engineering Festival 전시 이력. 공개 설치 지도 운영. 기관당 비용은 자체 조달이므로 총예산 산정 불가 |
| 기술 | 실제 모래 + Microsoft Kinect + 데이터 프로젝터 + 오픈소스 SARndbox(GPU에서 생-브낭 천수방정식 해석). 소프트웨어·설명서 무료 |
| 출처 | https://datalab.ucdavis.edu/project/ar-sandbox/ · https://web.cs.ucdavis.edu/~okreylos/ResDev/SARndbox/ |

이 축에서 압도적으로 가장 널리 실제 설치된 시스템이며, 동시에 '조경 설계 도구가 아니다'라는 점이 중요한 사례다. UC 데이비스의 컴퓨터과학자 Oliver Kreylos가 KeckCAVES(지구과학 능동가시화 센터, 현 DataLab)에서 만들었고, 미국 NSF의 비형식 과학교육 사업으로 UC 데이비스 타호환경연구센터, Lawrence Hall of Science, ECHO Leahy Center for Lake Champlain과 협력해 개발했다. 구성은 실제 모래, Microsoft Kinect 3D 카메라, 데이터 프로젝터, 오픈소스 시뮬레이션·가시화 소프트웨어다. 사용자가 모래를 빚으면 표고 색상지도, 등고선, 시뮬레이션된 물(또는 용암)이 실시간으로 그 위에 겹쳐진다. 물 흐름은 GPU에서 생-브낭(Saint-Venant) 천수방정식을 풀어 계산한다. 소프트웨어와 조립 설명서는 무료로 배포하고, 건축 재료만 각자 조달하면 된다.

지속. UC Davis DataLab이 현재도 'Active'로 유지하며 설치 지도와 지원을 운영한다. 벨기에 왕립자연과학연구소, 브라질 판타나우 인근, 오스트리아 빈 ZOOM 어린이박물관, 이탈리아 CNR 볼로냐 해양과학연구소 등에서 자발적 구축 후기가 접수됐다. 그러나 목적이 처음부터 '지형도 읽기·유역 개념 교육'이었고, 설계 의사결정 도구로 진화하지 않았다 — 이 계보에서 확산에 성공한 것은 교육용 분파였다.

### MIT CityScope 플랫폼
| 항목 | 내용 |
| --- | --- |
| 주체 | MIT Media Lab City Science group(前 Changing Places). 총괄 Kent Larson. 주요 연구자 Ariel Noyman, Luis Alonso, Arnaud Grignard, Ira Winder, Yan Zhang, Yasushi Sakai, Markus ElKatsha, Ronan Doorley |
| 도시·연도 | 미국 케임브리지(MIT) 개발. 1999년 계보 시작, CityScope 명칭은 2014년 전후, 현재까지 |
| 증거 수준 | 연구 프로토타입 + 공공 시범사업 (사안별로 다름. 항목 13~15 참조) |
| AR 여부 | 부분적. 투영은 하지만 정합 대상이 '형태가 있는 지형 표면'이 아니라 격자 위 중성 백색 블록(지도 투영용 캔버스)이거나 평면이다. Illuminating Clay나 Tangible Landscape처럼 3차원 표면 형상을 스캔해 그 형상에 되맞추는 루프가 아니다. 실세계 정합 기준으로 보면 탁상 디스플레이+탠저블 UI에 더 가깝고, MIT 자신도 'AR·VR'을 피드백 모듈의 선택 옵션으로 별도 열거한다. AR로 뭉뚱그리면 안 된다. |
| 규모 | 도시·근린·가로 규모 축소모형. 함부르크 배치의 탁자는 2m×2m 맞춤 제작(Pipan 2018 확인) |
| 기술 | 색상 코드 레고 블록 + 카메라 기반 실시간 스캔(OpenCV) + 프로젝터 투영 + cityIO 클라우드 데이터 플랫폼. 오픈소스: https://cityscope.github.io/ |
| 출처 | https://www.media.mit.edu/projects/cityscope/overview/ · https://arxiv.org/pdf/1811.10123 (Noyman et al. 2017, 2.2절 일반 구성) · https://api.github.com/orgs/CityScope/repos (저장소 활동) |

레고 블록 실물모형 위에 데이터를 투영해 즉시 분석 결과를 보여주는 방식의 대표 계보다. 표준 구성은 세 덩어리다 — (1) 탁자 프레임 위에 놓인 탠저블 도시모형(도시·근린·가로 규모), (2) 실시간으로 장면을 스캔하는 센서·카메라와 컴퓨터로 이루어진 계산·해석 유닛, (3) 화면·프로젝터, 때로는 AR·VR·촉각 피드백을 포함하는 피드백 모듈. 탠저블 요소는 색상 태그가 붙은 블록으로, 건물이나 매싱 요소 역할을 한다. 저자들은 이 계보를 1999년 Underkoffler·Ishii·Ben-Joseph의 'Augmented urban planning workbench'와 'Illuminating clay', 그리고 Kent Larson의 2000년 'Louis I. Kahn — Unbuilt Ruins' 전시(위치 태그 건물 오브젝트)로 직접 연결한다. 핵심 차별점은 전문가용 특화 도구와 달리 전문지식이나 사전지식에 제약되지 않는 논의를 유도한다는 것이다. 프로젝트는 데모(MIT 내부 실험)와 배치(실제 계획 과정의 능동적 도구)로 나뉘고, 2017년 시점에 UAE, 호주, 중국, 안도라, 보스턴, 대만, 그리고 함부르크에서 배치가 있었다고 서술한다. 모든 개발·도구·소프트웨어는 오픈소스다.

플랫폼은 유지되지만 무게중심이 이동했다. 탠저블 모듈 라이브러리 CS_Brix는 2022-08-09 이후 푸시가 없고, 웹 저작 도구 CS_cityscopeJS는 2025-05-06이 마지막이다. 2026년 9월 현재 CityScope GitHub 조직에서 활발한 저장소는 대중교통·접근성 분석용 파이썬 도구들(UrbanAccessAnalyzer, transitLOS 등)이다. 레고 테이블에서 웹·시뮬레이션 분석으로 무게중심이 옮겨갔다.

### FindingPlaces — 함부르크 난민 주거 입지 선정 (2016)
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주·지시: 함부르크 제1시장 올라프 숄츠. 수행: HCU 시티사이언스랩 + MIT Media Lab Changing Places Group. 협력 행정: 상원사무처, 중앙난민조정본부(ZKF), 각 구청. 시민참여 진행: steg(함부르크 도시재생공사, 전문 모더레이션). 논문 저자: Ariel Noyman, Tobias Holtz, Johannes Kröger, Jörg Rainer Noennig, Kent Larson |
| 도시·연도 | 독일 함부르크. 2016년 5월~7월 (개발 기간 2016년 2월부터 3개월) |
| 증거 수준 | 공공 시범사업 (시장 직접 지시, 행정 기관이 결과를 실제로 심사·공개) |
| AR 여부 | 부분적. 위성영상·지도를 중성 백색 블록으로 채운 격자 탁자 표면에 상부 프로젝터로 투영하고, 탁자 하부에서 카메라가 블록 밑면 색상코드를 읽는 방식이다. 3차원 지형 형상에 되맞추는 정합 루프가 없고, 투영 대상은 실세계가 아니라 축소 지도 평면이다. 실세계 정합 기준으로는 AR이라 부르기 어렵다 — 탠저블 UI + 상부 투영 디스플레이로 서술하는 것이 정확하다. |
| 규모 | 워크숍 34회, 각 2시간, 총 참여자 약 400명(회당 평균 11명, 정원 20명, 월~토 다양한 시간대). 대상 7개 구(區), 구별 1회만 중복참여 허용. 장소는 HCU 1층 약 150㎡ 갤러리. 운영팀 6~8명(모더레이터 1, 기록 1, CSL 연구자 1, 기술 1, ZKF·구청 대표 1~2). 홍보 브로셔 약 4만 부, 도달 약 500만 시민. 개발·운영 예산은 공개된 적 없음 |
| 기술 | 탁자 2대(각 2m×2m 맞춤 제작), 각 탁자를 프로젝터 2대가 절반씩 조명. 투명 탁자 하부를 카메라 4대가 사분면씩 촬영해 레고 블록 밑면의 정사각 색상코드를 판독(단일보드 컴퓨터 2대가 ffserver/ffmpeg로 스트리밍, OpenCV+numpy로 처리). 통신은 Crossbar 라우터 + Autobahn WebSocket 퍼블리시/서브스크라이브. 백엔드 Python, 프런트 JS/HTML/CSS. GIS는 GeoServer + PostgreSQL/PostGIS, 지도는 OpenLayers, 질의는 WFS + OGR/GDAL. 축척 1:약 750m. 시유지 여부·현황용도·자연보전 등 다수 레이어를 교차·가중해 3등급 적합도 사전산출(최하등급 기준: 강한 제약 없고 약한 제약이 면적 50% 미만) |
| 출처 | https://arxiv.org/pdf/1811.10123 (Noyman et al., Procedia Computer Science, KES2017 / DOI https://doi.org/10.1016/j.procs.2017.08.180 — 전문) · https://www.media.mit.edu/projects/finding-places/overview/ · 사이트 접속 확인 2026-09-30 (TCP 타임아웃) |

실물모형+투영이 실제 행정 절차에 들어간, 이 축에서 가장 중요하고 가장 상세히 기록된 사례다. 2015년 유럽에 난민 신청 120만 건이 들어오고 독일이 그 3분의 1 이상(44만 2천 건)을 받는 가운데, 함부르크는 특정 지구에만 수용시설이 몰려 시민 항의가 일었다. 2015년 6월 올라프 숄츠 제1시장과 조이 이토 MIT 미디어랩 소장이 장기 연구협약을 맺어 하펜시티대(HCU)에 시티사이언스랩(CSL)을 세웠고, 2016년 2월 시장이 CSL에 시민참여 절차 개발을 직접 지시했다 — 연말까지 약 7만 9천 명 유입 예측에 대응할 입지를 시민 지식으로 찾자는 것이었다. 개발 기간으로 준 것은 3개월이었다. 워크숍은 세 스테이션으로 구성됐다: (I) 함부르크 전역 지도와 목표 2만 명 실시간 카운트다운, (II) 위성영상을 투영한 첫 번째 CityScope 탁자에서 적합도 3색 분류(빨강=부적합 지표 높음, 주황=중간, 노랑=적합 가능)로 지구 전체를 훑고 관심 구역 선택, (III) 두 번째 탁자에서 필지 위에 마커 블록을 놓으면 면적(㎡)·계획규제·용도지정·자연보전·비오톱·고압선 제약과 산정 수용력이 화면에 뜨고, 토론 내용이 로그로 기록됐다. 적합 판단이 서면 40~1,500명 범위의 수용인원 블록을 올려 시에 제안했다. 각 워크숍 후 제안 목록이 중앙난민조정본부(ZKF)에 바로 넘어가 타당성 심사를 받고, 결과와 사유가 2주 안에 온라인 공개됐다.

숫자가 이 사례의 핵심이다. 시민이 161개 입지를 제안해 약 2만 4천 명분 수용안을 냈고 목표 2만 명을 초과했다. 그러나 초기 심사에서 약 4분의 3이 부적합 판정을 받아 44곳만 남았고, 상세검토에서 24곳이 추가 탈락, 최종적으로 6곳이 실행 권고를 받고 10곳이 장래 계획 검토 대상이 됐다. 그 6곳의 수용 규모는 약 750명 — 당초 목표의 약 4%다. 제안 필지의 절반 이상이 자연·경관보전 대상인 공원·도심 녹지·농경지였고 15%가 운동장·놀이터였다. 저자들이 직접 적은 약점: 3개월이라는 촉박한 일정, 탁자가 커서 옮길 수 없어 모든 워크숍을 HCU에서 열었고 그 결과 참여자 선택편향이 생긴 것, 도시 데이터 부족, 비전문가가 계획 용어를 이해하지 못하고 투영된 지도·위성영상의 방향조차 잡기 어려워한 것. 일부 참여자는 이 절차를 '가짜 참여'라고 비판했다. 저자들은 사전 데이터 가공이 결과를 조작할 여지(암시적 색상 코딩이 논의 방향을 유도)와 정치세력에 의한 도구화 위험도 명시했다. 그리고 프로젝트 결과 공개 사이트 findingplaces.hamburg는 2026년 9월 30일 현재 DNS(194.95.76.18)는 남아 있으나 서버가 응답하지 않는다 — 인터넷 아카이브 최종 캡처는 2022년 7월 15일이다.

### CityScope 사전 실증 2건 — 보스턴 BRT 공청회(2015) / Kendall Sq·CCES-KACST 사용성 실험(2015)
| 항목 | 내용 |
| --- | --- |
| 주체 | 보스턴: MIT Media Lab Changing Places Group + MIT DUSP Mobility Futures Collaborative + 지역 커뮤니티 퍼실리테이터. Kendall Sq 논문: Tarfah Alrashed, Almaha Almalki, Salma Aldawood, Tariq Alhindi, Ira Winder, Ariel Noyman, Anas Alfaris, Areej Alwabil — CCES(KACST-MIT Center for Complex Engineering Systems, 리야드) 중심 |
| 도시·연도 | 미국 보스턴, 2015년 10월(워크숍 6회) / 미국 케임브리지 Kendall Sq, 2015년 논문 |
| 증거 수준 | 보스턴 BRT = 공공 시범사업(실제 커뮤니티 공청회). Kendall Sq·CCES = 연구 프로토타입(통제된 관찰 실험) |
| AR 여부 | 부분적/아님. 보스턴 BRT의 권역 도구는 터치스크린 웹이고, 근린·가로의 CityScope 탁자는 레고 블록 + 상부 투영 방식으로 실세계 정합이 아니다. Kendall Sq 실험도 동일하다. |
| 규모 | 보스턴: 워크숍 6회, 회당 약 2시간. 참여 인원 총계는 논문에 없음. Kendall Sq: 참여자 수를 초록에서 확인 못함(MIT 커뮤니티의 학생·직원·관계자 표본) |
| 기술 | 보스턴: 대형 수직 터치스크린(권역 웹 도구) + CityScope 탁자 2대(근린·가로). Kendall Sq: CityScope 탠저블 모형 + 반응형 동적 조닝 메커니즘, 영상 녹화 + 행동 코딩 스킴 |
| 출처 | https://arxiv.org/pdf/1811.10123 (2.3절, 보스턴 BRT 및 CS PlayGround 상세) · https://doi.org/10.1016/j.promfg.2015.07.243 (Alrashed et al., Procedia Manufacturing 3:1974-1980) |

FindingPlaces가 근거로 삼은 두 건의 선행 실증이며, 각각 공공 참여와 통제 실험을 맡았다. (1) 보스턴 BRT: 2015년 초 MIT Changing Places가 MIT 도시계획과(DUSP)의 Mobility Futures Collaborative와 함께 간선급행버스(BRT) 도입 영향을 전달하는 대화형 도구를 만들고, 2015년 10월에 6회의 진행형 워크숍을 열었다. 회당 약 2시간, 등록→오리엔테이션→도구 탐색→사후 설문의 동일 구성이었다. 세 축척을 동시에 썼다 — 권역은 대형 수직 터치스크린의 웹 도구, 근린과 가로는 CityScope 탁자 2대. 진행은 지역 커뮤니티 퍼실리테이터가 맡았는데, 참여자가 '기술과 분석의 통제권이 개발자에게 있다'고 느끼지 않게 하려는 의도였다. (2) Kendall Sq 'CS PlayGround': MIT 동캠퍼스 재개발을 소재로, 참여자를 두 집단으로 나눠 한쪽은 통상적 '펜과 종이' 토론, 다른 쪽은 CityScope 탠저블 모형으로 같은 계획 과제를 풀게 했다. 두 세션을 영상 녹화하고 코딩 스킴으로 행동·발화·제스처를 계량해 비교했다. 이 실험은 사우디 KACST와 MIT의 공동연구센터 CCES 연구자들이 주저자로 논문화했다 — 과제가 언급한 'Riyadh 배치'에 해당하는 실체는 이 연구 협력 라인이다.

보스턴의 자체 평가는 양면적이다. 참여자는 사후 설문에서 '아주 많이 배웠다'고 답했고 다축척 표현이 학습과 공동창작을 도왔다. 그러나 저자들이 적은 약점이 결정적이다 — 탠저블 모형은 조작 가능한 조각이 몇 개뿐이어서 창의적 탐색이 제약됐고, '세 축척 어디에서도 사용자가 만든 결과물이 문서화되지 않았다'(선호 노선 유형, 버스 우선권과 주차면의 상충 수용 의사 등). 즉 워크숍이 남긴 산출물이 없었다. 여기서 얻은 교훈(실시간 다축척 표현, 명확·단순한 목표, 잘 훈련된 현지 모더레이션)이 FindingPlaces 설계에 반영됐다. Kendall Sq 실험은 탠저블 방식이 통상 방식보다 참여자를 더 능동적으로 만들고 공통 이해를 빠르게 형성한다는 결과를 얻어 25회 피인용됐다.

### 접힌 것들 — 함부르크 이후 CityScope 탠저블의 퇴각 (2019~2026)
| 항목 | 내용 |
| --- | --- |
| 주체 | DIPAS: 함부르크 도시개발주택청 + 주정부 지리정보측량청(LGV) + HCU 시티사이언스랩. 2019 입찰 도구: Jesús López Baeza, Julia L. Sievert, André Landwehr, Jonas Luft, Philipp Preuner(HCU), Jürgen Bruns-Berentelg(HafenCity Hamburg GmbH), Ariel Noyman(MIT), Jörg Rainer Noennig. ChampScope: Ariel Noyman, Arnaud Grignard, Nicolas Ayoub, Tri Nguyen-Huu, Luis Alonso, Kent Larson. 하르키우: MIT City Science + 노먼포스터재단·노먼포스터연구소 + 하르키우 시의회 + UNEC |
| 도시·연도 | 독일 함부르크 DIPAS 2021 공개~현재 / 함부르크 신지구 입찰 2019(논문 2021) / 파리 2020 / 우크라이나 하르키우 2023~ / 칠레 라 이게라 2026년 9월 |
| 증거 수준 | 실제 납품·제도화 (DIPAS: 150개 이상 절차 / 2019 함부르크 입찰: 실제 공모 절차 적용) + 개념·온라인 전환(ChampScope) |
| AR 여부 | 아님. DIPAS, 2019 입찰 도구, 하르키우, MineScope 모두 화면 기반(웹·터치테이블)이며 실세계 정합이 없다. ChampScope도 결과적으로 온라인 플랫폼이 됐다. 이 항목의 논점 자체가 'AR/투영형이 화면으로 되돌아갔다'는 것이다. |
| 규모 | DIPAS: 150개 이상 절차에서 검증(참여 인원 총계는 해당 페이지에 없음). 나머지 사업의 참여 인원·예산은 확인 못함 |
| 기술 | DIPAS: 웹 + 현장 터치테이블. 인터랙티브 지도, 항공영상, 3D 모델, 지리데이터 통합. GPL 오픈소스. 2019 입찰 도구: 온라인, 소음 전파·보행 접근성 등 목표 지표 즉시 평가. 하르키우: 웹(scopekharkiv.org), 지표는 자연 접근성·보행성·입도(granularity). MineScope: HTML/CSS/JS + Leaflet, 정부 SIMBIO 서비스 연동, 워크숍 노트 GeoJSON 내보내기 |
| 출처 | https://www.dipas.org/ · https://doi.org/10.4018/ijepr.20211001.oa8 (López Baeza 외, IJEPR 10(4):121-137) · https://www.media.mit.edu/projects/champscope/overview/ · https://www.media.mit.edu/projects/kharkiv-masterplan-visualization-tool/overview/ · https://github.com/CityScope/MineScope · https://api.github.com/repos/CityScope/CS_Brix (최종 푸시 2022-08-09) |

이 축에서 책의 신뢰를 만들 항목이다. FindingPlaces가 성공 서사로 회자되는 동안, 실제 제도화된 것은 레고 테이블이 아니었다. (1) 함부르크가 제도로 남긴 것은 DIPAS(디지털 참여시스템)다 — 도시개발주택청이 주정부 지리정보측량청과 HCU 시티사이언스랩과 함께 개발해 2021년 GPL 라이선스로 공개했고, 150개 이상의 절차에서 검증됐으며, 독일 행정 클라우드를 통해 조달 절차 없이 다른 지자체가 쓸 수 있다. 구성은 온라인 참여 + 현장 인터랙티브 터치테이블이다. 레고 블록도, 상부 투영도, 하부 카메라도 없다. (2) 2019년 함부르크가 새 주거·업무지구 입찰에 CityScope를 적용했을 때, 그것은 '디지털 온라인 도구'였다 — 설계자와 심사위원이 소음 전파와 보행 접근성 등 목표 지표에 대해 즉시 평가를 받는 방식이다(López Baeza 외, IJEPR 2021). (3) 2020년 파리 ChampScope는 샹젤리제 개편을 다루는 물리 설치물로 Pavillon de l'Arsenal 전시(PCA-STREAM 큐레이션)에 나갈 예정이었으나 코로나로 가상 플랫폼으로 전환됐다 — 팀 소개문이 '3개 대륙, 5개 도시, 6개 집에서, 그중 파리는 없이'다. (4) 2023년 하르키우 마스터플랜 도구(노먼포스터재단, 하르키우 시의회, UNECE, Arup 협력)는 웹 기반이다. (5) 2026년 9월 공개된 최신 커뮤니티 워크숍 도구 MineScope(칠레 라 이게라 Dominga 광산 프로젝트)는 Leaflet 웹 지도다. (6) 코드로도 확인된다 — 탠저블 모듈 라이브러리 CS_Brix는 2022년 8월 이후 푸시가 없다.

레고 테이블은 제도화되지 못했다. 함부르크가 실제로 운영하는 것은 터치테이블+웹인 DIPAS이고, 같은 도시의 대형 공모에 쓰인 CityScope도 온라인 도구였다. FindingPlaces 결과 공개 사이트는 응답하지 않는다(2026-09-30 확인, IA 최종 캡처 2022-07-15). 2026년 현재 CityScope 조직에서 활발한 코드는 대중교통·접근성 분석 파이썬 도구이며, 탠저블 관련 저장소는 정지 상태다. 접힌 이유로 1차 자료가 직접 지목하는 것: 탁자가 커서 옮길 수 없어 참여자가 연구소로 와야 했고(선택편향), 사안마다 맞춤 GIS 전처리와 알고리즘 개발이 필요했고, 회당 정원이 20명에 묶였다.

### Pipan 2018 — 탠저블 계획지원시스템의 정치성 비판
| 항목 | 내용 |
| --- | --- |
| 주체 | Tomaž Pipan. 학술지 Urbani izziv 29권 보충호 63~78쪽 |
| 도시·연도 | 슬로베니아 발행. 2018 |
| 증거 수준 | 학술 비판 문헌 (오픈액세스 심사논문, 사례 2건 비교) |
| AR 여부 | 해당 없음(문헌 비판). 비판 대상인 CityScope는 위 12·13항 기준에 따라 '부분적'. |
| 규모 | 비교 사례 2건. 인용된 함부르크 수치: 워크숍 회당 정원 20명, 총 400명, 탁자 2m×2m |
| 기술 | 분석 대상: Digital Scenario Game(플레이 카드+인터랙티브 테이블, 수동형) vs CityScope(레고 블록+알고리즘 시뮬레이션, 능동형) |
| 출처 | https://doi.org/10.5379/urbani-izziv-en-2018-29-supplement-004 · 전문 PDF https://urbaniizziv.uirs.si/Portals/urbaniizziv/Clanki/2018/04_63-78_Pipan_UI_supplement_2018.pdf |

이 축의 유일한 본격 비판 문헌이며, FindingPlaces를 사례로 삼는다. 저자는 두 종류의 탠저블 계획지원시스템(PSS)을 비교했다 — 카드를 쓰는 'Digital Scenario Game'(수동형)과 CityScope(능동형)다. 비판은 세 층이다. 첫째 물리적 규모: 업계 표준 인터랙티브 테이블이 약 1.6m×1m인데 HCU의 CityScope 탁자는 2m×2m 맞춤 제작이었고, 좋은 인터넷 회선·전용 컴퓨터·화면·프로젝터까지 필요해 운반과 설치에 상당한 시간과 노력이 든다. 그래서 함부르크는 모든 워크숍을 HCU에서 열었고 '참여자들이 그것을 불편하게 느꼈다'. 공공 참여는 매우 민감한 일이라 그런 이유가 참여자 수와 분위기, 편향, 유의미한 피드백 의지에 영향을 준다. 둘째 규모의 한계: 워크숍은 회당 최대 20명이었고, 설계사고 방식상 퍼실리테이터 1인당 4~8명이 적정이다. 참여자를 늘리려면 워크숍 조를 늘려야 하고 그것은 장비를 늘리는 일이라, 대규모 여론 수집 포맷에는 부적합하다. 셋째가 가장 무겁다 — CityScope는 사전 구현된 알고리즘으로 새 공간데이터를 실시간 생성하는 '능동형'이므로, 결과는 프로그래머의 분석 역량과 기술에 크게 좌우된다. 저자는 라투르를 끌어와, 시뮬레이션 해답이 단 하나의 제시로 '반박 불가한 진리'처럼 렌더링되어 '관심의 문제(matters of concern)'를 우회해 '사실의 문제(matters of fact)'로 칠해진다고 비판한다. 그리고 그 사실성이 행정에는 유용하다 — 답이 없던 자리에 구체적 답을 주고, 해답이 기적처럼 나타나 관료와 과학자 양쪽을 책임에서 면제하면서 절차를 객관·투명·설득적으로 보이게 만든다.

저자의 결론은 타협적이다 — 촉각적 계기는 사람에게 통제권과 권위를 주므로 설계사고형 공공 참여에 매우 중요하지만, '크기와 기술적 복잡성은 탠저블 인터랙티브 PSS의 극복하기 어려운 한계'다. 온라인 도구는 큰 표본을 덮되 개인의 기여도가 낮고, 탠저블은 구체적 제안을 내는 포커스 그룹은 되지만 더 큰 대중의 대표성은 없다. 이 진단은 이후 실제 전개(함부르크가 DIPAS라는 온라인+터치테이블로 간 것)와 정확히 일치한다.

#### 검증에서 잡힌 정정
- 오슬로 항목 — 저자 소속 추정이 틀렸고, 그 결과 항목 분류도 틀렸다. 조사는 'Ortega·Zanusso의 소속 기관이 OpenAlex에 기재되어 있지 않아 확인 못함(노르웨이 소재 대학 추정)'이라 쓰고, 성격을 '지자체가 제시한 실제 대안을 대학이 검증'으로 분류했다. 그러나 소속은 미기재가 아니라 발행사가 Crossref에 직접 예치해 두었고, 내용이 다르다 — Rengifo Ortega = 'MSc and CEO at TLO Ortega'(사기업 대표), Enrico Zanusso = 'Landscape Architect (Freelance)'(프리랜서 조경가). 둘 다 대학이 아니다. 따라서 '대학이 검증'은 사실이 아니며, 데이터베이스 한 곳만 보고 추정한 결과다. 부수 효과로 같은 줄의 '지자체 발주 용역이라는 증거는 없음'이라는 단서도 전제가 무너진다 — 사기업 대표 + 프리랜서 실무자 조합은 지자체가 용역을 주는 전형적 구성이므로, 발주 가능성을 낮추는 근거가 아
- FindingPlaces MIT 페이지 접속 상태 — '사이트 접속 확인 2026-09-30 (TCP 타임아웃)'은 틀렸다. 같은 날짜(2026-09-30 KST)에 https://www.media.mit.edu/projects/finding-places/overview/ 는 HTTP 200, TTFB 0.64초, 147,752 바이트로 정상 응답한다. 타임아웃이 아니다. 날짜까지 명시한 검증 기록이므로 그대로 두면 이후 재현 시 어긋난다. (같은 도메인의 champscope/kharkiv 페이지도 모두 200 정상)
- López Baeza 외 2021 논문 — Philipp Preuner의 소속이 잘못 배치됐다. 조사는 'Philipp Preuner(HCU)'로 묶고 'Jürgen Bruns-Berentelg(HafenCity Hamburg GmbH)'만 따로 떼었으나, Crossref 발행사 예치 메타데이터에서 Preuner는 Bruns-Berentelg와 같은 HafenCity Hamburg GmbH 소속이다. HCU 소속은 López Baeza·Sievert·Landwehr·Luft·Noennig 5인이다. 출처: https://api.crossref.org/works/10.4018/ijepr.20211001.oa8
- Tangible Landscape 하드웨어 총액의 산출 근거 표현이 부정확하다 — '하드웨어 총액 대략 2,300~4,000달러(공개 부품표 합산)'에서 결과 범위는 타당하지만 '부품표 합산'이라는 근거 서술은 맞지 않는다. Parts 위키는 프로젝터 3종($500/$950/$1000)과 C-스탠드 여러 종을 택일 대안으로 나열하므로 문자 그대로 전부 합산하면 약 $5,450~6,450이 나온다. 조사의 범위는 '구성요소별 1종 택일' 시의 값(실제 계산 약 $2,590~$3,414)으로, 결론은 옳고 근거 문구만 틀렸다. '부품표 합산'이 아니라 '구성요소별 1종 택일 기준'으로 써야 재현 가능하다. 출처: https://github.com/tangible-landscape/grass-tangible-landscape/wiki/Parts
- SandScape의 '아르스 일렉트로니카 센터 상설 전시'에서 '상설'은 출처에 없는 격상이다. MIT 페이지 원문은 "SandScape has been exhibited at 'Get in Touch' exhibition at the Ars Electronica Center in Linz, Austria since September 2002" — 'Get in Touch'라는 특정 기획전 이름을 명시하며 'since'로 계속성만 시사한다. 상설(permanent) 설치라는 표현은 없다. 조사가 뒤에서 '전시 종료 시점과 이후 행방은 확인하지 못했다'고 자인한 것과도 앞뒤가 맞지 않는다. 출처: https://tangible.media.mit.edu/project/sandscape/
- CS_Brix를 '탠저블 모듈 라이브러리'로 부른 것은 부정확하고, 이 저장소만으로 '탠저블의 퇴각'을 논증하는 것은 근거가 약하다. GitHub 공식 설명은 "A python library for CityScope modules which handles communication with City I/O" — 모듈 간 통신 라이브러리이며 탠저블 전용이 아니다. 더 중요하게, 실제 탠저블 탁자의 스캐너 코드인 CS_CityScoPy는 2024-05-21 푸시로 CS_Brix(2022-08-09)보다 나중까지 손질됐다. 즉 '2022-08-09 이후 푸시 없음'이라는 단일 지표는 탠저블 퇴각의 증거로 부적절하다(다만 조직 전체의 2025~2026 활동이 교통·접근성·인구 분석으로 이동한 것은 사실이어서 결론 자체는 유지된다). 출처: https://api.github.com/orgs/CityScope/repos
- 검증 불가(반박은 아님) — Tabrizian 2016의 "논문도 'immersive virtual environment'라고 명시한다"는 직접 인용을 확인하지 못했다. 발행사가 초록을 비공개 처리했고(Semantic Scholar 'abstract elided by the publisher', ACM DL 403, CumInCAD 차단) 원문 접근이 막혔다. 정황(제목 'Immersive tangible geospatial modeling', 공식 기능 목록의 'Virtual Reality' 별항)은 주장을 뒷받침하지만, 따옴표로 묶은 인용문 자체는 1차 확인이 안 된 상태다.
- 검증 불가(반박은 아님) — MIT CityScope 인력 명단 중 Yan Zhang·Yasushi Sakai·Ronan Doorley는 인용된 MIT 개요 페이지에서 확인되지 않는다. 현재 페이지가 열거하는 인물은 Kent Larson·Ariel Noyman·Arnaud Grignard·Markus Elkatsha·Luis Alonso 5인뿐이다. Ira Winder는 별도로 확인됨(Alrashed 2015 공저자). 과거 참여자일 가능성이 높으나 인용 출처로는 뒷받침되지 않는다. 출처: https://www.media.mit.edu/projects/cityscope/overview/
- AR 판정 기준의 내부 모순(핵심 결함): 조사는 '3차원 표면 형상을 스캔해 되맞추는 정합 루프'를 투영형 AR의 기준으로 세워 CityScope·FindingPlaces를 '부분적/아님'으로 강등했으나, 같은 기준을 충족하지 못하는 Urp는 'AR 맞음'으로 인정했다. Urp의 CHI'99 초록 원문은 'physical architectural models placed on an ordinary table surface'로, 평면 탁자 위 이산 모형 + I/O Bulb 태그 추적 + 상부 투영이며 연속 표면 스캔 루프가 없다. CityScope(이산 레고 브릭 + 하부 카메라 색상코드 판독 + 상부 투영)와 구조적으로 동일하다. 두 판정은 양립할 수 없다.
- AR 판정의 보조 근거인 '자기 서술' 기준이 역으로 작동한다: 조사는 'MIT 자신도 AR·VR을 피드백 모듈의 선택 옵션으로 별도 열거한다'를 CityScope 강등 근거로 썼으나, Tangible Landscape 공식 사이트(tangible-landscape.github.io)의 기능 목록도 'Collaborative, Tangible freeform modeling, Object detection & classification, Real-time geospatial analytics, Real-time 3D rendering, Time series, Virtual Reality'로 VR을 별도 열거하며 'augmented reality'라는 용어를 한 번도 쓰지 않는다. 같은 잣대라면 조사가 'AR 맞음(투영형·공간형)'이라 단정한 TL 본체도 강등 대상이다.
- 'Tangible Landscape 설치 확산 — 문서화된 19개 기관' / '위키 기록 19건' → 틀렸다. 조사가 인용한 Community 위키(2026-09-30 확인)가 문서화한 최상위 기관은 16곳이다: NCSU GeoForAll Lab, NCSU GAPS, Masaryk 대학 지리학과, NGA, St Johns College+Kartoza, Palacký Olomouc, NVE, Macroscopia, Centro Regional de Geomática, UGA, Šafárik 대학(Košice), Brawijaya 대학, LSU, USDA-ARS, Wuhan Tangible GIS Lab, NUST. 하위 프로젝트 항목까지 세면 약 23건이 되어 19는 어느 집계와도 맞지 않는다. 또 '9개국 이상'은 실제로 정확히 9개국(미국·체코·남아공·노르웨이·아르헨티나·슬로바키아·인도네시아·중국·파키스탄)이다. 최초 2013-11-20과 최종 2024년 5월 NUST는 정확하다.
- Gaydos 2019 '참여 이해관계자 수·회차·예산은 초록에서 확인 못함' → 초록이 아니라 전문을 봐야 했고 그 전문은 무료다. 오픈액세스 전문(PMC6558554)은 'a participatory workshop in October 2017'(1회), 'We limited the maximum number of participants to 20', 'Twelve stakeholders from the US Forest Service, Oregon Department of Forestry and Oregon State University participated in a modelling workshop'을 명시한다. 즉 워크숍 1회·2017년 10월·이해관계자 12명(정원 20명)이 확인 가능하다.
- Ortega & Zanusso 2022의 '소속 기관이 OpenAlex에 기재되어 있지 않아 확인 못함(노르웨이 소재 대학 추정)' → 추정이 틀렸고 소속은 조사가 같은 문서에서 이미 인용한 출처에 적혀 있다. Tangible Landscape Community 위키의 NVE 항목은 'Institution: The Norwegian Water Resources and Energy Directorate (NVE) / Department: Hydrological department, GIS Section / Team: Ortega Mora Rengifo Zenon / Date: Spring, 2017'이다. 대학이 아니라 정부기관이며, 따라서 '지자체가 제시한 대안을 대학이 검증'이라는 성격 규정도 재검토가 필요하다. 논문 페이지도 누락됐다(Kart og Plan 115(4):382-399).
- SandScape를 '아르스 일렉트로니카 센터 상설 전시'로 적은 것 → MIT 프로젝트 페이지는 'Get in Touch' 기획전에 '2002년 9월부터' 출품됐다고만 적고 상설(permanent)이라 하지 않는다. 조사 자신이 같은 칸에서 '전시 종료 시점과 이후 행방은 확인하지 못했다'고 쓴 것과도 모순된다(종료 시점을 모르면서 상설이라 단정).
- SandScape 설명의 시대착오: '모래 + Kinect + 프로젝터라는 이 조합은 10년 뒤 UC Davis의 AR Sandbox로 저비용 재구현되어'는 2002년 시스템에 Kinect를 귀속시킨다. SandScape(2002)는 반투명 표면 아래 적외선 LED 배열과 IR 카메라로 모래 두께의 광 감쇠를 읽는 투과조명 방식이고 Microsoft Kinect는 2010년 11월 출시다. Kinect는 AR Sandbox의 기여이지 SandScape의 구성요소가 아니다.
- Tangible Landscape '하드웨어 총액 대략 2,300~4,000달러(공개 부품표 합산)' → 인용된 Parts 위키는 총액을 제시하지 않고 항목별로 상호 배타적인 대안을 나열한다(프로젝터 Optoma ML750 $500 / Epson 1795F $950 / Optoma EH460ST $1000, C-stand 키트 $120·$200·$200, 컴퓨터 System76 Oryx Pro $1500). 나열된 모든 가격의 단순 합은 약 $4,784이고 어떤 조합을 고르느냐로 값이 달라진다. 이 범위는 조사가 대안 목록 위에서 직접 계산한 값이며 '공개 부품표'에 적힌 수치가 아니다. 위키 가격표에는 깊이 센서 가격도 나타나지 않는다.
- 피인용 수치를 출처 표기 없이 사실처럼 적었고 데이터베이스에 따라 크게 갈린다. 'Urp ... 625회 피인용'은 Semantic Scholar 값이고 OpenAlex는 같은 DOI에 603회를 준다. 'Harmon et al. 2018 ... 13회 피인용'은 Semantic Scholar 값이고 OpenAlex는 20회다(약 54% 차이). 특히 후자는 '13회'라는 낮은 숫자로 '실무 채택으로 이어지지 않았다'는 논지를 받치는데, 근거 수치가 DB에 따라 20회로 바뀌는 만큼 단정할 수 없다.
- 'Augmented Urban Planning Workbench'를 Urp·Luminous Planning Table과 나란한 제3의 프로젝트명으로 올린 것 → 이는 논문 제목의 서술어이고 ISMAR 2002 논문이 명명한 시스템 이름은 'Luminous Table'이다. 초록 원문: 'We propose an augmented reality workbench called "Luminous Table"'. 2001년 JPER의 'Luminous Planning Table'과 2002년의 'Luminous Table'은 같은 계보의 장비명이므로, 세 개의 프로젝트명이 아니라 두 개의 장비명 + 한 개의 논문 제목이다.
- AR Sandbox의 '소프트웨어 페이지 최종 갱신 표기 2012-05-06' → 이 날짜는 Kreylos 페이지의 프레임셋 껍데기 하단 표기이며, 실제 내용 페이지(MainPage.html)는 'As of 03/31/2022, there is a new AR Sandbox User Support Forum on the Doc-Ok.org site.'까지 갱신돼 있고 '현재 릴리스'와 '다가오는 2.0 릴리스'를 언급한다. 2012년 표기를 소프트웨어의 최종 갱신처럼 인용하면 실제보다 10년 정체된 인상을 준다.
- 하르키우 항목의 '노먼포스터재단·노먼포스터연구소' → MIT 프로젝트 페이지가 명시하는 협력 주체는 Norman Foster Foundation, Kharkiv City Council, UNECE, Arup이며 별도의 '노먼포스터연구소'는 나오지 않는다. 그 페이지는 연도를 전혀 적지 않으므로 '2023~'의 근거가 해당 출처에는 없고, MIT 측 인원은 Adrian Mora(프로젝트 리드)·Izaskun Martinez-Jorcano·Luis Alonso·Kent Larson이다.
- MineScope를 '탠저블의 퇴각(2019~2026)'의 증거로 배치한 것은 표본으로 성립하지 않는다. 해당 저장소는 2026-09-18 생성(스타 0)으로 조사 시점 기준 열이틀 된 것이며 기관 차원의 경향을 입증할 이력이 없다. 또 README는 'Automatic tour movements do not send Unity scene commands'라고 적어 Unity 3D 장면 연동이 존재함을 시사하므로 '화면 기반(웹·터치테이블)'이라는 단정도 불완전하다(AR 아님이라는 결론 자체는 유효).
- 'Tangible Landscape ... 2026-09-21에도 푸시되었고'를 현재 개발 중이라는 근거로 쓴 것은 다소 과대하다. GitHub API상 pushed_at은 2026-09-21이지만 기본 브랜치의 최종 커밋은 2026-06-03이고 updated_at도 2026-06-03이다. 9월 푸시는 브랜치·태그 이벤트로 보이며 새 개발이 아니다(2026년 5~6월 활동 자체는 사실).
- AR Sandbox 규모 '전 세계 수천 곳(thousands of locations)에 설치' — 원문이 근거로 든 그 공개 지도가 부정한다. WorldMap.html 본문: "The AR Sandbox World Map was last updated on 07/31/2022, and contains 857 AR Sandbox locations." 원본 GeoJSON(ARS_locations.txt)을 직접 내려받아 계수한 결과 feature 860건·고유 기관명 854건. 900곳 미만이며 '수천 곳'은 UC Davis 홍보문의 미감사 자체 주장이다.
- AR Sandbox '공개 설치 지도 운영' / '현재도 ... 설치 지도와 지원을 운영한다' — 그 지도는 2022-07-31 이후 갱신되지 않았다(페이지 자체 표기). 4년 넘게 동결된 등록부를 '운영 중'으로 서술한 것은 성과 과대다.
- AR Sandbox '2026년 현재 Active' / '지속'을 유지보수 근거로 쓴 것 — 정본 구현 저장소 KeckCAVES/SARndbox의 최종 푸시는 2019-06-17이고, 소프트웨어 페이지 표기는 'Last change: 05/06/2012'. 'Active'는 DataLab 프로젝트 페이지의 상태 라벨일 뿐 코드 유지보수 증거가 아니다.
- SandScape → AR Sandbox 계보('모래+Kinect+프로젝터 조합이 10년 뒤 UC Davis의 AR Sandbox로 저비용 재구현') — UC Davis 본인 페이지는 착상 출처를 'a video created by a group of Czech researchers'와 'an even earlier project, Project Mimicry'(mimicry.monobanda.nl)로 명시한다. AR Sandbox 페이지군 전체를 검색해도 SandScape·Illuminating Clay·Tangible Media Group·Ishii·MIT 언급이 0건이다. 1차 출처가 부인하는 계보다.
- SandScape '아르스 일렉트로니카 센터 상설 전시' — MIT 프로젝트 페이지는 "exhibited at 'Get in Touch' exhibition at the Ars Electronica Center in Linz, Austria since September 2002"라고만 적는다. 기획전 명칭이 명시되어 있고 permanent 진술은 없다. 원문이 스스로 '전시 종료 시점을 확인하지 못했다'고 적으면서 '상설'로 분류한 것은 내부 모순이다.
- 오슬로 Ortega & Zanusso의 소속 '확인 못함(노르웨이 소재 대학 추정)' 및 '대학이 검증' 분류 — Crossref 발행사 메타데이터에 명기되어 있다: Rengifo Ortega = 'MSc and CEO at TLO Ortega'(민간 회사), Enrico Zanusso = 'Landscape Architect (Freelance)'. 둘 다 대학 소속이 아니다. 추가로 TL Community 위키는 동일인('Ortega Mora Rengifo Zenon')을 NVE 수문부 GIS과 소속, 2017년 봄 노르웨이 TL 구축자로 기록한다. 면수도 382–399로 확인된다.
- 이 축의 핵심 성과 결론 '조경 실무의 도구 채택으로 이어진 흔적은 없다 / 이후 확산은 설계사무소가 아니라 대학·공공기관·박물관' 및 '설계사무소나 발주처가 설계 산출물을 만들기 위해 도입한 사례는 목록에 없다' — 원문 자신의 사례 9번이 반증이다. 오슬로 건은 프리랜서 조경가(Zanusso)와 민간 컨설팅(TLO Ortega)이 오슬로 시의 실제 개천복원 대안 3안에 TL을 적용한 것이다. Community 목록에도 민간이 있다: Macroscopia(Simon Chambert, 요하네스버그, 2017-08)와 St Johns College + Kartoza(민간 지오공간 기업).
- Gaydos 2019 '참여 이해관계자 수·회차·예산은 초록에서 확인 못함' — 이 논문은 완전 오픈액세스(PMC6558554)이고 전문에 수치가 있다: 'Twelve stakeholders from the US Forest Service, Oregon Department of Forestry and Oregon State University participated in a modelling workshop', 'a participatory workshop in October 2017'(1회), 참가자 상한 20명. 실제 규모는 12명·1회이며, 원문의 공백은 회피 가능했고 규모 인식을 왜곡한다.
- (외 8건)

## municipal
항목 16개 · 검증 정정 지적 47건

> 해외 지자체가 조경·도시공간 증강현실을 실제 행정 절차에 넣은 사례는, 뒤져보면 거의 없다. 있는 것은 두 갈래다. 하나는 2016년 함부르크 FindingPlaces처럼 탁자 위에 레고와 프로젝터를 얹은 '공간증강' 계열이고, 다른 하나는 2025년 일본 PLATEAU의 지상·지하 보행 내비게이션처럼 스마트폰을 들고 현장에 서는 계열이다. 전자는 실제 행정 결과를 냈다 — 34회 워크숍, 시민 약 400명, 후보지 161곳 중 44곳 적합 판정, 6곳 시행 권고, 10곳 장래 검토. 그런데 그 뒤 함부르크가 150개 이상 절차에 실제로 돌린 도구는 AR이 아니라 2D 터치테이블 DIPAS였다. 증강현실은 시범사업에서 검증되고 상용 단계에서 탈락했다.  유럽연합 연구비도 같은 모양이다. 시민 공동설계를 정면으로 겨눈 U_CODE(약 360만 유로, 2016~2019)는 VR과 탠지블 테이블을 골랐고 AR은 넣지 않았다. AR을 제목에 박은 ARtwin(약 383만 유로, 2019~2022)은 산업·건설용이었고 종료 후 프로젝트 웹사이트조차 남지 않았다. 5G-TOURS(약 1,470만 유로)는 도시 3곳에 5G를 깔았지만 공공공간 AR은 없다. 유럽 7개 도시에 자연기반해법을 심은 URBiNAT(약 1,302만 유로)에도 AR은 등장하지 않는다. 국가 단위로 내려가면 규모가 드러난다 — 스웨덴 VINNOVA가 2018년 '도시계획용 AR'에 낸 과제는 기간 5개월, 수행기관 중소기업 한 곳이었다.  일본이 가장 멀리 갔다. 다만 방향이 뜻밖이다. MLIT PLATEAU가 2025년 구라시키·교토에서 옥외광고·경관 심의에 넣은 '경관마을만들기DX v3.0'은 AR이 아니라 Windows 데스크톱 3D 앱이었다. 경관 심의라는, AR이 가장 쓸모 있어 보이는 자리에서 행정은 현장 중첩 대신 책상 위 3D를 선택했다.  요청받은 도시 목록 대부분은 빈칸이다. 헬싱키는 3D 메시와 에너지·기후 아틀라스를 갖췄지만 AR은 없다. 토론토 Quayside는 US$5천만을 약속하고 2020년 5월 접혔는데 그 기술도 AR이 아니라 센서·데이터였다. UN-Habitat는 2012년부터 55개국에서 공공공간을 함께 설계해왔는데 도구는 마인크래프트다. 국제기구도, 연방정부도, EU도 AR을 고르지 않았다.


### FindingPlaces — 함부르크 난민 주거지 입지 선정 시민참여
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주=함부르크시(당시 시장 Olaf Scholz). 수행=MIT Media Lab City Science group + HafenCity University CityScienceLab |
| 도시·연도 | 독일 함부르크, 2016년(워크숍 2016년 5~7월) |
| 증거 수준 | 공공 시범사업 — 시장 발주, 실제 행정 검토로 이어진 산출물 있음. 다만 상설 시스템은 아니었다. |
| AR 여부 | 부분적 — 머리에 쓰거나 손에 드는 기기는 없다. 실물 도시 모형에 프로젝터로 정보를 덧씌우는 공간증강현실(Spatial AR / Projection Mapping)이다. MIT 측 설명도 피드백 수단을 '스크린, 프로젝터, 그리고 AR·MR·VR 또는 터치'로 병기한다. 실세계(축소 모형) 위에 정합된 중첩이라는 점에서 AR 계열이지만, 야외 현장 정합은 아니다. |
| 규모 | 워크숍 34회(각 2시간), 시민 약 400명, 함부르크 7개 구 전역. 목표 수용 20,000명 → 제안 161곳/약 24,000명분. 예산 미확인. |
| 기술 | CityScope 탠지블 플랫폼 — 색상 태그 레고 블록 + 카메라·센서 실시간 스캔 + 프로젝터/스크린 피드백. 도시 지오데이터 연동 실시간 시뮬레이션. |
| 출처 | https://www.media.mit.edu/projects/finding-places/overview/ |

2015년 난민 유입으로 함부르크시가 2만 명분 주거지를 찾아야 했던 상황에서, 당시 시장 올라프 숄츠가 2016년 초 직접 발주한 시민참여 절차다. MIT 미디어랩 City Science 그룹과 하펜시티대학(HCU) CityScienceLab이 공동 수행했다. 도구는 CityScope — 색으로 태그된 레고 블록을 올린 탠지블 도시 모형에 카메라·센서가 실시간으로 배치를 읽고, 그 위에 시뮬레이션 결과를 프로젝터로 되쏘는 방식이다. 시민은 탁자 위 실제 블록을 옮기며 후보지를 놓았고, 시스템은 즉시 수용 인원·법적 제약을 계산해 되돌려줬다. 2016년 5~7월, 함부르크 7개 구(區)에서 2시간짜리 워크숍 34회, 시민 약 400명이 참여했다. 결과로 후보지 161곳(수용 약 24,000명)이 제안되고, 그중 44곳이 행정 검토에서 적합 판정을 받았으며, 6곳이 시행 권고, 10곳이 장래 계획 검토 대상이 됐다. 이 책에서 이 사례가 중요한 이유는 두 가지다 — 실제 행정 결정에 숫자로 들어간 드문 사례이고, 동시에 이 방식이 그 뒤 함부르크의 상용 도구로 이어지지 '않았다'는 점이다.

제안 161곳 → 행정 적합 판정 44곳 → 시행 권고 6곳, 장래 검토 10곳. 난민 주거 입지에 대한 지역 수용성을 높인 것으로 평가된다. 그러나 함부르크가 이후 150개 이상 참여 절차에 실제로 투입한 도구는 이 탠지블·프로젝션 방식이 아니라 2D 지도 기반 터치테이블 DIPAS였다. 즉 검증은 됐고 상용화는 안 됐다.

### DIPAS (Digitales Partizipationssystem) — 함부르크가 실제로 쓰기로 고른 것
| 항목 | 내용 |
| --- | --- |
| 주체 | 함부르크시 도시개발·주택청(BSW) 주도 개발. CityScienceLab·측량지리정보청 협력(문서상 BSW가 주체로 명기). |
| 도시·연도 | 독일 함부르크, 소스 첫 공개 2021년(GPL) |
| 증거 수준 | 실제 납품·운영 — 150개 이상 실제 참여 절차에서 사용, 오픈소스 배포, 타 도시 도입. |
| AR 여부 | 아님 — 3D 모델을 '데이터로' 쓰지만 표시는 웹 지도와 터치테이블이다. 실세계 정합 중첩이 없다. |
| 규모 | 150개 이상 참여 절차. 도입 도시: 함부르크 외 뤼베크·밤베르크. 예산 미확인. |
| 기술 | 웹 기반 참여 플랫폼 + 참여행사용 터치테이블. 대화형 지도·항공사진·3D 모델·지오데이터 통합. AI 보조 의견 분석. 코드 공개(BitBucket). |
| 출처 | https://dipas.org/ |

FindingPlaces 이후 함부르크시 도시개발·주택청(Behörde für Stadtentwicklung und Wohnen)이 개발해 실제 행정에 정착시킨 시민참여 시스템이다. 시민은 온라인에서 도시계획안에 대해 아이디어를 올리고 지도 위에 댓글을 달 수 있고, 오프라인 참여 행사에서는 같은 시스템을 대형 터치테이블로 쓴다. 연동 데이터는 대화형 지도, 항공사진, 3D 모델, 각종 지오데이터다. 2021년 GPL 라이선스로 공개된 오픈소스이며, 지금까지 150개 이상의 참여 절차에서 사용됐다. 최근 반년 사이 뤼베크, 밤베르크, 그리고 Code for Hamburg가 새 회원으로 합류했다. 이 책에 이 항목을 넣는 이유는 대조 때문이다 — 같은 도시가 같은 문제를 놓고 AR/탠지블 실험을 거친 뒤, 확장 단계에서 고른 것은 2D 지도와 터치스크린이었다.

현재 운영 중이며 타 지자체로 확산. AR이 아닌 쪽이 살아남았다는 것이 이 항목의 결론이다.

### CityScope (MIT City Science) — 도시별 탠지블·프로젝션 플랫폼
| 항목 | 내용 |
| --- | --- |
| 주체 | MIT Media Lab City Science group. 도시별로 하펜시티대학(함부르크), 통지대학(상하이) 등 현지 기관 협력. |
| 도시·연도 | 미국 케임브리지·보스턴, 프랑스 파리, 중국 상하이, 독일 함부르크. 개별 배치 연도는 공개 개요에 명시되지 않음. |
| 증거 수준 | 연구 프로토타입 + 공공 시범사업 혼재 — 대학 연구실 플랫폼이며, 지자체 발주 절차(함부르크)와 도시 협의체 협력(파리·상하이·보스턴)에 투입된 기록이 있다. |
| AR 여부 | 부분적 — 공간증강현실(탠지블 + 프로젝션). MIT 측 개요도 이를 'spatial augmented reality' 모델로 설명한다. 야외 현장 정합형 AR은 아니다. |
| 규모 | 개별 배치별 참여 인원·예산 미공개(함부르크 사례만 34회·400명 확인). |
| 기술 | 색상 태그 레고 블록·RoboScope 변형 탠지블 인터페이스 + 카메라 스캔 + 프로젝션/스크린 피드백. 도시 시뮬레이션 엔진. 오픈소스(GitHub). |
| 출처 | https://www.media.mit.edu/projects/cityscope/overview/ |

MIT 미디어랩 City Science 그룹이 만든 '공유·대화형 도시계획 연산' 플랫폼이다. 레고 기반 실물 블록(RoboScope 등 변형형 탠지블 인터페이스 포함)을 도시 모형 위에 놓으면 카메라가 배치를 읽고, 계산된 결과가 프로젝션으로 모형 위에 되씌워진다. 즉 축소된 실세계에 정합해 겹치는 공간증강현실이다. 공개된 배치 사례로 CityScope Volpe(미국 매사추세츠 케임브리지 볼프 부지 재개발), CityScope Champs-Élysées 및 ChampScope(파리 샹젤리제), CityScope LivingLine Shanghai(상하이, 통지대학 협력), Boston Bus Rapid Transit 커뮤니티 참여, Cooper Hewitt(자율주행 시나리오)가 있다. 모든 개발물·도구·소프트웨어는 오픈소스로 GitHub에 공개돼 있다. 함부르크 FindingPlaces가 이 플랫폼의 가장 성공한 행정 적용 사례다.

플랫폼 자체는 지속 중이고 오픈소스로 유지된다. 다만 개별 도시 배치가 상설 행정 도구로 정착한 기록은 확인되지 않는다. 워크숍 장치로 남았다.

### Project PLATEAU (국토교통성) — 전국 3D 도시모델 개방과 AR의 기반
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주·주관=일본 국토교통성(MLIT). 컨소시엄 방식으로 지자체·민간 참여. |
| 도시·연도 | 일본 전국. 공개 자료상 2022년 이전부터 활동 기록, 2025년도 유스케이스까지 진행 중. |
| 증거 수준 | 실제 운영 중인 국가 사업 — 오픈데이터 상시 공개, 연차별 실증 유스케이스 발주. |
| AR 여부 | 아님(기반 데이터·플랫폼) — PLATEAU 자체는 3D 도시모델 오픈데이터와 웹 뷰어다. 다만 AR 응용을 명시적으로 유도·발주한다. |
| 규모 | 유스케이스 등재 148건. 전국 다수 지자체. 총예산은 홈페이지에 미공개. |
| 기술 | CityGML 기반 3D 도시모델(LOD1~LOD4), 오픈데이터 배포, PLATEAU VIEW 웹 뷰어. 응용 측에서 Unity·AR SDK·CesiumJS 등 사용. |
| 출처 | https://www.mlit.go.jp/plateau/ |

일본 국토교통성(MLIT)이 주도하는 전국 단위 3D 도시모델 개방 사업이다. CityGML 기반 3D 도시모델을 오픈데이터로 공개하고, 지자체·기업·대학이 이를 써서 유스케이스를 만들게 하는 컨소시엄 구조다. 공개 홈페이지는 이 모델로 '도시를 모든 각도에서 관찰하고 정보를 자유롭게 겹치는' 것을 목표로 제시하고, 실증 항목에 'XR 기반 시민참여 도시계획', '지하가 데이터를 쓴 내비게이션'을 명시한다. 유스케이스 목록에는 148건이 등재돼 있고, 태그로 AR·Unity·CesiumJS·BIM 등 사용 기술이 표시된다. 대상 지자체로 도쿄 미나토·시부야·신주쿠, 히로시마, 교토 등이 언급된다. 조경·도시공간 AR을 이야기할 때 해외에서 데이터 기반이 가장 정비된 곳이 일본이라는 점, 그리고 그 기반 위에서 실제로 AR로 간 유스케이스는 손에 꼽는다는 점을 함께 봐야 한다.

계속 운영·확장 중. 다만 뒤의 두 항목이 보여주듯, 정비된 데이터가 곧 AR 채택으로 이어지지는 않았다.

### PLATEAU bz25-05 — 지상·지하 모델 활용 보행자 내비게이션(Station Navi)
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주=국토교통성 PLATEAU. 수행=JR東日本コンサルタンツ(JR East Consultants). 대상지 협력=도쿄 신주쿠구·도시마구. |
| 도시·연도 | 일본 도쿄 신주쿠역·이케부쿠로역 일대, 2025년도(실증 2025.12~2026.02) |
| 증거 수준 | 공공 시범사업(실증) — MLIT PLATEAU 사업 내 실증. 상용 운영 전 단계. |
| AR 여부 | AR 맞음(부분 기능) — 실외 GPS·실내 콜로컬라이제이션으로 위치를 잡고 카메라 화면에 경로를 정합해 겹친다. 단 앱의 주 표시 방식은 2.5D/3D 지도이고 AR은 보조 모드다. |
| 규모 | 세계 최대 승객량급 터미널역 2곳. 이용자 설문 실시(응답자 수 미공개). 예산 미공개. |
| 기술 | 3D 도시모델 CityGML(지하 LOD4/도로·지형 LOD1/건물 LOD2/도시시설 LOD3) + BIM·CAD + 네트워크 데이터 + POI. 측위=실내 콜로컬라이제이션·Wi-Fi·BLE 비콘, 실외 GPS. 개발=Unity, PostGIS. |
| 출처 | https://www.mlit.go.jp/plateau/use-case/bz25-05/ |

신주쿠역·이케부쿠로역 일대에서 지상과 지하를 이어 안내하는 3D 보행 내비게이션 앱 'Station Navi'를 만든 실증이다. 수행은 JR동일본컨설턴츠. 3D 도시모델(CityGML), BIM 데이터, CAD 도면을 합쳐 실내·실외, 지상·지하를 끊김 없이 안내한다. 사용 데이터의 상세도는 지하 LOD4, 도로·지형 LOD1, 건물 LOD2, 도시시설 LOD3다. 측위는 실내에서 콜로컬라이제이션·Wi-Fi·블루투스 비콘, 실외에서 GPS를 쓴다. 표시 방식은 2.5D/3D 지도와 AR을 함께 제공한다. 실증 기간은 2025년 12월~2026년 2월. 이용자 설문에서 2.5D/3D 지도 시인성은 80% 이상 긍정, 낯선 역에서 쓰고 싶다는 응답은 70% 이상이었다. 그런데 29.2%가 3D 표시가 느리다고 답했고, 휠체어 접근성 기능은 절반가량이 '있는 줄 알았지만 쓰지 않았다'고 했다. 보고서는 AR 기능에 대해 'AR에 익숙하지 않은 이용자가 기능을 발견하고 켜기까지의 UI 안내가 개선돼야 한다'고 적었다 — AR이 있어도 쓰이지 않는다는, 드물게 솔직한 기록이다.

실증 종료, 상용화로 가는 경로상의 단계로 기록됨. 남은 과제로 3D 렌더링 속도(29.2% 불만), AR 기능 발견성, 접근성 기능 활용률이 명시됐다.

### PLATEAU uc25-12 — 경관마을만들기DX v3.0 (구라시키·교토 경관·옥외광고 심의)
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주=국토교통성 PLATEAU. 수행=株式会社シネステジア(Synesthesia). 참여 지자체=구라시키시, 교토시(경관·옥외광고 담당 부서). |
| 도시·연도 | 일본 오카야마현 구라시키시 + 교토시, 2025년도(2025.08~2026.01). 선행 v2.0은 2024년도. |
| 증거 수준 | 공공 시범사업(실증) + 실무 운용 시험 — 지자체 직원이 실제 업무 흐름으로 약 2주 시험. 정식 상시 도입 여부는 미확인. |
| AR 여부 | 아님 — Windows 데스크톱 3D 애플리케이션(Unity). 현장 카메라 정합 중첩이 없다. 경관 심의라는, AR이 가장 쓸모 있어 보이는 자리에서 행정이 책상 위 3D를 고른 사례로 읽어야 한다. |
| 규모 | 대상 면적 구라시키 약 24.6㎢, 교토 약 6.5㎢. 시험 참여는 두 지자체 담당 직원(인원 미공개). 예산 미공개. |
| 기술 | 3D 도시모델 + Unity 기반 Windows 데스크톱 앱. 벽면비·이격거리 산정, 후퇴 규제 가시화, 먼셀 값 3D 색채 확인, BIM 모델 배치(v2.0). |
| 출처 | https://www.mlit.go.jp/plateau/use-case/uc25-12/ |

이 책의 주제에 가장 가까운 해외 공공사업이다. 국토교통성 PLATEAU 사업으로 수행기관은 시네스테지아(Synesthesia). 대상은 오카야마현 구라시키시(약 24.6㎢)와 교토시(약 6.5㎢)이며 기간은 2025년 8월~2026년 1월. 지자체 옥외광고·경관 심의 담당자가 2D 서류 대신 3D 도시모델로 규제 적합성을 판단하도록 만든 도구다. 세 가지 실제 업무 흐름을 지원한다 — 신규 옥외광고 신청(벽면 면적비 산정, 이격거리 측정, 후퇴 규제 가시화), 위반 시정(현황 재현, 거리 측정, 규제 범위 표시), 건축물·구조물 개별 심의(먼셀 값을 3D 공간에서 확인하는 색채 심의). 구라시키·교토 담당자가 약 2주간 기존 2D 서류 심의와 비교하는 운용 시험을 했고, 구라시키 담당자는 '주장의 진위를 공간적으로 확인할 수 있어 신청자에게 되묻는 일이 줄겠다'고 평했다. v2.0(2024년)에서는 경관계획 가시화, 높이 제한 표시, BIM 모델 배치 기능이 추가됐다. 결정적인 점은 이 도구가 AR이 아니라는 것이다 — Unity로 만든 Windows 데스크톱 애플리케이션이다.

'판단 지원 장치'로 규정됨 — 인간의 결정을 대체하지 않고 공간 관계를 명확히 하는 역할. v1.0→v2.0→v3.0으로 3년 연속 발전했으나 방향은 계속 데스크톱 3D였고 AR로 가지 않았다.

### Streetmuseum — 런던박물관 도시 역사 AR (소멸)
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주·소유=Museum of London(현 London Museum). 재정·통제=City of London Corporation + Greater London Authority(2008.04.01부터 공동). 제작=Brothers and Sisters(광고대행사). |
| 도시·연도 | 영국 런던, 2010년 공개 |
| 증거 수준 | 실제 납품·공개 배포(현재 소멸) — 일반 대중용 앱스토어 배포까지 갔고, 지금은 접근 불가. 공식 소개 페이지도 사라졌다. |
| AR 여부 | AR 맞음 — 위치·방위 기반으로 역사 사진을 실제 거리 풍경에 정합해 중첩. 마커 없는 지오로케이션 AR의 초기 대중 사례. |
| 규모 | 수록 이미지 수·다운로드 수는 이번 조사에서 1차 자료로 확인하지 못함. 예산 미확인. |
| 기술 | iPhone 앱. GPS·방위센서 기반 위치 정합, 박물관 소장 역사 사진 오버레이. SLAM·평면인식 이전 세대 기술. |
| 출처 | https://www.museumoflondon.org.uk/discover/streetmuseum (301 → https://www.londonmuseum.org.uk/blog/) · 기관 재정구조: https://en.wikipedia.org/wiki/Museum_of_London |

도시 공공공간에 AR을 얹은 초기 사례 중 가장 널리 인용된 것이다. 런던박물관(Museum of London)이 2010년 무료 iPhone 앱으로 공개했다. 이용자가 런던 거리의 특정 지점에 서서 카메라를 들면, 박물관 소장 역사 사진이 현재 풍경에 위치 정합해 겹쳐지는 방식이었다. 광고대행사 Brothers and Sisters가 제작했고 당시 여러 국제 광고·디자인 상을 받았다. 이 사업이 여기 들어가는 이유는 발주 구조 때문이다 — 런던박물관은 2008년 4월 1일부터 런던시티법인(City of London Corporation)과 런던광역시청(Greater London Authority)이 공동으로 통제·재정지원하는 기관이다. 즉 민간 콘텐츠가 아니라 광역 지자체 예산으로 만든 공공 옥외 AR이다. 그런데 앱은 앱스토어에서 내려갔고, 박물관 공식 페이지(museumoflondon.org.uk/discover/streetmuseum)는 2026년 현재 301 리다이렉트로 블로그 목록으로 넘어간다. 소장 컬렉션을 도시 현장에 되돌려놓았던 사업이, 기기와 OS가 바뀌는 동안 조용히 사라졌다.

소멸. 앱 배포 중단, 박물관 공식 소개 페이지는 301 리다이렉트로 블로그로 넘어간다. 공공 AR 콘텐츠의 수명이 기관의 수명보다 짧다는 증거.

### CityViewAR — 크라이스트처치 지진 후 소실 건물 현장 AR
| 항목 | 내용 |
| --- | --- |
| 주체 | HIT Lab NZ, University of Canterbury(뉴질랜드). 발주처 확인되지 않음. |
| 도시·연도 | 뉴질랜드 크라이스트처치, 2011년 |
| 증거 수준 | 연구 프로토타입(공개 배포까지 감) — 대학 연구실 산출물이며, 지자체 발주 사업이 아니다. 두 앱스토어 정식 배포 기록 있음. |
| AR 여부 | AR 맞음 — GPS·방위 기반으로 실제 도심 현장에 소실 건물·파노라마를 정합 중첩. 단 파노라마 중심이라 3D 모델 전체를 자세 정합한 것은 아니다. |
| 규모 | 참여 인원·예산·다운로드 수 미확인. |
| 기술 | 모바일 AR 앱(Android·iOS). 지진 직후 촬영 파노라마 + 3D 건물 모델. GPS 위치, 기기 회전 연동 파노라마, 지도 보기·목록 보기. |
| 출처 | https://www.hitlabnz.org/index.php/products/cityviewar |

2011년 크라이스트처치 지진으로 도심 건물이 대량 철거된 뒤, 뉴질랜드 캔터베리대학 HIT Lab NZ가 만든 모바일 AR 앱이다. 이용자가 실제 도심에 서서 기기를 들면, 지진 직후 촬영한 파노라마와 사라진 건물의 모습을 그 자리에 겹쳐 볼 수 있었다. 기기를 회전시키면 파노라마도 함께 돌아가는 방식이었고, GPS 기반 지도 보기와 전 세계에서 접근 가능한 목록 보기를 함께 제공했다. 참여 연구진은 Mark Billinghurst, Gun Lee, Jason Mill, Rob Lindeman, Adrian Clark, Thammathip Piumsomboon, Rory Clifford, Shunsuke Fukuden이다. Google Play와 Apple App Store 양쪽에 정식 배포됐다. 도시 조경·경관 분야에서 '사라진 것을 그 자리에 되돌려 보여주는' AR의 원형 사례로 지금도 인용된다. 다만 연구실 홈페이지는 여전히 '유지 중'이라고 적고 있으나, HIT Lab NZ 자체가 축소·해산 경로를 걸었고 현재 스토어에서 실제 설치 가능한지는 이번 조사에서 확인하지 못했다.

연구실 페이지는 계속 이용 가능하다고 적고 있으나, HIT Lab NZ의 활동 축소 이후 실제 스토어 가용성은 미확인. 학술 인용은 지금도 활발하다 — 즉 논문으로는 살아 있고 앱으로는 불확실하다.

### U_CODE (EU Horizon 2020) — 시민 도시 공동설계 환경
| 항목 | 내용 |
| --- | --- |
| 주체 | 조정=Technische Universität Dresden(독일). 참여 7개 기관(TU Delft, YNCREA Méditerranée, ACONEX Services, Oracle Deutschland, OPTIS, GMP International, Silicon Saxony Management). |
| 도시·연도 | 실증=독일 장거하우젠(2019.05~06), 테스트베드=독일 함부르크 클라이너 그라스브로크. 과제 기간 2016.02.01~2019.07.31 |
| 증거 수준 | EU 연구사업(공공 연구비) — 실증 워크숍까지 수행. 상용 제품·행정 도입 기록 없음. |
| AR 여부 | 아님 — 다섯 도구 중 몰입 기술은 VR Fox(VR)와 ShapeTable(탠지블 테이블)뿐이다. CORDIS 개요와 프로젝트 홈페이지 어디에도 AR 언급이 없다. |
| 규모 | EU 지원금 €3,603,831.25(총사업비 동일). 참여기관 7곳. 실증 참여 시민 수는 공개 자료에 미표기. |
| 기술 | 클라우드 Project Information Model. 도구 5종: DesignStormer, 스마트폰 공동창작 도구, VR Fox(VR), ShapeTable(탠지블 테이블), Sentiment Analyser. |
| 출처 | https://cordis.europa.eu/project/id/688873 · https://www.u-code.eu/ |

EU가 시민 참여형 도시설계 도구를 정면으로 겨눠 만든 Horizon 2020 과제다. 정식 명칭은 'Urban Collective Design Environment: A new tool for enabling expert planners to co-create and communicate with citizens in urban design'. 조정기관은 독일 드레스덴공대(TU Dresden)이고 TU Delft, YNCREA Méditerranée, ACONEX Services, Oracle Deutschland, OPTIS, GMP International, Silicon Saxony Management 등 7개 기관이 참여했다. EU 지원금은 €3,603,831.25이며 총사업비도 같은 액수, 기간은 2016년 2월 1일~2019년 7월 31일이다. 클라우드 기반 'Project Information Model'로 기술 데이터와 시민 의견을 통합하고, 'Project Play Ground'와 'Co-design Workspace'를 통해 비전문가와 전문 계획가를 잇는 구조였다. 만든 도구는 다섯 개 — DesignStormer, 스마트폰 공동창작 도구, VR Fox, ShapeTable, Sentiment Analyser. 실증은 독일 장거하우젠(Sangerhausen)에서 2019년 5~6월에 했고, 함부르크 클라이너 그라스브로크(Kleiner Grasbrook)가 테스트베드로 언급된다. 이 책의 논점은 명확하다 — EU가 시민 공동설계에 36억 원 규모를 쓰면서 고른 몰입 기술은 VR과 탠지블 테이블이었고, AR은 들어가지 않았다.

2019년 7월 종료. 프로젝트 사이트는 아카이브 상태이고 2019년 이후 후속 개발·행정 도입 정보가 없다. 장거하우젠 실증에서는 이용자 피드백 수집과 '개선 필요 사항 도출'로 마무리됐다.

### ARtwin (EU Horizon 2020) — 산업·건설용 AR 클라우드 + 디지털트윈 (흔적만 남음)
| 항목 | 내용 |
| --- | --- |
| 주체 | 참여=Siemens, Alcatel-Lucent, b<>com, Czech Technical University in Prague, HOLO-INDUSTRIE 4.0 SOFTWARE, Nokia Networks France, Artefacto, Q-PLAN INTERNATIONAL. 조정기관은 이번 조사에서 특정하지 못함. |
| 도시·연도 | 프랑스·독일·체코 등 다국. 2019.10.01~2022.12.31 |
| 증거 수준 | EU 연구사업 — 현장 파일럿 실증을 수행했다고 기술되나 구체적 장소·발주처·성과가 공개 결과에 없다. 공공기관 도입 기록 없음. |
| AR 여부 | AR 맞음(기술 목표) — AR 클라우드, 대규모 협업 AR, 실내 측위·카메라 기하가 명시적 연구 대상. 다만 도시경관·조경이 아니라 산업·건설 4.0 용도다. |
| 규모 | EU 지원금 €3,825,150. 참여기관 8곳. 산출물 문서 10건, 논문 14편, 웹 포털 1건. 파일럿 현장 규모·참여 인원 미공개. |
| 기술 | AR Cloud(대규모 협업 AR 인프라), 디지털트윈 연동, 컴퓨터비전(카메라 기하·모션 분할), 실내 측위, 5G 연계(Nokia·Alcatel-Lucent 참여). |
| 출처 | https://cordis.europa.eu/project/id/856994/results |

제목에 AR을 박은 드문 EU 대형 과제다. 정식 명칭 'An AR cloud and digital twins solution for industry and construction 4.0', 과제번호 856994, H2020-ICT-2018-3 콜. EU 지원금 €3,825,150, 기간 2019년 10월 1일~2022년 12월 31일. 참여기관은 Siemens(독), Alcatel-Lucent(프), b<>com(프), 프라하 체코공대, HOLO-INDUSTRIE 4.0 SOFTWARE(독), Nokia Networks France, Artefacto(프), Q-PLAN INTERNATIONAL(그리스)이다. 대규모 협업 AR을 위한 'AR Cloud' 구축이 핵심으로, 산출물은 요구사항 명세·플랫폼 아키텍처 등 문서·보고서 10건과 컴퓨터비전·AR 분야 피어리뷰 논문 14편, 그리고 ARtwin 웹 포털이다. 논문 주제는 카메라 기하, 모션 분할, 실내 측위, 'AR Cloud: Towards Collaborative Augmented Reality at a Large-Scale' 등이다. 문제는 결과 페이지가 '파일럿 유스케이스 현장 실증 평가'를 언급하면서도 어느 건설·도시 현장이었는지 명시하지 않고, 공공기관 배치나 실제 현장 적용 정보가 없다는 점이다. CORDIS는 프로젝트 웹사이트에 대해 '더 이상 이용 가능하지 않거나 원래 내용이 없을 수 있다'고 표시한다. 즉 논문과 보고서는 남고 시스템은 남지 않았다.

2022년 12월 31일 종료. 프로젝트 웹사이트 소멸 표시. 공공 발주처 배치나 상용 제품 전환 기록 확인되지 않음. AR을 정면에 내세운 EU 과제의 전형적 종착점이다.

### MARCUS (FP7) · VINNOVA '도시계획용 AR' — 연구비 목록에만 남은 두 건
| 항목 | 내용 |
| --- | --- |
| 주체 | MARCUS: Fraunhofer Society(독일), EU FP7 Marie Curie IRSES. VINNOVA 과제: Tomorrow Digital AB(스웨덴), 발주=Swedish Governmental Agency for Innovation Systems(VINNOVA). |
| 도시·연도 | MARCUS 2009.01.01~2011.12.31(독일). VINNOVA 과제 2018.05.03~2018.10.03(스웨덴). |
| 증거 수준 | 연구 프로토타입 이하 — 연구비 데이터베이스 등재 기록만 확인됨. 산출물·시연·납품 증거 없음. 이 항목은 '사례'가 아니라 '부재의 증거'로 써야 한다. |
| AR 여부 | AR 맞음(주제상) — 두 과제 모두 제목에 증강현실과 도시를 함께 명시한다. 다만 실제로 무엇을 만들었는지 확인할 산출물이 데이터베이스에 없다. |
| 규모 | 두 건 모두 데이터베이스상 지원 금액 €0으로 표기 — 실제 금액 미확인. VINNOVA 과제는 수행기관 1곳, 기간 5개월. |
| 기술 | 미공개. MARCUS는 '모바일 AR과 도시 맥락(context)' 연구, VINNOVA 과제는 도시계획용 AR로만 기재. |
| 출처 | https://api.openaire.eu/search/projects?keywords=%22augmented+reality%22+urban&format=json&size=50 |

도시 AR을 공공 연구비 데이터베이스에서 훑으면 실제로 걸리는 것이 놀랄 만큼 적다. OpenAIRE 과제 검색에서 '증강현실 + 도시' 조건에 남는 것은 사실상 두 건이다. 첫째 MARCUS — 'Mobile Augmented Reality and Context in Urban Settings', EU FP7-PEOPLE-IRSES-2008(마리퀴리 액션), 수행기관 독일 프라운호퍼, 기간 2009년 1월 1일~2011년 12월 31일. 제목만 보면 이 책의 주제 그대로인데, 데이터베이스에 기록된 지원 금액이 €0으로 비어 있고 산출물·후속 흔적을 추적할 수 없다. 둘째는 스웨덴 국가혁신청 VINNOVA가 낸 'AR (Augmented Reality) for urban planning' 과제로, 수행기관은 Tomorrow Digital AB 한 곳, 기간 2018년 5월 3일~2018년 10월 3일, 즉 5개월이다. 지원 금액도 데이터베이스상 €0으로 표기돼 실액을 알 수 없다. 이 두 건을 나란히 놓으면 규모의 현실이 드러난다 — '도시계획용 AR'이라는 주제에 국가 혁신기관이 붙인 것은 중소기업 한 곳, 5개월짜리 과제였다.

두 건 모두 후속 흔적이 추적되지 않는다. 특히 MARCUS는 2009년에 이미 이 책의 주제를 제목으로 달았으나 남은 것이 없다.

### Block by Block (UN-Habitat + Mojang/Microsoft) — 국제기구가 고른 것은 마인크래프트였다
| 항목 | 내용 |
| --- | --- |
| 주체 | 주관=UN-Habitat(2012년 방법론 개시·실행 총괄). 파트너=Mojang(마인크래프트 라이선스·자금), Microsoft(모조직 지원). 2015년 Block by Block Foundation 설립. |
| 도시·연도 | 55개국 이상. 2012년 개시, 현재 진행 중. 명시 사례: 나이로비(케냐), 뭄바이(인도), 쿨나(방글라데시), 리마(페루), 캄팔라(우간다). |
| 증거 수준 | 실제 준공 다수 — 쿨나(방글라데시) 솔라파크, 리마(페루) 공원 등 실제 조성 사례 존재. 국제기구 상설 프로그램. |
| AR 여부 | 아님 — 복셀 게임(마인크래프트) 기반 3D 공동설계. 실세계 정합 중첩이 없다. 디지털 참여설계지만 AR·MR 계열이 아니다. |
| 규모 | 55개국 이상, 공공공간 사업 수십 건, 수혜 인원 수십만 명(공개 자료 표현). Mojang 굿즈 수익 기여 500만 달러 이상. |
| 기술 | 마인크래프트(복셀 3D). 워크숍 진행 방법론 + 지역 파트너 체계. 특수 하드웨어 없음. |
| 출처 | https://www.blockbyblock.org/about |

UN-Habitat가 2012년에 개시해 지금까지 이어지는 공공공간 시민 공동설계 프로그램이다. 도구는 마인크래프트다. 주민이 나이·배경과 무관하게 3D 환경을 직접 만져보고 아이디어를 내고 합의를 만들도록 한다는 취지이며, 특히 여성·아동·노인·장애인·난민 같은 과소대표 집단의 목소리를 겨냥한다. Mojang은 마인크래프트를 워크숍용으로 라이선스하고 굿즈 판매 수익에서 500만 달러 이상을 냈고, Microsoft는 Mojang 인수 후 조직적 지원을 맡았다. 2015년 영향력 확대를 위해 별도 재단이 설립됐다. 55개국 이상에서 수십 개 공공공간 사업이 진행됐고, 수십만 명이 수혜를 봤다고 공개 자료는 밝힌다. 실제 조성된 곳으로 나이로비·뭄바이(초기 시범), 방글라데시 쿨나의 솔라파크 복원, 페루 리마의 공공 공원, 우간다 캄팔라 워크숍이 언급된다. 마인크래프트를 고른 이유를 '비용 효율적이고 빠른 반복과 아이디어 공유에 맞는다'고 스스로 적는다. 국제기구가 십수 년간 공공공간 참여설계를 하면서 AR을 고르지 않은 이유가 그 한 문장에 있다.

14년째 지속 중이며 실제 공원·공공공간 조성으로 이어진 사례가 여럿 있다. 참여설계 도구로서 '지속'과 '실제 준공'을 둘 다 달성한 유일한 국제 사례인데, 그 도구가 AR이 아니라는 것이 이 항목의 핵심이다.

### Connected Urban Twins (CUT) — 독일 연방 3개 도시 도시디지털트윈
| 항목 | 내용 |
| --- | --- |
| 주체 | 재원=Bundesministerium für Wohnen, Stadtentwicklung und Bauwesen(BMWSB) + KfW. 수행=함부르크·라이프치히·뮌헨 3개 도시. |
| 도시·연도 | 독일 함부르크·라이프치히·뮌헨, 2021~2025년(종료) |
| 증거 수준 | 실제 운영·종료된 공공사업 — 연방 재원, 3개 도시 공동, 산출물(플랫폼·DIN SPEC 표준) 확정. |
| AR 여부 | 아님 — 웹 기반 디지털 플랫폼 방식이라고 공식 자료가 명시한다. 도시 데이터 플랫폼·디지털트윈·웹 애플리케이션이며 실세계 정합 중첩이 없다. |
| 규모 | 3개 도시. 총예산은 공식 홈페이지에 미공개 — 이번 조사에서 확인하지 못함. |
| 기술 | 도시 데이터 플랫폼, 웹 애플리케이션. DIPAS navigator(참여형 매핑), DIPAS_stories(지도 스토리텔링), 도시개발 분석 전문 포털. DIN SPEC 91607 표준 제정. |
| 출처 | https://www.connectedurbantwins.de/en/ |

함부르크·라이프치히·뮌헨 세 도시가 공동으로 수행한 독일 연방 지원 도시디지털트윈 사업이다. 재원은 연방 주택·도시개발·건설부(BMWSB)와 KfW이고 기간은 2021~2025년으로 이미 종료됐다. 통합적 도시개발에 쓰는 'Urban Digital Twin'을 만들어 지속가능한 개발 시나리오를 검토하게 한다는 목표였다. 산출물은 도시 데이터 플랫폼과 웹 기반 애플리케이션이며, 구체적으로 DIPAS navigator(참여형 매핑 플랫폼), DIPAS_stories(지도 기반 스토리텔링), 도시개발 데이터 분석용 전문 포털이 나왔다. 여기에 지자체 도시디지털트윈을 위한 기술 표준 DIN SPEC 91607을 제정한 것이 눈에 띈다. 홈페이지는 사업 종료 후에도 지식 저장소로 유지되고 있다. 이 항목은 유럽 최대 규모급 공공 도시디지털트윈 사업이 무엇을 만들었는지 보여준다 — 웹 플랫폼과 표준이다. AR은 없다.

2025년 종료. 홈페이지는 지식 저장소로 유지. 가장 실질적인 유산은 DIN SPEC 91607이라는 표준과 DIPAS 계열 참여 도구다 — 둘 다 AR이 아니다.

### Helsinki 3D+ / Kalasatama Digital Twins — AR이 없는 모범 도시
| 항목 | 내용 |
| --- | --- |
| 주체 | 운영=헬싱키시(City of Helsinki). 문의 helsinki3d@hel.fi. Kalasatama Digital Twins의 개별 참여기업은 이번 조사에서 미확인. |
| 도시·연도 | 핀란드 헬싱키. 연혁 1980년대~, 2010년대 본격 확장. Kalasatama Digital Twins 2018.04~2019.01 |
| 증거 수준 | 실제 운영 중인 공공 서비스(단 AR 아님) — 오픈데이터·웹 뷰어 상시 운영. Kalasatama는 종료된 시범사업. |
| AR 여부 | 아님 — 3D 디지털 모델과 브라우저 기반 시각화. 공식 설명에 AR 응용이 전혀 언급되지 않는다. |
| 규모 | 도시 전역. 예산 공개되지 않음. |
| 기술 | 항공사진 기반 3D 메시, CityGML 계열 Urban Data Model(지형·건물·파사드 이미지·주소 검색), Energy and Climate Atlas(에너지 소비·태양광 잠재량 계산). 브라우저 시각화. |
| 출처 | https://www.hel.fi/en/decision-making/information-on-helsinki/maps-and-geospatial-data/helsinki-3d |

헬싱키는 도시 3D 데이터 분야의 대표적 선도 도시로 자주 인용된다. 실제로 헬싱키시가 운영하는 Helsinki 3D는 '도시 환경·운영·변화하는 상황의 가상 렌더링'을 정보기술·오픈데이터·상시 갱신 정보와 결합한 서비스로 규정된다. 구성은 세 가지다 — 항공사진 기반 3D 메시(건물·차량·선박 등 정지 객체 포함), 지형·건물·파사드 이미지를 담고 주소로 검색되는 Urban Data Model, 건물 에너지 소비와 태양광 잠재량을 계산하는 Energy and Climate Atlas. 개발 연혁은 1980년대까지 올라가고 2010년대에 기술 발전과 함께 크게 확장됐다. 명시된 시범사업으로 Kalasatama Digital Twins(2018년 4월~2019년 1월)가 있는데, 지역 건설 복합체의 디지털트윈 모델을 만들어 '설계·시험·응용·서비스 플랫폼'으로 삼는 사업이었다. 문의 창구는 helsinki3d@hel.fi다. 그런데 공식 소개 어디에도 증강현실 응용이 없다. 제공물은 3D 디지털 모델과 브라우저 기반 시각화 도구로 한정된다. 조사 대상으로 헬싱키를 지목한 이유가 '시민참여 AR'이었다면, 답은 그런 것이 없다는 것이다.

3D 데이터·오픈데이터 기반은 계속 확장 중이다. AR 방향으로는 가지 않았다. Kalasatama Digital Twins는 2019년 1월 종료 후 후속이 명시되지 않는다.

### Sidewalk Toronto / Quayside — US$5천만을 쓰고 접힌 스마트시티
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주=Waterfront Toronto. 수행=Sidewalk Labs(Alphabet 자회사). 후속=Quayside Impact LP(Dream Unlimited + Great Gulf Group). |
| 도시·연도 | 캐나다 토론토 Quayside. RFP 2017.03, 공식화 2017.10, 철수 발표 2020.05.07, 신규 RFP 2021.07, 우선협상자 2022.02 |
| 증거 수준 | 실제 발주·계약 후 철수 — 제안요청·선정·자금 약정까지 간 뒤 2020년 5월 7일 중단. 산출물은 실행계획 문서뿐. |
| AR 여부 | 아님 — 제안된 기술은 센서 네트워크·도시 데이터 수집·재생에너지 발전 등이다. AR이나 디지털트윈 시각화가 핵심으로 명시된 바 없다. 스마트시티와 AR을 섞어 쓰는 흔한 오독을 경계하기 위해 넣는다. |
| 규모 | Sidewalk Labs 약정 US$5,000만 + 1년치 참여 활동. Quayside 2.0은 주거 4,634세대·5개 블록 규모. |
| 기술 | 센서 기반 도시 데이터 수집, 전기차 활용 촉진, 현장 재생에너지 발전소 계획. AR·MR은 핵심 기술로 제시되지 않음. |
| 출처 | https://en.wikipedia.org/wiki/Quayside,_Toronto |

공공 스마트시티 사업이 어떻게 접히는지 보여주는 표준 교재다. 워터프론트 토론토가 2017년 3월 제안요청서를 냈고 같은 해 10월 알파벳 자회사 Sidewalk Labs가 선정돼 공식화됐다. Sidewalk Labs는 'US$5,000만과 1년치 참여 활동'을 실행계획 수립에 투입하겠다고 약속했다. 그러나 사업은 비밀주의와 개인정보 문제로 강한 반발을 받았다 — 이사회가 계약 서명 전 검토에 쓴 시간이 나흘이었고, 프라이버시 전문가들은 알파벳이 주민 데이터를 수집할 유인 구조를 문제 삼았다. 2020년 5월 7일 Sidewalk Labs CEO 댄 닥터로프가 '경제 불확실성과 부동산 시장 변동'을 이유로 사업 철수를 발표했다. 워터프론트 토론토는 2021년 7월 새 제안요청서를 냈고, 2022년 2월 Dream Unlimited와 Great Gulf Group 컨소시엄(Quayside Impact LP)이 우선협상자가 됐다. 이른바 'Quayside 2.0'은 주거 4,634세대, 부담가능 주택, 공립학교, 문화센터를 5개 블록에 배치하는 안으로, 2025년 착공 예정이었다. 중요한 점 — 이 사업의 기술은 AR이 아니었다. 센서·데이터 수집이었고, 그 때문에 접혔다.

2020년 5월 7일 중단. 사유는 공식적으로 경제 불확실성·부동산 변동이나, 실질적 원인은 비밀주의와 데이터 프라이버시 반발이었다는 것이 기록된 평가다. 부지는 전통적 개발 방식으로 넘어갔다.

### 영국 공공 디지털계획 예산의 실제 행선지 — PropTech Innovation Fund · NUAR
| 항목 | 내용 |
| --- | --- |
| 주체 | PropTech Innovation Fund: 영국 MHCLG Digital Planning Programme. 수혜=사우샘프턴시의회, 왓퍼드 자치구의회, 플리머스시의회, 다수 런던 자치구 등. NUAR: 구축=DSIT GDS:Geospatial, 운영=Ordnance Survey(2025.06~). |
| 도시·연도 | 영국. PropTech 라운드1 2021년, 라운드2 2022년, 라운드3~6 ~2026/27년. NUAR 2019.04 시범발표 → 2021.09 구축 → 2023.04 MVP → 2025.06 퍼블릭 베타 → 2025.12 정식 운영 |
| 증거 수준 | 실제 운영 중인 국가 프로그램(단 AR 아님) — 예산 배정·지자체 선정 내역 공개, NUAR은 2025년 12월 정식 운영. |
| AR 여부 | 아님 — PropTech Innovation Fund가 공개한 기술 유형은 3D 매핑·시각화와 부지 평가 소프트웨어이며 AR 구현 특정 기록이 없다. NUAR도 공식 문서에 AR 언급이 없는 데이터 등록부다. |
| 규모 | PropTech: R1 13개 지자체 £1,166,418 / R2 28개 과제 £3,020,321 / R3~6 37개 이상 시범사업. NUAR: 자산 보유기관 600곳 이상, 매설관·케이블 300만 km 이상, 주장 경제효과 연 £4억 이상. NUAR 총 구축비는 미공개. |
| 기술 | PropTech: 3D 매핑·시각화, 부지 평가 소프트웨어(개별 지자체별 기술 스택은 공개 문서에 미표기). NUAR: 지하시설물 통합 데이터 등록부·보안 열람 시스템. |
| 출처 | https://www.localdigital.gov.uk/funding/ · https://www.gov.uk/government/collections/national-underground-asset-register-nuar |

영국은 지방자치단체의 디지털 계획 도구에 전용 예산을 붙인 드문 나라다. MHCLG의 Digital Planning Programme 아래 PropTech Innovation Fund가 '계획 수립 절차를 앞당길 디지털 계획 도구 도입 가속'을 목표로 운영된다. 라운드 1(2021년)에 13개 지자체가 총 £1,166,418을 받았고(사우샘프턴시의회, 왓퍼드 자치구의회 등 각 £9만~10만), 라운드 2(2022년)에 28개 과제가 총 £3,020,321을 받았다(플리머스시의회 £285,000 등, 건당 £40,500~£285,000). 라운드 3~6은 2026/27년까지 이어지며 37개 이상의 지자체 주도 시범사업을 지원한다. 지원 주제는 커뮤니티 참여, 토지 평가, Section 106 협상 등이다. 그런데 공개된 기술 유형은 '3D 매핑 및 시각화', '지자체 간 계획·부지 평가 소프트웨어'이고, AR이나 VR 구현을 특정한 기록은 없다. 지하 쪽도 마찬가지다. 국가 지하시설물 등록부 NUAR은 DSIT의 GDS:Geospatial이 구축해 2025년 6월부터 Ordnance Survey가 운영하고, 2019년 4월 시범 발표·2021년 9월 구축 착수·2023년 4월 MVP·2025년 6월 퍼블릭 베타·2025년 12월 정식 운영의 경로를 걸었다. 600개 이상 자산 보유기관 데이터, 매설관·케이블 300만 km 이상, 연 £4억 이상의 경제효과를 주장한다. 그런데 공식 문서에 AR 언급이 없다. 한국이 제주·한전KDN·대구에서 지하시설물 AR을 실제로 돌리고 있는 것과 정면으로 대비된다.

둘 다 진행·운영 중이다. 결론은 부재의 확인이다 — 디지털 계획에 전용 예산을 붙인 나라에서도 돈은 3D 시각화와 데이터 등록부로 갔고 AR로는 가지 않았다.

#### 검증에서 잡힌 정정
- ARtwin 참여기관을 8곳으로 적고 Alcatel-Lucent을 넣었으나, CORDIS 856994의 기관은 총 7곳이다 — Q-PLAN INTERNATIONAL ADVISORS PC(조정, 그리스), B-COM(프랑스), SIEMENS AKTIENGESELLSCHAFT(독일), CESKE VYSOKE UCENI TECHNICKE V PRAZE(체코), NOKIA NETWORKS FRANCE(프랑스), HOLO-INDUSTRIE 4.0 SOFTWARE GMBH(독일), ARTEFACTO SAS(프랑스). Alcatel-Lucent은 참여기관 목록에 없고, Nokia Networks France의 기관 웹사이트 링크가 alcatel-lucent.com을 가리키는 것뿐이다.
- ARtwin '조정기관은 이번 조사에서 특정하지 못함'은 사실이 아니다. 인용한 https://cordis.europa.eu/project/id/856994/results 와 그 프로젝트 페이지에 조정기관이 Q-PLAN INTERNATIONAL ADVISORS PC(그리스)로 명기돼 있다. 정보 비공개가 아니라 조사 누락이며, 같은 조사가 Q-PLAN을 일반 참여기관으로 나열한 것과도 모순된다.
- ARtwin EU 지원금 '€3,825,150'은 부정확하다. CORDIS 표기는 총사업비 €3,825,148.75, EU 지원금 €3,825,148.75(동일)이다.
- U_CODE 참여기관 구성이 틀렸다. CORDIS 688873의 참여기관은 조정기관 포함 총 7곳(TECHNISCHE UNIVERSITAET DRESDEN, YNCREA MEDITERRANEE, TECHNISCHE UNIVERSITEIT DELFT, ACONEX SERVICES LIMITED, OPTIS, GMP INTERNATIONAL GMBH, SILICON SAXONY MANAGEMENT GMBH)이고, ORACLE Deutschland B.V. & Co. KG는 참여기관이 아니라 '제3자(third party)'로 별도 등재돼 있다. 조사는 Oracle을 참여기관 목록에 넣어 TU Dresden 외 7곳(총 8곳)으로 셈했으나 실제는 총 7곳이다.
- NUAR '자산 보유기관 600곳 이상'은 현재 규모가 아니라 장래 목표치다. gov.uk NUAR 안내는 현재 'contains data from over 350 asset owners'이고 'over 600 public and private sector asset owners'는 도달 목표로 기술한다. 목표치를 실적으로 옮겨 적었다.
- CityScope 항목의 "MIT 측 개요도 이를 'spatial augmented reality' 모델로 설명한다"는 인용 출처에 없는 서술이다. https://www.media.mit.edu/projects/cityscope/overview/ 와 https://cityscope.media.mit.edu/ 모두 'spatial augmented reality'는 물론 'augmented reality' 자체를 쓰지 않으며, 자기 서술은 'a slew of tangible and digital platforms'다. AR·MR·VR 병기는 FindingPlaces 페이지('display screens, projectors, as well as AR, MR, VR, or touch feedback')에만 존재한다.
- FindingPlaces 깔때기 '제안 161곳 → 행정 적합 판정 44곳 → 시행 권고 6곳, 장래 검토 10곳'은 중간 탈락 단계를 누락했다. MIT 페이지는 44곳 적합 판정 뒤 'A further 24 were excluded after a detailed examination'을 명기한다. 실제 경로는 161 → 44 → (24곳 추가 탈락) → 20 → 권고 6 + 장래 검토 10이다.
- Block by Block의 'Mojang 굿즈 수익 기여 500만 달러 이상'은 출처 표현과 다르다. blockbyblock.org/about의 문구는 'over $5 million mobilized from the Minecraft community'(마인크래프트 커뮤니티로부터 조성)로, 굿즈 판매 수익으로 특정하지 않는다.
- PropTech Innovation Fund 'R3~6 37개 이상 시범사업'은 한 라운드 수치를 네 라운드 합계처럼 쓴 것이다. localdigital.gov.uk는 라운드별로 R3(2023) 15개 지자체 주도 과제·27개 LPA·£3.2M, R4(2024/25) 37개 파일럿·49개 LPA, R5(2025/26) Geovation 챌린지 £1.2M, R6(2026/27) 11개 파일럿·44개 기관(지방계획·연합기관 28곳 포함)으로 공개한다. '37개'는 R4 단독 수치다.
- PLATEAU '공개 자료상 2022년 이전부터 활동 기록'은 불필요하게 모호하고 출처보다 늦다. 인용한 유스케이스 목록 페이지의 연도 태그가 2020年度부터 2025年度까지 걸쳐 있어 개시 연도(2020년도)가 명확히 공개돼 있다.
- Streetmuseum의 제작사 'Brothers and Sisters(광고대행사)'와 2010년 공개 연도는 이 항목이 제시한 두 각주(museumoflondon.org.uk/discover/streetmuseum → 301로 londonmuseum.org.uk/blog/ 일반 목록, 그리고 Museum of London 위키 재정구조 항목)로 전혀 지지되지 않는다. 확인해 보면 리다이렉트 도착지 블로그 목록 20건에는 Streetmuseum도 augmented reality도 언급이 없고, 위키 항목에도 앱 서술이 없다. 각주가 주장을 뒷받침하지 못하는 상태다.
- CityScope: '다만 MIT 측 개요도 이를 spatial augmented reality 모델로 설명한다'는 허위. media.mit.edu/projects/cityscope/overview/ 원문에는 'spatial augmented reality'라는 구절이 없고, CityScope를 'a concept for shared, interactive computation for urban planning'으로만 정의한다. 'augmented reality'는 Andorra 프로젝트의 연구 태그와 그룹 토픽 목록에만 등장한다.
- FindingPlaces: MIT 문장을 반대로 인용했다. 원문은 'The feedback module contains display screens, projectors, as well as AR, MR, VR, or touch feedback'로 프로젝터와 AR·MR·VR을 구분해 열거한다. 조사는 이를 '프로젝션=AR 계열'의 근거로 썼으나, 오히려 프로젝션이 AR로 분류되지 않음을 보여준다. FindingPlaces 개요에는 AR을 실제 사용했다는 서술이 전혀 없다(플랫폼의 선택 옵션일 뿐).
- PLATEAU uc25-01 누락(가장 중대). 2025년도 Public Solution으로, 내각부 SIP 3기 '被災現場支援ツール'(리얼타임 重畳)과 3D 도시모델로 현지에서 시·실동기관 직원에게 'AR技術による3D都市モデルの重畳'을 체험시키고 소방대 청취까지 한 공공 발주 실증. 발주=MLIT, 수행=株式会社雪研スノーイーターズ, 협력=防災科学技術研究所·マイスター, 장소=신潟 나가오카역 주변/삿포로 기요타구, 기간=삿포로 2025.8·나가오카 2025.12~2026.1. 조사의 '야외 현장 정합 AR 부재' 및 'PLATEAU 데이터가 AR 채택으로 이어지지 않았다'는 결론을 직접 반증한다.
- MARCUS 지원금 '€0으로 표기 — 실제 금액 미확인'은 오류. CORDIS(project/id/230831)는 총사업비·EU 지원금을 모두 €102,600.00으로 명기한다. 조사가 유일한 출처로 쓴 것은 CORDIS가 아니라 OpenAIRE 검색 API이고, €0은 그 레코드의 결손값이다.
- MARCUS '산출물·시연·납품 증거 없음 / 실제로 무엇을 만들었는지 확인할 산출물이 데이터베이스에 없다'는 범주 착오. CORDIS 목적문은 이 과제가 FP7-PEOPLE-IRSES(연구자 교류) 사업으로 EU 3개 기관 12명과 NZ 2개 기관 9명의 상호 파견·워크숍 2회를 산출로 선언했음을 명시한다. 애초에 제품 산출물이 없는 유형의 그랜트다.
- MARCUS '2009년에 이미 이 책의 주제를 제목으로 달았으나 남은 것이 없다'는 오류. CORDIS가 명시한 NZ 파트너는 University of Canterbury HIT Lab NZ(및 University of Otago)로, 조사가 별 항목으로 올린 CityViewAR(2011)을 만든 바로 그 연구실이며 과제 기간(2009~2011) 중 산출됐다. 또 목적문은 'The exchange supports the existing EU funded IPCity program'이라고 명시하는데, 조사는 선행 EU 도시 혼합현실 통합과제 IPCity를 전혀 다루지 않았다.
- ARtwin '조정기관은 이번 조사에서 특정하지 못함'은 조사 실패. 조사가 인용한 그 CORDIS 페이지 자체가 'Coordinated by Q-PLAN INTERNATIONAL ADVISORS PC, Greece'를 명기한다(Net EU contribution €608,500.00).
- ARtwin '참여기관 8곳' 오류. CORDIS는 조정기관 1곳 + 'Participants (6)' = 총 7곳(Q-PLAN, B-COM, Siemens AG, ČVUT Praha, Nokia Networks France, HOLO-INDUSTRIE 4.0 SOFTWARE, ARTEFACTO SAS)이다.
- ARtwin 참여기관에 'Alcatel-Lucent'를 별도로 올린 것은 오류. CORDIS 페이지에 ALCATEL이라는 문자열은 존재하지 않고, 해당 법인은 'NOKIA NETWORKS FRANCE'(Massy)로 등재돼 있다. 조사는 동일 법인을 두 곳으로 중복 계상했다.
- ARtwin 'EU 지원금 €3,825,150' 오류. CORDIS 실제 값은 €3,825,148.75(총사업비 동일).
- ARtwin 국가 표기 '프랑스·독일·체코 등 다국'에서 조정기관 소재국 그리스가 빠졌다.
- PLATEAU 개시 시점 '공개 자료상 2022년 이전부터 활동 기록'은 부정확. mlit.go.jp/plateau/about/ 이 '2020年にスタートしたPLATEAU'라고 명시한다(로드맵상 2022년 약 100도시 → 2024~2027년 약 500도시).
- DIPAS '도입 도시: 함부르크 외 뤼베크·밤베르크'는 출처 오독. dipas.org 뉴스(2026.06.30)는 'Mit Code for Hamburg sowie den Städten Lübeck und Bamberg sind im letzten halben Jahr drei neue Mitglieder' — 최근 반년간 새로 합류한 3곳이라는 뜻이며 전체 도입 목록이 아니다. 게다가 세 곳 중 'Code for Hamburg'는 도시가 아니라 시빅테크 자원봉사 단체다.
- CityScope '개별 배치 연도는 공개 개요에 명시되지 않음'은 오류. 같은 MIT 페이지가 'Since 2013, CityScope deployments took place in the Riyadh, Shanghai, Andorra, Boston, Helsinki, and Hamburg'라고 적는다.
- CityScope '개별 도시 배치가 상설 행정 도구로 정착한 기록은 확인되지 않는다. 워크숍 장치로 남았다'는 인용 출처와 상충. 같은 MIT 페이지는 'In some cases, such as in Andorra, Hamburg, or Boston, CityScope is in active use by both stakeholders and communities'라고 적는다(출처를 반박 없이 뒤집었다).
- CityScope 배치 도시 목록 '미국 케임브리지·보스턴, 프랑스 파리, 중국 상하이, 독일 함부르크'는 불완전. 동일 페이지들이 UAE/리야드, 안도라, 헬싱키, 타이베이, 하르키우(Kharkiv Masterplan Visualization Tool)를 함께 명시한다.
- PLATEAU bz25-05 '실내 콜로컬라이제이션'은 오역. 원문은 '屋内測位機能（コアロケーション、Wi-Fi、Beacon等）' — コアロケーション은 Apple CoreLocation이며 co-localization이 아니다. 또 '실외 GPS'는 페이지에 없는 서술이다.
- PropTech Innovation Fund 'R1 13개 지자체 £1,166,418' 부정확. localdigital.gov.uk/funding/ 는 라운드1을 13개 '프로젝트'(£1,166,418)로 적는다(지자체 수가 아님).
- PropTech 'R3~6 37개 이상 시범사업'은 혼동. 실제로는 R3 15개 프로젝트/27 LPA(£3.2m), R4 37개 파일럿/49 LPA, R4-continuous 12개/22 LPA, R5(£1.2m), R6 11개 파일럿/28 기관이다. 37은 R4 단일 라운드 수치이며, R3~R6 합계는 75건 이상이다. 아울러 '예산 배정 내역 공개'라 하면서 공개된 R3(£3.2m)·R5(£1.2m) 총액을 누락했다.
- (외 17건)

## outdoor_research
항목 18개 · 검증 정정 지적 60건

> 야외 경관 AR의 실상은 브리핑의 예상과 다르다. 지목된 기관 중 Wageningen·TU München·UCL Bartlett CASA·Harvard GSD·SLU/Lund에서는 옥외 경관 AR 프로젝트를 특정할 수 없었다(Crossref·OpenAlex 기관 필터 교차검색 결과 해당 소속의 경관 AR 논문 0건). 반면 실제로 15년 이상 축적을 가진 곳은 목록에 없던 두 곳이다. 오사카대학 Fukuda Tomohiro·Yabuki Nobuyoshi 연구실(2010~2026)이 세계 유일의 연속적 옥외 경관 AR 프로그램이고, 셰필드대학 조경학과 Eckart Lange·Sigrid Hehl-Lange 그룹(2018~2023)이 그 다음이다. 초기 원점은 2005년 남호주대학 ARVino(포도밭 삼각대 AR)와 2008년 멜버른대학 Ghadirian & Bishop이다.  ETH Zürich는 경관 시각화의 기함이지만 AR을 택하지 않았다. LVML은 2023년 Design++로 편입되며 명칭조차 'Landscape Visualization'에서 'Large-scale Virtualization'으로 바뀌었고, 풍력 평가는 Manyoky·Wissen Hayek의 GIS 기반 시청각 3D 시뮬레이션(데스크톱·VR)으로 갔다. ETH의 실제 AR은 산림 생물다양성 쪽(HoloFlora, 2025)에서 나왔다.  풍력·송전 경관영향 사전 시각화 — 브리핑이 "실무 수요가 확실한 영역"으로 본 곳 — 이 가장 의외다. 돈이 실제로 움직인 독일 사례(Dezent Zivil, Elzach, Eltville)는 AR을 쓰지 않았다. 전부 360° 사진 파노라마와 음향 시뮬레이션이다. 풍력 VIA에 AR을 쓴 시도는 ETH의 2016년 개념 논문과 글래스고대학의 2015년 학회 슬라이드(비심사) 둘뿐이다. 그리고 AR의 효과를 정면으로 검증한 Rannow 등(2023)은 AR이 정적 사진·텍스트보다 낫지 않았다고 보고했다. 역사적 도구 계보(Lenné3D/Biosphere3D, Visual Nature Studio, Virtual Terrain Project)는 모두 AR이 아니며 일부는 접혔다. 지금 살아 움직이는 옥외 환경 AR의 중심은 경관 설계가 아니라 산림 계측이다(COST Action ARiF, Arboreal 등 상용 앱).


### 오사카대학 Fukuda–Yabuki 연구실의 옥외 경관 AR 장기 프로그램 (SOAR, 불가시 높이 평가 시스템 등)
| 항목 | 내용 |
| --- | --- |
| 주체 | 오사카대학 대학원 공학연구과 지속가능에너지·환경공학 전공(Division of Sustainable Energy and Environmental Engineering). Nobuyoshi Yabuki 교수, Tomohiro Fukuda 교수. 2010년 논문 공동저자 Kyoko Miyashita는 효고현 국토정비부 지역재생국 도시정책과 소속. |
| 도시·연도 | 일본 오사카(스이타시 야마다오카) 및 효고현. 2010~2026년 |
| 증거 수준 | 연구 프로토타입. 다만 2010년 논문은 효고현 공무원이 공동저자여서 행정 실무 문제의식이 직접 반영됐다. 실제 심의 절차에 제도적으로 채택됐다는 증거는 찾지 못했다. |
| AR 여부 | AR 맞음. 실외 실제 시야에 가상 형상을 정합해 겹치는 것이 연구의 핵심 주제 그 자체이고, 정합 정확도·차폐 처리가 반복되는 연구 대상이다. |
| 규모 | 논문 단위 프로토타입. 2010년 논문 피인용 56~64회, 2014년 정합 정확도 논문 15회. 대상지 규모·참여 인원·예산은 공개 서지정보로 확인 불가. |
| 기술 | 초기에는 GPS+자세센서 기반 마커리스 옥외 AR(핸드헬드·타블렛), 2014년 정합 정확도 개선, 2019년 이후 의미분할(semantic segmentation) 기반 동적 차폐 처리, UAV 연동, 실시간 반사 렌더링, 2026년 단안 깊이추정. 데이터는 도시 3D 모델·GIS. |
| 출처 | Yabuki, Miyashita, Fukuda, Automation in Construction 20(3), 2011 https://doi.org/10.1016/j.autcon.2010.08.003 · Fukuda, Zhang, Yabuki, Frontiers of Architectural Research 3(4), 2014 https://doi.org/10.1016/j.foar.2014.08.003 · Fukuda 외, SOAR, CAADRIA 2012 https://doi.org/10.52842/conf.caadria.2012.387 · Kido, Fukuda, Yabuki, eCAADe/SIGraDi 2019 https://doi.org/10.5151/proceedings-ecaadesigradi201 |

세계에서 가장 오래 끊기지 않고 이어진 옥외 경관 AR 연구 계보다. 출발점은 2010~2011년 Automation in Construction에 실린 '불가시 높이 평가 시스템'이다. 경관 보전을 위한 건축물 높이 규제를 현장에서 검증하는 것이 목적으로, 규제 한도만큼의 가상 볼륨을 실제 시야에 겹쳐 '보이면 안 되는 높이'를 눈으로 확인하게 했다. 공동저자에 효고현(兵庫県) 국토정비부 지역재생국 도시정책과 소속 연구자가 들어가 있다는 점이 중요하다. 순수 학술 호기심이 아니라 지방정부의 경관 심의 실무에서 나온 문제였다는 뜻이다. 이후 2012년 SOAR(센서 지향 모바일 AR), 2014년 핸드헬드 AR의 정합 정확도 개선, 2019년 의미분할 기반 동적 차폐 처리, 같은 해 UAV 연동 경관 원격 시뮬레이션, 2021~2022년 실시간 반사 구현으로 이어졌고 2026년에는 항공 시점 단안 깊이추정 기반 실시간 AR까지 나왔다. 16년간 같은 문제 — 옥외에서 가상 경관을 실제 경관에 정확히 겹치는 일 — 를 붙잡고 있다.

연구는 지금도 계속된다(2026년 Engineering Applications of AI 게재). 그러나 상용 제품이나 제도화된 심의 도구로 전환된 증거는 없다. 16년간 프로토타입 단계에 머물러 있는 셈이다.

### 도시 디지털트윈 기반 미래 경관 가시화 — AR·드론 통합과 3D 모델 기반 차폐 처리
| 항목 | 내용 |
| --- | --- |
| 주체 | Naoki Kikuchi, Tomohiro Fukuda, Nobuyoshi Yabuki. 오사카대학 대학원 공학연구과 지속가능에너지·환경공학 전공. |
| 도시·연도 | 일본 오사카. 2021~2022년 |
| 증거 수준 | 연구 프로토타입. 검증 실험까지 수행했으나 실제 주민설명회나 인허가 절차에 투입된 기록은 논문에 없다. |
| AR 여부 | AR 맞음. 실세계 영상에 3D 모델을 정합해 겹치고, 실물과의 전후 관계(차폐)를 실제 도시 3D 모델로 계산한다. 디지털트윈을 데이터 소스로 쓸 뿐 결과물은 AR이다. |
| 규모 | 프로토타입 1건 + 검증 실험. 피인용 82회(2026년 9월 기준)로 이 분야에서 이례적으로 높다. 대상지 면적·참여 인원·예산은 미공개. |
| 기술 | 옥외 AR + 드론(공중 시점) + 도시 디지털트윈 3D 모델. 3D 모델 기반 차폐 처리(IoU 0.8), 30fps, 지연 3초, 인터넷 기반 클라이언트-서버 구조. |
| 출처 | Kikuchi, Fukuda, Yabuki, Journal of Computational Design and Engineering 9(3), 2022 https://doi.org/10.1093/jcde/qwac032 (오픈액세스) · 선행 발표: eCAADe 2021 https://doi.org/10.52842/conf.ecaade.2021.2.521 |

같은 오사카대학 연구실에서 나온 기술적 정점이다. AR과 드론을 결합해 지상 1인칭 시점과 조감(bird's-eye) 시점 양쪽에서 과거·미래 경관을 실세계에 겹쳐 보게 했다. 해결한 문제는 옥외 AR의 고질병인 차폐(occlusion)다. 가상 건물·식재가 실제 전경 물체 앞에 잘못 떠 보이는 현상을 도시 3D 모델을 깊이 기준으로 써서 잡았다. 검증 실험에서 차폐 처리 정확도는 IoU(intersection over union) 약 0.8, 전체 프레임레이트 30fps, 조작기와 기기 사이 지연 3초를 기록했다. 인터넷 기반 아키텍처로 드론과 AR을 묶어, 현장에 있는 사람과 원격에 있는 사람이 웹 브라우저로 같은 미래 경관을 동시에 볼 수 있게 설계했다. 목적은 전문가가 아닌 시민이 도시 설계 의사결정에 참여하게 하는 것이었다.

논문으로 남고 연구 계보는 이어졌다. 2021년 eCAADe 발표를 거쳐 2022년 저널 게재. 제품화·실무 도입 증거는 없다.

### Mobile Augmented Reality for Flood Visualisation (셰필드대학 조경학과)
| 항목 | 내용 |
| --- | --- |
| 주체 | Paul Haynes, Sigrid Hehl-Lange, Eckart Lange. University of Sheffield, Department of Landscape(현 Department of Landscape Architecture), The Arts Tower 13층. |
| 도시·연도 | 영국 셰필드. 2018년(투고 2017년) |
| 증거 수준 | 연구 프로토타입 + 소규모 전문가 사용자 연구. 실제 홍수위험관리 업무에 납품된 것은 아니다. |
| AR 여부 | AR 맞음. 현장 실세계 영상에 가상 수면을 정합해 겹친다. |
| 규모 | 프로토타입 1건, 물 전문가 대상 소규모(small) 사용자 연구. 정확한 참여 인원·예산은 서지정보로 확인 불가. 피인용 108회. |
| 기술 | 모바일 스마트기기 기반 AR(전용 HMD 아님), 현장 콘텐츠 저작 기능, 라이브 센서 데이터 네트워크 연동, 기존 기술 조합으로 구현 복잡도를 낮추는 전략. |
| 출처 | Haynes, Hehl-Lange, Lange, Environmental Modelling & Software 109, 2018, pp.380-389 https://doi.org/10.1016/j.envsoft.2018.05.012 · PDF https://www.sciencedirect.com/science/article/pii/S1364815217302529/pdf |

조경학과가 직접 만든, 현장에서 작동하는 모바일 AR 홍수 가시화 시제품이다. 핵심은 두 가지다. 첫째, 현장에서 콘텐츠를 저작(on-site content authoring)한다 — 사무실에서 미리 만들어 온 장면을 재생하는 게 아니라 현장에 서서 침수 수위를 얹는다. 둘째, 실시간 센서 값을 네트워크로 받아 주석으로 붙인다. 즉 가상 수면이 실제 수위계 데이터에 연동된다. 연구팀은 이것을 기존 홍수위험관리(FRM) 도구를 대체하는 게 아니라 보완하는 것으로 위치시켰고, 물 분야 전문가들을 대상으로 소규모 사용자 연구를 수행해 어떻게 평가받는지를 확인했다. 논문은 '환경 계획·설계를 위한 모바일 AR은 거의 손대지 않은 영역'이라는 문장으로 시작한다. 2018년에도 그랬다는 뜻이다.

이 분야에서 가장 많이 인용되는 조경 AR 논문 중 하나가 됐다(108회). 그러나 도구로 제품화되지 않았고, 후속 연구는 현장 AR이 아니라 탁상(지도 위) AR 쪽으로 방향을 틀었다 — 다음 항목 참조.

### 적응형 시각화 프레임워크와 탁상 AR — Pazhou Island 사례 (셰필드대학)
| 항목 | 내용 |
| --- | --- |
| 주체 | Adam Tomkins, Eckart Lange. University of Sheffield, Department of Landscape Architecture. Lange는 2023년 논문 시점에 Hamburg Institute for Advanced Study 겸직. |
| 도시·연도 | 영국 셰필드(연구), 중국 광저우 파저우섬(사례지). 2019년, 2023년 |
| 증거 수준 | 연구 프로토타입. 2023년 논문은 이론 프레임워크 + 사례 적용이며, 실제 발주된 설계 프로젝트의 납품물은 아니다. |
| AR 여부 | 부분적. 실세계 정합이 맞지만, 정합 대상이 실제 경관이 아니라 워크숍 탁자 위의 지도·모형이다. 옥외 현장 AR이 아니라 실내 탁상형 AR이다. 이 구분은 이 책에서 분명히 밝혀야 한다. |
| 규모 | 2019년 논문 피인용 28~31회, 2023년 논문 5회. 워크숍 참여 인원·예산은 확인 불가. |
| 기술 | 탁상 지도 위 3D 카토그래픽 AR, 실시간 다중사용자 협업, 홍수 시나리오 가시화. 구체적 SDK·기기는 확인하지 못했다. |
| 출처 | Tomkins & Lange, Multimodal Technologies and Interaction 3(2):43, 2019 https://doi.org/10.3390/mti3020043 · Tomkins & Lange, Land 12(2):377, 2023 https://doi.org/10.3390/land12020377 (PDF https://www.mdpi.com/2073-445X/12/2/377/pdf) |

앞의 현장 AR 이후 같은 그룹이 택한 방향이다. 2019년 논문에서 이들은 이해관계자 참여 워크숍의 전통적 지도 작업을 AR로 보강하는 도구를 제시했다. 실제 경관에 겹치는 것이 아니라, 워크숍 탁자 위의 지도에 3D 지도 시각화를 겹치고 여러 사람이 동시에 실시간으로 경관 개입 설계와 홍수 가시화를 수행하게 한다. 2023년에는 이를 '적응형 시각화(Adaptive Visualization, AV)' 이론 프레임워크로 정리했다. 그 논지가 흥미롭다 — 시각화 결과물이 너무 자주 '정적인 산출물'로 취급되는데, 이는 사용된 아날로그·디지털 기술 자체의 제약 때문이었고, 이제는 상호작용적으로 진화하는 도구가 될 수 있다는 것이다. 실증 사례지는 중국 광저우 주강삼각주의 파저우섬(Pazhou Island)이며 주제는 홍수 위험 저감이었다.

연구는 이어지고 있으나 셰필드 그룹의 무게중심이 옥외 현장 AR에서 실내 탁상 AR로 이동했다는 점이 관찰된다. 야외 정합의 어려움을 우회한 선택으로 읽힌다.

### Integration of augmented reality and GIS — 경관 AR의 학술적 원점
| 항목 | 내용 |
| --- | --- |
| 주체 | Payam Ghadirian, Ian David Bishop. Department of Geomatics, The University of Melbourne, 호주. |
| 도시·연도 | 호주 멜버른. 2008년 |
| 증거 수준 | 연구 프로토타입. 개념·방법 제안과 구현 수준이며 실무 납품 사례가 아니다. |
| AR 여부 | AR 맞음. 제목과 주제 자체가 실세계 영상에 GIS 데이터를 겹쳐 사실적 경관 시각화를 만드는 것이다. |
| 규모 | 논문 1편, 피인용 112회. 대상지·예산 미공개. |
| 기술 | AR + GIS 통합. 2008년 기술 환경이므로 GPS·방위센서 기반 옥외 AR로 추정되나, 원문을 열람하지 못해 기기·정합 방식을 단정하지 않는다(오픈액세스 아님). |
| 출처 | Ghadirian & Bishop, Landscape and Urban Planning 86(3-4), 2008, pp.226-232 https://doi.org/10.1016/j.landurbplan.2008.03.004 · 후속 방향: Pettit, Bishop, Sposito, Aurambout, Landscape Ecology 27, 2012 https://doi.org/10.1007/s10980-012-9716-5 |

경관 분야에서 AR과 GIS의 결합을 정면으로 다룬 최초의 주요 논문이다. Landscape and Urban Planning에 실렸고 피인용 112회로, 이후 거의 모든 경관 AR 연구가 인용하는 출발점이 됐다. 저자들은 멜버른대학 지오매틱스학과 소속으로, Ian Bishop은 1990년대부터 경관 시각화와 가상환경 연구를 이끌어 온 이 분야의 1세대다. 이 논문의 위치를 정확히 이해하는 것이 중요하다 — 2008년이라는 시점은 iPhone 3G가 나온 해이고 ARKit·ARCore는 각각 9년·10년 뒤의 일이다. 즉 이 논문은 기술이 준비되기 전에 문제를 정의한 논문이다. Bishop 그룹은 이후 AR보다 다중스케일 기후변화 시각화, 온라인 경관계획 데이터 전달 쪽으로 이동했다.

분야의 정초 논문으로 남았다. 그러나 이 계보가 멜버른대학에서 지속적 옥외 경관 AR 프로그램으로 발전한 흔적은 없다. Bishop은 이후 기후변화 시각화·온라인 계획도구로 옮겼다(Pettit, Bishop 외, Landscape Ecology 2012).

### ARVino — 포도밭 GIS 데이터의 옥외 AR 가시화
| 항목 | 내용 |
| --- | --- |
| 주체 | G. R. Gnana King, Wayne Piekarski, Bruce H. Thomas. Wearable Computer Laboratory, School of Computer and Information Science, University of South Australia, Mawson Lakes. |
| 도시·연도 | 호주 남호주주(University of South Australia, Mawson Lakes). 2005년 |
| 증거 수준 | 연구 프로토타입 + 전문가 리뷰. 상용화나 재배농가 납품은 아니다. |
| AR 여부 | AR 맞음. 옥외 실제 포도밭 시야에 GIS 레이어를 정합해 겹친다. 'outdoor augmented reality'가 제목에 명시돼 있다. |
| 규모 | 프로토타입 1대, 전문가 리뷰 평가. 참여 전문가 수·예산은 확인 불가. 피인용 70회. |
| 기술 | 삼각대 거치식 이동형 옥외 모바일 컴퓨터, 옥외 AR 플랫폼, 3D GIS 데이터 가시화. 정합은 당시 기술상 GPS+자세센서 기반으로 추정되나 원문 미열람. |
| 출처 | King, Piekarski, Thomas, Proc. ISMAR 2005 (4th IEEE/ACM Int. Symp. on Mixed and Augmented Reality) https://doi.org/10.1109/ismar.2005.14 |

야외 환경 AR의 가장 이른 실물 구현 중 하나다. 남호주대학 웨어러블 컴퓨터 연구실이 만들었고, 포도재배(viticulture) GIS 데이터를 포도밭 현장에서 3D로 겹쳐 보게 했다. 재배자는 수확량과 포도 품질에 영향을 주는 변수들을 GIS로 관리하는데, 그것을 사무실 모니터가 아니라 밭에 서서 보면 유용하다는 것이 동기였다. 시스템은 삼각대 위에 올린 이동식 옥외 모바일 컴퓨터로 구성됐다 — 2005년에 사람이 들고 다닐 수 있는 옥외 AR 장비는 없었다는 뜻이다. 논문이 정직한 점은 '구현 중 마주친 몇 가지 문제들(some problems that were encountered)'을 따로 서술하고, 평가를 사용자 실험이 아니라 전문가 리뷰(expert review)로 한정했다는 것이다. 피인용 70회.

제품화되지 않았다. 남호주대학 웨어러블 컴퓨터 연구실은 이후 옥외 AR 일반 기술로 방향을 넓혔고, 경관·농업 AR 계보로 이어지지 않았다. 2005년의 삼각대 AR이 21년 뒤에도 실무 도구가 되지 못한 것이 이 분야의 속도를 보여준다.

### 3D augmented reality for improving social acceptance and public participation in wind farms planning (ETH Zürich)
| 항목 | 내용 |
| --- | --- |
| 주체 | Stefano Grassi (Institute of Cartography and Geoinformation, ETH Zürich), Thomas M. Klein (Planning of Landscape and Urban Systems, ETH Zürich). 스위스 취리히 Stefano-Franscini-Platz 5. |
| 도시·연도 | 스위스 취리히. 2016년 |
| 증거 수준 | 연구 프로토타입 또는 개념 제안. 학술대회 논문집(Journal of Physics: Conference Series)이며 IOP가 봇 차단으로 전문 열람을 막아 구현 수준을 확인하지 못했다. 공공 시범사업이라는 증거는 없다. |
| AR 여부 | AR로 표방하고 있으나 부분적. 초록은 '3D 동적 상호작용 플랫폼과 AR의 장점을 서술한다(describe the advantages)'는 개념 제시형 표현이고, 실제 옥외 정합 구현·검증 여부를 원문에서 확인하지 못했다. AR로 단정하지 않는다. |
| 규모 | 논문 1편, 피인용 12~17회. 대상지·참여 인원·예산 미공개. |
| 기술 | 3D 동적 상호작용 플랫폼 + AR. 구체적 기기·SDK·정합 방식은 전문 미열람으로 확인 불가. |
| 출처 | Grassi & Klein, Journal of Physics: Conference Series 749:012020, 2016 https://doi.org/10.1088/1742-6596/749/1/012020 |

풍력 경관영향에 AR을 적용하려 한, 확인 가능한 가장 명확한 학술적 시도다. 저자들은 풍력의 가장 큰 걸림돌이 경관에 대한 시각적 영향과 '이 사업이 불공정하다'는 지역 인식이라고 진단했다. 그리고 문제의 본질을 커뮤니케이션 도구의 부재로 규정했다 — 개발사, 지역 주민, 행정, NGO 사이에 투명하고 효율적인 상호작용을 가능하게 하는 계획·소통 수단이 없다는 것이다. 특히 '대안 배치안(alternative layouts)을 효과적으로 시각화하는 데 결정적 공백이 있다'고 짚었다. 제안은 3D 동적 상호작용 플랫폼과 AR을 계획가 지원 도구로 쓰자는 것이었다. 저자 두 사람의 소속이 의미심장하다 — 한 사람은 ETH 지도·지리정보연구소(IKG), 한 사람은 ETH 경관·도시시스템계획 교수단(PLUS)이다. 즉 지리정보 쪽과 경관계획 쪽이 만난 지점에서 나왔다.

이 계보가 ETH에서 이어지지 않았다. 같은 기간 ETH의 풍력 경관평가 주력은 AR이 아니라 GIS 기반 시청각 3D 시뮬레이션(데스크톱·VR)이었고, ETH의 실제 AR 구현은 10년 뒤 산림 생물다양성 쪽(HoloFlora)에서 나왔다. 사실상 단발 시도로 끝났다.

### HoloFlora — 혼합현실 기반 산림 생물다양성 지표 가시화 (ETH Zürich)
| 항목 | 내용 |
| --- | --- |
| 주체 | Cyprien R. Fol, Jiayan Zhao, Leonhard Späth, Arnadi Murtiyoso, Fabio Remondino(FBK Trento), Verena C. Griess. ETH Zürich Forest Resources Management 중심. 윤리심의: ETH Zurich Ethics Commission EK-2024-N-88 (2024년 5월 18일 승인). |
| 도시·연도 | 스위스 바덴(Baden) 마르텔로스코프, 취리히. 2024~2025년 |
| 증거 수준 | 연구 프로토타입 + 전문가 휴리스틱 평가·포커스그룹. 상용 제품 없음. 논문은 '현재 산림용 전용 상용 MR 솔루션은 존재하지 않는다'고 명시했다. |
| AR 여부 | AR(MR) 맞음. 실제 숲 현장에서 실제 나무 줄기에 가상 정보를 센티미터급으로 정합해 겹친다. 이 축에서 정합 정확도가 수치로 검증된 유일한 사례다. |
| 규모 | 대상지: 스위스 바덴 마르텔로스코프의 서식처목(habitat tree). 전문가 평가 3명(TreM 식별 전문가), 5분 기록 구간 기하오차 측정. 예산 미공개. 조회 8,907회·피인용 7회(2026년 9월 기준). |
| 기술 | Microsoft HoloLens 2(시투과형 MR HMD), MRTK2 툴킷, Unity 엔진, Immersal 공간지도(VPS) 기반 정합. 입력 데이터는 3D 점군(사진측량). 검증은 M3C2 다중스케일 모델간 점군 비교. 정확도 평균 0.2cm / 표준편차 1.4cm. |
| 출처 | Fol, Zhao, Späth, Murtiyoso, Remondino, Griess, Scientific Reports 15:15908, 2025년 5월 7일 https://doi.org/10.1038/s41598-025-00285-y (오픈액세스) · 관련 VR 연구: Hu, Fol, Chou, Griess, Kakehi, 'Immersive flora', CHI 2024 https://doi.org/10.1145/3613905.3648675 |

ETH Zürich에서 실제로 야외에 나가 작동한 AR/MR 시스템이다. 목적은 산림 생물다양성 평가다. 수목 미소서식처(TreMs, tree-related microhabitats)를 실제 나무 줄기 위에 3D 홀로그램과 텍스트로 겹쳐, 관찰자 편향을 줄이고 생태적 특징을 현장에서 공간적으로 맥락화한다. 연구진은 이것을 '나무 줄기에 생물다양성 지표를 가시화하는 최초의 상호작용형 MR 애플리케이션'으로 규정했다. 성과의 핵심은 정합 정확도다. 가상 요소와 실물의 대응점 간 평균 거리 0.2cm, 표준편차 1.4cm를 달성했다 — 숲이라는 최악의 정합 환경에서 센티미터급이다. 검증은 M3C2 기법으로 밀집 사진측량 점군을 기준 삼아 수행했다. 대상지는 스위스 바덴(Baden)의 마르텔로스코프(marteloscope, 시범 간벌 훈련림)다. 논문이 정직한 점: 전문가 평가 참여자는 단 3명이고, 그것이 휴리스틱 평가에 적합한 규모라는 근거를 따로 밝혔다. 그리고 한계로 '드문드문한 광량 변화에서 트래킹 불안정'을 명시했다.

2025년 5월 Scientific Reports 게재. 전문가 3명 모두 MR의 장래성에 동의했고 한 대학 강사는 교육과정에 넣겠다고 했다. 반면 확인된 한계는 명확하다 — 광량 변동에 따른 트래킹 불안정, 좁은 시야각(수관 같은 큰 부위 평가 시 특히), 기상 조건 적응성. 전문가 중 한 명은 '이런 통합이 자연과의 연결을 오히려 바꿔버릴 수 있다'는 우려를 제기했다. 방법론은 Unity 기반으로 플랫폼 독립적이어서 일반화 가능성이 높다고 저자들은 평가했다.

### ETH Zürich LVML / PLUS — 경관 시각화의 기함이 AR을 택하지 않은 경우
| 항목 | 내용 |
| --- | --- |
| 주체 | ETH Zürich. PLUS(Planning of Landscape and Urban Systems, IRL 소속) — Adrienne Grêt-Regamey 교수. LVML — D-ARCH·D-BAUG 공동 운영, 2023년부터 Design++ 편입. 풍력 시청각 연구: Madeleine Manyoky, Ulrike Wissen Hayek(ETH), Kurt Heutschi, Reto Pieren(Empa). |
| 도시·연도 | 스위스 취리히. 2011~2026년(LVML 명칭·소속 변경 2023년) |
| 증거 수준 | 실제 납품·준공에 준함(상설 연구 인프라). 랩은 D-ARCH와 D-BAUG가 공동 설치·운영하며 ETH Hönggerberg HIL H층에 물리적 공간(AudioVisual Room HIL H40.5, Computer Room HIL H40.8)을 갖고 있다. |
| AR 여부 | 아님(VR). LVML의 가상화 인프라는 명시적으로 virtual reality이고, PLUS의 AudioVisual Lab도 VR 시스템이다. Manyoky 등의 풍력 시청각 시뮬레이션도 AR이 아니다. 이 구분을 흐리면 안 된다. |
| 규모 | 상설 랩 2개 공간(HIL H40.5, H40.8). Manyoky 외 2014년 논문 피인용 35회, Wissen Hayek 2011년 논문 45회, Neuenschwander·Wissen Hayek·Grêt-Regamey 2014년 논문 54회. 예산 미공개. |
| 기술 | 레이저스캐닝·사진측량·음향 녹음·소음강도·온도 측정 기반 디지털화, 점군 모델링, GIS, VR 시각화 + 음향화(auralization). 풍력은 GIS 기반 시각-음향 3D 시뮬레이션. |
| 출처 | PLUS 연구 소개 https://plus.ethz.ch/research.html · LVML https://lvml.ethz.ch/ · Manyoky, Wissen Hayek, Heutschi, Pieren, ISPRS Int. J. Geo-Information 3(1):29, 2014 https://doi.org/10.3390/ijgi3010029 · Wissen Hayek, Environment and Planning B 38, 2011 https://doi.org/10.1068/b36113 · Neuenschwander, Wissen Hayek, Grêt-Regamey, Computers, Environment and Urban Systems 48, 2014 https://doi.org/10.1016 |

이 항목은 '있는 것'이 아니라 '없는 것'을 기록하기 위한 것이다. ETH Zürich는 유럽 경관 시각화 연구의 중심이다. PLUS(Planning of Landscape and Urban Systems, Adrienne Grêt-Regamey 교수단)는 참여형 경관계획을 위해 사람의 경관 인지를 인지심리학 방법으로 측정하며, AudioVisual Lab에서 VR 시스템으로, Mobile Visual-Acoustic Lab으로 생리·인지 반응을 기록한다. 그런데 이 모든 인프라가 VR과 음향화(auralization)다. AR이 아니다. LVML 자체의 변화가 상징적이다. 원래 'Landscape Visualization and Modeling Lab'이던 이름이 현재 'Large-scale Virtualization and Modeling Lab'이고, 2023년부터 부서 간 이니셔티브 Design++에 편입됐다. 랩 소개문은 '가상화(Virtualization)'를 '가상현실을 사용해 기존 및 상상의 환경을 시각화·음향화하는 것'으로 정의한다. 풍력 경관평가의 주력 성과도 Manyoky·Wissen Hayek 등의 GIS 기반 시청각 3D 시뮬레이션이며, 음향은 Empa(스위스 연방재료과학기술연구소)의 Heutschi·Pieren이 맡았다 — 데스크톱·몰입형이지 현장 정합 AR이 아니다.

지금도 활발히 운영된다. 다만 방향은 AR이 아니다. 이름에서 'Landscape'가 빠지고 'Large-scale Virtualization'이 들어간 것, 2023년 Design++로 편입된 것은 경관 전용 시각화 랩에서 범용 디지털 설계 인프라로 성격이 옮겨간 흔적으로 읽힌다. ETH에서 실제 야외 AR이 나온 곳은 경관계획이 아니라 산림자원관리(HoloFlora)였다.

### COST Action CA23135 ARiF — Bringing Digital Data and Reality Together: Augmented Reality in Forestry
| 항목 | 내용 |
| --- | --- |
| 주체 | COST(European Cooperation in Science and Technology) Action CA23135. 리뷰 주저자 Felipe De Miguel-Díez, 책임 Thomas Purfürst(프라이부르크대학 산림작업학 교수단). 참여 기관 예: 프라이부르크대학, 드레스덴공대, 파도바대학, 폴란드과학원 수목학연구소, 바야돌리드대학, 동핀란드대학, 포즈난생명과학대학, 이즈미르카티프첼레비대학, 리스본대학, 트벤테대학, 불가리아과학원, 우크라이나생명환경과학대학, 이탈리아 CNR-IBE, IIASA, WSL 등. |
| 도시·연도 | 유럽 11개국(본부 성격의 조정은 독일 프라이부르크). 2024~2028년 |
| 증거 수준 | 공공 연구 프로그램(EU COST Action). MoU 048/24, CSO 승인 2024년 5월 17일, 시작 2024년 9월 26일, 종료 2028년 9월 25일. 산하 개별 프로젝트는 연구 프로토타입~상용 제품이 섞여 있다. |
| AR 여부 | AR 맞음. 프로그램 정의 자체가 실세계 중심을 유지하며 디지털 콘텐츠로 보강하는 것이고, 실시간 상호작용·공간 정합·안정적 트래킹을 핵심 기술 요건으로 명시한다. |
| 규모 | 11개국 23명 공동저자, 25년치 문헌·회색문헌·상용도구 대상. 부속 연구비: 독일 BMEL/FNR 과제번호 2223NR030X(ForestAR), 바덴뷔르템베르크 재단 WaldAgil 과제 KLR-030. 그 밖에 불가리아 '산림에서의 AR 기술·시스템 적용' 과제, 오스트리아 Citizens for Copernicus 과제. |
| 기술 | AR 런타임: ARKit, ARCore, AR Foundation, visionOS, Windows MR(MRTK). 엔진: Unity 3D(지배적), Unreal. 점군 렌더러 Pcx. 계측: 원/원통 피팅, SfM, Segment Anything Model(SAM), OpenCV, 경량 CNN, Bitterlich 각산정 알고리즘. 센싱: 스마트폰 LiDAR, RGB-D, SLAM, VIO. |
| 출처 | De Miguel-Díez 외 23인, Current Forestry Reports 12:21, 2026 https://doi.org/10.1007/s40725-026-00283-x (CC-BY, 미러 https://pure.iiasa.ac.at/id/eprint/21787/1/s40725-026-00283-x.pdf) · COST Action 페이지 https://www.cost.eu/actions/CA23135/ · 프로그램 사이트 https://arif-cost.eu · ForestAR 앱: Kushwaha, Rai, Hristova, Sagar, Mokros, Schweier, ISPRS Archives XLVIII-G-2025, pp.831-838 https://doi.org/10.5194/ispr |

야외 환경 AR에서 현재 가장 규모 있는 조직적·장기적 연구 프로그램이다. 유럽 11개국 23명의 공동저자가 참여해 2000~2025년 25년간의 산림 AR을 정리한 리뷰를 2026년에 냈고, 그 리뷰가 이 프로그램의 첫 산출물이다. 결론이 이 책에 그대로 쓸 만하다. 산림 AR은 고립된 프로토타입에서 초기 운용 단계로 넘어가는 중이고, 가장 성숙한 영역은 산림 조사·도시산림·원목 계측이다. 스마트폰·타블렛의 LiDAR, RGB-D, SLAM, 컴퓨터비전을 쓰는 도구들이 중상 수준의 성숙도에 도달했고 일부는 상용화됐다. HMD와 기계 통합 시스템은 임분 시각화, 디지털 수목 표시, 식재 유도, 수확 지원에 시험되고 있으나 대부분 파일럿 단계다. 그리고 결정적 수치 — 대부분의 시스템이 TRL 4~6에 몰려 있고, TRL 7~9에 도달한 것은 제한된 일부뿐이다. 잔존 장벽도 명시했다: 수관 아래 트래킹 불안정, 약한 지리참조, 부족한 견고성과 배터리 수명, 인체공학적 제약, 낮은 상호운용성, 검증 부족.

2028년까지 진행 중. 리뷰의 자기평가가 냉정하다 — '산림 부문은 근본적 발명이 아니라 기술 이전 단계에 있다'. 인접 분야에서 이미 성숙한 것을 산림 특유의 제약(지형, 차폐, 제한된 GNSS와 통신, 안전 중요 작업환경)에 맞추는 것이 과제이고, 산림 사용자 집단을 대상으로 한 효과의 신뢰할 만한 증거 생산이 남았다고 했다. 또한 '상용화되었다는 사실을 보편적 정확도·신뢰성·이전가능성과 동일시해서는 안 된다'고 못 박았다.

### 오스트리아 연방산림청(ÖBf) HoloLens 2 파일럿 및 상용 산림 AR 앱군 (Arboreal, ForestScanner, Forstify, Timbeter)
| 항목 | 내용 |
| --- | --- |
| 주체 | Österreichische Bundesforste(ÖBf, 오스트리아 국유 산림기업) + D. Lepizh. Arboreal AB(스웨덴, Johan Ekenstedt). Forstify Digital GmbH(독일, Christian Kaulich). Timbeter(에스토니아). ForestScanner: Tatsumi, Yamaguchi, Furuya(일본). Skogforsk(스웨덴 산림연구소): Englund, Lundström, Brunberg, Löfgren. Optea AB(스웨덴, Esteban Arboix). |
| 도시·연도 | 오스트리아(ÖBf, 2023), 스웨덴(Arboreal 2018~, Skogforsk), 독일(Forstify), 에스토니아(Timbeter), 일본(ForestScanner). 2018~2026년 |
| 증거 수준 | 혼합. ÖBf는 공공 시범사업(2023년 잠정 평가 보고서). Arboreal·Forstify·Timbeter·ForestScanner는 실제 판매·배포되는 상용 제품(TRL 7~9). Skogforsk HUD와 HoloLens 2 식재 유도는 현장 시험·실험 단계. HoloLens 2 임지경계 가시화는 파일럿. |
| AR 여부 | AR 맞음(대부분). 실제 나무·지면·임지에 가상 계측 링, 경계선, 식재 지점을 정합해 겹친다. 단 원목 더미 계측 앱 일부는 지속적 공간 오버레이가 없고 동일한 모바일 센싱·공간추정 파이프라인을 쓴다는 이유로 'AR 보조(AR-assisted)'로 분류된다 — 리뷰가 직접 그렇게 구분했다. |
| 규모 | Arboreal Forest 2019년 출시. ForestScanner·Arboreal Forest 비교연구에서 흉고직경 추정에 통계적 유의차 없음(둘 다 실측 대비 과소추정 경향). ARKit 기반 구현 R²=0.95, RMSE=2.71cm(414본 대상), ARCore+RGB-D 딥러닝 구현 R²=0.98, RMSE=2.46cm(340본 대상). M-Tree 앱은 85개 대상 RMSE 0.192m. 개별 기업 매출·예산은 미확인. |
| 기술 | 스마트폰·타블렛 LiDAR와 RGB-D, ARKit/ARCore, SLAM, 광학 SLAM + 레이캐스팅, 원/원통 피팅, Bitterlich 각산정 디지털 구현. HMD: Microsoft HoloLens 2(시투과형). 조종실: 반투명 빔스플리터 HUD. Apple Vision Pro도 직경 추정용으로 평가됨. |
| 출처 | Österreichische Bundesforste, Lepizh, 'Hololens 2 & Augmented Reality. Ein vorläufiges Fazit', 2023 (PDF: verwaltungspreis.gv.at) · Arboreal AB https://arboreal.se/en/arboreal-forest · Tatsumi, Yamaguchi, Furuya, ForestScanner · Skogforsk: Englund, Lundström, Brunberg, Löfgren · 종합 출처: Current Forestry Reports 12:21, 2026 https://doi.org/10.1007/s40725-026-00283-x |

야외 환경 AR에서 실제로 돈이 움직이고 제품이 팔리는 유일한 영역이다. 경관 설계가 아니라 나무를 재는 일이다. 국유기업인 오스트리아 연방산림청(Österreichische Bundesforste)은 Microsoft HoloLens 2로 임지 경계와 임분 속성을 현장 지형에 직접 겹쳐 보고, 지리참조된 사진과 공간 고정 주석을 계획용으로 수집했다. 2023년에 '잠정 결론(Ein vorläufiges Fazit)'이라는 제목의 평가 보고서를 냈다. 상용 앱 쪽에서는 스웨덴 Arboreal AB가 중심이다. Arboreal Forest(2019)는 스마트폰 AR과 LiDAR로 흉고직경, 수고, 임분 단면적, 재적, ha당 본수를 추정하며, 가상 줄기 정렬 링을 실제 나무에 겹쳐 비전문가의 진입장벽을 낮췄다. Arboreal Tree Height(2018), 개발 중인 Tree Scanner도 같은 계열이다. 일본에서 나온 ForestScanner는 LiDAR 탑재 iOS 기기로 임분을 걸어 다니며 SLAM 기반 실시간 조사를 한다. 독일 Forstify Digital GmbH는 원목 더미 계측·거래를, 에스토니아 Timbeter는 사진광학 재적 산정을 한다. 스웨덴 Skogforsk는 상용 하베스터 조종실에 반투명 빔스플리터로 조재 정보를 띄우는 HUD를 시험했다. 그리고 HoloLens 2로 식재 열과 개별 식재 지점을 지면에 투사해 조림 작업을 유도하는 실험도 있다.

이 영역만 실제 운용에 들어갔다. 다만 리뷰의 유보가 중요하다 — 상용 앱들도 수종, 줄기 형태, 임분 밀도, 하층 차폐, 육림 체계, 취득 프로토콜에 따라 성능이 달라지며, '규제 등급(regulatory-grade) 계측에는 엄밀한 보정과 불확실성 처리 없이는 불충분하다'. 동일 하드웨어에서도 정확도 변동의 주원인이 센서 품질이 아니라 알고리즘 구현이었다. Skogforsk HUD 현장시험은 유의한 생산성 향상을 보이지 못했고, 조종사들이 개념적으로 직관적이라고 평가한 수준에서 끝났다.

### Tangible Landscape — 물리 모형과 GIS를 결합한 투영식 지형 인터페이스 (NC State University)
| 항목 | 내용 |
| --- | --- |
| 주체 | North Carolina State University, Center for Geospatial Analytics, NCSU GeoForAll Lab. 저자·개발진: Anna Petrasova, Brendan Harmon, Vaclav Petras, Payam Tabrizian(2판 추가), Helena Mitasova. 센터장(Executive Director): Ross Meentemeyer. |
| 도시·연도 | 미국 노스캐롤라이나주 랄리(NC State University). 2015~2026년(2판 2018) |
| 증거 수준 | 연구 프로토타입 + 상설 연구·교육 인프라. 센터는 Geovisualization Lab을 운영하며 온라인 가상 투어(Matterport)까지 제공한다. 타 기관이 자체 제작할 수 있도록 오픈소스 문서와 자문을 제공한다. |
| AR 여부 | 부분적. 투영식 공간 AR(spatial AR)로, 실제 물리적 모래·모형 표면에 정합해 디지털 정보를 겹친다는 점에서 AR이다. 그러나 정합 대상이 실제 대상지 경관이 아니라 실내의 축소 물리 모형이다. 옥외 현장 AR과 혼동하면 안 된다. |
| 규모 | 단행본 1판(2015) 피인용 28회, 2판(2018) 19회. 최근 활동: 2025년 CSDMS(Community Surface Dynamics Modeling System) 학술대회 워크숍, 노스캐롤라이나주 농업 유출수 저감 전략, 병해충 예측 모델링. 설치 대수·예산·참여 인원은 웹페이지에 미공개. |
| 기술 | 3D 스캔(점군 처리)으로 물리 모형 표면을 연속 취득 → GRASS GIS로 지형·수문·화재·확산 모델 계산 → 프로젝터로 모형 표면에 투영. 렌더링은 Blender. 오픈소스. |
| 출처 | 프로젝트 사이트 https://tangible-landscape.github.io/ · NC State 연구 페이지 https://cnr.ncsu.edu/geospatial/research/models-through-tangible-interaction/ · Petrasova, Harmon, Petras, Mitasova, 'Tangible Modeling with Open Source GIS', Springer 2015 https://doi.org/10.1007/978-3-319-25775-4 · 2판(+Tabrizian) 2018 https://doi.org/10.1007/978-3-319-89303-7 |

경관을 손으로 만지면서 지리공간 모델을 실시간으로 돌리는 오픈소스 인터페이스다. 사용자가 물리적 지형 모형을 손으로 조각하면 그 표면을 3D 스캔해 GIS로 넘기고, 물 흐름·침식·일사·침수·화재 확산·병해 확산·도시 성장 같은 프로세스를 계산해 그 결과를 다시 모형 표면에 투영한다. 코딩 없이 복잡한 모델을 조작할 수 있게 하는 것이 목표다. NC State 지리공간분석센터(Center for Geospatial Analytics)의 GeoForAll Lab이 개발했고, GRASS GIS와 Blender로 구동되며 오픈소스로 공개됐다. 2015년 Springer에서 단행본 'Tangible Modeling with Open Source GIS'를 냈고 2018년 2판을 냈다. 연구 초점은 세 갈래다: 직관적 모델링(손으로 복잡한 모델 제어), 인간-컴퓨터 상호작용(유형 사용자 인터페이스와 VR 시각화의 오픈소스 혁신), 학습과 인지(유형 인터페이스가 교육을 어떻게 돕고 인지부하를 줄이는지).

10년 이상 유지되며 지금도 활동 중이다. 단행본 2판까지 나오고 워크숍이 계속되는 것은 이 분야에서 드문 지속성이다. 다만 상용 제품이나 발주된 설계 프로젝트의 납품 도구가 된 증거는 없고, 성격이 연구·교육 인프라에 머문다. 개별 연구자 이름·연구비 과제번호는 센터 웹페이지에서 확인되지 않았다.

### AR Sandbox — 증강현실 모래상자 (UC Davis)
| 항목 | 내용 |
| --- | --- |
| 주체 | 제작: Oliver Kreylos 박사(컴퓨터과학자). 소속: UC Davis DataLab, 이전 소속은 UC Davis W.M. Keck Center for Active Visualization in the Earth Sciences(KeckCAVES). 지원: NSF. 협력: UC Davis Tahoe Environmental Research Center, Lawrence Hall of Science, ECHO Leahy Center for Lake Champlain. |
| 도시·연도 | 미국 캘리포니아 데이비스(UC Davis) 개발, 전 세계 확산. 2012년경~2026년 |
| 증거 수준 | 실제 납품·준공. 전 세계 수천 개 장소에 설치됐다고 UC Davis가 밝히고 있으며(박물관·대학·중고등학교), 알려진 설치 위치를 표시한 인터랙티브 지도를 운영한다. 백악관, USA Science and Engineering Festival, 다수의 국제 학술대회에도 전시됐다. ECHO Lake Aquarium and Science Center에는 '박물관 등급' 사양이 설치돼 있다. |
| AR 여부 | 부분적. 실제 모래 표면에 실시간 정합해 정보를 투영하는 투영식 공간 AR이다. 그러나 대상지 경관이 아니라 실내 모래상자다. 명칭에 AR이 들어 있다는 이유로 옥외 경관 AR 사례로 인용하면 안 된다. |
| 규모 | 전 세계 수천 개 장소 설치. 대상은 초등학생부터 대학생, 연구자, 일반 대중. 개별 설치 비용·총예산·NSF 과제번호는 해당 페이지에서 확인되지 않았다. |
| 기술 | 실제 모래 + Microsoft Kinect 3D 카메라(깊이 센싱) + 데이터 프로젝터 + 오픈소스 시뮬레이션·시각화 소프트웨어. 출력은 표고 색상지도, 등고선, 유체 시뮬레이션(물·용암). |
| 출처 | UC Davis DataLab https://arsandbox.ucdavis.edu/ · 설치 위치 인터랙티브 지도(동 페이지 링크) · 파생: Cortés, Garcia-Castellanos 외, EGU General Assembly 2020 https://doi.org/10.5194/egusphere-egu2020-7069 · Klump 외, EGU 2020 https://doi.org/10.5194/egusphere-egu2020-12020 |

야외 환경 AR 계보에서 가장 널리 퍼진 물건이다. 실제 모래, Microsoft Kinect 3D 카메라, 데이터 프로젝터, 오픈소스 시뮬레이션·시각화 소프트웨어로 구성된다. 사용자가 모래를 손으로 빚으면 그 형상 위에 표고 색상지도, 등고선, 그리고 시뮬레이션된 물(또는 용암)이 실시간으로 투영된다. 유역이 무엇인지 파악하는 것부터 지형도 읽기까지, 지리·지질·수문·화산 개념을 가르치는 것이 목적이었다. NSF(미국 국립과학재단)가 지원한 비형식 과학교육 과제의 일부로 만들어졌고, 협력기관은 UC Davis 타호환경연구센터, Lawrence Hall of Science, ECHO Leahy Center for Lake Champlain이었다. 소프트웨어·튜토리얼·제작 지침을 모두 공개해 누구나 자기 기관에 만들 수 있게 한 것이 확산의 결정적 요인이다.

상태는 'Active'로 표시돼 있고 지금도 유지된다. 이 분야에서 가장 성공적으로 확산된 사례다. 성공 요인이 명확하다 — 값싼 상용 부품(Kinect+프로젝터), 완전 공개된 제작 지침, 그리고 정밀 정합이 필요 없는 문제 설정. 옥외 경관 AR이 실패하는 지점(GNSS 정밀도, 수관 아래 트래킹, 옥외 광량)을 전부 회피했기 때문에 퍼진 것으로 읽힌다. 이것이 이 축에서 가장 중요한 교훈일 수 있다. 다만 파생 연구(EGU 2020년 침식·지형진화 교육, 지구물리·구조지질 확장 등)는 개별 학회 초록 수준에 머문다.

### Lenné3D / Biosphere3D — 독일 경관 시각화 소프트웨어의 26년 계보 (AR 아님)
| 항목 | 내용 |
| --- | --- |
| 주체 | Lenné3D GmbH. 창립 파트너: Philip Paar(초대 대표), Prof. Dr. Oliver Deussen, Prof. Dr. Jürgen Döllner, Hans-Christian Hege, Prof. Dr. Jörg Rekittke, Dr. Wieland Röhricht, Dr. Liviu Coconu, 2006년 Dr. Malte Clasen 합류. 2010년부터 대표 Jochen Mülder(카셀대학 조경계획 전공, 학위논문 주제가 경관계획 시각화 3D 방법들의 지각가능성·이해가능성이었다). Biosphere3D 개발자 Steffen Ernst. |
| 도시·연도 | 독일. 베를린(2005)→함부르크(2012)→빌레펠트(2014~현재). 2000~2026년 |
| 증거 수준 | 실제 납품·준공. 공공기관·지자체·지역계획공동체·엔지니어링사 발주 프로젝트가 약 40건 공개돼 있고 발주처와 수행기간이 명시된다. |
| AR 여부 | 아님. 26년 계보 전체가 3D 경관 시각화, 사진 기반 시뮬레이션, 360° 파노라마, 가상 지구, 그리고 일부 VR(헤로데스 궁전 VR 애플리케이션)이다. 실세계 정합 AR은 프로젝트 목록 전체(약 40건)에 한 건도 없다. 조경 시각화의 주류가 AR이 아니었다는 가장 강한 증거다. |
| 규모 | 공개 프로젝트 약 40건. 그중 풍력 관련이 14건 내외로 가장 많다. 재원: DBU(타당성 연구 2000, 4년 연구과제), BMBF(SILVISIO 3년, RAME). 매출·인원은 미공개. |
| 기술 | Biosphere3D(오픈소스 가상 지구), 사진 기반 3D 시뮬레이션, 사실적 3D 시각화, 4D 애니메이션, 360° 파노라마, 최대 8K 출력, 자유보행 3D 장면, 풍력 음향 시뮬레이션 연계. 식생 렌더링과 식물 분포 방법론이 회사의 고유 기술이다. |
| 출처 | 회사 연혁(1차 자료) https://www.lenne3d.com/history/ · 회사 소개·팀 https://www.lenne3d.com/about/ · 전체 프로젝트 목록 https://www.lenne3d.com/all-projects/ · Biosphere3D https://www.lenne3d.com/biosphere3d-en/ · 대조 사례(역사적 도구, 모두 AR 아님): Visual Nature Studio / 3DNature(현재 AlphaPixel이 발행·지원, VNS 3가 최종 버전, Forestry Edition과 Bighorn National Forest 사례 보유) http://3dnature.com/ · Virtual Terrain Project(활동기간 2001~2013로 스 |

브리핑이 '역사적인 것 포함'으로 지목한 계보이며, 실제 이력이 이례적으로 정확하게 공개돼 있다. 시작은 2000년, 독일연방환경재단(DBU) 지원으로 경관 3D 시각화 전문 소프트웨어의 사용자·잠재사용자를 대표성 있게 설문조사한 타당성 연구였다. 최신 소프트웨어 수요가 확인되자, 라이프니츠 농업경관연구센터(ZALF) 토지이용시스템연구소에 기반을 둔 4년짜리 연구과제가 이어졌고(역시 DBU 지원) 여기서 공간데이터 대화형 시각화 시스템 'Lenné3D'가 개발됐다. 2005년 회사로 분사했다. 모회사가 셋이다 — ZALF(뮌헤베르크), 취제연구소 베를린(ZIB), 하소플라트너연구소(포츠담). 본사는 베를린, 대표는 Philip Paar. 최대 과제는 독일연방교육연구부(BMBF)가 지원한 3년 과제 SILVISIO('숲의 미래를 보이게 하다')였고, 여기서 Lenné3D의 방법론과 소프트웨어가 함께 개발됐다. 오픈소스 가상 지구 Biosphere3D는 ZIB에서 Malte Clasen이 프로그래밍했고 2010년 이후 Lenné3D가 계속 최적화·확장했다.

회사는 지금도 운영된다(2026년 현재). 그러나 두 번의 축소가 기록돼 있다. 첫째, 2007년부터 Esri의 비즈니스 파트너로 ArcGIS Desktop용 플러그인을 여러 버전 개발해 자사의 식물 분포·식물 렌더링 방법을 Esri 제품군에서 쓸 수 있게 했는데, 2015년 플러그인 개발이 중단되고 Esri와의 파트너십이 종료됐다. 둘째, 2010년 창업자 Paar가 대표에서 물러나고 회사는 소프트웨어 개발사에서 프로젝트·서비스 중심 전문업체로 성격이 바뀌었다. 본사도 베를린→함부르크(2010·2012 파트너 구조 변경)→빌레펠트(2014)로 이동했다. 즉 소프트웨어 제품 회사가 되려던 시도는 접혔고, 시각화 용역 회사로 살아남았다.

### Dezent Zivil · Elzach · Eltville — 독일 풍력 경관영향 사전 시각화의 실제 실무 (AR 아님)
| 항목 | 내용 |
| --- | --- |
| 주체 | Dezent Zivil — 발주: 카셀대학 공법(특히 환경·기술법) 교수단(Universität Kassel, Fachgebiet Öffentliches Recht, insb. Umwelt- und Technikrecht). 지원: 독일연방교육연구부(BMBF, 베를린). 시각화: Lenné3D. 가시권 분석: 뉘르팅겐-가이슬링겐대학 Michael Roth 교수. / Eltville — 발주: Dialog Basis(데텐하우젠), 헤센주 위탁. / Elzach — 발주: Forum Energiedialog Baden-Württemberg(로텐부르크 암 네카어). 음향: Möhler + Partner. |
| 도시·연도 | 독일. 쇼프하임-게르스바흐(바덴뷔르템베르크), 엘트빌레 암 라인(헤센), 엘차흐(바덴뷔르템베르크), 라인슈테텐, 남서튀링겐. 2013~2021년 |
| 증거 수준 | 실제 납품. 발주처, 계약 기간, 수행 내역, 협력기관이 모두 명시돼 있고 주민 대상 공개 행사에서 사용됐다. |
| AR 여부 | 아님. 세 사례 모두 사진 기반 360° 파노라마 시뮬레이션과 음향 시뮬레이션이다. 실세계 카메라 영상에 실시간 정합해 겹치는 것이 아니라, 미리 촬영한 파노라마에 풍력발전기를 합성한 뒤 대화형으로 시점을 바꾸게 하는 방식이다. |
| 규모 | Dezent Zivil: 과제 전체 2013-04-01~2016-06-30, Lenné3D 참여 2014-12-01~2016-03-01. 시범지역 쇼프하임-게르스바흐, 풍력단지 2개×5기, 시각화 지점 약 25개, 현장 행사 3회. / Eltville: 2015-03-01~2015-05-01, 주요 시점 5개. / Elzach: 2016-06-01~2016-10-01, 시각 10개·음향 6개(예산 제약으로 축소), 주민 회의 2회. / 추가: 라인슈테텐 풍력 시각화 2021-05-31~2021-08-19(발주 Stadt Rheinstetten), 남서튀링겐 풍력 2020-09-01~2021-02-12(발주 Regionale Planungsgemeinschaft Südwestthüringen). 예산액은 미공 |
| 기술 | 사진 기반 3D 시뮬레이션, 계절별·풍속별 대화형 360° 파노라마, 개요 지도 연동 가상 투어, GIS 기반 가시권 분석, 음향 시뮬레이션(Dezent Zivil에서 검증된 방법론을 Elzach에 재사용), 시각-음향 동기 전환. |
| 출처 | Dezent Zivil https://www.lenne3d.com/energy/3d-simulation-dezent-zivil · Eltville 시민포럼 https://www.lenne3d.com/energy/citizens-forum-eltville · Elzach 시각·음향 시뮬레이션 https://www.lenne3d.com/energy/acoustic-optical-visualisation-wind-turbines · 라인슈테텐 https://www.lenne3d.com/energy/visualisation-wind-turbines-rheinstetten · 남서튀링겐 https://www.lenne3d.com/energy/visualisation-wind-turbines-southwest-thur |

브리핑이 '실무 수요가 확실한 영역'으로 지목한 곳의 실상이다. 독일에서 풍력 경관영향 사전 시각화에 실제로 공적 자금이 투입되고 주민 앞에서 사용된 사례들이며, 전부 AR이 아니다.  Dezent Zivil은 BMBF가 지원한 연구과제로 2013년 4월 1일부터 2016년 6월 30일까지 재생에너지 분야의 계획·인허가 절차와 시민 참여를 조사했다. 시범 지역은 바덴뷔르템베르크주 쇼프하임이었고, 그 자치구 게르스바흐에서 각각 풍력발전기 5기 규모의 서로 다른 두 풍력단지가 동시에 계획되고 있었다. 과제의 목표는 계획에 관여하지 않은 외부 기관이 중립적 시각화·시뮬레이션·분석을 만들어 현장 논쟁을 객관화하는 것이었다. Lenné3D가 2015년 1월부터 참여해 수행한 것은: 현장 주민 면담으로 중요한 시각적 관계를 수집·논의, 게르스바흐 일대 약 25개 지점의 사진 기반 시각화를 계절별 대화형 360° 파노라마로 제작, 개정 중인 토지이용계획에 근거한 풍력 개발 가능 입지 시각화, 현장 3회 행사 발표, GIS 기반 가시권 분석(뉘르팅겐-가이슬링겐대학 Michael Roth 교수 협력), 2015년 여름 두 단지의 음향 영향 분석 추가.  Eltville에서는 헤센주의 '에너지주 헤센' 시민포럼 틀에서, 세계문화유산급 에버바흐 수도원과 라인강 바로 인근의 풍력 확대를 두고 주민투표가 예정돼 있었다. 쟁점은 문화재 보호와 경관이었다. Lenné3D는 수도원 주변 5개 주요 시점의 사진사실적 시뮬레이션을 만들었고, 시민단체가 만든 입지안을 검증하는 역할도 맡았다. 360° 파노라마들을 개요 지도와 함께 가상 투어로 묶어 시점을 대화형으로 바꿀 수 있게 했다.  Elzach에서는 바덴뷔르템베르크주 에너지대화포럼 의뢰로 시각·음향 시뮬레이션을 만들었다. 가장 영향을 받는 두 지구(엘차흐 중심부, 야흐) 주민과의 진행자 중재 회의에서 시점을 수집했고, 예산에 맞춰 시각 10개·음향 6개로 합의해 줄였다. 지형 조건 때문에 가시성이 변동이 심해 Lenné3D가 360° 파노라마를 권고했다. 결과 발표 때 시각과 음향이 약풍·중풍·강풍 사이를 동기적으로 전환됐다.

이것이 이 축에서 가장 중요한 발견이다. 풍력 경관영향 사전 시각화라는, 실무 수요가 가장 확실한 영역에서 실제 선택된 기술은 AR이 아니라 360° 사진 파노라마였다. 이유가 사례 기술에 드러난다 — 지형 때문에 가시성이 변동이 심할 때 '공간적 맥락과 방향 감각을 잃지 않으면서 풍력발전기를 사실적으로 표현'하는 것이 요구였고, 예산 제약으로 시점 수를 협상해 줄여야 했고, 중립적 외부 전문가로서의 신뢰성이 핵심이었다. 사진 기반 파노라마는 이 세 요구를 모두 만족시킨다. 현장 정합 AR은 그중 어느 것도 보장하지 못한다. Lenné3D는 이 방식으로 2016년 이후에도 계속 수주하고 있다(2020년 남서튀링겐, 2021년 라인슈테텐).

### 풍력 VIA용 AR의 효과 검증 시도와 그 결과 — 글래스고대학(2015)과 Rannow 등(2023)
| 항목 | 내용 |
| --- | --- |
| 주체 | Larissa Szymanek, David R. Simmons — University of Glasgow, 영국. / Bailey Rannow, Ingrid E. Schneider, Marcella Windmuller-Campione, Matthew Russell, Angela Gupta — 미네소타대학 계열로 추정되나 소속 원문 미확인. |
| 도시·연도 | 영국 글래스고(2015), 미국 중서부 한 주의 공원(2023) |
| 증거 수준 | 글래스고: 전시·시연 수준(비심사 학회 슬라이드). Rannow 등: 연구 프로토타입 + 현장 무작위 실험(심사 통과, Journal of Outdoor Recreation and Tourism 및 Environmental Management 게재). |
| AR 여부 | AR 맞음(둘 다 AR을 명시적 처리 조건으로 다룸). 다만 글래스고 사례는 슬라이드만 남아 구현 방식·정합 여부를 확인할 수 없다. |
| 규모 | 글래스고: 슬라이드 1건, 1.26MB, 조회 238회·다운로드 16회. / Rannow 등: 공원 방문객 대상 4조건 무작위 배정. 정확한 표본 수·대상지명·예산은 원문 미열람으로 확인하지 못했다. 피인용 3~10회. |
| 기술 | 글래스고: 미확인. / Rannow 등: AR과 VR 메시지 전달물. 기기·SDK 미확인. |
| 출처 | Szymanek & Simmons, F1000Research 4:1020 (slides, not peer reviewed), 2015년 10월 8일 https://doi.org/10.7490/f1000research.1110764.1 · Rannow, Schneider, Windmuller-Campione, Russell, Gupta, Journal of Outdoor Recreation and Tourism 42:100640, 2023 https://doi.org/10.1016/j.jort.2023.100640 · 관련: Schneider 외, Environmental Management, 2023 https://doi.org/10.1007/s00267-023-01787-z · 인용 맥락: Current  |

AR이 야외 환경 의사결정에서 실제로 더 나은가를 정면으로 물은 두 시도이며, 둘 다 약하게 끝났다. 이 책의 신뢰는 여기에 달려 있다.  첫째, 글래스고대학의 Larissa Szymanek과 David R. Simmons는 '풍력발전 개발의 시각영향평가 경험을 증강현실이 얼마나 효과적으로 향상시키는가'를 다뤘다. 제목만 보면 이 축의 핵심 문헌처럼 보인다. 그러나 실체는 2015년 유럽시각지각학회(ECVP) 발표 슬라이드이고, F1000Research에 'NOT PEER REVIEWED'로 명시돼 게재됐다. 조회 238회, 다운로드 16회다. 후속 심사논문으로 발전한 흔적을 찾지 못했다. 즉 풍력 VIA에 AR을 적용한 시도는 학회 발표 한 번으로 끝났다.  둘째, Rannow 등(2023)은 미국 중서부 한 주의 공원 방문객을 대상으로 무작위 배정 실험을 했다. 서령나무좀(emerald ash borer, Agrilus planipennis) 피해에 대응한 산림관리에 관해 네 가지 메시지 중 하나를 받게 했다 — 대조군, 사진, AR, VR. 기대는 '더 몰입적인 정보가 더 큰 효과를 낸다'는 것이었다. 결과는 반대였다. AR은 벌채 같은 관리 행위의 수용도를 정적인 사진·텍스트 전시물보다 유의하게 높이지 못했다. 저자들과 후속 리뷰의 해석이 중요하다 — 옥외 환경에서는 벌레, 소음 같은 환경적 방해 요소와 사용성 문제가, AR이 더 설득력을 가지려면 필요한 인지적 정교화(cognitive elaboration)를 오히려 방해할 수 있다는 것이다.

글래스고 시도는 학회 발표 후 끊겼다. Rannow 등의 결과는 부정적이었고, 2026년 산림 AR 종합 리뷰가 이 결과를 그대로 인용하며 '옥외 환경에서는 환경적 방해와 사용성 문제가 AR의 설득력을 단순 매체 이하로 끌어내릴 수 있다'는 경고로 삼았다. 야외 환경 AR에 대한 가장 냉정한 실증 증거다.

### ReforestAR — 조림용 증강현실 모바일 애플리케이션 (포르투갈)
| 항목 | 내용 |
| --- | --- |
| 주체 | M. Luna, E. Gomes, A. Gonçalves, N. Rodrigues, A. Marto, R. Ascenso. 포르투갈 소재 기관으로 추정되나 정확한 소속 기관명을 확인하지 못했다. |
| 도시·연도 | 포르투갈. 2022년 |
| 증거 수준 | 연구 프로토타입(TRL 4로 분류). 실제 조림 사업 납품 증거 없음. HoloLens 2 식재 유도는 실험적 설정(experimental setups) 단계로 명시돼 있다. |
| AR 여부 | AR 맞음. 조림 대상 지면에 식재 계획을 정합해 겹치는 것이 기능이다. 단 ReforestAR 자체의 정합 방식은 원문 미열람으로 확인하지 못했다. |
| 규모 | 학술대회 논문 1편(pp.180-187). 대상지 면적·식재 본수·참여 인원·예산 모두 미확인. |
| 기술 | 모바일 AR. 구체적 기기·SDK·정합 방식은 원문 미열람. HoloLens 2 식재 유도 실험은 시투과형 MR HMD로 지면에 식재 열·지점 투사. |
| 출처 | Luna, Gomes, Gonçalves, Rodrigues, Marto, Ascenso, 'ReforestAR: An augmented reality mobile application for reforest purposes', 17th Int. Conf. on Computer Graphics Theory and Applications (GRAPP), 2022, pp.180-187 https://doi.org/10.5220/0010833200003124 · TRL 분류 및 HoloLens 2 식재 유도: Current Forestry Reports 12:21, 2026 https://doi.org/10.1007/s40725-026-00283-x |

산림·생태 복원 시나리오 시각화에 AR을 적용한, 이름이 명확한 소수 사례 중 하나다. 조림(reforest) 목적의 AR 모바일 애플리케이션으로 2022년 제17회 컴퓨터그래픽 이론·응용 국제학술대회(GRAPP)에서 발표됐다. 2026년 산림 AR 종합 리뷰가 TRL 4 수준으로 분류한 시스템 군에 속한다. 즉 실험실 환경에서 개념이 검증된 단계다. 같은 리뷰가 확인한 조림 분야 AR의 다른 축은 Microsoft HoloLens 2로 식재 열과 개별 식재 지점을 지면에 투사해 작업자가 시각적으로 복잡한 지형에서도 목표 간격을 유지하게 돕는 실험이다. 규칙적으로 배치된 점과 선이 보이므로 거리를 눈대중으로 추정하는 인지부하가 줄고 조림 배치가 더 일관되게 된다는 것이 기대 효과였다.

2022년 발표 이후 후속 전개를 확인하지 못했다. 2026년 리뷰는 조림 분야 AR 전체를 여전히 파일럿 단계로 평가하며, 산림 AR에서 가장 성숙한 영역은 조림이 아니라 조사·계측이라고 명시했다. 산림·생태 복원 시나리오 시각화는 이 축에서 가장 증거가 얇은 영역이다.

### Trimble SiteVision — 옥외 정밀 정합 AR의 유일한 상용 해답, 그러나 조경은 대상이 아니다
| 항목 | 내용 |
| --- | --- |
| 주체 | Trimble Inc.(미국), Trimble Geospatial 사업부. |
| 도시·연도 | 미국(Trimble), 전 세계 판매. 2019년경 출시~2026년 |
| 증거 수준 | 실제 납품(상용 제품). 2026년 현재 판매·지원 중이며 데모 요청, 사양서, FAQ가 공개돼 있다. |
| AR 여부 | AR 맞음. 제품 자체가 'Trimble SiteVision augmented reality'로 명시되고, GNSS RTK 기반으로 실세계에 설계 모델을 센티미터급으로 정합한다. 이 축에서 정합 정확도가 가장 높은 실제 제품이다. |
| 규모 | 정확도 수평 1cm / 수직 2cm(RTK). 안드로이드·iOS 지원. 도입 기관 수·가격·누적 판매량은 확인 불가. |
| 기술 | Trimble Catalyst DA2 GNSS(RTK), 스마트폰·타블렛 연결형, 폴·핸들 거치, 클라우드 연동 라이다 스캐닝, 지오레퍼런스 컬러 점군 취득. |
| 출처 | Trimble SiteVision 제품 페이지 https://sitevision.trimble.com/ · 수요 측 해석: Fol 외, Scientific Reports 15:15908, 2025 https://doi.org/10.1038/s41598-025-00285-y · Current Forestry Reports 12:21, 2026 https://doi.org/10.1007/s40725-026-00283-x |

야외 AR의 근본 문제인 정밀 측위를 실제로 해결해 상용화한 제품이다. 실시간 이동측위(RTK) 정확도가 수평 1cm, 수직 2cm다. Trimble Catalyst DA2 GNSS 시스템을 안드로이드 또는 iOS 스마트폰·타블렛에 연결하고 폴 또는 핸들에 거치해 쓴다. 기능은 설계안을 실세계에 정확히 배치해 AR로 확인하는 것, 지오레퍼런스된 라이다 점군을 즉시 취득하는 것, 위치·체적·면적·경사·절토/성토를 현장에서 계측하는 것, 그리고 사진·과제·상태를 실시간으로 보고·공유하는 것이다. 핵심 가치는 '설계와 현실의 간극을 메우는 것'과 '지상·지하의 설계-현황 불일치를 조기에 발견해 재작업 비용을 막는 것'이다. 특히 지하 매설물 가시화가 강조된다.

이 항목의 핵심은 대상 산업 목록이다. Trimble이 명시한 산업은 유틸리티, 건설, 주거단지 개발, 측량, 교통이다. 조경·경관은 없다. 옥외 AR의 정밀 측위 문제는 이미 상업적으로 풀렸는데, 그 해답이 향한 곳은 경관 설계가 아니라 땅 밑 매설물과 토목 시공이었다는 뜻이다. 2026년 산림 AR 리뷰도 같은 맥락을 짚었다 — 산림용 전용 상용 MR 솔루션이 없는 이유는 기술이 아니라 수요이며, '제조사가 현재 솔루션을 적응시키게 할 만큼의 고객 수요'가 관건이고 그 선례가 건설용 Trimble MR 헬멧과 HoloLens 2 산업용 에디션이라고 서술했다.

#### 검증에서 잡힌 정정
- ARVino 저자명이 틀렸다. 'G. R. Gnana King'이 아니라 Gary R. King이다. DBLP 키가 conf/ismar/KingPT05이고 Semantic Scholar는 'Gary R. King', Crossref/IEEE 원 레코드는 'G.R. King'으로 적는다. 'Gnana'는 OpenAlex가 동명 인도 연구자(S. Gnana King)와 저자 엔티티를 병합한 오류이며, 이 조사가 OpenAlex를 1차 확인 없이 받아썼음을 보여주는 흔적이다. 소속(Wearable Computer Laboratory, School of Computer and Information Science, University of South Australia, Mawson Lakes)과 4th IEEE/ACM ISMAR, pp.52-55는 맞다.
- Kikuchi 논문 권호가 틀렸다. Journal of Computational Design and Engineering '9(3)'이 아니라 9(2), pp.837-856이다(Crossref, 2022-04-28 온라인).
- Rannow의 이름이 틀렸다. 'Bailey Rannow'가 아니라 Brett Rannow다. JORT 42:100640(2023)과 Environmental Management 71(6):1199-1212(2023) 두 논문 모두 Brett Rannow로 적는다.
- Rannow 등의 소속을 '미네소타대학 계열로 추정되나 소속 원문 미확인'이라고 했지만 원문에 명시돼 있다. University of Minnesota – Twin Cities, Department of Forest Resources, 2005 Upper Buford Circle, St Paul, MN (Rannow·Schneider·Windmuller-Campione·Russell), Angela S. Gupta는 University of Minnesota Extension, 140 Elton Hills Lane NW, Rochester, MN이다.
- Rannow 등 2023을 '풍력 VIA용 AR의 효과 검증'으로 묶은 것은 주제 오분류다. JORT 논문의 제목·주제는 서울호좀나무(emerald ash borer, 서울호좀나무=물푸레나무좀) 대응 산림관리에 대한 공원 방문객 수용성이고, 함께 묶은 Environmental Management 논문은 육상 침입종(terrestrial invasive species) 관리 메시징이다. 둘 다 풍력발전과 무관하다. 2026년 리뷰도 이 연구를 침입종 메시징 사례로 인용한다. 같은 항목에 있는 글래스고(Szymanek & Simmons 2015)만 실제로 풍력 시각영향평가 주제다.
- ReforestAR의 소속을 '포르투갈 소재 기관으로 추정되나 정확한 소속 기관명을 확인하지 못했다'고 했지만 원문에 있다. School of Technology and Management, Polytechnic of Leiria(Politécnico de Leiria), Portugal이고 Nuno Rodrigues와 Rita Ascenso는 CIIC, ESTG, Polytechnic of Leiria다. 저자 전체 이름도 Matias Luna, Enrico Gomes, Alexandrino Gonçalves, Nuno Rodrigues, Anabela Marto, Rita Ascenso로 확인된다.
- COST Action CA23135의 규모를 '유럽 11개국'으로 적은 것은 자릿수가 틀렸다. cost.eu의 CA23135 Management Committee에는 약 43개국이 등재돼 있다(알바니아·오스트리아·보스니아·불가리아·크로아티아·체코·에스토니아·핀란드·프랑스·독일·그리스·헝가리·아일랜드·이스라엘·이탈리아·리투아니아·룩셈부르크·몰도바·네덜란드·북마케도니아·노르웨이·폴란드·포르투갈·루마니아·세르비아·슬로바키아·슬로베니아·스페인·스위스·튀르키예·우크라이나·영국·키프로스·벨기에·아제르바이잔·팔레스타인 등). '11개국'은 리뷰 논문 한 편의 공동저자 소속 국가 수(유럽 11개국 + 호주)이며, Action 자체의 회원국 수가 아니다.
- COST Action의 '본부 성격의 조정은 독일 프라이부르크'와 '책임 Thomas Purfürst(프라이부르크대학 산림작업학 교수단)'가 현재 상태와 맞지 않는다. cost.eu의 CA23135 페이지는 Action Chair를 Prof Thomas Purfürst, 연락처 thomas.purfuerst@tu-dresden.de(드레스덴공대)로 싣는다. 리뷰 논문에서 Purfürst는 소속 1(Chair of Forest Operations, University of Freiburg)과 소속 2(Chair of Digitized Forestry Processes and Systems, Dresden University of Technology)를 겸하며, 주저자 De Miguel-Díez의 교신 메일도 @tu-dresden.de다. 또 Action Vice Chair인 Prof Petre Lameski(FINKI, 북마케도니아)가 누락됐다.
- COST Action 참여 기관 예시에 넣은 WSL은 이 리뷰의 소속 목록에 없다. 리뷰의 소속 1~21은 프라이부르크·TU드레스덴·파도바·폴란드과학원 수목학연구소(Kórnik)·바야돌리드(Palencia)·동핀란드(Joensuu)·포즈난생명과학·Łukasiewicz 포즈난공학연구소·이즈미르카티프첼레비·리스본·에보라·트벤테·기레순·불가리아과학원 지구물리측지지리연구소·우크라이나생명환경과학·CNR-IBE·CoLAB ForestWISE·IIASA·독일 KWF(Groß-Umstadt)·Luke(핀란드)·University of the Sunshine Coast(호주)다. WSL 인물(Schweier·Hristova·Kushwaha)은 별건인 ISPRS ForestAR 논문 저자다.
- 서로 다른 두 개의 'ForestAR'을 하나로 합쳤다. 리뷰가 독일의 국가 과제로 언급하는 ForestAR(BMEL/FNR 과제번호 2223NR030X)과, 증거로 단 ISPRS Archives 2025 논문의 ForestAR 앱은 다른 것이다. 후자는 WSL(Swiss Federal Institute for Forest, Snow and Landscape Research) 주도이고 공동저자 소속이 IIT Roorkee(Abhishek Rai), 싱가포르국립대(Ankit Sagar), UCL(Martin Mokroš)로 스위스·인도·싱가포르·영국 구성이다. 독일 과제의 산출물로 제시할 근거가 없다.
- 'ARKit 기반 구현 R²=0.95, RMSE=2.71cm(414본 대상)'의 기술 귀속이 원문과 다르다. 2026년 리뷰 본문은 이 결과를 optical SLAM과 ray casting을 쓴 시스템의 것으로 적는다('using optical SLAM and ray casting, reporting strong agreement with manual DBH measurements (R² = 0.95; RMSE = 2.71 cm) across 414 trees'). ARKit이라는 언급은 없다. 반면 짝으로 든 'ARCore+RGB-D 딥러닝, R²=0.98, RMSE=2.46cm(340본)'은 Feng et al. 2024로 원문과 일치하고, M-Tree(Mahmud et al. 2025) 85개 대상 RMSE 0.192m도 일치한다.
- Trimble SiteVision 항목이 출처로 단 Current Forestry Reports 12:21(2026)에는 SiteVision이 한 번도 등장하지 않는다. 리뷰 전문(PDF→텍스트 176,905자)에서 'SiteVision' 검색 결과 0건이다. 제품 사양 자체(RTK 수평 1cm·수직 2cm, 대상 산업 utilities·construction·residential development·surveying·transportation, 조경 없음)는 Trimble 공식 페이지로 정확히 확인되므로, 틀린 것은 이 리뷰를 수요측 근거로 끌어온 출처 귀속이다.
- Yabuki를 2026년까지 오사카대학 소속으로 둔 것이 최신 상태와 다르다. 이 조사가 근거로 든 2026년 Engineering Applications of AI 논문(Yang, Fukuda, Yabuki, vol.176, 114825)의 소속 표기 자체가 Yabuki를 'Advanced Research Laboratories, Tokyo City University, Setagaya-ku, Tokyo'로 적고 오사카는 부기다. 즉 '오사카대학 Fukuda–Yabuki 연구실'이라는 현재형 단위 설명은 2026년 시점에 성립하지 않고, 지속되는 쪽은 Fukuda 연구실이다. 같은 논문에서 오사카대학은 영문 명칭을 'The University of Osaka'로 쓴다.
- HoloFlora를 '이 축에서 정합 정확도가 수치로 검증된 유일한 사례'라고 한 것은 같은 목록 안에서 반증된다. Fukuda·Zhang·Yabuki 2014 논문은 제목 자체가 'Improvement of registration accuracy of a handheld augmented reality system'이고, Trimble SiteVision은 RTK 1cm/2cm를 공표하며, 산림 상용 앱군은 R²·RMSE 수치를 갖는다.
- Kikuchi 논문 피인용 82회를 '이 분야에서 이례적으로 높다'고 한 판단이 이 조사 자신의 수치와 어긋난다. 같은 OpenAlex 기준으로 같은 축의 Ghadirian & Bishop 2008이 112회, Haynes 등 2018이 108회로 둘 다 더 높고, 두 수치 모두 이 조사가 직접 적어 놓은 값이다.
- Manyoky 등 2014(ISPRS IJGI 3(1):29-48) 저자 목록에서 제5저자 Adrienne Grêt-Regamey가 빠졌다. 같은 항목이 그를 PLUS 교수로 소개하면서 저자에서 누락한 것이라 특히 어긋난다. 정확한 저자는 Madeleine Manyoky, Ulrike Wissen Hayek, Kurt Heutschi, Reto Pieren, Adrienne Grêt-Regamey다.
- Pettit 등 2012(Landscape Ecology 27(4):487-508) 저자에서 제5저자 Falak Sheth가 빠졌다. 제목은 'Developing a multi-scale visualisation framework for use in climate change response'다.
- Lenné3D를 '2000~2026년', '26년 계보'로 잡은 것은 법인 실체와 어긋난다. 회사 연혁 페이지는 Lenné3D 설립을 2005년으로 적고, 2000년은 DBU 타당성 연구와 그에 이은 4년 연구과제(라이프니츠 농업경관연구센터)의 시점이다. 즉 2005년 창업(21년)이고 그 앞의 연구 전사가 2000년이다. 나머지 연혁은 정확하다 — Philip Paar 초대 대표, 2006년 Malte Clasen 합류, 2010년 Jochen Mülder 승계, 베를린→함부르크→2014년 이후 빌레펠트, 2007년 Esri 비즈니스 파트너·2015년 플러그인 개발 중단 및 파트너십 종료.
- Lenné3D 풍력 관련 프로젝트를 '14건 내외'로 적었으나 현재 전체 프로젝트 목록(41건) 기준 13건이다. 전체 건수 '약 40건'과 AR 0건은 정확하다.
- 2026년 리뷰의 문헌 범위를 '25년치'로 적었으나 초록은 'between 2000 and 2025'(26년)로 명시한다.
- ÖBf 근거 문서의 성격이 다르게 소개됐다. 리뷰 참고문헌 64의 URL 파일명은 'Revolutionäre_digitale_Naturvermittlung_mittels_Augmented_-_Reality'로, 오스트리아 행정혁신상(Verwaltungspreis) 제출 자료이며 주제는 일반인 대상 자연해설(Naturvermittlung)이다. '임지경계 가시화 파일럿'이라는 규정은 리뷰 본문의 서술을 따른 것이지 이 1차 문서의 자기 규정이 아니다. 문서명 'Ein vorläufiges Fazit'(잠정 결론)과 2023년, 저자 D. Lepizh는 맞다.
- Arboreal 'Arboreal Forest 2019년 출시'는 인용한 벤더 페이지에 없는 수치다. arboreal.se/en/arboreal-forest는 출시 연도를 적지 않고 2020년 석사논문 평가와 2020년 LiDAR 센서 출시를 언급할 뿐이며, 'augmented reality'라는 표현도 쓰지 않는다. 이 앱의 AR 분류는 2026년 리뷰의 서술('virtual stem-alignment rings')에 의존하는 것이고 벤더 자기표현이 아니다.
- ARVino 제1저자 이름 오류. 조사는 'G. R. Gnana King'으로 적었으나 ISMAR'05 원서지 저자는 'G.R. King'(Gareth R. King), W. Piekarski, B.H. Thomas다. 'Gnana'는 실재하지 않는 삽입(다른 연구자와 혼동). 수록면은 pp.52-55. 출처: https://api.crossref.org/works/10.1109/ismar.2005.14
- 항목 전체 오분류 — '풍력 VIA용 AR의 효과 검증 … Rannow 등(2023)'. Journal of Outdoor Recreation and Tourism 42:100640의 실제 제목은 'Research note: The impact of advanced information communication technologies on visitor acceptance of forest management in response to emerald ash borer'다. 풍력발전 경관영향평가가 아니라 침입해충(에메랄드 물푸레나무 천공충) 대응 산림관리(벌채 등)에 대한 공원 방문객 수용성 연구다. 동반 논문 Environmental Management 71:1199-1212도 'What Really Works? Testing Augmented and Virtual Reality Messaging in Terrestrial Invasive Species Management Commu
- 저자 이름 오류: 'Bailey Rannow' → 실제는 'Brett Rannow'(JORT 저자 목록 및 2026 리뷰 참고문헌 11·60번 모두 'Rannow B').
- HoloFlora 공동저자 소속 오류. 조사는 'ETH Zürich Forest Resources Management 중심'이며 Remondino(FBK Trento)만 외부라고 적었으나, 원문 소속은 Fol·Griess=Forest Resources Management(ETH), Späth=Transdisciplinarity Lab(ETH), Jiayan Zhao=Laboratory of Geo-Information Science and Remote Sensing, Wageningen University & Research(네덜란드), Arnadi Murtiyoso=ICube Laboratory, INSA Strasbourg(프랑스), Remondino=3DOM, Fondazione Bruno Kessler(이탈리아)다. Zhao·Murtiyoso는 ETH 소속이 아니다.
- HoloFlora 대상지 오류. 논문은 'Baden marteloscope, located in the Swiss canton of Aargau'로 명시한다. 아르가우주이며, 대상지로 '취리히'를 병기한 것은 근거 없다(취리히는 ETH 소재지일 뿐).
- HoloFlora 전문가 평가자 성격 오류. 조사는 '전문가 평가 3명(TreM 식별 전문가)'이라 적었으나 원문은 'Participant A worked in forest inventory for a canton, Participant B was a forest owner, and Participant C was a pioneer in TreM research'다. 3명 모두 TreM 식별 전문가가 아니다. 또한 '한 대학 강사는 교육과정에 넣겠다고 했다'는 서술은 이 3인의 역할 기술(주 산림조사 실무자·산림 소유자·TreM 연구자)과 대응하지 않아 원문에서 확인되지 않는다.
- HoloFlora 정확도 측정 서술 오류. 1.4 cm는 '5분 기록 구간의 기하오차'가 아니라, 근접 사진측량 모델과 Immersal 맵을 CloudCompare M3C2로 비교해 산출한 표준편차(standard deviation of 1.4 cm)이며, 측정은 2일차에 5분짜리 시행 8회(eight trials of 5 min)로 수행됐다.
- 'HoloFlora가 이 축에서 정합 정확도가 수치로 검증된 유일한 사례'는 거짓. 같은 목록의 Fukuda·Zhang·Yabuki 2014는 제목 자체가 'Improvement of registration accuracy of a handheld augmented reality system for urban landscape simulation'이고, Kikuchi·Fukuda·Yabuki 2022는 차폐 처리 정확도 IoU 약 0.8·30 fps를 보고하며, Trimble SiteVision은 RTK 1 cm 수평/2 cm 수직을 제품 사양으로 명시한다.
- (외 30건)

## participation
항목 16개 · 검증 정정 지적 71건

> 시민참여는 조경·도시설계 AR 문헌에서 가장 두꺼운 축이면서 가장 허약한 축이다. 실제 행정계획에 붙어 시민이 놓은 것이 시공까지 간 사례는 두 건뿐이다. 첫째는 오슬로다. Kai Reaver(오슬로건축디자인대학)가 2020~2021년 ByKuben(오슬로 계획건축국 도시생태센터)과 함께 8개 구 청소년 5개 그룹(그룹당 9~18명)에게 iPad Pro를 주고 '10만 그루' 계획의 일부를 직접 배치시켰다. AR로 놓인 나무는 약 8,000그루(중복 제거 시 약 5,000), 논문은 "몇몇 제안이 실제로 실행됐다"고 쓰지만 그 근거는 2022년 11월 시청 회의 한 건이라고 각주에 밝힌다. 둘째는 마이애미다. FIU 연구진이 The Underline 공원 재설계 전에 노인 10명에게 HoloLens를 씌워 도로 차단벽 세 안을 현장에서 보여줬고, 90%가 투명벽을 택했으며 "결과가 Underline 팀에 전달되어 재설계에 사용되고 있다"고 명기했다. 이 둘 외에 설계 변경으로 이어진 기록은 찾지 못했다.  나머지는 대부분 프로토타입에서 멈춘다. TUM(2018)·빅토리아웰링턴(2021)·하펜시티함부르크(2022)는 시스템을 만들었으나 시민 실사용 시험이 없거나 "사용성 연구는 아직 진행 중"이라고 스스로 적는다. 비엔나 BRISE(EU Urban Innovative Action, UIA04-081)는 5개 분야 전문가 14명 인터뷰로 AR 활용사례 12개를 도출하고 도면검토 2건을 최우선으로 꼽았지만, 실제 인접주민 청문에 투입된 증거는 없다. 밀라노 AR4CUP은 H2020 EIT Digital로 2019년 1월~12월 단년 과제였고 2019년 12월 'Experiencing VITAE' 행사에서 시민 63명을 모았으나, 그 감정 데이터가 설계를 바꿨다는 보고는 없다.  종이 도면·VR과의 비교실험은 얇다. Boos 등(2022, 취리히대·ETH)이 스위스 건축측량틀(Baugespann)과 AR을 피험자간 현장실험으로 붙인 것이 사실상 유일하며, LOD 3단계 간 주관평가 차이는 유의하지 않았다. 배제 문제에는 단단한 수치가 하나 있다. 마이애미에서 AR 안경은 노인의 자세동요 면적을 약 25%, VR 고글은 약 70% 늘렸다. 그리고 모든 사례에서 기기는 예외 없이 주최측이 공급했다. 시민 자기 기기로 굴러간 참여 AR은 한 건도 없다.


### Oslo Trees(Oslotrær) 청소년 AR 나무 배치 워크숍 — 소프트웨어 'Udaru'
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주·초기 제안: 오슬로시 계획건축국 도시생태센터 ByKuben + 시의회 도시개발 담당(City Council for Urban Development). 수행·연구: Kai Reaver 단독저자, 오슬로건축디자인대학(AHO, The Oslo School of Architecture and Design) Creative Technologies 과정. 참여자 모집·인건비·인솔 직원: 오슬로시 부담. 기술비 일부도 시가 지원. |
| 도시·연도 | 노르웨이 오슬로 / 2020년 8월(5주) + 2021년 반복 / 논문 2023-02-13 게재 |
| 증거 수준 | 공공 시범사업(실제 행정계획에 연동된 지자체 발주·자금 지원 워크숍). 일부 제안은 실제 시공까지 갔다고 논문이 밝히나 그 근거는 회의 전언 1건. |
| AR 여부 | AR 맞음. iPad Pro 카메라 화면의 실제 가로·공지에 3D 수목을 실제 치수로 겹쳐 놓고, 그 자리에서 보면서 위치를 정했다. 다만 정합은 GPS 기반으로 부정확했고 저자가 '실측 수준에 못 미친다'고 명시한다. |
| 규모 | 청소년 5개 그룹, 오슬로 8개 구, 그룹당 9~18명. 주당 1그룹씩 5주. 워크숍당 3~5일, 하루 4~5시간, 하루 4~5개 지점 답사. AR로 배치된 나무 약 8,000그루(중복 제안 통합 시 원안 약 5,000그루). 예산 비공개. 워크숍4에서 2명은 '실제로 나무 심는 일인 줄 알았다'며 참여를 거부해 실물 식재 작업으로 대체 배정. |
| 기술 | iPad Pro(1인 또는 2인 1대). Apple ARKit + Unity로 만든 자체 소프트웨어 'Udaru(User-driven Augmented Reality Urbanism)'. 여기에 상용 Augment 패키지와 AR 조경앱 iScape의 요소를 섞어 썼다. 정합은 GPS + iPad 메타데이터 위치. 익명 보호를 위해 iPad별 익명 아이디로 데이터를 수집. 결과물은 화면녹화·스크린샷으로 클라우드 업로드. 실제 식재 위치를 확정하려면 워크숍 결과를 다시 CAD 도면 또는 GIS에서 수동으로 좌표 지정해야 했다. |
| 출처 | https://doi.org/10.3389/frvir.2023.1055930 (Frontiers in Virtual Reality 4:1055930, 오픈액세스 전문) · https://www.frontiersin.org/articles/10.3389/frvir.2023.1055930/full |

오슬로시가 2030년까지 새 나무 10만 그루를 심기로 한 'Oslo Trees' 계획의 일부를 청소년이 AR로 직접 배치하게 한 연구다. 시작은 시 쪽이었다. 오슬로 계획건축국 산하 도시생태센터 ByKuben과 시의회 도시개발 담당이 오슬로건축디자인대학(AHO)에 먼저 물어왔고, Kai Reaver가 이를 실지 사례연구로 설계했다. 진행은 매 워크숍 3~5일 구조였다. 첫날 AHO 통제 환경에서 1시간 AR 조작·화면녹화 훈련, 이어 1시간 구글맵·스트리트뷰로 자기 동네에서 심을 만한 자리를 청소년 스스로 골랐고, 그다음 3~4일간 하루 4~5시간씩 도보와 대중교통으로 하루 4~5개 지점을 돌며 iPad로 나무를 놓았다. 마지막에 각자 iPad에서 마음에 드는 안을 골라 정치인·시 공무원·구청 담당자 앞에서 직접 발표했다. Arnstein의 참여 사다리를 평가 틀로 쓴 것이 이 연구의 뼈대인데, 저자는 최상단 '시민 통제'에 닿았다고 볼 여지가 있다면서도 곧바로 반론을 스스로 적는다 — 전문가의 구조·훈련·장비 없이는 이 워크숍 자체가 성립하지 않았다는 것이다. 배제 문제에서도 예상이 뒤집혔다. 청소년이 AR을 어려워할까 봐 긴 훈련 시간을 잡아뒀지만 2020년 첫 시험 후 '불필요하고 심지어 과잉'이라 판단해 줄였고, 대부분이 몇 분 안에 인터페이스와 공간 배치를 이해했다. 반대로 전문가는 끝까지 필요했다 — 토양, 수종, 용도지역, 근계 크기를 청소년이 모르기 때문에 어떤 안이 실행 가능한지 검증하는 일은 전문가 몫으로 남았다.

논문 본문: "we learned after the case study that several of the proposals were, in fact, implemented, with more implementation planned in future." 그리고 청소년이 자기 선호대로 만든 안이 "even implemented by the municipality"라고 적는다. 그러나 각주는 그 출처를 "From meeting with Oslo municipality and ByKuben 11 November 2022" 한 건으로 밝힌다 — 즉 시공 기록이 아니라 사후 회의 전언이다. 기술적 실패도 분명히 남았다: 위치추적·측위가 부정확하고 자주 '버그'가 나 이용자 짜증을 유발했고, 많은 나무가 토지 이용권상 법적으로 어려운 자리나 근계가 들어갈 수 없는 지하 조건에 놓였다. 저자는 AR이 디지털 도구의 사다리 8단계(시민 통제)를 가능케 하는지 재정의가 필요하다는 과제를 남기고 끝낸다.

### AR4CUP(Augmented Reality for Collaborative Urban Planning) → 밀라노 'Experiencing VITAE' 공개행사
| 항목 | 내용 |
| --- | --- |
| 주체 | 자금: EU Horizon 2020 — EIT Digital 2019 및 2020 'AR4CUP'. 컨소시엄: Artefacto(프랑스 AR 기업, 기술개발), VTT(핀란드 국립기술연구소, 기술개발), 밀라노공대 Laboratorio di Simulazione Urbana Fausto Curti(건축·도시학과), Covivio(부동산 개발사). 대상 설계안 VITAE의 설계자: Carlo Ratti Associati. 논문 저자: Barbara E.A. Piga, Gabriele Stancato(밀라노공대), Marco Boffi, Nicola Rainisio(밀라노대). |
| 도시·연도 | 이탈리아 밀라노 Porta Romana 지구 via Serio(Scalo di Porta Romana 남측) / 과제 2019.01~2019.12 / 공개행사 2019년 12월 |
| 증거 수준 | 공공 시범사업(EU 자금 + 민간 개발사 공동). 2019년 12월 실제 공개행사에서 일반 시민 대상으로 운영됐으므로 전시·시연 이상이지만, 납품된 상용 제품으로 남았는지는 확인 불가. |
| AR 여부 | AR 맞음. 대상지 현장에서 사진사실적 3D 모델을 실제 치수로 자동 지오레퍼런싱해 스마트폰 화면의 실세계에 겹쳤다. |
| 규모 | 수요분석 인터뷰: 개발사 3 + 건축사무소 3 + 전임 시의원 1 = 7명, 각 90분. 후속 실증: 2019년 12월 'Experiencing VITAE' 야외 공개행사에서 AR 참여 시민 63명(평균 41세). 비교군 VR 실험은 대학생 48명(평균 26세)으로 별도 수행. 대상지 VITAE는 현재 주차장으로 쓰이는 5,000㎡ 규모 도시 공지. |
| 기술 | 모바일 앱 'City Sense'에 exp-EIA©(체험적 환경영향평가) 방법을 탑재. 도시 변화의 사진사실적 3D 모델을 현장에 자동 지오레퍼런싱. 감정 반응은 앱 안에서 수집해 자동 분석. AR4CUP 앱의 기술 개발은 Artefacto와 VTT가 담당했다고 각주에 명시. 정밀 측위(RTK·VPS) 사용 여부는 공개되지 않음. |
| 출처 | https://doi.org/10.5821/ctv.8622 (Piga et al., XIII CTV 2019, 전문 PDF: https://upcommons.upc.edu/bitstream/2117/185564/1/8622-8998-1-PB.pdf) · 후속: https://doi.org/10.3390/su132313388 (Sustainability 13(23):13388) |

부동산 개발사가 실제로 짓는 프로젝트를 현장에서 AR로 보여주고 시민의 감정 반응을 수치로 수집한, 이 분야에서 드물게 발주처가 민간인 사례다. H2020 EIT Digital(Digital Cities) 과제로 2019년 1월 시작해 같은 해 12월 종료된 단년 과제였고, AR 기업 Artefacto, 밀라노공대, 핀란드 VTT, 부동산 개발사 Covivio가 컨소시엄을 이뤘다. 앱의 설계 목표는 네 가지였다 — 현장에서 실제 치수로 지오로케이션된 건축·도시 제안을 보여주고, 시민의 감정 반응을 수집하고, 자동 분석하고, 결과를 표현한다. 첫 단계는 앱을 만들기 전에 고객 수요를 캐는 인터뷰였다. 국제 부동산 개발사 3곳, 대형 도시개발을 맡은 국제 건축사무소 3곳, 그리고 인구 규모 있는 도시의 전임 도시계획 담당 시의원 1명에게 각 1시간 30분씩 반구조화 인터뷰를 했다. 여기서 나온 결과가 흥미롭다. 실무자들은 시중 AR 앱을 못 믿는다고 했고, 이유는 두 가지였다 — 디테일·텍스처·반사·음영 품질이 낮아 최종 프로젝트를 과소평가하게 만든다는 것, 그리고 리얼리즘 때문에 마케팅에 필요한 '꿈 효과(dream effect)'가 사라진다는 것. AR을 팔려는 쪽이 정작 사려는 쪽에게서 '너무 현실적이어서 못 쓴다'는 말을 들은 셈이다.

VITAE는 C40 Reinventing Cities 당선안이었고 Covivio가 실제로 개발했다. 그러나 AR로 모은 시민 감정 데이터가 설계를 바꿨다는 보고는 논문에 없다. 2021년 Sustainability 후속 논문은 녹색·라임색의 가중 채도가 불쾌감을 낮춘다는 색채 상관만 보고하고, 시민 피드백의 설계 반영은 다루지 않는다. 과제 자체는 2019년 12월로 끝났고, AR4CUP 앱이 상용 제품으로 남았는지 폐기됐는지 1차 자료로 확인하지 못했다. 연구팀은 이후 'City Sense' 앱 계보로 연구를 이어갔다.

### The Underline 고령자 친화 공원 재설계 — HoloLens 현장 선호조사
| 항목 | 내용 |
| --- | --- |
| 주체 | 수행: Edgar Ramos Vieira, Fernanda Civitella, Jorge Carreno, G. Miburge(세르지페연방대 겸직), César Ferreira Amorim, Newton D'souza, Ebru Özer — 이상 플로리다국제대(FIU). Francisco Raul Ortega — 콜로라도주립대. 자금·연계: Miami-Dade County Age-Friendly Initiative 소액보조금(minigrant). 대상 사업: Miami-Dade Underline Project(The Underline, 메트로레일 고가 하부 선형공원). |
| 도시·연도 | 미국 플로리다주 마이애미(Miami-Dade County), The Underline 대상지 / 논문 2020년(Journal of Aging Research) |
| 증거 수준 | 연구 프로토타입(파일럿 연구). 다만 결과가 실제 공원 재설계 팀에 전달되어 사용되고 있다고 논문이 명기했으므로, 실무로 이어진 드문 경우다. |
| AR 여부 | AR 맞음. HoloLens 광학 투과형 HMD로 실제 공원 현장에 가상 차단벽 홀로그램을 겹쳤다. 같은 연구에서 HTC Vive VR도 대조군으로 썼고, 두 조건의 자세동요를 분리해 보고한다. |
| 규모 | 노인 10명, 평균 68±5세. 모집: 주민회의가 열리는 지역 관공서 시설 + 참여자의 친구·이웃 구전. 전원 공원에서 2마일 이내 거주. 사례비 1인 10달러. 시험 대상: 차단벽 3안(높은 실벽·낮은 실벽·투명벽) 및 기타 공원 요소. |
| 기술 | Microsoft HoloLens(AR), HTC Vive(VR 대조군). 측정: force plate(균형), instrumented mat(보행). 가상 차단벽을 실제 공원 좌표에 어떻게 정합·앵커링했는지는 논문에 기술되지 않았다. |
| 출처 | https://doi.org/10.1155/2020/8341034 (Journal of Aging Research 2020:8341034) · 전문: https://pmc.ncbi.nlm.nih.gov/articles/7482015/ |

이 목록에서 '참여 결과가 실제 설계에 쓰이고 있다'고 문서로 명기한 두 번째 사례다. 마이애미 노인들이 공원을 잘 쓰지 않는다는 문제에서 출발했다. 이유가 공원이 그들의 필요와 선호를 지원하지 않기 때문이라면, 재설계 단계에서 노인을 끌어들여야 한다는 가설이었다. 연구진은 노인 10명을 공원으로 데려와 HoloLens를 씌우고, 산책로와 차도를 가르는 차단벽 세 가지 안 — 높은 실벽, 낮은 실벽, 투명벽 — 을 현장에 겹쳐 보여줬다. 단순한 선호 설문이 아니었다. 힘판(force plate)과 계측 매트로 균형과 보행을 동시에 측정해 'AR 기기를 씌우는 것 자체가 노인에게 안전한가'를 물었다. 결과는 두 층으로 나왔다. 선호 쪽에서는 90%가 투명벽을 '좋다' 또는 '아주 좋다'로 표시했고, 40%는 높은 실벽을 '아주 싫다'로 골랐다 — 시야 차단과 그로 인한 안전 우려가 이유였다. 반면 벽 종류가 보행 자체를 바꾸지는 않았는데, 연구진은 두 가지 해석을 나란히 적는다 — 실제로 걸음이 달라지지 않았거나, 홀로그램이 걸음을 바꿀 만큼 사실적이지 않았거나. 기기 안전 쪽 결과가 이 연구의 가장 단단한 기여다. 안경을 안 쓴 상태와 비교해 AR 안경 착용 시 자세동요 면적이 약 25%, VR 고글 착용 시 약 70% 늘었다. 저자는 이 차이가 '임상적으로 유의미하다'고 쓰면서도, 표본이 작고 변동이 커 통계적 유의를 낼 검정력이 없었다고 솔직히 적는다.

논문 명시: "The findings were shared with the Underline team and are being used in the redesign of the area." 즉 시민 참여 결과가 실제 설계 과정에 투입된, 이 축에서 두 건뿐인 사례 중 하나다. 다만 재설계가 실제로 투명벽을 채택해 준공됐는지는 논문 시점(2020)에 확인되지 않으며 후속 문서도 찾지 못했다. 부수적으로, 이 연구는 '고령자를 AR 참여에서 배제하는 것이 무엇인가'에 대한 이 축의 유일한 정량 증거를 남겼다 — 기기 착용 자체가 노인의 자세 안정성을 떨어뜨린다(AR +25%, VR +70%).

### City Craft — 다중 사용자 협업 AR 도시설계 앱 (잘츠부르크 Science City)
| 항목 | 내용 |
| --- | --- |
| 주체 | Irina Paraschivoiu(잘츠부르크대 Human-Computer Interaction Division 및 Polycular), Robert Steiner, Judith Wieser, Alexander Meschtscherjakov(잘츠부르크대 HCI Division). 자금: Land Salzburg(잘츠부르크 주정부) WISS 2025 프로그램, 과제명 '5G Exploration Space'. 오픈액세스 게재비는 Paris Lodron University of Salzburg 부담. |
| 도시·연도 | 오스트리아 잘츠부르크, Science City 지구 / 논문 2025년(CSCW: Computer Supported Cooperative Work) |
| 증거 수준 | 연구 프로토타입. 실제 공공공간에서 수행된 현장 실험이지만 실제 행정 계획 절차에 연동되지 않았다. |
| AR 여부 | AR 맞음. Android 기기 카메라로 실제 공공공간에 3D 에셋을 배치하고, 클라우드 앵커로 위치를 고정해 여러 기기가 같은 장소에서 같은 설계안을 보게 했다. |
| 규모 | 본 실험 총 33명. 1차: 3세션×6명=18명(남5·여13), 2인 1조 태블릿 공유, 총 9쌍, 세션당 2시간. 2차: 2세션(8명+7명)=15명(남5·여10), 1인 1기기. 모집: 메일링리스트·SNS·대학 캠퍼스 인쇄 포스터. 구성: 학생·행정직원·연구자·음악가·건축가 2명·디자이너·엔지니어. 약 30%가 같은 세션의 다른 참여자를 이미 알고 있었음. 앞선 설계 단계 참여자는 별도로 전문가 4명 + 66명, 인터뷰 10명, 관찰·스토리보드 28명, 중간 워크숍 6명, 프로토타입 시험 6세션. |
| 기술 | Unity3D + AR Foundation + ARCore Extensions의 persistent cloud anchor(환경 이미지 캡처로 앵커 위치 복원) → 장소 고정형 '설계 공간' 구현. 다중접속은 AR Foundation이 Android 멀티플레이를 기본 지원하지 않아 Unity Netcode로 대체 구현. Android 전용. 에셋 40종을 Autodesk Maya로 모델링, Adobe Substance Painter로 텍스처링, 모바일에서 50개 모델 규모 씬이 돌도록 메시를 최소화하고 텍스처·노멀맵으로 디테일 복원. 1차 실험: Samsung Tab S6, 로컬 무선망. 2차 실험: Samsung Galaxy A30S, Huawei P20 Pro 2대, Moto 5G, Moto G 5G P |
| 출처 | https://doi.org/10.1007/s10606-025-09510-8 (CSCW 2025) · 오픈액세스 전문: https://eplus.uni-salzburg.at/obvusboa/content/titleinfo/13793676/full.pdf |

협업 AR 도시설계 도구를 실험실이 아니라 실제 공공공간에서 33명에게 쓰게 하고, '누가 어떻게 협업하는가'를 측정한 드문 현장연구다. 대상지는 잘츠부르크의 Science City — 대학·연구시설·기업·주거·학생기숙사가 모인 조밀한 구역인데 식당 하나, 학생식당 하나, 슈퍼마켓 하나뿐이고 모일 만한 야외 공간이 부족하다는 문제가 있었다. 개발은 2주기로 진행됐다. 1주기는 '미래로부터의 엽서' 같은 디자인 픽션 활동으로 전문가 4명과 참여자 66명을 모아 미래상을 뽑았고, 2주기는 요구사항 수집(주민·직원·전문가 인터뷰 10명), 참여자 28명의 민족지적 관찰과 스토리보드 14편 제작, 중간 공동설계 워크숍 6명, 클릭형 프로토타입 개인 시험 6세션으로 앱을 다듬었다. 핵심은 스토리보드가 3D 에셋 목록으로 직결됐다는 점이다 — 앉을 자리 부족, 보행자·자전거 편의시설, 녹지, 사교 공간 부족이라는 주민 관찰이 그대로 40개 에셋(공공 좌석·녹지·편의시설·건물·인프라) 카탈로그가 됐다. 좌석 하나에도 전통 목재 벤치, 파라메트릭 디자인, 암석형 구조 같은 스타일 선택지를 뒀다. 본 실험은 두 번이었다. 1차는 3세션×6명으로 2인 1조가 태블릿 한 대를 공유했고, 2차는 2세션(8명, 7명)으로 각자 자기 기기를 썼다. 과제는 셋 — 개선안 3개 이상 제안, 개선안 토론, 실행을 전제로 우선순위 매기기. 결과가 명확하게 갈렸다. 한 대를 공유한 쌍은 동기적으로, 공동 소유 감각으로 협업했지만 다른 쌍과는 거의 교류하지 않았다. 기기를 각자 든 큰 집단은 비동기적으로 — 서로의 안을 보고 편집하며 — 움직였다.

실제 계획 절차로 이어진 기록은 없다. 저자들이 밝힌 한계 세 가지가 이 축 전체에 적용된다. (1) 과제 순서가 결과를 편향시켰을 수 있다 — 참여자는 과제1(제안)에서 자기 안에만 집중하고 과제2·3(개선·우선순위)에서야 남의 안을 봤다. (2) 기술적으로 렉이 걸렸다 — 짧은 시간에 여러 사용자가 객체를 많이 추가하면 성능이 떨어졌다. (3) 자기선택 편향 — 워크숍 등록이 자발적이었으므로 참여자는 애초에 이 주제에 관심 있는 사람들이었고, 관심·즐거움 증가가 이 표본에 한정된 것인지 알 수 없다. 저자 결론도 신중하다: AR 도구는 관심을 끌어올리지만 "설계 과정의 여러 단계에 걸쳐 디지털·아날로그 도구를 섞어야 하며, 어떤 단일 도구도 다양한 이해관계자를 다 수용할 수 없다."

### BRISE-Vienna — 건축허가 행정의 AR 활용사례 12개
| 항목 | 내용 |
| --- | --- |
| 주체 | 수행: Alexander Gerger, Harald Urban, Christian Schranz — 이상 TU Wien(빈공과대). 발주·주체: 빈시(City of Vienna) 건축국(Vienna Building Authority). 인터뷰 참여: 건축사협회(association of architects) 등. 자금: EU Urban Innovative Action(UIA), 보조금 번호 UIA04-081. |
| 도시·연도 | 오스트리아 빈 / 논문 2023년(Buildings 13(6):1462). 과제 시작·종료일 미확인 |
| 증거 수준 | 공공 시범사업의 개념설계 단계. 앱이 구현·시험됐다는 서술은 있으나 실제 허가 청문 절차에 시민을 대상으로 투입된 증거는 논문에 없다. |
| AR 여부 | AR 맞음(개념 단계). 모바일 AR과 HMD 양쪽을 플랫폼으로 검토했고, 실세계 대지에 허가 신청 건물을 겹쳐 보는 것이 05·06번 활용사례의 핵심이다. 다만 실제 인접주민 청문에 투입된 증거는 없다. |
| 규모 | 전문가 인터뷰 14명, 5개 분야(용도지역·측량·건축·건축국·소방). 도출된 AR 활용사례 12개, 최고 평가 2개(UC05 관청 도면검토 디지털화, UC06 현장 시민 AR 도면검토). 총 사업비 미확인. 배경 수치: 빈의 아날로그 허가 절차 최대 18개월. |
| 기술 | BIM 기반. 모바일 AR(mAR)과 head-mounted display(HMD) 양쪽을 플랫폼 후보로 검토. 구체적 기기명·SDK·정합 방식은 논문에 명시되지 않음. |
| 출처 | https://doi.org/10.3390/buildings13061462 (Buildings 13(6):1462, 오픈액세스) |

AR을 '시민 설득'이 아니라 '행정 절차 단축'의 도구로 접근한 유럽 공공 프로젝트다. 문제 설정이 구체적이었다. 빈에서 아날로그 건축허가 절차는 최대 18개월이 걸리고, 그 지연 원인 하나가 비전문가 이해관계자의 이의제기다 — 2D 도면만으로는 프로젝트를 이해할 수 없기 때문에 나오는 이의다. 빈시는 BIM과 AR로 건축국 절차 자체를 재설계하기로 하고 이를 BRISE-Vienna 연구과제에 넣었다. TU Wien 연구진이 절차 분석과 전문가 인터뷰로 AR 활용사례 12개를 도출했다: (01) AR 협력계획 워크숍, (02) 정보 전시회의 AR, (03) 의사결정자 시각 지원, (04) AR 측량 지원, (05) 관청 내 도면검토 디지털화, (06) 현장에서 시민이 하는 AR 도면검토, (07) AR로 도시경관 검토, (08) 현장 건축국 담당자 지원, (09) 디지털 건축물대장과 AR, (10) 시설관리의 AR, (11) AR 소방작전 지원, (12) 기존 건축물 상태 AR 평가. 이 목록 자체가 유용하다 — 조경·도시 분야에서 AR을 어디에 쓸 수 있는지 행정 실무자가 직접 꼽은 것이기 때문이다. 평가 결과 최고점은 05번과 06번, 즉 도면검토 두 건이었다. 05번은 '바로 실행 가능'하고 시민과 관청 양쪽에 '매우 유용'하다고 평가됐고, 06번은 기술적으로 더 복잡하지만 비슷하게 높은 점수를 받았다. 주목할 것은 시민 참여 워크숍(01번)과 전시(02번)가 최우선이 아니었다는 점이다 — 행정이 원한 것은 참여 확대보다 절차 속도였다.

최고 평가를 받은 도면검토 2건이 연구과제 안에서 더 개발될 예정이라고 밝혔고, 빈의 절차를 크게 단축해 다른 도시·국가의 기반이 되기를 목표로 한다고 썼다. 2023년 논문 시점에서 AR이 실제 허가 청문에 쓰였다는 증거는 없다 — 앱 구현·시험 서술은 있으나 실증 대상이 시민이었다는 기록이 없다. 이후 진척은 확인하지 못했다. 시민참여 축에서 이 사례의 값은 '참여를 늘리려고 AR을 도입한 것이 아니라, 참여(이의제기) 때문에 늘어난 절차 시간을 줄이려고 AR을 도입했다'는 동기의 역전에 있다.

### AR 대 건축측량틀(Baugespann) 비교 현장실험
| 항목 | 내용 |
| --- | --- |
| 주체 | Ursina Christina Boos, Tumasch Reichenbacher(취리히대 University of Zurich), Peter Kiefer, Christian Sailer(ETH Zürich 지도학·지리정보연구소 Institute of Cartography and Geoinformation). 스위스. |
| 도시·연도 | 스위스(정확한 도시 미확인) / 논문 2022년(Journal of Location Based Services 16권) |
| 증거 수준 | 연구 프로토타입(현장 피험자간 실험). 실제 허가 절차나 주민 협의에 투입된 것은 아니다. |
| AR 여부 | AR 맞음. 현장 대지에 계획 건물을 실제 치수로 겹쳐 보는 프로토타입 앱을 썼고, 비교군인 Baugespann은 AR이 아닌 실물 목재 구조물이다. |
| 규모 | 측량틀 추정과제 2개 + AR 추정과제 6개를 각 참여자가 수행. AR은 LOD 3단계 그룹으로 분리. 정확한 피험자 수, 연령, 모집 방식, 실험 일자를 전문 접근 실패로 확인하지 못했다. |
| 기술 | 프로토타입 AR 애플리케이션, 동일 건물 프로젝트의 디테일 수준(LOD) 3단계. 기기·SDK·정합 방식은 확인하지 못했다. 비교군: Baugespann(건축측량틀) — 실제 대지에 목재로 세우는 건물 윤곽·높이 표시 관행. |
| 출처 | https://doi.org/10.1080/17489725.2022.2086309 (Journal of Location Based Services, CC-BY) · 저장소: https://doi.org/10.3929/ethz-b-000542298 · https://doi.org/10.5167/uzh-220841 |

이 축에서 요청받은 '종이 도면·VR·AR 비교 실험'에 가장 가까운 연구다. 비교 대상이 흥미롭다 — 종이 도면이 아니라 스위스·독일어권의 제도적 관행인 Baugespann, 즉 신축 건물의 윤곽과 높이를 실제 대지에 목재 틀로 세워 인접 주민이 볼 수 있게 하는 '건축측량틀'이다. 이것은 이미 법으로 굳은 실물 규모 시각화 수단이고, 따라서 AR이 이길 상대로 정확히 적합하다. 연구진은 같은 건축 프로젝트에 대해 측량틀 조건과 AR 앱 조건(디테일 수준 LOD 3단계)을 피험자간(between-subjects) 현장실험으로 붙였다. 참여자는 측량틀로 추정과제 2개, AR 앱으로 추정과제 6개를 푼 뒤 각 시각화 방식에 대한 설문에 답했다. 결과는 AR 지지자에게 미묘하다. 참여자들은 AR의 잠재력을 확신했지만, LOD 그룹 간 주관적 평가에서 유의한 차이는 나오지 않았다. 대신 다른 것이 드러났다 — GIS 같은 사전 지식이 치수 추정 성능에 긍정적 영향을 줄 수 있다는 것, 그리고 파사드 요소나 창 같은 디테일이 있으면 건물 크기를 유추할 근거가 되어 추정과제를 돕는다는 것. 즉 '디테일을 많이 넣으면 좋아한다'가 아니라 '디테일이 크기 판단의 단서를 제공한다'는 기능적 발견이다.

AR이 측량틀을 명확히 이겼다는 결론은 나오지 않았다. 참여자는 AR의 잠재력에 확신을 보였으나 LOD 3단계 간 주관적 평가에 유의한 차이가 없었다. 부수 발견: GIS 등 사전 지식이 치수 추정 성능에 긍정적 영향을 줄 가능성, 파사드·창 같은 디테일이 건물 크기 유추의 단서가 되어 추정과제를 돕는다는 점. 이 축에서 '비교 실증'을 인용할 때 사실상 유일하게 기댈 수 있는 연구이지만, 그 결론은 'AR이 낫다'가 아니라 'AR이 유망하지만 정밀도 차이가 주관 평가에 안 잡힌다'에 가깝다.

### Citizen-Centered Design in Urban Planning — 저기술 사용자를 위한 레고·점토 공동설계법
| 항목 | 내용 |
| --- | --- |
| 주체 | Sheree May Saßmannshausen, Jörg Radtke, Nino S. Bohn, Hassan Hussein, Dave Randall, Volkmar Pipek — 전원 지겐대(University of Siegen), 독일. ACM DIS 2021 발표. |
| 도시·연도 | 독일(지겐대 소재 지역 추정, 정확한 도시·대상지 미확인) / 2021년(ACM Designing Interactive Systems 2021) |
| 증거 수준 | 연구 프로토타입. 실제 지자체 계획 절차에 투입된 기록은 없다. |
| AR 여부 | AR 맞음. Unity3D로 만든 AR 앱이 건축 프로젝트와 환경 변화를 실세계에 시각화한다. 다만 워크숍에서 쓴 레고·점토는 AR이 아닌 촉각적 설계 도구로, AR 시스템을 설계하기 위한 참여 수단이다. |
| 규모 | 인터뷰 40건 + 설문 1건 + 참여형 설계 워크숍 4회. 워크숍별 참여 인원, 연령 분포, 모집 방식은 전문 접근 실패로 확인하지 못했다. 실제 계획 프로젝트명도 미확인. |
| 기술 | Unity3D로 개발한 AR 앱. 기기·SDK·정합 방식 미확인. 병행 도구: 레고, 점토 등 촉각적 3D 도구를 저기술 사용자의 AR 시스템 공동설계 수단으로 사용. |
| 출처 | https://doi.org/10.1145/3461778.3462130 (ACM DIS 2021) · PDF: https://dl.acm.org/doi/pdf/10.1145/3461778.3462130 |

AR 참여의 가장 까다로운 문제, 즉 '고기술 도구를 설계하는 자리에 저기술 사용자를 어떻게 앉히나'를 정면으로 다룬 연구다. 출발점은 냉정한 진단이다 — 도시계획의 기존 참여 절차는 유인이 빈약하고, 특히 젊은 시민에게 그렇기 때문에 중요한 시민 요구가 아예 배제된다. 지겐대 연구진은 Unity3D로 AR 앱을 만들어 건축 프로젝트와 환경 변화를 시각화하고 시민이 설계 아이디어를 낼 수 있게 했다. 여기까지는 다른 연구와 비슷하다. 차별점은 방법론이다. 인간중심설계 접근으로 여러 이해관계자를 불러 인터뷰 40건과 설문을 수행하고, 이어 참여형 설계 워크숍 4회를 통해 시민이 직접 상호작용 개념을 발전시키게 했다. 그 워크숍에서 저기술 사용자를 참여시키기 위해 레고나 점토 같은 촉각적 3D 도구를 썼다 — AR이라는 고기술 시스템을 설계하는 자리에 기술에 익숙하지 않은 사람을 앉히는 우회로다. 저자들은 이것을 별도의 기여로 명시한다. 결과는 AR이 도시계획 참여 동기를 높일 수 있다는 것, 그리고 AR을 협업적으로 쓰고 기존 참여 절차 안에 박아 넣는 방법의 제안이었다.

AR이 도시계획 참여 동기를 높일 수 있다는 것을 보였고, AR을 협업적으로 쓰고 기존 참여 절차에 통합하는 방안을 제안했다. 그러나 실제 지자체 절차에 들어가 설계를 바꾼 기록은 없다. 피인용 73회로 이 축에서 영향력이 큰 논문인데, 그 기여가 'AR로 설계를 바꿨다'가 아니라 '저기술 사용자를 고기술 도구 설계에 참여시키는 방법을 만들었다'는 점에 있다는 것이 이 축의 현실을 요약한다.

### 지표 평가 기반 AR 시민참여 플랫폼 (호놀룰루)
| 항목 | 내용 |
| --- | --- |
| 주체 | Yuchen Wang, Yin-Shan Lin — 하와이대 마노아 건축대학(School of Architecture, University of Hawaii at Manoa). 미국. |
| 도시·연도 | 미국 하와이 호놀룰루, 전형적 도시 환경의 가로 모퉁이 공지 / 논문 2023년(Frontiers in Virtual Reality), 2024년 정정문(corrigendum) 게재 |
| 증거 수준 | 연구 프로토타입(현장 사용자 연구). 실제 도시설계 지침이 이 결과로 바뀐 기록은 없다. |
| AR 여부 | AR 맞음. 마커·GPS 없이 AR Plane Manager의 평면 검출과 점군으로 마커리스 정합해, 실제 가로 모퉁이 공지에 가상 모델을 겹쳤다. |
| 규모 | 유효 데이터 50명. 연령: 18~25세 11명, 26~60세 12명, 61세 이상 27명. 모집: 무작위로 접근한 행인(passers-by). 학습 효과: 정답 수 평균 2.6 → 4.5, 중위값 2.5 → 5.0. |
| 기술 | 안드로이드 스마트폰. Unity 2021.3.9f1(Windows 11), AR Foundation + XR Interaction Toolkit(신 XR Tech Stack). 정합은 AR Plane Manager 컴포넌트의 마커리스 평면 검출과 점군 — GPS도, 인공 마커도 쓰지 않았다. 평가 지표 6종: FAR, CVG, 높이 제한, 녹지율, 투과율, 접선율. |
| 출처 | https://doi.org/10.3389/frvir.2023.1071355 (Frontiers in Virtual Reality 4:1071355, 오픈액세스) · 정정문: https://doi.org/10.3389/frvir.2024.1424951 |

고령자를 표본에 실제로 많이 넣은, 이 축에서 드문 연구다. 표본 50명 중 61세 이상이 27명 — 절반이 넘는다. 문제 설정은 도시설계 참여의 가장 추상적인 벽이다. 하향식 도시설계 의사결정은 결과 검토에 오래 걸리고 시행 후에는 되돌릴 수 없는 영향을 남긴다. 그래서 상향식 참여가 필요한데, 용적률이나 건폐율 같은 '지표'라는 추상적 개념이 들어가는 순간 일반 시민은 참여할 수 없다. 하와이대 연구진의 접근은 지표를 눈에 보이게 만드는 것이었다. 안드로이드 스마트폰 AR로 도시설계 결과 장면을 실세계에 겹쳐 보여주고, 시민이 프로토타입 설계안과 상호작용하면서 6개 형태 지표 — 용적률(FAR), 건폐율(CVG), 높이 제한, 녹지율(GR), 투과율(porosity), 접선율(near-line rate) — 의 초기값을 직접 평가하게 했다. 이 과정에서 시민이 지표 개념 자체에 익숙해지고, 그래서 나중에 공표될 도시설계 지침의 함의를 더 잘 이해하게 된다는 것이 설계 의도였다. 학습 효과는 측정됐다. 정답 수 평균이 사전 2.6에서 사후 4.5로, 중위값은 2.5에서 5.0으로 올랐다. 참여자는 학생이 아니라 무작위로 접근한 행인이었다.

실제 도시설계 지침이 바뀌었다는 보고는 논문에 없다. 저자가 밝힌 한계 6개가 조경·도시 AR 참여의 기술적 천장을 그대로 보여준다. (1) 지표가 여러 개면 서로 충돌할 소지가 있다. (2) 스마트폰 AR의 오클루전 성능은 거리가 멀어지면 떨어진다. (3) 대규모 가상 모델에서는 몰입감이 줄어든다. (4) 여러 환경에 걸쳐 시민 참여를 지속시키기 어렵다. (5) 안전하게 볼 수 있는 동선을 확보하려면 물리적 공간 제약이 있다. (6) 대상지 모델링이 수작업이고, 갱신하려면 프로그래밍 기술이 필요하다. 2024년에 정정문이 게재됐으나 정정 내용은 확인하지 못했다.

### 빈·루체른 도시계획 참여의 AR 적용 (GAIA 사례연구)
| 항목 | 내용 |
| --- | --- |
| 주체 | Frank Othengrafen, Lars Sievers, Eva Reinecke. 소속 기관이 OpenAlex 및 접근 가능한 서지정보에 비어 있어 확인하지 못했다. |
| 도시·연도 | 오스트리아 빈 + 스위스 루체른 / 논문 2023년(GAIA - Ecological Perspectives for Science and Society 32권 Supplement 1, pp.54-63) |
| 증거 수준 | 공공 시범사업 사례연구(저자가 '사례연구'로 명시). 두 사례의 발주 주체와 규모는 확인하지 못했다. |
| AR 여부 | AR 맞음(초록 기준). 다만 두 사례에서 쓰인 구체적 도구와 정합 방식을 확인하지 못했으므로, AR로 분류되는 근거는 저자 서술에 의존한다. |
| 규모 | 두 사례의 프로젝트 명칭, 발주처, 연도, 참여 인원을 전문 접근 실패로 확인하지 못했다. 초록만 확보. |
| 기술 | 사용된 AR 도구·기기·정합 방식을 확인하지 못했다. |
| 출처 | https://doi.org/10.14512/gaia.32.S1.9 (GAIA 32/S1, 2023) |

AR이 도시계획 참여 절차의 어느 단계까지 실제로 들어갔는지를 두 도시 사례로 점검한 연구다. 논지는 두 갈래다. 긍정 쪽에서, AR 적용은 참여 절차의 질을 높이고 지속가능한 도시 발전에 기여한다고 본다. 주민의 참여 동기를 높이고, 여러 시각화 형식을 통해 서로 다른 계획 구상을 더 현실감 있게 제시할 수 있기 때문이다. 부정 쪽 서술이 이 연구의 값이다. 저자들은 자기 사례연구가 보여주듯 그 잠재력이 아직 온전히 활용되지 않았다고 명시하며, 이유를 하나로 못 박는다 — AR이 계획의 모든 단계에서 쓰이지는 않고 있다는 것이다. 즉 AR은 특정 단계(주로 시각화·설명)에만 들어가고, 문제 정의나 대안 형성이나 의사결정 단계로는 확산되지 않았다는 진단이다. 이 축의 다른 문헌들이 대개 자기 프로토타입의 가능성을 말하는 반면, 이 연구는 실제 적용 사례를 놓고 '어디까지 갔고 어디서 멈췄나'를 물었다는 점에서 인용 가치가 있다.

저자 결론: AR 적용이 주민 참여 동기를 높이고 참여 절차의 질을 높여 도시의 지속가능한 전환을 촉발할 수 있다. 그러나 동시에 "이 잠재력은 아직 온전히 활용되지 않았으며, AR이 모든 계획 단계에서 쓰이고 있지는 않다"고 명시한다. 이 축에서 'AR 참여는 시각화 단계에 갇혀 있다'는 진단을 실제 적용 사례에 근거해 내놓은 드문 문헌이다.

### Smart-phone augmented reality for public participation in urban planning (오타고대, 2011)
| 항목 | 내용 |
| --- | --- |
| 주체 | Max Allen, Holger T. Regenbrecht, M. Abbott — 오타고대(University of Otago), 뉴질랜드. |
| 도시·연도 | 뉴질랜드(도시 미확인, 오타고대 소재지 더니든 추정이나 확인 못함) / 2011년, OzCHI(제23회 호주 컴퓨터-인간 상호작용 학술대회) |
| 증거 수준 | 연구 프로토타입(추정). 초록 미확보로 실증 수준을 확정하지 못했다. |
| AR 여부 | AR 맞음(제목·시기 기준). 다만 실제 정합 방식과 구현 내용을 확인하지 못했으므로 '부분적으로 확인'이라고 보는 것이 정확하다. 2011년 모바일 AR은 통상 GPS·나침반 기반이었다. |
| 규모 | 참여 인원, 대상 계획 사안, 실험 규모를 확인하지 못했다. ACM DL 접근 차단으로 초록도 얻지 못했다. 피인용 91회(OpenAlex 기준). |
| 기술 | 확인하지 못했다. 2011년 시점의 모바일 AR이므로 GPS·나침반·가속도계 기반 센서 정합일 가능성이 높으나 이는 추정이다. |
| 출처 | https://doi.org/10.1145/2071536.2071538 (OzCHI 2011, Proceedings of the 23rd Australian Computer-Human Interaction Conference) — 전문 접근 실패 |

이 축의 계보 첫머리에 놓이는 논문이다. 2011년, 즉 ARKit(2017)이나 ARCore(2018)보다 6~7년 앞서, iPhone 4 세대의 스마트폰으로 도시계획 시민참여에 AR을 쓰겠다고 제안한 연구다. 뉴질랜드 오타고대 정보과학과의 Holger Regenbrecht 연구실에서 나왔고 — Regenbrecht는 AR·원격현장감 분야의 오래된 연구자다 — 피인용 91회로 이 축에서 가장 많이 인용된 초기 문헌에 속한다. 이 시기의 AR은 GPS와 나침반, 가속도계에 의존한 '센서 기반 AR'이었고 SLAM은 모바일에 없었다. 따라서 이 논문의 값은 기술적 성취가 아니라 시기에 있다 — 스마트폰에 AR을 실어 도시계획 참여에 쓴다는 발상이 2011년에 이미 제시됐고, 그로부터 15년이 지난 지금도 이 축의 문헌 대부분이 여전히 프로토타입 단계에 머물러 있다는 사실이 이 논문의 존재로 드러난다. 다만 이 항목은 정직하게 말해 서지정보 수준에서만 확인된 것이다. ACM Digital Library가 봇 접근을 차단해 초록조차 얻지 못했다.

확인하지 못했다. 후속 상용화나 지자체 채택 기록도 찾지 못했다. 이 항목의 인용 가치는 '2011년에 이미 이 발상이 제시됐다'는 연대 표지에 있으며, 단행본에 쓸 때는 내용을 서술하지 말고 연대와 피인용만 언급하는 것이 안전하다.

### 반둥 청소년 AR 학습 기반 도시환경계획 참여
| 항목 | 내용 |
| --- | --- |
| 주체 | Teti Armiati Argo(반둥공과대 지역·도시계획 프로그램, Jalan Ganesha 10, Bandung 40132), Shinta Prabonno(Bandung Creative City Forum), Prima Singgi(BCCF 및 반둥공과대). 인도네시아. |
| 도시·연도 | 인도네시아 반둥 / 2016년(Procedia - Social and Behavioral Sciences) |
| 증거 수준 | 확인하지 못했다. 학술대회 논문(Procedia)으로 연구 프로토타입 또는 교육 프로그램 수준일 가능성이 높다. |
| AR 여부 | 확인하지 못했다. 제목은 'Augmented Reality Learning'이라고 명시하지만 초록 미확보로 실세계 정합 여부를 판정할 수 없다. 교육용 마커 AR일 가능성이 있다. |
| 규모 | 확인하지 못했다. 참여 청소년 수, 기간, 예산 모두 공백. 피인용 11회. |
| 기술 | 확인하지 못했다. |
| 출처 | https://doi.org/10.1016/j.sbspro.2016.06.149 (Procedia - Social and Behavioral Sciences, 2016) — 초록·전문 접근 실패 |

비서구·글로벌사우스에서 청소년 AR 참여를 시도한 드문 사례다. 인도네시아 반둥공과대(ITB) 지역·도시계획 프로그램의 Teti Armiati Argo가 주저자이고, 공동저자 두 명이 Bandung Creative City Forum(BCCF) 소속이라는 점이 특징이다 — BCCF는 반둥의 실제 도시 시민단체로, 학술 연구가 아니라 지역 조직과 함께 움직였다는 뜻이다. 접근 방식도 다르다. 제목이 밝히듯 이 연구는 AR을 '설계 도구'가 아니라 '학습(learning)' 매개로 놓았다 — 청소년에게 도시 환경계획을 가르치는 수단으로 AR을 쓰고, 그 학습을 통해 참여로 넘어가게 하는 경로다. 오슬로 사례가 청소년에게 직접 나무를 놓게 한 것과 대비된다. 이 항목은 서지정보와 소속 기관까지만 확인됐다. Elsevier와 OpenAlex 모두 초록이 비어 있어 참여 인원, 실제 진행 방식, 사용 기술, 계획 반영 여부를 전혀 확인하지 못했다. 단행본에 쓸 때는 '이런 시도가 2016년 반둥에 있었다'는 사실 표지로만 쓰고, 내용을 서술하지 말아야 한다.

확인하지 못했다. 실제 계획 반영 여부, 후속 진행 모두 미확인.

### Take a Look Through My Eyes — AR 계획 소통 시스템 (TUM)
| 항목 | 내용 |
| --- | --- |
| 주체 | Michael Mühlhaus, Sarah Louise Jenney, Frank Petzold — 뮌헨공과대(Technische Universität München), 독일. CAADRIA 2018 발표. |
| 도시·연도 | 독일(대상지 없음 — 시스템 개념 연구) / 2018년(CAADRIA 2018 Proceedings Vol.1, pp.379-388) |
| 증거 수준 | 연구 프로토타입. 시민 실사용 시험 없음 — 논문은 '작동하는 프로토타입'을 만들었다고만 하고, 사용자 프로필 요구사항은 '다가오는 연구 과제'에서, 현장 AR 소통 요구사항은 '학생 과제'에서 조사할 예정이라고 결론에 적는다. |
| AR 여부 | AR 맞음(프로토타입 수준). Unity 기반으로 Vuforia·ARCore·ARKit·HoloLens를 배포 대상에 포함시켰다. 다만 실제 현장 정합 시험 기록은 논문에 없다. |
| 규모 | 시민 참여자 없음. 실증 규모 0. 후속 계획으로 '대형 주택회사와 협력하는 연구 과제'에서 사용자 프로필 요구사항을 분석하고, '학생 프로젝트'에서 현장 AR 소통 프로토타입을 만들겠다고 밝혔다. |
| 기술 | 파라메트릭-의미론적 페트리넷 도시 모델(USP 계획도구) 기반. Unity를 주로 렌더 엔진으로 사용하며 VR(Oculus Rift, SteamVR, Windows Mixed Reality)과 AR(Vuforia, ARCore, ARKit, HoloLens), Android·iOS 태블릿·스마트폰, 브라우저 배포를 소소한 수정으로 지원하도록 설계. 사용자 프로필·상황 템플릿·시각지각 파라미터로 정보를 개인화. |
| 출처 | http://papers.cumincad.org/data/works/att/caadria2018_284.pdf (CAADRIA 2018) · https://doi.org/10.52842/conf.caadria.2018.1.379 |

'만들었지만 시민에게 써보지 못한' 사례로 정직하게 기록해야 할 연구다. 뮌헨공대(TUM) 연구진이 도시계획 소통의 근본 문제에서 출발했다. 계획을 만드는 사람(전문가)과 그것을 따라야 하는 사람(다른 전문가 또는 초보자)이 같은 이해나 배경을 갖지 않을 때 '계획'에 관한 소통은 어려워진다. 저자들은 Rittel의 '불명확한 문제(ill-defined problem)' 개념을 끌어와, 계획 문제는 확정적으로 표현할 수 없고 끝이 정의되지 않으며 해답이 무한하고 옳거나 틀린 것이 아니라 좋거나 나쁠 뿐이라고 정리한다. 그래서 소통은 계획의 품질이 아니라 계획 성공의 필수 매개라는 것이다. 독일은 건축허가 신청 수리 전에 계획안을 공개 열람·질의·의견 제출에 부쳐야 하므로, 이 문제는 제도적 문제이기도 하다. 만든 것은 파라메트릭 도시 모델에 기반한 AR 다중 클라이언트 소통 프로토타입이다. Unity를 주로 렌더 엔진으로 써서, VR(Oculus Rift·SteamVR·WMR)과 AR(Vuforia·ARCore·ARKit·HoloLens), 안드로이드·iOS 태블릿·스마트폰, 브라우저까지 소소한 수정으로 배포할 수 있게 설계했다. 핵심 발상은 정보의 개인화다 — 계획 데이터의 선별·처리·시각화가 개별 이해관계자의 지식·기술 수준, 문화적 배경, 관심사를 고려하고, 사회자의 중재와 시점 전환 기능으로 이해를 돕는다.

실제 시민 참여에 투입되지 않았다. 저자들은 결론에서 '구현된 작동 프로토타입이 개념을 증명한다'고 쓰면서도, 물리적·인지적 접근성 개선만으로는 부족하고 절차가 더 동기부여적이어야 한다며 게임화(레벨·리더보드·점수, 계획가가 퀘스트를 내고 지역 지식을 활용)를 향후 과제로 남긴다. 마지막 문장은 "시스템 개념의 개별 구성요소들을 하나로 모아야 한다"다 — 즉 시스템도 완결되지 않았다. 이 축에서 '프로토타입에서 멈춘 사례'의 전형이며, 저자가 그것을 숨기지 않았다는 점에서 인용 가치가 있다.

### AR/Urban 및 Participatory AR — 마커 기반 촉각 인터페이스 참여 도구 (빅토리아 웰링턴)
| 항목 | 내용 |
| --- | --- |
| 주체 | 빅토리아대학 웰링턴(Victoria University of Wellington) 소속 연구. 학위논문 'AR/Urban: Exploring Augmented Reality for Participatory Urban Design'과 학술대회 논문 'Participatory AR - A Parametric Design Instrument'(CAADRIA 2021)가 같은 계보다. 저자명은 확인하지 못했다. |
| 도시·연도 | 뉴질랜드 웰링턴 / CAADRIA 2021, 학위논문 연도 미확인 |
| 증거 수준 | 연구 프로토타입(석사학위 논문 + 학술대회 논문). 실제 주민 워크숍 적용 기록 없음. |
| AR 여부 | AR 맞음. 다만 실세계 대지 정합이 아니라 이미지 마커(Vuforia 타깃) 위에 모델을 띄우는 마커 기반 AR이다 — 실내 테이블에서 쓰는 촉각 인터페이스에 가깝고, 현장 1:1 정합 사례가 아니다. |
| 규모 | 일반인 참여자 수, 시험 규모, 기간 모두 논문에 제시되지 않았거나 확인하지 못했다. |
| 기술 | 실시간 가상 엔진(게임엔진) + XR + 파라메트릭 백엔드. Vuforia의 virtual buttons 기능을 인코딩한 이미지 기반 AR 마커로 촉각 인터페이스(TUI) 구성. 마커 조작으로 파라메트릭 설계 대안 순환. 1인칭 시점 관람 병행. HoloLens 같은 HMD를 의도적으로 배제했다 — 전문성이나 안내자를 요구하기 때문. |
| 출처 | https://doi.org/10.26686/wgtn.15085743 (AR/Urban 학위논문) · https://doi.org/10.52842/conf.caadria.2021.2.295 · PDF: http://papers.cumincad.org/data/works/att/caadria2021_312.pdf |

'일반인이 도면을 못 읽는다'는 문제를 AR의 정합 정밀도가 아니라 조작 방식으로 풀려 한 사례다. 저자들의 진단은 이렇다. CAD 연구는 대규모 도시설계 재개발의 시민참여를 오랫동안 다뤘고 해법도 많이 내놨지만, 반복되는 문제는 일반인이 2D·3D 그래픽 정보를 효과적으로 해석하지 못해 설계 전개에 능동적으로 참여할 수 없다는 것이다. 그리고 기존 연구 대부분은 HoloLens 같은 최신 기기를 쓰는데, 그런 기기는 맞춤 인터페이스와 상당한 전문성 또는 숙련된 안내자를 요구한다. 그래서 이들은 반대 방향으로 갔다. 실시간 가상 엔진과 XR, 파라메트릭 백엔드를 묶고, 조작은 촉각적 사용자 인터페이스(TUI)로 했다. 구체적으로는 Vuforia의 '가상 버튼(virtual buttons)' 기능을 이미지 타깃에 심은 AR 마커를 만들어, 일반인이 그 마커를 만지고 움직이는 것만으로 파라메트릭 설계 대안들을 순환시킬 수 있게 했다 — 일반인에게는 없는 수준의 '연산적 유창성'을 손으로 얻게 한 셈이다. 동시에 1인칭 시점 관람을 권장해 2D에서 3D로의 번역, 대지 위 건물 배치 같은 구체적 이해 장벽을 다뤘다.

실제 참여 절차 적용 기록 없다. 이 사례의 값은 '접근성을 높이는 방향이 정합 정밀도가 아니라 조작 방식일 수 있다'는 반대 방향 제안에 있다. 기기 진입 장벽을 문제로 명시하고 HMD를 버렸다는 점에서, 배제 문제를 기술 선택으로 다룬 드문 사례다. 후속 상용화나 지자체 채택은 확인되지 않았고, 학위논문 프로토타입으로 남았을 가능성이 높다.

### 오프사이트·온사이트·온라인 참여 환경 통합 시스템 (하펜시티 함부르크)
| 항목 | 내용 |
| --- | --- |
| 주체 | Patrick Postert, Jochen Schiewe(하펜시티대학 함부르크, HafenCity University Hamburg), Anna E. M. Wolf(함부르크응용과학대, HAW Hamburg). 독일. |
| 도시·연도 | 독일 함부르크 / 2022년(ISPRS International Journal of Geo-Information 11(3):156) |
| 증거 수준 | 연구 프로토타입. 저자 스스로 "상세한 실증 사용성 연구는 아직 진행 중(still pending)"이라고 명시했고, 근거로 제시한 것은 사전 테스트(pretests)뿐이다. |
| AR 여부 | 부분적. 시스템에 AR 기기가 포함되지만 AR은 세 참여 환경 중 '온사이트' 한 축을 담당하는 구성요소이며, 논문 전체는 터치테이블·VR·AR·온라인을 묶는 동기화 아키텍처다. AR 단독 사례로 인용하면 과장이다. |
| 규모 | 사용성 연구 미수행. 사전 테스트만 언급되며 인원·규모는 제시되지 않았다. 실제 계획 절차 적용 없음. |
| 기술 | 인터랙티브 터치 테이블 + 추가 화면 + VR 기기 + AR 기기를 실시간 동기화. 세 참여 환경(오프사이트·온사이트·온라인) 통합. 기기 횡단 통일 상호작용 개념, 매우 낮은 지연의 실시간 동기화, 협업 중 상태의 지속적 저장이 세 가지 기술 요건. 구체적 기기명·SDK·정합 방식은 확인하지 못했다. |
| 출처 | https://doi.org/10.3390/ijgi11030156 (ISPRS IJGI 11(3):156, 오픈액세스) · PDF: https://www.mdpi.com/2220-9964/11/3/156/pdf |

참여 도구를 하나 더 만드는 대신, 흩어진 도구들을 실시간으로 묶으려 한 연구다. 문제 인식이 실무적이다. 도시계획에서 참여자 관여 수요는 크고 이해관계자 간 소통과 절차 투명성을 위한 도구가 절실하지만, 지금까지 일반적 방법들은 서로 다른 도구와 플랫폼을 각각 따로 쓴다. 그래서 효과적이고 효율적이고 창의적인 협업의 잠재력이 온전히 실현되지 않는다는 것이다. 함부르크 연구진의 해법은 세 가지 참여 환경 — 오프사이트(현장 밖), 온사이트(현장), 온라인 — 을 하나로 잇는 것이었다. 인터랙티브 터치 테이블과 추가 화면, 그리고 VR·AR 기기를 실시간 동기화했다. 기술적으로 세 가지를 풀어야 했다. 첫째, 다양한 환경과 기기 요구에 맞는 통일적·기기 횡단 상호작용 개념. 둘째, 참여 과정의 모든 변경 — 객체 추가·조작·삭제 — 이 모든 기기에 매우 낮은 지연으로 실시간 동기화되어야 한다. 셋째, 협업 과정 중 여러 상태가 지속적으로 저장되어야 한다. 프로토타입까지는 갔다. 그런데 이 논문에서 가장 정직한 문장이 결론에 있다 — 상세한 실증 사용성 연구는 아직 진행 중이며, 사전 테스트가 개념이 좋게 평가받았고 다른 계획 절차로 이식 가능하다는 것을 시사한다고만 쓴다.

저자 결론 그대로: "Detailed empirical usability studies are still pending; however, pretests indicate that the concept is appreciated, and the transferability to other planning processes is given." 즉 개념과 프로토타입까지이고 사용자 검증은 미완이다. 이 축에서 '참여 도구 통합'을 시도한 대표 문헌으로 인용되지만, 실제 참여자 데이터가 없다는 점을 밝히지 않고 인용하면 오독이 된다.

### 공간증강현실(SAR)이 공동설계 세션의 참여도에 미치는 영향 — 사례연구
| 항목 | 내용 |
| --- | --- |
| 주체 | Maud Poulin(HES-SO 서부스위스 응용과학예술대, Haute Ecole Arc Ingénierie), Cédric Masclet, Jean-François Boujut(그르노블 공과대학 Institut polytechnique de Grenoble, CNRS, 설계·최적화·생산과학연구소 G-SCOP, 그르노블알프대). 스위스·프랑스. |
| 도시·연도 | 스위스·프랑스(대상지 미확인) / 2024년 게재(Computers in Industry, 온라인 2023) |
| 증거 수준 | 연구 프로토타입(사례연구, case study). 실제 납품이나 공공사업이 아니다. |
| AR 여부 | AR 맞음(방식은 투영형). 공간증강현실은 프로젝터로 실물 표면에 정합해 투영하는 AR의 한 계열이며 VR이 아니다. 다만 휴대기기를 통해 실세계를 보는 방식과는 정합 원리가 다르다. |
| 규모 | 공동설계 세션 수, 참여 인원, 측정 지표를 확인하지 못했다. 초록 미확보. 피인용 3회. |
| 기술 | 공간증강현실(SAR) — 프로젝션 기반. 구체적 장비, 투영면(실물 모형 여부), 정합 방식은 확인하지 못했다. |
| 출처 | https://doi.org/10.1016/j.compind.2023.104023 (Computers in Industry, 2024) — 초록·전문 접근 실패 |

'AR이 참여를 늘린다'는 통념을 측정 대상으로 놓은 연구다. 대부분의 참여 AR 연구가 설문으로 '참여 의향이 높아졌다'를 보고하는 데 그치는 반면, 이 연구는 공동설계 세션에서 설계자와 사용자 사이의 상호작용을 분석해 사용자 참여도(user participation) 자체를 측정하려 했다. 쓴 기술도 다르다. 휴대기기 AR이 아니라 공간증강현실(Spatial Augmented Reality, SAR) — 프로젝터로 실제 물체나 모형 표면에 직접 정보를 투영하는 방식이다. 이 방식은 안경이나 화면을 들지 않아도 되므로, 여러 사람이 같은 것을 동시에 보며 손으로 가리키고 토론하는 공동설계 자리에 원리적으로 적합하다. 결과는 AR 기술이 사용자 참여도를 높이는 데 기여하는 것으로 나타났다. 단, 이 항목에는 중요한 유보가 붙는다. 게재지가 Computers in Industry이고 저자들이 산업 설계·제조 연구 계열(그르노블 LS2N 계열 및 스위스 HES-SO)이므로, 대상이 도시·조경 공동설계가 아니라 산업 제품·공정 설계일 가능성이 높다. 초록을 확보하지 못해 이를 확정하지 못했다. 조경 참여 사례로 인용하기 전에 반드시 원문으로 대상 영역을 확인해야 한다.

AR 기술이 사용자 참여도를 높이는 데 기여하는 것으로 나타났다는 수준까지만 확인됐다. 대상이 도시·조경 설계인지 산업 설계인지 확정하지 못했으므로, 이 항목은 '참여도를 정량 측정하려 한 연구가 있다'는 방법론 표지로만 쓰고, 조경 사례로는 쓰지 않는 것이 맞다.

### 민주주의 지수와 도시계획 몰입·참여 기법 연구 강도의 상관 분석
| 항목 | 내용 |
| --- | --- |
| 주체 | Jan Kabrhel, Jan Maňas — 체코생명과학대 프라하(Czech University of Life Sciences Prague). 체코. |
| 도시·연도 | 국가 단위 비교(대상지 없음) / 2025년(PRESENCE: Virtual and Augmented Reality) |
| 증거 수준 | 연구(문헌계량·통계 분석). 현장 적용 없음. |
| AR 여부 | 아님(메타 연구). AR·VR 기법을 분석 대상으로 삼은 문헌계량·상관 분석 연구이며, 그 자체가 AR 시스템을 구현하거나 적용한 것이 아니다. |
| 규모 | 국가 단위 분석. GDP가 충분한 국가만 포함. 상관계수 r = 0.376, p ≪ 0.001. 포함 국가 수와 분석 대상 논문 수는 확인하지 못했다. |
| 기술 | 해당 없음. 방법: 도시계획 의도의 대중 제시 기법별 정의 수립 + 기법별 달성 가능 몰입 수준 정리 + 국가별 연구 강도 측정 + 민주주의 지수와의 상관 분석. |
| 출처 | https://doi.org/10.1162/pres.a.9 (PRESENCE: Virtual and Augmented Reality, 2025) |

이 축에서 '누가 배제되는가'를 개인이 아니라 국가 단위로 물은 유일한 연구다. 체코생명과학대 연구진은 먼저 도시계획 의도를 대중에게 제시하는 개별 방법들 — AR·VR 신기법을 포함해 — 을 정의하고 각 기법이 달성할 수 있는 몰입 수준을 정리했다. 그다음 그 정의를 써서 나라별로 AR·VR 활용 연구가 얼마나 활발한지 강도를 측정하고, 그 강도와 그 나라의 민주주의 지수(Democracy Index, DI) 사이의 상관을 분석했다 — 국내총생산이 충분한 국가만 포함시켜 경제력 요인을 통제하려 했다. 결과는 통계적으로 유의했다. 상관계수 r = 0.376, p 값은 0.001보다 훨씬 작았다. 민주주의가 더 발달한 나라에서 이런 기법 연구가 더 활발하다는 것이고, 저자들도 '예상대로'라고 쓴다. 이 결과가 조경·도시 AR을 다루는 단행본에 중요한 이유는, 이 축의 문헌 지도 자체가 편향돼 있다는 것을 수치로 보여주기 때문이다. 오슬로·빈·취리히·잘츠부르크·함부르크·밀라노 — 지금까지 이 목록에 등장한 도시들의 목록이 그 편향의 결과다. 저자들은 마지막에 중요한 유보를 남긴다. 더 높은 수준의 가상화가 반드시 더 나은 참여를 뜻하지는 않는다는 것이다.

제시된 기법 정의들이 향후 연구의 결과 비교 가능성을 높이는 데 도움이 될 수 있다고 결론했고, 예상대로 민주주의가 더 발달한 국가에서 이런 기법 연구가 더 활발하다는 것을 확인했다. 그러면서 "더 높은 수준의 가상화가 반드시 [더 나은 참여를 뜻하지는] 않는다"는 유보를 남긴다. 이 축을 정리할 때 '참여 AR 사례가 왜 특정 나라들에만 있는가'라는 질문의 답으로 인용할 수 있는 유일한 정량 근거다.

#### 검증에서 잡힌 정정
- Boos et al. 권호 오류: 'Journal of Location Based Services 16권'이라 했으나 Crossref·OpenAlex 모두 Volume 17, Issue 1, pp.48-77(온라인 2022-06-12, 인쇄 2023-01-02)이다. 16권이 아니다.
- Boos et al. '전문 접근 실패'는 과장이다. 하이브리드 CC-BY로 ZORA(eprint 220841, file 8)와 ETH Research Collection(10.3929/ethz-b-000542298)에 전문이 공개 기탁돼 있다. 초록만으로도 피험자간 현장실험·측량틀 2과제+AR 6과제·LOD 3그룹이 확인되므로(조사가 이미 적은 내용) 접근 경로 누락에 가깝다.
- The Underline 저자 누락: 실제 저자는 9명인데 조사는 8명만 적었다. 9번째 저자 Jansen A. Estrázulas(FIU + Amazonas State University)가 빠졌다. 또 Cesar F. Amorim의 제2소속(Sao Paulo City University)이 누락되고, 표기가 'César Ferreira Amorim'으로 적혔으나 게재 바이라인은 'Cesar F. Amorim'이다. 게재 면수는 pp.1-8(논문번호 8341034).
- 오슬로 '정합은 GPS 기반으로 부정확했다'는 논문에 없는 서술이다. 논문은 부정확의 원인을 (a)이미지·영상 메타데이터 위치정보와 (b)AR 객체의 내부 좌표로 지목하고, 워크숍 후 연구팀이 수동으로 재배치했다고 적는다. 사용 스택은 Apple ARKit + 자체 Unity 앱 Udaru + Augment 패키지 + iScape 요소이며 GPS 기반 정합이라고 명시한 곳이 없다.
- 오슬로 '실측 수준에 못 미친다고 저자가 명시한다'는 직접 인용이 아니다. 실제 문장은 'not accurate enough for a direct translation from AR data to the planning system used by the municipality'로, 측량 등급(survey-grade) 비교가 아니라 지자체 계획시스템 직접 연동 불가를 말한다.
- 오슬로 '소프트웨어 Udaru'는 단순화다. Udaru(User-driven Augmented Reality Urbanism)는 혼합 스택 중 자체 Unity 구성요소 하나이며, 논문은 ARkit·Udaru·Augment·iScape의 혼합(a mix of)이라고 명시한다. Udaru를 단독 소프트웨어로 제시하면 과장이다.
- AR4CUP '납품된 상용 제품으로 남았는지는 확인 불가'는 반박된다. 밀라노공대 LABSIMURB 과제 페이지는 Software-as-a-Service 제품을 산출했고 LAVAL AWARD EUROPE 2021(제23회) 서비스 부문을 수상했으며 2020년 개발 지속이 계획됐다고 밝힌다. 데모·전시를 넘는 제품화 증거가 공개돼 있다.
- AR4CUP 예산을 조사가 공백으로 뒀으나 공개돼 있다. LABSIMURB 과제 페이지 기준 총예산 529,271유로, 기간 2019년 1월~12월이다.
- AR4CUP VITAE 설계자 귀속이 불완전하다. 조사는 Carlo Ratti Associati 단독으로 적었으나 과제 페이지는 Covivio, Carlo Ratti Associati, Habitech 3자를 개발·설계 주체로 명기한다.
- AR4CUP 논문 2건이 뒤섞였다. 조사는 2019 CTV DOI(10.5821/ctv.8622)에 저자를 'Piga, Stancato, Boffi, Rainisio'로 달았으나, CTV 2019 전문의 실제 바이라인 순서는 Piga, Boffi, Rainisio, Stancato이고 제목은 'Augmented Reality for Co-Design: The Perspective of Real Estate Developers, Architectural Firms, and Public Administrations'이다. CTV 2019는 1단계(인터뷰)만 다루며 본문에 '시범적용은 2019년 말에 수행될 예정'이라고 적어 63명/48명 수치를 담고 있지 않다. 그 수치는 후속 Sustainability 2021 논문('How Do Nature-Based Solutions’ Color Tones Influence People’s Emotional Reaction? An Assessmen
- BRISE 최고평가 활용사례 2건의 명칭이 틀렸을 가능성이 높다. 조사는 'UC05 관청 도면검토 디지털화, UC06 현장 시민 AR 도면검토'로 둘 다 도면검토로 적었으나, CC-BY 초록 원문은 'The best-rated AR use cases (plan checking and hearing during the permission process) will be further developed'로 두 번째를 허가절차의 청문(hearing)이라 명시한다. 이는 조사가 별도로 단 '실제 인접주민 청문에 투입된 증거는 없다'는 판단과도 긴장을 일으킨다 — 청문 활용사례가 바로 추가개발 대상 2건 중 하나다. (MDPI 차단으로 전문 대조는 못 했고 발행사 초록 근거다.)
- 반둥 항목의 'AR여부: 확인하지 못했다'와 '초록·전문 접근 실패'는 둘 다 사실과 다르다. 이 논문은 Procedia SBS vol.227, pp.808-814의 다이아몬드/오픈액세스이고 초록이 공개 색인돼 있다. 초록 원문은 'an apps is developed and refined through augmented reality and interactive storytelling based on local folklore'라고 AR을 저자가 직접 주장하며, 내용은 고교생의 수질오염·수역 영향 지식을 활용한 게임 시뮬레이션 + 데이터 수집이다. 즉 현장 1:1 설계 배치가 아니라 환경 모니터링·교육형 AR이며, 성과는 '지자체의 인식을 환기'하는 수준이다. 조사에 권·면수도 빠졌다.
- OzCHI 2011 '초록도 얻지 못했다'는 사실과 다르다. 초록이 공개 색인돼 있고 'Members of the public participated in a user study where they used the prototype system as part of a simulated urban planning event'라고 명시한다. 따라서 '연구 프로토타입(추정)'은 추정이 아니라 확인이며, 정합 방식도 '기존 실세계 건축물 위에 제안 설계의 3D를 겹쳤다'로 확인된다. 면수는 pp.11-20, 발표일 2011-11-28.
- 웰링턴 AR/Urban '저자명은 확인하지 못했다'는 사실과 다르다. 조사가 직접 링크한 cumincad PDF 1쪽에 DAVID SILCOCK, MARC AUREL SCHNABEL, TANE MOLETA, ANDRE BROWN(전원 Victoria University of Wellington)이 인쇄돼 있다. 학위논문 10.26686/wgtn.15085743의 제목은 'AR/Urban: Exploring Augmented Reality for Participatory Urban Design'이며 동일 주저자다. 마커기반 Vuforia라는 조사의 성격 규정은 본문에서 확인된다.
- Poulin SAR 항목은 도시·조경이 아니라 산업 제품 공동설계다. 조사는 '도시·조경 설계인지 산업 설계인지 확정하지 못했다'고 뒀으나 Crossref 자금 데이터가 Horizon 2020 grant 869984를 지목하고, 이는 CORDIS 기준 OPEN!NEXT 'Company-Community Collaboration for Open Source Development of products and services'(오픈소스 하드웨어 제품 개발, TU Berlin 주관 19개 파트너)다. 게재지 Computers in Industry, 공저자 소속 G-SCOP(설계·최적화·생산과학연구소)와 합쳐 산업·제품 설계로 확정된다. 이 축에 넣으면 도메인 오분류다. 부수 사항: HES-SO ArODES 기탁 파일명이 'Julmy_2023_...'이므로 주저자 표기(Poulin/Julmy)를 인용 전 확인해야 한다.
- Postert 항목 저자 순서 오류: 조사는 'Patrick Postert, Jochen Schiewe, Anna E. M. Wolf' 순으로 적었으나 실제 바이라인은 Postert, Wolf, Schiewe다(Wolf가 2저자, Schiewe가 3저자). 소속 귀속은 정확하다. 실제 제목은 'Integrating Visualization and Interaction Tools for Enhancing Collaboration in Different Public Participation Settings'(2022-02-22).
- GAIA 권호 미세 불일치(경미): 조사는 '32권 Supplement 1'이라 했고 DOI 슬러그(10.14512/gaia.32.S1.9)는 이를 뒷받침하나, Crossref·OpenAlex는 volume 32, issue 1, pp.54-63으로 기록한다. 인용 시 판본 표기를 확인할 필요가 있다. 한편 '소속 기관이 비어 있어 확인 못 함'은 정확하다 — OpenAlex·Crossref 모두 세 저자의 소속이 공백이며 나도 독립 확인하지 못했다.
- City Craft 2차 세션 분할 '8명+7명'은 확인되지 않았다. 전문은 2세션 총 15명(남5·여10)만 명시하고 8+7 분할을 제시하지 않는다. 그 외 이 항목의 모든 수치(1차 18명 남5·여13, 9쌍, 세션당 2시간, 30% 지인, 자금 Land Salzburg WISS 2025 '5G Exploration Space', 오픈액세스비 Paris Lodron University of Salzburg, 초기단계 4전문가+66명·N=10/28/6/6)는 전문에서 정확히 확인됐다. 게재 면수 CSCW 34:249-291이 조사에 빠졌다.
- Postert & Schiewe(IJGI 11(3):156) — 'AR여부: 부분적. 시스템에 AR 기기가 포함되지만'은 틀렸다. AR 앱은 미구현이다. 전문: 'Additionally, to the off-site focused prototypes for VR and touch tables, in the next step, we will develop the AR application for the presented on-site scenario and connect it with the presented prototype.' 구현된 것은 터치테이블+VR(Oculus Quest 1/2)의 오프사이트 프로토타입뿐. (프로젝트명 PaKOMM) https://www.mdpi.com/2220-9964/11/3/156
- Postert 항목 '사전 테스트만 언급되며 인원·규모는 제시되지 않았다' — 제시돼 있다. 2021년 10월 함부르크 사진박람회에서 13명(여6·남7, 20~56세, 평균 32, SD 12)이 설문을 완료했고, 7명은 VR+터치테이블, 2명은 VR만, 4명은 터치테이블만 테스트했다. AR을 테스트한 사람은 0명이다.
- Mühlhaus et al.(CAADRIA 2018) 'Unity 기반으로 Vuforia·ARCore·ARKit·HoloLens를 배포 대상에 포함시켰다' — 오독. 원문은 Unity의 일반적 다중 플랫폼 지원을 설명하는 문장이며(VR로 HTC-Vive·Oculus Rift·SteamVR·WMR도 같은 괄호에 나열됨) 이 프로토타입의 배포 대상 선언이 아니다. Figure 3 캡션은 'Unity augmented reality mockup', 결론은 'the suggested prototype uses augmented reality'다.
- Poulin et al.(Computers in Industry, 2024) '대상이 도시·조경 설계인지 산업 설계인지 확정하지 못했다' — 산업 제품 공동설계로 확정된다. 동일 저자·동일 SAR 플랫폼 선행 논문이 'collaborative product co-creativity sessions'(hal-02360201), 'Exploring Tablet Interfaces for Product Appearance Authoring in Spatial Augmented Reality'(IJHCS 2021, 10.1016/j.ijhcs.2021.102719)라고 명시. 소속은 설계·최적화·생산과학연구소 G-SCOP. 조경·도시 참여 사례가 아니므로 이 축에서 빼야 한다. 피인용도 3회가 아니라 4회(Semantic Scholar) / 3회(OpenAlex)로 출처에 따라 다르다.
- Oslo(Reaver 2023) '정합은 GPS 기반으로 부정확했고' — 틀렸다. 정합은 ARKit이다. 원문: 'This prototype utilized a mix of ARkit from Apple, a custom piece of software in Unity titled Udaru (User-driven Augmented Reality Urbanism), the Augment software package, and elements from iScape, an AR landscape app.' 부정확하다고 한 대상은 (a) 사진·영상의 위치 메타데이터('this is not accurate enough')와 (b) 객체의 내부좌표('also not precise enough and required manual positioning by the research team after the workshops')로, 현장 중첩이 아니라 계획좌표계 지오레퍼런싱이다. 또 '실측 수준에
- Oslo '소프트웨어 Udaru' — 논문에서 Udaru는 본 워크숍 앱이 아니라 사전 프로토타입 구성요소 한 개의 이름으로 단 1회만 등장하고, 같은 프로토타입에 상용 앱 Augment와 iScape 요소가 함께 들어간다. 워크숍에서 실제로 쓴 앱의 이름은 논문에 나오지 않고 'the AR application'으로만 지칭된다.
- Oslo '워크숍당 3~5일' — 논문은 '3–4 days'다. 원문: 'We spent 3–4 days for a duration of approximately 4–5 h each day on this component of the workshop.'(하루 4~5시간, 하루 4~5개 지점은 맞음)
- BRISE-Vienna '전문가 인터뷰 14명, 5개 분야(용도지역·측량·건축·건축국·소방)' — 소방은 없다. Table 1의 분야는 District planning and zoning, Architecture and urban design/Architecture, Building authority, Geo-information·Photogrammetry·Survey(3D모델링/측량), Innovation 다섯이다. 소방(fire department)은 절차 분석의 이해관계자 목록에만 나오고 14명 인터뷰 대상에는 포함되지 않는다. 평균 인터뷰 시간은 약 2시간.
- BRISE-Vienna '실세계 대지에 허가 신청 건물을 겹쳐 보는 것이 05·06번 활용사례의 핵심이다' — UC05에는 틀렸다. UC05는 'Digitisation of plan checking and hearing at the authority's office using AR'로 관청 실내용이며, 논문은 'can be implemented directly due to the lack of reference to existing buildings'라고 명시한다(기존 건물 참조가 없어서 바로 구현 가능). 현장 실세계 중첩은 UC06('AR plan checking for citizens on-site')뿐이고 이쪽은 '1~5년 내 구현 가능'으로 분류됐다. 또 UC05 명칭에서 '청문(hearing)'이 누락됐다.
- BRISE-Vienna '총 사업비 미확인' — 확인된다. UIA 프로젝트 페이지 기준 BRISE-Vienna 총사업비 €4,859,418.56, 파트너는 빈시·TBW-ODE·WH Media·TU Wien·건축사·엔지니어협회(Chamber of Architects and Civil Engineers). https://uia.urban-initiative.eu/en/uia-cities/vienna-call4
- Boos et al. '정확한 피험자 수, 연령, 모집 방식, 실험 일자를 전문 접근 실패로 확인하지 못했다' — 전부 확인된다(조사표가 링크한 ETH 리포지토리의 CC-BY 전문). 참여자 30명(여18·남12), 21~58세, 취리히대·ETH 메일링리스트와 대학 홈페이지 공고로 모집, 도시 출신 12명·시골 18명, 학사이상 16명·고졸 10명·직업교육 4명, 색약 2명·시력저하 2명. 실험 기간 2020년 6월 26일~7월 31일. LOD 1/2/3 세 군에 10명씩 배정. https://www.research-collection.ethz.ch/handle/20.500.11850/542298
- Boos et al. '스위스(정확한 도시 미확인)' — 취리히 남부다. 논문에 좌표까지 있다: '(47.341 N, 8.520 E)'. Baugespann 사진 캡션은 'staked out on the project development ground in Zurich, Switzerland (47.341 N, 8.519 E) on 25th June 2020'.
- (외 41건)

## failures
항목 16개 · 검증 정정 지적 51건

> 조경·도시 분야 증강현실의 실패는 개별 프로젝트가 망한 이야기가 아니다. 프로젝트가 올라섰던 바닥이 통째로 꺼진 이야기다. 2015년 Metaio/Junaio, 2018년 Google Tango와 Layar·Blippar, 2023년 Unity Reflect와 VisualLive, 2024년 Wikitude와 HoloLens 2·Magic Leap 1, 2025년 Adobe Aero와 Trimble XR10. 옥외 지리정합 AR을 떠받친 SDK·기기·저작도구가 10년에 걸쳐 차례로 사라졌고, 그 위에 지어진 도시 규모 앱들은 자기 잘못 없이 죽었다. 크라이스트처치 지진 도시를 실물 크기로 겹쳐 보여준 CityViewAR이 대표적이다. 2011년 뉴질랜드 캔터베리대가 시의회·문화유산청 데이터로 만든 이 앱은 안드로이드 스토어에서 사라졌고, 곁들여 운영한 Junaio 채널도 2015년에 함께 끊겼다. 2021년 되살아난 iOS판은 파노라마 사진 뷰어다 — 되살아난 것은 앱이고, 사라진 것은 AR이다.  원인은 네 갈래로 갈린다. 첫째 기술 한계. 취리히에서 ETH·취리히대가 30명을 데리고 실제 학교 신축 부지에서 Baugespann(실물 골조 표시)과 ARKit 앱을 맞붙인 2023년 실험에서, 피험자는 AR 건물 높이를 약 31% 과대추정하고 길이는 과소추정했다. 드리프트와 캘리브레이션 오차가 크기 판단을 흐렸다. AR이 하려던 단 하나의 일, '크기를 몸으로 알게 하기'가 실패했다. 둘째 데이터 부재. 올보르대가 2025년 덴마크 업계 17명을 인터뷰한 결과, AR은 유용하지만 지하시설물의 실측 기록과 데이터 교환 체계가 없어 효용이 나오지 않는다고 결론냈다. 셋째 비용과 업무흐름. 1만 5천 달러 건설용 스마트헬멧을 팔던 Daqri는 2억 7,500만 달러를 태우고 2019년에 문을 닫았다. 같은 겨울에 Meta와 ODG가 함께 무너졌다. 넷째 사업성. Snap은 AR 기업사업부를 7개월 만에 접었고, 니안틱은 8th Wall 엔진을 오픈소스로 풀면서 도시 정합의 핵심인 Lightship VPS는 빼놓았다.  없는 것도 분명하다. 조경설계사무소가 AR을 도입했다가 접었다는 1차 기록을 찾지 못했다. 옥외 AR의 실제 예산은 '식물을 어떻게 보여줄까'가 아니라 그라츠 VIDENTE부터 덴마크 굴착까지 일관되게 '파기 전에 땅 밑을 보자'에 쓰였다.


### Unity Reflect · VisualLive 일몰 (2023~2024)
| 항목 | 내용 |
| --- | --- |
| 주체 | Unity Technologies. VisualLive는 2021년 Unity가 인수한 미국 스타트업. 전환 대안으로 Unity가 지정한 업체는 아이슬란드 Arkio. Unity Reflect Review에서 Arkio로 갈아탄 사용자로 노르웨이 엔지니어링·설계사 Norconsult가 공개 언급됐다. |
| 도시·연도 | 글로벌, 2019 출시 → 2023년 8월 일몰 발표 → 2024년 6월 30일 서비스 종료 |
| 증거 수준 | 실제 납품 — 상용 판매된 제품의 단종. 발표가 아니라 유료 고객이 있던 제품이 끊겼다. |
| AR 여부 | 부분적. VisualLive는 AR 맞음 — HoloLens 2·iPad로 BIM 모델을 실제 현장 좌표에 정합해 겹쳤다. Unity Reflect 본체는 화면·VR 설계검토가 중심이고 AR 뷰어가 부가 기능이었다. |
| 기술 | Revit·Navisworks·SketchUp·Rhino 직결 플러그인, 자체 동기화 서버. VisualLive는 HoloLens 2 / iOS. 파일 포맷(IFC·FBX·DWG) 미지원이 구조적 제약이었다. |
| 출처 | https://www.arkio.is/blog/arkio-unity-reflect/ · https://www.linkedin.com/posts/cdiggins_unity-reflect-activity-7098008146949861376-HMOm · https://www.reddit.com/r/HoloLens/comments/13rmgnm/visuallive_no_new_purchases_offline_63024/ · (리다이렉트 확인) https://unity.com/products/visuallive |

Unity는 2019년 AEC 전용 실시간 시각화 플랫폼 Unity Reflect를 내놓고 Revit·Navisworks·SketchUp·Rhino와 메모리-투-메모리로 직결시켰다. 2021년에는 HoloLens 2와 iPad에서 BIM 모델을 실제 건설 현장에 1:1로 겹쳐 보여주는 VisualLive를 인수해 AR 축을 보강했다. 그러나 2023년 8월 Unity는 두 제품을 조용히 일몰시켰다. 파트너사 Arkio는 2023년 8월 1일 블로그에서 'Unity가 2023년 8월 AEC 설계검토 플랫폼 Unity Reflect의 일몰을 발표했고, Unity 팀이 기존 고객에게 Arkio를 대안으로 권한다'고 공표했다. VisualLive는 신규 구매가 막힌 뒤 서비스가 완전히 종료됐다(이용자들이 인용한 Unity FAQ 기준: 2023년 6월 30일 판매 종료, 2024년 6월 30일 오프라인). 2026년 9월 현재 unity.com/products/unity-reflect와 unity.com/products/visuallive는 모두 unity.com/industry로 301 리다이렉트되고, unity.com/aec/reflect/faq는 일반 AEC 솔루션 페이지로 넘어간다. VisualLive 앱은 App Store 검색에서 사라졌고 'Unity Reflect Review'만 잔존 등록 상태다. 애플 Vision Pro 발표로 공간컴퓨팅 기대가 정점이던 시기에 벌어진 일이어서 업계는 당황했다.

두 제품 모두 폐기. 고객은 Arkio·BIM Holoview 등 제3자 도구로 이전했다. Unity는 AEC 라인을 접고 Unity Industry로 재편했다.

### Trimble XR10 · Trimble Connect AR/MR · SketchUp Viewer for HoloLens 순차 철수
| 항목 | 내용 |
| --- | --- |
| 주체 | Trimble Inc. 기기 기반은 Microsoft HoloLens. 유통: 니콘·트림블(일본). 2016년 공동 발표 파트너는 AECOM, Gensler. |
| 도시·연도 | 글로벌, 2016 발표 → 2021-08-30(HoloLens 1 앱) → 2024-07-08(SketchUp Viewer) → 2025-12-31 판매 종료 / 2027-09-30 지원 종료 |
| 증거 수준 | 실제 납품 — 유통망(니콘·트림블, 대만 총판)이 판매 종료를 공지한 상용 하드웨어·소프트웨어 |
| AR 여부 | AR 맞음. HoloLens 광학투과 HMD로 BIM 모델을 실제 구조물에 정합했고, XR10은 이를 현장 안전모에 통합한 기기다. SketchUp Viewer PCVR·Quest 부분만 VR이다. |
| 기술 | HoloLens 1/2 광학투과 HMD, 안전모 일체형(XR10, ANSI/CSA 규격 하드햇), Trimble Connect 클라우드 모델 동기화, 현장 정렬은 마커·수동 정합 기반 |
| 출처 | https://www.nikon-trimble.co.jp/TrimbleXR10/ · https://www.zhinc.com.tw/news/AGJMD7W.html · https://help.sketchup.com/en/accounts-and-administration/end-life-sketchup-viewers-hololens-and-virtual-reality · https://forums.sketchup.com/t/heads-up-sketchup-xr-users-pcvr-and-hololens-viewers-are-going-away/283305 · https://aecom.com/press-releases/aecom-trimble-pioneering-use-mixed-reality-technology- |

Trimble은 건설 현장용 AR에 가장 오래 투자한 측량·BIM 벤더다. 2016년 AECOM과 함께 'HoloLens를 엔지니어링·건설에 쓴 세계 최초'라고 발표했고 같은 해 Gensler와도 AR 파트너십을 맺었다. 제품 계보는 HoloLens 1용 Trimble Connect for HoloLens(TCH), HoloLens 2를 안전모에 내장한 XR10, 그리고 SketchUp Viewer for HoloLens였다. 이 계보가 통째로 끊겼다. TCH v2.x는 지원이 종료되고 Microsoft Store에서 철수해 2021년 8월 30일 이후 HoloLens 1에서는 쓸 수 없게 됐다. SketchUp Viewer for HoloLens와 PCVR은 2024년 7월 8일부터 구매·다운로드가 불가해졌고 개발이 중단됐다(Meta Quest용은 2025년 9월 16일 종료). XR10과 Connect MR은 마이크로소프트의 HoloLens 2 판매·지원 종료에 따라 2025년 12월 31일 판매 종료, 2027년 9월 30일 서비스·기술지원 종료가 공지됐다. 니콘·트림블 일본 법인도 XR10 판매 종료를 공지하며 HoloLens 2 부분의 보안·소프트웨어 지원은 마이크로소프트가 2027년 12월 31일까지만 제공한다고 밝혔다. 기존 Connect AR 이용자는 헤드셋이 아닌 스마트폰·태블릿 기반 SiteVision으로 유도됐다. 현재 trimble.com의 XR10 제품 페이지는 'Page Not Found'이고 mixedreality.trimble.com은 일반 페이지로 리다이렉트된다.

머리에 쓰는 AR은 철수. 남은 경로는 Trimble SiteVision(GNSS+스마트폰/태블릿)으로 축소됐다. HMD 종속이 단일 실패점이었다 — 마이크로소프트가 기기를 접자 그 위의 AEC 앱 생태계가 같이 접혔다.

### HoloLens 2 생산 종료 · Magic Leap 1 EOL · Windows Mixed Reality 제거
| 항목 | 내용 |
| --- | --- |
| 주체 | Microsoft, Magic Leap, Google |
| 도시·연도 | 글로벌, 2023-03-15(Glass) / 2024-10-01(HoloLens 2 생산종료) / 2024-12-31(Magic Leap 1) / 2024-10(WMR 제거) |
| 증거 수준 | 실제 납품 — 제조사 공식 EOL 공지 |
| AR 여부 | HoloLens 2·Magic Leap 1·Google Glass는 AR 맞음(광학투과, 실세계 정합). Windows Mixed Reality는 AR 아님 — VR 헤드셋 플랫폼이다. 이름에 'Mixed Reality'가 붙었을 뿐이다. |
| 규모 | HoloLens 2 출고가 3,500달러(기업 구독 월 125달러, 개발자 월 99달러) |
| 기술 | 광학투과 씨스루 디스플레이, 인사이드아웃 SLAM, 손·시선 추적 |
| 출처 | https://en.wikipedia.org/wiki/HoloLens_2 · https://www.magicleap.care/hc/en-us/articles/18878883445645-Magic-Leap-1-End-of-Life · https://en.wikipedia.org/wiki/Google_Glass · https://www.uploadvr.com/windows-11-24h2-kills-windows-mr-support/ |

옥외·현장 AR을 실제로 굴릴 수 있는 광학투과 HMD는 사실상 세 종류였고 2023~2024년에 셋 다 정리됐다. Google Glass Enterprise Edition은 2023년 3월 15일 생산·판매가 중단되고 2023년 9월 15일로 지원이 끝났다. HoloLens 2는 2019년 2월 기업용으로 공개되고 같은 해 11월 7일 일반 출시된 3,500달러 기기인데, 2024년 10월 1일 생산이 종료됐고 소프트웨어 업데이트만 2027년 12월 31일까지 제공된다. Magic Leap 1은 2024년 12월 31일부로 지원이 끝났다 — OS 업데이트도, Care 지원도, 클라우드 서비스도 없어졌고 매직리프 공식 사이트의 제품 페이지는 'Magic Leap 1 End of Life' 문서로 리다이렉트된다. 데스크톱 쪽에서는 마이크로소프트가 2023년 12월 Windows Mixed Reality를 폐지 예고하고 2024년 10월 Windows 11 24H2에서 제거했다(소비자 지원 2026년 11월 1일, 상용 2027년 11월 1일 종료). 기기를 산 발주처와 설계사는 감가상각이 끝나기도 전에 플랫폼을 잃었다.

전량 단종. 현장 AR 업무는 스마트폰·태블릿으로 후퇴했다. HMD를 전제로 설계된 워크플로(양손 자유, 시선 정합)는 대체되지 못했다.

### Google Tango 종료, 그리고 Google Measure의 조용한 삭제
| 항목 | 내용 |
| --- | --- |
| 주체 | Google(현 Alphabet), 하드웨어 파트너 Lenovo·ASUS·Intel RealSense |
| 도시·연도 | 글로벌, 2014 공개 → 2018-03-01 종료 / Measure 2021-06 삭제 |
| 증거 수준 | 실제 납품 — 양산 스마트폰 2기종과 스토어 배포 앱 |
| AR 여부 | AR 맞음. Tango는 depth·모션 트래킹으로 실공간에 정합했고 Measure는 그 위에서 실측치를 겹쳐 표시했다. |
| 기술 | 적외선 심도센서 + 모션트래킹 + 영역학습(area learning). 후속 ARCore는 전용 센서 없이 단안 카메라+IMU로 전환 |
| 출처 | https://en.wikipedia.org/wiki/Tango_(platform) · https://arstechnica.com/gadgets/2021/06/google-kills-its-augmented-reality-measure-app/ · https://9to5google.com/2021/06/08/google-measure-ar-app-sunset/ · https://9to5google.com/2026/09/07/samsung-is-shutting-down-quick-measure-and-ar-doodle-apps-for-galaxy-phones/ |

Tango는 구글이 2014년 6월 5일 공개한 심도센서 기반 모바일 AR 플랫폼이다. 전용 하드웨어를 요구했고, Peanut 폰과 Yellowstone 태블릿을 거쳐 레노보 Phab 2 Pro(2016년 8월 발표, 11월 미국 출시)와 에이수스 ZenFone AR(2017년 CES)로 상용화됐다. 실내외 공간을 3D로 스캔해 실물 크기로 겹치는 일이 처음 대중 기기에서 가능해졌고, 측량·조경 스케일 확인용 앱들이 여기에 붙었다. 구글은 2017년 12월 15일 ARCore를 택하면서 2018년 3월 1일부로 Tango 지원 종료를 발표했다. 전용 센서를 단 두 기종은 그날로 플랫폼을 잃었다. Tango에서 태어난 'Measure' 앱은 2018년 ARCore용 단독 앱으로 이식돼 수백만 대의 안드로이드로 퍼졌지만, 2021년 6월 구글이 아무 공지 없이 Play 스토어에서 내렸다. 삼성도 2026년 9월 Quick Measure와 AR Doodle 종료를 알렸다. 현장에서 '치수를 대충 재는' AR — 조경 실무자가 가장 먼저 손대던 기능 — 이 플랫폼 사업자들 손에서 두 번 죽었다.

Tango 폐기, ARCore로 노선 변경. Measure 앱은 삭제. 전용 센서를 산 이용자와 그 위에 앱을 올린 개발자는 보상 없이 정리됐다.

### Metaio · Junaio 종료 — 1세대 AR 브라우저의 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | Metaio GmbH(뮌헨, 2003~2015). 인수자 Apple Inc. |
| 도시·연도 | 독일 뮌헨, 2003 창업 → 2015년 5월 판매 중단·애플 인수 → 2015년 12월 서비스 종료 |
| 증거 수준 | 실제 납품 — 상용 SDK와 iOS·안드로이드 배포 앱, 다수의 3자 채널 운영 |
| AR 여부 | AR 맞음. 카메라 영상에 지리좌표로 등록된 3D·2D 콘텐츠를 겹치는 옥외 AR 브라우저였다. |
| 기술 | LLA 마커(위·경도·고도 마커), 영상 기반 트래킹, 채널형 콘텐츠 배포 API, Creator 저작도구 |
| 출처 | https://en.wikipedia.org/wiki/Metaio · https://en.wikipedia.org/wiki/Junaio · https://rip.so/metaio.html · (DNS 무응답 확인) https://www.junaio.com/ , https://www.metaio.com/ |

Metaio는 2003년 뮌헨공대에서 분사한 독일 AR 회사다(창업자 Günter Greiner, Peter Meier, Thomas Alt). 브랜드·박물관·도시 콘텐츠에 AR SDK를 라이선스했고, 소비자용 AR 브라우저 Junaio를 운영했다. Junaio의 핵심은 LLA 마커(위도·경도·고도 마커)로 GPS의 정확도 한계를 보정한다는 것이었다 — 옥외 지리정합 AR이 처음으로 실용 수준에 근접한 시도였다. 콘텐츠 제공자는 '채널'을 만들어 올렸고, 지자체·대학·문화기관이 여기에 붙었다. 2015년 5월 Metaio는 예정된 컨퍼런스를 취소하고 전 제품 판매를 중단했다. 곧 애플이 인수를 마무리했다. SDK와 Junaio 채널은 같은 해 12월 오프라인 처리됐다. 지금 junaio.com과 metaio.com은 DNS가 응답하지 않는다. 남의 서버에 콘텐츠를 얹은 모든 프로젝트가 자기 잘못 없이 함께 죽었다 — 뉴질랜드 CityViewAR의 Junaio 채널도 그중 하나다. 2년 뒤 애플은 ARKit을 발표했다.

회사·SDK·브라우저 전부 소멸. 애플은 인수 기술을 사내화하고 외부 개발자 지원을 승계하지 않았다. 지리기반 AR 콘텐츠 계보가 여기서 한 번 끊겼다.

### Layar → Blippar, 그리고 'AR City' 도시 내비게이션의 붕괴
| 항목 | 내용 |
| --- | --- |
| 주체 | Layar B.V.(암스테르담) → Blippar Ltd.(런던). 투자자에 Qualcomm Ventures 등. 2019년 IP 인수자는 Nick Candy가 이끄는 투자사. |
| 도시·연도 | 암스테르담·런던, 2009 → 2014 인수 → 2017-11 AR City → 2018-12-18 관리절차 |
| 증거 수준 | 실제 납품 — App Store 배포 앱과 상용 AR 플랫폼. 다만 AR City는 스스로 '베타'로 표기했다. |
| AR 여부 | AR 맞음. 옥외에서 카메라 영상에 지리등록 콘텐츠를 겹쳤고, UVP는 실제 건물 외관을 이용한 시각 측위였다. |
| 규모 | Blippar 시리즈 D 5,400만 달러(2016년 초). AR City는 300개 이상 도시, iOS 전용 |
| 기술 | GPS·나침반·가속도계 기반 지리정합 + urban visual positioning(건물 외관 컴퓨터비전 측위). 위치·방향 수동 보정 UI 포함 |
| 출처 | https://www.blippar.com/welcome-ar-city-future-maps-and-navigation/ · https://en.wikipedia.org/wiki/Layar · https://www.cnbc.com/2018/12/18/uk-ar-startup-blippar-collapses-into-administration-lays-off-staff.html · https://www.telecomtv.com/content/ai-ml/where-are-they-now-blippar-bites-the-dust-33640/ · https://docs.blippar.com/blippbuilder-documentation/faqs/blippbuilder-faqs |

Layar는 2009년 6월 암스테르담에서 창업한(Raimo van der Klein, Claire Boonstra, Maarten Lens-FitzGerald) 지리기반 AR 브라우저다. 가속도계·GPS·나침반·카메라를 묶어 시야에 POI를 겹쳤고, 도시 정보 AR의 원형으로 불렸다. 2014년 6월 영국 Blippar가 Layar를 인수했다. Blippar는 2016년 초 5,400만 달러 시리즈 D를 받고 2017년 11월 'AR City' 베타를 내놨다 — iOS 전용, 전 세계 300개 이상 도시에서 AR 길찾기를 제공하고, 일부 지역에서는 GPS보다 정확하다는 자체 기술 'urban visual positioning(UVP)'로 컴퓨터비전 측위를 붙였다. 그런데 Blippar 자신의 출시 공지가 '이번 버전에서는 이용자가 위치와 방향을 수동으로 조정해 AR 경험을 개선하게 했다'고 적었다. 도시 규모 정합이 자동으로는 안 됐다는 뜻이다. Layar 암스테르담 사무소는 2016년에 닫혔고 Reality Browser 앱은 2018년경 단종됐다. Blippar는 2018년 12월 18일 자금 조달 실패로 관리절차(administration)에 들어갔고, 2019년 초 IP가 Nick Candy 측 투자사에 팔렸다. 지금 layar.com은 blippar.com으로 리다이렉트되고, AR City는 App Store에서 찾을 수 없다. Blippar 문서는 '앱 기반 AR 프로젝트는 이미 중단됐다'며 WebAR 전환을 안내한다.

Layar 브랜드 소멸, AR City 소멸, 모회사 관리절차. 도시 규모 AR 길찾기라는 아이디어는 이후 구글 Live View가 이어받았지만 Blippar 계보는 끊겼다. 창업자들은 2017년 이미 경영진의 전략 부재를 공개 비판했다.

### Wikitude 서비스 전면 종료 (2024-09-21)
| 항목 | 내용 |
| --- | --- |
| 주체 | Wikitude GmbH(오스트리아). 종료 공지가 안내하는 후속 플랫폼은 퀄컴 Snapdragon Spaces. |
| 도시·연도 | 오스트리아, 2008 창업 → 2024-09-21 전면 종료 |
| 증거 수준 | 실제 납품 — 상용 SDK·클라우드 서비스의 공식 종료 공지 |
| AR 여부 | AR 맞음. 지리좌표 기반 옥외 AR과 이미지·객체 인식 AR을 모두 제공한 SDK였다. |
| 기술 | Geo-AR(위·경도 기반 POI 정합), 이미지·객체 인식, 인스턴트 트래킹, Wikitude Studio/Cloud 클라우드 저작·타깃 관리 |
| 출처 | https://www.wikitude.com/ |

Wikitude는 오스트리아 잘츠부르크에서 출발한 AR SDK로, 지리좌표 기반 옥외 AR을 가장 오래 상용 지원한 도구였다. 도시·조경·문화유산 분야의 학술 프로토타입과 지자체 앱이 이 SDK로 만들어졌다 — 자체 앱을 개발할 여력이 없는 발주처가 선택하던 경로였다. 회사 홈페이지는 2024년 9월 '이제 작별할 때가 왔다'고 공지하고, 2024년 9월 21일 모든 Wikitude 서비스를 종료하고 저장된 데이터는 접근 불가가 된다고 밝혔다. Wikitude Studio, Cloud, Studio API가 모두 비활성화되고 관련 데이터는 삭제됐다. 남은 SDK 라이선스 키는 iOS·안드로이드·윈도우가 호환성을 깨는 변경을 하기 전까지만 작동하며, 지원과 업데이트는 없다. 공지는 이용자를 퀄컴의 Snapdragon Spaces XR 개발자 플랫폼으로 안내한다 — 즉 스마트폰 지리기반 AR에서 헤드셋 AR로의 노선 전환이다. 클라우드에 타깃·콘텐츠를 올려 쓰던 방식이었으므로, 종료와 함께 배포된 앱들이 기능을 잃었다.

서비스 전면 종료, 데이터 삭제. 클라우드 의존 앱은 작동 불가. 옥외 지리기반 AR을 상용 지원하는 독립 SDK 축이 사실상 사라졌고, 남은 선택지는 플랫폼 사업자(애플 ARKit·구글 ARCore) 직접 개발뿐이다.

### Adobe Aero 종료 · Torch AR 종료 — 디자이너용 무코드 AR 저작도구의 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | Adobe Inc.(Aero), Torch 3D Inc.(미국 오리건주 포틀랜드, 2017 창업) |
| 도시·연도 | 글로벌, Torch AR 2020-07-01 종료 / Adobe Aero 2019 출시 → 2025-11-06 단종, 2025-12-03 데이터 종료 |
| 증거 수준 | 실제 납품 — Creative Cloud에 포함돼 배포된 상용 앱의 공식 단종 |
| AR 여부 | AR 맞음. ARKit/ARCore 기반으로 3D 자산을 실공간 평면에 정합해 배치·게시하는 저작도구였다. |
| 기술 | ARKit/ARCore, Adobe Substance·Illustrator·Photoshop 자산 연동, 웹·앱 게시, 노코드 인터랙션 편집 |
| 출처 | https://helpx.adobe.com/aero/aero-end-of-support-faq.html · https://en.wikipedia.org/wiki/Adobe_Aero · https://thomasdeneuville.com/building-ar-experience/ · https://www.reddit.com/r/augmentedreality/comments/hkeyjf/torch_ar_closes_its_doors_what_happens_straight/ |

설계자가 코드 없이 AR을 만들 수 있게 해준 도구가 두 번 죽었다. Torch 3D(2017년 미국 포틀랜드 창업)의 Torch AR은 Unity 같은 게임엔진의 복잡성을 걷어내고 모바일에서 AR을 설계·배포하게 한 노코드 앱이었다. Sketch·Adobe 파일을 들여오고 Sketchfab·Poly 3D 라이브러리에 붙는 식으로 디자이너 워크플로에 맞췄다. 2020년 7월 1일 서비스 중단을 발표했다. 그 자리를 Adobe Aero가 이어받았다. Aero는 2019년 Adobe MAX에서 발표된 Creative Cloud의 유일한 AR 저작·게시 플랫폼으로, Photoshop·Illustrator 자산을 그대로 실공간에 배치할 수 있어 조경·전시 분야에서 진입 경로가 됐다. 어도비는 2025년 11월 6일부로 iOS·안드로이드·Creative Cloud 데스크톱에서 Aero를 단종하고, 기존 이용자는 2025년 12월 3일까지만 앱 접근과 콘텐츠 다운로드가 가능하다고 공지했다. 그 이후 사용자 프로젝트는 삭제됐다. 현재 App Store에서 Adobe Aero는 검색되지 않는다. 대안으로 Hoverlay·Zapworks 같은 소규모 업체가 이전 경로를 안내하고 있다.

둘 다 폐기. 코드를 모르는 설계자가 AR을 직접 만들 경로가 다시 닫혔다. 어도비 커뮤니티에는 '차라리 기술을 다른 회사에 팔아라'는 항의가 남았다.

### Esri ArcGIS AR 툴킷 deprecate — GIS 벤더의 월드스케일 AR 철수
| 항목 | 내용 |
| --- | --- |
| 주체 | Esri |
| 도시·연도 | 글로벌, .NET 200.0(2022~) / Qt 200.8 deprecate |
| 증거 수준 | 실제 납품 — 상용 SDK 문서의 deprecation 고지 및 공개 이슈 트래커 |
| AR 여부 | AR 맞음. world-scale 패턴은 GIS 장면을 실제 좌표에 정합해 현장에서 실물 크기로 겹치는 것이고, ARCore/ARKit 세션을 SceneView에 직접 결합했다. |
| 기술 | ARSceneView가 ARCore/ARKit 세션을 시작·관리하고 ArcGIS SceneView와 동기화. tabletop / flyover / world-scale 3패턴 |
| 출처 | https://developers.arcgis.com/qt/v200/toolkit/ · https://developers.arcgis.com/qt/v200/scenes-3d/display-scenes-in-augmented-reality/ · https://community.esri.com/t5/qt-maps-sdk-questions/augmented-reality-deprecated-what-to-use-instead/td-p/1647323 · https://github.com/Esri/arcgis-maps-sdk-dotnet-toolkit/issues/467 |

조경·도시 분야의 AR은 결국 GIS 데이터를 현장에 겹치는 일이다. 그 경로를 공식 지원한 곳이 Esri였다. ArcGIS Maps SDK 계열은 tabletop(탁상 축소 모형), flyover(창처럼 들여다보기), world-scale(실물 크기 현장 정합) 세 가지 AR 패턴을 툴킷으로 제공했다. 이 지원이 조용히 후퇴했다. .NET용 툴킷에서는 200.0 초기 릴리스에 AR Toolkit이 포함되지 않았는데, 공개된 이유가 '.NET의 ARCore 기반 지원 문제'였다 — 즉 안드로이드 AR 런타임을 붙일 수 없었다. Qt용 SDK에서는 AR 툴킷 구성요소가 deprecate 처리돼 '향후 릴리스에서 제거된다'고 API 참조와 툴킷 문서에 명시됐다(Esri 커뮤니티 문의에 따르면 Qt SDK 200.8). 문의한 개발자가 대안을 물었을 때 제시된 것은 QtQuick 3D XR이며, ArcGIS 기능을 어떻게 붙일지는 미해결이었다. 지도·지형·3D 도시모델을 현장에 실물 크기로 겹치는 표준 경로가 벤더 지원 밖으로 밀려난 것이다. 앞의 취리히 ETH 연구가 바로 이 스택(ArcGIS 런타임 + Survey123) 위에서 만들어졌다.

Qt용 AR 툴킷 deprecate(제거 예정), .NET용은 200.0에서 제외. GIS 기반 옥외 AR을 벤더 지원으로 만들 길이 좁아졌다. 원인은 시장 축소보다 하위 AR 런타임 대응 부담으로 보인다.

### CityViewAR — 크라이스트처치 지진 도시의 실물 크기 AR, 그리고 그것이 사라진 방식
| 항목 | 내용 |
| --- | --- |
| 주체 | HIT Lab NZ, University of Canterbury(개발팀: Mark Billinghurst, Raphael Grasset, Gun Lee, Leigh Beattie, Tim Hobbs, Seungwon Kim, Alaeddin Nassani, Rohit Sharma, Sophia Grey, Kamaran Noori, Rozhen Mohammad-Amin, Rob de Voer). 3D 모델 제공 ZNO 건축가 Jason Mill. 데이터 제공 Christchurch City Council, Historic Places Trust. 부분 후원 Vodafone New Zealand Ltd. |
| 도시·연도 | 뉴질랜드 크라이스트처치, 2011 출시 → 안드로이드판 소멸 / iOS 재출시 2021-02-25 |
| 증거 수준 | 실제 납품 — 공공기관(시의회·문화유산청)이 데이터를 제공하고 일반 스토어에 배포된 앱 |
| AR 여부 | 원본은 AR 맞음 — GPS·나침반 정합으로 실물 크기 3D 건물을 현장에 겹쳤다. 현행 iOS판은 AR 아님 — 파노라마 사진 뷰어다. |
| 규모 | 도심 전역, 핵심 건물 '수백 개'의 3D 모델. 예산 비공개 |
| 기술 | HIT Lab NZ Android AR 플랫폼(GPS + 나침반 센서 정합), 병행 Junaio 채널(LLA 마커), 현지에 없는 이용자를 위한 가짜 GPS 주입 모드 |
| 출처 | http://web.archive.org/web/20120108004757/http://www.hitlabnz.org/index.php/products/cityviewar · (404 확인) https://play.google.com/store/apps/details?id=com.hitlabnz.equar · https://apps.apple.com/us/app/cityviewar/id1554970855 |

2010년 9월부터 크라이스트처치는 연속 지진으로 도심 상당 부분이 철거됐다. 평생 그 도시에 산 사람도 어느 자리에 무슨 건물이 있었는지 떠올리지 못하게 됐다. 캔터베리대학교 HIT Lab NZ는 2011년 CityViewAR을 내놨다. 안드로이드폰을 들고 도심을 걸으면 철거된 건물들이 실물 크기 3D 모델로 그 자리에 나타나고 사진과 건물 이력이 붙었다. 핵심 건물 수백 개의 3D 모델은 ZNO의 건축가 Jason Mill이 제공했고, 사진과 건물사는 크라이스트처치 시의회와 Historic Places Trust가 댔다. HIT Lab NZ의 Android AR 플랫폼이 GPS와 나침반으로 정합했다 — 모바일 AR로 수십 채를 한꺼번에 보여준 것도, 지진 복구에 모바일 AR을 쓴 것도 세계 최초라고 스스로 기록했다. 프로젝트 문서는 후속 계획을 이렇게 적었다. 이용자가 건물에 의견을 달게 해서 '건축가와 도시계획가가 제안한 설계에 대한 사람들의 의견을 받는 도구'로 쓰고, GIS와 연결해 지하시설물 같은 다른 데이터도 올리고, 재난 직후 신속 배치가 가능한 모바일 AR 플랫폼으로 키우겠다는 것이었다. 그 후속은 오지 않았다. 안드로이드 앱(com.hitlabnz.equar)은 Play 스토어에서 404다. 병행 운영한 Junaio 채널은 2015년 Junaio가 죽을 때 함께 끊겼다. 2021년 2월 캔터베리대 이름으로 같은 제목의 iOS 앱이 다시 올라왔지만(v2.02, 2026년 2월 갱신), 이것은 지진 직후 파노라마 사진을 GPS 지도와 자이로 회전으로 보여주는 'Education' 카테고리 앱이다. 실물 크기 건물 정합은 없다. 되살아난 것은 이름이고, 사라진 것은 AR이다.

안드로이드 앱 삭제(Play 404), Junaio 채널은 2015년 플랫폼 종료와 함께 소멸. 문서에 적힌 '설계안 의견수렴 도구' 후속은 실행되지 않았다. 2021년 iOS 재출시판은 AR 기능을 버리고 파노라마 뷰어가 됐다.

### ARCHEOGUIDE — EU 옥외 AR 프로젝트(고대 올림피아), 34개월로 종료
| 항목 | 내용 |
| --- | --- |
| 주체 | 총괄 INTRACOM S.A.(그리스). 참여: A&C 2000 S.R.L.(이탈리아), CCG/ZGDV(포르투갈), Fraunhofer-Gesellschaft(독일), ZGDV e.V.(독일), 그리스 문화부, Post Reality S.A.(그리스) |
| 도시·연도 | 그리스 고대 올림피아, 1999 착수 → 2002년 10월 종료 |
| 증거 수준 | 연구 프로토타입 (공공 연구비 기반, 현장 이용자 평가까지 수행). 상용 서비스로 전환되지 않았다. |
| AR 여부 | AR 맞음. 씨스루 HMD로 실제 폐허 위에 복원 형상을 정합해 겹쳤다. |
| 규모 | 34개월, 7개 기관 4개국. 대상지 고대 올림피아. 사업비는 CORDIS에 미공개 |
| 기술 | 씨스루 HMD + 차분 GPS + 영상 기반 트래킹, 배낭형 모바일 유닛, 3D 복원 모델 실시간 렌더링 |
| 출처 | https://cordis.europa.eu/project/id/IST-1999-11306/results · https://cordis.europa.eu/project/id/IST-1999-11306 · https://dl.acm.org/doi/10.1145/584993.585015 · https://dl.acm.org/doi/epdf/10.1145/584993.585018 |

옥외 AR을 실제 유적에 적용한 최초의 대형 공공 연구사업이다. EU 제5차 프레임워크 IST 프로그램 과제(IST-1999-11306)로, 그리스 INTRACOM S.A.가 총괄하고 이탈리아 A&C 2000, 포르투갈 CCG/ZGDV, 독일 Fraunhofer-Gesellschaft와 ZGDV, 그리스 문화부, 그리스 Post Reality S.A. 등 7개 기관이 참여했다. 대상지는 고대 올림피아 유적. 씨스루 HMD와 차분 GPS, 영상 기반 트래킹을 결합해 폐허 위에 복원 건물을 겹치고 위치·방향에 따라 안내를 제공하는 배낭형 장비를 만들었다. 프로토타입은 올림피아 현장에서 대표 이용자군을 대상으로 평가됐고, 논문에는 HMD와 카메라 시스템 실험, 연산 성능 최적화, 입력장치 개선 필요 같은 기술 과제가 남았다. 프로젝트는 2002년 10월 34개월로 종료됐다. 2004 아테네 올림픽을 겨냥한 타이밍이었는데 운영 서비스로 넘어가지 않았다. CORDIS의 총사업비·EU 분담금은 '데이터 없음'으로 비어 있다. 프로젝트 도메인 archeoguide.com은 현재 무관한 이탈리아 도메인으로 넘어가며 503을 반환한다. 옥외 AR의 정합·무게·전원 문제를 처음 정면으로 만난 사업이고, 그 문제들은 20년 뒤에도 같은 형태로 남았다.

2002년 10월 종료 후 후속 없음. 프로젝트 도메인은 제3자에게 넘어갔다. 기술적으로는 장비 무게·연산 성능·입력장치가, 제도적으로는 유적 운영기관의 상시 운용 역량이 벽이었다.

### VIDENTE / SMART VIDENTE — 지하시설물 AR, 논문으로 남고 제품으로 남지 않음
| 항목 | 내용 |
| --- | --- |
| 주체 | Graz University of Technology, Institute of Computer Graphics and Vision + GRINTEC GmbH(그라츠). 연관 과제 POMAR 3D는 OHB Austria, 오스트리아 우주프로그램 지원. |
| 도시·연도 | 오스트리아 그라츠, 2007~2012(VIDENTE·SMART VIDENTE) |
| 증거 수준 | 연구 프로토타입 (공공 연구비 + 산업 파트너). 상용 제품화는 확인되지 않음. |
| AR 여부 | AR 맞음. GIS의 지하 관로를 실제 도로면에 정합해 핸드헬드 화면에 겹쳤다. |
| 기술 | Ultra-Mobile PC → 전용 핸드헬드, RTK급 GNSS + 방위 센서 융합, GIS(지하 관로 3D) 직접 연동, AR 레드라이닝·준공측량, 굴착부 가시화 |
| 출처 | https://tugraz.elsevierpure.com/en/projects/vidente-augmented-reality-system-for-visualisation-of-subsurface-/ · https://tugraz.elsevierpure.com/en/projects/smart-vidente-subsurface-mobile-augmented-reality-technology-for-/ · https://schmalstieg.github.io/pdf/Schmalstieg_138.pdf · https://schmalstieg.github.io/pdf/Schmalstieg_401.pdf · https://austria-in-space.at/en/projects/2008/positioning-and-o |

오스트리아 그라츠공대 컴퓨터그래픽·비전연구소(Gerhard Schall, Dieter Schmalstieg, Erick Mendez, Ernst Kruijff, Eduardo Veas)와 그라츠의 GIS 회사 GRINTEC GmbH가 2007년부터 수행한 옥외 핸드헬드 AR 사업이다. 목표는 명확했다. 상하수·전력·통신 관로를 GIS에서 불러와 도로 위에 실물 크기로 정합해 보여주고, 현장에서 3D 모델의 기하·속성을 수정하고 준공측량까지 하게 하는 '차세대 현장정보 시스템'. Ultra-Mobile PC에 다중 센서를 붙인 초기 장비에서 전용 핸드헬드 설계로 넘어갔고, AR 방식의 레드라이닝(현장 주석) 도구도 만들었다. 측위 정확도 문제는 별도 과제로 떼어내 오스트리아 우주프로그램 지원의 POMAR 3D(OHB Austria)에서 고정밀 위치·방위 모듈을 개발했다 — 옥외 AR의 병목이 어디였는지를 그 자체로 말해주는 구성이다. 성과는 Personal and Ubiquitous Computing 등에 논문으로 남았고 후속 SMART VIDENTE까지 이어졌다. 그러나 'Vidente'라는 이름의 상용 제품은 확인되지 않는다. 같은 연구그룹이 10년 뒤 'Augmented Reality for Subsurface Utility Engineering, Revisited'를 내며 옥외 측위, 물리 스프레이 마킹 대체, 굴착부 3D 재구성을 다시 다룬다 — 덴마크 올보르 현장 실험까지 포함해서. 문제가 풀려서 끝난 게 아니라, 연구가 한 바퀴 더 돌았다는 뜻이다.

논문과 시제품으로 종료. 상용 브랜드로 남지 않았다. 동일 과제가 2020년대에 재시도됐다는 사실이 그 자체로 결론이다 — 옥외 정합 정확도와 지하 데이터 품질 두 축이 모두 해결되지 않았다.

### 취리히 현장실험 — AR이 Baugespann을 대체하지 못했다 (높이 31% 과대추정)
| 항목 | 내용 |
| --- | --- |
| 주체 | University of Zurich 지리학과 + ETH Zurich 지도학·지리정보연구소. 데이터 제공: 취리히시 건축국(Amt für Hochbauten, 담당 Christian Hürzeler), 설계 Studio Burkhardt(학교), hls Architekten(주거). |
| 도시·연도 | 스위스 취리히, 2022 수행 → Journal of Location Based Services 17(1) 48-77, 2023 |
| 증거 수준 | 연구 프로토타입 — 다만 실제 허가 대상지, 실제 설계 데이터, 시 당국 협조로 수행된 현장 실험 |
| AR 여부 | AR 맞음. ARKit 3으로 실제 건설부지에 계획 건물을 실물 크기로 정합했다. |
| 규모 | 참가자 30명, 대상지 2곳(취리히 남부 개발구역), 과제 8개(Baugespann 2 + AR 6). 예산 비공개 |
| 기술 | iOS 11+ 네이티브, Swift + ARKit 3, ArcGIS 런타임 기반 모바일 씬 패키지(오프라인), 수동 높이 보정 슬라이더, 스마트폰 화면 + iPad(6세대) 설문 |
| 출처 | https://doi.org/10.1080/17489725.2022.2086309 · https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/542298/Anaugmentedrealitystudyforpublicparticipationinurbanplanning.pdf?sequence=2 |

스위스는 건축허가 절차에서 실물 골조 표시(Baugespann)로 계획 건물의 규모를 현장에 1:1로 공표한다. 조경·도시 분야가 AR에 기대한 바로 그 일을 제도가 이미 하고 있다는 뜻이다. 취리히대 지리학과와 ETH 지도학·지리정보연구소(Ursina C. Boos, Tumasch Reichenbacher, Peter Kiefer, Christian Sailer)는 둘을 정면으로 맞붙였다. 취리히 남부 개발구역의 두 실제 프로젝트를 썼다 — 하나(P1)는 Baugespann이 세워진 주거단지, 하나(P2)는 계획이 상당히 진행된 학교 신축. 취리히시 건축국이 설계사 Studio Burkhardt의 계획 모델을 FBX로 제공했고, 주변 건물은 취리히 3D 도시모델, 배경은 Esri World Imagery를 썼다. iOS·Swift·ARKit 3으로 프로토타입을 만들고 LOD 1/2/3 세 단계를 피험자간 설계로 비교했다. 참가자 30명(여 18·남 12, 21~58세, ArcGIS Survey123로 설문). 결과가 냉정했다. Baugespann에서는 한 명을 빼고 모두 높이를 과소추정했고 평균 약 34%였다. 그런데 AR에서는 높이를 평균 약 31% 과대추정하고 길이는 과소추정했다 — 오차의 방향이 바뀌었을 뿐 크기 판단은 여전히 틀렸다. 가려지는 건물 5채를 고르는 과제에서 평균 3채를 맞혔다. LOD 세 조건 간 주관 평가에 유의한 차이가 없었고, 가장 상세한 LOD 3에서는 모델이 간헐적으로 모션 랙을 보여 오히려 '부정확하다'고 읽혔다. 논문은 드리프트 효과가 건물 크기 오해로 이어질 수 있고, 캘리브레이션의 작은 오차가 정합 어긋남을 만들어 결과에 영향을 줬을 수 있다고 적었다. GIS 사전지식이 있는 참가자가 더 잘 추정했다는 결과도 나왔다 — 일반 시민을 위한 도구라는 전제와 어긋난다.

AR이 Baugespann을 대체할 만큼 크기 인지를 개선하지 못했다. 참가자들은 AR의 잠재력을 긍정 평가했지만 수행 성적은 따라오지 않았다. 후속 실무 도입 사례는 확인되지 않는다. 논문 스스로 장기적 참여 효과는 미검증이라고 적었다.

### 덴마크 굴착손상 방지 AR — 기술이 아니라 데이터가 없어서 막혔다
| 항목 | 내용 |
| --- | --- |
| 주체 | Aalborg University — Department of Sustainability and Planning / Danish Centre for Spatial Planning. 저자 Hansen, Wyke, Bodum. |
| 도시·연도 | 덴마크(올보르 등), 2025 |
| 증거 수준 | 연구 프로토타입 + 업계 질적 평가 (인터뷰 17명). 상용 도입 여부는 이 논문의 범위 밖. |
| AR 여부 | AR 맞음. 지하 관로와 굴착부 3D 재구성을 실제 노면에 정합해 겹치는 것을 대상으로 한 연구다. |
| 규모 | 반구조화 인터뷰 응답자 17명. 논문 15쪽, Innovative Infrastructure Solutions 10(12), article 575, 2025 |
| 기술 | 리얼리티 캡처(포인트클라우드·사진측량)로 굴착부 3D 재구성 + 옥외 AR 정합. 덴마크 지하시설물 등록제도 LER 2.0 맥락 |
| 출처 | https://doi.org/10.1007/s41062-025-02372-5 · https://vbn.aau.dk/en/publications/using-augmented-reality-to-avoid-excavation-damage-in-denmark-a-q/ · https://schmalstieg.github.io/pdf/Schmalstieg_401.pdf |

올보르대학교(Lasse Hedegaard Hansen, Simon Wyke, Lars Bodum)가 2025년 Innovative Infrastructure Solutions에 발표한 질적 평가 연구다. 굴착 중 지하 관로를 치는 사고는 직접비(관로 수리·구조물 복구)만이 아니라 간접비가 훨씬 크고, 초록은 간접비가 직접비의 최대 29배로 보고된다고 적었다. 그래서 덴마크는 지하시설물 문서화 정확도에 집중해왔다. 연구는 리얼리티 캡처와 증강현실이 굴착 계획, 지하 관로 유지관리, 신설 공사의 의사소통과 의사결정에 실제로 쓸 수 있는 도구인지를 물었다. 방법은 업계 관계자 17명 반구조화 인터뷰와 관련 문헌 대조. 결론은 두 겹이다. AR과 리얼리티 캡처는 지하를 보여주고 소통하는 데 유익하다. 그러나 '덴마크에 기존 지하시설물의 리얼리티 캡처 문서와 데이터 교환 체계가 없다는 점이 그 잠재적 효용을 실현하는 데 한계로 확인됐다.' 도구는 준비됐는데 겹쳐 보여줄 정확한 원본이 없다는 것이다. 같은 팀과 그라츠 연구그룹은 올보르 현장에서 가상 관로 마킹과 굴착부 3D 재구성을 AR로 실험한 바 있는데, 물리적 스프레이 마킹을 대체하려면 결국 그 마킹의 근거가 되는 데이터가 정확해야 한다. 조경·도시 AR이 자주 빠지는 함정이 여기에 정확히 드러난다 — 실패 원인이 정합 기술이 아니라 데이터 부재인 경우.

'유익하지만 실현 불가'로 정리됐다. 병목은 AR 기술이 아니라 기존 지하시설물의 실측 기록 부재와 데이터 교환 체계 부재. 도입 결정은 도구 구매가 아니라 데이터 정비 투자의 문제로 옮겨갔다.

### 2019년 'AR 겨울' — Daqri·Meta·ODG 동시 붕괴, 건설용 스마트헬멧의 종말
| 항목 | 내용 |
| --- | --- |
| 주체 | Daqri(로스앤젤레스, 2010~2019, 투자 주도 Tarsadia Investments). Meta Company(캘리포니아, 창업자 Meron Gribetz) → Meta View. Osterhout Design Group(샌프란시스코, 창업자 Ralph Osterhout). |
| 도시·연도 | 미국, 2019년 1월(Meta·ODG) · 9월(Daqri) |
| 증거 수준 | 실제 납품 — 상용 출하된 기기(Smart Helmet, Meta 2, ODG R-7)의 회사 청산 |
| AR 여부 | AR 맞음. 세 회사 모두 광학투과 씨스루 HMD로 실세계에 정합해 겹치는 기기를 만들었다. |
| 규모 | Daqri 조달 2억 7,500만 달러, Smart Helmet 1만 5천 달러 / Smart Glasses 약 5천 달러. ODG 조달 5,800만 달러. |
| 기술 | 광학투과 씨스루 HMD, 안전모 일체형(Daqri), 광시야각 디스플레이(Meta 2), 안드로이드 기반 독립형 스마트글래스(ODG R-9) |
| 출처 | https://techcrunch.com/2019/09/12/another-high-flying-heavily-funded-ar-headset-startup-is-shutting-down/ · https://en.wikipedia.org/wiki/Daqri · https://techcrunch.com/2019/01/10/an-ar-glasses-pioneer-collapses/ · https://www.theverge.com/2019/1/18/18187315/meta-vision-ar-headset-company-asset-sale-unknown-buyer-insolvent · https://www.digitalbodies.net/that-was-fast-three-ar-companies-fail-in-a- |

현장 AR 하드웨어 시장이 한 해에 무너졌다. Daqri는 2010년 로스앤젤레스에서 창업해 2016년 DAQRI Smart Helmet을 1만 5천 달러에 공개했다 — 건설·제조·석유가스·중공업 현장을 겨냥한, 헤드업 디스플레이와 다중 카메라·센서를 박은 안전모였다. 이후 약 5천 달러의 Smart Glasses로 내려왔다. Tarsadia Investments가 주도한 두 차례 사모 라운드로 총 2억 7,500만 달러를 모았지만, 2019년 9월 본사를 닫고 대부분을 해고하고 자산을 매각하며 사업을 종료했다. 같은 해 1월에는 Meta(Meta Company, Meta 2 헤드셋)가 특허 소송과 자금난 속에 자산을 매각하고 문을 닫았다(5월에 Meta View가 IP를 인수, CEO는 퀄컴 Vuforia 출신 Jay Wright). 같은 1월 ODG(Osterhout Design Group, 1999년 창업)도 붕괴했다 — 5,800만 달러를 조달하고 2017년 CES에서 R-8·R-9를 화려하게 발표했지만 둘 다 출하하지 못했고 R-7 주문도 다 채우지 못했다. 세 회사가 4주 안에 쓰러졌다는 당시 기록이 남아 있다. 지금 daqri.com은 도메인 파킹 랜더로 넘어가고, osterhoutgroup.com은 무관한 외부 사이트로 리다이렉트된다. 실패 원인으로 반복 지목된 것은 기술이 아니라 단가와 예산 주기였다 — 데모는 항상 훌륭했고, 건설 현장의 예산 사이클은 그렇지 않았다.

세 회사 모두 청산·자산매각. Daqri 자산은 Snap이 인수했다고 보도됐다. 건설 현장용 헤드마운트 AR의 독립 공급자가 사라지고, 남은 선택지는 마이크로소프트 HoloLens 하나였다 — 그마저 2024년에 단종됐다.

### Snap AR 기업사업부 7개월 폐쇄 · 니안틱 8th Wall/Lightship VPS 종료 — 플랫폼 사업자의 이탈
| 항목 | 내용 |
| --- | --- |
| 주체 | Snap Inc.(ARES). Niantic → Niantic Spatial(8th Wall, Lightship ARDK/VPS) |
| 도시·연도 | 미국, ARES 2023-03~2023-09 / 8th Wall 2022-03 인수 → 2027-02-28 호스팅 종료 |
| 증거 수준 | 실제 납품 — 상용 서비스의 폐쇄 및 공식 전환 공지 |
| AR 여부 | AR 맞음. 둘 다 실세계 정합 AR 인프라이고, Lightship VPS는 실제 도시 랜드마크에 콘텐츠를 고정하는 시각 측위였다. |
| 규모 | ARES 출범 2023년 3월, 폐쇄 2023년 9월, 감원 약 170명. 8th Wall 인수 2022년 3월(금액 비공개, 니안틱 역대 최대). Lightship VPS 베타 대상 도시 5곳 |
| 기술 | Lightship VPS(건물 외관 기반 시각 측위 + 영구 앵커), 8th Wall WebAR 엔진, Snap 카메라 AR 스택 |
| 출처 | https://techcrunch.com/2023/09/27/snap-shutters-its-enterprise-services-division-after-less-than-a-year/ · https://info.nianticspatial.com/blog/8th-wall-update-engine-distribution-and-open-source-plans · https://www.niantic.dev/learn/tools/tutorials/vps/ardk_fundamentals/system_reqs.html · (404 확인) https://www.snap.com/en-US/ar-enterprise |

도시 규모 AR의 마지막 기술적 관문은 측위다. GPS로는 수 미터가 어긋나므로 실제 건물 외관을 인식해 위치를 잡는 VPS(Visual Positioning System)가 필요하다. 그 인프라를 가진 곳은 소수의 플랫폼 사업자였고, 둘이 물러났다. Snap은 2023년 3월 AR Enterprise Services(ARES)를 출범시켜 자사 AR 기술을 기업 앱·웹·매장에 넣어주는 사업을 시작했다. 7개월 뒤인 2023년 9월 사업부를 폐쇄하고 약 170명을 감원했다 — AI 도구의 등장으로 경쟁우위가 흐려지고 투자 우선순위를 옮겨야 한다는 이유가 보도됐다. snap.com의 AR 기업 페이지는 현재 404다. 니안틱(현 Niantic Spatial)은 2022년 3월 WebAR 플랫폼 8th Wall을 '역대 최대 규모 인수'로 사들여 Lightship ARDK와 묶었고, Lightship VPS로 시애틀·뉴욕·샌프란시스코·로스앤젤레스·런던의 랜드마크에 WebAR 콘텐츠를 영구 고정할 수 있게 했다. 지금 호스팅된 8th Wall 서비스는 2027년 2월 28일까지만 유지되고, 엔진은 배포·오픈소스화된다. 문제는 그 다음 문장이다 — Niantic Spatial 서비스가 8th Wall 엔진에서 분리되어 배포 바이너리에 포함되지 않으며, 여기에 Niantic Spatial VPS, Lightship Maps, Geospatial Browser가 포함된다. 엔진은 남고 도시 정합 능력은 남지 않는다.

Snap ARES 폐쇄. 8th Wall 호스팅은 2027-02-28까지, 이후 오픈소스 엔진만 남고 VPS·Lightship Maps·Geospatial Browser는 제외. 도시 규모 AR을 외부 개발자가 쓸 수 있는 상용 VPS 경로가 좁아졌다.

#### 검증에서 잡힌 정정
- ARCHEOGUIDE '1999 착수'는 오류. CORDIS 팩트시트는 Start date 1 January 2000 / End date 30 June 2002로 명시한다. '1999'는 과제번호 IST-1999-11306의 공모 연도이며 착수 연도가 아니다. (덧붙여 '34개월·2002년 10월 종료'는 CORDIS 팩트시트가 아니라 같은 사이트의 IST Results 해설 기사에만 나오는 값으로, 팩트시트의 30개월·2002-06-30과 자체 모순이다.)
- VIDENTE·SMART VIDENTE 기간 '2007~2012'는 양끝 모두 오류. TU Graz 공식 프로젝트 페이지는 VIDENTE 1/03/06 → 30/09/08, Smart Vidente 1/03/09 → 28/02/11로 적는다. 실제 합산 구간은 2006-03 ~ 2011-02이다.
- POMAR 3D의 참여기관으로 적은 'OHB Austria'는 해당 austria-in-space.at 과제 페이지에 존재하지 않는다. 문서에 적힌 수행기관은 TU Graz Institute for Computer Graphics and Vision(Dieter Schmalstieg, Gerhard Schall)과 TU Graz Institute of Navigation and Satellite Geodesy(Bernhard Hofmann-Wellenhof, Norbert Kühtreiber)이며 기간은 2007년 9월~2008년 9월이다.
- 취리히 현장실험 '2022 수행'은 오류. 논문 본문: 'a field study had been conducted in the south of Zurich, Switzerland (47.341 N, 8.520 E) between 26th June and 31st July 2020.' 실험은 2020년 6월 26일~7월 31일에 수행됐고 2022는 온라인 게재 연도다.
- 취리히 사례의 결론 서술('AR이 Baugespann을 대체하지 못했다', '수행 성적은 따라오지 않았다')은 논문 내용과 반대 방향이다. 논문 수치는 AR 높이 약 31% 과대추정(평균 오차 6.27 m)이고 Baugespann은 '한 명을 제외한 전원이 과소추정, 평균 약 34%'로, AR 오차가 더 작다. 결론부는 'Participants rated the suitability of construction spans as visualisation method lower than an AR application'이며 두 방법을 대체 관계가 아니라 용도 분담(스팬=고지, AR=설계 상세)으로 정리한다.
- Unity Reflect의 '2024년 6월 30일 서비스 종료'는 제품 혼동. 2024-06-30은 VisualLive의 날짜다(Unity 공식 FAQ 아카이브: 'The last day to purchase VisualLive ... is June 30, 2023 ... Maintenance support ... will end one year later, on June 30, 2024'). 같은 항목이 인용한 Arkio 글은 Unity Reflect에 대해 '2024년 말까지 지원'이라 적고, 아카이브된 Unity Reflect 제품 페이지에는 종료일 없이 '계약 기간까지'만 나온다.
- 'Trimble XR10 ... 2016 발표'는 오류. XR10은 HoloLens 2 기반 제품이고 HoloLens 2 자체가 2019년 2월 24일 발표다. 인용된 AECOM 보도자료는 2016년 6월 13일자 Microsoft HoloLens+Trimble 혼합현실 소프트웨어 발표이며 XR10은 등장하지 않는다.
- '2016년 공동 발표 파트너는 AECOM, Gensler'에서 Gensler는 인용 출처에 없다. AECOM 보도자료(2016-06-13)에는 AECOM, Trimble, Microsoft HoloLens만 나오고 Gensler도 SketchUp Viewer도 언급되지 않는다.
- 8th Wall 제외 서비스 목록의 'Geospatial Browser'는 공지에 없다. Niantic Spatial 공지가 엔진 바이너리에서 제외한다고 적은 것은 Niantic Spatial VPS(Lightship VPS for Web), Lightship Maps, Hand Tracking 세 가지다. (또한 엔진 바이너리 유지는 2026년 3월까지이고 이후에도 영구 다운로드 가능이라고 적혀 있어 '오픈소스 엔진만 남는다'는 요약과 결이 다르다.)
- '2024-10-01 HoloLens 2 생산종료'는 인용 출처가 뒷받침하지 않는다. 인용한 위키백과 HoloLens 2 문서의 infobox discontinued 필드는 비어 있고, 본문 근거는 2024년 10월 1일자 The Verge 기사 'Microsoft is discontinuing its HoloLens headsets'다. 즉 이 날짜는 단종 발표·보도일이며 생산 종료일로 특정할 근거는 없다(지원 종료 2027-12-31만 명시).
- Daqri의 'Smart Helmet 1만 5천 달러 / Smart Glasses 약 5천 달러'와 '자산은 Snap이 인수했다고 보도됐다'는 인용된 6개 출처(TechCrunch 2019-09-12, Wikipedia Daqri, digitalbodies 등) 어디에도 없다. TechCrunch는 '$275 million 조달'과 '자산 매각 추진(pursuing an asset sale)'까지만 말하고 인수자를 특정하지 않으며, digitalbodies 기사에는 Daqri가 아예 등장하지 않는다(해당 기사의 가격 정보는 ODG 안경 $1,000~$2,000이다). Snap 인수는 별도 확인도 되지 않았다.
- Trimble의 '2027-09-30 지원 종료'는 출처 간 충돌을 단일 날짜로 단정한 것이다. 대만 총판(zhinc)은 '2025/12/31 판매 종료, 2027/9/30 지원 종료'라 하지만, 같은 항목이 인용한 니콘·트림블(일본) 페이지(2026.02.05 공지)는 'HoloLens 2部の ... サポートにつきましては、2027年12月31日までマイクロソフトより提供されます'로 2027-12-31을 제시한다(HoloLens 2 본체 지원 종료일과 일치).
- 취리히 현장실험 결론 역전 (가장 심각): 사례는 '높이 31% 과대추정'을 근거로 'AR이 Baugespann을 대체하지 못했다'고 했으나, Boos et al. 2023 원문 결론은 정반대다 — "In line with the results of our study we conclude that AR applications are more suitable than construction spans for visualising a building project." 31%는 AR 가상 학교건물 높이의 과대추정치이고, 같은 논문에서 Baugespann 높이는 평균 약 34% 과소추정됐다("all other participants underestimated them, by about 34% on average", 정확 추정 3명, 과대추정 1명). 즉 AR 오차가 Baugespann보다 작았다. 출처: research-collection.ethz.ch 전문(JLBS 17(1) 48-77)
- 취리히 현장실험 수행 연도: '2022 수행'이 아니라 2020년 6월 26일~7월 31일 수행. 원문 3장 "a field study had been conducted in the south of Zurich, Switzerland (47.341 N, 8.520 E) between 26th June and 31st July 2020"; Baugespann 사진 캡션도 2020-06-25. 2022는 논문 접수(2022-02-06)·게재승인(2022-06-01) 연도다.
- ARCHEOGUIDE 기간·종료일: 사례가 인용한 바로 그 CORDIS(IST-1999-11306)는 시작 2000-01-01, 종료 2002-06-30(= 30개월)로 표기한다. '1999 착수 → 2002년 10월 종료', '34개월'은 인용 출처와 불일치.
- ARCHEOGUIDE 사업비 '미공개' 주장: CORDIS 해당 과제 페이지는 Total cost €4,851,991.00, EU contribution €2,600,000.00을 명시하고 있다. '사업비는 CORDIS에 미공개'는 사실과 반대.
- VisualLive 일몰 타임라인: Unity 공식 VisualLive 종료 FAQ(archive 2023-09-14)는 '구매 마지막 날 2023-06-30', '유지보수 종료 2024-06-30'으로 적는다. 따라서 '2023년 8월 일몰 발표'는 VisualLive에 적용되지 않는다(구매창이 이미 6월 말 닫혔다). 사례가 근거로 붙인 LinkedIn 글(activity 7098008146949861376 = 2023-08-17)은 Unity Reflect 건이다.
- Unity Reflect 종료일: 사례가 인용한 Arkio 블로그는 Unity Reflect가 '2024년 말까지 지원(supported until the end of 2024)'된다고 명시한다. '두 제품 모두 2024년 6월 30일 서비스 종료'는 틀림 — 2024-06-30은 VisualLive만 해당.
- '전환 대안으로 Unity가 지정한 업체는 아이슬란드 Arkio' (VisualLive 맥락): Unity의 VisualLive 종료 FAQ 전문에는 Arkio·BIM Holoview·대안·third-party가 단 한 번도 등장하지 않는다(0건). Arkio 블로그가 말하는 것은 Unity Reflect Review 사용자 대상 권고다. '고객은 Arkio·BIM Holoview 등 제3자 도구로 이전했다'의 BIM Holoview는 인용 출처 어디에도 없다.
- Trimble/HoloLens 2016년 공동 발표 파트너 'Gensler': 사례가 인용한 AECOM 보도자료(2016-06-13)에 등장하는 조직은 AECOM, Trimble, Microsoft, Serpentine Galleries뿐이며 Gensler는 언급되지 않는다.
- Trimble XR10 판매·지원 종료 날짜의 출처 혼합: 사례가 1순위로 붙인 니콘·트림블 공지는 게시일 2026-02-05이며 판매 종료 날짜를 명시하지 않고 'HoloLens 2 주요 기능 지원은 2027년 12월 31일까지 마이크로소프트가 제공'이라고 적는다. '2025-12-31 판매 종료 / 2027-09-30 지원 종료'는 대만 총판(中翰國際) 공지에만 있는 수치로, 두 출처의 지원 종료일(2027-12-31 vs 2027-09-30)이 상충하는데 사례는 이를 하나로 섞었다.
- POMAR 3D 참여기관 'OHB Austria': 사례가 인용한 austria-in-space.at 과제 페이지의 Project Partners는 Graz University of Technology, Institute for Computer Graphics and Vision(조정자, Dieter Schmalstieg·Gerhard Schall)과 Graz University of Technology, Institute of Navigation and Satellite Geodesy(Bernhard Hofmann-Wellenhof·Norbert Kühtreiber) 둘뿐. 페이지 전문에 'OHB' 문자열은 0건이다.
- VIDENTE·SMART VIDENTE 기간 '2007~2012': TU Graz 과제 DB(사례 인용 URL)는 VIDENTE 2006-03-01~2008-09-30, Smart Vidente 2009-03-01~2011-02-28로 적는다. 실제 범위는 2006~2011이며 2012년까지 이어지지 않았다.
- Google Measure를 Tango 종속 앱으로 서술: 사례 인용 9to5Google(2021-06-08)은 Measure가 원래 Tango 앱이었으나 2018년 Tango 종료 시 ARCore로 이식돼 '모든 안드로이드폰'에서 동작하게 됐다고 명시한다. 2021년 삭제된 것은 그 ARCore 버전이다. '(Tango) 그 위에서 실측치를 겹쳐 표시했다' 및 '전용 센서를 산 이용자와 그 위에 앱을 올린 개발자는 보상 없이 정리됐다'는 인과는 성립하지 않는다.
- 'Blippar 계보는 끊겼다': Blippar Group Limited는 2019년 Candy Ventures 인수 이후 현재까지 운영 중이다. blippar.com은 Blippbuilder·WebAR SDK·Solutions를 판매하며 '© Blippar Group Limited', 'Trusted by 100,000+ brands'를 게시하고(신규 구독만 일시 중단 고지), 사례가 각주로 인용한 docs.blippar.com도 살아 있다. 소멸한 것은 2018년 법인과 AR City 앱이지 계보가 아니다.
- AR City '300개 이상 도시': 사례 인용 Blippar 공지 원문은 'The app helps you navigate and explore 300 cities worldwide' — 정확히 300으로, '이상'이 아니다. 또 그 공지의 published_time 메타데이터는 2018-10-10T11:08:09+01:00이고 본문 서명도 '10/10/2018'인데, 사례는 같은 URL을 근거로 'AR City 2017-11'이라 적었다.
- Snap ARES를 '실세계 정합 AR 인프라'로 분류: 사례 인용 TechCrunch(2023-09-27)에 따르면 ARES가 제공한 것은 AR 트라이온 Shopping Suite, 3D 제품 뷰어, 핏·사이즈 추천, 에셋 호스팅 매니저, Live Garment Transfer로 커머스/착용 AR이다. 월드스케일·지리등록 인프라가 아니므로 Lightship VPS와 '둘 다 실세계 정합 AR 인프라'로 묶을 수 없다.
- 'Daqri 자산은 Snap이 인수했다고 보도됐다': 사례가 붙인 6개 출처 전부에 Snap이 없다. TechCrunch 2019-09-12은 'pursuing an asset sale'만 적고 인수자를 밝히지 않으며, Wikipedia Daqri도 인수자를 특정하지 않는다. TechCrunch 2019-12-20은 Meta 자산이 Olive Tree Ventures(→Meta View)로, ODG 자산은 'an undisclosed buyer'로 갔다고 적는다 — 사례는 이 두 건과 혼동한 것으로 보인다.
- Lightship VPS '베타 대상 도시 5곳'의 근거 부재: 사례가 인용한 niantic.dev/learn/tools/tutorials/vps/ardk_fundamentals/system_reqs.html은 ARDK 시스템 요구사항 문서이며(현재 nianticspatial.com/docs/nsdk로 307 리다이렉트) 도시 목록이나 도시 수를 담고 있지 않다.
- Trimble '2021-08-30(HoloLens 1 앱)': 사례가 나열한 5개 URL 중 어느 것도 이 날짜를 담고 있지 않다(SketchUp EOL 페이지는 2024-07-08 구매 종료·2025-07-08 지원 종료만 명시). 출처 미지원 날짜.
- (외 21건)

\newpage

# 조경 — 국내·식생

## korea
항목 14개 · 검증 정정 지적 0건

> 한국에서 '조경'과 '증강현실'을 정면으로 붙인 사례는 손에 꼽는다. 2018년 11월 대우건설이 반포 써밋 단지 정원에 'AR 가든' 앱을 넣은 것이 국내 최초로 기록되고, 이듬해 안산 초지역 메이저타운 푸르지오 3개 단지로 확대됐다. 그러나 이 계보는 조경 설계·시공의 도구가 아니라 입주민 체험 콘텐츠였고, 지금 구글플레이에서 그 앱은 검색되지 않는다.  돈이 실제로 들어가고 지금도 돌아가는 쪽은 조경이 아니라 땅 밑이다. 제주도는 2021년 9월 한전·한전KDN과 협약한 뒤 2025년 5월 'AR 기반 지하시설물 모바일 현장업무 지원시스템'을 본격 운영에 넣었고, 한전KDN은 Multi-GNSS와 AR을 묶은 지하시설물 안전관리 솔루션으로 2023년 11월 행안부·산업부 장관 표창을 받았다. 대구 에이알미디어웍스는 수성알파시티 실증을 거쳐 안심뉴타운(2022)·금호워터폴리스(2024)에 통합관제시스템을 납품했다 — 다만 2024년 매출 16억1천만원인 회사다. 옥외 AR의 실체적 수요는 '식물을 어떻게 보여줄까'가 아니라 '파기 전에 땅 밑을 보자'였다.  공공 공간 콘텐츠 쪽은 부침이 심하다. 국립공원공단 '스마트탐방 파크'(2018~2019)와 서울시·문화재청의 돈의문 AR(2019)은 앱 자체가 사라졌다. 반면 2023년 '1887 경복궁 진하례'는 근정전 현장 AR로 남았고, 2026년 서울국제정원박람회는 앱 설치 없는 QR/웹 방식 AR 보물찾기 '가든헌터스'로 돌아섰다 — 전용 앱 설치라는 문턱이 실패 원인으로 학습된 흔적이다. 2024년 10월 '메타버스 서울'이 55억~60억원을 쓰고 1년 9개월에 문을 닫은 사건이 이 학습의 배경에 있다. 2026년 3월에는 도시공원에 AR·VR을 쓸 법적 근거를 만들자는 이른바 '디지털 공원법' 개정안이 발의됐다. 그동안 근거가 없었다는 뜻이다.


### 대우건설 '푸르지오 AR가든' (반포 써밋 → 안산 메이저타운)
| 항목 | 내용 |
| --- | --- |
| 주체 | 대우건설(IT실 자체개발). 발주처 없음 — 시공사 자체 서비스 |
| 시기·장소 | 대한민국 서울 서초구 반포동(2018.11) → 경기 안산 초지역 메이저타운 3개 단지(2019.09) → 화성 동탄 행복마을 |
| 증거 수준 | 실제 납품 |
| 수치 | 적용 단지: 반포 써밋 1개 + 안산 3개 + 동탄 1개. 명화 12점, 동물 20여 종. 개발비·이용자 수는 공개된 적 없음 |
| 기술 | 스마트폰 전용 앱, GPS 위치 트리거 기반 마커리스 AR(단지 좌표에 콘텐츠를 배치하는 방식). SLAM이나 정밀 측위 언급 없음. 명화 12점, 동물 캐릭터 20여 종 |
| 출처 | 조선일보 '아파트 조경에 증강현실 적용' https://n.news.naver.com/article/023/0003411612 · 환경과조경 '"아파트 조경 증강현실로 체험한다"' http://www.lak.co.kr/news/boardview.php?id=5604 · 글로벌이코노믹 http://m.g-enews.com/view.php?ud=201909271602004834891d26c649_1 · 아시아투데이 '정원에 토끼가 깡총' http://m.asiatoday.co.kr/kn/view.php?key=20181121010012124 · 구글플레이 검색(2026-09-30) |

아파트 단지 조경 공간에 스마트폰 AR을 얹은 입주민 체험 서비스다. 대우건설 IT실이 자체 개발했고, 2018년 11월 서울 서초구 반포동 삼호가든4차 재건축 단지 '반포 써밋'에 처음 적용됐다. 앱을 켜면 단지 네 곳에서 노루·새·다람쥐·토끼 같은 숲속 동물 캐릭터가 나타나 같이 사진을 찍을 수 있는 방식이었다. 2019년 9월에는 경기 안산 초지역 메이저타운 푸르지오 메트로·파크·에코 3개 단지로 확대하면서 GPS 수신으로 단지 안에서 모나리자·진주 귀걸이를 한 소녀 등 명화 12점을 찾는 갤러리 서비스와 놀이터의 동물 20여 종, 어린이 안전교육 동영상을 추가했다. 이후 '동탄 행복마을 푸르지오'에서도 AR가든을 적용 사례로 내세웠다. 조경 '설계'나 '시공'의 도구가 아니라 준공된 조경을 놀이 콘텐츠로 재소비하는 방향이었다는 점이 중요하다.

현재 구글플레이 스토어에서 '푸르지오 AR가든' 또는 'AR가든' 앱이 검색되지 않는다(2026년 9월 확인). 공식 종료 공고는 찾지 못했으나 사실상 소멸로 보인다. 종료 이유는 회사가 밝힌 바 없음. 추정 요인: 전용 앱 설치 요구, 단지별 콘텐츠 제작비, 분양 마케팅이 끝나면 유지 동기가 사라지는 구조

### 2026 서울국제정원박람회 AR 보물찾기 '가든헌터스'
| 항목 | 내용 |
| --- | --- |
| 주체 | 발주·주최: 서울특별시. 콘텐츠·플랫폼: 유니크굿컴퍼니(AR·AI 경험 플랫폼 '리얼월드') |
| 시기·장소 | 대한민국 서울 성동구 서울숲·성수동 일대. 2026년 5월 6일 개시, 박람회 기간 2026년 5월 1일~10월 말(180일) |
| 증거 수준 | 실제 납품 |
| 수치 | 박람회 전체: 정원 167개소, 180일, 개막 48일 만에 누적 방문객 500만 명 돌파(2026.06.17 기준, 서울시 발표). 가든헌터스 자체 참여자 수는 공개되지 않음 |
| 기술 | 앱 설치 없는 QR 진입(웹 기반), GPS 측위 + AR 오버레이. 정밀 측위나 VPS 사용 여부는 공개되지 않음 |
| 출처 | 연합뉴스 https://n.news.naver.com/article/001/0016053132 · 중앙일보 https://n.news.naver.com/article/025/0003520280 · 헤럴드경제 https://n.news.naver.com/article/016/0002640982 · 디스이즈게임(유니크굿컴퍼니 협업 명시) https://www.thisisgame.com/articles/421808 · 소년한국일보(500만 명) https://www.kidshankook.kr/news/articleView.html?idxno=17447 |

서울시가 서울숲을 중심으로 2026년 5월 1일부터 180일간 연 역대 최대 규모 정원박람회의 공식 참여 프로그램이다. 관람객이 서울숲과 성수동 일대를 돌아다니며 스마트폰으로 미션을 수행하는 AR+GPS 기반 보물찾기로, 2026년 5월 6일부터 운영을 시작했다. 핵심은 기술이 아니라 전달 방식이다 — 별도 애플리케이션 설치 없이 QR코드만 스캔해 참여한다. AR·AI 기반 경험 플랫폼 '리얼월드'를 운영하는 유니크굿컴퍼니와 협업해 구현했다. 도슨트 투어, 9개 언어 모바일 도슨트와 함께 '체험 프로그램' 묶음으로 배치됐고, 외국인 관람객 호응을 기대한다고 서울시가 밝혔다.

박람회 기간 중 운영. 방문객 500만 명은 박람회 전체 수치이고 AR 프로그램의 이용 실적으로 볼 수는 없다. 8월 서울시의회 환경수자원위원회 현장점검에서도 도슨트 투어·AR 체험이 '시민 참여 프로그램'으로만 언급됐고 별도 이용 지표는 제시되지 않았다. 박람회 종료 후 존속 여부 미정

### 제주특별자치도 AR 기반 지하시설물 모바일 현장업무 지원시스템
| 항목 | 내용 |
| --- | --- |
| 주체 | 제주특별자치도(혁신산업국·미래전략국). 협력: 한국전력공사 제주본부, 한전KDN 전력ICT연구원 |
| 시기·장소 | 대한민국 제주특별자치도 전역. 2021년 9월 MOU → 2022년 6월 착수보고 → 2025년 5월 본격 운영 |
| 증거 수준 | 실제 납품 |
| 수치 | 병행 추진된 지하시설물 정확도 개선사업 사업비 약 7억 원(국비 2억·도비 5억), 상수관로 77.6km 정확도 개선. AR 시스템 자체의 사업비는 공개되지 않음. 착수보고회 참석 20여 명 |
| 기술 | AR + GNSS(위성항법) 정밀 측위, 태블릿 앱. 상·하수관로 및 전력 지하매설물 대상 |
| 출처 | 삼다일보(2025.05.08) http://www.samdailbo.com/news/articleView.html?idxno=246095 · 헤드라인제주(2022.06.21, 사업비·77.6km) http://www.headlinejeju.co.kr/news/articleView.html?idxno=489590 · 제주도민일보(2021.09.14 MOU) https://www.jejudomin.co.kr/news/articleView.html?idxno=205830 · 보안뉴스(현장 시현) http://m.boannews.com/html/detail.html?idx=100741 |

도내 상하수관로의 위치와 심도 등 속성정보를 현장에서 태블릿으로 조회하고 AR로 중첩 표시하는 시스템이다. 종이 도면을 출력해 현장에 들고 가야 했고 도면 정보를 실시간 확인할 수 없었던 문제를 해결하려는 목적이었다. 2021년 9월 제주도가 한국전력공사 제주본부와 한전KDN 전력ICT연구원과 'AR 기반 도로기반시설물 통합 안전관리체계' 업무협약을 맺으면서 시작됐고, 2022년 6월 지하시설물 정확도 개선사업과 함께 AR 통합관리시스템 구축을 착수했다. 2025년 5월 8일 제주도는 상하수도 담당자 교육을 마치고 5월 말부터 본격 운영한다고 발표했다. 국내 공공 AR 지하시설물 사업 중 협약에서 실운영까지 4년의 경로가 문서로 확인되는 드문 사례다.

2025년 5월 운영 개시, 시범운영으로 기능 보완 병행. 이후 이용 실적·정확도 개선 효과에 대한 독립 검증 자료는 찾지 못했다. 효율성 향상 주장은 모두 제주도 자체 기대치

### 한전KDN AR 기반 지하시설물 통합 안전관리시스템 (Multi-GNSS 연계)
| 항목 | 내용 |
| --- | --- |
| 주체 | 한전KDN(전력ICT연구원). 적용·협력: 한국전력공사 전북본부, 해양에너지, 한국전력기술, 제주특별자치도 |
| 시기·장소 | 대한민국 전북(송전, 2020.02) · 광주·전남 효천지구(도시가스, 2020.07) · 경북 김천 한국전력기술(발전소, 2021.02 협약) · 제주(2021~2025) |
| 증거 수준 | 실제 납품 |
| 수치 | 사업비·적용 현장 수·정확도(측위 오차) 수치는 공개 자료에서 확인되지 않음 |
| 기술 | AR 중첩 + Multi-GNSS 정밀 측위. 태블릿·모바일 앱. 대상: 송전·배전 지하설비, 도시가스 배관, 상하수도, 발전소 지하매설물 |
| 출처 | 전남일보(2020.02.13) https://jnilbo.com/?p=879927 · 이투뉴스(해양에너지, 2020.07.02) http://www.e2news.com/news/articleView.html?idxno=223917 · 국토일보(한전기술 MOU, 2021.02.17) http://www.ikld.kr/news/articleView.html?idxno=230775 · 컨슈머타임스(장관 표창, 2023) https://www.cstimes.com/news/articleView.html?idxno=570129 · 이투뉴스(정부혁신 박람회) http://www.e2news.com/news/articleView.html?idxno=228063 |

한전KDN이 개발한, 굴착 전에 지하 매설물 위치를 현장에서 AR로 겹쳐 보는 안전관리 솔루션이다. 핵심은 AR 렌더링이 아니라 측위다 — 작업 현장에서 지하시설물의 정확한 위치를 잡기 위해 Multi-GNSS 기반 위성항법시스템을 함께 개발했다. 2020년 2월 한전 전북본부와 협업해 송전 분야 지하시설물 AR 솔루션을 개발하고 현장 적용을 완료했고, 같은 해 7월 광주·전남 도시가스 공급사 해양에너지가 효천지구 정압기 인근에서 도시가스 배관 AR 안전관리를 시연했다. 2021년 2월에는 한국전력기술과 'AR 활용 발전소 지하매설물 관리시스템 구축' 협약을 맺었다. 2020년 정부혁신 박람회에 출품하고, 2023년 11월 행정안전부·산업통상자원부 장관 표창을 동시 수상했다.

현장 적용 완료 및 확산. 2023년 11월 정부 혁신 우수사례로 장관 표창 2건. 다만 '싱크홀·도로굴착사고 불안 해소'라는 효과 주장은 한전KDN 관계자 발언이며, 사고 감소를 측정한 제3자 평가는 확인되지 않았다

### 에이알미디어웍스 — 대구 스마트시티 지하매설물 AR 통합관제
| 항목 | 내용 |
| --- | --- |
| 주체 | (주)에이알미디어웍스(대표 손정봉). 지원: 경북대 지산학연협력기술연구소. 발주: 대구시 및 스마트시티 사업 주체 |
| 시기·장소 | 대한민국 대구광역시 — 수성알파시티(실증), 안심뉴타운 스마트시티(2022), 금호워터폴리스(2024) |
| 증거 수준 | 실제 납품 |
| 수치 | 매출 2023년 9억6천만 원 → 2024년 16억1천만 원. 수출액 2023년 2만 달러 → 2024년 8만 달러. 구축 현장 3곳(실증 1 + 납품 2) |
| 기술 | AR SDK 자체 개발, 지하매설물 AR 관제 특허 + GS인증, 스마트글래스 하드웨어 자체 설계, AI 균열 탐지 |
| 출처 | 매일신문(2026.02.24) https://n.news.naver.com/article/088/0000998204 · 보안뉴스(수성알파시티 MR 지하매설물 콘텐츠, 2020.07.28) http://m.boannews.com/html/detail.html?idx=90093 |

2012년 설립된 대구 기업으로, 초기에는 AR 소프트웨어 개발 툴킷(SDK)을 만들었고 이후 증강현실 기반 지하매설물 관제시스템 특허와 GS인증을 받았다. 상·하수도와 통신관로 등 지하 매설 관로를 AR로 시각화하고 굴착 공사를 실시간 관리하는 것이 주력이다. 대구 수성알파시티에서 실증을 거쳐 안심뉴타운 스마트시티(2022년)와 금호워터폴리스(2024년)에 통합관제시스템을 구축했다. 경북대 지산학연협력기술연구소의 '대구형 R&D 전주기 지원체계' 사업으로 스마트글래스 하드웨어 제작, AI 모델 고도화, 플랫폼 구축 초기 개발비를 지원받아 수성알파시티 실증을 완료했다. 2026년 1월 CES에서 AI 기반 스마트글래스 교량 안전진단 솔루션을 선보였다. 국내 옥외 AR 전업 기업의 실제 사업 규모를 보여주는 표본이다.

사업 계속 중, 인프라 안전관리(교량·터널·댐)로 확장 추진. 성장하고 있지만 절대 규모는 매출 16억 원대다 — 국내 옥외 AR 시장이 아직 산업이라 부를 크기가 아님을 시사한다. '높은 균열 탐지 정확도'는 대표 발언이며 구체 수치나 독립 검증 없음

### 국립공원공단 '스마트탐방 파크(PARK)' AR 앱 — 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | 환경부 산하 국립공원관리공단(이사장 권경업 당시) |
| 시기·장소 | 대한민국 경주국립공원(2018년 시작) → 설악산 등 확대(2019년 11월 25일) |
| 증거 수준 | 실제 납품 |
| 수치 | 사업비, 대상 공원 수, 다운로드·이용자 수 모두 공개 자료에서 확인되지 않음 |
| 기술 | 스마트폰 전용 앱, 카메라 영상 위 가상 이미지·영상 중첩. 측위·정합 방식은 공개 자료에 명시되지 않음 |
| 출처 | 경남일보(2019.12.04) http://www.gnnews.co.kr/news/articleView.html?idxno=429535 · 보안뉴스(2019.11.26) http://m.boannews.com/html/detail.html?idx=84759 · 에너지데일리(토왕성폭포 재현) http://www.energydaily.co.kr/news/articleView.html?idxno=104258 · 월간 산(국립공원 산행정보 앱 2024.12.31 종료) https://n.news.naver.com/article/094/0000012318 · 구글플레이 검색(2026-09-30) |

환경부 산하 국립공원관리공단(현 국립공원공단)이 만든 AR 기반 국립공원 탐방 앱이다. 스마트폰 화면의 실제 영상 위에 가상 이미지를 중첩해 부가 정보를 주는 방식으로, 2018년 경주국립공원의 불국사·감은사지 등 문화재 복원 해설로 시작했다. 2019년 11월 25일부터 설악산 등으로 확대 제공했는데, 대표 콘텐츠는 물이 마른 설악산 토왕성폭포에 물줄기를 AR로 재현해 보여주는 것이었다. 국내 공공기관이 자연·경관 공간 자체를 대상으로 AR을 넣은 몇 안 되는 사례이고, 특히 '없어진 자연 현상(폭포 수량)을 현장에 되돌려 보여주는' 조경적 발상이 들어간 드문 시도였다.

소멸. 2026년 9월 현재 구글플레이 스토어에서 '스마트탐방 파크'가 검색되지 않는다(검색 결과에는 '국립공원 탐방알리미' 등 다른 앱만 나옴). 공식 종료 공고는 찾지 못했다. 같은 기관의 '국립공원 산행정보' 앱도 2024년 12월 31일까지만 운영한다고 보도된 바 있어, 공단의 앱 포트폴리오 정리 흐름과 맞물린 것으로 보인다. 기술적 실패가 아니라 유지·갱신 주체와 예산이 끊기는 공공 앱의 전형적 소멸로 읽힌다

### 돈의문 AR·VR 디지털 복원 — 소멸
| 항목 | 내용 |
| --- | --- |
| 주체 | 서울특별시 + 문화재청 + 우미건설(우미희망재단) + 제일기획 |
| 시기·장소 | 대한민국 서울 종로구 정동사거리(돈의문 터). MOU 2018년 12월 6일, 공개 2019년 8월 20일 |
| 증거 수준 | 실제 납품 |
| 수치 | 프로젝트 사업비는 공개되지 않음(참고: 별개 사업인 돈의문 박물관마을 조성 예산 330억 원, 2017년). 이용자 수 미공개 |
| 기술 | 스마트폰 전용 AR 앱 + VR. 특정 장소(정동사거리)에서 실행하는 위치 기반 방식. 정합 정확도·측위 방식은 공개되지 않음 |
| 출처 | 경인일보(2018.12.06 MOU) http://m.kyeongin.com/view.php?key=20181206010001942 · MBC(2019.08.20 공개) https://n.news.naver.com/article/214/0000973304 · 아주경제 http://m.kr.ajunews.com/view/20190821085148378 · MBC(2024.01.15 실물 복원 재검토·330억) https://n.news.naver.com/article/214/0001324757 · 대한경제(도시재생포럼) http://m.dnews.co.kr/m_home/view.jsp?idxno=202011180827294430880 · 구글플레이 검색(2026-09-30) |

1915년 일제가 전차 복선화를 위해 강제 철거한 한양도성 사대문 중 서쪽 문 돈의문을, 실물 복원 대신 AR로 제자리에 되살린 프로젝트다. 2018년 12월 6일 경복궁 고궁박물관에서 서울시·문화재청·우미건설·제일기획이 '문화재 디지털 재현 및 역사문화도시 활성화' MOU를 체결하고, 2019년 8월 20일 완료를 발표했다. 전용 AR 앱을 내려받아 종로구 정동사거리 주변에서 실행하면 과거 돈의문의 모습을 여러 각도에서 볼 수 있었다. 이 프로젝트의 배경이 중요하다 — 돈의문 실물 복원은 오세훈 시장 시절 교통난과 보상 비용, 시장 중도 사퇴로 무산됐고, 박원순 시장 시절 2017년 예산 330억 원으로 돈의문 박물관마을을 조성했다. 물리적 복원이 불가능한 도시 공간에 AR이 대체재로 투입된 사례다.

소멸. 2026년 9월 현재 구글플레이에서 '돈의문 AR' 해당 앱이 검색되지 않는다. 2024년 1월 서울시는 돈의문 실물 복원 방안을 다시 검토한다고 밝히며 문화재청 협의가 필요하다고 했다 — AR 복원이 실물 복원 논의를 대체하지 못했다는 뜻이다. 제작 주체 중 우미건설은 2020년 도시재생포럼에서 이 사업을 '도시역사재생'으로 소개했으나, 이후 확장 사례는 확인되지 않는다

### '1887 경복궁 진하례' AR·XR 궁중의례 재현
| 항목 | 내용 |
| --- | --- |
| 주체 | 문화재청(청장 최응천) + 서울특별시(시장 오세훈) + 우미희망재단(이사장 이석준) + 제일기획(대표 김종현) |
| 시기·장소 | 대한민국 서울 종로구 경복궁 근정전. 2023년 11월 22일 서비스 개시(선행: 군기시 2023년 2월, 돈의문 2019년 8월) |
| 증거 수준 | 실제 납품 |
| 수치 | 사업비·이용자 수는 공개 자료에서 확인되지 않음 |
| 기술 | 모바일 앱 기반 AR + XR. 근정전 현장에서 앱을 실행하면 진하례 장면이 재현되는 위치 기반 방식 |
| 출처 | 서울문화투데이(2023.11.24) http://www.sctoday.co.kr/news/articleView.html?idxno=41881 · 뉴스저널리즘 https://www.ngetnews.com/news/articleView.html?idxno=427088 · 충청타임즈(근정전 현장 AR) http://www.cctimes.kr/news/articleView.html?idxno=776914 · 투어코리아뉴스(군기시, 2023.02) http://www.tournews21.com/news/articleView.html?idxno=57574 · 이투데이(2021.07 제일기획 협약) https://m.etoday.co.kr/view.php?idxno=2041981 |

조선 신정왕후 조씨(효명세자 비)의 팔순을 축하한 1887년 궁중행사를 디지털로 복원하고, 경복궁 근정전 현장에서 모바일 앱으로 AR·XR로 재현한 실감콘텐츠다. 2023년 11월 22일 서비스를 시작했다. 궁중의례를 궁궐 현장에서 디지털로 복원한 것은 이때가 처음이라고 문화재청이 밝혔다. 유네스코 세계기록유산인 '정해진찬의궤' 등을 고증 근거로 삼아, 무형의 제례를 유형 공간 위에 얹는 방식이다. 이 프로젝트는 같은 컨소시엄의 단계적 계보에 속한다 — 2018년 돈의문(성문), 2023년 2월 군기시(관청, 140여 년 만의 디지털 복원), 그리고 경복궁(궁궐)으로 이어졌다. 조경의 관점에서는 건축물이 아니라 '의례가 벌어지던 외부 공간(근정전 조정)'을 대상으로 삼은 점이 눈에 띈다.

2023년 11월 서비스 개시. 국가유산진흥원은 2026년 1월 수상 기사에서 VR·AR·메타버스로 소실되거나 접근이 어려운 국가유산을 가상 복원하는 사업을 계속하고 있다고 밝혔다. 다만 '1887 경복궁 진하례' 앱의 현재 운영 여부와 누적 이용자 수는 확인하지 못했다

### LX한국국토정보공사 + 서울시 + 딥파인 — 광화문 일대 대규모 옥외 AR 지도 및 서울기록문화관 AR 체험
| 항목 | 내용 |
| --- | --- |
| 주체 | 서울특별시 + LX한국국토정보공사. 기술 공급: (주)딥파인(XR 공간정보 솔루션, DSC) |
| 시기·장소 | 대한민국 서울 중구 서울도서관(서울기록문화관) 및 종로구 광화문 광장 일대. 2023년 11월 27일~2024년 1월(약 2개월) |
| 증거 수준 | 시범사업 |
| 수치 | AR 지도 구현 면적 약 5만㎡(광화문 일대). 시범운영 기간 약 2개월. 사업비·이용자 수는 공개되지 않음 |
| 기술 | 서울시 3차원 공간정보·디지털트윈 기반, 딥파인 DSC(공간 정합/측위 기술), 위치 기반 AR. 단말: 스마트폰 + 스마트안경 |
| 출처 | 뉴시스(2023.11.20) https://n.news.naver.com/article/003/0012218434 · 보안뉴스 http://m.boannews.com/html/detail.html?idx=123928 · 파이낸셜뉴스(딥파인, 2개월 시범운영) https://n.news.naver.com/article/014/0005106482 · 중앙일보(AR 실내 측위 내비게이션) https://n.news.naver.com/article/025/0003324748 · AI타임스(5만㎡ AR 지도, 2025.05.28) https://www.aitimes.com/news/articleView.html?idxno=170838 · 뉴스핌(공간정보 민간제공 협약) http://m.newspim.com/news/ |

서울시의 디지털트윈 공간정보를 기반으로, 광화문 일대에 대규모 옥외 AR 지도 서비스와 AR 실내외 내비게이션을 구현한 실증 사업이다. 2023년 11월 20일 서울시가 '서울기록문화관 증강현실 체험 서비스'를 시범 운영한다고 발표했다. 서울도서관(구 시청사) 3층 서울기록문화관과 옛 시장실을 대상으로, 스마트폰이나 스마트안경을 통해 조선 육조거리를 AR로 보고 길 안내를 받는 방식이다. 사용자의 위치에 따라 가상 전시를 보여주는 위치 기반 AR로, 현장 전시와 가상 전시의 장점을 결합해 접근성을 높이려는 의도였다. XR 공간정보 솔루션 기업 딥파인이 자사 DSC 기술로 광화문 역사와 광장 일대 약 5만㎡ 규모의 AR 지도를 구현했다. 국내 공공 부문에서 확인되는 가장 큰 옥외 AR 정합 면적 사례다.

약 2개월 시범운영으로 종료. 정규 서비스 전환 여부를 확인하지 못했다. 딥파인은 이 사례를 2025년 5월 AI·빅데이터쇼에서 자사 XR 서비스의 물류·건설·관광 적용 레퍼런스로 계속 소개하고 있다 — 기업의 기술 실증 자산으로는 남았으나, 시민 서비스로 지속됐다는 근거는 없다. LX와 서울시는 2023년 3월 공개제한 공간정보의 민간 제공 협약을 별도로 맺어, VR·AR 기업의 지형·지물 데이터 수요에 대응하는 경로를 열었다

### 대구수목원 IoT 기반 현장 체험·교육용 VR·AR 콘텐츠
| 항목 | 내용 |
| --- | --- |
| 주체 | 대구광역시(주관) + 경북대학교 산학협력단·첨단정보통신융합산업기술원 + (주)바나나몬 + (주)리얼미디어웍스. 재원: 문화체육관광부 공모(국비) |
| 시기·장소 | 대한민국 대구광역시 대구수목원. 2017년 6월 공모 선정, 2017년 12월 22일 시범서비스 개시 |
| 증거 수준 | 실제 납품 |
| 수치 | 총 사업비 10억 원 규모(문체부 공모). 콘텐츠 종수·이용자 수는 공개되지 않음 |
| 기술 | IoT 센서 연계 + VR·AR 콘텐츠. 현장 체험·교육용. 구체적 AR 정합 방식(마커/위치 기반)은 보도자료에 명시되지 않음 |
| 출처 | 국제뉴스(2017.06 공모 선정, 10억 원) http://www.gukjenews.com/news/articleView.html?idxno=721177 · 세계일보(아마존 열대우림 체험) https://n.news.naver.com/article/022/0003182264 · 경상매일신문(2017.12.22 시범서비스 개시) http://www.ksmnews.co.kr/default/index_view_page.php?idx=194061 · 경북신문 http://www.kbsm.net/default/index_view_page.php?idx=194341 |

대구시가 4차 산업혁명 기술을 수목원에 접목한 사업이다. 2017년 6월 문화체육관광부 공모 'IoT 기반 현장 체험·교육용 VR·AR 콘텐츠 개발'에 최종 선정돼 총 10억 원 규모로 추진됐고, 2017년 12월 22일 콘텐츠 제작을 완료해 시범서비스를 개시했다. 대구수목원에서 보기 어려운 식물을 VR·AR 존에서 체험하게 하고, 아마존 열대우림 같은 다른 기후대의 식물 경관을 가상으로 보여주는 구성이었다. 대구시와 경북대학교 첨단정보통신융합산업기술원, 지역기업 (주)바나나몬·(주)리얼미디어웍스 등이 참여했다. 국내에서 수목원이라는 식물 전시 공간 자체를 대상으로 AR·VR을 제작한 초기 공공 사례다.

확인 실패. 2017년 12월 시범서비스 개시 이후의 운영 실적, 정규화, 종료 여부를 보여주는 자료를 찾지 못했다. 2018년 이후 이 사업에 관한 후속 보도가 사실상 없다는 점이 시사적이다. 참여 기업 (주)리얼미디어웍스의 이후 행적도 확인하지 못했다

### 현대건설·삼성물산·태영건설 — BIM 기반 시공 AR (조경 시공에 가장 근접한 국내 도구)
| 항목 | 내용 |
| --- | --- |
| 주체 | 현대건설(자체 개발) · 삼성물산 건설부문 + KCIM(XRlize) · 태영건설 + Trimble(SiteVision, 한국도로공사 현장) · ㈜한라 |
| 시기·장소 | 대한민국. 현대건설 택지개발 현장(2021.03), 터널 현장(2022.04); 삼성물산·KCIM XRlize 공개(2023.03); 태영건설 도로 현장(2024.05~06) |
| 증거 수준 | 실제 납품 |
| 수치 | 생산성·효율 향상 수치는 대부분 시공사 자체 주장이거나 사용자 인터뷰 수준이다('검측 생산성 향상', '효율성 크게 향상'). 정량적 수치를 제3자가 측정한 자료는 확인하지 못했다 |
| 기술 | Autodesk Revit 등 BIM 모델 → 경량화 → Microsoft HoloLens / HoloLens 2 / Trimble XR10(홀로렌즈2+안전모) / Trimble SiteVision(GNSS 기반 옥외 AR) / 태블릿. 기능: 객체 정보 조회, 길이 측정, 3D 모델 현장 중첩, 검측 |
| 출처 | SR타임스(현대건설, 2021.03.29) http://m.srtimes.kr/news/articleView.html?idxno=89867 · 정보통신신문 http://www.koit.co.kr/news/articleView.html?idxno=81580 · 대한경제(삼성물산·KCIM XRlize) https://m.dnews.co.kr/m_home/view.jsp?idxno=202303221229316470676 · 대한경제(트림블 사이트비전·㈜한라) https://m.dnews.co.kr/m_home/view.jsp?idxno=202110071658345540609 · 국민일보(태영건설 사이트비전, 2024) https://n.news.naver.com/article/005/0001699187 · 뉴스웨 |

조경 전용은 아니지만, 국내에서 '설계 도면을 현장 실물 위에 겹쳐 본다'는 AR을 실제로 돌리는 곳은 건설 시공 현장이다. 현대건설은 2021년 3월 시공 품질관리와 검측 생산성을 위해 BIM 기반 'AR 품질관리 플랫폼'을 자체 개발했다고 발표했다. BIM 데이터를 최적화해 마이크로소프트 홀로렌즈와 태블릿PC에서 쓸 수 있는 애플리케이션을 함께 만들었고, 객체 정보 확인·길이 측정·3D 모델 중첩 기능을 넣어 택지개발 현장에 적용했다. 2022년에는 터널 현장에서 TVWS 무선통신과 홀로렌즈를 연계한 품질관리 업무에 썼다. 삼성물산 건설부문은 KCIM과 홀로렌즈2 기반 'XRlize'를 공동 개발해 Autodesk Revit 모델을 현장에서 XR로 보게 했다(2023년 공개). 태영건설은 Trimble SiteVision을 도로 건설 현장(한국도로공사 양평 사업 등)에 적용해 완성될 도로를 AR로 미리 보여줬다(2024년). ㈜한라도 2021년 Trimble SiteVision을 BIM 활용 도구로 도입했다.

각 사에서 계속 사용 중으로 보도된다. 조경 분야로 넘어온 흔적은 아직 구상 단계다 — 환경과조경의 2026년 아파트 조경 기획 인터뷰에서 대우건설 실무자들은 "시공자가 증강현실 장비를 쓰면 눈앞 실제 공간 위에 3D 도면의 완성선이 겹쳐 보이고, 경계석 위치나 레벨, 수목 규격도 현장에서 확인할 수 있다"고 말했으나, 이는 입체설계의 전망으로 제시된 것이고 실제 조경 현장 적용 사례로 보도된 것은 아니다

### '메타버스 서울' 종료 — 공공 실감기술 사업 실패의 교본
| 항목 | 내용 |
| --- | --- |
| 주체 | 서울특별시 |
| 시기·장소 | 대한민국 서울특별시. 2023년 1월 16일 개시, 2024년 10월 16일 종료 |
| 증거 수준 | 실제 납품 |
| 수치 | 투입 예산 55억~60억 원(보도에 따라 상이). 1년 9개월간 120채팅민원상담 이용 445건. 민원서류 발급·민원 상담 하루 평균 1건 미만. 청소년 상담은 거의 없음(국회 행정안전위원회 양부남 의원 분석, 2024년 국정감사) |
| 기술 | 아바타 기반 3D 가상공간 플랫폼(모바일 앱). AR 아님 |
| 출처 | 디스이즈게임(2024.07.02, 55억·종료 일정) https://m.sports.naver.com/esports/article/439/0000028934 · JTBC(60억·이용률) https://n.news.naver.com/article/437/0000399767 · 더팩트(2024 국감, 445건·일평균 1건 미만) https://n.news.naver.com/article/629/0000332352 · 세계일보 https://n.news.naver.com/article/022/0003980349 · 시사오늘(국내 메타버스 종료 연표) http://www.sisaon.co.kr/news/articleView.html?idxno=181791 |

AR이 아니라 VR·메타버스 사업이지만, 국내 공공 공간 실감콘텐츠의 사업성 판단 기준을 결정적으로 바꾼 사건이므로 함께 기록한다. 서울시는 세계 도시 최초의 공공 메타버스 플랫폼을 구축했다고 홍보하며 2023년 1월 16일 서비스를 시작했다. 민원 상담을 가상공간에서 하고 주민등록등·초본 같은 서류도 발급할 수 있다고 했다. 2024년 7월 서비스 중단 공고를 내고 같은 해 10월 16일 종료했다. 서비스 기간은 1년 9개월이었다. 종료 이유는 기술 실패가 아니라 이용률이었다 — 예산 대비 이용자 수가 적다는 지적이 서울시의회에서 나왔고 대안을 찾지 못했다.

2024년 10월 16일 종료. 국회 국정감사에서 '혈세 낭비'로 지적됐다. 같은 흐름에서 SK텔레콤 '이프랜드'(2024 종료), 카카오 계열 '컬러버스'(파산 절차), KT '메타라운지'·'지니버스'(각 출시 약 1년 만에 종료)가 줄줄이 접혔다. 전용 앱 설치와 아바타 공간이라는 형식 자체가 공공 서비스에서 작동하지 않았다는 판정이고, 이 학습이 2026년 서울국제정원박람회의 '앱 설치 없는 QR 기반 AR' 선택 배경에 있다(인과관계는 서울시가 명시한 바 없으므로 추정)

### '디지털 공원법' 개정안 발의 (2026.03) — AR을 공원에 쓸 법적 근거가 없었다는 증거
| 항목 | 내용 |
| --- | --- |
| 주체 | 김미애 의원(국민의힘, 부산 해운대을) 대표 발의 |
| 시기·장소 | 대한민국 국회. 2026년 3월 16일 발의 보도 |
| 증거 수준 | 입법 발의 (제도적 조건) |
| 수치 | 조문 수·적용 대상 공원 규모 등 구체 수치는 보도에서 확인되지 않음 |
| 기술 | 해당 없음(제도). 대상 기술로 AR·VR·미디어아트 명시 |
| 출처 | 뉴스핌(2026.03.16) https://m.newspim.com/news/view/20260316000502 · 핀포인트뉴스(2026.03.17) https://www.pinpointnews.co.kr/news/articleView.html?idxno=437229 |

김미애 국민의힘 의원(부산 해운대을)이 2026년 3월 도시공원에 증강현실(AR)·가상현실(VR)·미디어아트 등 디지털 기술을 활용할 수 있는 제도적 기반을 마련하는 법 개정안을 대표 발의했다. 발의 배경으로 제시된 문제 인식이 중요하다 — 대규모 도시공원과 수목원에서 청소년·가족 단위 체류형 콘텐츠가 부족하고, 야간 활용의 제도적 근거가 미비하며, 고령자·장애인의 정보 접근성에 한계가 있다는 것이다. 즉 그동안 한국의 도시공원에 AR을 상설로 넣기 어려웠던 이유 중 하나가 기술이나 예산이 아니라 근거 법령의 부재였음을 입법부가 공식 확인한 셈이다. 국내 조경·공원 분야 AR 사례가 대부분 축제·박람회 같은 한시적 행사에 붙어 있었던 현상과 정확히 맞물린다.

발의 단계. 2026년 9월 30일 기준 통과·시행 여부를 확인하지 못했다. 이 항목은 '한국의 조경 AR이 왜 행사성 체험에 머물렀는가'를 설명하는 제도적 배경 자료로 쓸 수 있다

### 지역 정원·공원 행사의 AR 체험 확산 (영월·거창·울산·과천)
| 항목 | 내용 |
| --- | --- |
| 주체 | 영월군 · 거창군 · 울산광역시(남구) · 과천시. 콘텐츠 제작사는 대부분 공개되지 않음(과천은 '스펀지 AR' 앱 사용) |
| 시기·장소 | 대한민국 — 강원 영월(2026.10.02~11) · 경남 거창 창포원(2026.10.02~06) · 울산 태화강국가정원(2026.10.17, 선행 2019.10) · 경기 과천 중앙공원(2026.06~) |
| 증거 수준 | 실제 납품(단, 모두 한시적 행사 콘텐츠) |
| 수치 | 과천 AR 포토존은 시 승격 40주년 기념. 태화강 국가정원 선포식(2019.10) 3일간 32만 명 방문(AR은 부대 체험 중 하나). 각 AR 프로그램 자체의 예산·참여자 수는 공개되지 않음 |
| 기술 | 스마트폰 앱 또는 QR 진입, GPS 기반 보물찾기형 AR, AR 포토존. 정밀 측위 사용 흔적 없음 |
| 출처 | 프레시안(영월) https://n.news.naver.com/article/002/0002456732 · 브레이크뉴스(영월) http://m.breaknews.com/1236607 · 아시아경제(거창) https://n.news.naver.com/article/277/0005822344 · 동아일보(울산 태화강국가정원) https://n.news.naver.com/article/020/0003751628 · CNB뉴스(울산 '보물 찾고') https://www.cnbnews.com/news/articleView.html?idxno=1017462 · 울산매일신문(2019 선포식 32만 명) http://m.iusm.co.kr/news/articleView.html?idxno=858904 · 문화일보(과천) h |

2026년 들어 조경·정원 관련 지역 행사에 AR 체험이 반복적으로 붙는 패턴이 나타난다. 영월군은 2026년 10월 2~11일 '2026 대한민국 영월 정원산업박람회'에서 AR 기반 체험 프로그램을 처음 선보였다 — 관람객이 스마트폰을 들고 박람회장을 이동하며 버섯도깨비 찾기, 꿀 모으기, 퍼즐 맞추기 임무를 수행하는 방식이고, 야간 미디어아트를 함께 강화했다. 거창군은 2026년 10월 2~6일 창포원에서 '2026 대한민국 거창 정원 치유박람회'를 열며 스마트폰 AR을 활용한 정원 체험을 주요 프로그램에 넣었다. 울산시는 2026년 10월 17일 태화강국가정원 남구 둔치에서 '보물 찾고(go)' 앱으로 국가정원에 숨겨진 보물을 찾는 AR 게임 중심의 '울산 피크닉 페스티벌'을 열었다(태화강 국가정원 선포식에서도 2019년 AR 체험이 운영된 이력이 있다). 과천시는 2026년 6월 시 승격 40주년을 맞아 중앙공원 양재천 입구에 QR + '스펀지 AR' 앱 기반 AR 포토존을 조성했다. 공통점은 한시적이고, 게임·포토존 형식이며, 조경 공간을 콘텐츠의 배경으로만 쓴다는 것이다.

행사 기간 한정 운영. 종료 후 상설화 사례를 찾지 못했다. 이 패턴은 앞의 '디지털 공원법' 항목과 함께 읽어야 한다 — 상설 근거가 없으니 행사 예산으로 붙였다가 걷는 구조가 반복된다

## vegetation
항목 14개 · 검증 정정 지적 0건

> 식생 AR은 두 갈래로 갈라져 있고 그 사이가 비어 있다. 한쪽은 측정이다. 스웨덴 우메오의 Arboreal은 아이폰 LiDAR와 AR로 표본조사구를 재는 앱을 2020년부터 판다. 직경 sub-cm 정확도는 2023년 Forests 비교연구와 2024년 학술논문으로 독립 검증됐다. Katam은 숲을 걸으며 찍은 영상에서 단목 직경·높이·밀도를 뽑아 칠레 CMPC, 브라질 Irani에 납품한다. 이 계열은 실재하고, 팔리고, 검증됐다. 다른 한쪽은 에셋이다. SpeedTree(2021년 Unity 인수)는 절차적 생성·바람 셰이더·계절 파라미터·LOD를 표준화했지만 제품이 명시하는 산업은 게임과 영화뿐, AR도 조경도 없다. Laubwerk는 2025년 1월 Maxon에 흡수돼 범용 CG 스택으로 들어갔다.  비어 있는 가운데가 조경이다. 설계한 식재를 현장에 정합해 보여준 사례는 발주처·연도를 특정할 수 있는 형태로 이번 조사에서 하나도 확인되지 않았다. 야외 고정밀 AR인 Trimble SiteVision은 수평 1cm를 내지만 공식 용도에 식생이 없고, 그 정확도는 개방된 하늘을 전제한다. 수관 아래 GNSS 음영은 조경 현장의 상수다. 도시숲 데이터를 가장 많이 가진 TreePlotter에는 AR 모듈이 없다. 조경 전용 BIM인 Vectorworks Landmark는 AR/VR을 홍보 문구로 걸지만, AR 뷰잉이 식물 객체의 수령·계절과 연결된다는 서술은 없다. 소비자 앱 iScape는 400만 다운로드에 정적 식물 에셋뿐이다.  가림 처리는 플랫폼이 아직 문제로 정의조차 하지 않았다. ARCore Depth API 문서는 depth-from-motion으로 0.5~5m가 정확하고 저텍스처 면에서 부정확하다고만 적는다. 잎·얇은 구조·투명·운동에 대한 지침은 없다. arXiv 초록에서 "augmented reality"와 occlusion, foliage를 함께 담은 논문은 0건이다.  움직임은 이제 막 열렸다. TreeDGS(항공 GS로 DBH), Sapling-NeRF(옥스퍼드, 유묘 지오로컬 복원), ChronoFuseGS(TU Wien VR/AR 그룹, 계절 변화 다중시점 융합), Wind on Trees(물리 파라미터 4D GS로 바람 흔들림)가 2024~2026년에 나왔다. Tree-D Fusion은 사진 한 장에서 시뮬레이션 준비된 수목 60만 개를 만들었다. 모두 연구 단계이고 현장 AR 배포는 없다.


### Arboreal Forest / Arboreal Tree / Arboreal Tree Scanner
| 항목 | 내용 |
| --- | --- |
| 주체 | Arboreal AB (스웨덴 우메오) |
| 시기·장소 | 스웨덴 우메오 본사. LiDAR 버전 2020년 출시, 현재 판매 중. 사용자 후기는 스웨덴·루마니아·브라질 |
| 증거 수준 | 실제 납품 |
| 수치 | 업체 주장: sub-cm 정확도, 대부분 편차 2cm 이내, 자체 평가 직경 MAE 3.9%·bias 0.67%, 재래식 대비 2.5배 빠름. 독립 검증: 2020년 스웨덴 농업과학대(SLU) Lina Lindberg 석사논문, 2021년 Sveaskog 평가, 2023년 Forests 저널 비교연구(경쟁 앱보다 우수), 2024년 학술논문(직경 sub-cm 확인) |
| 기술 | iOS ARKit + iPhone/iPad LiDAR 센서. 구독제(주/월). 엔터프라이즈는 REST-API 제공 |
| 출처 | https://www.arboreal.se/en/home , https://www.arboreal.se/en/arboreal-forest (2026-09-30 확인) |

스마트폰으로 수목과 임분을 재는 앱 3종이다. Arboreal Forest는 LiDAR와 AR 기술로 표본조사구 데이터를 수집해 직경·흉고단면적·ha당 본수·재적·수고·수종을 낸다. Arboreal Tree는 폰만으로 수고와 수관폭을 잰다. Arboreal Tree Scanner는 폰 LiDAR로 개별 통나무·수목을 정밀 스캔한다. 참조봉이나 별도 기구가 필요 없다는 것이 판매 논점이다. 조경이 아니라 임업 계측 시장을 겨냥했지만, 식생을 AR로 다룬 상용 제품 중 독립 검증이 가장 두터운 사례다.

계속 판매·사용 중. 업체 주장과 독립 검증이 분리 가능한 드문 경우. 다만 조경 설계용 식재 시각화가 아니라 계측 도구다

### Katam Forest (스마트폰·드론 산림 계측)
| 항목 | 내용 |
| --- | --- |
| 주체 | Katam Technologies AB (스웨덴) |
| 시기·장소 | 스웨덴. 고객 사례는 칠레·브라질·스웨덴, 2024년 기사 및 인도네시아 진출 언급 |
| 증거 수준 | 실제 납품 |
| 수치 | 고객: CMPC(칠레), Irani(브라질), Plockhugget(스웨덴). 인도네시아 총 산림 9천만 ha 언급. 정확도 수치는 공개하지 않음 |
| 기술 | 스마트폰 동영상 기반 재구성(SLAM/포토그래메트리 계열로 추정, 페이지에 명시 없음) + 드론 사진측량 |
| 출처 | https://www.katam.se/ (2026-09-30 확인) |

나무 사이를 걷거나 차로 지나가며 폰으로 촬영하면 개별 수목의 높이·직경·밀도와 단목 GPS 좌표를 산출한다. 드론이 자율 비행으로 상부에서 촬영하는 경로도 병행한다. 목표는 데이터 기반 간벌로 생장을 늘리는 것이다. 질병 식별용 고정밀 시각화도 내세운다. 제품 페이지는 AR이라는 말을 쓰지 않는다. 즉 카메라로 공간을 재구성하는 기술은 AR과 같은 계열이되, 출력은 현장 오버레이가 아니라 지도·수치다.

운영 중. 정확도 독립 검증은 확인하지 못했다. Arboreal과 달리 검증 논문을 스스로 내걸지 않는다는 차이가 있다

### SpeedTree (Unity)
| 항목 | 내용 |
| --- | --- |
| 주체 | IDV Inc.(2002~) 개발, 2021년 7월 Unity Technologies 인수 |
| 시기·장소 | 미국. 2002년부터 현재까지 |
| 증거 수준 | 실제 납품 |
| 수치 | Indie $19/월(매출 10만$ 미만), Pro $899/년(100만$ 미만), 라이브러리 애드온 $999/년, Enterprise 별도. 30일 무료 체험(내보내기 제한) |
| 기술 | 절차적 생성, 바람 셰이더, 계절 파라미터, 동적 LOD, Runtime SDK(PC·콘솔·모바일·VR) |
| 출처 | https://unity.com/products/speedtree (2026-09-30 확인, speedtree.com 301 리다이렉트로 소유권 확인) |

절차적 수목 생성 툴킷의 업계 표준이다. 절차적 생성기와 수작업 편집을 비파괴로 섞고, 물리 기반 덩굴, 셰이더·버텍스컬러 기반 바람 애니메이션, 계절 조정, 동적 LOD 생성, 8K PBR 텍스처 라이브러리를 제공한다. Runtime SDK는 PC·콘솔·모바일·VR을 지원한다고 적혀 있다. 그런데 제품 페이지가 명시하는 산업은 게임과 영화뿐이고 AR/XR, 건축, 조경 시각화 언급이 없다. 조경 실무가 쓰려면 Unity나 Unreal을 경유해야 하며, 좌표계·측량 정합은 SpeedTree 바깥의 문제로 남는다. 즉 바람과 계절을 가장 잘 다루는 도구가 조경 AR을 겨냥하지 않는다.

계속 쓰임. speedtree.com은 unity.com/products/speedtree로 301 리다이렉트된다. 독립 회사에서 엔진 벤더 산하 자산으로 편입

### Laubwerk 식물 에셋 라이브러리 → Maxon 인수
| 항목 | 내용 |
| --- | --- |
| 주체 | Laubwerk GmbH(독일) → Maxon |
| 시기·장소 | 독일. 2025년 1월 6일 인수 발표 |
| 증거 수준 | 실제 납품 |
| 수치 | 100개국 이상 고객(업체 주장). 종 수는 발표문에 없음 |
| 기술 | 정적 3D 식물 메시 + PBR 텍스처, 호스트 플러그인 방식 |
| 출처 | https://www.maxon.net/article/maxon-welcomes-laubwerk-to-their-expanding-family-of-innovative-tools (2026-09-30 확인) |

건축·VFX·3D 디자인용 사실적 3D 식물 모델을 팔던 회사다. 최소 작업으로 최대 디테일과 제어를 준다는 노선이었고, 100개국 이상에 고객이 있었다. 인수 후 Redshift-ready 나무·식물로 Cinema 4D Asset Browser에 편입되어 Maxon One 구독자에게 제공된다. 계절 변형과 수령 변형 옵션은 인수 발표문에 명시되지 않았다(구제품 문서는 이번에 확인하지 못함). 조경 관점의 의미는 식물 에셋이 범용 CG 스택 안으로 들어가면서 수령·규격·식재기준 같은 조경 고유 속성과 더 멀어졌다는 것이다.

독립 회사로서는 종료. 제품은 구독 번들로 흡수. 조경 전용화가 아니라 범용화 방향으로 귀결

### Trimble SiteVision
| 항목 | 내용 |
| --- | --- |
| 주체 | Trimble Inc. |
| 시기·장소 | 미국 본사, 전 세계 판매. 인용 사례는 Skanska 영국(수석측량기사 Mark Lawton) |
| 증거 수준 | 실제 납품 |
| 수치 | 수평 1cm, 수직 2cm (실시간 키네매틱) |
| 기술 | GNSS RTK(Catalyst DA2) + 카메라 AR + 라이다 스캔. 옵션 Trimble HPS2, TDC6 |
| 출처 | https://geospatial.trimble.com/en/products/software/trimble-sitevision (2026-09-30 확인) |

야외 현장용 AR과 라이다 스캔, GNSS 측위를 결합한 현장 시각화·현실캡처 소프트웨어다. Trimble Catalyst DA2 GNSS 수신기를 Android/iOS 기기에 붙여 폴 또는 핸들 마운트로 쓴다. 용도는 지하 매설물 시각화, 설계 검증, 준공 기록, 측량, 교통·주거 개발이다. 제품이 공식으로 내세우는 용도 목록에 조경과 식생이 없다. 조경에 중요한 사실은 이 1cm급 정확도가 개방된 하늘을 전제한다는 점이다. 수관 아래 GNSS 음영은 조경 현장의 상수이므로, 야외 AR에서 가장 정확한 제품조차 나무 밑에서는 전제가 무너진다.

판매 중. 조경·식생 사례는 확인하지 못했다. 수관 아래 성능 저하는 GNSS 물리상 필연이지만 Trimble 문서로 직접 확인하지 못했다

### iScape (조경 디자인 AR 앱)
| 항목 | 내용 |
| --- | --- |
| 주체 | iScape (iOS/Android 앱 개발사) |
| 시기·장소 | 미국 기반. 출시 연도는 페이지에 없음. 현재 App Store·Google Play 판매 중 |
| 증거 수준 | 실제 납품 |
| 수치 | 약 400만 다운로드, 평점 4.6(업체 주장). Free 제한판, Pro $29.99/월 또는 $299.99/년, Enterprise 별도 |
| 기술 | iOS/Android AR(프레임워크 미명시), 사진 기반 합성 + AR 배치, 2D 이미지와 3D 모델 혼용 |
| 출처 | https://www.iscapeit.com/ (2026-09-30 확인) |

마당이나 현장 사진 위에 2D 또는 3D 증강현실 디자인을 올리는 조경 디자인 앱이다. 수천 종의 식물, 포장재, 가구, 하드스케이프 요소를 사실적 디테일로 제공한다고 주장한다. 홈오너·취미가와 조경업자 양쪽을 고객으로 잡는다. 식물은 정적 에셋이고 생장이나 계절 변화 기능은 페이지에 언급되지 않는다. 정합도 사진 합성 또는 평면 인식 수준으로 보이며 측량 좌표와의 연결은 없다. 즉 조경 AR 중 가장 많이 팔린 제품이 식생의 시간성을 전혀 다루지 않는다.

계속 판매 중. 다운로드 수는 업체 주장이며 독립 검증 없음

### Vectorworks Landmark + Cloud Services(Nomad) AR 뷰잉
| 항목 | 내용 |
| --- | --- |
| 주체 | Vectorworks, Inc. (Nemetschek 그룹) |
| 시기·장소 | 미국. AR 기능 도입 연도는 이번 조사에서 확인 못함 |
| 증거 수준 | 실제 납품 |
| 수치 | 없음(페이지에 수치 없음) |
| 기술 | 클라우드 렌더링 + 모바일 AR 뷰어(기기 요건 미명시). VR은 별도 Quest 앱 |
| 출처 | https://www.vectorworks.net/landmark , https://www.vectorworks.net/cloud-services (2026-09-30 확인) |

Landmark는 조경 전용 BIM 제품이고, 제품 페이지가 AR/VR을 포인트클라우드·포토그래메트리와 함께 앞서가는 기술로 명시한다. 클라우드 서비스는 3D 모델의 AR 뷰잉을 제공해 클라이언트에게 몰입형 프레젠테이션을 준다고 적는다. VR은 Meta Quest용 Vectorworks Odyssey로 분리돼 있다. 문제는 AR 뷰잉이 Landmark의 식물 객체, 수령, 계절 표현과 연결된다는 서술이 어디에도 없다는 점이다. 즉 조경 전용 BIM에서도 AR은 범용 모델 뷰어이고, 식생 특수성은 AR 경로에 반영되지 않았다.

기능 제공 중. 다만 조경 전용 BIM 벤더의 몰입형 투자 중심이 현장 AR보다 헤드셋 VR로 기울어 있다

### Tangible Landscape (투영식 공간증강 + 숲 심기)
| 항목 | 내용 |
| --- | --- |
| 주체 | NCSU GeoForAll Lab, 노스캐롤라이나주립대학교 |
| 시기·장소 | 미국 노스캐롤라이나. 사이트 저작권 표기 2016년, 이후 유지 상태 미확인 |
| 증거 수준 | 연구 프로토타입 |
| 수치 | 없음(설치 수·워크숍 수는 페이지에 없음) |
| 기술 | 실시간 3D 스캐너 + 프로젝터 + GRASS GIS + Blender. 오픈소스 |
| 출처 | https://tangible-landscape.github.io/ (2026-09-30 확인) |

물리 모형을 손으로 조형하면 실시간 3D 스캔과 포인트클라우드 처리를 거쳐 GRASS GIS가 지리연산을 수행하고, 그 결과를 프로젝터가 모형 위에 투영하며 Blender가 3D 렌더를 띄운다. 핵심은 색 펠트 조각을 모형에 놓으면 그 자리에 숲이 심어지고 즉시 3D 나무로 렌더링된다는 점이다. 객체 인식, 시계열 분석, 협업 상호작용도 지원한다. 오픈소스이고 초심자와 전문가 모두를 겨냥한다. 식생을 증강현실로 다룬 드문 실제 구현이지만, 현장 정합형 모바일 AR이 아니라 실내 테이블 위 투영식 공간증강이다. 조경의 손 작업과 연산 모델을 잇는 방식으로는 지금도 가장 구체적인 사례다.

오픈소스로 공개돼 교육·워크숍에 쓰였다. 사이트 저작권이 2016년에 멈춰 있어 활발한 유지 여부는 확인하지 못했다

### Tree-D Fusion (단일 사진 → 시뮬레이션 준비 수목 60만 개)
| 항목 | 내용 |
| --- | --- |
| 주체 | Jae Joong Lee, Bosheng Li, Sara Beery(MIT), Jonathan Huang, Songlin Fei(Purdue), Raymond A. Yeh, Bedrich Benes(Purdue) |
| 시기·장소 | 미국. arXiv 2024년 7월 14일 |
| 증거 수준 | 연구 프로토타입 |
| 수치 | 수목 모델 60만 개 |
| 기술 | 디퓨전 프라이어 기반 단일 이미지 3D 복원 + 절차적 분지 구조 추정. 데이터 소스는 구글 스트리트뷰 계열 Auto Arborist |
| 출처 | arXiv:2024-07-14 "Tree-D Fusion: Simulation-Ready Tree Dataset from Single Images with Diffusion Priors" (arXiv API로 2026-09-30 확인) |

단일 이미지에서 디퓨전 프라이어로 3D 수목을 복원해 시뮬레이션 준비된 수목 모델 60만 개 데이터셋을 만들었다. 대상 이미지는 구글의 Auto Arborist Dataset이다. 속(genus)을 지시하는 텍스트 프롬프트로 형상을 복원하고, 3D 수관 외피와 포인트 마커를 생성해 분지 구조를 추정한다. 절차적 생성(SpeedTree)과 실측 기반(LiDAR·포토그래메트리) 사이의 제3경로다. simulation-ready라는 표현은 생장·바람 시뮬레이션에 투입할 수 있는 형태라는 뜻이다. 도시 수목 디지털트윈의 자산 문제를 규모로 푸는 첫 시도이고, 조경 AR이 쓸 수 있는 식생 자산의 공급 경로가 될 수 있다.

연구 데이터셋으로 공개. AR 현장 배포 사례는 확인하지 못했다

### Scaniverse → Niantic Spatial (온디바이스 3D Gaussian Splatting)
| 항목 | 내용 |
| --- | --- |
| 주체 | Niantic Spatial, Inc. |
| 시기·장소 | 미국. 소비자 3D 스캔 앱에서 기업용 공간 데이터 서비스로 재편(시점은 페이지에 명시 없음) |
| 증거 수준 | 실제 납품 |
| 수치 | SPZ 포맷 파일 크기 90% 절감(업체 주장). VPS는 5천만 개 신경망·150조 파라미터 규모라 주장. 가격은 플랜별 비공개 |
| 기술 | 온디바이스 3D Gaussian Splatting + 메시. SPZ·USDZ 내보내기. VPS(Visual Positioning System) 기반 GPS 비의존 측위 |
| 출처 | https://www.nianticspatial.com/ , https://www.nianticspatial.com/products/capture (2026-09-30 확인, scaniverse.com 302 리다이렉트) |

시장을 선도했던 모바일 3D 스캔 앱이 확장 가능한 공간 데이터 수집 서비스로 바뀌었다. iOS·Android 기기, 360 카메라, 드론, 그리고 조직 자체의 이미지·라이다·센서 데이터를 받는 BYOD 경로를 지원한다. Gaussian Splat과 메시를 기기 위에서 처리하고, 자체 오픈소스 포맷 SPZ(파일 크기 90% 절감)와 USDZ로 내보낸다. Capture·Reconstruct·Localize·Understand 네 기능을 묶어 디지털트윈을 만든다고 설명한다. 조경에 중요한 대목은 타깃 시장이다. embodied AI·로보틱스, 국방·정보, 석유가스로 명시돼 있고 소비자와 설계 실무는 전면에서 사라졌다. 잎처럼 얇은 구조를 잘 담는 스플랫 캡처가 폰에서 무료로 가능해진 바로 그 시점에, 공급자는 조경이 아닌 곳을 보고 있다.

제품은 유지되나 사업 방향이 전환됐다. scaniverse.com이 nianticspatial.com/products/capture로 리다이렉트된다. 소비자·설계 시장 경로는 사실상 접혔다(경제적 이유: 화면 밖 경제활동 80%를 겨냥한다는 자체 서술)

### 식생 3DGS 재구성 연구군 (TreeDGS, Sapling-NeRF, 임분 비교연구, WildFireGS)
| 항목 | 내용 |
| --- | --- |
| 주체 | TreeDGS: Belal Shaheen 등(James Tompkin 그룹 포함) / Sapling-NeRF: Miguel Ángel Muñoz-Bañón, Nived Chebrolu, Maurice Fallon 등(옥스퍼드) / 비교연구: Guoji Tian, Chongcheng Chen, Hongyu Huang / WildFireGS: Nienke Driessen, Sören Pirk, Dominik L. Michels, Michael Weinmann 등 |
| 시기·장소 | 2024년 10월 ~ 2026년 8월. 영국·중국·네덜란드·독일·사우디 등 |
| 증거 수준 | 연구 프로토타입 |
| 수치 | 개별 수치는 논문별. 공통 벤치마크나 조경 설계 대상 검증은 없음 |
| 기술 | 3D Gaussian Splatting, NeRF, 항공·UAV·지상 촬영, 의미분할 결합 |
| 출처 | arXiv API 검색(abs:"Gaussian splatting" AND abs:forest, 2026-09-30 확인): TreeDGS 2026-01-19, Sapling-NeRF 2026-02-26, Tian 등 2024-10-08, WildFireGS 2026-08-11 |

3D Gaussian Splatting이 식생에 유리하다는 실증이 쌓이는 중이다. TreeDGS(2026-01-19)는 항공 영상 GS 재구성으로 원거리 흉고직경(DBH)을 측정한다. Sapling-NeRF(2026-02-26)는 개별 유묘를 지오로컬라이즈해 복원하고 산림 갱신과 수목 구조 형질을 모니터링한다. Tian 등(2024-10-08)은 복잡한 산림 임분 재구성에서 신규시점합성(GS·NeRF)과 포토그래메트리를 비교하고 수목 측정값을 추출한다. WildFireGS(2026-08-11)는 의미정보를 부여한 GS 산림 장면에 물리 기반 연소 모델을 붙여 산불 전파를 시뮬레이션한다. 잎과 가지 같은 얇은 구조에서 스플랫이 메시보다 유리하다는 것이 공통 전제다. 그러나 목적은 산림계측·로봇·재난이고, 조경 설계의 현장 AR은 하나도 없다.

모두 연구 단계. 제품화나 현장 AR 배포는 확인되지 않았다

### 시간축과 바람: ChronoFuseGS, Wind on Trees (4D Gaussian Splatting)
| 항목 | 내용 |
| --- | --- |
| 주체 | ChronoFuseGS: Tobias Batik, Diana Marin, Peter Kán, Hannes Kaufmann(TU Wien) / Wind on Trees: Weiying Chen, Edmond Lou |
| 시기·장소 | 오스트리아 빈 및 미상. 각각 2026년 9월 25일, 2026년 9월 15일 arXiv |
| 증거 수준 | 연구 프로토타입 |
| 수치 | 없음(정량 비교는 논문 내부 지표) |
| 기술 | 다중시점 Gaussian 융합(splat별 persistence), 물리 파라미터화 변형장 기반 4D GS, 비디오 디퓨전 기반 앰비언트 모션 |
| 출처 | arXiv API 검색(abs:"Gaussian splatting" AND abs:vegetation, 2026-09-30 확인): ChronoFuseGS 2026-09-25, Wind on Trees 2026-09-15, AniGS 2026-07-20 |

조경의 두 고유 문제가 이제야 연구 대상이 됐다. ChronoFuseGS는 서로 다른 시점에 촬영한 여러 Gaussian 모델을 splat 단위 persistence로 융합해 야외 장면의 계절 식생 변화를 추적하고 변화를 시각화한다. 저자 그룹이 TU Wien의 VR/AR 연구실(Kaufmann)이라는 점이 조경 AR과의 직접 접점이다. Wind on Trees는 학습된 모션이 아니라 물리 파라미터화된 변형장으로 바람에 흔들리는 수목 운동을 모델링하고 4D GS의 물리적 타당성을 검증한다. 관련 흐름으로 AniGS(2026-07-20)는 비디오 디퓨전으로 정적 재구성에 식생 미세 운동을 덧붙인다. 다만 어느 것도 실시간 AR 렌더링 부하나 현장 정합을 다루지 않는다. 즉 자라고 흔들리는 것을 스플랫으로 담는 길은 열렸지만, 그것을 현장에 겹쳐 놓는 문제는 아직 손대지 않았다.

연구 단계. 2026년 9월 프리프린트로 가장 최신 흐름. 제품 없음

### ARCore Depth API — 수관 가림 처리의 플랫폼 공백
| 항목 | 내용 |
| --- | --- |
| 주체 | Google |
| 시기·장소 | 전 세계 Android. Depth API 2020년 공개, 문서는 2026-09 기준 |
| 증거 수준 | 실제 납품 |
| 수치 | 깊이 범위 0~65m, 정확 구간 0.5~5m. 보강 정황: arXiv 초록에 "augmented reality"와 occlusion, foliage를 함께 담은 논문 0건(2026-09-30 검색) |
| 기술 | depth-from-motion 다중프레임 스테레오 + ToF 센서 융합(있을 경우) |
| 출처 | https://developers.google.com/ar/develop/depth (2026-09-30 확인) + arXiv API 검색 결과 0건 |

AR 가림(occlusion)을 담당하는 표준 플랫폼 기능이다. 서로 다른 각도의 여러 프레임을 비교하는 depth-from-motion으로 깊이 영상을 만들고, ToF 같은 전용 센서가 있으면 자동으로 병합한다. 측정 범위는 0~65m이며 가장 정확한 구간은 기기에서 0.5~5m다. 알고리즘이 운동에 의존하므로 사용자가 기기를 움직인 뒤에야 유효 깊이가 생긴다. 흰 벽처럼 특징 없는 저텍스처 면은 깊이가 부정확하다고 명시한다. 지원 기기가 제한되고 수동 활성화가 필요하다. 정작 조경이 필요한 것 — 잎처럼 얇은 구조, 흔들리는 물체, 반투명 수관, 야외 강광 조건 — 에 대한 지침은 문서에 없다. 수관 투과와 잎 사이 가림은 플랫폼이 해결하지 못한 문제가 아니라, 아직 문제로 정의되지도 않은 상태다.

플랫폼 기능으로 계속 제공. 식생 특수 조건에 대한 공식 대응은 없음. arXiv 0건은 검색 범위 한계가 있으나 공백의 정황 증거로 쓸 수 있다

### TreePlotter (PlanIT Geo) — 도시숲 데이터의 AR 부재
| 항목 | 내용 |
| --- | --- |
| 주체 | PlanIT Geo, Inc. |
| 시기·장소 | 미국 본사, 영국 지사. 캐나다 진출 언급. 연도 미명시 |
| 증거 수준 | 실제 납품 |
| 수치 | 명시 고객: ClimbingHI Maui, Texas Trees Foundation, Canopy Palo Alto. 데이터 규모·도시 수는 페이지에 없음 |
| 기술 | 웹·모바일 GIS SaaS. AR 없음 |
| 출처 | https://www.planitgeo.com/treeplotter/ (2026-09-30 확인) |

도시숲 수목 인벤토리와 수관 분석의 사실상 표준 SaaS다. TreePlotter INVENTORY는 어떤 기기에서든 실시간으로 데이터를 수집·관리하고, CANOPY는 도시숲을 보고 계획하고 키우는 분석 도구를 제공한다. Mobile, Projects, 커스터마이징, NatureScore 애드온이 붙는다. 정부·민간·비영리 고객을 세계적으로 보유한다고 주장한다. 그런데 제품 페이지 전체에 증강현실 언급이 하나도 없다. 조경에서 수목의 위치·수종·규격 데이터를 가장 많이 쥔 업계가, 그 데이터를 현장 AR로 내보내는 경로를 제품화하지 않았다는 뜻이다. 수요가 없다고 봤는지, 현장 정합 정확도를 낼 수 없다고 봤는지는 알 수 없다.

성장 중(캐나다 진출, 영국 지사). AR은 제품 로드맵에 나타나지 않는다