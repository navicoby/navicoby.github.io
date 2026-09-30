(() => {
'use strict';
const chapterLinks = [...document.querySelectorAll('.reading-nav nav a')];
const chapters = chapterLinks.map(a => document.querySelector(a.getAttribute('href')));
function updateReadingPosition() {
  let current = chapters[0];
  for (const chapter of chapters) if (chapter.getBoundingClientRect().top <= 160) current = chapter;
  for (const link of chapterLinks) {
    const active = link.hash === '#' + current.id;
    link.classList.toggle('active', active);
    if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
  }
}
let scrollPending = false;
window.addEventListener('scroll', () => {
  if (!scrollPending) requestAnimationFrame(() => { updateReadingPosition(); scrollPending = false; });
  scrollPending = true;
}, {passive:true});
updateReadingPosition();
function openAxisFromHash() {
  const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (target && target.classList.contains('axis')) target.open = true;
}
window.addEventListener('hashchange', openAxisFromHash);
openAxisFromHash();

const loadButton = document.getElementById('load-sources');
const reader = document.getElementById('archive-reader');
const status = document.getElementById('archive-status');
const select = document.getElementById('source-select');
const text = document.getElementById('source-text');
const title = document.getElementById('archive-title');
const search = document.getElementById('source-search');
const searchStatus = document.getElementById('search-status');
let reports = null, activeReport = null, hits = [], hitIndex = -1, searchTimer;
function showReport() {
  activeReport = reports.find(r => r.id === select.value);
  title.textContent = activeReport.title;
  search.value = '';
  searchStatus.textContent = '';
  text.textContent = activeReport.text;
  text.scrollTop = 0;
  hits = []; hitIndex = -1;
}
loadButton.addEventListener('click', async () => {
  if (reports) {
    reader.hidden = false; loadButton.hidden = true; status.textContent = '';
    return;
  }
  loadButton.disabled = true;
  status.textContent = '세 보고서의 전체 원문을 불러오고 있습니다…';
  try {
    const response = await fetch('./source-library.json.gz');
    if (!response.ok) throw new Error('HTTP ' + response.status);
    const bytes = new Uint8Array(await response.arrayBuffer());
    let raw;
    if (bytes[0] === 31 && bytes[1] === 139) {
      if (!('DecompressionStream' in window)) throw new Error('이 브라우저는 압축 원문을 지원하지 않습니다. 최신 브라우저에서 다시 열어주세요.');
      raw = await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
    } else raw = new TextDecoder().decode(bytes);
    reports = JSON.parse(raw).reports;
    showReport(); reader.hidden = false; loadButton.hidden = true;
    status.textContent = '전체 문헌 목록을 포함한 세 보고서가 준비되었습니다.';
  } catch (error) {
    status.textContent = '원문을 불러오지 못했습니다. 인터넷 연결을 확인한 뒤 다시 시도해주세요.';
    loadButton.disabled = false;
  }
});
select.addEventListener('change', showReport);
document.getElementById('close-sources').addEventListener('click', () => {
  reader.hidden = true; loadButton.hidden = false; loadButton.disabled = false;
  status.textContent = ''; loadButton.focus();
});
document.getElementById('download-source').addEventListener('click', () => {
  const blob = new Blob([activeReport.text], {type:'text/plain;charset=utf-8'});
  const url = URL.createObjectURL(blob), link = document.createElement('a');
  link.href = url; link.download = activeReport.filename; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
function highlightSearch() {
  const term = search.value.trim();
  hits = []; hitIndex = -1;
  text.textContent = '';
  if (!term) { text.textContent = activeReport.text; searchStatus.textContent = ''; return; }
  const raw = activeReport.text, lower = raw.toLocaleLowerCase(), needle = term.toLocaleLowerCase();
  const fragment = document.createDocumentFragment();
  let start = 0, index;
  while ((index = lower.indexOf(needle, start)) !== -1) {
    fragment.append(document.createTextNode(raw.slice(start, index)));
    const mark = document.createElement('mark'); mark.textContent = raw.slice(index, index + term.length);
    hits.push(mark); fragment.append(mark); start = index + term.length;
  }
  fragment.append(document.createTextNode(raw.slice(start))); text.append(fragment);
  if (hits.length) goToNextHit(); else searchStatus.textContent = '검색 결과가 없습니다.';
}
function goToNextHit() {
  if (!hits.length) return;
  if (hitIndex >= 0) hits[hitIndex].classList.remove('current');
  hitIndex = (hitIndex + 1) % hits.length;
  const hit = hits[hitIndex]; hit.classList.add('current');
  text.scrollTop += hit.getBoundingClientRect().top - text.getBoundingClientRect().top - 70;
  searchStatus.textContent = (hitIndex + 1) + ' / ' + hits.length + '개 결과';
}
search.addEventListener('input', () => { clearTimeout(searchTimer); searchTimer = setTimeout(highlightSearch, 180); });
search.addEventListener('keydown', event => {
  if (event.key === 'Enter') { event.preventDefault(); clearTimeout(searchTimer); if (!hits.length) highlightSearch(); else goToNextHit(); }
});
document.getElementById('search-next').addEventListener('click', () => {
  clearTimeout(searchTimer); if (!hits.length) highlightSearch(); else goToNextHit();
});
})();