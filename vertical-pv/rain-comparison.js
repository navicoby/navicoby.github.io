(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('rain-data').textContent);
  const amount = document.getElementById('rain-amount');
  const wind = document.getElementById('rain-wind');
  const body = document.getElementById('rain-body');
  const entries = new Map(data.map(row => [[row.family,row.wind,row.face,row.rainfall_mm,row.adhesion,row.coefficient_multiplier].join('|'),row]));
  function update() {
    const rain = Number(amount.value);
    const find = (family,face,pool,multiplier) => entries.get([family,wind.value,face,rain,pool,multiplier].join('|'));
    body.replaceChildren();
    for (const [family,label] of [['vertical','수직 양면형'],['tilted','경사 단면형']]) {
      for (const [face,side] of [['front','앞면'],['rear','뒷면']]) {
        const tr = document.createElement('tr');
        const th = document.createElement('th'); th.scope='row';th.textContent=label+' '+(family==='tilted'&&face==='rear'?'비발전 뒷면':side);tr.append(th);
        const dose=document.createElement('td');dose.textContent=find(family,face,'loose_dominated',1).surface_rain_mm.toFixed(2)+' mm';tr.append(dose);
        const control=document.createElement('td');control.textContent='100.0%';tr.append(control);
        for (const pool of ['loose_dominated','adhered_dominated']) {
          const td=document.createElement('td');
          td.textContent=find(family,face,pool,1).remaining_percent.toFixed(1)+'%';
          const small=document.createElement('small');
          small.textContent='('+find(family,face,pool,2).remaining_percent.toFixed(1)+'–'+find(family,face,pool,.5).remaining_percent.toFixed(1)+'%)';
          td.append(small);tr.append(td);
        }
        body.append(tr);
      }
    }
    document.getElementById('rain-status').textContent=rain+'mm · '+wind.options[wind.selectedIndex].text+' · 초기 오염 100mg/m²/면';
    document.getElementById('rain-note').textContent=rain===0 ? '무강우 대조: 모든 면의 초기 먼지가 그대로 남습니다.' : '표면 강우 0은 처방한 직선 궤적에서 직접 빗방울이 닿지 않았다는 뜻입니다. 물막·튐·가장자리 유출은 계산하지 않았습니다. 괄호는 가정 민감도이며 신뢰구간이 아닙니다.';
  }
  amount.addEventListener('change',update);wind.addEventListener('change',update);update();
})();
