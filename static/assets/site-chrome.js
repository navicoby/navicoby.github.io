// Fallback for browsers without declarative Shadow DOM support.
for (const host of document.querySelectorAll('spatialflare-header, spatialflare-footer')) {
  if (host.shadowRoot) continue;
  const template = host.querySelector('template[shadowrootmode]');
  if (!template) continue;
  host.attachShadow({mode: 'open'}).append(template.content.cloneNode(true));
  template.remove();
}
