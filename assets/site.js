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

/* home: soap-foam window – pop the bubbles to reveal the clean view */
(()=>{
  const win=$('window'), cv=$('grime'); if(!win||!cv) return;
  const ctx=cv.getContext('2d');
  const cur=$('squeegee'), hint=$('hint'), hintTxt=$('hintTxt'), badge=$('badge'), reset=$('reset');
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hv=$('heroVideo'); if(reduce&&hv){hv.removeAttribute('autoplay');hv.pause();}
  let W=0,H=0,dpr=1,bubbles=[],fx=[],done=false,released=false,haze=1,total=1,raf=0,visible=true,demo=false,lastT=0;
  const PAL=['255,160,220','120,230,255','255,236,140','160,255,210','190,170,255'];

  function seed(){
    const r=cv.getBoundingClientRect(); dpr=Math.min(devicePixelRatio||1,2); W=r.width; H=r.height;
    cv.width=W*dpr; cv.height=H*dpr; ctx.setTransform(dpr,0,0,dpr,0,0);
    bubbles=[]; fx=[]; done=false; released=false; haze=1;
    const target=W*H*1.05; let area=0, tries=0;
    while(area<target && tries<6000){
      tries++;
      const big=Math.random()<.22, rad=big?28+Math.random()*26:9+Math.random()*20;
      const x=Math.random()*W, y=Math.random()*H;
      if(bubbles.some(b=>Math.hypot(b.x-x,b.y-y)<(b.r+rad)*.72)) continue;
      bubbles.push({x,y,r:rad,ph:Math.random()*6.28,sp:.6+Math.random()*.8,c:PAL[Math.random()*PAL.length|0],c2:PAL[Math.random()*PAL.length|0],pop:0,vy:0,a:1});
      area+=Math.PI*rad*rad;
    }
    total=bubbles.length;
    cv.classList.remove('done'); win.classList.remove('clean'); badge.classList.remove('show'); reset.classList.remove('show'); hint.classList.remove('hide');
    setHint(); kick();
  }
  const alive=()=>bubbles.filter(b=>!b.pop).length;
  function setHint(){const n=alive(); hintTxt.textContent = n===total ? 'Blasen platzen lassen' : `Noch ${n} Blasen`}

  function drawBubble(b,t){
    const wob=reduce?0:Math.sin(t*.0018*b.sp+b.ph);
    const rx=b.r*(1+.05*wob), ry=b.r*(1-.05*wob), x=b.x+(reduce?0:Math.sin(t*.0011+b.ph)*1.6), y=b.y;
    ctx.save(); ctx.globalAlpha=b.a; ctx.translate(x,y);
    const g=ctx.createRadialGradient(-rx*.25,-ry*.3,rx*.1,0,0,rx);
    g.addColorStop(0,'rgba(255,255,255,.10)'); g.addColorStop(.7,'rgba(255,255,255,.16)');
    g.addColorStop(.92,`rgba(${b.c},.45)`); g.addColorStop(1,'rgba(255,255,255,.75)');
    ctx.fillStyle=g; ctx.beginPath(); ctx.ellipse(0,0,rx,ry,0,0,6.283); ctx.fill();
    const rim=ctx.createLinearGradient(-rx,-ry,rx,ry);
    rim.addColorStop(0,`rgba(${b.c},.9)`); rim.addColorStop(.5,'rgba(255,255,255,.5)'); rim.addColorStop(1,`rgba(${b.c2},.9)`);
    ctx.strokeStyle=rim; ctx.lineWidth=Math.max(1.2,b.r*.06); ctx.stroke();
    ctx.fillStyle='rgba(255,255,255,.85)'; ctx.beginPath(); ctx.ellipse(-rx*.38,-ry*.42,rx*.2,ry*.11,-.7,0,6.283); ctx.fill();
    ctx.fillStyle='rgba(255,255,255,.5)'; ctx.beginPath(); ctx.arc(rx*.42,ry*.38,Math.max(1,rx*.07),0,6.283); ctx.fill();
    ctx.restore();
  }
  function frame(t){
    raf=0; const dt=lastT?Math.min(6,(t-lastT)/16.7):1; lastT=t; ctx.clearRect(0,0,W,H);
    if(haze>.01){ // milky foam between the bubbles
      const hg=ctx.createLinearGradient(0,0,0,H); hg.addColorStop(0,`rgba(236,244,248,${.55*haze})`); hg.addColorStop(1,`rgba(214,228,236,${.72*haze})`);
      ctx.fillStyle=hg; ctx.fillRect(0,0,W,H);
    }
    let busy=!reduce&&!done;
    for(const b of bubbles){
      if(b.pop) continue;
      if(released){ b.vy-=.12*dt; b.y+=b.vy*dt; b.a=Math.max(0,b.a-.014*dt); busy=true; }
      drawBubble(b,t);
    }
    if(released){ bubbles=bubbles.filter(b=>!b.pop&&b.a>0&&b.y+b.r>-10); haze=Math.max(0,haze-.04*dt); if(!bubbles.length&&haze<=0&&!fx.length) return finish(); }
    fx=fx.filter(f=>f.k<1);
    for(const f of fx){ // pop: ring + droplets
      f.k+=(reduce?.2:.07)*dt; busy=true;
      ctx.strokeStyle=`rgba(255,255,255,${.8*(1-f.k)})`; ctx.lineWidth=2; ctx.beginPath(); ctx.arc(f.x,f.y,f.r*(1+f.k*.7),0,6.283); ctx.stroke();
      for(const d of f.d){ const dist=f.r*(.6+f.k*1.3); ctx.fillStyle=`rgba(${f.c},${1-f.k})`; ctx.beginPath(); ctx.arc(f.x+Math.cos(d)*dist,f.y+Math.sin(d)*dist+f.k*f.k*12,2.2*(1-f.k)+.6,0,6.283); ctx.fill(); }
    }
    busyLoop=false; if((busy||released)&&visible){ busyLoop=true; raf=requestAnimationFrame(frame) }
  }
  function kick(){ if(!raf){ if(!busyLoop) lastT=0; busyLoop=true; raf=requestAnimationFrame(frame) } }
  let busyLoop=false;

  function popAt(x,y,reach=16){
    if(done||released) return;
    let hit=0;
    for(const b of bubbles){
      if(b.pop) continue;
      if(Math.hypot(b.x-x,b.y-y)<b.r+reach){ b.pop=1; hit++; fx.push({x:b.x,y:b.y,r:b.r,k:0,c:b.c,d:Array.from({length:6},()=>Math.random()*6.283)}); }
    }
    if(!hit) return;
    cur.classList.add('hit'); setTimeout(()=>cur.classList.remove('hit'),120);
    haze=Math.max(0,alive()/total*1.1-.1);
    setHint(); kick();
    if(alive()/total<.3){ released=true; hint.classList.add('hide'); kick(); }
  }
  function finish(){
    if(done) return; done=true; released=false; ctx.clearRect(0,0,W,H);
    cv.classList.add('done'); win.classList.add('clean'); badge.classList.add('show'); reset.classList.add('show');
  }

  const pos=e=>{const r=cv.getBoundingClientRect();return{x:e.clientX-r.left,y:e.clientY-r.top}};
  const moveCur=e=>{const r=win.getBoundingClientRect(); cur.style.left=(e.clientX-r.left)+'px'; cur.style.top=(e.clientY-r.top)+'px'};
  let last=null;
  function sweep(p){ // pop along the path so fast moves don't skip bubbles
    if(last){const dx=p.x-last.x, dy=p.y-last.y, n=Math.ceil(Math.hypot(dx,dy)/10); for(let i=1;i<=n;i++) popAt(last.x+dx*i/n,last.y+dy*i/n)} else popAt(p.x,p.y);
    last=p;
  }
  win.addEventListener('pointermove',e=>{if(demo)return; moveCur(e); if(e.pointerType==='mouse'||e.buttons) sweep(pos(e))});
  win.addEventListener('pointerdown',e=>{if(demo)return; last=null; moveCur(e); sweep(pos(e))});
  win.addEventListener('pointerleave',()=>last=null);
  win.addEventListener('pointerup',()=>last=null);
  reset.addEventListener('click',e=>{e.stopPropagation(); last=null; seed()});
  let rt; addEventListener('resize',()=>{clearTimeout(rt); rt=setTimeout(()=>{if(Math.abs(cv.getBoundingClientRect().width-W)>2&&!done){last=null;seed()}},200)});
  new IntersectionObserver(es=>{visible=es[0].isIntersecting; if(visible) kick()}).observe(win);
  seed();

  if(!reduce){ // short auto demo: the wand pops a curved line of bubbles
    setTimeout(()=>{
      if(done||released) return;
      demo=true; win.classList.add('demo'); last=null; const s=performance.now(), dur=1400;
      const wr=win.getBoundingClientRect(), cr=cv.getBoundingClientRect(), ox=cr.left-wr.left, oy=cr.top-wr.top;
      (function f(t){const k=Math.min(1,(t-s)/dur), e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;
        const x=W*(.15+.7*e), y=H*(.62-Math.sin(e*Math.PI)*.22);
        sweep({x,y}); cur.style.left=(x+ox)+'px'; cur.style.top=(y+oy)+'px';
        if(k<1) requestAnimationFrame(f); else {demo=false; win.classList.remove('demo'); last=null}
      })(s);
    },1200);
  }
})();
