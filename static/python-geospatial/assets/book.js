"use strict";
document.querySelectorAll("pre").forEach((pre, index) => {
  const tools = document.createElement("div");
  tools.className = "code-tools";
  const copy = document.createElement("button");
  copy.type = "button";
  copy.textContent = "코드 복사";
  copy.setAttribute("aria-label", `코드 ${index + 1} 복사`);
  copy.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(pre.textContent);
      copy.textContent = "복사 완료";
      document.getElementById("status").textContent = "코드를 복사했습니다.";
    } catch {
      document.getElementById("status").textContent = "복사를 허용하지 않는 환경입니다. 코드를 직접 선택해 복사하세요.";
      pre.focus();
    }
  });
  const wrap = document.createElement("button");
  wrap.type = "button";
  wrap.textContent = "줄바꿈";
  wrap.setAttribute("aria-label", `코드 ${index + 1} 줄바꿈`);
  wrap.setAttribute("aria-pressed", "false");
  wrap.addEventListener("click", () => {
    const active = pre.classList.toggle("wrap-code");
    wrap.setAttribute("aria-pressed", String(active));
  });
  pre.tabIndex = 0;
  tools.append(copy, wrap);
  pre.before(tools);
});
document.querySelectorAll("button[data-map-src]").forEach(button => {
  button.addEventListener("click", () => {
    const frame = document.createElement("iframe");
    frame.src = button.dataset.mapSrc;
    frame.title = "3,000제곱미터 가상공원과 주변 건물 지도";
    frame.loading = "lazy";
    frame.className = "map-frame";
    button.parentElement.append(frame);
    button.textContent = "지도 열림";
    button.disabled = true;
  }, {once: true});
});
