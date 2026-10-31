/* Brain presentation adapter; original geometry, records and handlers are retained. */
(()=>{
 'use strict';
 const version='1.22.0',header=document.getElementById('aw-header-family');
 document.documentElement.classList.add('wl-brain-layout');
 const right=header.querySelector('.atlas-family-right');
 header.insertBefore(document.querySelector('.segmented'),right);
 const depthLabel=document.getElementById('awDepthStrength').closest('label');
 depthLabel.id='wl-depth-control';depthLabel.firstChild.textContent='Depth strength ';
 header.insertBefore(depthLabel,right);
 header.querySelector('.atlas-family-subtitle').textContent='Brain regions and circuits';
 document.getElementById('depthButton').textContent='Estimated depth';
 const callout=document.querySelector('.aw-v19-brain-callout');
 document.querySelector('.map-context').append(callout);
 const context=document.createElement('div');context.id='wl-brain-context';context.setAttribute('aria-label','Schematic projection and depth context');
 context.append(document.querySelector('.aw-brain-view-card'),document.getElementById('awDepthLegend'));
 const stage=document.querySelector('.brain-stage');stage.after(context);
 const mapNote=document.createElement('p');mapNote.id='wl-brain-map-note';mapNote.textContent='Authored schematic projection · estimated depth, not volumetric anatomy';stage.append(mapNote);
 const strength=document.getElementById('awDepthStrength');
 function syncDepth(){strength.disabled=document.getElementById('depthButton').getAttribute('aria-pressed')!=='true';}
 new MutationObserver(syncDepth).observe(document.getElementById('depthButton'),{attributes:true,attributeFilter:['aria-pressed']});syncDepth();

 const updates=['Moved native projection/depth controls into a compact responsive header.',
  'Improved selected-region and scientific-panel hierarchy; moved orientation reference off the interactive map.',
  'Preserved authored geometry, region/circuit records, time filters and depth calculations, with explicit schematic/estimated labels.'];
 const release=document.createElement('details');release.className='aw-release';release.open=true;
 const summary=document.createElement('summary');summary.textContent='v'+version+' · October 30, 2026';
 const list=document.createElement('ul');for(const text of updates){const item=document.createElement('li');item.textContent=text;list.append(item);}release.append(summary,list);
 const history=document.querySelector('#aw-version-modal .aw-releases');history.querySelectorAll('details').forEach(e=>e.open=false);history.prepend(release);
 document.querySelector('#aw-version-modal .aw-stat-summary').textContent='Current release v'+version+' · October 30, 2026';
 function versionLabels(){document.title='Brain Atlas — v'+version;header.dataset.awVersion=version;header.querySelector('.atlas-family-version strong').textContent='v'+version;document.getElementById('versionTrigger').setAttribute('aria-label','Open v'+version+' release history');}
 versionLabels();window.addEventListener('load',versionLabels);

 let lastHeading='';
 const details=document.getElementById('details');
 new MutationObserver(()=>{const heading=details.querySelector('h2')?.textContent||'';if(heading!==lastHeading){details.scrollTo({top:0,behavior:'instant'});lastHeading=heading;}}).observe(details,{childList:true});
})();
