---
title: "존재론에서 OWL까지: 장기 독서 로드맵"
date: 2026-10-05
draft: false
---

철학적 존재론에서 시작해 형식논리, 형식 존재론, Description Logic, OWL, 실제 Ontology Engineering까지 하나씩 읽고 익히기 위한 장기 로드맵이다.

## 전체 흐름

아리스토텔레스의 존재론  
→ 중세의 보편자·본질·존재 논의  
→ 프레게·러셀의 현대 논리학  
→ 후설·잉가르텐의 형식 존재론  
→ Barry Smith·Guarino의 현대 Formal Ontology  
→ BFO·DOLCE 같은 Upper Ontology  
→ Description Logic  
→ RDF / RDFS / OWL  
→ Protégé / Reasoner / SPARQL / SHACL  
→ Domain Ontology

---

## 1단계 — 고대 존재론과 논리

1. 아리스토텔레스, 《범주론》 — 완료  
   실체, 개별자, 종, 유(類), 질, 양, 관계, 바탕.

2. 아리스토텔레스, 《명제에 관하여》  
   이름, 동사, 명제, 긍정과 부정, 참과 거짓.

3. 아리스토텔레스, 《형이상학》  
   존재, 실체, 본질, 형상과 질료, 가능태와 현실태. 특히 IV권(Γ), VII~IX권(Ζ·Η·Θ).

4. 포르피리오스, 《이사고게(Isagoge)》  
   유, 종, 차이성, 고유성, 우유성.

## 2단계 — 중세 존재론

5. 토마스 아퀴나스, 《존재자와 본질에 관하여(De ente et essentia)》  
   존재와 본질의 구별.

6. 오컴, 《논리학대전(Summa Logicae)》 1부 선별  
   보편자, 이름, 개념, 지시.

## 3단계 — 현대 논리학의 출발

7. 프레게, 〈함수와 개념〉  
   함수와 논항, 주어-술어 구조의 재구성.

8. 프레게, 〈뜻과 지시체에 관하여〉  
   Sinn / Bedeutung, 이름과 지시.

9. 프레게, 〈개념과 대상에 관하여〉  
   object와 concept의 차이.

10. 프레게, 《산술의 기초》  
    수란 무엇인가, 논리주의, 심리주의 비판.

## 4단계 — 러셀과 분석철학

11. 버트런드 러셀, 《철학의 문제들》  
    감각자료, 외부세계, 지식, 보편자, 관계.

12. 러셀, 〈On Denoting〉  
    기술구 이론, 언어의 표면구조와 논리구조.

13. 러셀, 《논리적 원자론의 철학》  
    individual, property, relation, fact.

14. 비트겐슈타인, 《논리철학논고》  
    세계, 사실, 사태, 대상, 명제, 논리적 형식.

15. 비트겐슈타인, 《철학적 탐구》  
    의미=사용, 언어게임, 가족유사성.

16. 카르납, 〈Empiricism, Semantics, and Ontology〉  
    존재론과 언어틀.

17. 콰인, 〈On What There Is〉  
    존재론적 개입(ontological commitment).

18. 크립키, 《이름과 필연》  
    고정지시어, 가능한 세계, 필연성과 우연성, 본질.

## 5단계 — 브렌타노·후설 계보

19. 브렌타노, 《경험적 관점에서 본 심리학》 선별  
    지향성(intentionality).

20. 후설, 《논리연구》  
    형식 존재론의 핵심. 특히 제2·제3·제5연구, 그중 제3연구의 부분-전체와 의존성.

21. 아돌프 라이낙, 〈부정 판단의 이론〉  
    사태(Sachverhalt), 판단, 부정.

22. 라이낙, 《민법의 선험적 기초》  
    약속, 권리, 의무 같은 사회적 존재자의 존재론.

23. 로만 잉가르텐, 《세계의 존재를 둘러싼 논쟁》  
    존재방식, 의존성, 객체와 과정, 형식적·질료적·실존적 존재론.

## 6단계 — 현대 형식 존재론

24. Peter Simons, *Parts: A Study in Ontology*  
    부분-전체론(mereology), identity, dependence.

25. Barry Smith & Kevin Mulligan, 〈Framework for Formal Ontology〉  
    부분-전체, dependent moments, substance, dependence.

26. Barry Smith, 〈The Basic Tools of Formal Ontology〉  
    part, whole, dependence, boundary, continuity, contact.

27. E. J. Lowe, *The Four-Category Ontology*  
    현대 아리스토텔레스적 존재론.

28. Nicola Guarino, 〈Formal Ontology, Conceptual Analysis and Knowledge Representation〉  
    철학적 존재론을 Knowledge Engineering과 연결.

29. Guarino & Welty의 OntoClean 논문들  
    rigidity, identity, unity, dependence로 class hierarchy를 검토.

## 7단계 — Upper Ontology

30. DOLCE — Descriptive Ontology for Linguistic and Cognitive Engineering  
    일상적·인지적 세계를 모델링하는 foundational ontology.

31. BFO 2020 Natural Language Specification  
    continuant / occurrent, independent / dependent, object / quality / role / disposition / process.

32. BFO와 DOLCE 비교  
    같은 현실을 서로 다른 철학적 전제에서 어떻게 모델링하는지 비교.

## 8단계 — Ontology Engineering 입문

33. Noy & McGuinness, *Ontology Development 101*  
    class, property, instance를 이용한 실제 온톨로지 구축.

34. 명제논리와 1차 술어논리  
    ∀, ∃, predicate, relation, implication, identity.

35. 집합론·관계·함수의 기초  
    set, subset, Cartesian product, relation, function, equivalence relation, partial order.

## 9단계 — Description Logic과 Semantic Web

36. Description Logic 입문  
    concept, individual, role, subsumption, satisfiability, restriction, reasoning.

37. Baader et al., *The Description Logic Handbook*  
    우선 입문·기초 장부터 읽는다.

38. RDF / RDFS  
    triple, subject–predicate–object, rdf:type, rdfs:Class, rdfs:subClassOf, domain/range.

39. W3C *OWL 2 Primer*  
    class, property, individual, restrictions, inference.

40. OWL 2 Structural Specification and Direct Semantics  
    someValuesFrom, allValuesFrom, cardinality, equivalentClass, disjointness의 정확한 의미.

41. Protégé + Reasoner 실습  
    class, individual, object property, restriction을 만들고 reasoner로 추론.

42. SPARQL  
    지식그래프와 온톨로지 질의.

43. SHACL  
    OWL 추론과 구분되는 데이터 shape·validation.

## 10단계 — 연구 단계

44. FOIS(Formal Ontology in Information Systems) 논문 선별독  
    책 중심 학습에서 최신 연구 논문 중심으로 전환.

45. 자신의 Domain Ontology 구축  
    class를 먼저 만들기보다 identity, dependence, role, state, process, event, quality, spatial entity, temporal entity를 먼저 분석한 뒤 OWL로 표현한다.

---

## 이 로드맵을 관통하는 두 계보

### 존재론 계보

아리스토텔레스  
→ 중세 스콜라철학  
→ 브렌타노  
→ 후설  
→ 라이낙 / 잉가르텐  
→ Smith / Mulligan / Simons  
→ Formal Ontology  
→ BFO / DOLCE

### 논리·지식표현 계보

아리스토텔레스 논리학  
→ 프레게  
→ 러셀  
→ 초기 비트겐슈타인 / 카르납  
→ 현대 술어논리  
→ Knowledge Representation  
→ Description Logic  
→ RDF / RDFS  
→ OWL

현대 Ontology Engineering은 이 두 흐름이 다시 만나는 지점이다.

Formal Ontology  
+ Formal Logic / Description Logic  
+ Domain Knowledge  
= 계산 가능한 Ontology

## 핵심 질문

아리스토텔레스는 “세계에는 어떤 종류의 것들이 있는가?”를 물었다.

후설과 잉가르텐은 “그 존재들의 일반적 구조와 의존관계는 무엇인가?”를 정교화했다.

프레게와 러셀은 “그 구조를 논리적으로 어떻게 분석할 것인가?”를 발전시켰다.

Smith와 Guarino는 “그 존재론적 구별을 정보시스템 설계에 어떻게 적용할 것인가?”를 연결했다.

Description Logic과 OWL은 “그것을 컴퓨터가 표현하고 추론할 수 있도록 어떻게 형식화할 것인가?”를 제공한다.

따라서 현대 Ontology Engineering은 철학을 버리고 등장한 기술이 아니라, 존재론·논리학·컴퓨터과학이 만나는 분야다.
