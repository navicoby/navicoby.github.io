const select = document.querySelector('#page-select');
if (select) select.addEventListener('change', () => {
  window.location.href = select.value;
});
