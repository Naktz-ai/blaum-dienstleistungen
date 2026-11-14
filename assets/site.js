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

/* home: before/after slider */
(()=>{
  const ba=document.getElementById('ba'), knob=document.getElementById('baKnob'); if(!ba||!knob) return;
  let pos=50, anim=0, dragging=false;
  function set(p){
    pos=Math.max(0,Math.min(100,p)); ba.style.setProperty('--pos',pos+'%');
    const v=Math.round(100-pos); knob.setAttribute('aria-valuenow',v); knob.setAttribute('aria-valuetext',v+' % Nachher');
    ba.classList.toggle('hide-l',pos<14); ba.classList.toggle('hide-r',pos>86);
  }
  const stop=()=>{if(anim){cancelAnimationFrame(anim);anim=0}};
  const fromEvent=e=>{const r=ba.getBoundingClientRect(); return (e.clientX-r.left)/r.width*100};
  ba.addEventListener('pointerdown',e=>{stop(); dragging=true; ba.classList.add('drag'); ba.setPointerCapture(e.pointerId); set(fromEvent(e))});
  ba.addEventListener('pointermove',e=>{if(dragging) set(fromEvent(e))});
  const end=()=>{dragging=false; ba.classList.remove('drag')};
  ba.addEventListener('pointerup',end); ba.addEventListener('pointercancel',end);
  knob.addEventListener('keydown',e=>{
    const step=e.shiftKey?10:2, k=e.key;
    if(k==='ArrowLeft'||k==='ArrowDown'){set(pos+step)} else if(k==='ArrowRight'||k==='ArrowUp'){set(pos-step)}
    else if(k==='Home'){set(100)} else if(k==='End'){set(0)} else return;
    stop(); e.preventDefault();
  });
  set(50);
  /* gentle hint on first view: wipe across once, then settle in the middle */
  if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const keys=[[0,50],[900,78],[2000,26],[2900,50]], ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
  function run(){
    let t0=null, last=null;
    anim=requestAnimationFrame(function f(now){
      if(t0===null) t0=now; const t=now-t0;
      if(t>=keys[keys.length-1][0]){set(50); anim=0; return}
      let i=0; while(t>keys[i+1][0]) i++;
      const [a,pa]=keys[i], [b,pb]=keys[i+1]; set(pa+(pb-pa)*ease((t-a)/(b-a)));
      anim=requestAnimationFrame(f);
    });
  }
  const io=new IntersectionObserver(es=>{if(es[0].isIntersecting){io.disconnect(); setTimeout(()=>{if(!dragging) run()},1300)}},{threshold:.5});
  io.observe(ba);
})();
