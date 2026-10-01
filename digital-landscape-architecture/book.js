/* Book navigation, local figure zoom and source-text search. No tracking/storage. */
(() => {
  'use strict';
  const base = '/digital-landscape-architecture/';
  const $ = q => document.querySelector(q);
  const $$ = q => Array.from(document.querySelectorAll(q));
  const dialogs = $$('dialog');
  const openDialog = d => typeof d.showModal === 'function' ? d.showModal() : d.setAttribute('open','');
  const closeDialog = d => typeof d.close === 'function' ? d.close() : d.removeAttribute('open');
  $$('[data-close]').forEach(b => b.addEventListener('click', () => closeDialog(document.getElementById(b.dataset.close))));
  dialogs.forEach(d => d.addEventListener('click', e => {
    if (e.target !== d) return;
    const r = d.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) closeDialog(d);
  }));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') { dialogs.filter(d=>d.open).forEach(closeDialog); $$('.mobile-toc').forEach(d=>d.open=false); }
  });
  $$('.mobile-toc a').forEach(a => a.addEventListener('click', () => a.closest('details.mobile-toc').open = false));
  let readingSize = 18;
  $$('[data-size]').forEach(b => b.addEventListener('click', () => {
    readingSize = Math.min(24, Math.max(16, readingSize + Number(b.dataset.size)));
    document.documentElement.style.setProperty('--reading-size', `${readingSize}px`);
    $$('[data-size]').forEach(control => { control.disabled = (Number(control.dataset.size)<0 && readingSize===16) || (Number(control.dataset.size)>0 && readingSize===24); });
  }));
  $$('[data-zoom]').forEach(a => a.addEventListener('click', e => {
    if (e.ctrlKey || e.metaKey || e.shiftKey || e.altKey) return;
    const figure = a.closest('figure');
    const img = figure.querySelector('img');
    if (!img) return;
    e.preventDefault();
    $('#large-figure').src = img.src;
    $('#large-figure').alt = img.alt;
    $('#figure-description').textContent = img.alt;
    $('#figure-label').textContent = figure.querySelector('.figure-meta span').textContent;
    $('#figure-file').href = img.src;
    openDialog($('#figure-viewer'));
    $('.figure-full').scrollLeft = 0;
    $('.figure-full').scrollTop = 0;
  }));
  let searchData = null, searchPromise = null, timer = null, queryVersion = 0;
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase('ko-KR');
  async function loadSearch() {
    if (searchData) return searchData;
    if (!searchPromise) {
      searchPromise = fetch(base+'search-index.json?v=20261002-book-1', {credentials:'same-origin'})
        .then(r=>{if(!r.ok)throw new Error('search response');return r.json();})
        .then(data=>{
          if(!Array.isArray(data))throw new Error('search format');
          searchData=data.map(x=>({...x,normalized:normalize(x.chapter_title+' '+x.title+' '+x.text)}));
          return searchData;
        }).catch(e=>{searchPromise=null;throw e;});
    }
    return searchPromise;
  }
  function addMarkedText(parent, text, tokens) {
    const normalized = normalize(text);
    let best = -1, term = '';
    for (const token of tokens) {
      const i = normalized.indexOf(token);
      if (i>=0 && (best<0 || i<best)) { best=i;term=token; }
    }
    if(best<0) {parent.textContent=text;return;}
    parent.append(document.createTextNode(text.slice(0,best)));
    const mark=document.createElement('mark');mark.textContent=text.slice(best,best+term.length);parent.append(mark,document.createTextNode(text.slice(best+term.length)));
  }
  async function search() {
    const version=++queryVersion;
    const value=$('#search-query').value.trim();
    const status=$('#search-status'), results=$('#search-results');
    results.replaceChildren();
    if(!value) {status.textContent='검색어를 입력하세요. 원고의 63개 집필 단위에서 찾습니다.';return;}
    status.textContent='본문에서 찾는 중입니다…';
    try {
      const data=await loadSearch();
      if(version!==queryVersion)return;
      const terms=normalize(value).split(/\s+/).filter(Boolean);
      const found=data.filter(x=>terms.every(t=>x.normalized.includes(t))).map(x=>({...x,score:terms.reduce((sum,t)=>sum+(normalize(x.title).includes(t)?4:0)+(normalize(x.chapter_title).includes(t)?2:0),0)})).sort((a,b)=>b.score-a.score||a.chapter-b.chapter);
      status.textContent=found.length ? `${found.length}개 집필 단위에서 찾았습니다${found.length>40?' · 앞의 40개를 표시합니다':''}.` : '일치하는 본문이 없습니다. 용어를 짧게 바꾸어 검색하세요.';
      found.slice(0,40).forEach(item=>{
        const li=document.createElement('li'),a=document.createElement('a'),small=document.createElement('small'),strong=document.createElement('strong'),excerpt=document.createElement('p');
        a.href=item.url;
        small.textContent=`${String(item.chapter).padStart(2,'0')}장 · ${item.chapter_title}`;
        strong.textContent=item.title;
        const position=terms.map(t=>normalize(item.text).indexOf(t)).filter(i=>i>=0).sort((a,b)=>a-b)[0] || 0;
        const start=Math.max(0,position-45),end=Math.min(item.text.length,start+190);
        addMarkedText(excerpt,(start?'…':'')+item.text.slice(start,end)+(end<item.text.length?'…':''),terms);
        a.append(small,strong,excerpt);li.append(a);results.append(li);
      });
    } catch (_) { if(version===queryVersion)status.textContent='검색 색인을 불러오지 못했습니다. 잠시 후 다시 검색하거나 전체 목차를 이용하세요.'; }
  }
  $$('.search-open').forEach(b=>b.addEventListener('click',()=>{
    const menu=$('.mobile-toc');if(menu)menu.open=false;
    openDialog($('#book-search'));
    $('#search-query').focus();
    search();
  }));
  $('#search-query').addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(search,140);});
  const reading=$('#reading'),bar=$('.reading-progress');
  let frame=null;
  function updateProgress() {
    frame=null;if(!reading)return;
    const bounds=reading.getBoundingClientRect(),available=Math.max(1,bounds.height-window.innerHeight+100);
    const progress=Math.min(1,Math.max(0,(100-bounds.top)/available));
    bar.style.transform=`scaleX(${progress})`;
  }
  if(reading) {
    const schedule=()=>{if(frame===null)frame=requestAnimationFrame(updateProgress);};
    window.addEventListener('scroll',schedule,{passive:true});window.addEventListener('resize',schedule);updateProgress();
    if('IntersectionObserver' in window) {
      const observer=new IntersectionObserver(entries=>{
        const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>a.boundingClientRect.top-b.boundingClientRect.top);
        if(!visible.length)return;
        const id=visible[0].target.id;
        $$('.unit-nav a').forEach(a=>{if(a.hash==='#'+id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});
      },{rootMargin:'-100px 0px -65% 0px',threshold:0});
      $$('#reading h2[id],#reading h3[id]').forEach(h=>observer.observe(h));
    }
  }
})();
