const chapters = [
{
 n:1, title:"컴퓨터, 사람, 프로그래밍", en:"Computers, People, and Programming", page:5,
 one:"프로그래밍은 코드를 많이 쓰는 기술이 아니라, 문제를 정확히 이해하고 아이디어를 코드로 직접 표현하는 기술이다.",
 easy:"이 장에는 코드가 거의 없다. 대신 왜 프로그래밍을 배우는지부터 묻는다. 컴퓨터는 세상 곳곳에 숨어 있고, 그 안의 소프트웨어는 사람이 만든다. 그래서 좋은 프로그래머는 컴퓨터만 보는 사람이 아니라 사용자·동료·문제를 함께 보는 사람이다. 중요한 기준은 정확성, 신뢰성, 유지보수성, 단순성, 그리고 아이디어가 코드에 곧바로 드러나는가이다.",
 concepts:[
  ["프로그래밍은 이해","어떤 일을 프로그램으로 만들 수 있다는 것은 그 일을 꽤 정확히 이해했다는 뜻이다."],
  ["두 종류의 품질","밖에서는 정확성·신뢰성·비용을 보고, 코드 안에서는 유지보수성·단순성·직접적 표현을 본다."],
  ["개발은 순환","분석 → 설계 → 프로그래밍 → 테스트가 일직선으로 끝나는 게 아니라 피드백으로 계속 되돌아간다."],
  ["직접적 표현","현실에서 이름 붙일 수 있는 개념이라면 코드 안에서도 타입과 연산으로 표현하는 것이 이상적이다."]
 ],
 pitfall:"코딩부터 시작하는 것. 막히면 키보드에 더 매달리기보다 문제 자체와 설계를 다시 보는 편이 낫다.",
 code:`// 좋은 코드의 출발은 보통 이런 질문이다.
// "무엇을 계산할까?" 보다 먼저
// "사용자가 실제로 원하는 것은 무엇인가?"`,
 quiz:["왜 유지보수성이 중요한가?","분석·설계·프로그래밍·테스트는 왜 반복되는가?","'아이디어를 코드로 직접 표현한다'는 말은 무엇을 뜻하는가?"]
},
{
 n:2, title:"Hello, World!", en:"Hello, World!", page:31,
 one:"소스 코드는 사람이 쓰고, 컴파일러와 링커가 그것을 기계가 실행할 수 있는 프로그램으로 바꾼다.",
 easy:"처음으로 프로그램을 실제로 실행한다. 핵심은 다섯 줄짜리 코드가 아니라 '사람이 쓴 글이 어떻게 실행 파일이 되는가'를 몸으로 익히는 것이다. 컴파일러는 소스 코드의 문법과 타입을 검사해 오브젝트 코드를 만들고, 링커는 여러 오브젝트 코드와 라이브러리를 묶어 실행 파일을 만든다.",
 concepts:[
  ["소스 코드","우리가 읽고 쓰는 .cpp와 헤더 파일의 텍스트."],
  ["컴파일","소스 코드를 검사하고 기계어에 가까운 오브젝트 코드로 번역하는 단계."],
  ["링크","우리 코드와 라이브러리 같은 여러 조각을 하나의 실행 프로그램으로 묶는 단계."],
  ["코드는 두 독자를 가진다","컴퓨터도 읽지만, 더 오래 읽는 쪽은 사람—특히 미래의 나—이다."]
 ],
 pitfall:"컴파일러 오류를 방해물로만 보는 것. 오류를 일찍 잡아주는 컴파일러는 오히려 디버깅 시간을 크게 줄여준다.",
 code:`#include <iostream>
int main() {
    std::cout << "Hello, World!\\n";
    return 0;
}
// 소스 → 컴파일 → 오브젝트 코드 → 링크 → 실행 파일`,
 quiz:["컴파일과 링크의 차이는?","main()은 왜 필요한가?","주석의 가장 중요한 독자는 누구인가?"]
},
{
 n:3, title:"객체, 타입, 값", en:"Objects, Types, and Values", page:51,
 one:"객체는 값을 담는 메모리이고, 타입은 그 값이 무엇이며 어떤 연산을 할 수 있는지를 정한다.",
 easy:"입력을 받으려면 값을 담을 자리가 필요하다. 그 메모리 자리가 객체이고, 이름이 붙으면 변수다. 타입은 '이 상자에 무엇을 넣을 수 있는가'와 '그 값으로 어떤 연산을 할 수 있는가'를 함께 정한다. 이 장의 진짜 주제는 타입 안전성이다.",
 concepts:[
  ["타입","가능한 값의 집합 + 허용되는 연산의 집합."],
  ["객체","특정 타입의 값을 담는 메모리 공간."],
  ["값","메모리의 비트가 타입에 따라 해석된 결과."],
  ["변수","이름이 붙은 객체."],
  ["초기화 vs 대입","처음 값을 넣는 것과 이미 있는 값을 새 값으로 바꾸는 것은 논리적으로 다르다."],
  ["타입 안전성","객체를 그 타입의 규칙에 맞게만 사용하는 것."]
 ],
 pitfall:"초기화하지 않은 변수와 narrowing 변환. 큰 타입의 값을 작은 타입에 조용히 넣으면 정보가 사라질 수 있다.",
 code:`int age {42};          // 초기화
age = 43;             // 대입
double x {2.7};
// int y {x};         // 오류: narrowing 가능
std::string name {"Kim"};`,
 quiz:["객체와 변수의 차이는?","타입이 정하는 두 가지는?","초기화와 대입은 무엇이 다른가?"]
},
{
 n:4, title:"계산", en:"Computation", page:82,
 one:"프로그램은 입력에서 출력을 만드는 계산이고, 계산을 조직하는 핵심 도구는 선택·반복·함수·vector다.",
 easy:"이 장이 끝나면 원리적으로 웬만한 계산을 모두 표현할 수 있다. 값과 표현식, if/switch, while/for, 함수, vector가 한꺼번에 등장한다. 하지만 문법보다 먼저 기억할 기준은 '정확하게, 단순하게, 효율적으로'라는 순서다.",
 concepts:[
  ["정확 > 단순 > 효율","빠르지만 틀리면 무의미하고, 맞지만 지나치게 복잡하면 유지보수가 어렵다."],
  ["추상화","구현 세부를 인터페이스 뒤로 숨겨 필요한 생각만 보게 한다."],
  ["분할정복","큰 계산을 이해 가능한 작은 계산으로 나눈다."],
  ["함수","계산에 이름을 붙여 분리·재사용·테스트를 쉽게 한다."],
  ["vector","같은 타입의 값을 순서대로 저장하고 크기를 스스로 관리하는 기본 컨테이너."]
 ],
 pitfall:"9/5가 1이라는 정수 나눗셈, switch의 break 누락, if 뒤의 실수한 세미콜론은 모두 컴파일될 수 있다.",
 code:`std::vector<int> v {5,7,9};
for (int x : v) {
    std::cout << x << '\\n';
}

double c = 20;
double f = 9.0/5 * c + 32; // 9/5가 아니라 9.0/5`,
 quiz:["정확·단순·효율의 순서는 왜 중요한가?","for와 while은 언제 나눠 쓰는가?","함수를 별도로 만드는 이유는?"]
},
{
 n:5, title:"오류", en:"Errors", page:113,
 one:"오류는 완전히 없애는 대상이라기보다, 일찍 발견하고 격리하고 복구하도록 설계해야 하는 대상이다.",
 easy:"컴파일 오류, 링크 오류, 런타임 오류, 논리 오류를 구분한다. 특히 예외를 통해 오류를 발견하는 곳과 처리하는 곳을 나눈다. 좋은 함수는 자기 사전조건을 검사하고, 테스트는 프로그램이 맞다는 믿음을 확인하는 일이 아니라 깨뜨릴 방법을 찾는 일이다.",
 concepts:[
  ["오류의 네 시점","컴파일 타임, 링크 타임, 런타임, 논리 오류."],
  ["사전조건","함수가 호출되기 전에 참이어야 하는 조건."],
  ["사후조건","함수가 끝난 뒤 보장해야 하는 조건."],
  ["예외","오류 탐지와 처리를 분리하면서 오류를 무시하기 어렵게 만든다."],
  ["테스트","체계적으로 입력을 선택해 예상과 실제 결과를 비교하는 활동."]
 ],
 pitfall:"'컴파일됐다 = 맞다'라고 믿는 것. 가장 골치 아픈 논리 오류는 정상적으로 컴파일되고 실행된다.",
 code:`double area(double w, double h) {
    if (w <= 0 || h <= 0)
        throw std::runtime_error("bad size");
    return w * h;
}`,
 quiz:["컴파일 오류와 논리 오류의 차이는?","예외가 오류 코드 반환보다 유리한 점은?","사전조건은 누가 검사하는 편이 좋은가?"]
},
{
 n:6, title:"프로그램 작성", en:"Writing a Program", page:148,
 one:"좋은 프로그램은 정답 코드를 한 번에 쓰는 것이 아니라, 작은 시도와 실패를 통해 문제 이해를 다듬으며 만들어진다.",
 easy:"계산기를 만들면서 분석→설계→구현을 반복한다. 토큰, 문법, 파서를 통해 사람이 쓰는 수식을 컴퓨터가 이해할 구조로 바꾼다. 핵심은 최종 코드보다 중간의 실패다. 첫 시도는 연산자 우선순위를 놓치고, 다음 시도는 결합 방향이 틀리고, 그 실패가 올바른 문법 설계로 이어진다.",
 concepts:[
  ["프로토타입","문제 이해와 아이디어를 시험하는 작고 제한된 판."],
  ["토큰","숫자·연산자·괄호처럼 입력에서 의미 단위로 취급할 조각."],
  ["문법","어떤 토큰 배열이 올바른 표현식인지 정밀하게 정의하는 규칙."],
  ["파서","문법 규칙에 따라 토큰을 읽어 구조와 의미를 해석하는 프로그램."],
  ["기능 확장 억제","핵심이 돌아가기 전에는 변수·함수 등 욕심나는 기능을 미룬다."]
 ],
 pitfall:"표준 해법이 있는 문제를 처음부터 혼자 발명하려는 것. 문법과 파싱처럼 오래 연구된 문제는 기존 지식을 찾아보는 편이 낫다.",
 code:`// 문법의 생각
// Expression = Term { ('+'|'-') Term }
// Term       = Primary { ('*'|'/') Primary }
// Primary    = Number | '(' Expression ')'`,
 quiz:["토큰화는 왜 필요한가?","프로토타입을 작게 만드는 이유는?","표현식 문법이 연산자 우선순위를 어떻게 보장하는가?"]
},
{
 n:7, title:"프로그램 완성", en:"Completing a Program", page:181,
 one:"'돌아간다'는 완성의 절반쯤일 뿐이고, 나머지는 깨뜨려 보고 정리하고 남에게 줄 수 있게 만드는 일이다.",
 easy:"6장의 계산기를 실제 사용 가능한 프로그램 쪽으로 다듬는다. 프롬프트, 오류 복구, 음수, %, 변수 등을 추가하고 코드를 다시 정리한다. 특히 테스트의 태도와 코드 정리 기준을 익힌다.",
 concepts:[
  ["깨뜨리는 테스트","정상 입력뿐 아니라 이상하고 악의적인 입력도 넣어본다."],
  ["이름 붙이기","반복되는 주석이나 의미 없는 문자 상수는 기호 상수와 이름 있는 함수로 바꾼다."],
  ["오류 복구","오류 처리 코드 자체는 최대한 단순하고 예외를 새로 만들지 않게 한다."],
  ["변경 규모 감각","기능을 40~50% 늘리는 변화는 사실상 새 프로그램처럼 취급해야 한다."]
 ],
 pitfall:"작은 편의를 위해 큰 구조를 섣불리 바꾸는 것. 프로그램 전체를 충분히 테스트하기 전에는 구조 변경 비용을 따져야 한다.",
 code:`constexpr char quit = 'q';
constexpr char print = ';';

while (std::cin) {
    // 명령을 읽고
    // expression()을 계산하고
    // 오류가 나면 복구한다
}`,
 quiz:["'돌아간다' 이후에 해야 할 일은?","왜 테스트에서 이상한 입력이 중요한가?","큰 기능 변경을 새 프로그램처럼 다뤄야 하는 이유는?"]
},
{
 n:8, title:"기술적 세부: 함수 등", en:"Technicalities: Functions, etc.", page:211,
 one:"이 장은 지금까지 감으로 쓰던 함수·선언·스코프·참조를 정확한 규칙으로 정리한다.",
 easy:"큰 프로그램은 한 파일에 다 넣지 않는다. 선언과 정의를 나누고 헤더를 사용해 여러 번역 단위가 같은 인터페이스를 보게 한다. 값 전달, const 참조 전달, 스코프, 전역 변수, 초기화 순서 같은 실제 C++ 코드의 뼈대를 정리한다.",
 concepts:[
  ["선언과 정의","이름과 타입을 알리는 것과 실제 저장공간·함수 본문을 제공하는 것을 구분한다."],
  ["헤더","사용자와 구현자가 동일한 선언을 보게 해 불일치를 컴파일러가 찾게 한다."],
  ["스코프","이름이 보이는 범위. 가능한 작게 유지하면 충돌과 오해가 줄어든다."],
  ["인자 전달","작은 값은 값으로, 큰 읽기 전용 객체는 const 참조로 전달하는 것이 기본 경험칙."],
  ["초기화","지역 변수와 멤버는 자동으로 '좋은 값'이 되는 것이 아니다."]
 ],
 pitfall:"헤더에 using namespace를 넣거나 전역 변수에 지나치게 의존하는 것. 큰 코드에서 이름 충돌과 초기화 순서 문제가 생긴다.",
 code:`// header
double area(double w, double h);

// source
double area(double w, double h) {
    return w*h;
}`,
 quiz:["선언과 정의는 어떻게 다른가?","큰 객체를 const 참조로 넘기는 이유는?","헤더가 인터페이스 일관성을 어떻게 지켜주는가?"]
},
{
 n:9, title:"기술적 세부: 클래스 등", en:"Technicalities: Classes, etc.", page:241,
 one:"클래스는 '데이터 묶음'이 아니라, 어떤 개념의 올바른 상태와 허용 연산을 함께 표현하는 사용자 정의 타입이다.",
 easy:"Date 같은 타입을 개선하면서 생성자, private 데이터, 불변식, enum class, 연산자 오버로딩을 배운다. 핵심은 사용자가 잘못된 상태를 만들기 어렵게 만드는 것이다.",
 concepts:[
  ["타입 = 표현 + 연산","무엇을 저장하는가와 무엇을 할 수 있는가가 함께 타입을 만든다."],
  ["불변식","객체가 살아 있는 동안 항상 참이어야 하는 조건."],
  ["생성자","객체가 만들어지는 순간부터 올바른 상태가 되도록 강제한다."],
  ["private","표현 세부를 숨겨 사용자가 불변식을 깨지 못하게 한다."],
  ["enum class","관련 상수에 타입과 스코프를 줘 잘못된 조합을 컴파일 시간에 줄인다."]
 ],
 pitfall:"모든 것을 public으로 열어두는 것. 무효 상태가 생길 수 있다면 그 클래스의 인터페이스가 불변식을 충분히 지키지 못한다는 신호다.",
 code:`class Date {
public:
    Date(int y, int m, int d);
    int year() const { return y; }
private:
    int y, m, d; // 표현 세부
};`,
 quiz:["불변식이란?","생성자가 왜 중요한가?","enum class가 단순 int 상수보다 안전한 이유는?"]
},
{
 n:10, title:"입출력 스트림", en:"Input and Output Streams", page:268,
 one:"스트림은 키보드·파일 같은 장치 차이를 감추고 '값을 읽고 쓴다'는 하나의 모델로 다루게 해준다.",
 easy:"iostream, 파일 스트림, 오류 상태를 다룬다. 파일을 열면 즉시 상태를 확인하고, eof/fail/bad를 구별한다. 견고한 입력은 한 함수가 모든 일을 하는 대신 읽기·검증·복구를 분리한다.",
 concepts:[
  ["스트림 추상화","장치가 무엇인지보다 어떤 타입의 값을 어떤 형식으로 주고받는지에 집중하게 한다."],
  ["파일 수명","fstream 객체를 만들며 열고, 스코프를 벗어나면 닫힌다."],
  ["상태 비트","eof, fail, bad를 구분해 복구 가능한 오류인지 판단한다."],
  ["관심사 분리","읽기, 범위 검사, 오류 메시지, 복구를 단계적으로 나누면 재사용성이 높아진다."]
 ],
 pitfall:"입력 실패 뒤 상태를 확인하지 않고 계속 읽는 것. fail 상태에서는 적절한 clear와 입력 정리가 필요하다.",
 code:`std::ifstream in("data.txt");
if (!in) throw std::runtime_error("cannot open");

double x;
while (in >> x) {
    // x 처리
}`,
 quiz:["스트림 추상화가 좋은 이유는?","eof와 fail은 어떻게 다른가?","파일을 연 직후 무엇을 해야 하는가?"]
},
{
 n:11, title:"입출력 맞춤화", en:"Customizing Input and Output", page:299,
 one:"입출력 형식은 데이터 그 자체와 다르며, 서식·문자 단위 처리·stringstream을 이용해 목적에 맞게 바꿀 수 있다.",
 easy:"숫자 출력 형식, 파일 열기 모드, 문자열 스트림, getline, 문자 단위 입력을 다룬다. 핵심은 I/O와 실제 처리 로직을 분리하고, 인터페이스를 먼저 설계하는 것이다.",
 concepts:[
  ["서식 상태","oct/hex, fixed/scientific, precision 같은 설정은 스트림에 남아 다음 출력에도 영향을 준다."],
  ["stringstream","문자열을 스트림처럼 다뤄 파싱과 메시지 조립을 쉽게 한다."],
  ["getline","공백을 포함한 한 줄이 필요할 때 사용한다."],
  ["문자 단위 I/O","가장 세밀한 제어를 주지만 직접 처리해야 할 책임도 커진다."],
  ["인터페이스 먼저","어떻게 사용할지 먼저 정하고 내부 구현을 맞춰가는 설계가 유리하다."]
 ],
 pitfall:"출력 서식을 바꾼 뒤 원래대로 돌리지 않아 뒤의 데이터까지 엉뚱한 형식으로 출력되는 것.",
 code:`std::ostringstream os;
os << "x=" << 42 << ", y=" << 3.14;
std::string message = os.str();`,
 quiz:["stringstream은 언제 유용한가?","getline과 >>의 차이는?","왜 setw만 다른 많은 서식 조작자와 다르게 '들러붙지' 않는가?"]
},
{
 n:12, title:"표시 모델", en:"A Display Model", page:329,
 one:"그래픽도 결국 객체를 만들고, 창에 붙이고, 표시하는 일이며 클래스 설계를 눈으로 확인하는 연습장이다.",
 easy:"화면 좌표, 선, 색, Shape 계열 클래스를 사용한다. 중요한 건 그림 그리기 자체보다 '사용자가 보는 개념'을 객체와 인터페이스로 어떻게 표현하는지다.",
 concepts:[
  ["표시 모델","도형 객체를 만들고 Window에 attach한 뒤 화면에 표시한다."],
  ["좌표계","화면에서는 좌상단이 (0,0)이고 y가 아래쪽으로 증가한다."],
  ["화면과 객체","화면에 같은 픽셀이 보여도 서로 다른 클래스는 서로 다른 개념일 수 있다."],
  ["소프트웨어 계층","우리 코드 → 그래픽 인터페이스 → FLTK → 운영체제처럼 층을 두어 복잡성을 감춘다."]
 ],
 pitfall:"화면에 보이는 것만 보고 객체가 무엇을 '알고 있는지'를 무시하는 것. 불변식은 화면이 아니라 객체 상태에 있다.",
 code:`// 개념적 흐름
// Shape s{...};
// win.attach(s);
// win.wait_for_button();`,
 quiz:["그래픽 객체는 언제 화면에 보이는가?","왜 Rectangle과 네 점짜리 Closed_polyline은 같지 않은가?","소프트웨어 계층을 두는 이유는?"]
},
{
 n:13, title:"그래픽 클래스", en:"Graphics Classes", page:353,
 one:"클래스 설계에서는 공통 부분을 재사용하고, 차이만 프로그래밍하면 코드와 오류가 함께 줄어든다.",
 easy:"Point, Color, Polygon, Polyline 같은 그래픽 클래스를 보며 상속 전 단계의 클래스 구성과 구현을 살핀다. 사용자에게 보이는 개념과 내부 저장 방식은 달라도 된다.",
 concepts:[
  ["표현 숨기기","FLTK 같은 구현 세부는 클래스 안에 숨기고 안정된 인터페이스만 밖으로 제공한다."],
  ["차이만 구현","비슷한 도형은 공통 동작을 공유하고 달라지는 동작만 추가한다."],
  ["하나의 개념 = 하나의 객체","선 두 개와 Lines 하나는 픽셀이 같아도 프로그램 의미는 다르다."],
  ["비용 있는 불변식","Polygon처럼 객체 완성 전에 모든 조건을 검사하기 어려운 경우 비용과 대안을 따져야 한다."]
 ],
 pitfall:"'상속할 수 있으니 상속한다'는 식의 설계. 타입은 일관된 개념이어야 하며, 수학적 포함관계와 클래스 상속은 같은 말이 아니다.",
 code:`// 화면에 보이는 중심을 저장하지 않고
// 내부적으로 좌상단 + 폭/높이를 저장해도 된다.
// 중요한 건 인터페이스가 개념을 잘 표현하는가이다.`,
 quiz:["사용자가 보는 표현과 내부 저장 방식은 왜 달라도 되는가?","'차이만 프로그래밍한다'는 뜻은?","Circle과 Ellipse의 관계를 무조건 상속으로 만들면 왜 문제가 될 수 있는가?"]
},
{
 n:14, title:"그래픽 클래스 설계", en:"Graphics Class Design", page:387,
 one:"상속과 가상 함수는 '기존 코드를 고치지 않고 새 종류를 추가하는' 인터페이스 설계를 가능하게 한다.",
 easy:"Shape 계층을 통해 추상 클래스, virtual, override, protected, slicing을 배운다. 핵심은 단지 문법이 아니라 '기반 타입으로 파생 객체를 다룰 수 있게 하는 인터페이스'다.",
 concepts:[
  ["추상 클래스","공통 인터페이스는 제공하지만 그 자체 객체는 만들지 않는 타입."],
  ["가상 함수","실제 객체 타입에 맞는 동작을 실행하는 동적 디스패치."],
  ["override","기반 함수와 정확히 맞는지 컴파일러가 검사하게 하는 표기."],
  ["slicing","파생 객체를 기반 객체 값으로 복사할 때 파생 부분이 잘려 나가는 문제."],
  ["인터페이스 상속","기존 사용 코드를 바꾸지 않고 새 파생 타입을 넣을 수 있게 한다."]
 ],
 pitfall:"클래스 계층을 값으로 복사하는 것. 다형성 객체는 대개 참조나 포인터로 다루고, 복사가 필요하면 명시적 clone 같은 정책을 둔다.",
 code:`struct Shape {
    virtual void draw() const = 0;
    virtual ~Shape() = default;
};
struct Circle : Shape {
    void draw() const override { /* ... */ }
};`,
 quiz:["추상 클래스는 왜 객체를 직접 만들지 못하게 하나?","virtual 함수는 어떤 문제를 해결하는가?","slicing이란?"]
},
{
 n:15, title:"함수와 데이터의 그래프", en:"Graphing Functions and Data", page:415,
 one:"수치·함수·데이터를 눈으로 보여 주려면 계산뿐 아니라 축·배율·레이아웃까지 명확한 객체로 모델링해야 한다.",
 easy:"Function, Axis, Scale 같은 작은 클래스를 통해 수학 함수와 데이터 시각화를 구성한다. 작은 클래스를 만드는 것이 과한 것이 아니라 반복과 오류를 줄이는 방법임을 보여준다.",
 concepts:[
  ["Function","함수를 점들로 샘플링해 Shape에 넣어 화면에 그리는 객체."],
  ["Scale","수학 좌표를 화면 좌표로 바꾸는 작은 변환 객체."],
  ["합성","Axis처럼 여러 하위 객체를 묶어 하나의 고수준 개념으로 만든다."],
  ["람다","짧은 함수를 그 자리에서 표현하고 필요한 값을 캡처한다."],
  ["합리적 범위 테스트","그래프가 '괜찮아 보인다'고 해서 계산이 맞는 것은 아니다."]
 ],
 pitfall:"오버플로 같은 수치 오류를 그래픽 문제로 착각하는 것. 시각화가 이상하면 데이터 생성 단계도 의심해야 한다.",
 code:`auto f = [](double x) { return x*x; };
// Function graph(f, ...);
// Axis x_axis(...);`,
 quiz:["Scale 같은 작은 클래스를 만드는 장점은?","그래프가 이상할 때 화면 코드만 의심하면 안 되는 이유는?","합성과 상속은 어떻게 다른가?"]
},
{
 n:16, title:"그래픽 사용자 인터페이스", en:"Graphical User Interfaces", page:439,
 one:"GUI에서는 프로그램이 순서를 정하는 것이 아니라 사용자의 이벤트가 순서를 정한다—이것이 제어 역전이다.",
 easy:"버튼, 입력 상자, 출력 상자, 콜백을 이용해 GUI를 만든다. 주 논리와 GUI 접착 코드를 분리해야 하고, 콜백 사이의 상태는 창 객체가 관리하게 한다.",
 concepts:[
  ["콜백","사용자 이벤트가 발생했을 때 GUI 시스템이 호출하는 함수."],
  ["접착 함수","시스템의 호출 규약을 C++ 객체의 멤버 함수로 연결하는 얇은 코드."],
  ["제어 역전","main이 순서를 밀어붙이지 않고 사용자의 클릭·입력이 흐름을 결정한다."],
  ["redraw","상태가 바뀌어도 화면은 자동으로 갱신되지 않을 수 있으므로 다시 그리기를 요청한다."],
  ["수명","창에 붙인 GUI 객체는 필요한 동안 살아 있어야 한다."]
 ],
 pitfall:"지역 변수로 만든 버튼·위젯을 attach해 두고 함수가 끝난 뒤에도 살아 있을 거라 생각하는 것.",
 code:`// 개념적 구조
// My_window win(...);
// win.attach(next_button);
// gui_main();  // 이벤트 루프`,
 quiz:["콜백이 필요한 이유는?","제어 역전이란?","GUI 객체의 수명 문제가 왜 중요한가?"]
},
{
 n:17, title:"vector와 자유 저장소", en:"Vector and Free Store", page:467,
 one:"포인터는 강력하지만 '주소만 알고 크기는 모르는' 도구이므로, 자원 수명과 범위를 객체가 대신 관리하게 해야 안전하다.",
 easy:"포인터, 참조, new/delete, 자유 저장소, this, 연결 리스트를 다룬다. 가장 중요한 메시지는 메모리를 직접 잡았으면 반드시 누가 언제 해제할지 명확해야 한다는 것. 그 책임을 소멸자에 넣는 방식이 RAII로 이어진다.",
 concepts:[
  ["포인터","객체의 주소 + 타입. 그 배열의 길이까지 알려주지는 않는다."],
  ["참조","기존 객체에 대한 별칭. 보통 '없음'이 허용되지 않는 매개변수에 유리하다."],
  ["new/delete","동적 객체를 만들고 없애지만, 직접 관리하면 누수·중복 해제 위험이 생긴다."],
  ["소멸자","객체가 사라질 때 반드시 실행되는 정리 동작."],
  ["RAII의 씨앗","자원 획득과 해제를 객체 수명에 묶는 설계."]
 ],
 pitfall:"벌거벗은 new와 delete를 여기저기 흩뿌리는 것. 소유권이 보이지 않으면 누수와 이중 해제가 생긴다.",
 code:`class Buffer {
    int* p;
public:
    Buffer(std::size_t n) : p(new int[n]{}) {}
    ~Buffer() { delete[] p; }
};`,
 quiz:["포인터가 배열의 크기를 모른다는 게 왜 위험한가?","소멸자의 장점은?","포인터와 참조를 언제 구분해 쓰는가?"]
},
{
 n:18, title:"vector와 배열", en:"Vectors and Arrays", page:497,
 one:"자원을 소유하는 클래스는 기본 복사로는 부족하며, 복사·대입·이동·소멸의 의미를 직접 정해야 한다.",
 easy:"배열과 포인터 관계, 복사 생성자, 복사 대입, 이동, operator[]를 다룬다. 포인터 멤버를 가진 객체를 단순 비트 복사하면 두 객체가 같은 메모리를 소유해 문제가 생긴다.",
 concepts:[
  ["깊은 복사","새 메모리를 만들어 원소까지 복사해 두 객체가 독립적으로 소유하게 한다."],
  ["복사 대입","자기 대입과 예외 안전까지 고려해 '새 것 먼저, 옛 것 나중'으로 처리한다."],
  ["이동","임시 객체의 자원을 복사하지 않고 훔겨 성능과 단순성을 얻는다."],
  ["Rule of resource ownership","소멸자가 필요하면 복사·대입·이동도 함께 점검한다."],
  ["배열의 한계","크기를 스스로 모르고, 범위 검사도 없고, 이름이 포인터로 붕괴한다."]
 ],
 pitfall:"포인터 멤버가 있는 클래스에서 컴파일러가 만든 기본 복사를 그대로 쓰는 것.",
 code:`// 개념
// Vector(const Vector& other);            // 깊은 복사
// Vector& operator=(const Vector& other); // 복사 대입
// Vector(Vector&& other) noexcept;        // 이동`,
 quiz:["얕은 복사가 왜 두 번 delete를 만들 수 있는가?","이동은 복사와 무엇이 다른가?","배열보다 vector가 안전한 이유는?"]
},
{
 n:19, title:"vector, 템플릿, 예외", en:"Vector, Templates, and Exceptions", page:528,
 one:"템플릿은 특정 타입에 묶인 알고리즘과 컨테이너를 일반화하고, RAII와 예외는 자원 안전성을 유지한다.",
 easy:"직접 만든 vector를 가변 크기로 완성하고 템플릿으로 일반화한다. reserve/push_back/resize의 관계, allocator, unique_ptr/shared_ptr, 범위 검사와 예외를 다룬다.",
 concepts:[
  ["템플릿","타입을 매개변수로 받아 같은 설계를 여러 타입에 적용한다."],
  ["reserve","용량만 늘려 재할당 횟수를 줄이는 vector의 기반 연산."],
  ["size vs capacity","실제 원소 수와 확보해 둔 저장 공간은 다르다."],
  ["RAII","예외로 함수를 빠져나가도 지역 객체의 소멸자는 실행돼 자원을 정리한다."],
  ["스마트 포인터","소유권을 타입으로 표현해 직접 delete할 필요를 줄인다."]
 ],
 pitfall:"처음부터 템플릿으로 쓰려는 것. 먼저 한 구체 타입으로 정확히 만든 뒤 일반화하는 편이 훨씬 쉽다.",
 code:`template<class T>
class Box {
    T value;
public:
    explicit Box(T v) : value(std::move(v)) {}
    const T& get() const { return value; }
};`,
 quiz:["size와 capacity의 차이는?","템플릿을 언제 일반화하는 편이 좋은가?","RAII가 예외와 잘 맞는 이유는?"]
},
{
 n:20, title:"컨테이너와 반복자", en:"Containers and Iterators", page:557,
 one:"반복자는 컨테이너의 저장 방식과 알고리즘을 분리해, N개의 컨테이너 × M개의 알고리즘을 N+M 구조로 줄인다.",
 easy:"vector와 list 같은 컨테이너를 하나의 '열(sequence)' 관점에서 보고, begin/end 반복자로 순회한다. 알고리즘은 컨테이너 내부 구조를 몰라도 반복자만 알면 된다.",
 concepts:[
  ["반열린 구간","[begin, end)로 표현하면 빈 범위와 부분 범위를 자연스럽게 다룰 수 있다."],
  ["반복자","*로 값에 접근하고 ++로 이동하며 ==/!=로 비교하는 순회 인터페이스."],
  ["컨테이너와 알고리즘 분리","vector/list가 같은 알고리즘을 공유할 수 있게 한다."],
  ["vector 우선","특별한 삽입·삭제 요구가 없다면 기본 선택은 vector가 되는 경우가 많다."],
  ["무효화","vector 재할당 뒤에는 예전 반복자가 더 이상 유효하지 않을 수 있다."]
 ],
 pitfall:"end()를 마지막 원소라고 생각하는 것. end는 '마지막 다음 위치'다.",
 code:`for (auto it = v.begin(); it != v.end(); ++it) {
    std::cout << *it << '\\n';
}`,
 quiz:["왜 [begin,end) 구간을 쓰는가?","반복자가 포인터와 비슷하지만 같은 것은 아닌 이유는?","vector에서 insert 후 반복자가 무효화될 수 있는 이유는?"]
},
{
 n:21, title:"알고리즘과 map", en:"Algorithms and Maps", page:588,
 one:"표준 알고리즘과 map을 잘 쓰면 직접 작성할 코드가 크게 줄고, 의도도 더 명확하게 표현된다.",
 easy:"find, count, sort, accumulate, inner_product, map, set, unordered_map 등을 다룬다. 핵심은 라이브러리가 이미 잘 푼 문제를 다시 풀지 않는 것과, 비교 함수·함수 객체·람다로 알고리즘을 매개변수화하는 것이다.",
 concepts:[
  ["표준 알고리즘","반복자 범위에 동작하며 컨테이너 종류와 독립적이다."],
  ["함수 객체와 람다","알고리즘의 판단 기준을 코드로 전달한다."],
  ["map","키→값 관계를 저장하고 키 순서로 순회한다."],
  ["unordered_map","순서가 필요 없고 큰 키 조회가 많을 때 평균 O(1) 접근을 기대한다."],
  ["이진 검색","정렬된 범위에서 선형 탐색보다 훨씬 적은 비교로 찾는다."]
 ],
 pitfall:"정렬되지 않은 데이터에 이진 검색을 쓰거나, accumulate의 초기값 타입을 잘못 골라 결과 타입을 의도치 않게 만드는 것.",
 code:`std::map<std::string,int> count;
for (const auto& word : words) ++count[word];

auto it = std::find(v.begin(), v.end(), target);`,
 quiz:["vector/map/unordered_map은 어떤 기준으로 고르는가?","함수 객체가 필요한 이유는?","이진 검색이 정렬을 요구하는 이유는?"]
},
{
 n:22, title:"이상과 역사", en:"Ideals and History", page:617,
 one:"프로그래밍 언어는 시대의 문제에 답한 설계이며, 좋은 코드는 언어 기능보다 더 오래된 '이상'에 의해 방향을 잡는다.",
 easy:"Fortran, COBOL, Lisp, Algol, Simula, C, C++의 흐름을 따라간다. 핵심은 어떤 언어도 모든 장점을 동시에 가질 수 없기 때문에, 정확성·단순성·유지보수성·성능 같은 이상이 설계의 절충을 이끈다는 것이다.",
 concepts:[
  ["이상의 역할","구체 문법보다 오래 남는 설계 기준."],
  ["효율적 추상화","C++의 큰 목표: 높은 수준의 개념을 표현하면서 불필요한 실행 비용을 강요하지 않는다."],
  ["다중 패러다임","절차적·객체지향·제네릭을 서로 배척하지 않고 상황에 따라 결합한다."],
  ["언어의 역사","각 언어는 특정 시대와 문제의 요구에 대한 사람들의 해법이다."],
  ["도구는 인간을 위해","언어 기능의 목적은 프로그래머가 문제를 더 직접 표현하도록 돕는 것이다."]
 ],
 pitfall:"'최고의 언어 하나'를 찾으려는 것. 문제와 팀과 환경에 따라 적절한 도구가 달라진다.",
 code:`// 언어 선택도 설계다.
// 필요한 추상화, 성능, 생태계, 팀 역량을 보고 고른다.`,
 quiz:["프로그래밍에서 '이상'이 왜 중요한가?","C++의 효율적 추상화란?","왜 여러 언어를 아는 것이 도움이 되는가?"]
},
{
 n:23, title:"텍스트 조작", en:"Text Manipulation", page:644,
 one:"텍스트 처리는 문자열을 값으로 바꾸는 일과 패턴을 찾는 일이며, 정규 표현식은 복잡한 if 묶음을 선언적인 패턴으로 바꾼다.",
 easy:"string, stringstream, map을 다시 활용하고 regex를 소개한다. 이메일·우편번호처럼 사람이 쓴 텍스트에서 구조를 찾아 데이터로 바꾸는 작업을 다룬다.",
 concepts:[
  ["문자열↔값","stringstream으로 변환을 안전하게 통일할 수 있다."],
  ["정규 표현식","문자열의 구조와 반복 패턴을 간결하게 표현하는 작은 언어."],
  ["regex_search vs regex_match","부분 일치와 전체 일치를 구분한다."],
  ["smatch","전체 일치와 괄호로 묶은 하위 패턴을 결과로 제공한다."],
  ["층 분리","일반 메시지 구조를 먼저 만들고 특정 검색·분석 기능을 나중에 올린다."]
 ],
 pitfall:"정규 표현식을 지나치게 영리하게 만들어 읽기 어려운 '쓰기 전용 언어'로 만드는 것.",
 code:`std::regex zip(R"(\\w{2}\\s*\\d{5}(-\\d{4})?)");
std::smatch m;
if (std::regex_search(line, m, zip)) {
    // m[0] = 전체 일치
}`,
 quiz:["regex_search와 regex_match의 차이는?","왜 raw string literal이 regex에 유용한가?","문자열 변환을 stringstream으로 통일할 장점은?"]
},
{
 n:24, title:"수치", en:"Numerics", page:678,
 one:"컴퓨터 숫자는 수학의 수가 아니라 제한된 근사 표현이며, 크기·정밀도·오버플로를 항상 의식해야 한다.",
 easy:"정수와 부동소수점의 한계, numeric_limits, 다차원 Matrix, 가우스 소거, 난수, 수학 함수, complex를 다룬다. 수치 계산에서 '그럴듯한가?' 검사가 중요한 이유가 반복된다.",
 concepts:[
  ["정수와 실수의 한계","정수는 오버플로하고, 부동소수점은 정밀도를 조용히 잃을 수 있다."],
  ["numeric_limits","타입의 최소·최대·정밀도를 하드코딩하지 않고 프로그램에서 확인한다."],
  ["Matrix","차원과 원소 타입을 명시한 고수준 배열 추상화."],
  ["난수 = 엔진 + 분포","난수 엔진은 수열을 만들고 분포가 원하는 확률 형태로 바꾼다."],
  ["부동소수점 비교","정확한 == 대신 허용 오차나 결과 검증을 고려한다."]
 ],
 pitfall:"수치 결과를 화면에 찍고 '그럴듯해 보이니 맞다'고 끝내는 것. 범위·오버플로·정밀도 손실을 별도로 시험해야 한다.",
 code:`auto max_i = std::numeric_limits<int>::max();
// 정수 오버플로 전 경계 확인

std::mt19937 rng(123);
std::uniform_int_distribution<int> dice(1,6);
int roll = dice(rng);`,
 quiz:["부동소수점 계산에서 ==가 위험한 이유는?","난수 엔진과 분포는 어떻게 다른가?","numeric_limits를 쓰는 이유는?"]
},
{
 n:25, title:"임베디드 시스템 프로그래밍", en:"Embedded Systems Programming", page:715,
 one:"임베디드에서는 '정답'뿐 아니라 언제 끝나는지, 얼마나 메모리를 쓰는지, 고장 때 어떻게 버티는지도 정확성의 일부다.",
 easy:"실시간성, 자원 제한, 비트 조작, 메모리 풀, 고장 허용, 코딩 표준을 다룬다. 그렇다고 고수준 추상화를 모두 버리는 것은 아니다. 필요한 경우에만 낮은 수준으로 내려가고, 그 이유를 측정과 도메인 지식으로 뒷받침한다.",
 concepts:[
  ["예측 가능성","하드 실시간에서는 실행 시간·할당·예외 경로가 예측 가능해야 한다."],
  ["자원 정책","동적 할당을 금지하거나 시작 시에만 허용하는 식으로 정책을 설계할 수 있다."],
  ["비트 조작","마스크와 시프트로 하드웨어 레지스터·플래그를 다룬다."],
  ["고장 허용","복제, 감시, 자가 점검, 계층적 오류 처리로 남은 실패와 함께 산다."],
  ["코딩 표준","도메인 위험을 줄이기 위한 검증 가능한 팀 규칙."]
 ],
 pitfall:"임베디드라는 이유로 '미화된 어셈블러'처럼만 코딩하는 것. 성능 문제가 실제로 있는지 측정하지 않고 추상화를 버리면 유지보수성만 잃을 수 있다.",
 code:`enum Flags : unsigned {
    ready = 1u << 0,
    error = 1u << 1
};
unsigned state = 0;
state |= ready;          // 플래그 세우기
bool bad = state & error;`,
 quiz:["임베디드에서 정확성의 범위가 더 넓은 이유는?","왜 동적 할당을 제한할 수 있는가?","비트 마스크는 무엇을 표현하는가?"]
},
{
 n:26, title:"테스트", en:"Testing", page:762,
 one:"테스트는 오류가 없음을 증명하지 못하지만, 오류가 숨을 곳을 줄이고 시스템이 실패를 견디도록 설계하게 만든다.",
 easy:"단위 테스트, 회귀 테스트, 테스트 하네스, 경계값, 성능 측정을 다룬다. 테스트를 나중에 붙이는 별도 작업이 아니라 설계의 일부로 본다.",
 concepts:[
  ["단위부터 위로","함수와 클래스 수준부터 신뢰를 쌓고 더 큰 시스템으로 올라간다."],
  ["회귀 테스트","고친 버그는 최소 재현 사례로 남겨 다시는 돌아오지 못하게 한다."],
  ["경계 테스트","빈 입력, 최소·최대, 홀짝, 중복, 바로 전·바로 후 값을 체계적으로 시험한다."],
  ["테스트 하네스","어떤 테스트가 실패했는지 명확히 말해 주는 실행 틀도 설계 대상이다."],
  ["측정 기반 성능","충분히 효율적인지 실제 큰 데이터와 chrono로 측정한 뒤 최적화한다."]
 ],
 pitfall:"커버리지 숫자만 보고 충분히 테스트했다고 생각하는 것. 실행된 줄 수보다 어떤 위험을 노렸는지가 중요하다.",
 code:`auto t0 = std::chrono::steady_clock::now();
// test target
auto t1 = std::chrono::steady_clock::now();
auto elapsed = t1 - t0;`,
 quiz:["회귀 테스트의 목적은?","경계값 테스트가 중요한 이유는?","왜 테스트하기 쉬운 설계가 좋은 설계인가?"]
},
{
 n:27, title:"C 프로그래밍 언어", en:"The C Programming Language", page:797,
 one:"C는 C++와 가까운 별개의 언어이며, 더 적은 안전 장치와 더 직접적인 메모리·문자열 관리를 요구한다.",
 easy:"C++를 아는 사람이 C를 읽고 쓸 수 있도록 차이를 정리한다. C에는 클래스·가상 함수·오버로딩·템플릿이 없고, 문자열과 메모리를 더 직접 관리한다. C와 C++를 섞을 때는 extern \"C\" 같은 링크 규칙을 사용한다.",
 concepts:[
  ["C와 C++는 별개","겹치는 부분이 크지만 하나의 'C/C++' 언어가 있는 것은 아니다."],
  ["더 약한 검사","C는 많은 오류를 컴파일러가 막아주지 않아 경고 수준과 lint가 더 중요하다."],
  ["C 문자열","0으로 끝나는 char 배열. 길이·복사 공간·종결 문자를 직접 신경 써야 한다."],
  ["함수 포인터","C에서 객체지향적 동작을 흉내 내는 핵심 수단 중 하나."],
  ["extern C","C++에서 C의 링크 이름 규칙을 사용해 상호 운용한다."]
 ],
 pitfall:"malloc/free와 new/delete를 섞거나, strcpy/scanf(\"%s\")처럼 버퍼 크기를 무시하는 코드를 가볍게 쓰는 것.",
 code:`extern "C" {
    int c_library_function(int);
}

// C++에서는 가능하면 std::string, vector,
// RAII 같은 안전한 추상화를 우선한다.`,
 quiz:["왜 'C/C++'라는 하나의 언어가 있다고 보면 안 되는가?","C 문자열이 std::string보다 위험한 이유는?","extern \"C\"의 목적은?"]
}
];

const partLabel = n => n<=7 ? "Part 1 · 기초와 프로그램 만들기" : n<=11 ? "Part 2 · 언어와 I/O" : n<=16 ? "Part 3 · 그래픽과 객체지향" : n<=21 ? "Part 4 · 메모리와 STL" : "Part 5 · 확장 주제";
const nav = document.getElementById("nav");
const chapterEl = document.getElementById("chapter");
const search = document.getElementById("search");
let current = Number(location.hash.replace("#ch","")) || 1;

function isDone(n){ return localStorage.getItem("ppp-done-"+n)==="1"; }
function updateProgress(){
  const done = chapters.filter(c=>isDone(c.n)).length;
  document.getElementById("progressBar").style.width = (done/chapters.length*100)+"%";
  document.getElementById("progressLabel").textContent = `${done} / ${chapters.length} 읽음`;
}
function renderNav(filter=""){
  const q = filter.trim().toLowerCase();
  let lastPart = "";
  nav.innerHTML = "";
  chapters.filter(c => !q || [c.title,c.en,c.one,...c.concepts.flat()].join(" ").toLowerCase().includes(q)).forEach(c=>{
    const p = partLabel(c.n);
    if(p!==lastPart){
      const t=document.createElement("div"); t.className="nav-title"; t.textContent=p; nav.appendChild(t); lastPart=p;
    }
    const a=document.createElement("a");
    a.href="#ch"+c.n; a.className="chapter-link"+(c.n===current?" active":"");
    a.innerHTML=`<span class="num">${String(c.n).padStart(2,"0")}</span><span>${c.title}</span>`;
    nav.appendChild(a);
  });
  if(!nav.children.length) nav.innerHTML='<div class="empty">검색 결과가 없습니다.</div>';
}
function renderChapter(n){
  const c=chapters.find(x=>x.n===n) || chapters[0];
  current=c.n;
  document.title = `${c.n}장 ${c.title} — PPP C++ 쉬운 설명`;
  chapterEl.innerHTML = `
    <div class="chapter-head">
      <div>
        <div class="chapter-kicker">${partLabel(c.n)} · Chapter ${c.n}</div>
        <h2>${c.title}</h2>
        <div class="en">${c.en}</div>
      </div>
      <div class="source-page">학습노트 시작 p.${c.page}<br><button class="done ${isDone(c.n)?"done-on":""}" id="doneBtn">${isDone(c.n)?"✓ 읽음":"읽음 표시"}</button></div>
    </div>
    <p class="one-liner">${c.one}</p>
    <section class="section easy"><h3>아주 쉽게 설명하면</h3><p>${c.easy}</p></section>
    <section class="section"><h3>핵심 개념</h3><div class="cards">${c.concepts.map(([a,b])=>`<div class="card"><strong>${a}</strong><span>${b}</span></div>`).join("")}</div></section>
    <section class="section"><h3>헷갈리기 쉬운 점</h3><div class="card pitfall"><strong>주의</strong><span>${c.pitfall}</span></div></section>
    <section class="section"><h3>코드로 보면</h3><pre><code>${escapeHtml(c.code)}</code></pre></section>
    <section class="section"><h3>3분 복습</h3><div class="quiz">${c.quiz.map((q,i)=>`<div class="q"><strong>Q${i+1}.</strong> ${q}</div>`).join("")}</div></section>
    <div class="pager">
      <button id="prev" ${c.n===1?"disabled":""}>← 이전 장</button>
      <button id="next" ${c.n===27?"disabled":""}>다음 장 →</button>
    </div>
    <p class="footer-note">이 웹 가이드는 업로드된 한국어 학습노트의 구조와 핵심 내용을 바탕으로 다시 풀어쓴 개인 학습용 요약입니다. 정확한 표현과 전체 맥락은 원 학습노트와 원서를 함께 확인하세요.</p>
  `;
  document.getElementById("doneBtn").onclick=()=>{
    localStorage.setItem("ppp-done-"+c.n, isDone(c.n)?"0":"1");
    updateProgress(); renderChapter(c.n);
  };
  document.getElementById("prev").onclick=()=>go(c.n-1);
  document.getElementById("next").onclick=()=>go(c.n+1);
  renderNav(search.value);
  window.scrollTo({top: document.querySelector(".layout").offsetTop-10, behavior:"smooth"});
}
function go(n){
  if(n<1||n>27) return;
  location.hash="#ch"+n;
}
function escapeHtml(s){
  return s.replace(/[&<>"']/g, m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[m]));
}
window.addEventListener("hashchange",()=>{
  const n=Number(location.hash.replace("#ch",""))||1;
  renderChapter(n);
});
search.addEventListener("input",e=>renderNav(e.target.value));
document.getElementById("resetProgress").onclick=()=>{
  if(confirm("27장 진도 표시를 모두 초기화할까요?")){
    chapters.forEach(c=>localStorage.removeItem("ppp-done-"+c.n));
    updateProgress(); renderChapter(current);
  }
};
updateProgress();
renderNav();
renderChapter(current);