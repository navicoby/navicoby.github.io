
window.PPP_DEMOS = {
  2:{type:"pipeline",title:"소스가 실행 파일이 되는 과정",items:[
    ["hello.cpp","사람이 쓰는 소스 코드"],
    ["컴파일러","문법·타입을 검사하고 번역"],
    ["hello.o / .obj","오브젝트 코드"],
    ["링커","라이브러리와 여러 오브젝트 결합"],
    ["hello","실행 파일"]
  ]},
  3:{type:"objects",title:"타입이 메모리에 의미를 주는 모습",items:[
    ["age","int","42"],["grade","char","A"],["name","string","Kim"]
  ]},
  6:{type:"parser",title:"2 + 3 * 4가 14가 되는 이유",items:[
    ["Expression","2 + (3 * 4)"],["Term","3 * 4"],["Primary","2 · 3 · 4"],["Result","14"]
  ]},
  17:{type:"pointer",title:"포인터는 주소를 알지만 범위는 모른다",items:["p","0x1000","int","42"]},
  19:{type:"vector",title:"push_back과 capacity 확장",initial:[10,20,30]},
  20:{type:"iterator",title:"[begin, end) 범위에서 반복자 이동",items:["A","B","C","D"]},
  26:{type:"tests",title:"경계값을 노리는 테스트",items:[
    ["빈 입력","원소 0개"],["최소 경계","첫 유효값"],["최대 경계","마지막 유효값"],["바로 바깥","범위 오류"],["중복","같은 값 반복"]
  ]}
};