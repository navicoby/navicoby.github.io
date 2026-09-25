"use strict";
const form=document.querySelector('#parameter-form');
function values(){return Object.fromEntries([...form.querySelectorAll('select')].map(s=>[s.name,Number(s.value)]));}
function refresh(){const p=values();document.querySelector('#config-summary').textContent=`평떼 ${p.turf_gangs}개 조의 전원 동시 작업에 필요한 인원: 조경공 ${p.turf_gangs}명 + 보통인부 ${p.turf_gangs*4}명.\n현재 공유 인원: 조경공 ${p.landscapers}명 · 보통인부 ${p.general_workers}명. 다른 공종이 같은 인원을 사용하면 대기합니다.`+(p.general_workers<p.turf_gangs*4?'\n현재 보통인부 수로는 평떼 작업조 전체를 동시에 투입할 수 없습니다.':'');}
form.addEventListener('change',refresh);refresh();
document.querySelector('#save-config').addEventListener('click',()=>{const data={schema:'RL-PARAM1',status:'USER_CONFIGURATION_NOT_SIMULATED',parameters:values(),fixed:{entry_slots:1,same_zone_parallel:false,workday_hours:8},note:'Availability limits only; productivity is not multiplied by crew count.'};const url=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='park-resource-configuration.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);});
