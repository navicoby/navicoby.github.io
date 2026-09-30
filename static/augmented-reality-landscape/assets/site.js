'use strict';
const progress = document.querySelector('#progress');
function updateProgress() {
  const d = document.documentElement;
  progress.style.width = (d.scrollHeight > d.clientHeight ? 100 * d.scrollTop / (d.scrollHeight - d.clientHeight) : 0) + '%';
}
addEventListener('scroll', updateProgress, { passive: true });
updateProgress();
const readerMenu = document.querySelector('.reader-sidebar details');
if (readerMenu && matchMedia('(max-width:700px)').matches) readerMenu.open = false;

const paperQuery = document.querySelector('#paper-query');
if (paperQuery) {
  const category = document.querySelector('#paper-category');
  const papers = [...document.querySelectorAll('.paper')];
  const normalize = text => text.normalize('NFC').toLocaleLowerCase();
  function filterPapers() {
    const terms = normalize(paperQuery.value.trim()).split(/\s+/).filter(Boolean);
    let count = 0;
    for (const paper of papers) {
      const match = (!category.value || paper.dataset.category === category.value) && terms.every(term => normalize(paper.dataset.search).includes(term));
      paper.hidden = !match;
      if (match) count++;
    }
    document.querySelector('#paper-count').textContent = `${count} / ${papers.length}개 문헌 기록`;
    document.querySelector('#paper-empty').hidden = count > 0;
  }
  paperQuery.value = new URLSearchParams(location.search).get('q') || '';
  paperQuery.addEventListener('input', filterPapers);
  category.addEventListener('change', filterPapers);
  document.querySelector('#paper-reset').addEventListener('click', () => {
    paperQuery.value = ''; category.value = ''; filterPapers(); paperQuery.focus();
  });
  filterPapers();
}

const form = document.querySelector('#search-form');
if (form) {
  const query = document.querySelector('#search-query');
  const status = document.querySelector('#search-status');
  const results = document.querySelector('#search-results');
  let documents;
  let request = 0;
  const normalize = text => text.normalize('NFC').toLocaleLowerCase();
  function highlighted(text, terms) {
    const fragment = document.createDocumentFragment();
    const pattern = new RegExp(terms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|'), 'giu');
    let start = 0;
    for (const match of text.matchAll(pattern)) {
      fragment.append(document.createTextNode(text.slice(start, match.index)));
      const mark = document.createElement('mark'); mark.textContent = match[0]; fragment.append(mark);
      start = match.index + match[0].length;
    }
    fragment.append(document.createTextNode(text.slice(start)));
    return fragment;
  }
  async function search() {
    const id = ++request;
    const value = query.value.trim().normalize('NFC');
    const terms = normalize(value).split(/\s+/).filter(Boolean);
    results.replaceChildren();
    if (!terms.length) {status.textContent = '검색어를 입력해 주세요.'; return;}
    history.replaceState(null, '', '?q=' + encodeURIComponent(value));
    status.textContent = '원고와 문헌을 검색하는 중입니다…';
    try {
      if (!documents) {
        const response = await fetch('assets/search-index.json');
        if (!response.ok) throw new Error('index');
        documents = await response.json();
      }
      if (id !== request) return;
      const matched = documents.map(doc => {
        const title = normalize(doc.title), text = normalize(doc.text);
        return {doc, match: terms.every(t => (title + ' ' + text).includes(t)), score: terms.reduce((n, t) => n + (title.includes(t) ? 10 : 0), 0)};
      }).filter(item => item.match).sort((a,b) => b.score - a.score);
      status.textContent = matched.length ? `${matched.length}개 결과` : '검색 결과가 없습니다. 더 짧은 단어나 다른 표현으로 검색해 보세요.';
      for (const {doc} of matched) {
        const article = document.createElement('article'); article.className = 'search-result';
        const kind = document.createElement('small'); kind.textContent = doc.kind;
        const heading = document.createElement('h2'); const link = document.createElement('a');
        link.href = doc.url; link.append(highlighted(doc.title,terms)); heading.append(link);
        const lower = normalize(doc.text);
        const positions = terms.map(t => lower.indexOf(t)).filter(i => i >= 0);
        const start = Math.max(0, (positions.length ? Math.min(...positions) : 0) - 55);
        const excerpt = (start ? '…' : '') + doc.text.slice(start, start + 210) + (doc.text.length > start + 210 ? '…' : '');
        const p = document.createElement('p'); p.append(highlighted(excerpt,terms));
        article.append(kind, heading, p); results.append(article);
      }
    } catch (error) {
      if (id !== request) return;
      status.textContent = '검색 자료를 불러오지 못했습니다. 다시 검색하거나 전체 목차를 이용해 주세요.';
      const a = document.createElement('a'); a.href = 'index.html#contents'; a.textContent = '전체 목차 보기'; results.append(a);
    }
  }
  form.addEventListener('submit', event => { event.preventDefault(); search(); });
  query.value = new URLSearchParams(location.search).get('q') || '';
  if (query.value) search();
}
