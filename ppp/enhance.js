
(() => {
  const flows = window.PPP_FLOWS || {};
  const css = document.createElement('style');
  css.textContent = `
    .extra-tools{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
    .extra-tools button,.copy-btn{border:1px solid var(--line);background:var(--panel2);color:var(--text);border-radius:10px;padding:8px 11px;cursor:pointer}
    .flow-wrap{border:1px solid var(--line);background:var(--panel2);border-radius:16px;padding:16px;overflow:auto}
    .flow{display:flex;gap:8px;align-items:stretch;min-width:680px}
    .flow-node{flex:1;border:1px solid var(--line);background:var(--panel);color:var(--text);border-radius:12px;padding:12px;cursor:pointer;text-align:left}
    .flow-node b{display:block;color:var(--accent2);margin-bottom:4px}
    .flow-arrow{align-self:center;color:var(--muted);font-size:1.2rem}
    .flow-detail{margin-top:12px;color:var(--muted);border-left:3px solid var(--accent);padding-left:12px}
    .flash-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
    .flash{border:1px solid var(--line);background:var(--panel2);border-radius:14px;padding:15px;cursor:pointer;min-height:110px}
    .flash .back{display:none;color:var(--muted);margin-top:8px}
    .flash.open .back{display:block}
    .study-map{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
    .study-map button{border:1px solid var(--line);background:var(--panel2);color:var(--text);border-radius:13px;padding:12px;text-align:left;cursor:pointer}
    .study-map button.done{border-color:var(--good)}
    .study-map small{display:block;color:var(--muted);margin-top:4px}
    .modal{position:fixed;inset:0;background:rgba(3,8,20,.78);display:none;z-index:999;padding:20px;overflow:auto}
    .modal.open{display:block}
    .modal-card{max-width:1000px;margin:30px auto;background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:20px}
    .modal-head{display:flex;justify-content:space-between;align-items:center;gap:10px}
    .modal-close{border:1px solid var(--line);background:var(--panel2);color:var(--text);border-radius:10px;padding:7px 10px;cursor:pointer}
    .glossary-search{width:100%;margin:12px 0;border:1px solid var(--line);background:var(--panel2);color:var(--text);border-radius:12px;padding:11px}
    .glossary-list{display:grid;gap:8px}
    .glossary-item{border:1px solid var(--line);background:var(--panel2);border-radius:12px;padding:12px}
    .glossary-item button{border:0;background:transparent;color:var(--accent);cursor:pointer}
    .hint-btn{border:0;background:transparent;color:var(--accent);cursor:pointer;padding:0;margin-top:7px}
    .hint{display:none;color:var(--muted);margin-top:7px}
    .hint.show{display:block}
    .copy-row{display:flex;justify-content:flex-end;margin-bottom:6px}
    @media(max-width:700px){.flash-grid,.study-map{grid-template-columns:1fr}}
  `;
  document.head.appendChild(css);

  function ensureModals(){
    if(document.getElementById('studyMapModal')) return;
    document.body.insertAdjacentHTML('beforeend', `
      <div class="modal" id="studyMapModal"><div class="modal-card">
        <div class="modal-head"><h2>27장 전체 학습지도</h2><button class="modal-close">닫기</button></div>
        <div class="study-map" id="studyMapGrid"></div>
      </div></div>
      <div class="modal" id="glossaryModal"><div class="modal-card">
        <div class="modal-head"><h2>개념 사전</h2><button class="modal-close">닫기</button></div>
        <input id="glossarySearch" class="glossary-search" placeholder="개념 검색">
        <div class="glossary-list" id="glossaryList"></div>
      </div></div>
    `);
    document.querySelectorAll('.modal-close').forEach(b=>b.onclick=()=>b.closest('.modal').classList.remove('open'));
    document.querySelectorAll('.modal').forEach(m=>m.onclick=e=>{if(e.target===m)m.classList.remove('open')});
    document.getElementById('glossarySearch').oninput=e=>renderGlossary(e.target.value);
  }

  function renderMap(){
    const el = document.getElementById('studyMapGrid');
    if(!el) return;
    el.innerHTML = chapters.map(c=>`
      <button data-n="${c.n}" class="${isDone(c.n)?'done':''}">
        <b>${String(c.n).padStart(2,'0')} · ${c.title}</b>
        <small>${c.one}</small>
      </button>`).join('');
    el.querySelectorAll('button[data-n]').forEach(b=>b.onclick=()=>{
      b.closest('.modal').classList.remove('open'); go(Number(b.dataset.n));
    });
  }

  function renderGlossary(q=''){
    const el = document.getElementById('glossaryList');
    if(!el) return;
    const s=q.trim().toLowerCase();
    const items=chapters.flatMap(c=>c.concepts.map(([term,desc])=>({term,desc,n:c.n,title:c.title})))
      .filter(x=>!s || (x.term+' '+x.desc+' '+x.title).toLowerCase().includes(s));
    el.innerHTML = items.map(x=>`
      <div class="glossary-item"><b>${x.term}</b> — ${x.desc}
      <button data-n="${x.n}">${x.n}장으로 →</button></div>`).join('') || '<div class="empty">검색 결과가 없습니다.</div>';
    el.querySelectorAll('button[data-n]').forEach(b=>b.onclick=()=>{
      b.closest('.modal').classList.remove('open'); go(Number(b.dataset.n));
    });
  }

  function addGlobalTools(){
    const a=document.querySelector('.hero-actions'); if(!a || document.getElementById('studyMapBtn')) return;
    const m=document.createElement('button');m.id='studyMapBtn';m.className='action';m.textContent='전체 학습지도';
    const g=document.createElement('button');g.id='glossaryBtn';g.className='action';g.textContent='개념 사전';
    a.append(m,g);
    m.onclick=()=>{renderMap();document.getElementById('studyMapModal').classList.add('open')};
    g.onclick=()=>{renderGlossary();document.getElementById('glossaryModal').classList.add('open')};
  }

  function augment(c){
    if(!c || chapterEl.querySelector('.flow-wrap')) return;

    const one=chapterEl.querySelector('.one-liner');
    const f=flows[c.n]||[];
    const sec=document.createElement('section');
    sec.className='section';
    sec.innerHTML='<h3>개념 흐름도</h3><div class="flow-wrap"><div class="flow">'+
      f.map((x,i)=>(i?'<span class="flow-arrow">→</span>':'')+
      '<button class="flow-node" data-i="'+i+'"><b>'+x[0]+'</b><span>'+x[1]+'</span></button>').join('')+
      '</div><div class="flow-detail">상자를 눌러 단계별 흐름을 확인하세요.</div></div>';
    one.after(sec);
    const detail=sec.querySelector('.flow-detail');
    sec.querySelectorAll('.flow-node').forEach(b=>b.onclick=()=>{
      const x=f[Number(b.dataset.i)]; detail.innerHTML='<b style="color:var(--accent2)">'+x[0]+'</b> · '+x[1];
    });

    const conceptSection=[...chapterEl.querySelectorAll('.section')].find(s=>s.querySelector('h3')?.textContent==='핵심 개념');
    if(conceptSection){
      const fl=document.createElement('section'); fl.className='section';
      fl.innerHTML='<h3>플래시카드</h3><p style="color:var(--muted)">카드를 눌러 설명을 펼치세요.</p><div class="flash-grid">'+
        c.concepts.map(([t,d])=>'<div class="flash"><b>'+t+'</b><div class="back">'+d+'</div></div>').join('')+'</div>';
      conceptSection.after(fl);
      fl.querySelectorAll('.flash').forEach(card=>card.onclick=()=>card.classList.toggle('open'));
    }

    const pre=chapterEl.querySelector('pre');
    if(pre){
      const row=document.createElement('div');row.className='copy-row';row.innerHTML='<button class="copy-btn">코드 복사</button>';pre.before(row);
      row.querySelector('button').onclick=async()=>{try{await navigator.clipboard.writeText(pre.innerText);row.querySelector('button').textContent='복사됨 ✓';setTimeout(()=>row.querySelector('button').textContent='코드 복사',1200)}catch{}};
    }

    const quiz=chapterEl.querySelector('.quiz');
    if(quiz){
      [...quiz.children].forEach((q,i)=>{
        const h=c.concepts[i%c.concepts.length];
        q.insertAdjacentHTML('beforeend','<br><button class="hint-btn">힌트 보기</button><div class="hint"><b>'+h[0]+'</b> — '+h[1]+'</div>');
        const b=q.querySelector('.hint-btn'), d=q.querySelector('.hint');
        b.onclick=()=>{d.classList.toggle('show');b.textContent=d.classList.contains('show')?'힌트 숨기기':'힌트 보기'};
      });
    }

    const head=chapterEl.querySelector('.chapter-head > div:first-child');
    if(head){
      const t=document.createElement('div');t.className='extra-tools';
      t.innerHTML='<button class="map-now">학습지도</button><button class="gloss-now">개념 사전</button><button class="print-now">이 장 인쇄</button>';
      head.appendChild(t);
      t.querySelector('.map-now').onclick=()=>{renderMap();document.getElementById('studyMapModal').classList.add('open')};
      t.querySelector('.gloss-now').onclick=()=>{renderGlossary();document.getElementById('glossaryModal').classList.add('open')};
      t.querySelector('.print-now').onclick=()=>window.print();
    }
  }

  ensureModals(); addGlobalTools();
  const baseRender=renderChapter;
  renderChapter=function(n){baseRender(n);augment(chapters.find(c=>c.n===n)||chapters[0]);renderMap();};
  augment(chapters.find(c=>c.n===current)||chapters[0]);

  window.addEventListener('keydown',e=>{
    const open=document.querySelector('.modal.open');
    if(open){if(e.key==='Escape')open.classList.remove('open');return;}
    if(e.target.matches('input,textarea')) return;
    if(e.key==='ArrowLeft') go(current-1);
    if(e.key==='ArrowRight') go(current+1);
  });
})();
