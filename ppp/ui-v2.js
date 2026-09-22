(function(){
var src=window.PPP_SOURCE||{}, flows=window.PPP_FLOWS||{}, deep=window.PPP_DEEP||{};
var rp={2:44,3:74,4:104,5:140,6:173,7:203,8:231,9:259,10:291,11:320,12:345,13:377,14:406,15:431,16:459,17:489,18:520,19:549,20:580,21:609,22:633,23:669,24:705,25:749,26:787,27:827};
function e(s){return String(s).replace(/[&<>"']/g,function(m){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[m]})}
function pos(c){
 var p=chapters.find(function(x){return x.n===c.n-1}),n=chapters.find(function(x){return x.n===c.n+1});
 if(!p&&n)return "책 전체의 출발점이다. 좋은 프로그램의 기준을 잡고 다음 "+n.n+"장 ‘"+n.title+"’에서 실제 코드 실행으로 넘어간다.";
 if(p&&n)return "앞의 "+p.n+"장 ‘"+p.title+"’에서 쌓은 내용을 바탕으로 이 장의 주제를 확장하며, 다음 "+n.n+"장 ‘"+n.title+"’의 직접적인 발판이 된다.";
 return "앞 장들에서 쌓은 C++의 개념과 기법을 바탕으로 C 언어와의 관계와 상호 운용을 정리하며 책을 마무리한다.";
}
function flowHTML(c){
 var f=flows[c.n]||[]; if(!f.length)return "";
 var h='<section class="section"><div class="section-kicker">Mental model</div><h3>이 장의 흐름을 먼저 잡기</h3><p class="deep-copy">세부 문법보다 먼저 아래 순서를 잡으면 예제가 왜 나오는지 훨씬 쉽게 연결된다.</p><div class="flow-wrap"><div class="flow">';
 f.forEach(function(x,i){if(i)h+='<span class="flow-arrow">→</span>';h+='<button class="flow-node" data-flow="'+i+'"><b>'+e(x[0])+'</b><span>'+e(x[1])+'</span></button>'});
 return h+'</div><div class="flow-detail">각 단계를 눌러 핵심 역할을 확인하세요.</div></div></section>';
}
function conceptHTML(c){
 var h='<section class="section"><div class="section-kicker">Core concepts</div><h3>핵심 개념을 한 단계 더 자세히</h3><div class="concept-list">';
 c.concepts.forEach(function(x,i){h+='<details class="concept" '+(i===0?'open':'')+'><summary>'+e(x[0])+'</summary><div class="concept-body"><p>'+e(x[1])+'</p><p><strong>읽는 포인트.</strong> 정의만 외우지 말고 위 흐름도에서 이 개념이 어떤 문제를 해결하는지 연결해서 보세요.</p></div></details>'});
 return h+'</div></section>';
}
function deepHTML(c){
 var a=deep[c.n]||[]; if(!a.length)return "";
 var h='<section class="section"><div class="section-kicker">Deep dive</div><h3>조금 더 깊게 이해하기</h3><p class="deep-copy">이 장의 본문 흐름을 세 가지 질문으로 다시 풀어 썼다. 정의를 외우기보다 왜 이런 설계가 필요한지에 초점을 맞춘다.</p><div class="concept-list">';
 a.forEach(function(x,i){h+='<details class="concept" '+(i===0?'open':'')+'><summary>'+e(x[0])+'</summary><div class="concept-body"><p>'+e(x[1])+'</p></div></details>'});
 return h+'</div></section>';
}
function sourceHTML(c){
 var s=src[c.n]; if(!s||!s.points)return "";
 var h='<section class="section"><div class="section-kicker">From the source notes</div><h3>원 학습노트에서 더 챙길 것</h3><p class="deep-copy">업로드된 학습노트의 장별 핵심 정리와 본문 논지를 기준으로 다시 압축했다.</p><div class="source-points">';
 s.points.forEach(function(p,i){h+='<div class="source-point"><span class="i">'+(i+1)+'</span><div>'+e(p)+'</div></div>'});
 return h+'</div></section>';
}
function quizHTML(c){
 var s=src[c.n]; if(!s||!s.quiz)return "";
 var h='<section class="section"><div class="section-kicker">Review</div><h3>원 학습노트 기반 복습 문제</h3><p class="deep-copy">이전 버전의 임의 퀴즈를 없애고 각 장의 실제 복습 문제와 본문 기반 답안에 맞췄다. 먼저 자기 말로 답한 뒤 정답을 여세요.</p><div class="quiz-list">';
 s.quiz.forEach(function(q,i){var meta=rp[c.n]?'학습노트 p.'+rp[c.n]+' · '+q.n:q.n;h+='<div class="quiz-card"><div class="quiz-meta">'+e(meta)+'</div><div class="quiz-q">Q'+(i+1)+'. '+e(q.q)+'</div><button class="answer-btn">정답 보기</button><div class="quiz-a">'+e(q.a)+'</div></div>'});
 return h+'</div></section>';
}
function chapterV2(n){
 var c=chapters.find(function(x){return x.n===n})||chapters[0]; current=c.n; document.title=c.n+'장 '+c.title+' · PPP C++ Study Guide';
 var meta='학습노트 시작 p.'+c.page+(rp[c.n]?' · 복습 문제 p.'+rp[c.n]:'');
 chapterEl.innerHTML=
 '<header class="chapter-head"><div class="chapter-num">'+partLabel(c.n)+' · Chapter '+String(c.n).padStart(2,'0')+'</div><h2>'+e(c.title)+'</h2><div class="chapter-en">'+e(c.en)+'</div>'+
 '<div class="chapter-actions"><button id="doneBtn" class="done '+(isDone(c.n)?'done-on':'')+'">'+(isDone(c.n)?'✓ 읽음':'읽음 표시')+'</button><button class="soft-btn" id="mapBtn">전체 학습지도</button><button class="soft-btn" id="glossaryBtn">개념 사전</button><button class="soft-btn" id="printBtn">인쇄 / PDF</button></div><div class="source-meta">'+meta+'</div></header>'+
 '<p class="one-liner">'+e(c.one)+'</p>'+
 '<section class="section easy"><div class="section-kicker">Why this chapter</div><h3>아주 쉽게 설명하면</h3><p>'+e(c.easy)+'</p><p class="deep-copy"><strong>책 전체에서의 위치.</strong> '+e(pos(c))+'</p></section>'+
 flowHTML(c)+conceptHTML(c)+deepHTML(c)+sourceHTML(c)+
 '<section class="section"><div class="section-kicker">Common trap</div><h3>헷갈리기 쉬운 점</h3><div class="warning">'+e(c.pitfall)+'</div></section>'+
 '<section class="section"><div class="section-kicker">Code</div><h3>코드로 확인하기</h3><p class="deep-copy">코드를 외우기보다 위 개념이 코드의 어느 부분에 나타나는지 찾는 용도로 보세요.</p><div class="code-wrap"><button class="copy-btn" id="copyBtn">코드 복사</button><pre><code>'+e(c.code)+'</code></pre></div></section>'+
 quizHTML(c)+
 '<div class="pager"><button id="prev" '+(c.n===1?'disabled':'')+'>← '+(c.n>1?chapters[c.n-2].title:'이전 장')+'</button><button id="next" '+(c.n===27?'disabled':'')+'>'+(c.n<27?chapters[c.n].title:'다음 장')+' →</button></div>'+
 '<p class="footer-note">설명은 업로드된 한국어 학습노트를 학습용으로 재구성한 것이다. 복습 문제의 정답 역시 해당 학습노트의 본문 기반 답안을 기준으로 하며 원서의 공식 해답은 아니다.</p>';
 document.getElementById('doneBtn').onclick=function(){localStorage.setItem('ppp-done-'+c.n,isDone(c.n)?'0':'1');updateProgress();chapterV2(c.n);mapRender()};
 document.getElementById('prev').onclick=function(){go(c.n-1)};
 document.getElementById('next').onclick=function(){go(c.n+1)};
 document.getElementById('printBtn').onclick=function(){window.print()};
 document.getElementById('mapBtn').onclick=openMap;
 document.getElementById('glossaryBtn').onclick=openGlossary;
 var cb=document.getElementById('copyBtn');cb.onclick=async function(){try{await navigator.clipboard.writeText(c.code);cb.textContent='복사됨 ✓';setTimeout(function(){cb.textContent='코드 복사'},1200)}catch(err){cb.textContent='복사 실패'}};
 chapterEl.querySelectorAll('.quiz-card').forEach(function(card){card.querySelector('.answer-btn').onclick=function(){card.classList.toggle('open');this.textContent=card.classList.contains('open')?'정답 숨기기':'정답 보기'}});
 var f=flows[c.n]||[];chapterEl.querySelectorAll('[data-flow]').forEach(function(b){b.onclick=function(){chapterEl.querySelectorAll('[data-flow]').forEach(function(x){x.style.outline='none'});b.style.outline='2px solid var(--accent)';var x=f[Number(b.dataset.flow)];chapterEl.querySelector('.flow-detail').innerHTML='<strong style="color:var(--accent)">'+e(x[0])+'</strong> — '+e(x[1])}});
 renderNav(search.value);window.scrollTo({top:document.querySelector('.shell').offsetTop-50,behavior:'smooth'});
}
function modals(){
 if(document.getElementById('studyMapModal'))return;
 document.body.insertAdjacentHTML('beforeend','<div class="modal" id="studyMapModal"><div class="modal-card"><div class="modal-head"><h2>27장 전체 학습지도</h2><button class="icon-btn modal-close">닫기</button></div><div class="study-map" id="studyMapGrid"></div></div></div><div class="modal" id="glossaryModal"><div class="modal-card"><div class="modal-head"><h2>개념 사전</h2><button class="icon-btn modal-close">닫기</button></div><input id="glossarySearch" class="glossary-search" placeholder="예: 객체, RAII, 반복자, regex"><div class="glossary-list" id="glossaryList"></div></div></div>');
 document.querySelectorAll('.modal-close').forEach(function(b){b.onclick=function(){b.closest('.modal').classList.remove('open')}});
 document.querySelectorAll('.modal').forEach(function(m){m.onclick=function(ev){if(ev.target===m)m.classList.remove('open')}});
 document.getElementById('glossarySearch').oninput=function(ev){glossRender(ev.target.value)};
}
function mapRender(){
 var el=document.getElementById('studyMapGrid');if(!el)return;var h='';
 chapters.forEach(function(c){h+='<button data-ch="'+c.n+'" class="'+(isDone(c.n)?'done':'')+'"><b>'+String(c.n).padStart(2,'0')+' · '+e(c.title)+'</b><small>'+e(c.one)+'</small></button>'});el.innerHTML=h;
 el.querySelectorAll('[data-ch]').forEach(function(b){b.onclick=function(){document.getElementById('studyMapModal').classList.remove('open');go(Number(b.dataset.ch))}});
}
function glossRender(q){
 var el=document.getElementById('glossaryList');if(!el)return;var s=(q||'').trim().toLowerCase(),items=[];
 chapters.forEach(function(c){c.concepts.forEach(function(x){if(!s||(x[0]+' '+x[1]+' '+c.title).toLowerCase().includes(s))items.push({t:x[0],d:x[1],n:c.n})})});
 el.innerHTML=items.map(function(x){return '<div class="glossary-item"><b>'+e(x.t)+'</b> — '+e(x.d)+' <button data-goto="'+x.n+'">'+x.n+'장으로 →</button></div>'}).join('')||'<div class="empty">검색 결과가 없습니다.</div>';
 el.querySelectorAll('[data-goto]').forEach(function(b){b.onclick=function(){document.getElementById('glossaryModal').classList.remove('open');go(Number(b.dataset.goto))}});
}
function openMap(){mapRender();document.getElementById('studyMapModal').classList.add('open')}
function openGlossary(){glossRender('');document.getElementById('glossaryModal').classList.add('open')}
function theme(){
 var saved=localStorage.getItem('ppp-theme'),dark=window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches;document.documentElement.dataset.theme=saved||(dark?'dark':'light');
 document.getElementById('themeToggle').onclick=function(){var n=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=n;localStorage.setItem('ppp-theme',n)};
}
modals();theme();renderChapter=chapterV2;chapterV2(current);
window.addEventListener('keydown',function(ev){var m=document.querySelector('.modal.open');if(m){if(ev.key==='Escape')m.classList.remove('open');return}if(ev.target.matches('input,textarea'))return;if(ev.key==='ArrowLeft')go(current-1);if(ev.key==='ArrowRight')go(current+1)});
if('serviceWorker' in navigator)window.addEventListener('load',function(){navigator.serviceWorker.register('./sw.js').catch(function(){})});
})();