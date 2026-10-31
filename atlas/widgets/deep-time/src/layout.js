/* Presentation adapter only. Scientific datasets and original handlers are retained. */
(()=>{
  'use strict';
  const version='1.19.0';
  const header=document.getElementById('aw-header-family');
  const tabs=document.getElementById('tabs');
  const search=document.querySelector('.atlas-deep-search');
  const right=header.querySelector('.atlas-family-right');
  document.documentElement.classList.add('wl-deep-layout');
  header.insertBefore(tabs,right);
  header.insertBefore(search,right);
  header.querySelector('.atlas-family-subtitle').textContent='Earth’s history through time';
  document.getElementById('search').placeholder='Search intervals and taxa…';

  const updates=[
    'Moved the existing topic tabs and search into a compact, responsive header.',
    'Improved the selected interval scene and enlarged nearby interval previews with source age labels.',
    'Retained original scientific data, interval/taxon IDs, topic panels, filters, timeline bars, and historical releases.'
  ];
  // Add a release without replacing or renumbering any original history entry.
  RELEASES.unshift({version,date:'October 30, 2026',updates});
  const release=document.createElement('details');
  release.className='aw-release';release.open=true;
  const summary=document.createElement('summary');
  summary.textContent='v'+version+' · October 30, 2026';
  const list=document.createElement('ul');
  for(const text of updates){const item=document.createElement('li');item.textContent=text;list.append(item);}
  release.append(summary,list);
  const history=document.querySelector('#aw-version-modal .aw-releases');
  history.querySelectorAll('details').forEach(item=>item.open=false);
  history.prepend(release);
  document.querySelector('#aw-version-modal .aw-stat-summary').textContent='Current release v'+version+' · October 30, 2026';
  function versionLabels(){
    document.title='Deep Time Atlas — v'+version;
    header.dataset.awVersion=version;
    const button=document.getElementById('versionBtn');
    button.querySelector('strong').textContent='v'+version;
    button.setAttribute('aria-label','Open v'+version+' release history');
    document.getElementById('versionNumber').textContent='v'+version;
  }
  versionLabels();window.addEventListener('load',versionLabels);

  const entries=JSON.parse(document.getElementById('atlas-art-manifest').textContent).entries;
  const labels=new Map(entries.map(entry=>[entry.label,entry]));
  const strip=document.querySelector('.aw-v19-scene-filmstrip');
  const fmt=value=>new Intl.NumberFormat('en-US',{maximumFractionDigits:6}).format(value);
  function ages(){
    for(const button of strip.querySelectorAll('button')){
      const label=button.querySelector('span')?.textContent;
      const entry=labels.get(label);if(!entry)continue;
      button.dataset.interval=entry.id;
      button.setAttribute('aria-current',String(button.classList.contains('active')));
      let age=button.querySelector('.wl-interval-age');
      if(!age){age=document.createElement('small');age.className='wl-interval-age';button.append(age);}
      age.textContent=fmt(entry.start_mya)+' – '+fmt(entry.end_mya)+' Ma';
      button.setAttribute('aria-label',entry.label+', '+age.textContent+', illustrative interval artwork');
    }
  }
  new MutationObserver(ages).observe(strip,{childList:true});ages();
})();
