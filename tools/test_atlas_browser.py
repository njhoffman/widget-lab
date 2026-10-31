#!/usr/bin/env python3
"""Exercise actual Atlas controls and save versioned browser regression evidence."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import sys
import tempfile

from capture_atlas_comparisons import Browser, digest
from check_project import ROOT


VISIBLE_DIALOGS = """[...document.querySelectorAll('[role=dialog],dialog')].filter(n=>n.getBoundingClientRect().width>0 && getComputedStyle(n).visibility!=='hidden')"""


class Suite:
    def __init__(self, browser, output):
        self.browser, self.output = browser, output
        self.results = []
        self.context = {}
        self.assertions = []

    def evaluate(self, expression):
        return self.browser.evaluate(expression)

    def wait(self):
        self.evaluate('new Promise(resolve=>setTimeout(resolve,150))')

    def click(self, selector):
        position = self.evaluate(f"""(()=>{{const n=document.querySelector({json.dumps(selector)});if(!n)throw Error('Missing control: '+{json.dumps(selector)});n.scrollIntoView({{block:'center',behavior:'instant'}});const r=n.getBoundingClientRect();if(!r.width||!r.height)throw Error('Invisible control');return {{x:r.x+r.width/2,y:r.y+r.height/2}}}})()""")
        self.browser.call('Input.dispatchMouseEvent', {'type': 'mousePressed', 'button': 'left', 'clickCount': 1, **position})
        self.browser.call('Input.dispatchMouseEvent', {'type': 'mouseReleased', 'button': 'left', 'clickCount': 1, **position})
        self.wait()

    def key(self, key, code):
        for action in ('keyDown', 'keyUp'):
            event = {'type': action, 'key': key, 'code': key, 'windowsVirtualKeyCode': code}
            if key == 'Enter' and action == 'keyDown':
                event.update(text='\r', unmodifiedText='\r')
            self.browser.call('Input.dispatchKeyEvent', event)
        self.wait()

    def text(self, selector, value):
        self.click(selector)
        # Browser editing commands keep input events identical to real typing.
        self.browser.call('Input.dispatchKeyEvent', {'type': 'keyDown', 'key': 'a', 'code': 'KeyA', 'windowsVirtualKeyCode': 65, 'modifiers': 2})
        self.browser.call('Input.dispatchKeyEvent', {'type': 'keyUp', 'key': 'a', 'code': 'KeyA', 'windowsVirtualKeyCode': 65, 'modifiers': 2})
        self.browser.call('Input.insertText', {'text': value})
        self.wait()

    def require(self, expression, message):
        passed = bool(self.evaluate(expression))
        self.assertions.append({'expectation': message, 'status': 'pass' if passed else 'fail'})
        if not passed:
            raise AssertionError(message)

    def check(self, name, operation):
        self.assertions = []
        try:
            operation()
            result = {'name': name, 'status': 'pass', **self.context}
        except Exception as error:
            result = {'name': name, 'status': 'fail', 'detail': str(error), **self.context}
            image = self.output / f'{self.context["widget"]}-{self.context["width"]}-{name}-failure.png'
            self.browser.screenshot(image)
            result['screenshot'] = image.name
        result['assertions'] = self.assertions
        self.results.append(result)
        print(f'{result["status"]}: {self.context["widget"]} {self.context["width"]} {name}', flush=True)

    def layout(self):
        dimensions = self.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})')
        if dimensions['scroll'] > dimensions['width'] + 2:
            raise AssertionError(f'Horizontal document overflow: {dimensions}')
        self.require("[...document.querySelectorAll('h1,.atlas-family-version')].filter(n=>n.getBoundingClientRect().width).every(n=>{const r=n.getBoundingClientRect();return r.left>=-1&&r.right<=innerWidth+1})", 'Title/version control clips outside viewport')
        if self.context['widget'] == 'brain' and self.context['version'] == '1.22.0':
            self.require("(()=>{const r=document.querySelector('.workspace>.left').getBoundingClientRect();return r.width>=180&&r.left>=0&&r.right<=innerWidth+1})()", 'Brain hierarchy panel collapsed or clipped outside the viewport')

    def keyboard_history(self):
        self.evaluate("document.querySelector('.atlas-family-version').focus()")
        self.key('Enter', 13)
        self.require(f'{VISIBLE_DIALOGS}.length>0', 'Enter did not open version history')
        self.require(f'{VISIBLE_DIALOGS}.some(n=>n.innerText.includes("{self.context["version"]}"))', 'Current version absent from visible history')
        self.key('Escape', 27)
        self.require(f'{VISIBLE_DIALOGS}.length===0', 'Escape did not dismiss version history')
        self.require("document.activeElement.matches('.atlas-family-version')", 'Dismissed history did not restore trigger focus')
        self.key('Tab', 9)
        self.require("document.activeElement.matches('button,input,select,a[href],[tabindex]')", 'Tab did not move to a focusable control')
        self.require("(()=>{const s=getComputedStyle(document.activeElement);return (s.outlineStyle!=='none'&&parseFloat(s.outlineWidth)>0)||s.boxShadow!=='none'})()", 'Keyboard focus lacks an outline or shadow')

    def deep(self):
        self.text('#search', 'Triassic')
        self.click('#searchHits [data-hit="0"]')
        self.require("document.getElementById('mainTitle').innerText.includes('Triassic')", 'Search failed to select Triassic')
        panes = []
        for tab in ('Overview', 'Climate', 'Continents', 'Geology', 'Life'):
            self.click(f'#tabs [data-tab="{tab}"]')
            self.require(f'document.querySelector("#tabs .on").dataset.tab==={json.dumps(tab)}', f'{tab} active state absent')
            panes.append(self.evaluate("document.getElementById('tabContent').innerText"))
        if len(set(panes)) != 5 or min(map(len, panes)) < 30:
            raise AssertionError('Five topics do not show distinct substantive content')
        original_art = self.evaluate("document.querySelector('main.panel.center').style.getPropertyValue('--aw-scene')")
        self.click('[data-timeline="jurassic"]')
        self.require("document.getElementById('mainTitle').innerText.includes('Jurassic') && document.querySelector('#path button:last-child').dataset.node==='jurassic'", 'Neighbor did not update selected title and breadcrumb to Jurassic')
        self.require(f"document.querySelector('main.panel.center').style.getPropertyValue('--aw-scene')!=={json.dumps(original_art)}", 'Neighbor did not update interval artwork')
        self.click('[data-timeline="triassic"]')
        self.require("document.getElementById('mainTitle').innerText.includes('Triassic') && document.querySelector('#path button:last-child').dataset.node==='triassic'", 'Return neighbor did not restore Triassic title and breadcrumb')
        self.click('#taxList [data-taxon]')
        self.require("document.getElementById('modalBack').classList.contains('show') && document.getElementById('modalContents').innerText.length>100", 'Representative-life card did not open a substantive taxon profile')
        self.click('#closeModal')
        self.require("!document.getElementById('modalBack').classList.contains('show')", 'Taxon profile failed to close')
        if self.context['version'] == '1.19.0':
            self.require("document.getElementById('aw-header-family').contains(document.getElementById('tabs')) && document.getElementById('aw-header-family').contains(document.getElementById('search'))", 'Topics/search were not retained in the compact header')
            if self.context['width'] >= 1200:
                self.require("document.getElementById('aw-header-family').getBoundingClientRect().height<=100", 'Desktop header is no longer compact')
            self.require("(()=>{const entries=JSON.parse(document.getElementById('atlas-art-manifest').textContent).entries;return [...document.querySelectorAll('.aw-v19-scene-filmstrip button')].every(b=>{const e=entries.find(e=>e.id===b.dataset.interval);const n=b.querySelector('.wl-interval-age')?.innerText.replaceAll(',','').match(/\\d+(?:\\.\\d+)?/g)?.map(Number);return e&&n&&n[0]===e.start_mya&&n[1]===e.end_mya})})()", 'Preview ages do not match the actual interval manifest')
            self.click('.aw-v19-scene-filmstrip [data-interval="jurassic"]')
            self.require("document.getElementById('mainTitle').innerText.includes('Jurassic') && document.querySelector('.aw-v19-scene-filmstrip [data-interval=jurassic]').getAttribute('aria-current')==='true'", 'Artwork preview did not select Jurassic and expose current state')
            self.click('.aw-v19-scene-filmstrip [data-interval="triassic"]')
            self.browser.call('Emulation.setEmulatedMedia', {'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]})
            self.require("getComputedStyle(document.querySelector('.aw-v19-interval-banner'),'::before').transitionDuration==='0s'", 'Reduced-motion preference did not suppress scene transition')
            self.browser.call('Emulation.setEmulatedMedia', {'features': []})
            self.text('#search', 'Holocene')
            self.click('#searchHits [data-hit="0"]')
            self.require("document.querySelector('.aw-v19-scene-filmstrip [data-interval=holocene] .wl-interval-age').innerText.includes('0.0117')", 'Recent interval preview rounded away the source boundary precision')
            self.text('#search', 'Triassic')
            self.click('#searchHits [data-hit="0"]')

    def brain(self):
        self.click('#brain circle:has(title)')
        self.require("document.getElementById('details').innerText.includes('EXPLORE SELECTED STRUCTURE')", 'Brain marker did not open structure details')
        for selector in ('#medialButton', '#axialButton', '#lateralButton'):
            self.click(selector)
            self.require(f'document.querySelector({json.dumps(selector)}).classList.contains("on")', f'{selector} did not become active')
        self.click('#depthButton')
        self.require("document.getElementById('depthButton').classList.contains('on')", 'Depth control did not become active')
        self.require("document.querySelector('.brain-stage').innerText.toLowerCase().includes('schematic')", 'Depth view lost its schematic disclosure')
        self.click('#timelineOpen')
        self.require("document.getElementById('timelineDialog').open", 'Time filter dialog did not open')
        # Overlapping range tracks expose draggable thumbs; focus the input for a
        # keyboard test instead of clicking the shared track's midpoint.
        self.evaluate("document.getElementById('oldSlider').focus()")
        before = self.evaluate("Number(document.getElementById('oldSlider').value)")
        self.key('ArrowRight', 39)
        self.require(f"Number(document.getElementById('oldSlider').value)>{before}", 'Time slider did not change by keyboard')
        self.click('#timelineDone')
        self.click('#timelineReset')
        self.require("document.getElementById('timelineOpen').innerText.includes('550')", 'Time reset did not restore original window')
        if self.context['version'] == '1.22.0':
            self.require("document.getElementById('aw-header-family').contains(document.getElementById('lateralButton')) && document.getElementById('aw-header-family').contains(document.getElementById('awDepthStrength'))", 'Projection/depth controls are missing from the header')
            if self.context['width'] >= 1200:
                self.require("document.getElementById('aw-header-family').getBoundingClientRect().height<=100", 'Brain desktop header is not compact')
            self.require("!document.querySelector('.brain-stage').contains(document.querySelector('.aw-brain-view-card')) && !document.querySelector('.brain-stage').contains(document.getElementById('awDepthLegend'))", 'Reference/depth context still covers interactive markers')
            if self.evaluate("document.getElementById('depthButton').getAttribute('aria-pressed')==='true'"):
                self.click('#depthButton')
            self.require("document.getElementById('awDepthStrength').disabled", 'Depth strength should be inactive while depth is off')
            self.evaluate("document.querySelector('#brainHits [aria-label=\"Select Orbitofrontal cortex (OFC)\"]').focus()")
            self.key('Enter', 13)
            self.require("document.getElementById('focusLabel').innerText.includes('Orbitofrontal') && document.querySelector('#details h2').innerText.includes('Orbitofrontal')", 'Keyboard marker selection lost the region/detail identity')
            references = set()
            for selector in ('#lateralButton', '#medialButton', '#axialButton'):
                self.click(selector)
                self.require("document.getElementById('focusLabel').innerText.includes('Orbitofrontal') && document.querySelector('#tree .region.sel').innerText.includes('Orbitofrontal')", 'Projection change lost selected region or hierarchy state')
                self.require("(()=>{const c=document.querySelector('#brainSelected circle');const v=document.getElementById('brain').viewBox.baseVal;const x=Number(c?.getAttribute('cx')),y=Number(c?.getAttribute('cy'));return c&&x>=v.x&&x<=v.x+v.width&&y>=v.y&&y<=v.y+v.height})()", 'Selected marker lies outside the authored projection bounds')
                references.add(self.evaluate("document.querySelector('.aw-brain-view-card img').getAttribute('src')"))
                before = self.evaluate("Number(document.querySelector('#brainHits [aria-label=\"Select Thalamus\"]').getAttribute('fill-opacity'))")
                self.click('#depthButton')
                self.require(f"Number(document.querySelector('#brainHits [aria-label=\"Select Thalamus\"]').getAttribute('fill-opacity'))<{before} && document.getElementById('focusLabel').innerText.includes('Orbitofrontal')", 'Projection-specific depth toggle did not change cues while retaining selection')
                self.click('#depthButton')
                self.require(f"Number(document.querySelector('#brainHits [aria-label=\"Select Thalamus\"]').getAttribute('fill-opacity'))==={before}", 'Projection-specific depth off did not restore native opacity')
            if len(references) != 3:
                raise AssertionError('Projection reference did not update for all three views')
            self.click('#lateralButton')
            marker = "document.querySelector('#brainHits [aria-label=\"Select Thalamus\"]')"
            baseline = self.evaluate(f"[Number({marker}.getAttribute('fill-opacity')),Number({marker}.getAttribute('r'))]")
            self.click('#depthButton')
            self.require("!document.getElementById('awDepthStrength').disabled && !document.getElementById('awDepthLegend').hidden", 'Enabled depth lost its native strength/legend controls')
            cues = []
            self.evaluate("document.getElementById('awDepthStrength').focus()")
            self.key('Home', 36)
            for index in range(3):
                if index:
                    self.key('ArrowDown', 40)
                cues.append(self.evaluate(f"[Number({marker}.getAttribute('fill-opacity')),Number({marker}.getAttribute('r'))]"))
                self.require("document.querySelector('#brainSelected circle').getAttribute('r')==='5' && document.querySelector('#brainSelected circle').getAttribute('fill')==='#f8ffff' && document.getElementById('focusLabel').innerText.includes('Orbitofrontal')", 'Depth strength altered selected marker clarity or identity')
            if not all(cues[0][i] > cues[1][i] > cues[2][i] for i in (0, 1)):
                raise AssertionError(f'Low/medium/high depth did not change opacity and radius monotonically: {cues}')
            self.click('#depthButton')
            restored = self.evaluate(f"[Number({marker}.getAttribute('fill-opacity')),Number({marker}.getAttribute('r'))]")
            if restored != baseline:
                raise AssertionError('Turning depth off did not restore native cue attributes')
            self.require("document.querySelector('.brain-stage').innerText.includes('not volumetric') && document.querySelector('.aw-brain-view-card').innerText.includes('not 3D')", 'Schematic/orientation limitations are not visible')
            total = self.evaluate("Number(document.getElementById('visibleCount').innerText)")
            self.click('#timelineOpen')
            self.click('#presets [data-old="70"][data-young="0"]')
            self.require(f"Number(document.getElementById('visibleCount').innerText)<{total} && document.getElementById('focusLabel').innerText.includes('Orbitofrontal')", 'Evolutionary preset failed to filter counts while retaining the eligible selected region')
            self.click('#timelineDone')
            self.click('#timelineReset')
            self.require(f"Number(document.getElementById('visibleCount').innerText)==={total}", 'Reset did not restore the original visible region count')
            self.require("document.querySelector('#tree .region.sel').getBoundingClientRect().width>=150", 'Selected hierarchy control is too narrow to remain usable')
            self.click('#tree .region.sel')
            self.require("document.getElementById('focusLabel').innerText.includes('Orbitofrontal')", 'Native hierarchy control failed to retain its selected region')

    def myth(self):
        self.text('#search', 'Zeus')
        self.click('#results [data-entry="zeus"]')
        self.require("document.getElementById('profileHead').innerText.includes('Zeus')", 'Figure search did not select Zeus')
        self.click('#clearFilters')
        self.click('[data-trad="norse"]')
        self.require("document.querySelector('[data-trad=norse]').getAttribute('aria-selected')==='true' && document.getElementById('indexedLeft').innerText.includes('Norse')", 'Tradition filter did not switch to Norse')
        self.click('[data-trad="greek"]')
        self.text('#search', 'no-such-figure-12345')
        self.require("document.getElementById('matchCount').innerText.startsWith('0')", 'Empty search did not produce zero matches')
        self.click('#clearFilters')
        self.require("!document.getElementById('matchCount').innerText.startsWith('0')", 'Reset did not restore figure index')
        if self.context['version'] == '1.14.0':
            self.require("document.getElementById('aw-header-family').contains(document.getElementById('search'))", 'Figure search is absent from the compact header')
            self.require("document.getElementById('wl-myth-art').getAttribute('aria-pressed')==='true' && !document.getElementById('awMythArtworkStage').hidden", 'Artwork is not the initial view')
            self.require("document.getElementById('awMythArtworkStage').dataset.artworkKey==='greek:zeus' && document.getElementById('awArtCredit').innerText.includes('AI concept')", 'Featured Zeus source key/disclosure is missing')
            self.require("getComputedStyle(document.querySelector('.maplegend')).display==='none'", 'Tree legend leaks into artwork view')
            self.click('#wl-myth-tree')
            self.require("selected==='zeus' && !document.getElementById('stage').hidden && document.getElementById('awMythArtworkStage').hidden", 'Switching to family tree lost selected figure or view state')
            parent = self.evaluate('byId.get(selected).parents[0]')
            self.click('#goParent')
            self.require(f'selected==={json.dumps(parent)}', 'Parent navigation changed the wrong figure')
            self.require("document.getElementById('profile').scrollTop===0", 'Changed figure retained the previous profile scroll position')
            self.click('#profileContent button[data-rel="zeus"]')
            self.require("selected==='zeus' && tradition==='greek'", 'Child relationship navigation lost figure/tradition')
            self.require("document.getElementById('profile').scrollTop===0", 'Child profile did not start at its figure heading')
            self.evaluate("document.getElementById('wl-myth-art').focus()")
            self.key('Enter', 13)
            self.require("selected==='zeus' && !document.getElementById('awMythArtworkStage').hidden", 'Keyboard artwork activation lost selection')
            self.click('[data-names="both"]')
            self.require("tradition==='greek' && selected==='zeus' && document.getElementById('profileHead').innerText.includes('Jupiter')", 'Complementary Roman name control changed figure identity or lost its counterpart')
            self.click('[data-names="primary"]')
            for selector, property_name in (('#groupFilter', 'group'), ('#storyFilter', 'stories'), ('#motifFilter', 'tags')):
                self.evaluate(f'document.querySelector({json.dumps(selector)}).focus()')
                self.key('Home', 36)
                self.key('ArrowDown', 40)
                self.require(f"(()=>{{const value=document.querySelector({json.dumps(selector)}).value;const rows=[...document.querySelectorAll('#results [data-entry]')];return value&&rows.length>0&&rows.every(r=>{{const field=byId.get(r.dataset.entry)[{json.dumps(property_name)}];return Array.isArray(field)?field.includes(value):field===value}})}})()", 'Native group/story/symbol filter did not constrain the original figure index')
                self.click('#clearFilters')
            for tradition in ('greek', 'roman', 'norse', 'mesopotamian', 'hindu'):
                self.click(f'[data-trad="{tradition}"]')
                self.require(f'tradition==={json.dumps(tradition)} && document.getElementById("awMythArtworkStage").dataset.artworkKey===tradition+":"+selected', 'Tradition switch retained a stale artwork key')
                self.require("(()=>{const b=[...document.querySelectorAll('#awMythRelated .aw-related-figure')];return b.length>0&&b.every(b=>b.dataset.artworkKey===tradition+':'+b.dataset.figureId&&b.querySelector('img')?.getAttribute('src')===window.AtlasMythologyArtwork.thumbFor(b.dataset.artworkKey))})()", 'Related thumbnails do not use current-tradition image keys')
                self.require("(()=>{const r=document.querySelector('#results .result[aria-selected=true]');return r&&r.dataset.entry===selected&&r.querySelector('img')?.getAttribute('src')===window.AtlasMythologyArtwork.thumbFor(tradition+':'+selected)&&getComputedStyle(r).boxShadow!=='none'})()", 'Selected result thumbnail/treatment does not follow the active tradition')
            self.click('[data-trad="greek"]')
            self.text('#search', 'Zeus')
            self.click('#results [data-entry="zeus"]')
            self.browser.call('Emulation.setEmulatedMedia', {'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]})
            self.require("getComputedStyle(document.querySelector('#awMythArtworkStage'),'::before').transitionDuration==='0s'", 'Artwork transition ignores reduced motion')
            self.browser.call('Emulation.setEmulatedMedia', {'features': []})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/browser-tests' / (ROOT / 'VERSION').read_text().strip())
    parser.add_argument('--widths', nargs='+', type=int, default=[390, 768, 1440])
    args = parser.parse_args()
    executable = shutil.which('google-chrome') or shutil.which('chromium')
    if not executable:
        parser.error('Chrome/Chromium is required')
    args.output.mkdir(parents=True, exist_ok=True)
    registry = json.loads((ROOT / 'project_manifest.json').read_text())
    sources = {}
    with tempfile.TemporaryDirectory(prefix='widget-lab-regression-') as profile:
        browser = Browser(executable, profile)
        suite = Suite(browser, args.output)
        try:
            for slug in ('deep-time', 'brain', 'mythology'):
                component = next(c for c in registry['atlas'] if c['slug'] == slug)
                source = ROOT / component['authoritative_source']
                sources[slug] = {'path': component['authoritative_source'], 'sha256': digest(source)}
                for width in args.widths:
                    browser.events.clear()
                    suite.context = {'widget': slug, 'width': width, 'version': component['release_version']}
                    browser.navigate(source, width, 1000)
                    suite.check('layout-initial', suite.layout)
                    suite.check('keyboard-history', suite.keyboard_history)
                    # Isolate application flow from an independently failed dialog check.
                    browser.navigate(source, width, 1000)
                    suite.check('navigation-filters-panels', getattr(suite, {'deep-time': 'deep', 'brain': 'brain', 'mythology': 'myth'}[slug]))
                    suite.check('layout-selected', suite.layout)
                    suite.evaluate("window.scrollTo({top:0,left:0,behavior:'instant'}); true")
                    suite.wait()
                    image = args.output / f'{slug}-{width}-selected.png'
                    browser.screenshot(image)
                    exceptions = [e['params']['exceptionDetails'] for e in browser.events if e.get('method') == 'Runtime.exceptionThrown']
                    suite.check('runtime-errors', lambda: suite.require('true' if not exceptions else 'false', str(exceptions)))
            report = {'repository_version': (ROOT / 'VERSION').read_text().strip(), 'captured_at': datetime.now(timezone.utc).isoformat(),
                      'browser': browser.version, 'sources': sources, 'results': suite.results,
                      'task_coverage': {'WL-005': 'All cases at 390/768/1440; incomplete if a width is omitted.',
                                        'T018': 'Deep Time navigation-filters-panels: click Jurassic then Triassic adjacent intervals.',
                                        'T021': 'Deep Time navigation-filters-panels: click representative life and inspect/close taxon profile.',
                                        'T022': 'Deep Time navigation-filters-panels: five topic controls, active state and distinct nonempty content.'},
                      'status': 'fail' if any(r['status'] == 'fail' for r in suite.results) else 'pass',
                      'limits': ['Chrome on Linux only; no Windows/IndexedDB/folder-picker, screen reader, contrast audit, or scientific verification.']}
            (args.output / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
            print(json.dumps({'status': report['status'], 'passed': sum(r['status']=='pass' for r in suite.results), 'total': len(suite.results)}), flush=True)
        finally:
            browser.close()
    return report['status'] != 'pass'


if __name__ == '__main__':
    sys.exit(main())
