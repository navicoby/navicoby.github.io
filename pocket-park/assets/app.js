(() => {
  'use strict';
  const model = window.PARK_MODEL;
  if (!model) return;
  const $ = id => document.getElementById(id);
  const objects = new Map(model.objects.map(o => [o.object_id, o]));
  const tasks = new Map(model.tasks.map(t => [t.task_id, t]));
  const outputs = new Map();
  model.tasks.forEach(t => t.output_object_ids.forEach(id => outputs.set(id, t)));
  const shapes = Array.from(document.querySelectorAll('#process-map [data-object]'));
  const rows = Array.from(document.querySelectorAll('.task-table tbody tr'));
  const endDay = model.endHours / 24;
  let currentHour = 0, stageMode = false, timer = null, selectedObject = null, linkedFilter = null;
  const units = {ea:'개',m:'m',m2:'㎡',m3:'㎥'};
  const dateText = hour => new Intl.DateTimeFormat('ko-KR', {timeZone:'Asia/Seoul',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date(Date.parse(model.start) + hour * 3600000));
  function state(task) { return currentHour >= task.finish - 1e-7 ? 'done' : currentHour >= task.start - 1e-7 ? 'active' : 'pending'; }
  function fact(name,value) { const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=name;dd.textContent=value;$('object-facts').append(dt,dd); }
  function selectObject(id) {
    const o=objects.get(id); if (!o) return;
    selectedObject=id;
    shapes.forEach(el=>el.classList.toggle('selected',el.dataset.object===id));
    $('object-title').textContent=o.name;
    $('object-detail').textContent=o.specification || 'R1 공간 객체';
    $('object-facts').replaceChildren();
    fact('객체 ID',o.object_id);
    fact('수량',new Intl.NumberFormat('ko-KR',{maximumFractionDigits:2}).format(o.quantity)+' '+(o.kind.includes('tree')||o.kind==='shrub_plant'?'주':units[o.unit]||o.unit));
    if(o.kind==='pipe') { const p=model.drainageLevels.pipes.find(p=>p.object_id===o.object_id); if(p){fact('상류 → 하류 관저고',p.upstream_invert_m.toFixed(3)+' → '+p.downstream_invert_m.toFixed(3)+' m');fact('관로 구배',p.slope_percent.toFixed(1)+'%');fact('고도 기준','가상 TBM 100.000m');} }
    if(o.kind==='chamber') { const n=model.drainageLevels.nodes.find(n=>'CHAMBER_'+n.node_id===o.object_id); if(n){fact('관저고',n.invert_level_m.toFixed(3)+' m');fact('고도 기준','가상 TBM 100.000m');} }
    fact('대표 WBS',o.primary_wbs || '참고 객체');
    fact('연결 작업',o.task_ids.length+'개');
    fact('IFC GUID',o.ifc_guid);
    const output=outputs.get(id);
    if(output) fact('시공 상태',({done:'완료',active:'진행 중',pending:'예정'})[state(output)]);
    $('show-linked').hidden=!o.task_ids.length;
  }
  function updateStage() {
    shapes.forEach(el=>{
      const task=outputs.get(el.dataset.object),s=task?state(task):'existing';
      ['pending','active','done'].forEach(cls=>el.classList.toggle(cls,stageMode&&s===cls));
    });
    $('map-mode-title').textContent=stageMode?'시공 단계 · '+(currentHour/24).toFixed(2)+'일':'R1 · 완성 배치';
    $('toggle-stage').setAttribute('aria-pressed',String(stageMode));
    $('toggle-stage').textContent=stageMode?'완성 배치 보기':'공정 단계 표시';
    const zones=new Set();
    if(stageMode) model.tasks.filter(t=>state(t)==='active').forEach(t=>t.work_zones.forEach(z=>zones.add(z)));
    $('active-zones').replaceChildren();
    const rects={A:[0,0],B:[20,0],C:[0,25],D:[20,25]};
    zones.forEach(z=>{if(!rects[z])return;const r=document.createElementNS('http://www.w3.org/2000/svg','rect');r.setAttribute('x',rects[z][0]);r.setAttribute('y',rects[z][1]);r.setAttribute('width',20);r.setAttribute('height',25);$('active-zones').append(r);});
  }
  function render(day) {
    currentHour=Math.max(0,Math.min(model.endHours,day*24));
    $('time-slider').value=currentHour/24;
    $('day-number').textContent=(currentHour/24).toFixed(2);
    $('current-date').textContent=dateText(currentHour);
    const counts={done:0,active:0,pending:0};
    const active=[];
    model.tasks.forEach(t=>{const s=state(t);counts[s]++;if(s==='active')active.push(t);});
    $('done-count').textContent=counts.done;$('active-count').textContent=counts.active;$('planned-count').textContent=counts.pending;
    $('current-tasks').replaceChildren();
    if(!active.length){const li=document.createElement('li');li.textContent=counts.done===model.tasks.length?model.tasks.length+'개 작업 완료':'현재 진행 작업 없음';$('current-tasks').append(li);}
    active.forEach(t=>{const li=document.createElement('li');li.textContent=t.wbs_code+' · '+t.wbs_name;$('current-tasks').append(li);});
    const working=model.segments.some(s=>s.start<=currentHour&&s.finish>currentHour);
    $('work-state').textContent=counts.done===model.tasks.length?'전체 완료 · 조건부 기준 일정':working?'작업 또는 구역 이동 중':'휴무·대기 구간 · 작업 시작~종료 범위에는 비작업 시간도 포함';
    updateStage();
    if(selectedObject)selectObject(selectedObject);
  }
  function stop() { if(timer){clearInterval(timer);timer=null;} $('play').textContent='▶ 재생';$('play').setAttribute('aria-pressed','false'); }
  function filterTasks() {
    const q=$('task-search').value.trim().toLowerCase(),category=$('task-category').value;
    let shown=0;
    rows.forEach(row=>{const id=row.querySelector('[data-task]').dataset.task,t=tasks.get(id);const ok=(!q||row.textContent.toLowerCase().includes(q))&&(!category||t.wbs_code.split('.')[1]===category)&&(!linkedFilter||linkedFilter.has(id));row.hidden=!ok;if(ok)shown++;});
    $('table-count').textContent=(linkedFilter?'선택 객체의 연결 작업 · ':'')+shown+'개 작업'+(shown===0?' · 검색 조건을 바꾸거나 초기화하세요':'');
  }
  function clearFilters(){linkedFilter=null;$('task-search').value='';$('task-category').value='';filterTasks();}
  shapes.forEach(el=>{
    el.addEventListener('click',()=>selectObject(el.dataset.object));
    el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();selectObject(el.dataset.object);}});
  });
  $('time-slider').addEventListener('input',e=>{stop();stageMode=true;const value=Number(e.target.value);render(value>endDay-.025?endDay:value);});
  $('toggle-stage').addEventListener('click',()=>{stageMode=!stageMode;updateStage();});
  $('to-start').addEventListener('click',()=>{stop();stageMode=true;render(0);});
  $('to-end').addEventListener('click',()=>{stop();stageMode=true;render(endDay);});
  $('play').addEventListener('click',()=>{
    if(timer){stop();return;}
    if(currentHour>=model.endHours)render(0);
    stageMode=true;$('play').textContent='Ⅱ 일시정지';$('play').setAttribute('aria-pressed','true');
    timer=setInterval(()=>{render(Math.min(endDay,currentHour/24+.25));if(currentHour>=model.endHours)stop();},350);
  });
  document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});
  $('show-linked').addEventListener('click',()=>{
    const o=objects.get(selectedObject);if(!o)return;
    $('task-search').value='';$('task-category').value='';linkedFilter=new Set(o.task_ids);filterTasks();
    $('task-search').focus({preventScroll:true});$('wbs').scrollIntoView({behavior:'auto',block:'start'});
  });
  $('task-search').addEventListener('input',()=>{linkedFilter=null;filterTasks();});
  $('task-category').addEventListener('change',()=>{linkedFilter=null;filterTasks();});
  $('clear-filter').addEventListener('click',clearFilters);
  document.querySelectorAll('.task-select').forEach(button=>button.addEventListener('click',()=>{
    const t=tasks.get(button.dataset.task);stop();stageMode=true;render(t.start/24);
    if(t.output_object_ids.length)selectObject(t.output_object_ids[0]);
    else{selectedObject=null;shapes.forEach(el=>el.classList.remove('selected'));$('object-title').textContent=t.wbs_name;$('object-detail').textContent='실행 작업 · '+t.wbs_code;$('object-facts').replaceChildren();fact('작업 ID',t.task_id);fact('작업 구역',t.work_zones.join(', '));fact('시작',dateText(t.start));fact('종료',dateText(t.finish));$('show-linked').hidden=true;}
    $('explorer').scrollIntoView({behavior:'auto',block:'start'});
  }));
  if('IntersectionObserver' in window){const links=Array.from(document.querySelectorAll('.contents a'));const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting)links.forEach(link=>{const active=link.hash==='#'+entry.target.id;link.classList.toggle('current',active);if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});});},{rootMargin:'-15% 0px -65% 0px'});links.forEach(link=>{const section=document.querySelector(link.hash);if(section)observer.observe(section);});}
  render(0);filterTasks();
})();
