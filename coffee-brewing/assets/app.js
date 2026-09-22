'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const recipes = {
    hot: {name:'기준 푸어오버', dose:15, ratio:16.67, temp:94, times:[0,40,75], finish:180, note:'94°C에서 시작 · 푸어오버용 분쇄 · 물 빠짐은 약 2:30~3:30을 참고합니다.'},
    kasuya: {name:'카스야 4:6', dose:20, ratio:15, temp:92, times:[0,45,90,130,160], finish:210, note:'92°C · 굵은 분쇄 · HARIO에 소개된 50·70·60·60·60g 주입의 비율을 적용합니다.'},
    iced: {name:'아이스 푸어오버', dose:15, ratio:15.33, temp:94, times:[0,30], finish:180, note:'93~95°C에서 시작 · 서버의 얼음을 먼저 계량합니다. 추가로 넣는 얼음은 별도로 기록하세요.'}
  };
  function brewPlan(mode, dose, ratio, icePercent = 39) {
    if (!recipes[mode] || !Number.isFinite(dose) || dose < 5 || dose > 60 || !Number.isFinite(ratio) || ratio < 10 || ratio > 20 || !Number.isFinite(icePercent) || icePercent < 20 || icePercent > 50) throw Error('원두는 5~60g, 배합비는 1:10~1:20, 얼음 비중은 20~50%로 입력하세요.');
    const total = Math.round(dose * ratio), ice = mode === 'iced' ? Math.round(total * icePercent / 100) : 0, hot = total - ice;
    const cumulative = mode === 'kasuya' ? [1/6,.4,.6,.8,1].map(x=>Math.round(hot*x)) : mode === 'iced' ? [Math.round(dose*2),hot] : [Math.round(dose*2),Math.round(hot*.6),hot];
    return {mode,dose,ratio,total,ice,hot,steps:cumulative.map((value,i)=>({at:recipes[mode].times[i],amount:value-(cumulative[i-1]||0),cumulative:value}))};
  }
  function hardness(ca,mg) { if(!Number.isFinite(ca)||!Number.isFinite(mg)||ca<0||mg<0||ca>1000||mg>1000) throw Error('칼슘과 마그네슘을 0~1,000mg/L 범위로 입력하세요.'); return 2.497*ca+4.118*mg; }
  function clock(ms) { const sec=Math.floor(ms/1000); return `${Math.floor(sec/60)}:${String(sec%60).padStart(2,'0')}`; }
  function numeric(id) { const el=$(id); return el.value.trim() === '' ? NaN : Number(el.value); }
  // Exposed only to the local build checks; the site sends no data to a server.
  if (typeof module !== 'undefined' && module.exports) { module.exports={brewPlan,hardness}; return; }
  const search=$('chapter-search');
  if(search) search.addEventListener('input',()=>{
    const q=search.value.trim().toLocaleLowerCase('ko'); let count=0;
    document.querySelectorAll('.chapter-row').forEach(row=>{const match=(row.textContent+' '+row.dataset.keywords).toLocaleLowerCase('ko').includes(q);row.hidden=!match;if(match)count++;});
    document.querySelectorAll('.chapter-group').forEach(group=>group.hidden=![...group.querySelectorAll('.chapter-row')].some(row=>!row.hidden));
    $('search-count').textContent=q?`${count}개의 글을 찾았습니다.`:'';
  });
  if ($('brew-form')) {
    let plan=null, running=false, elapsed=0, started=0, tick=null, lastStep='';
    const totalElapsed=()=>elapsed+(running?performance.now()-started:0);
    function paintTimer(){
      const ms=totalElapsed(); $('timer-time').textContent=clock(ms);
      if(!plan)return;
      const secs=ms/1000;
      let index=0; plan.steps.forEach((s,i)=>{if(secs>=s.at)index=i;});
      document.querySelectorAll('#schedule-body tr').forEach((row,i)=>row.classList.toggle('active',i===index));
      const step=plan.steps[index], next=plan.steps[index+1];
      const text=next?`지금: 누적 ${step.cumulative}g까지 · 다음 주입 ${clock(next.at*1000)}`:`마지막 주입: 누적 ${step.cumulative}g까지. 물 빠짐을 살피고 종료 시간을 기록하세요.`;
      if(text!==lastStep){$('timer-step').textContent=text;lastStep=text;}
    }
    function resetTimer(){running=false;clearInterval(tick);tick=null;elapsed=0;lastStep='';$('timer-start').textContent='시작';paintTimer();}
    function updatePlan(){
      resetTimer();
      try{
        plan=brewPlan($('recipe').value,numeric('dose'),numeric('ratio'),numeric('ice-percent'));
        $('brew-error').textContent='';$('brew-results').hidden=false;$('timer-start').disabled=false;
        $('result-total').textContent=`${plan.total}g`;
        $('result-detail').textContent=plan.ice?`뜨거운 물 ${plan.hot}g + 서버의 얼음 ${plan.ice}g · 원두 ${plan.dose}g`:`추출에 붓는 물의 총량 · 원두 ${plan.dose}g`;
        $('recipe-note').textContent=recipes[plan.mode].note;
        $('actual-ratio').textContent=`계량 기준 약 1:${(plan.total/plan.dose).toFixed(2)} · 1g 단위로 반올림`;
        $('schedule-body').replaceChildren();
        plan.steps.forEach(s=>{const tr=document.createElement('tr');[clock(s.at*1000),`+${s.amount}g`,`${s.cumulative}g`].forEach(t=>{const td=document.createElement('td');td.textContent=t;tr.append(td);});$('schedule-body').append(tr);});
        $('journal-link').href=`journal.html?${new URLSearchParams({method:plan.mode,dose:plan.dose,water:plan.hot,ice:plan.ice,temp:recipes[plan.mode].temp})}`;
        lastStep='';paintTimer();
      }catch(error){plan=null;$('brew-error').textContent=error.message;$('brew-results').hidden=true;$('timer-start').disabled=true;}
    }
    function setRecipe(){const r=recipes[$('recipe').value];$('dose').value=r.dose;$('ratio').value=r.ratio;$('ice-percent').value=39;$('ice-field').hidden=$('recipe').value!=='iced';updatePlan();}
    const requested=new URLSearchParams(location.search).get('recipe');if(recipes[requested])$('recipe').value=requested;
    $('recipe').addEventListener('change',setRecipe);
    ['dose','ratio','ice-percent'].forEach(id=>$(id).addEventListener('input',updatePlan));
    $('brew-form').addEventListener('submit',e=>e.preventDefault());
    $('timer-start').addEventListener('click',()=>{if(!plan)return;if(running){elapsed=totalElapsed();running=false;clearInterval(tick);$('timer-start').textContent='계속';}else{started=performance.now();running=true;$('timer-start').textContent='일시정지';tick=setInterval(paintTimer,200);}paintTimer();});
    $('timer-reset').addEventListener('click',resetTimer);
    document.addEventListener('visibilitychange',()=>{if(!document.hidden)paintTimer();});
    setRecipe();
    const calcWater=()=>{try{$('water-result').textContent=`약 ${hardness(numeric('calcium'),numeric('magnesium')).toFixed(1)} mg/L as CaCO₃`;}catch(error){$('water-result').textContent=error.message;}};
    ['calcium','magnesium'].forEach(id=>$(id).addEventListener('input',calcWater));calcWater();
    const tasteAdvice={sour:'덜 익은 과일처럼 시고 가볍다면, 다음 잔에서 분쇄를 한 단계 가늘게 해 보세요. 같은 원두·물·온도를 유지하고 향과 질감을 비교합니다. 원두 고유의 산미일 수도 있습니다.',bitter:'거칠고 떫은 느낌이 크다면, 다음 잔에서 과도한 스월이나 젓기를 줄여 보세요. 쓴맛이 로스팅에서 비롯됐는지도 확인합니다.',weak:'향과 맛은 괜찮지만 너무 연하다면, 원두를 고정하고 총 물을 조금 줄여 보세요. 배합비를 바꾸면 추출 상태도 함께 달라질 수 있습니다.',strong:'맛의 균형은 괜찮지만 너무 진하다면, 완성한 커피 일부에 뜨거운 물을 조금 더해 비교해 보세요. 더한 물의 무게도 기록합니다.',uneven:'매번 맛이 달라진다면, 먼저 주입량과 시작 시각을 같게 맞춰 보세요. 저울·분쇄 눈금·필터·물도 같은 조건인지 살핍니다.'};
    const updateTaste=()=>{$('taste-advice').textContent=tasteAdvice[$('taste').value];};$('taste').addEventListener('change',updateTaste);updateTaste();
  }
  if($('journal-form')) {
    const KEY='coffee-brewing:journal:v1'; let records=[], storageOK=true;
    const now=new Date();$('entry-date').value=`${now.getFullYear()}-${String(now.getMonth()+1).padStart(2,'0')}-${String(now.getDate()).padStart(2,'0')}`;
    const query=new URLSearchParams(location.search);
    if(recipes[query.get('method')])$('entry-method').value=query.get('method');
    [['dose','entry-dose',5,60],['water','entry-water',1,2000],['ice','entry-ice',0,2000],['temp','entry-temp',0,100]].forEach(([p,id,min,max])=>{const n=Number(query.get(p));if(query.has(p)&&Number.isFinite(n)&&n>=min&&n<=max)$(id).value=n;});
    function validRecord(r){return r && typeof r==='object' && typeof r.id==='string' && typeof r.bean==='string' && typeof r.date==='string' && ['hot','kasuya','iced','other'].includes(r.method) && ['dose','water','ice'].every(k=>Number.isFinite(r[k])) && ['grind','temp','time','notes','next'].every(k=>typeof r[k]==='string');}
    try{const saved=localStorage.getItem(KEY);if(saved){const data=JSON.parse(saved);if(!Array.isArray(data)||!data.every(validRecord))throw Error();records=data;}}catch{storageOK=false;$('journal-status').textContent='저장된 기록을 읽을 수 없거나 브라우저가 저장을 막고 있습니다. 기존 자료를 덮어쓰지 않았습니다. 브라우저 설정을 확인해 주세요.';}
    function persist(next){if(!storageOK){$('journal-status').textContent='브라우저 저장 공간을 사용할 수 없어 저장하지 못했습니다.';return false;}try{localStorage.setItem(KEY,JSON.stringify(next));records=next;return true;}catch{$('journal-status').textContent='저장 공간을 사용할 수 없습니다. 브라우저 설정과 남은 저장 공간을 확인해 주세요.';return false;}}
    const methodName=key=>recipes[key]?.name||'기타';
    function render(){
      $('record-list').replaceChildren();$('record-count').textContent=`${records.length}잔의 기록`;
      ['clear-records'].forEach(id=>$(id).disabled=!records.length);
      if(!records.length){const p=document.createElement('p');p.className='empty';p.textContent='아직 기록이 없습니다. 오늘의 한 잔에서 느낀 점을 남겨 보세요.';$('record-list').append(p);return;}
      [...records].reverse().forEach(r=>{
        const article=document.createElement('article');article.className='journal-entry';
        const date=document.createElement('small');date.textContent=`${r.date} · ${methodName(r.method)}`;
        const title=document.createElement('h3');title.textContent=r.bean;
        const dl=document.createElement('dl');
        const info=[['배합',`원두 ${r.dose}g · 물 ${r.water}g${r.ice?` · 얼음 ${r.ice}g`:''}`],['분쇄·온도',`${r.grind||'미기록'} · ${r.temp?`${r.temp}°C`:'미기록'}`],['종료 시간',r.time||'미기록'],['느낀 맛',r.notes||'미기록'],['다음 한 잔',r.next||'미기록']];
        info.forEach(([k,v])=>{const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=k;dd.textContent=v;dl.append(dt,dd);});
        const del=document.createElement('button');del.type='button';del.textContent='이 기록 삭제';del.setAttribute('aria-label',`${r.bean} 기록 삭제`);del.addEventListener('click',()=>{if(persist(records.filter(item=>item.id!==r.id))){render();$('journal-status').textContent='기록 한 건을 삭제했습니다.';}});
        article.append(date,title,dl,del);$('record-list').append(article);
      });
    }
    $('journal-form').addEventListener('submit',e=>{
      e.preventDefault();if(!$('journal-form').reportValidity())return;
      if(records.length>=500){$('journal-status').textContent='이 브라우저에는 최대 500잔을 보관합니다. 더 이상 필요하지 않은 기록을 지운 뒤 다시 저장해 주세요.';return;}
      const bean=$('entry-bean').value.trim();if(!bean){$('journal-status').textContent='원두 이름을 입력해 주세요.';$('entry-bean').focus();return;}
      const r={id:globalThis.crypto?.randomUUID?.()||`${Date.now()}-${Math.random().toString(36).slice(2)}`,date:$('entry-date').value,bean,method:$('entry-method').value,dose:numeric('entry-dose'),water:numeric('entry-water'),ice:numeric('entry-ice'),grind:$('entry-grind').value.trim(),temp:$('entry-temp').value,time:$('entry-time').value.trim(),notes:$('entry-notes').value.trim(),next:$('entry-next').value.trim()};
      if(!validRecord(r)){$('journal-status').textContent='배합과 기록 값을 확인해 주세요.';return;}
      if(persist([...records,r])){render();$('journal-status').textContent='오늘의 한 잔을 이 브라우저에 저장했습니다.';$('entry-notes').value='';$('entry-next').value='';}
    });
    $('clear-records').addEventListener('click',()=>{if(window.confirm('이 브라우저의 커피 기록을 모두 지울까요? 삭제한 기록은 되돌릴 수 없습니다.')&&persist([])){render();$('journal-status').textContent='저장된 기록을 모두 삭제했습니다.';}});
    render();
  }
})();
