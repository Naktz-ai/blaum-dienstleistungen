/* Blaum Dienstleistungen: shared site script */
const SERVICES = [
  {id:"unterhalt", page:"unterhaltsreinigung/", icon:"i-unterhalt", name:"Unterhaltsreinigung", tag:"Regelmäßige Pflege für dauerhafte Sauberkeit.",
   desc:"Die laufende Reinigung in festgelegten Intervallen: täglich, wöchentlich oder monatlich. Für Büros, Praxen, Geschäfte, Schulen und öffentliche Einrichtungen. Sie entscheiden, wann und wie oft wir reinigen. Wir erledigen den Rest.",
   items:["Oberflächen- und Bodenreinigung","Sanitärreinigung inkl. Auffüllen von Verbrauchsmaterial","Entleerung von Mülleimern","Staubwischen & Desinfektion häufig berührter Flächen"],
   foot:"Diskret, gründlich und angepasst an Ihre Betriebszeiten."},
  {id:"praxis", page:"praxisreinigung/", icon:"i-praxis", name:"Praxisreinigung", tag:"Hygiene ist Vertrauen. Wir sorgen für beides.",
   desc:"Speziell abgestimmt auf Arztpraxen, Zahnarztpraxen, Physiotherapiepraxen und andere Behandlungsräume. Wir reinigen mit größter Sorgfalt und unter Beachtung hygienischer Richtlinien, damit Patienten sich sicher fühlen.",
   items:["Desinfektion von Behandlungsstühlen, Ablagen und Kontaktflächen","Reinigung von Empfangs- und Wartebereichen","Fußbodenreinigung mit professionellen Maschinen","Entleerung und Säuberung von Mülleimern inkl. Hygienebehältern"],
   foot:"Geschultes Personal für sensible Bereiche, stets diskret und verantwortungsbewusst."},
  {id:"glas", page:"glasreinigung/", icon:"i-glas", name:"Glasreinigung", tag:"Streifenfreier Glanz für Ihre Glasflächen.",
   desc:"Klare Fenster und saubere Glasflächen hinterlassen den besten Eindruck bei Kunden, Gästen und Bewohnern. Professionelle Glasreinigung in Köln und Umgebung.",
   items:["Reinigung von Fenstern und Rahmen","Schaufensterreinigung für Ladengeschäfte","Glasfassaden und Wintergärten","Glastrennwände und Glastüren im Innenbereich","Umweltfreundliche und streifenfreie Reinigung"],
   foot:"Zuverlässig und flexibel, ganz nach Ihrem Bedarf und Zeitplan."},
  {id:"treppe", page:"treppenhausreinigung/", icon:"i-treppe", name:"Treppenhausreinigung", tag:"Der erste Eindruck zählt.",
   desc:"Ein sauberes Treppenhaus spricht für Ihre Immobilie. Ob Mietshaus, Bürogebäude oder Eigentumsanlage: Wir sorgen für die regelmäßige, zuverlässige Reinigung Ihrer Treppenhäuser.",
   items:["Fegen und Wischen von Stufen, Podesten und Fluren","Reinigung von Geländern, Briefkästen und Handläufen","Entfernung von Spinnweben und Verschmutzungen an Wänden","Säuberung von Eingangsbereichen und Fußmatten"],
   foot:"Gerne mit individuellem Reinigungsplan, abgestimmt auf Ihr Objekt."},
  {id:"bau", page:"baureinigung/", icon:"i-bau", name:"Baureinigung", tag:"Vom Rohbau bis zur Schlüsselübergabe.",
   desc:"Nach Bau- oder Renovierungsarbeiten bleibt häufig viel Schmutz zurück. Unsere Baureinigung sorgt dafür, dass Ihre Räume bezugsfertig und vorzeigbar sind.",
   items:["Baugrobreinigung: Bauschutt, Staub und Verpackungen entfernen","Bauendreinigung: feine Reinigung aller Oberflächen","Böden, Fenster und Sanitärbereiche","Enge Abstimmung mit Bauherren, Handwerkern und Architekten"],
   foot:"Für eine reibungslose Übergabe an Ihre Kunden oder Mieter."},
  {id:"grund", page:"grundreinigung/", icon:"i-grund", name:"Grundreinigung", tag:"Tiefensauberkeit bis ins letzte Detail.",
   desc:"Mehr als nur Putzen: eine umfassende Intensivreinigung aller Flächen, Ecken und schwer zugänglichen Stellen. In Wohn- und Geschäftsräumen, nach Auszügen, Umbauten oder als regelmäßige Frischzellenkur.",
   items:["Entfernung von hartnäckigem Schmutz und Rückständen","Fensterreinigung inkl. Rahmen und Falzen","Reinigung von Türen, Lichtschaltern und Heizkörpern","Gründliche Bodenpflege, auch Versiegelung möglich"],
   foot:"Ideal für Eigentümer, Mieterwechsel oder nach Renovierungen."},
  {id:"airbnb", page:"airbnb-service/", icon:"i-airbnb", name:"AirBnB-Service", tag:"Saubere Wohnungen, zufriedene Gäste.",
   desc:"Als Gastgeber möchten Sie, dass sich Ihre Gäste sofort wohlfühlen. Wir übernehmen die vollständige Reinigung und Übergabe Ihrer Ferienwohnung oder Ihres AirBnB-Apartments.",
   items:["Reinigung von Bad, Küche, Böden, Möbeln und Oberflächen","Frisches Bettzeug & Handtücher bereitlegen (optional)","Müllentsorgung & Nachfüllen von Verbrauchsartikeln","Kontrolle auf Schäden oder vergessene Gegenstände"],
   foot:"Auch kurzfristig bei neuen Gästewechseln, zuverlässig und pünktlich."},
  {id:"haus", page:"hausmeisterservice/", icon:"i-haus", name:"Hausmeisterservice", tag:"Alles im Blick. Gepflegte Immobilien, zufriedene Bewohner.",
   desc:"Ordnung, Sicherheit und ein reibungsloser Ablauf in und rund um Ihre Immobilie. Ob kleine Reparaturen, regelmäßige Kontrollgänge oder die Pflege von Außenanlagen: Wir sind zuverlässig zur Stelle.",
   items:["Kontrolle technischer Einrichtungen & Allgemeinbereiche","Durchführung kleiner Reparaturen","Bereitstellung & Reinigung der Mülltonnen","Pflege von Gehwegen, Höfen & Grünflächen","Ansprechpartner für Bewohner & Eigentümer","Koordination externer Handwerker bei Bedarf"],
   foot:"Freundlich, zuverlässig und einsatzbereit in Köln und Umgebung."}
];
const ico = (id, cls="ico", style="") => `<svg class="${cls}"${style?` style="${style}"`:""}><use href="#${id}"/></svg>`;
const $ = id => document.getElementById(id);

/* header, menu, mobile bar */
(()=>{
  const header=$('top'), mbar=$('mbar'), burger=document.querySelector('.burger');
  const onScroll=()=>{header.classList.toggle('scrolled',scrollY>20); if(mbar) mbar.classList.toggle('show',scrollY>500)};
  addEventListener('scroll',onScroll,{passive:true}); onScroll();
  burger.addEventListener('click',()=>{const o=header.classList.toggle('open'); burger.setAttribute('aria-expanded',o)});
  document.querySelectorAll('.menu a').forEach(a=>a.addEventListener('click',()=>{header.classList.remove('open');burger.setAttribute('aria-expanded',false)}));
  addEventListener('keydown',e=>{if(e.key==='Escape'&&header.classList.contains('open')){header.classList.remove('open');burger.setAttribute('aria-expanded',false);burger.focus()}});
  if(matchMedia('(prefers-reduced-motion: reduce)').matches) document.querySelectorAll('video[autoplay]').forEach(v=>{v.removeAttribute('autoplay');v.pause()});
  const yr=$('yr'); if(yr) yr.textContent=new Date().getFullYear();
})();

/* home: services tabs */
(()=>{
  const list=$('svcList'), panel=$('svcPanel'); if(!list||!panel) return;
  list.innerHTML = SERVICES.map((s,i)=>`<button class="svc-tab" role="tab" id="tab-${s.id}" aria-controls="svcPanel" aria-selected="${i===0}" tabindex="${i===0?0:-1}" data-i="${i}"><span class="tic">${ico(s.icon)}</span>${s.name}${ico('i-arrow','ico arr','width:18px;height:18px')}</button>`).join('');
  function show(i){
    const s=SERVICES[i];
    list.querySelectorAll('.svc-tab').forEach((b,j)=>{b.setAttribute('aria-selected',j===i);b.tabIndex=j===i?0:-1});
    panel.setAttribute('aria-labelledby','tab-'+s.id);
    panel.innerHTML=`<div class="fade-in">
      <figure class="svc-img"><img src="assets/svc-${s.id}.webp" alt="${s.name}" loading="lazy"><figcaption>${ico(s.icon)}</figcaption></figure>
      <span class="num">${String(i+1).padStart(2,'0')} / ${String(SERVICES.length).padStart(2,'0')}</span>
      <h3>${s.name}</h3><p class="tag">${s.tag}</p><p class="desc">${s.desc}</p>
      <ul class="checks">${s.items.map(t=>`<li><span class="ck">${ico('i-check')}</span>${t}</li>`).join('')}</ul>
      <div class="svc-foot"><p>${s.foot}</p><div style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn-ghost" href="${s.page}">Mehr erfahren</a><a class="btn btn-primary" href="#kontakt" data-pick="${s.id}">${s.name} anfragen <span class="dot">${ico('i-arrow','ico','width:14px;height:14px')}</span></a></div></div></div>`;
  }
  list.addEventListener('click',e=>{const b=e.target.closest('.svc-tab'); if(b){show(+b.dataset.i); if(innerWidth<1020) b.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'})}});
  list.addEventListener('keydown',e=>{
    const tabs=[...list.children], cur=tabs.indexOf(document.activeElement); if(cur<0) return;
    let n=null; if(['ArrowDown','ArrowRight'].includes(e.key)) n=(cur+1)%tabs.length; if(['ArrowUp','ArrowLeft'].includes(e.key)) n=(cur-1+tabs.length)%tabs.length;
    if(n!==null){e.preventDefault();tabs[n].focus();show(n)}
  });
  show(0);
  addEventListener('load',()=>SERVICES.forEach(s=>{const i=new Image();i.src=`assets/svc-${s.id}.webp`}));
})();

/* contact form (home + Kontakt page) */
(()=>{
  const chips=$('chips'), form=$('form'); if(!form) return;
  if(chips) chips.innerHTML=SERVICES.map(s=>`<label class="chip"><input type="checkbox" name="svc" value="${s.name}" id="chip-${s.id}"><span>${s.name}</span></label>`).join('');
  const pre=new URLSearchParams(location.search).get('leistung'); const ps=pre&&SERVICES.find(s=>s.id===pre||s.page===pre+'/'); if(ps){const c=$('chip-'+ps.id); if(c) c.checked=true}
  document.addEventListener('click',e=>{const p=e.target.closest('[data-pick]'); if(p){const c=$('chip-'+p.dataset.pick); if(c) c.checked=true}});
  form.addEventListener('submit',e=>{
    e.preventDefault(); const f=e.target, sent=$('sent');
    if(!f.checkValidity()){ f.reportValidity(); return; }
    const svcs=[...f.querySelectorAll('input[name=svc]:checked')].map(i=>i.value).join(', ');
    const tel=f.tel?f.tel.value:'';
    const body=`Name: ${f.name.value}\nFirma: ${f.firma.value||'-'}\nE-Mail: ${f.email.value}${f.tel?`\nTelefon: ${tel||'-'}`:''}\nLeistung: ${svcs||'-'}\n\n${f.msg.value}`;
    location.href=`mailto:info@blaum-dienstleistungen.de?subject=${encodeURIComponent('Anfrage über die Website'+(svcs?': '+svcs:''))}&body=${encodeURIComponent(body)}`;
    sent.querySelector('span').textContent='Danke! Ihr E-Mail-Programm öffnet sich mit Ihrer Anfrage.'; sent.classList.add('show');
  });
})();



/* home: clean the four panes of the window with a squeegee, against the clock */
(()=>{
  const win=document.getElementById('wipe'), cv=document.getElementById('grime'); if(!win||!cv) return;
  const ctx=cv.getContext('2d',{willReadFrequently:true}), el=id=>document.getElementById(id);
  const sq=el('squeegee'), txt=el('wipeTxt'), sub=el('wipeSub'), panel=el('wipePanel'), reset=el('wipeReset'), badge=el('wipeBadge'),
        panes=[...el('panes').children], mini=[...el('wipeMini').children];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const img=new Image(); img.src='assets/window-dirty.webp';
  let W=0,H=0,dpr=1,last=null,done=false,demo=false,checkT=0,replay=false,ok=[0,0,0,0],t0=0;

  function paint(){
    if(!cv.offsetWidth) return;
    dpr=Math.min(devicePixelRatio||1,2); W=cv.offsetWidth; H=cv.offsetHeight;
    cv.width=Math.round(W*dpr); cv.height=Math.round(H*dpr); ctx.setTransform(dpr,0,0,dpr,0,0);
    ctx.globalCompositeOperation='source-over';
    const s=Math.max(W/img.naturalWidth,H/img.naturalHeight), w=img.naturalWidth*s, h=img.naturalHeight*s;
    ctx.drawImage(img,(W-w)*.5,(H-h)*.35,w,h);
    done=false; ok=[0,0,0,0]; t0=0; last=null;
    win.classList.remove('clean'); panel.classList.remove('done'); badge.classList.remove('show');
    panes.forEach(e=>e.classList.remove('ok')); mini.forEach(e=>e.classList.remove('ok'));
    txt.textContent=replay?'Auf die Plätze …':'Vier Scheiben, eine Mission';
    sub.textContent=replay?'Die Zeit läuft ab dem ersten Wisch':'Wischen Sie alle blitzblank';
  }
  const blade=()=>Math.max(60,W*.24);
  function stamp(x,y){
    const bw=blade(), bh=Math.max(16,bw*.18);
    ctx.globalCompositeOperation='destination-out';
    ctx.fillStyle='rgba(0,0,0,.35)'; ctx.beginPath(); ctx.roundRect(x-bw/2-6,y-bh/2-6,bw+12,bh+12,bh); ctx.fill();
    ctx.fillStyle='#000'; ctx.beginPath(); ctx.roundRect(x-bw/2,y-bh/2,bw,bh,bh/2); ctx.fill();
  }
  function wipeTo(p){
    if(done) return;
    if(!t0&&!demo) t0=performance.now();
    if(last){const dx=p.x-last.x, dy=p.y-last.y, n=Math.max(1,Math.ceil(Math.hypot(dx,dy)/6)); for(let i=1;i<=n;i++) stamp(last.x+dx*i/n,last.y+dy*i/n)}
    else stamp(p.x,p.y);
    last=p;
    if(!checkT) checkT=setTimeout(check,160);
  }
  function check(){
    checkT=0; if(done||demo) return;
    const cw=cv.width, ch=cv.height, d=ctx.getImageData(0,0,cw,ch).data, clr=[0,0,0,0], tot=[0,0,0,0];
    for(let y=0;y<ch;y+=6) for(let x=0;x<cw;x+=6){const q=(y>ch/2?2:0)+(x>cw/2?1:0); tot[q]++; if(d[(y*cw+x)*4+3]<90) clr[q]++}
    for(let q=0;q<4;q++) if(!ok[q]&&clr[q]/tot[q]>=.6){
      ok[q]=1; ctx.globalCompositeOperation='destination-out'; ctx.fillStyle='#000'; ctx.fillRect(q%2?W/2:0,q>1?H/2:0,W/2,H/2);
      panes[q].classList.add('ok'); mini[q].classList.add('ok');
    }
    const n=ok[0]+ok[1]+ok[2]+ok[3];
    if(n===4) return finish();
    if(n){ txt.textContent=n+' von 4 Scheiben sauber'; sub.textContent=n===3?'Nur noch eine!':'Weiter so'; }
  }
  function finish(){
    done=true; last=null; win.classList.add('clean'); win.classList.remove('wiping'); panel.classList.add('done');
    const sec=((performance.now()-t0)/1000).toFixed(1).replace('.',',');
    txt.textContent='Streifenfrei in '+sec+' s!';
    setTimeout(()=>badge.classList.add('show'),900);
  }
  const pos=e=>{const r=cv.getBoundingClientRect(), k=W/r.width; return {x:(e.clientX-r.left)*k,y:(e.clientY-r.top)*k}};
  const moveSq=p=>{sq.style.left=p.x+'px'; sq.style.top=p.y+'px'};
  cv.addEventListener('pointerleave',()=>{win.classList.remove('hover','wiping'); last=null});
  cv.addEventListener('pointerdown',e=>{if(demo) return; try{cv.setPointerCapture(e.pointerId)}catch(_){} win.classList.add('wiping'); last=null; const p=pos(e); moveSq(p); wipeTo(p)});
  cv.addEventListener('pointermove',e=>{if(demo) return; const p=pos(e); moveSq(p); if(e.buttons||e.pointerType==='mouse'){win.classList.add('hover'); wipeTo(p)}});
  const up=()=>{win.classList.remove('wiping'); last=null; if(!done) check()};
  cv.addEventListener('pointerup',up); cv.addEventListener('pointercancel',up);
  reset.addEventListener('click',()=>{replay=true; paint()});
  let rt; new ResizeObserver(()=>{clearTimeout(rt); rt=setTimeout(()=>{if(!done&&W&&Math.abs(cv.offsetWidth-W)>2) paint()},150)}).observe(cv);

  /* first view only: the squeegee pulls one short stroke in the top-left pane */
  function runDemo(delay){
    if(reduce) return;
    setTimeout(()=>{
      if(done||t0||win.classList.contains('wiping')) return;
      demo=true; win.classList.add('demo','wiping'); last=null;
      const s0=performance.now(), dur=1300, ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
      (function f(now){
        const k=Math.min(1,(now-s0)/dur), e=ease(k), p={x:W*(.27+.04*Math.sin(e*Math.PI)), y:H*(.14+.28*e)};
        moveSq(p); wipeTo(p);
        if(k<1) requestAnimationFrame(f); else {demo=false; last=null; win.classList.remove('demo','wiping')}
      })(s0);
    },delay);
  }
  const start=()=>{paint(); const io=new IntersectionObserver(es=>{if(es[0].isIntersecting){io.disconnect(); runDemo(1300)}},{threshold:.5}); io.observe(win)};
  if(img.complete&&img.naturalWidth) start(); else img.addEventListener('load',start,{once:true});
})();
