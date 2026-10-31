/* Presentation adapter. Original figure records and relationship handlers remain intact. */
(()=>{
 'use strict';
 const version='1.14.0';
 const featured=__WL_FEATURED_ASSETS__;
 const manifest=new Map(JSON.parse(document.getElementById('atlas-art-manifest').textContent).entries.map(e=>[e.key,e]));
 const header=document.getElementById('aw-header-family');
 const right=header.querySelector('.atlas-family-right');
 const search=document.querySelector('.searchwrap');
 document.documentElement.classList.add('wl-myth-layout');
 header.insertBefore(search,right);
 header.querySelector('.atlas-family-subtitle').textContent='Stories, figures and genealogies';
 const nativeToggle=document.getElementById('awMythArtToggle');
 nativeToggle.hidden=true;
 const views=document.createElement('div');views.id='wl-myth-views';views.setAttribute('role','group');views.setAttribute('aria-label','Figure view');
 const artButton=document.createElement('button'),treeButton=document.createElement('button');
 artButton.id='wl-myth-art';treeButton.id='wl-myth-tree';
 for(const [button,label] of [[artButton,'Artwork'],[treeButton,'Family tree']]){button.type='button';button.className='wl-view';button.textContent=label;views.append(button);}
 header.insertBefore(views,right);
 function syncMode(){
  const artwork=nativeToggle.getAttribute('aria-pressed')==='true';
  artButton.setAttribute('aria-pressed',String(artwork));treeButton.setAttribute('aria-pressed',String(!artwork));
  document.documentElement.classList.toggle('wl-myth-art-mode',artwork);
 }
 function mode(artwork){if((nativeToggle.getAttribute('aria-pressed')==='true')!==artwork)nativeToggle.click();syncMode();}
 artButton.addEventListener('click',()=>mode(true));treeButton.addEventListener('click',()=>mode(false));
 new MutationObserver(syncMode).observe(nativeToggle,{attributes:true,attributeFilter:['aria-pressed']});

 const updates=['Added a compact search header and explicit Artwork / Family tree view controls.',
  'Refined the selected-figure artwork stage and profile using existing local illustrations and disclosed concept artwork.',
  'Kept related-figure thumbnails within the active tradition; original records, genealogy and filter logic remain intact.'];
 const release=document.createElement('details');release.className='aw-release';release.open=true;
 const summary=document.createElement('summary');summary.textContent='v'+version+' · October 30, 2026';
 const list=document.createElement('ul');for(const text of updates){const item=document.createElement('li');item.textContent=text;list.append(item);}release.append(summary,list);
 const history=document.querySelector('#aw-version-modal .aw-releases');history.querySelectorAll('details').forEach(e=>e.open=false);history.prepend(release);
 document.querySelector('#aw-version-modal .aw-stat-summary').textContent='Current release v'+version+' · October 30, 2026';
 function versionLabels(){document.title='Mythology Atlas — v'+version;header.dataset.awVersion=version;header.querySelector('.atlas-family-version strong').textContent='v'+version;document.getElementById('versionButton').setAttribute('aria-label','Open v'+version+' release history');document.querySelector('meta[name="atlas-version"]')?.setAttribute('content',version);}
 versionLabels();window.addEventListener('load',versionLabels);

 let lastFigureKey='';
 function update(){
  const key=tradition+':'+selected, entry=manifest.get(key), scene=featured[key]?.src||window.AtlasMythologyArtwork.sceneFor(key);
  if(key!==lastFigureKey){document.getElementById('profile').scrollTo({top:0,behavior:'instant'});lastFigureKey=key;}
  const stage=document.getElementById('awMythArtworkStage');
  if(scene){stage.style.setProperty('--aw-art-bg','url("'+scene+'")');document.getElementById('profileHead').style.setProperty('--aw-myth-hero','url("'+scene+'")');}
  stage.dataset.artworkKey=key;stage.dataset.sourceType=entry?.source_type||'original_symbolic';
  document.getElementById('awArtCredit').title=entry?.disclosure||'';
  document.getElementById('awArtCredit').textContent=featured[key]?
   'Modern AI concept illustration, not historical artwork. Cultural review pending.':
   'Modern symbolic illustration, not historical artwork or a verified likeness. Source traditions and references remain in the profile.';
  const related=document.getElementById('awMythRelated');if(!related)return;
  const heading=related.querySelector('.aw-micro-heading');if(heading)heading.textContent='Related figures';
  for(const button of related.querySelectorAll('.aw-related-figure')){
   const name=button.querySelector('.aw-related-name')?.textContent;
   const source=[...document.querySelectorAll('#profileContent .relationrow button[data-rel]')].find(b=>b.textContent.trim()===name);
   if(!source)continue;
   const id=source.dataset.rel,thumb=window.AtlasMythologyArtwork.thumbFor(tradition+':'+id);
   button.dataset.figureId=id;button.dataset.artworkKey=tradition+':'+id;
   const image=button.querySelector('img');
   if(image&&thumb&&image.getAttribute('src')!==thumb)image.src=thumb;
   if(image&&!thumb)image.remove();
  }
 }
 let pending=false;
 function queue(){if(pending)return;pending=true;queueMicrotask(()=>{pending=false;update()});}
 new MutationObserver(queue).observe(document.getElementById('profileHead'),{childList:true});
 new MutationObserver(queue).observe(document.getElementById('profileContent'),{childList:true});
 document.getElementById('results').addEventListener('click',event=>{if(innerWidth<900&&event.target.closest('[data-entry]')&&nativeToggle.getAttribute('aria-pressed')==='true')requestAnimationFrame(()=>document.getElementById('awMythArtworkStage').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth',block:'start'}));});
 mode(true);queue();
})();
