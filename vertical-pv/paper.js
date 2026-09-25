'use strict';
document.querySelector('[data-print]')?.addEventListener('click',()=>window.print());
const sectionLinks=[...document.querySelectorAll('.sidebar nav a')];
const sections=[...document.querySelectorAll('article section[id]')];
function updateReading(){
  const total=document.documentElement.scrollHeight-window.innerHeight;
  document.querySelector('.reading-progress').style.transform=`scaleX(${total>0?Math.min(1,Math.max(0,window.scrollY/total)):0})`;
  let current=sections[0]?.id;
  for(const section of sections){if(section.getBoundingClientRect().top<=155)current=section.id;}
  for(const link of sectionLinks){if(link.hash===`#${current}`)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');}
}
let ticking=false;
window.addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{updateReading();ticking=false;});ticking=true;}},{passive:true});
document.querySelectorAll('.mobile-toc a').forEach(a=>a.addEventListener('click',()=>{document.querySelector('.mobile-toc').open=false;}));
updateReading();
