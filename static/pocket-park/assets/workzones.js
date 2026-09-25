"use strict";
const proposed=document.querySelector('#show-proposed');const original=document.querySelector('#show-original');const plan=document.querySelector('#zone-plan');
function show(newPlan){plan.src=newPlan?'assets/workzones-R2.png':'assets/workzones-R1.png';plan.alt=newPlan?'식재와 시설물 단위를 유지한 비균등 공구 조정안':'면적 500제곱미터씩 나눈 기존 R1 공구';proposed.setAttribute('aria-pressed',String(newPlan));original.setAttribute('aria-pressed',String(!newPlan));}
proposed.addEventListener('click',()=>show(true));original.addEventListener('click',()=>show(false));
