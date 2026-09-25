'use strict';
let activeCorner=1;
const numberOrDash=(v,digits=1)=>v==null?'—':Number(v).toFixed(digits);
function distanceDifference(a,b){if(a==null||b==null)return '비교 지점 없음';const d=a-b;return Math.abs(d)<1?'거의 같은 위치':`${Math.abs(d).toFixed(0)}m ${d<0?'앞':'뒤'}`}
function speedDifference(a,b){if(b==null)return '';const d=a-b;return `${d>0?'+':''}${d.toFixed(1)} km/h`}
function addText(parent,tag,content,className){const e=document.createElement(tag);e.textContent=content;if(className)e.className=className;parent.append(e);return e}
function trainingRowCell(tr,value,sub){const td=addText(tr,'td','');addText(td,'span',value);if(sub)addText(td,'small',sub);return td}
function renderTraining(){
 const target=$('training-summary'),body=$('corner-body'),detail=$('corner-detail');target.replaceChildren();body.replaceChildren();detail.replaceChildren();
 const t=lap?.training,rt=reference?.training;
 if(!t?.available){addText(target,'p',t?.reason||'비교 가능한 주행 랩을 선택하세요.','muted');$('corner-note').textContent='불완전한 기록에서 정밀 제동 분석을 만들지 않습니다.';return}
 const comparableTraining=rt?.available;
 const pairs=t.corners.map(c=>({c,r:comparableTraining?rt.corners.find(x=>x.id===c.id):null}));
 $('corner-note').textContent=`공통 기준 경로의 같은 위치에서 비교합니다. 표본 간격 약 ${t.sampleInterval.toFixed(2)}초, 최고 속도에서 한 표본 이동 거리 약 ${t.positionUncertainty.toFixed(0)}m. 위치 차이가 이 수준이면 우열을 단정하지 않습니다. 코너 구간은 기준 궤적에서 추정한 범위입니다.`;
 const ranked=pairs.filter(x=>x.r).map(x=>({...x,loss:x.c.seconds-x.r.seconds,tradeoff:x.c.brakeStart!=null&&x.r.brakeStart!=null&&x.c.brakeStart-x.r.brakeStart>t.positionUncertainty&&x.c.minimumSpeed<x.r.minimumSpeed-2&&x.c.exitSpeed<x.r.exitSpeed-1}));
 const chosen=[];const push=x=>{if(x&&!chosen.some(y=>y.c.id===x.c.id))chosen.push(x)};
 push(ranked.filter(x=>x.loss>.15).sort((a,b)=>b.loss-a.loss)[0]);
 push(ranked.filter(x=>x.tradeoff).sort((a,b)=>b.loss-a.loss)[0]);
 ranked.filter(x=>x.loss<-.15).sort((a,b)=>a.loss-b.loss).forEach(x=>{if(chosen.length<3)push(x)});
 if(chosen.length){chosen.forEach(({c,r,loss,tradeoff})=>{const card=addText(target,'article','', 'training-card');addText(card,'span',loss>.15?'다시 살필 구간':tradeoff?'늦은 제동의 결과':'재현할 구간','eyebrow');addText(card,'h4',c.name);let observation=Math.abs(loss)<.1?'구간 시간은 비교 랩과 거의 같음. ':`비교 랩보다 ${Math.abs(loss).toFixed(2)}초 ${loss<0?'빠름':'느림'}. `;if(c.brakeStart!=null&&r.brakeStart!=null)observation+=`제동은 ${distanceDifference(c.brakeStart,r.brakeStart)}에서 시작, `;observation+=`최저 속도 ${speedDifference(c.minimumSpeed,r.minimumSpeed)}, 탈출 ${speedDifference(c.exitSpeed,r.exitSpeed)}.`;addText(card,'p',observation);addText(card,'p',tradeoff?'더 늦게 제동했지만 탈출은 느렸습니다. 다음 랩에서는 비교 랩의 제동 위치 부근을 시험하고, 탈출 속도와 시간을 함께 확인하세요.':loss>.15?'이 코너만 골라 제동 시작 또는 재가속 위치 중 하나를 바꿔 보세요. 나머지 조건을 유지하고 구간 시간이 줄었는지 확인하세요.':'빠른 랩에서 관측된 패턴입니다. 다음 랩에서 제동·해제·가속 순서를 반복해 같은 구간 시간이 나오는지 확인하세요.','practice');const b=addText(card,'button','지도에서 보기 →');b.onclick=()=>focusCorner(c.id)})}
 else addText(target,'p',reference?'측정 오차를 넘는 뚜렷한 차이를 찾지 못했습니다. 여러 랩에서 같은 경향이 반복되는지 살펴보세요.':'비교 랩을 고르면 코너별 차이와 다음 랩에서 시험할 항목을 표시합니다.','muted');
 for(const {c,r} of pairs){const tr=document.createElement('tr');if(c.id===activeCorner)tr.className='selected-corner';const td=addText(tr,'td','');const b=addText(td,'button',c.name);b.onclick=()=>focusCorner(c.id);addText(td,'small',`${c.direction}회전 · ${Math.round(c.windowStart)}–${Math.round(c.windowEnd)}m`);
 trainingRowCell(tr,`${c.seconds.toFixed(2)}초`,r?(Math.abs(c.seconds-r.seconds)<.01?'차이 <0.01초':`${c.seconds-r.seconds>0?'+':''}${(c.seconds-r.seconds).toFixed(2)}초`):'');
 trainingRowCell(tr,c.brakeStart==null?'제동 없음':`${Math.round(c.brakeStart)}m`,r&&c.brakeStart!=null?distanceDifference(c.brakeStart,r.brakeStart):'');
 trainingRowCell(tr,c.brakeRelease==null?'—':`${Math.round(c.brakeRelease)}m`,r&&c.brakeRelease!=null?distanceDifference(c.brakeRelease,r.brakeRelease):'');
 trainingRowCell(tr,c.accelerationAt==null?'변화 없음':`${Math.round(c.accelerationAt)}m`,r&&c.accelerationAt!=null?distanceDifference(c.accelerationAt,r.accelerationAt):'');
 trainingRowCell(tr,`${c.minimumSpeed.toFixed(1)}`,r?speedDifference(c.minimumSpeed,r.minimumSpeed):'km/h');
 trainingRowCell(tr,`${c.exitSpeed.toFixed(1)}`,r?speedDifference(c.exitSpeed,r.exitSpeed):'km/h');
 trainingRowCell(tr,`${c.coastSeconds.toFixed(2)}초`,r?`비교 ${r.coastSeconds.toFixed(2)}초`:'');body.append(tr)}
 const c=t.corners.find(x=>x.id===activeCorner)||t.corners[0];if(!c)return;activeCorner=c.id;
 addText(detail,'h4',`${c.name} · 페달과 속도`);
 const stats=addText(detail,'div','','corner-metrics');
 for(const [label,value] of [['진입 속도',c.entrySpeed.toFixed(1)+' km/h'],['제동 시작 속도',c.brakeStartSpeed==null?'제동 없음':c.brakeStartSpeed.toFixed(1)+' km/h'],['최대 브레이크 입력',c.peakBrake==null?'—':Math.round(c.peakBrake*100)+'%'],['제동 지속 시간',c.brakeDuration==null?'—':c.brakeDuration.toFixed(2)+'초'],['페달 동시 입력',c.overlapSeconds.toFixed(2)+'초'],['전가속 시간',c.fullThrottleSeconds.toFixed(2)+'초']]){const item=addText(stats,'div','');addText(item,'span',label);addText(item,'strong',value)}
 addText(detail,'p','진입·탈출 속도는 매 랩 동일한 기준 위치에서 읽습니다. 제동은 5% 초과 입력이 0.15초 이상 지속된 구간, 해제는 3% 미만, 재가속은 20% 이상으로 올라가 약 0.2초 지속된 지점입니다. 페달 동시 입력과 코스팅은 관측값이며 잘못된 운전으로 단정하지 않습니다.','muted');
}
function focusCorner(id){if(!lap?.training?.available)return;activeCorner=id;const c=lap.training.corners.find(x=>x.id===id);if(!c)return;progress=c.minimumAt/lap.training.referenceLength;$('position').value=progress*1000;renderTraining();map();chart();cursor();document.querySelector('.map-card').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'})}
function drawTrainingMarkers(){
 if(!lap?.training?.available||!project)return;
 const c=lap.training.corners.find(x=>x.id===activeCorner);if(!c)return;
 const base=lap.training.distanceTrace,marks=[];
 for(const [label,s,color] of [['제동',c.brakeStart,'#a44b39'],['해제',c.brakeRelease,'#795898'],['최저',c.minimumAt,'#245f45'],['가속',c.accelerationAt,'#256a8a']]){
  if(s==null)continue;
  let index=base.findIndex(p=>p[0]>=s);if(index<0)index=base.length-1;
  const row=lap.trace[index],q=project(row[1],row[2]);marks.push({label,color,q});
 }
 marks.sort((a,b)=>a.q.y-b.q.y);let previous=-20;
 marks.forEach(m=>{m.labelY=Math.max(m.q.y,previous+20);previous=m.labelY});
 const shift=Math.max(0,previous-410);
 marks.forEach(({label,color,q,labelY})=>{
  const x=q.x>690?q.x-45:q.x+16,y=labelY-shift;
  node('path',{d:`M${q.x},${q.y} L${x-3},${y-4}`,stroke:color,'stroke-width':.8,opacity:.65},$('map'));
  node('circle',{cx:q.x,cy:q.y,r:4.5,fill:color,stroke:'#f6f8f6','stroke-width':1.5},$('map'));
  const labelNode=text($('map'),x,y,label,color,11);labelNode.setAttribute('paint-order','stroke');labelNode.setAttribute('stroke','#f6f8f6');labelNode.setAttribute('stroke-width','3');
 });
}
