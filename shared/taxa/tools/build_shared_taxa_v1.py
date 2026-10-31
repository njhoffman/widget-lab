#!/usr/bin/env python3
"""Preservation-first Shared Taxa v1.0 reproducible reconciler. No network calls."""
import json, re, zipfile, hashlib, shutil, collections, copy, io, os, pathlib, datetime, unicodedata
from decimal import Decimal
from urllib.parse import urlparse
from jsonschema import Draft202012Validator
from PIL import Image

BASE=pathlib.Path('/mnt/data'); OUT=BASE/'Shared_Taxa_v1.0'; TREE_Z=BASE/'shared_taxa_tree_of_life_v1.7_export(1).zip'; DEEP_Z=BASE/'Shared_Taxa_Deep_Time_Atlas_v1.6_Export(2).zip'
OUT.mkdir(exist_ok=True,parents=True)
FDATE='2026-10-15'; VERSION='1.0'; SCHEMA_V='1.0';
SRC_T='tree_of_life_explorer_v1.7';SRC_D='deep_time_atlas_v1.6'

def digest(bs):return hashlib.sha256(bs).hexdigest()
def dump(o,p):
 p=OUT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2,sort_keys=False)+'\n',encoding='utf8')
def textout(txt,p):
 p=OUT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(txt,encoding='utf8')
def loadfile(n):return json.loads((BASE/n).read_text(encoding='utf8'))
def canon_id(kind,key):
 slug=re.sub(r'-+','-',re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',str(key)).encode('ascii','ignore').decode().lower())).strip('-')[:54] or 'unnamed'
 return f'stx:{kind}:{slug}-{digest(str(key).encode())[:10]}'
def ranknorm(s):
 s=(s or '').lower().strip();s=re.sub(r'^(extinct\s*/\s*debated|extinct|traditional)\s+','',s)
 return s

def provenance(src,source_id,source_path,version=None):return {'source_export':src,'source_id':source_id,'source_file':source_path,'source_version':version or ('1.7' if src==SRC_T else '1.6')}

TREE_FILES=['AMBIGUITIES.md','README.md','SCHEMA.md','diversity.json','geologic_time.json','manifest.json','organisms.json','rank_guides.json','sources.json','taxon_details.json','taxon_history.json','taxonomy.json','validation_report.json']
# Explicitly verify the original export and loose copies match.
with zipfile.ZipFile(TREE_Z) as tz:
 tzn=tz.namelist(); print('Tree archive items',len(tzn),tzn[:15]);
 # source export may put files in root
 tree_zip_members={pathlib.PurePosixPath(k).name:k for k in tzn if not k.endswith('/')}
 tree_mismatches=[n for n in TREE_FILES if n in tree_zip_members and digest(tz.read(tree_zip_members[n]))!=digest((BASE/n).read_bytes())]
 print('Loose Tree / zip mismatches',tree_mismatches)
with zipfile.ZipFile(DEEP_Z) as dz:
 prefix='Shared_Taxa_Deep_Time_Atlas_v1.6/'
 def deep(path):return json.loads(dz.read(prefix+path))
 dtaxa=deep('data/taxa.json'); dint=deep('data/geologic_intervals.json'); dlinks=deep('data/geologic_taxon_links.json'); dimages=deep('data/images_manifest.json'); dmeta=deep('metadata.json'); dambi=deep('AMBIGUITIES.json'); drefs=deep('data/source_references.json')
 deep_member_count=sum(1 for i in dz.infolist() if not i.is_dir())
 deep_file_map={i.filename[len(prefix):]:i for i in dz.infolist() if i.filename.startswith(prefix) and not i.is_dir()}

ttax=loadfile('taxonomy.json')['records']; tdetails=loadfile('taxon_details.json')['records']; thist=loadfile('taxon_history.json')['records']; tdiv=loadfile('diversity.json'); torg=loadfile('organisms.json')['representatives']; tgeo=loadfile('geologic_time.json')['source_hierarchy']; tguide=loadfile('rank_guides.json'); tsrc=loadfile('sources.json'); tmanifest=loadfile('manifest.json')
tax_tree={r['id']:r for r in ttax}; details_tree={r['taxon_id']:r for r in tdetails}; hist_tree={r['taxon_id']:r for r in thist}
assert len(tax_tree)==len(ttax)==238 and len(dtaxa)==200 and len(dint)==172 and len(torg)==95
assert not tree_mismatches

# Lossless preservation: both original ZIPs, loose uploads, all embedded images and extracted JSON.
for src,archive in [(SRC_T,TREE_Z),(SRC_D,DEEP_Z)]:
 dest=OUT/'source_archives'/archive.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(archive,dest)
for n in TREE_FILES:
 d=OUT/'source_exports'/SRC_T/n;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(BASE/n,d)
with zipfile.ZipFile(DEEP_Z) as dz:
 for rel,info in deep_file_map.items():
  if '..' in pathlib.PurePosixPath(rel).parts:raise ValueError('Unsafe ZIP path')
  dst=OUT/'source_exports'/SRC_D/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(dz.read(info))

# Match by named scientific identity, not by superficial source ID. Manual aliases are reviewed and explicit.
name_index=collections.defaultdict(list)
for t in ttax:name_index[t['id'].casefold()].append(t)
CURATED_ALIASES={'cyanobacteria':('Cyanobacteriota','Cyanobacteria is the source common name for the cyanobacterial phylum (Cyanobacteriota).'),
 'angiosperms':('Angiospermae','Angiosperms is the English rendering of the flowering-plant clade Angiospermae.')}
canonical=[]; tcross={};dcross={};matching=[];ambiguous_matches=[]; new_from_deep=[]
for t in ttax:
 cid=canon_id('taxon','tree:'+t['id']);tcross[t['id']]=cid
 canonical.append({'id':cid,'name':t['id'],'common_name':t.get('common_name'),
 'primary_rank':ranknorm(t['rank']),'rank_original':t['rank'], 'extinct':t['extinct'],
 'parent_id':None,'primary_classification_scheme':'tree_of_life_v1.7_educational',
 'classification_assertions':[],'alternative_classifications':[],
 'name_variants':[{'name':t['id'],'type':'source_label','source_export':SRC_T}],
 'source_records':[provenance(SRC_T,t['id'],'taxonomy.json')],
 'source_common_icon':t.get('icon'),'editorial_flags':[]})
lookup={c['id']:c for c in canonical}
for t in ttax:
 c=lookup[tcross[t['id']]]; par=t.get('parent_id');c['parent_id']=tcross.get(par) if par else None
 c['classification_assertions'].append({'source_export':SRC_T,'name':t['id'],'rank':t['rank'],'normalized_rank':ranknorm(t['rank']),'parent_id':c['parent_id'],'source_parent_id':par,'source_data_semantics':'educational navigation topology; not consensus phylogeny'})

for d in dtaxa:
 di=d['id'];n=d['name'];rank=d['rankLabel'];normalized=ranknorm(rank);method=None;to=None;reason=None
 if di=='bacteria':to=tax_tree.get('Bacteria_domain');method='domain_identity_selected_over_same-name-kingdom';reason='Deep Time calls Bacteria a Domain, while Tree contains separate Domain and Kingdom records.'
 elif di=='archaea':to=tax_tree.get('Archaea_domain');method='domain_identity_selected_over_same-name-kingdom';reason='Deep Time calls Archaea a Domain, while Tree contains separate Domain and Kingdom records.'
 elif di in CURATED_ALIASES:
  id_,reason=CURATED_ALIASES[di];to=tax_tree.get(id_);method='curated_taxonomic_alias'
 elif n.casefold() in name_index:
  candidates=name_index[n.casefold()]
  if len(candidates)==1:to=candidates[0];method='exact_scientific_name'
  else:
   equivalent=[c for c in candidates if ranknorm(c['rank'])==normalized]
   if len(equivalent)==1:to=equivalent[0];method='exact_scientific_name_rank_disambiguated'
   else:ambiguous_matches.append({'deep_id':di,'name':n,'candidate_tree_ids':[x['id'] for x in candidates],'reason':'non-unique scientific name and rank'});
 if to:
  cid=tcross[to['id']];kind='matched';matching.append({'deep_id':di,'deep_name':n,'tree_id':to['id'],'canonical_id':cid,'matching_method':method,'rationale':reason,'rank_agreement':ranknorm(to['rank'])==normalized})
 else:
  cid=canon_id('taxon','deep:'+di);kind='deep_only';new_from_deep.append(di)
  c={'id':cid,'name':n,'common_name':None,'primary_rank':normalized,'rank_original':rank,'extinct':None,'parent_id':None,'primary_classification_scheme':'unplaced_deep_time_source_concept',
    'classification_assertions':[],'alternative_classifications':[], 'name_variants':[], 'source_records':[], 'source_common_icon':None,
    'editorial_flags':['deep_time_cladogram_is_unstructured','canonical_parent_unresolved']}
  lookup[cid]=c;canonical.append(c)
 dcross[di]=cid;c=lookup[cid]
 c['source_records'].append(provenance(SRC_D,di,'data/taxa.json'))
 c['name_variants'].append({'name':n,'type':'deep_time_display_name','source_export':SRC_D})
 cl={'source_export':SRC_D,'name':n,'rank':rank,'normalized_rank':normalized,'parent_id':None,'source_parent_id':None,
     'source_data_semantics':'free-text illustrative cladogram, not a validated parent-child graph',
     'literal_cladogram':d.get('clade'),'kind':d.get('kind')}
 c['classification_assertions'].append(cl)
 if kind=='matched' and normalized!=c['primary_rank']:
  c['alternative_classifications'].append({'source_export':SRC_D,'rank':rank,'reason':'source_ranks_differ; no implicit reclassification'})
  c['editorial_flags'].append('cross_source_rank_disagreement')

# Sources merged by URL identity; per-source instances preserved for provenance.
references=[];ref_by_url={};source_ref_map={}
def add_reference(source,record,old_id,filename):
 url=(record.get('url') or '').strip();normalized=url.rstrip('/')
 cid=ref_by_url.get(normalized)
 if not cid:
  cid=canon_id('source',normalized or source+old_id)
  references.append({'id':cid,'url':url or None,'title':record.get('label') or record.get('title'), 'publication_date':None,'link_check_status':'not_checked',
   'usage':'general_unless_explicit_population','source_claims':[]})
  ref_by_url[normalized]=cid
 r=next(x for x in references if x['id']==cid)
 r['source_claims'].append({'source_export':source,'source_reference_id':old_id,'source_file':filename,'citation_usage':record.get('citation_usage') or record.get('cited_for')})
 source_ref_map[(source,old_id)]=cid
for r in tsrc['references']:add_reference(SRC_T,r,r['reference_id'],'sources.json')
for r in drefs['references']:add_reference(SRC_D,r,r['id'],'data/source_references.json')

# Names/details: one canonical details record per concept with ALL conflicting text retained per source.
canon_details=[];canon_hist=[];taxonomy_conflicts=[];age_comparisons=[];name_variants=[]
for c in canonical:
 cid=c['id'];tid=next((x['source_id'] for x in c['source_records'] if x['source_export']==SRC_T),None);did=next((x['source_id'] for x in c['source_records'] if x['source_export']==SRC_D),None)
 values=[]; histories=[]
 if tid:
  t=details_tree[tid];hist=hist_tree[tid]
  values.append({'source_export':SRC_T,'source_taxon_id':tid,'pronunciation':t.get('pronunciation'),'etymology':t.get('etymology'),
    'description':t.get('evolutionary_history_text'),'diagnostic_characteristics':t.get('distinguishing_traits_text'),'adaptations':None,
    'original_diversity_or_population_text':t.get('original_diversity_or_population_text'),'verbatim_source_record':t})
  histories.append({'source_export':SRC_T,'source_taxon_id':tid,'origin_ma':hist.get('estimated_lineage_origin_ma'),
    'origin_age_type':'unspecified_approximate_lineage_origin','earliest_fossil_ma':None,'crown_origin_ma':None,'stem_divergence_ma':None,
    'lineage_end_ma':hist.get('lineage_end_ma'),'lineage_end_type':hist.get('end_date_type'),'extinct':hist.get('extinct'),
    'uncertainty_ma':None,'citation_ids':[],'verbatim_source_record':hist})
 if did:
  d=next(x for x in dtaxa if x['id']==did)
  values.append({'source_export':SRC_D,'source_taxon_id':did,'pronunciation':d.get('pron'),'etymology':d.get('etym'),
    'description':d.get('what'),'diagnostic_characteristics':d.get('traits'),'adaptations':None,'tagline':d.get('tagline'),
    'literal_cladogram':d.get('clade'),'verbatim_source_record':d})
  da=d.get('lineage_age') or {};histories.append({'source_export':SRC_D,'source_taxon_id':did,'origin_ma':da.get('first_ma'),
    'origin_age_type':'approximate_first_range_boundary_unspecified_biological_meaning','earliest_fossil_ma':None,'crown_origin_ma':None,'stem_divergence_ma':None,
    'lineage_end_ma':da.get('last_ma'),'lineage_end_type':'approximate_last_range_boundary_not_necessarily_extinction','extinct':d.get('extinction',{}).get('is_extinct_explicit'),
    'uncertainty_ma':None,'citation_ids':[],'verbatim_source_record':da,
    'source_example_statuses':d.get('extinction',{}).get('source_status_texts',[])})
  if tid:
   a=details_tree[tid]
   if d.get('pron') and a.get('pronunciation') and d['pron']!=a['pronunciation']:
    taxonomy_conflicts.append({'type':'pronunciation_variant','taxon_id':cid,'source_values':[{ 'source_export':SRC_T,'value':a['pronunciation']},{'source_export':SRC_D,'value':d['pron']}], 'interpretation':'Textual variation, both preserved.'})
 if len(histories)==2:
  a,b=histories
  if a['origin_ma'] is not None and b['origin_ma'] is not None and a['origin_ma']!=b['origin_ma']:
   age_comparisons.append({'taxon_id':cid,'tree_origin_ma':a['origin_ma'],'deep_time_first_ma':b['origin_ma'],'difference_ma':round(abs(a['origin_ma']-b['origin_ma']),6),
      'interpretation':'Unresolved date disagreement; source fields have non-equivalent evidence definitions. Do not treat as a calibrated crown/stem/fossil conflict.'})
 canon_details.append({'taxon_id':cid,'source_assertions':values,'preferred_description_source':SRC_T if tid else SRC_D,'editorial_note':'Source descriptions are source-attributed, not independently fact-checked.'})
 canon_hist.append({'taxon_id':cid,'source_age_assertions':histories,'canonical_crown_origin_ma':None,'canonical_stem_divergence_ma':None,'canonical_earliest_fossil_ma':None,
 'canonical_extinction_ma':None,'interpretation_status':'not_scientifically_recalibrated'})

# Explicit alternative parent assertions preserve differing schemes; Deep Time has no linked parents.
for m in matching:
 if not m['rank_agreement']:
  taxonomy_conflicts.append({'type':'rank_disagreement','taxon_id':m['canonical_id'],'tree_source_id':m['tree_id'],'deep_source_id':m['deep_id'],
    'tree_rank':tax_tree[m['tree_id']]['rank'],'deep_rank':next(x['rankLabel'] for x in dtaxa if x['id']==m['deep_id']),
    'interpretation':'Same named taxonomic concept represented with a different rank; retain both source assertions.'})

# Species richness and subdivision counts are a different data type from indexed clade counts.
def parse_amount(text):
 """Only normalize unambiguous source-native amounts; never infer a count from prose."""
 if isinstance(text,(int,float)) and not isinstance(text,bool):
  return {'estimate_type':'source_stated_number','value':text,'minimum':None,'maximum':None,'comparator':None,'unit_multiplier':1,'approximate':False}
 if not isinstance(text,str):return {'estimate_type':'unparsed','value':None,'minimum':None,'maximum':None,'comparator':None,'unit_multiplier':None,'approximate':None}
 raw=text.strip(); s=raw.lower().replace(',','').replace(' ','')
 approximate=bool(re.match('^[≈~]',s));s=re.sub('^[≈~]','',s)
 comp=None
 if s.startswith('≥'):comp='>=';s=s[1:]
 elif s.startswith('>'):comp='>';s=s[1:]
 elif s.startswith('≤'):comp='<=';s=s[1:]
 elif s.startswith('<'):comp='<';s=s[1:]
 # Trailing words allowed only for explicit postscript notes; keep raw.
 s=re.sub('livingbirds$','',s)
 m=re.fullmatch(r'(\d+(?:\.\d+)?)([kmb]?)(?:[–-](\d+(?:\.\d+)?)([kmb]?))?',s)
 if not m:return {'estimate_type':'unparsed','value':None,'minimum':None,'maximum':None,'comparator':comp,'unit_multiplier':None,'approximate':approximate}
 x,unit1,y,unit2=m.groups();mults={'':1,'k':1000,'m':1000000,'b':1000000000}
 mul1=mults[unit1 or unit2 or ''];mul2=mults[unit2 or unit1 or '']
 a=float(Decimal(x)*mul1);b=float(Decimal(y)*mul2) if y else None
 a=int(a) if a.is_integer() else a
 if b is not None:b=int(b) if b.is_integer() else b
 return {'estimate_type':'range' if b is not None else ('bound' if comp else 'approximate' if approximate else 'source_stated_number'),
  'value':None if b is not None or comp else a,'minimum':a if b is not None or comp in ('>=','>') else None,
  'maximum':b if b is not None else a if comp in ('<=','<') else None,'comparator':comp,
  'unit_multiplier':mul1,'approximate':approximate}

subs=[];pop=[]
for row in tdiv['worldwide_subdivision_count_references']:
 for rank,raw in row['estimates_by_rank'].items():
  parsed=parse_amount(raw)
  subs.append({'id':canon_id('estimate','subdiv:'+row['taxon_id']+':'+rank),'taxon_id':tcross[row['taxon_id']], 'count_kind':'estimated_extant_species_richness' if rank=='species' else 'estimated_taxonomic_subdivisions',
   'subdivision_rank':rank,'geographic_scope':'worldwide_reference_estimate','extant_status_scope':'extant_only_or_extant_focused_not_confirmed',
   'as_of_date':None,'source_reference_ids':[],'source_export':SRC_T,'verbatim_value':raw,'parsed':parsed,'units':'taxa_at_specified_rank',
   'uncertainty_note':'Source-native estimate or lower bound; assembled from multiple classification schemes; not a complete census.'})

# The primary source offers only text/heterogeneous units, so do not coerce into a single count.
org_by_name=collections.defaultdict(list)
for o in torg:org_by_name[o['name'].casefold()].append(o['key'])
for idx,row in enumerate(tdiv['population_estimates']):
 name=row['taxon_or_organism_name'];target=tcross.get(name);refid=ref_by_url.get((row.get('href') or '').rstrip('/'))
 # Safe parser for a single count in prose; unit semantics remain explicit, including mature individuals vs colonies.
 e=row.get('estimate','');se=e.lower().replace(',','')
 known_e='unknown' in se
 m=re.fullmatch(r'\s*([≈~>≥<≤]*)\s*(\d+(?:\.\d+)?)\s*(?:[–-]\s*(\d+(?:\.\d+)?))?\s*(billion|million|thousand)?\s+(wild individuals|surveyed individuals|individuals|mature birds|birds|wild individuals|overwintering butterflies|sharks in eastern australasia)\s*',se)
 parse={'estimate_type':'unknown' if known_e else 'unparsed','value':None,'minimum':None,'maximum':None,'unit':None,'approximate':None}
 if m:
  marker,lo,hi,unit,units=m.groups();factor={'billion':10**9,'million':10**6,'thousand':1000,None:1}[unit]
  a=float(lo)*factor;b=float(hi)*factor if hi else None
  parse={'estimate_type':'range' if b is not None else ('lower_bound' if '>' in marker or '≥' in marker else 'approximate' if '≈' in marker or '~' in marker else 'source_stated_number'),
    'value':a if not (b is not None or '>' in marker or '≥' in marker) else None,'minimum':a if (b is not None or '>' in marker or '≥' in marker) else None,
    'maximum':b,'unit':'mature_individuals' if 'mature' in units else 'individuals','approximate':bool('≈' in marker or '~' in marker)}
 # Special case Apis mellifera has TWO colony totals, not bees; retain two components.
 if name=='Apis mellifera':
  parse={'estimate_type':'two_components','value':None,'minimum':None,'maximum':None,'unit':'colonies',
    'components':[{'population_category':'wild','value':280000000,'unit':'colonies','qualifier':'approximate'},{'population_category':'managed','value':102000000,'unit':'colonies','qualifier':'source_rounded'}]}
 if name=='Prochlorococcus marinus':
  parse={'estimate_type':'species_unknown_genus_reference_only','value':None,'minimum':None,'maximum':None,'unit':None,
    'other_scope_assertion':{'name':'Prochlorococcus genus','estimated_cells':2.9e27,'unit':'cells','not_same_as_subject':True}}
 scope_text=row.get('scope') or ''
 years=[int(y) for y in re.findall(r'(?<![0-9])(?:19|20)[0-9]{2}(?![0-9])',scope_text)]
 # Years are recorded with their SOURCE precision; do not invent a calendar date.
 temporal={'original_text':scope_text,'reported_years':years,'observed_from_year':min(years) if years else None,
 'observed_to_year':max(years) if years else None,'exact_date_known':False}
 if len(years)==1:
  suffix=re.search(r'\b(?:19|20)[0-9]{2}\s*[–-]\s*([0-9]{2})\b',scope_text)
  if suffix:
   y2=years[0]//100*100+int(suffix.group(1));temporal['observed_to_year']=y2
 pop.append({'id':canon_id('estimate','population:'+str(idx)+':'+name),'subject_name':name,'subject_taxon_id':target,
  'subject_tree_organism_keys':org_by_name.get(name.casefold(),[]),'source_export':SRC_T,
  'source_reference_ids':[refid] if refid else [],'verbatim_estimate':e,'verbatim_scope':row.get('scope'),
  'geographic_scope':row.get('scope'),'as_of_date':None,'temporal_scope':temporal,'source_label':row.get('source'),
  'uncertainty_note':row.get('note'),'parsed':parse,'source_record':row})

# All organisms are retained as source-specific curated EXAMPLES, NOT species-rank index records.
org=[];media=[];image_id_tree_by_org={}
for o in torg:
 kid=o['key']; oid=canon_id('organism','tree:'+kid);rids=[]
 article=o.get('wikipedia_article_url');fallback=o.get('wikimedia_commons_fallback_url');filename=o.get('wikimedia_commons_fallback_filename')
 if article:
  mid=canon_id('image','tree:runtime:'+kid);media.append({'id':mid,'type':'runtime_wikipedia_article_image_resolution',
   'source_export':SRC_T,'source_organism_key':kid,'wikipedia_article_url':article,'image_url':None,
   'verification_status':'unchecked_network_runtime_image','license_status':'unknown','attribution_status':'unknown'});rids.append(mid)
 if filename or fallback:
  mid=canon_id('image','tree:commons:'+kid);media.append({'id':mid,'type':'wikimedia_commons_fallback', 'source_export':SRC_T,
   'source_organism_key':kid,'image_url':fallback,'filename':filename,'verification_status':'unchecked_external_url',
   'license_status':'unknown','attribution_status':'unknown'});rids.append(mid)
 org.append({'id':oid,'display_name':o['name'],'scientific_name':o['name'] if re.fullmatch(r'[A-Z][a-z]+\s[a-z-]+',o['name']) else None,
   'common_name':o['name'] if not re.fullmatch(r'[A-Z][a-z]+\s[a-z-]+',o['name']) else None,'linked_taxon_id':tcross[o['linked_taxon_id']],
   'link_semantics':'atlas_selected_branch_not_guaranteed_exact_species','living_status_source_text':o['status'],
   'description':o['source_record'].get('detail'), 'population_estimate_ids':[], 'image_reference_ids':rids,
   'source_records':[provenance(SRC_T,kid,'organisms.json')], 'verbatim_source_record':o})
 image_id_tree_by_org[kid]=rids

# Deep Time media: physical image bytes are checksum and decoding validated; external license not inferred.
image_key_lookup={}
for asset in dimages['images']:
 key=asset['image_key'];mid=canon_id('image','deep:'+key);image_key_lookup[key]=mid
 p=OUT/'source_exports'/SRC_D/asset['relative_path']
 # relative_path is usually prefixed images/...; verify using exported asset path.
 if not p.is_file():
  candidates=list((OUT/'source_exports'/SRC_D/'images').glob('*'))
  matches=[f for f in candidates if f.name==pathlib.Path(asset['relative_path']).name]
  if matches:p=matches[0]
 is_verified=p.is_file() and digest(p.read_bytes())==asset['sha256']
 decoded=False
 if p.is_file():
  try:
   with Image.open(p) as im:im.verify();decoded=True
  except Exception:pass
 media.append({'id':mid,'type':'bundled_illustrative_image','source_export':SRC_D,'source_image_key':key,
 'local_path':p.relative_to(OUT).as_posix() if p.is_file() else None,'original_relative_path':asset['relative_path'],
 'sha256':asset['sha256'],'mime_type':asset['mime_type'],'bytes':asset['bytes'],'credit':asset.get('credit'),
 'verification_status':'local_hash_and_decode_verified' if is_verified and decoded else 'local_file_verification_failed',
 'license_status':'source_says_illustrative_ai_art_not_verified_for_license','source_reference_ids':[],
 'external_url':None})
for d in dtaxa:
 for ix,e in enumerate(d['examples']):
  key=e.get('img');oid=canon_id('organism','deep:'+d['id']+':'+str(ix));cid=dcross[d['id']]
  org.append({'id':oid,'display_name':e.get('name'),'scientific_name':None,'common_name':e.get('name'),
   'linked_taxon_id':cid,'link_semantics':'illustrative_example_of_group_not_necessarily_exact_taxon',
   'living_status_source_text':e.get('status'),'description':None,'population_estimate_ids':[],
   'image_reference_ids':[image_key_lookup[key]] if key in image_key_lookup else [],
   'source_records':[provenance(SRC_D,d['id']+':example:'+str(ix),'data/taxa.json')],
   'source_example_index':ix,'source_parent_taxon_id':d['id'],'verbatim_source_record':e})

# Annotate population references where possible without assuming species example is a taxon.
by_display=collections.defaultdict(list)
for x in org:by_display[(x['display_name'] or '').casefold()].append(x)
for p in pop:
 for x in by_display.get(p['subject_name'].casefold(),[]):x['population_estimate_ids'].append(p['id'])

# Deep Time chronological intervals form primary graph. Tree time is a second age scheme, not a redefinition.
grank={0:'Scale',1:'Eon',2:'Era',3:'Period',4:'Epoch_or_series',5:'Age_or_stage'}
intervals=[];dc_geo={};tc_geo={};gname=collections.defaultdict(list);geodiff=[]
for x in dint:
 cid=canon_id('geo','deep:'+x['id']);dc_geo[x['id']]=cid;gname[x['name'].casefold()].append(x)
for x in dint:
 cid=dc_geo[x['id']];par=x.get('parent');intervals.append({'id':cid,'name':x['name'],'rank':grank[x['rank']],
  'rank_original':x['rank'],'parent_id':dc_geo.get(par),'older_boundary_ma':float(x['start']),
  'younger_boundary_ma':float(x['end']), 'boundary_uncertainty_ma':None,
  'classification_scheme':'deep_time_ics_2026_06_widget_rendering',
  'source_assertions':[{'source_export':SRC_D,'source_interval_id':x['id'],'old_ma':x['start'],'young_ma':x['end'],
    'source_rank':x['rank'],'source_parent_id':par,'canonical_parent_id':dc_geo.get(par)}],
  'original_description':{'summary':x.get('summary'),'climate':x.get('climate'),'geo':x.get('geo'),'continents':x.get('continents'),
    'life':x.get('life'),'etym':x.get('etym'),'events':x.get('events')},
  'alternate_parent_assertions':[], 'source_taxon_link_assertions':[]})
glookup={x['id']:x for x in intervals}

def tree_walk(n,parent_id=None):
 name=n['name'];rank=n['rank'];candidate=gname.get(name.casefold(),[])
 # Disambiguate by name; rank is not always comparable (Deep numeric names); source ID match if possible.
 if len(candidate)==1:cid=dc_geo[candidate[0]['id']]
 else:
  cid=canon_id('geo','tree:'+name+':'+rank)
  intervals.append({'id':cid,'name':name,'rank':rank,'rank_original':rank,'parent_id':None,'older_boundary_ma':float(n['old']),
   'younger_boundary_ma':float(n['young']),'boundary_uncertainty_ma':None,'classification_scheme':'tree_of_life_v1.7_geologic',
   'source_assertions':[],'original_description':None,'alternate_parent_assertions':[], 'source_taxon_link_assertions':[]})
  glookup[cid]=intervals[-1]
 tc_geo[name]=cid;g=glookup[cid]
 g['source_assertions'].append({'source_export':SRC_T,'source_interval_id':name,'old_ma':n['old'],'young_ma':n['young'],
   'source_rank':rank,'source_parent_id':parent_id,'canonical_parent_id':tc_geo.get(parent_id) if parent_id else None})
 if parent_id:
  cp=tc_geo[parent_id]
  if g['parent_id'] is None and cid not in dc_geo.values():g['parent_id']=cp
  elif cp!=g['parent_id']:g['alternate_parent_assertions'].append({'source_export':SRC_T,'parent_id':cp,'source_parent_name':parent_id})
 if len(g['source_assertions'])>1:
  a=g['source_assertions'][0];b=g['source_assertions'][-1]
  if (a['old_ma']!=b['old_ma'] or a['young_ma']!=b['young_ma']):
   geodiff.append({'interval_id':cid,'interval_name':name,'source_bounds':[{ 'source_export':a['source_export'],'old_ma':a['old_ma'],'young_ma':a['young_ma']},{'source_export':b['source_export'],'old_ma':b['old_ma'],'young_ma':b['young_ma']}],
     'interpretation':'Conflicting source vintages, rounding, or stage boundary revisions; Deep Time values retained as primary for its detailed scheme.'})
 for ch in n.get('children',[]):tree_walk(ch,name)
tree_walk(tgeo)

# Curated vs UI-computed age interval links must never be merged into one "evidence" field.
curated=[];inferred=[]
for ix,ln in enumerate(dlinks['source_curated_direct_links']):
 cid=dcross.get(ln['taxon_id']);gid=dc_geo.get(ln['geologic_interval_id'])
 curated.append({'id':canon_id('geolink','curated:'+str(ix)), 'interval_id':gid,'taxon_id':cid,
  'type':'source_curated_direct_association','confidence':'source_widget_curated_not_independently_verified',
  'source_export':SRC_D,'verbatim_source_record':ln})
for ix,ln in enumerate(dlinks['ui_inferred_age_range_links']):
 inferred.append({'id':canon_id('geolink','inferred:'+str(ix)), 'interval_id':dc_geo.get(ln['geologic_interval_id']),
  'taxon_id':dcross.get(ln['taxon_id']),'type':'ui_age_range_filter_match',
  'scientific_evidence':False,'source_export':SRC_D,'verbatim_source_record':ln})

# Rank guides, additional geologic science, paleogeography and original logic retained without laundering derived data.
guides={'schema_version':SCHEMA_V,'guides':[]}
for rank,item in tguide['guides'].items():guides['guides'].append({'id':canon_id('rank',rank),'name':rank, 'source_export':SRC_T,'source_record':item})

# Structured preservation of Deep's other reusable evolutionary/geologic data.
with zipfile.ZipFile(DEEP_Z) as dz:
 extras={n:json.loads(dz.read(prefix+n)) for n in ['data/geologic_details.json','data/paleogeography.json','data/source_logic.json','data/taxon_source_layers.json']}
dump({'schema_version':SCHEMA_V,'units':'Ma before present','intervals':intervals,
 'deep_time_original_rank_codes':grank,'note':'Primary chronology from Deep Time Atlas; alternate Tree of Life boundaries retained under source_assertions.'},'geologic_time.json')
dump({'schema_version':SCHEMA_V,'records':canonical,'classification_schemes':[
 {'id':'tree_of_life_v1.7_educational','description':'Source hierarchy for Tree of Life; includes seven-kingdom categories and unranked clades.'},
 {'id':'unplaced_deep_time_source_concept','description':'Deep Time textual cladograms are unlinked assertions. Do not invent parent-child edges.'}]},'taxonomy.json')
dump({'schema_version':SCHEMA_V,'records':canon_details},'taxon_details.json')
dump({'schema_version':SCHEMA_V,'records':canon_hist,'units':'Ma before present'},'taxon_history.json')
dump({'schema_version':SCHEMA_V,'subdivision_estimates':subs,'population_estimates':pop,
 'interpretation':'Indexed records, subdivision estimates, species richness and living-individual populations have separate units and scopes.'},'diversity.json')
dump({'schema_version':SCHEMA_V,'representatives':org,'record_kind':'representative examples, not exhaustive species inventory'},'organisms.json')
dump(guides,'rank_guides.json')
dump({'schema_version':SCHEMA_V,'references':references,
 'original_source_general_notes':[{'source_export':SRC_T,'text':tsrc.get('original_footer_cautions')},
 {'source_export':SRC_D,'text':drefs.get('completeness')}],
 'citations_per_claim_coverage':'incomplete; do not conflate a general source URL with taxon-specific scientific verification'},'sources.json')
dump({'schema_version':SCHEMA_V,'media':media,'image_source_notes':'Deep: local generated illustrative paleoart. Tree: external runtime Wikimedia images not verified.'},'images_manifest.json')
dump({'schema_version':SCHEMA_V,'curated_direct_associations':curated,
 'ui_inferred_age_filter_matches':inferred,'ui_inference_rule':dlinks['ui_inference_rule'],
 'migration_rule':'Never promote age-filter matches to fossil observations or reviewed evolutionary ranges.'},'geologic_taxon_links.json')
dump({'schema_version':SCHEMA_V,'deep_time_data':extras,'source_export':SRC_D,
 'canonical_science_status':'preserved raw claim and heuristic, not externally verified.'},'additional_science.json')

tmap=[{'source_export':SRC_T,'source_id':k,'canonical_id':v,'source_file':'taxonomy.json'} for k,v in tcross.items()]
tmap.extend({'source_export':SRC_D,'source_id':k,'canonical_id':v,'source_file':'data/taxa.json'} for k,v in dcross.items())
gmap=[{'source_export':SRC_T,'source_id':k,'canonical_id':v,'source_file':'geologic_time.json'} for k,v in tc_geo.items()]
gmap.extend({'source_export':SRC_D,'source_id':k,'canonical_id':v,'source_file':'data/geologic_intervals.json'} for k,v in dc_geo.items())
dump({'schema_version':SCHEMA_V,'taxa':tmap,'geologic_intervals':gmap,
 'identity_resolution':{'exact_name_matches':sum(m['matching_method'].startswith('exact_scientific_name') for m in matching),
 'explicit_domain_resolution':sum(m['matching_method']=='domain_identity_selected_over_same-name-kingdom' for m in matching),
 'curated_synonyms':sum(m['matching_method']=='curated_taxonomic_alias' for m in matching),'all_matches':matching,
 'unmatched_deep_ids':new_from_deep,'ambiguous_candidates':ambiguous_matches},
 'id_stability_contract':'Never recompute or change an already-issued canonical ID; reuse this mapping in all future releases.'},'ID_MAPPING.json')

# Machine-readable reconciliation: every differing numeric value, rank and pronunciation, plus known conceptual hazards.
issue_notes=[{'id':f'tree:{i+1}','source_export':SRC_T,'text':line.strip()} for i,line in enumerate((BASE/'AMBIGUITIES.md').read_text().splitlines()) if line.strip().startswith(tuple(f'{j}.' for j in range(1,16)))]
issue_notes.extend({'id':x['id'],'source_export':SRC_D,'area':x['area'],'severity':x['severity'],'text':x['description']} for x in dambi['findings'])
dump({'schema_version':SCHEMA_V,'cross_source_matches':matching,'rank_and_text_conflicts':taxonomy_conflicts,
 'dated_lineage_ambiguities':age_comparisons,'geologic_boundary_conflicts':geodiff,
 'source_ambiguities':issue_notes,'ambiguous_identity_candidates':ambiguous_matches,
 'scientific_review_status':'scientific_source_conflicts_preserved_pending_external_authority_review'},'RECONCILIATION_REPORT.json')

stats={
 'taxa_total_canonical':len(canonical),'taxa_source_tree':len(ttax),'taxa_source_deep':len(dtaxa),
 'taxa_added_tree_before_merging':len(ttax),'taxa_added_deep_unique':len(new_from_deep),'duplicate_taxon_source_records_reconciled':len(matching),
 'unranked_clade_records':sum(1 for c in canonical if 'clade' in c['primary_rank'].lower()),
 'ranked_taxonomic_concept_records':sum(1 for c in canonical if c['primary_rank'] not in ('clade','informal group','informal grade','assemblage','group','traditional group','historical group','extinct / debated clade','extinct lineage') and c['primary_rank'] not in ('root','')), 
 'organism_example_records':len(org),'organism_examples_tree':len(torg),'organism_examples_deep':sum(len(x['examples']) for x in dtaxa),
 'population_estimate_records':len(pop),'population_estimates_with_explicit_unknown':sum(x['parsed']['estimate_type']=='species_unknown_genus_reference_only' for x in pop),
 'subdivision_reference_taxa':len(tdiv['worldwide_subdivision_count_references']),'subdivision_estimate_values':len(subs),
 'image_reference_records':len(media),'images_bundled_locally':len(dimages['images']),
 'images_local_content_verified':sum(x['verification_status']=='local_hash_and_decode_verified' for x in media),
 'images_external_links_checked':0,'image_references_tree_runtime':len(torg),'image_references_tree_commons_fallback':sum(bool(x.get('wikimedia_commons_fallback_filename')) for x in torg),
 'deep_time_example_image_usages':sum(len(x['image_reference_ids']) for x in org if x['source_records'][0]['source_export']==SRC_D),
 'geologic_intervals_canonical':len(intervals),'geologic_intervals_tree_source':len(tc_geo),'geologic_intervals_deep_source':len(dint),
 'curated_interval_taxon_associations':len(curated),'derived_ui_age_filter_matches':len(inferred),
 'source_reference_records_canonical':len(references), 'source_reference_entries_tree':len(tsrc['references']), 'source_reference_entries_deep':len(drefs['references']),
 'rank_disagreements':sum(x['type']=='rank_disagreement' for x in taxonomy_conflicts),
 'lineage_age_source_differences':len(age_comparisons),'geologic_boundary_source_differences':len(geodiff),
 'source_ambiguity_notes':len(issue_notes),'unresolved_scientific_ambiguities':len(issue_notes)+len(age_comparisons)+len(geodiff)+sum(x['type']=='rank_disagreement' for x in taxonomy_conflicts)
}
# JSON schema generators provide required core typing + typed estimate records; raw source records remain extensible.
def schema_record(req,props,extra=True):return {'type':'object','required':req,'properties':props,'additionalProperties':extra}
S={'schema_version':{'type':'string','const':SCHEMA_V}}
ID={'type':'string','pattern':'^stx:'};ST={'type':'string'};NULL_ID={'anyOf':[ID,{'type':'null'}]};NUM={'type':['number','null']}
def records_schema(key,required,properties):
 return {'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object',
 'required':['schema_version',key], 'properties':{**S,key:{'type':'array','items':schema_record(required,properties)}},'additionalProperties':True}
schemas={
 'taxonomy.json':records_schema('records',['id','name','parent_id','classification_assertions'],{'id':ID,'name':ST,'parent_id':NULL_ID,'classification_assertions':{'type':'array'},'extinct':{'type':['boolean','null']}}),
 'taxon_details.json':records_schema('records',['taxon_id','source_assertions'],{'taxon_id':ID,'source_assertions':{'type':'array','minItems':1}}),
 'taxon_history.json':records_schema('records',['taxon_id','source_age_assertions','canonical_crown_origin_ma'],{'taxon_id':ID,'source_age_assertions':{'type':'array','minItems':1},'canonical_crown_origin_ma':NUM}),
 'diversity.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['schema_version','subdivision_estimates','population_estimates'],'properties':{**S,
 'subdivision_estimates':{'type':'array','items':schema_record(['id','taxon_id','subdivision_rank','parsed'],{'id':ID,'taxon_id':ID,'subdivision_rank':ST,'parsed':{'type':'object','required':['estimate_type','value','minimum','maximum']}})},
 'population_estimates':{'type':'array','items':schema_record(['id','subject_name','parsed','verbatim_estimate'],{'id':ID,'subject_name':ST,'parsed':{'type':'object'},'verbatim_estimate':ST})}}},
 'organisms.json':records_schema('representatives',['id','display_name','linked_taxon_id','image_reference_ids'],{'id':ID,'display_name':ST,'linked_taxon_id':ID,'image_reference_ids':{'type':'array','items':ID}}),
 'geologic_time.json':records_schema('intervals',['id','name','parent_id','older_boundary_ma','younger_boundary_ma'],{'id':ID,'name':ST,'parent_id':NULL_ID,'older_boundary_ma':{'type':'number','minimum':0},'younger_boundary_ma':{'type':'number','minimum':0}}),
 'rank_guides.json':records_schema('guides',['id','name','source_record'],{'id':ID,'name':ST,'source_record':{'type':'object'}}),
 'sources.json':records_schema('references',['id','source_claims'],{'id':ID,'url':{'type':['string','null']},'source_claims':{'type':'array','minItems':1}}),
 'images_manifest.json':records_schema('media',['id','type','verification_status'],{'id':ID,'type':ST,'verification_status':ST}),
 'geologic_taxon_links.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object', 'required':['schema_version','curated_direct_associations','ui_inferred_age_filter_matches'], 'properties':{**S,'curated_direct_associations':{'type':'array','items':schema_record(['id','interval_id','taxon_id','type'],{'id':ID,'interval_id':ID,'taxon_id':ID,'type':ST})},'ui_inferred_age_filter_matches':{'type':'array','items':schema_record(['id','interval_id','taxon_id','scientific_evidence'],{'id':ID,'interval_id':ID,'taxon_id':ID,'scientific_evidence':{'const':False}})}}},
 'additional_science.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['schema_version','deep_time_data'], 'properties':{**S,'deep_time_data':{'type':'object'}}},
 'VALIDATION_REPORT.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['dataset','version','schema_version','validation_status','checks','statistics'], 'properties':{'dataset':ST,'version':ST,'schema_version':ST,'validation_status':ST,'checks':{'type':'array'},'statistics':{'type':'object'}}},
 'manifest.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['dataset','dataset_version','release_date','schema_version','source_exports','counts','files'], 'properties':{'dataset':ST,'dataset_version':ST,'release_date':{'type':'string','format':'date'},'schema_version':ST,'source_exports':{'type':'array','minItems':2},'counts':{'type':'object'},'files':{'type':'array','minItems':1}}},
 'ID_MAPPING.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['schema_version','taxa','geologic_intervals'], 'properties':{**S,'taxa':{'type':'array','items':schema_record(['source_export','source_id','canonical_id'],{'source_export':ST,'source_id':ST,'canonical_id':ID})},'geologic_intervals':{'type':'array','items':schema_record(['source_export','source_id','canonical_id'],{'source_export':ST,'source_id':ST,'canonical_id':ID})}}},
 'RECONCILIATION_REPORT.json':{'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':['schema_version','cross_source_matches','source_ambiguities'], 'properties':{**S,'cross_source_matches':{'type':'array'},'source_ambiguities':{'type':'array'}}}
}
for name,sch in schemas.items():dump(sch,'schemas/'+name+'.schema.json')

# Explicit referential audits.
checks=[]
def chk(name,errors, severity='error'):
 checks.append({'check':name,'status':'PASS' if not errors else 'FAIL' if severity=='error' else 'WARNING','severity':severity,'error_count':len(errors),'examples':errors[:12]});return not errors

allids=[x['id'] for x in canonical];idset=set(allids);geoidset={x['id'] for x in intervals};imgids={x['id'] for x in media};refids={x['id'] for x in references}
chk('unique_canonical_taxon_ids',[x for x,n in collections.Counter(allids).items() if n>1])
chk('primary_taxon_parent_refs',[x['id'] for x in canonical if x['parent_id'] and x['parent_id'] not in idset])
chk('taxon_source_inventory_crosswalk',[src for src,expected,mp in [(SRC_T,len(ttax),tcross),(SRC_D,len(dtaxa),dcross)] if len(mp)!=expected or any(x not in idset for x in mp.values())])
chk('taxon_source_entry_multiplicity',[c['id'] for c in canonical if not c['source_records'] or any(s['source_export'] not in (SRC_T,SRC_D) for s in c['source_records'])])
chk('taxon_hierarchy_cycle',[
 c['id'] for c in canonical if (lambda start:(lambda f:f(f,start,set()))(lambda f,k,vis:False if k is None else True if k in vis else f(f,lookup[k]['parent_id'],vis|{k})))(c['id'])])
chk('taxon_detail_history_relationships',[x['taxon_id'] for x in canon_details+canon_hist if x['taxon_id'] not in idset])
chk('organism_taxon_references',[x['id'] for x in org if x['linked_taxon_id'] not in idset])
chk('organism_image_references',[x['id'] for x in org if any(k not in imgids for k in x['image_reference_ids'])])
chk('subdivision_taxon_references',[x['id'] for x in subs if x['taxon_id'] not in idset])
chk('population_source_reference_integrity',[x['id'] for x in pop if any(k not in refids for k in x['source_reference_ids'])])
chk('population_estimates_scope_source_metadata',[x['id'] for x in pop if not x['geographic_scope'] or not x['source_label'] or not x['uncertainty_note']])
chk('population_estimates_no_spurious_speciation_counts',[x['id'] for x in pop if x['subject_name']=='Prochlorococcus marinus' and x['parsed']['value'] is not None])
chk('geologic_parent_references',[g['id'] for g in intervals if g['parent_id'] and g['parent_id'] not in geoidset])
chk('geologic_boundary_ordering',[g['id'] for g in intervals if g['older_boundary_ma']<g['younger_boundary_ma'] or g['younger_boundary_ma']<0])
chk('history_origin_extinction_range_consistency',[(x['taxon_id'],a['origin_ma'],a['lineage_end_ma']) for x in canon_hist for a in x['source_age_assertions'] if a['origin_ma'] is not None and a['lineage_end_ma'] is not None and a['origin_ma']<a['lineage_end_ma']])
chk('history_all_ages_nonnegative',[(x['taxon_id'],k,a[k]) for x in canon_hist for a in x['source_age_assertions'] for k in ('origin_ma','lineage_end_ma') if a[k] is not None and a[k]<0])
chk('taxon_parent_origin_chronology',[(c['id'],c['parent_id']) for c in canonical if c['parent_id'] and hist_tree.get(next((x['source_id'] for x in c['source_records'] if x['source_export']==SRC_T),''),{}).get('estimated_lineage_origin_ma') is not None and hist_tree.get(next((x['source_id'] for x in lookup[c['parent_id']]['source_records'] if x['source_export']==SRC_T),''),{}).get('estimated_lineage_origin_ma') is not None and hist_tree[next(x['source_id'] for x in c['source_records'] if x['source_export']==SRC_T)]['estimated_lineage_origin_ma']>hist_tree[next(x['source_id'] for x in lookup[c['parent_id']]['source_records'] if x['source_export']==SRC_T)]['estimated_lineage_origin_ma']])
chk('alternate_geologic_parent_assertions',[(g['id'],a['parent_id']) for g in intervals for a in g['alternate_parent_assertions'] if a['parent_id'] not in geoidset])
chk('alternate_taxonomic_classifications',[(c['id'],a) for c in canonical for a in c['classification_assertions'] if a['parent_id'] and a['parent_id'] not in idset])
chk('geologic_hierarchy_parent_duration',[g['id'] for g in intervals if g['parent_id'] and
  (g['older_boundary_ma']>glookup[g['parent_id']]['older_boundary_ma']+0.1 or g['younger_boundary_ma']<glookup[g['parent_id']]['younger_boundary_ma']-0.1)])
chk('geologic_hierarchy_cycle',[
 g['id'] for g in intervals if (lambda start:(lambda f:f(f,start,set()))(lambda f,k,vis:False if k is None else True if k in vis else f(f,glookup[k]['parent_id'],vis|{k})))(g['id'])])
chk('geologic_taxon_links',[x['id'] for x in curated+inferred if x['taxon_id'] not in idset or x['interval_id'] not in geoidset])
chk('geologic_curated_and_inferred_partition',[len(curated),len(inferred)] if len(curated)!=580 or len(inferred)!=8916 else [])
chk('cross_source_duplicate_mapping',[m['canonical_id'] for m in matching if tcross[m['tree_id']]!=dcross[m['deep_id']]])
chk('geologic_time_source_inventory',[len(tc_geo),len(dc_geo)] if len(tc_geo)!=44 or len(dc_geo)!=172 else [])
chk('image_local_artwork_integrity',[x['id'] for x in media if x['type']=='bundled_illustrative_image' and x['verification_status']!='local_hash_and_decode_verified'])
chk('scientific_uncertainties_documented',[] if issue_notes and geodiff and age_comparisons else ['unreconciled divergence tracking absent'])
chk('external_image_urls_unverified',[] if all('verified' not in x['verification_status'] for x in media if x['type']!='bundled_illustrative_image') else ['External image verification incorrectly asserted'])
chk('source_tree_zip_checksum_inventory',tree_mismatches)
chk('source_deep_file_inventory',[str(len(deep_file_map))] if len(deep_file_map)!=deep_member_count else [])
chk('source_export_original_record_counts',[len(ttax),len(dtaxa),len(dint),len(torg),len(curated),len(inferred)] if [len(ttax),len(dtaxa),len(dint),len(torg),len(curated),len(inferred)] != [238,200,172,95,580,8916] else [])

schema_errors=[]
for name,sch in schemas.items():
 Draft202012Validator.check_schema(sch)
 if name in ('manifest.json','VALIDATION_REPORT.json'):continue
 data=json.loads((OUT/name).read_text(encoding='utf8'))
 schema_errors += [name+': '+str(e) for e in Draft202012Validator(sch).iter_errors(data)]
chk('json_schemas_correctness_and_conformity',schema_errors)
for name in schemas:assert (OUT/name).is_file()

schema_count=len(schemas)
validation={'dataset':'Shared Taxa','version':VERSION,'date':FDATE,'schema_version':SCHEMA_V,
 'validation_status':'PASS_WITH_DOCUMENTED_SCIENTIFIC_WARNINGS' if not any(c['status']=='FAIL' for c in checks) else 'FAIL',
 'checks':checks,'statistics':stats,
 'scientific_verification':'Scientific claims and source URLs are not independently checked; substantial unresolved historical interpretation questions remain.',
 'source_export_checksums':{SRC_T:digest(TREE_Z.read_bytes()),SRC_D:digest(DEEP_Z.read_bytes())},
 'content_integrity':'Source archives, source exports and Deep Time illustration byte copies all included.'}
dump(validation,'VALIDATION_REPORT.json')
assert not list(Draft202012Validator(schemas['VALIDATION_REPORT.json']).iter_errors(validation))

# Markdown summaries and actual expandable changelog (HTML <details open>).
textout(f'''# Shared Taxa v{VERSION}\n\n**Release date:** {FDATE}  
**Schema:** {SCHEMA_V}  
**Validation:** {validation['validation_status']}\n\n## Reconciliation overview\n\n- Tree of Life Explorer v1.7 supplied **238** unique source nodes (237 indexed descendants plus hidden root).\n- Deep Time Atlas v1.6 supplied **200** source taxon profiles; **{len(matching)}** mapped to an existing Tree concept and **{len(new_from_deep)}** retained as additional concepts.\n- **{len(canonical)}** canonical concepts in this release, including educational nodes and unplaced historical groups; not an estimate of worldwide extant taxa.\n- **{len(org)}** source representative examples (95 Tree, 400 Deep). These examples are not an exhaustive species census.\n- **{len(intervals)}** canonical geologic intervals; preserve {len(geodiff)} inter-source boundary disagreements.\n- **{len(curated)}** curated Deep Time interval–taxon associations separate from **{len(inferred)}** UI age-filter display matches.\n- **{len(media)}** media references: 23 bundled images decoded and hash-verified locally; external images were not URL-tested.\n\n## Files\n\nThe root contains `taxonomy.json`, `taxon_details.json`, `taxon_history.json`, `diversity.json`, `organisms.json`, `geologic_time.json`, `rank_guides.json`, `sources.json`, `images_manifest.json`, `geologic_taxon_links.json`, `additional_science.json`, `manifest.json`, `ID_MAPPING.json`, `VALIDATION_REPORT.json`, and `RECONCILIATION_REPORT.json`.\n\nMachine-readable JSON Schema 2020-12 files live in `schemas/`. `source_exports/` and `source_archives/` preserve both original datasets and images losslessly.\n\n## Rules for consumers\n\n1. Join on canonical IDs from `ID_MAPPING.json`, **not** original widget IDs or names.\n2. Accept `parent_id:null` for Deep Time concepts without scientifically grounded parent mapping; do not infer edges from literal cladogram text.\n3. Read `classification_assertions[]` to distinguish ranking conventions.\n4. Read source values under `source_age_assertions[]`; canonical crown/stem/earliest fossil ages remain **null** without specific evidence.\n5. Do not use `ui_inferred_age_filter_matches` as observations or curated fossil-range evidence.\n6. Population, taxonomic subdivisions and indexed record counts are separate kinds of quantities; unknown remains null.\n7. Per-taxon citations remain sparse. Source URL presence is not independent verification.\n8. Deep Time artworks are illustrative AI-generated images, and Tree images are runtime references with unverified licenses.\n9. Do not remove embedded data from either original widget until separately tested migrations are complete.\n\n## Release rollback and stability\n\nv1.0 is fully self-contained. Keep this ZIP immutable and retain `ID_MAPPING.json`. Use stable IDs forever; future minor versions add records, while a breaking schema or ID migration needs a major version bump with a documented crosswalk.\n''','README.md')
textout(f'''# Shared Taxa changelog\n\n## v{VERSION} — {FDATE}\n\n- Reconciled all 238 Tree of Life source taxon records and 200 Deep Time source profiles using conservative taxon concept matching.\n- Produced {len(canonical)} canonical taxon concepts, with {len(matching)} matched cross-source profiles and full source-ID mapping.\n- Preserved all source records, alternative ranks, lineage ages and incompatible source definitions.\n- Integrated 172 Deep Time intervals and 44 Tree of Life interval source records into {len(intervals)} canonical intervals, preserving boundary disagreements.\n- Retained 495 organism-example records, numeric diversity metadata and population estimate units without conflation.\n- Preserved 23 local illustrative images with checksum verification; no external image-link verification claimed.\n- Added JSON schemas, validation reports, migration guide and two source export archives.\n\n**Files changed:** all canonical JSON files; all JSON schemas; manifest; ID mapping; reports and migration documentation.\n\n**Validation:** {validation['validation_status']}; source inventories and referential constraints checked.\n''','CHANGELOG.md')
textout('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Shared Taxa — Release history</title><style>body{font:16px/1.5 system-ui,sans-serif;background:#101827;color:#e6edf5;max-width:850px;margin:3rem auto;padding:1rem}details{border:1px solid #35435c;border-radius:12px;padding:16px;background:#182338}summary{cursor:pointer;font-weight:700}code{color:#9dcaff}</style><h1>Shared Taxa — Release history</h1><details open><summary>v1.0 — October 15, 2026</summary><ul><li>Integrated Tree of Life Explorer v1.7 and Deep Time Atlas v1.6 scientific source snapshots.</li><li>Canonical taxonomic ID crosswalks and provenance-backed classifications.</li><li>Preserved source intervals, taxon examples, diversity estimates and embedded illustrations.</li><li>Validation, reconciliation reports and compatibility documentation.</li></ul><p>Scientific ambiguities remain disclosed in <code>RECONCILIATION.md</code>.</p></details></html>''','CHANGELOG.html')

samples=age_comparisons[:8]; geos=geodiff[:8]
textout('# Scientific reconciliation and unresolved ambiguities\n\n'+
 f'**Matched taxon source profiles:** {len(matching)} (matching by exact scientific names plus two explicit domain and two curated synonym resolutions).\n\n'+
 f'**Additional Deep Time concepts:** {len(new_from_deep)}; no unsupported cladogram parent edges invented.\n\n'+
 f'**Rank disagreements:** {stats["rank_disagreements"]}. **Approximate source age differences:** {len(age_comparisons)}. **Chronological boundary differences:** {len(geodiff)}. **Source ambiguity notes:** {len(issue_notes)}.\n\n'+
 '## Identity policy\n\nShared names do not always imply an identical taxonomic rank, circumscription or classification. The Bacteria and Archaea domain concepts are matched to the Tree of Life domain records rather than similarly named kingdom records. Kingdom records remain available as distinct *classification concepts* to avoid self-parenting cycles. Cyanobacteria ↔ Cyanobacteriota and Angiosperms ↔ Angiospermae are explicit curated aliases, not fuzzy substring matches.\n\n'+
 '## Sample lineage age disagreements (Ma)\n\n'+ '\n'.join(f'- `{x["taxon_id"]}`: Tree origin {x["tree_origin_ma"]}; Deep first-range boundary {x["deep_time_first_ma"]}. Not equivalent evidence types.' for x in samples)+'\n\n'+
 '## Sample geologic boundary differences (Ma)\n\n'+ '\n'.join(f'- {x["interval_name"]}: '+ '; '.join(f'{v["source_export"]} {v["old_ma"]}–{v["young_ma"]}' for v in x['source_bounds']) for x in geos)+'\n\n'+
 '## Outstanding issues\n\n- Deep Time cladogram strings are not an edge-resolved taxonomy; unmatched groups remain unplaced rather than forcing a Tree parent.\n- Tree of Life historic kingdom headings include non-monophyletic groupings; retain alternative classifications and provenance.\n- First occurrence, lineage origin, crown group and stem divergence are not interchangeable. Canonical calibrated dates remain null.\n- Counts from disparate catalogs, categories and geographic scopes cannot be added as if they were one census.\n- Deep Time geologic association links are curated source associations, not independently reviewed fossil finds; 8,916 UI-derived matches are strictly separate.\n- Source reference URLs do not substantiate every entry; URL verification and scientific fact-checking remain outstanding.\n- Deep Time embedded images are illustrative AI paleoart; Tree Wikipedia and Commons links remain unchecked.\n\nAll recorded differences and source metadata are in `RECONCILIATION_REPORT.json`. Original files are available verbatim in `source_exports/`.\n','RECONCILIATION.md')
textout('''# Compatibility and widget migration guide\n\n## Version matrix\n\n| Consumer | Compatible source input | Shared Taxa target | Status |\n|---|---|---|---|\n| Tree of Life Explorer v1.7 | embedded Tree JSON/JS | Shared Taxa schema 1.0 | Data crosswalk available; widget not migrated |\n| Deep Time Atlas v1.6 | embedded Deep Time JS | Shared Taxa schema 1.0 | Data crosswalk available; widget not migrated |\n| Future Atlas / quiz widgets | schema 1.0 JSON | Shared Taxa v1.0 | Integration contract ready |\n\n## Safe migration sequence\n\n1. Keep original widget source and embedded scientific records intact.\n2. Include Shared Taxa JSON as a separate versioned dataset and load `manifest.json`.\n3. Lookup original widget IDs in `ID_MAPPING.json`, keyed by both `source_export` and `source_id`.\n4. For Tree widgets, use `parent_id` for the exported educational tree, but provide a classification selector for alternate rank conventions and disputed relationships.\n5. For Deep Time, use geologic interval IDs and `geologic_taxon_links.json`; **never** use age-filter matches as a validated scientific relationship.\n6. Preserve old page and card display text until UI audits confirm consistency.\n7. Present source age interpretations and disagreements instead of selecting undocumented dates.\n8. Use local verified images only with credit and illustration warnings; check live image URLs and licensing separately.\n9. Run regression testing (same navigation, same lineage cards, same counts, source images), then switch source in a separate widget release.\n10. Roll back by restoring original widget build; never let a dataset revision silently change a widget version.\n\n## API contract\n\nEach JSON file has `schema_version: "1.0"` and a top-level array of named records. Canonical taxon IDs have `stx:taxon:` namespace. `ID_MAPPING.json` supports taxon and geologic interval lookup. Optional attributes may remain `null`. Consumers must not assume all taxa have parent IDs, calibrated first-appearance dates, exact global abundance estimates, static public image URLs or taxon-specific bibliography.\n\n## Change management\n\nA new minor release should carry the prior ID mapping forward and be fully additive where practical. Breaking schema/reparenting changes need an explicit major version and migration checklist. Retain immutable prior archives for rollback.\n''','MIGRATION_GUIDE.md')

# Keep the release's source-reconstruction script for future replays and audits.
(OUT/'tools').mkdir(parents=True,exist_ok=True)
shutil.copy2(BASE/'build_shared_taxa_v1.py',OUT/'tools'/'build_shared_taxa_v1.py')
# package manifest with integrity checksums for every file but manifest itself (self hash recursion).
manifest={'dataset':'Shared Taxa','dataset_version':VERSION,'release_date':FDATE,'schema_version':SCHEMA_V,
 'release_status':'published_with_documented_scientific_ambiguities' if validation['validation_status'].startswith('PASS') else 'NOT_VALIDATED',
 'source_exports':[
 {'name':'Tree of Life Explorer','version':'1.7','archive':'source_archives/'+TREE_Z.name,'sha256':digest(TREE_Z.read_bytes()),'taxon_source_records':len(ttax),'export_date':FDATE},
 {'name':'Deep Time Atlas','version':'1.6','data_snapshot_version':'1.5','archive':'source_archives/'+DEEP_Z.name,'sha256':digest(DEEP_Z.read_bytes()),'taxon_source_records':len(dtaxa),'geologic_source_intervals':len(dint),'export_date':FDATE}],
 'counts':stats,'compatibility':{'Tree of Life Explorer':'1.7 source records indexed, migration not performed','Deep Time Atlas':'1.6 source records indexed, migration not performed',
 'schema_version':SCHEMA_V,'future_widgets':'canonical JSON 1.0 consumers'},
 'release_history':[{'version':VERSION,'date':FDATE,'expand_by_default':True,'changes':['Initial conservative taxon ID reconciliation','Geologic interval and provenance merges','Full original source snapshots retained','Machine schema and cross-file integrity validation']}],
 'validation_status':validation['validation_status'],'validation_report':'VALIDATION_REPORT.json','schema_standard':'https://json-schema.org/draft/2020-12/schema',
 'checksum_algorithm':'sha256','checksum_note':'manifest.json intentionally not self-hashed to avoid recursive checksum; all other files included.',
 'files_changed':['taxonomy.json','taxon_details.json','taxon_history.json','diversity.json','organisms.json','geologic_time.json','rank_guides.json','sources.json','images_manifest.json','geologic_taxon_links.json','additional_science.json','ID_MAPPING.json','RECONCILIATION_REPORT.json','VALIDATION_REPORT.json','manifest.json','schemas/*','README.md','CHANGELOG.md','CHANGELOG.html','RECONCILIATION.md','MIGRATION_GUIDE.md'],
 'files':[]}
for p in sorted(OUT.rglob('*')):
 if p.is_file() and p != OUT/'manifest.json':
  manifest['files'].append({'path':p.relative_to(OUT).as_posix(),'size_bytes':p.stat().st_size,'sha256':digest(p.read_bytes())})
dump(manifest,'manifest.json')
assert not list(Draft202012Validator(schemas['manifest.json']).iter_errors(manifest))

# final manifest and archive verification
assert all(digest((OUT/x['path']).read_bytes())==x['sha256'] for x in manifest['files'])
assert len(set(x['path'] for x in manifest['files']))==len(manifest['files'])
archive_path=BASE/'Shared_Taxa_v1.0_2026-10-15.zip'
with zipfile.ZipFile(archive_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as archive:
 for f in sorted(OUT.rglob('*')):
  if f.is_file():archive.write(f,arcname='Shared_Taxa_v1.0/'+f.relative_to(OUT).as_posix())
with zipfile.ZipFile(archive_path) as archive:
 bad=archive.testzip();assert bad is None,bad
 assert len(archive.namelist())==len(manifest['files'])+1
print('RESULT',json.dumps({'zip':str(archive_path),'bytes':archive_path.stat().st_size,'records':stats,'schema_count':schema_count,
 'validation':validation['validation_status'],'failing_checks':[x for x in checks if x['status']=='FAIL'],
 'warning_checks':[x for x in checks if x['status']=='WARNING'],'archive_files':len(manifest['files'])+1},indent=2))
