/* Original educational model. No real site data, tracking, API keys or book text. */
(() => {
  'use strict';
  const $ = (q, root = document) => root.querySelector(q);
  const $$ = (q, root = document) => Array.from(root.querySelectorAll(q));
  const svgNS = 'http://www.w3.org/2000/svg';
  const themeButton = $('#dw-theme');
  function themeLabel() {
    const dark = document.documentElement.dataset.dwTheme !== 'light';
    themeButton.textContent = dark ? '밝게' : '어둡게';
    themeButton.setAttribute('aria-label', dark ? '읽기 화면 밝게 전환' : '읽기 화면 어둡게 전환');
    const meta = $('meta[name="theme-color"]');
    if (meta) meta.content = dark ? '#111713' : '#f2f3ec';
  }
  themeButton.addEventListener('click', () => {
    const next = document.documentElement.dataset.dwTheme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.dwTheme = next;
    try { localStorage.setItem('dwn-theme', next); } catch (_) { /* Reading works without storage. */ }
    themeLabel();
  });
  themeLabel();

  // Abstract topographic linework, designed here rather than traced from a source.
  const terrain = $('#dw-terrain-lines');
  for (let j = 0; j < 21; j++) {
    let d = '';
    for (let i = 0; i <= 70; i++) {
      const x = 35 + i * 6.65;
      const y = 110 + j * 9.1 + 21 * Math.sin(i / 9 + j / 8) - 60 * Math.exp(-Math.pow((i - 42) / 16, 2)) * Math.sin(j / 12 + .5);
      d += `${i ? 'L' : 'M'}${x.toFixed(1)} ${y.toFixed(1)} `;
    }
    const p = document.createElementNS(svgNS, 'path');
    p.setAttribute('d', d);
    p.setAttribute('opacity', String(.22 + j / 35));
    terrain.appendChild(p);
  }

  const weights = ['water', 'heat', 'habitat'];
  const defaults = [45, 30, 25];
  const labels = {combined: '중첩', water: '물', heat: '열', habitat: '연결'};
  const gaussian = (x, y, cx, cy, sx, sy) => Math.exp(-((x-cx)**2/(2*sx**2)+(y-cy)**2/(2*sy**2)));
  const clamp = n => Math.min(1, Math.max(0, n));
  const cols = 18, rows = 12;
  const cells = [];
  let layer = 'combined', selected = 7 * cols + 11;
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const river = 8.3 + 2.1 * Math.sin(y / 2.5);
      const missing = x >= 15 && y <= 2;
      const excluded = Math.abs(x - river) < .65 || ((x-2)**2+(y-2)**2 < 3);
      const data = {
        x, y, missing, excluded,
        water: clamp(.12+.77*Math.exp(-((x-river)**2)/9)*(.5+y/22)),
        heat: clamp(.13+.85*gaussian(x,y,14,3,4,3)),
        habitat: clamp(.1+.87*gaussian(x,y,4,8,4.3,2.5))
      };
      const rect = document.createElementNS(svgNS, 'rect');
      const index = cells.length;
      Object.entries({x:x*30+1,y:y*30+1,width:28,height:28,rx:2,role:'button',tabindex:index===selected?0:-1}).forEach(([k,v]) => rect.setAttribute(k,String(v)));
      rect.addEventListener('click', () => choose(index, false));
      rect.addEventListener('keydown', event => {
        let next = index;
        if (event.key === 'ArrowRight') next = Math.min(cols*rows-1,index+1);
        else if (event.key === 'ArrowLeft') next = Math.max(0,index-1);
        else if (event.key === 'ArrowDown') next = Math.min(cols*rows-1,index+cols);
        else if (event.key === 'ArrowUp') next = Math.max(0,index-cols);
        else if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); choose(index,false); return; }
        else return;
        event.preventDefault(); choose(next,true);
      });
      data.rect = rect;
      cells.push(data);
      $('#dw-cells').appendChild(rect);
    }
  }
  function currentWeights() { return weights.map(k => Number($('#dw-'+k).value)); }
  function score(c, w) {
    if (c.missing || c.excluded) return null;
    if (layer !== 'combined') return c[layer];
    const sum = w.reduce((a,b) => a+b,0);
    return sum ? weights.reduce((s,k,i) => s+c[k]*w[i],0)/sum : null;
  }
  function color(value) {
    const a = [37,62,50], b = [184,212,155];
    return `rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*value)).join(',')})`;
  }
  function describe() {
    const c = cells[selected], w = currentWeights(), value = score(c,w);
    const readout = $('#dw-readout');
    readout.replaceChildren();
    const heading = document.createElement('b');
    heading.textContent = `선택 위치 · ${c.x+1}열 ${c.y+1}행`;
    readout.append(heading,document.createElement('br'));
    if (c.missing) { readout.append('자료 부족 구간입니다. 값이 0이라는 뜻이 아니며, 비교값을 산출하지 않습니다.'); return; }
    if (c.excluded) { readout.append('하천 또는 기존 서식처 핵심구간으로 가정한 셀입니다. 신규 시설 개입 비교에서 제외합니다. 보전·관리의 필요가 없다는 뜻은 아닙니다.'); return; }
    readout.append(`물 ${Math.round(c.water*100)} · 열 ${Math.round(c.heat*100)} · 연결 ${Math.round(c.habitat*100)}`,document.createElement('br'));
    readout.append(value === null ? '가중치 합계가 0이므로 중첩값을 산출하지 않습니다.' : `${labels[layer]} 검토 지수 ${Math.round(value*100)} / 100`);
    readout.append(document.createElement('br'),'모든 값은 학습을 위해 생성한 가상 수치입니다.');
  }
  function choose(index, focus) {
    cells[selected].rect.setAttribute('tabindex','-1');
    cells[selected].rect.classList.remove('selected');
    selected = index;
    cells[selected].rect.setAttribute('tabindex','0');
    cells[selected].rect.classList.add('selected');
    if (focus) cells[selected].rect.focus();
    describe();
  }
  function render() {
    const w = currentWeights(), sum = w.reduce((a,b)=>a+b,0);
    weights.forEach((key,i) => { $('#dw-'+key+'-out').value = String(w[i]); });
    cells.forEach(c => {
      const value = score(c,w);
      const fill = c.missing ? 'url(#dw-missing)' : c.excluded ? '#151d17' : value === null ? '#505b50' : color(value);
      c.rect.setAttribute('fill', fill);
      const desc = c.missing ? '자료 부족' : c.excluded ? '개입 제외 가정' : value === null ? '가중치 미설정' : `${labels[layer]} 검토 지수 ${Math.round(value*100)}`;
      c.rect.setAttribute('aria-label',`${c.x+1}열 ${c.y+1}행, ${desc}`);
    });
    $('#dw-lab-status').textContent = layer !== 'combined' ? `${labels[layer]} 단일 지수 표시 중 · 가중치는 중첩 화면에 적용됩니다.` : sum ? `정규화 비중: 물 ${Math.round(w[0]/sum*100)}% · 열 ${Math.round(w[1]/sum*100)}% · 연결 ${Math.round(w[2]/sum*100)}% (반올림)` : '하나 이상의 가중치를 0보다 크게 설정하세요.';
    choose(selected,false);
  }
  weights.forEach(k => $('#dw-'+k).addEventListener('input',render));
  $$('[data-layer]').forEach(button => button.addEventListener('click',() => {
    layer = button.dataset.layer;
    $$('[data-layer]').forEach(b => b.setAttribute('aria-pressed',String(b===button)));
    render();
  }));
  $('#dw-reset').addEventListener('click',() => {
    weights.forEach((k,i) => { $('#dw-'+k).value=defaults[i]; });
    layer='combined';
    $$('[data-layer]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.layer===layer)));
    render();
  });
  render();

  $$('[data-filter]').forEach(button => button.addEventListener('click',() => {
    const topic=button.dataset.filter;
    $$('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
    let count=0;
    $$('.dw-solution').forEach(card=>{card.hidden=topic!=='all'&&card.dataset.topic!==topic;if(!card.hidden)count++;});
    $('#dw-filter-status').textContent=`${button.textContent} · ${count}개 항목`;
  }));

  const key='dwn-notebook-v1';
  const form=$('#dw-note-form');
  const fields=$$('textarea',form);
  const status=$('#dw-save-status');
  try {
    const saved=JSON.parse(localStorage.getItem(key)||'null');
    if(saved&&saved.version===1&&saved.notes&&typeof saved.notes==='object') {
      fields.forEach(f=>{if(typeof saved.notes[f.name]==='string')f.value=saved.notes[f.name].slice(0,6000);});
      status.textContent='이 브라우저에 저장한 노트를 불러왔습니다. 수정한 뒤 다시 저장하세요.';
    }
  } catch (_) { /* A damaged or unavailable store must never prevent reading. */ }
  form.addEventListener('submit',e=>e.preventDefault());
  form.addEventListener('input',()=>{status.textContent='수정 중 · 변경 내용은 아직 저장하지 않았습니다. 서버로 전송하지 않습니다.';});
  const getNotes=()=>Object.fromEntries(fields.map(f=>[f.name,f.value]));
  $('#dw-save').addEventListener('click',()=>{
    try {
      localStorage.setItem(key,JSON.stringify({version:1,updatedAt:new Date().toISOString(),notes:getNotes()}));
      status.textContent='이 브라우저에 저장했습니다. 다른 기기로 전송하거나 동기화하지 않습니다.';
    } catch (_) { status.textContent='브라우저 저장소를 사용할 수 없습니다. 노트 내려받기로 기록을 보관하세요.'; }
  });
  $('#dw-clear').addEventListener('click',()=>{
    if(!window.confirm('입력한 노트와 이 기기에 저장된 노트를 모두 지울까요?'))return;
    fields.forEach(f=>{f.value='';});
    try {localStorage.removeItem(key);status.textContent='입력한 노트와 이 기기에 저장한 노트를 지웠습니다.';}
    catch (_) {status.textContent='화면의 노트는 지웠습니다. 저장소 접근이 차단되어 저장 내용 삭제 여부는 확인할 수 없습니다.';}
  });
  $('#dw-export').addEventListener('click',()=>{
    const titles=['대상지와 해결하려는 문제','작동하는 자연의 과정','개입과 대안','사람과 생물다양성','자료와 불확실성','검증과 운영'];
    const text='# 자연기반해법 대상지 검토노트\n\n출처: https://navicoby.github.io/designwnature/\n작성일: '+new Date().toLocaleDateString('ko-KR')+'\n\n독립적인 학습용 기록입니다. 공식 NbS 적합성 평가나 인증이 아닙니다.\n\n'+fields.map((f,i)=>`## ${i+1}. ${titles[i]}\n\n${f.value||'(미작성)'}\n`).join('\n');
    const url=URL.createObjectURL(new Blob([text],{type:'text/markdown;charset=utf-8'}));
    const a=document.createElement('a');a.href=url;a.download='designwnature-field-notes.md';document.body.append(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1500);
    status.textContent='노트 파일을 만들었습니다. 이 동작은 브라우저 저장과 별개입니다.';
  });
  $('#dw-print').addEventListener('click',()=>window.print());

  $$('.dw-mobile-menu nav a').forEach(link=>link.addEventListener('click',()=>{link.closest('details').open=false;}));
  const sideLinks=$$('.dw-sidebar nav a');
  if('IntersectionObserver' in window) {
    const observer=new IntersectionObserver(entries=>{
      const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>a.boundingClientRect.top-b.boundingClientRect.top);
      if(!visible.length)return;
      sideLinks.forEach(a=>{
        if(a.hash==='#'+visible[0].target.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');
      });
    },{rootMargin:'-90px 0px -60% 0px',threshold:0});
    $$('.dw-section').forEach(s=>observer.observe(s));
  }
})();
