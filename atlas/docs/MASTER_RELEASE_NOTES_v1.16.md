# Atlas Widgets — Master Development v1.16

**Release:** 2026-10-17. **Functional/style iteration (no new artwork generated).**

## Source baselines
- Deep Time v1.17 → **v1.18**
- Brain v1.20 → **v1.21**
- Mythology v1.12 → **v1.13**
- Unchanged: Tree of Life v1.14, Muscle v1.8, Emergence v1.10, Widget Launcher v1.12, Shared Taxa v1.0, Artwork Studio v1.9.

## Implemented
1. Deep Time's five fully active topic tabs — Overview, Climate, Continents, Geology, Life — populated from the existing geologic records. Representative indexed taxa display a clickable image-card strip beside the original taxa list. Clicking opens the existing taxon detail dialog. No geologic facts or taxon links invented.
2. Brain selected-region detail navigation is generated from the actual available profile sections. Evolution, Function & circuits, Neurotransmitters and Clinical shortcuts are shown only when corresponding content exists. Clicking scrolls to and highlights the correct scientific section. The complete original content remains accessible.
3. Mythology now surfaces up to 12 actually recorded related figures with locally available icon illustrations and one-click navigation to their normal genealogy profiles, plus a shortcut to the current figure's Artwork view. This is **related-figure navigation**, not a licensed historical-artwork gallery.
4. Shared header and detail-control polish follows the existing navy/cyan/green style, with restrained subject-aware lighting and accessible hover/focus states. Existing borderless responsive header preferences are respected.
5. Version-history entries appended without deleting any older entries. Screenshots of the actual HTML are paired with the newest approved goal concept crops; concept counts/visuals are *not* treated as verified real data.

## Important scientific/product distinctions
- Schematic Brain projections remain schematic, with existing anatomy-aware approximate depth mode.
- Deep Time artwork and taxon images remain modern illustrative assets, and field text inherits from existing records when finer intervals have no dedicated notes.
- Mythology's new related cards use indexed figure identity and actual relationship buttons; historical cultural artwork and license review remain future work.
- No source atlas scientific/genealogy data records, Shared Taxa manifest, or prior artwork binaries were changed in this release.

## QA
Standalone HTML browser tests: Deep Time five topic tabs, interval change and taxon modal; Brain OFC profile plus detail shortcuts; Mythology related figure navigation and Artwork view switch. Three responsive widths (390, 768, 1440px) for each widget showed no horizontal overflow; no reported JavaScript errors. External URLs, licensed artwork accuracy, local folder permissions and cross-session launcher synchronization were not tested.

## Goal checklist delta
- **T021** Representative life: planned → implemented (cards tied to indexed taxon profiles).
- **T022** Deep Time tabs: partial → implemented (all five backed by records).
- **T035** Brain profile navigation: remains partial; shortcuts work, but richer integrated cards from the goal reference remain.
- **T047** Mythology related artwork: planned → partial; related figures and modern illustrative previews now navigate, but source-specific historic-artwork carousel with citations/licensing remains.
- **T008/T009** Shared controls/panel polish: partial, not fully complete across all seven widgets.

**Next suggested release focus:** Tree of Life / Muscle / Emergence presentation styling, true sourced brain renders, Deep Time paleomaps, and properly attributed Mythology historical-artwork carousel.
