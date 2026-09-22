(() => {
  const drills = (window.DRILLS || []).slice().sort((a,b)=>a.id-b.id);
  const $ = s => document.querySelector(s);
  const list = $("#drillList"), hero = $("#hero"), lesson = $("#lesson");
  const storageKey = "cpp100drills:v1";
  const recallKey = "cpp100drills:recall:v1";
  const lastKey = "cpp100drills:last";
  const themeKey = "cpp100drills:theme";
  let done = new Set(JSON.parse(localStorage.getItem(storageKey) || "[]"));
  let recalls = new Set(JSON.parse(localStorage.getItem(recallKey) || "[]"));
  let current = null;

  function applyTheme(theme){
    const value = theme === "light" ? "light" : "dark";
    document.documentElement.dataset.theme = value;
    try { localStorage.setItem(themeKey,value); } catch (_) {}
    const meta=document.querySelector('meta[name="theme-color"]');
    if(meta) meta.setAttribute("content", value==="light" ? "#f7f8fa" : "#0b0d10");
    const btn=$("#themeToggle");
    if(btn){
      const isLight=value==="light";
      btn.textContent=isLight ? "☾ 어둡게" : "☀ 밝게";
      btn.setAttribute("aria-pressed",isLight ? "true" : "false");
      btn.title=isLight ? "어두운 배경으로 전환" : "밝은 배경으로 전환";
    }
  }

  function initTheme(){
    let theme=document.documentElement.dataset.theme;
    if(theme!=="light" && theme!=="dark") theme="dark";
    applyTheme(theme);
  }

  const pad = n => String(n).padStart(3,"0");
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const fmt = s => "<p>" + esc(s).replace(/\`([^\`]+)\`/g,"<code>$1</code>").replace(/\n/g,"</p><p>") + "</p>";
  const save = () => {
    localStorage.setItem(storageKey, JSON.stringify([...done]));
    localStorage.setItem(recallKey, JSON.stringify([...recalls]));
  };

  function updateProgress(){
    const n=done.size, pct=Math.round(n/drills.length*100);
    $("#sideProgressText").textContent=`${n} / ${drills.length}`;
    $("#sideProgressFill").style.width=pct+"%";
    $("#heroPercent").textContent=pct+"%";
    $("#continueBtn").textContent=n===drills.length ? "100개 다시 보기" : "이어서 하기";
  }

  function fillPartFilter(){
    const parts=[...new Map(drills.map(d=>[d.part,d.partTitle])).entries()];
    for(const [p,t] of parts){
      const o=document.createElement("option"); o.value=p; o.textContent=`${p} · ${t}`;
      $("#partFilter").appendChild(o);
    }
  }

  function renderList(){
    const q=$("#searchInput").value.trim().toLowerCase();
    const pf=$("#partFilter").value, sf=$("#statusFilter").value;
    const filtered=drills.filter(d=>{
      const match=!q || `${d.id} ${d.title} ${d.goal} ${d.partTitle}`.toLowerCase().includes(q);
      const part=pf==="all" || d.part===pf;
      const status=sf==="all" || (sf==="done" ? done.has(d.id) : !done.has(d.id));
      return match && part && status;
    });
    list.innerHTML="";
    if(!filtered.length){ list.innerHTML='<div class="empty">조건에 맞는 Drill이 없습니다.</div>'; return; }
    let prevPart="";
    for(const d of filtered){
      if(d.part!==prevPart){
        const label=document.createElement("div"); label.className="part-label";
        label.textContent=`${d.part} · ${d.partTitle}`; list.appendChild(label); prevPart=d.part;
      }
      const b=document.createElement("button");
      b.className="drill-item"+(done.has(d.id)?" done":"")+(current===d.id?" active":"");
      b.innerHTML=`<span class="num">${pad(d.id)}</span><span class="title">${esc(d.title)}</span><span class="state">${done.has(d.id)?"✓":"·"}</span>`;
      b.addEventListener("click",()=>openDrill(d.id));
      list.appendChild(b);
    }
  }

  function openDrill(id, pushHash=true){
    const d=drills.find(x=>x.id===id); if(!d) return;
    current=id; localStorage.setItem(lastKey,String(id));
    hero.classList.add("hidden"); lesson.classList.remove("hidden");
    $("#lessonPart").textContent=`${d.part} · ${d.partTitle}`;
    $("#lessonNumber").textContent=`DRILL ${pad(d.id)} / 100`;
    $("#lessonTitle").textContent=d.title;
    $("#lessonGoal").textContent=d.goal;
    $("#lessonConcept").innerHTML=d.concept;
    $("#codeBlock").textContent=d.code;
    $("#compileCommand").textContent="$ "+d.compile;
    $("#breakIt").innerHTML=fmt(d.breakIt);
    $("#observe").innerHTML=fmt(d.observe);
    $("#challenge").innerHTML=fmt(d.challenge);
    $("#hint").innerHTML=fmt(d.hint);
    $("#answerBlock").textContent=d.answer;
    const complete=$("#completeBtn");
    complete.classList.toggle("done",done.has(id));
    complete.setAttribute("aria-pressed",done.has(id)?"true":"false");
    complete.innerHTML=done.has(id)?"<span>✓</span> 완료됨":"<span>✓</span> 완료";
    $("#recallCheck").checked=recalls.has(id);
    $("#lessonPrev").disabled=id===1; $("#prevBtn").disabled=id===1;
    $("#lessonNext").disabled=id===drills.length; $("#nextBtn").disabled=id===drills.length;
    $("#lessonNext").textContent=id===drills.length?"100 DRILLS COMPLETE":"다음 Drill →";
    if(pushHash && location.hash!==`#drill-${pad(id)}`) history.pushState(null,"",`#drill-${pad(id)}`);
    renderList(); closeSidebar(); window.scrollTo({top:0,behavior:"smooth"});
  }

  function showHome(){
    current=null; lesson.classList.add("hidden"); hero.classList.remove("hidden");
    renderList(); history.pushState(null,"",location.pathname);
    window.scrollTo({top:0,behavior:"smooth"});
  }

  function toggleComplete(){
    if(!current) return;
    if(done.has(current)) done.delete(current); else done.add(current);
    save(); updateProgress(); openDrill(current,false);
  }

  function nextIncomplete(){
    const d=drills.find(x=>!done.has(x.id)) || drills[0];
    openDrill(d.id);
  }

  function copyTarget(id,btn){
    const el=document.getElementById(id); if(!el) return;
    navigator.clipboard.writeText(el.textContent).then(()=>{
      const old=btn.textContent; btn.textContent="Copied"; btn.classList.add("copied");
      setTimeout(()=>{btn.textContent=old;btn.classList.remove("copied")},1200);
    });
  }

  function openSidebar(){ $("#sidebar").classList.add("open"); $("#scrim").classList.add("show"); }
  function closeSidebar(){ $("#sidebar").classList.remove("open"); $("#scrim").classList.remove("show"); }

  $("#themeToggle").addEventListener("click",()=>{
    const currentTheme=document.documentElement.dataset.theme==="light" ? "light" : "dark";
    applyTheme(currentTheme==="light" ? "dark" : "light");
  });
  $("#completeBtn").addEventListener("click",toggleComplete);
  $("#recallCheck").addEventListener("change",e=>{
    if(!current)return; if(e.target.checked) recalls.add(current); else recalls.delete(current); save();
  });
  $("#startBtn").addEventListener("click",()=>openDrill(1));
  $("#continueBtn").addEventListener("click",()=>{
    const last=Number(localStorage.getItem(lastKey));
    if(last && !done.has(last)) openDrill(last); else nextIncomplete();
  });
  $("#randomBtn").addEventListener("click",()=>{
    const pool=drills.filter(d=>!done.has(d.id)); const src=pool.length?pool:drills;
    openDrill(src[Math.floor(Math.random()*src.length)].id);
  });
  $("#resetBtn").addEventListener("click",()=>{
    if(confirm("100개 Drill의 완료 기록과 recall 기록을 초기화할까요?")){
      done.clear(); recalls.clear(); save(); updateProgress(); renderList();
      if(current) openDrill(current,false);
    }
  });
  ["searchInput","partFilter","statusFilter"].forEach(id=>{
    $("#"+id).addEventListener(id==="searchInput"?"input":"change",renderList);
  });
  $("#lessonPrev").addEventListener("click",()=>current>1&&openDrill(current-1));
  $("#lessonNext").addEventListener("click",()=>current<drills.length&&openDrill(current+1));
  $("#prevBtn").addEventListener("click",()=>current>1&&openDrill(current-1));
  $("#nextBtn").addEventListener("click",()=>current&&current<drills.length?openDrill(current+1):openDrill(1));
  document.querySelectorAll("[data-copy]").forEach(b=>b.addEventListener("click",()=>copyTarget(b.dataset.copy,b)));
  $("#openSidebar").addEventListener("click",openSidebar); $("#closeSidebar").addEventListener("click",closeSidebar); $("#scrim").addEventListener("click",closeSidebar);
  document.querySelector(".brand-mark").addEventListener("click",e=>{e.preventDefault();showHome();});

  window.addEventListener("popstate",()=>{
    const m=location.hash.match(/drill-(\d+)/);
    if(m) openDrill(Number(m[1]),false); else { current=null; lesson.classList.add("hidden"); hero.classList.remove("hidden"); renderList(); }
  });
  document.addEventListener("keydown",e=>{
    if(["INPUT","SELECT","TEXTAREA"].includes(document.activeElement.tagName)) return;
    if(e.key==="ArrowLeft" && current>1) openDrill(current-1);
    if(e.key==="ArrowRight" && current<drills.length) openDrill(current+1);
  });

  initTheme(); fillPartFilter(); updateProgress(); renderList();
  if(drills.length!==100){
    console.warn(`Expected 100 drills, loaded ${drills.length}`);
  }
  const m=location.hash.match(/drill-(\d+)/);
  if(m) openDrill(Number(m[1]),false);
})();