// Design with Nature follows the site's light background, including old visits.
// Only the retired palette preference is removed; field notes are untouched.
if (document.documentElement.hasAttribute('data-dw-theme')) {
  document.documentElement.dataset.dwTheme = 'light';
  try { localStorage.removeItem('dwn-theme'); } catch (_) { /* Storage is optional. */ }
  const toggle = document.getElementById('dw-theme');
  if (toggle) {
    toggle.hidden = true;
    toggle.tabIndex = -1;
    toggle.setAttribute('aria-hidden', 'true');
  }
  const themeColor = document.querySelector('meta[name="theme-color"]');
  if (themeColor) themeColor.content = '#f5f6f2';
  let colorScheme = document.querySelector('meta[name="color-scheme"]');
  if (!colorScheme) {
    colorScheme = document.createElement('meta');
    colorScheme.name = 'color-scheme';
    document.head.append(colorScheme);
  }
  colorScheme.content = 'light';
}

// Fallback for browsers without declarative Shadow DOM support.
for (const host of document.querySelectorAll('spatialflare-header, spatialflare-footer')) {
  if (host.shadowRoot) continue;
  const template = host.querySelector('template[shadowrootmode]');
  if (!template) continue;
  host.attachShadow({mode: 'open'}).append(template.content.cloneNode(true));
  template.remove();
}
