# Image2 Interface Moodboard Prompt

Use this module when the user asks to see the future design of an HTML presentation, PDF slidument, interactive catalogue, client cabinet or another multi-screen client material before production.

## Hard distinction

An interface moodboard shows how the artifact works and reads. It must contain representative screens, information hierarchy, navigation, charts, forms, editable fields, image roles and design tokens.

The following outputs fail this task:

- a collage of photographs, textures and colour swatches;
- one hero image with empty headline space;
- a generic dashboard unrelated to the planned material;
- eight cosmetic variants of the same card layout;
- invented brand-critical text, logos, numbers or medical results;
- device mockups that hide the actual screen hierarchy.

## Admission fields

Complete before calling Image2:

- client and material family;
- primary surface and aspect ratio;
- 6–8 real screen types from the approved meaning plan;
- main information object on every screen;
- required editable fields and controls;
- approved brand codes and client assets;
- 3–5 best-in-class references and the exact mechanics transferred;
- territory name and proposition;
- deliberate visual exclusions;
- Human Gate question.

## Reusable prompt template

```text
Design a high-fidelity UI moodboard for a future self-contained [HTML presentation / PDF slidument / interactive catalogue / client cabinet] for [CLIENT AND OFFERING].

This is NOT a photography or atmosphere moodboard. Show one coherent presentation interface system as a 16:9 Figma-style art-direction board containing 8 miniature 16:9 screen designs at readable scale plus a compact design-token and component strip.

Territory: [TERRITORY NAME].
Creative proposition: [WHAT THIS TERRITORY MAKES THE READER BELIEVE AND HOW].

Required screen types:
1. [cover job and primary object];
2. [programme / route / product overview and primary object];
3. [assessment / evidence screen and primary chart or annotated image];
4. [expert / team / RTB screen and proof object];
5. [process / responsibility / comparison screen];
6. [progress / economics / result screen and chart];
7. [case / timeline / scenario screen];
8. [editable next-step / form / X-Y-Z fields / CTA screen].

Interface requirements:
- [grid and composition grammar];
- [display and body typography roles];
- [palette and surface modes];
- [navigation rail, folio, progress or section controls];
- [chart, diagram and evidence treatment];
- [form fields, selectors, editable placeholders and states];
- [photo role and crop logic];
- every chart visibly fits with generous margins;
- screens differ by information object while remaining one design family;
- show responsive HTML component logic rather than a static poster collage.

Transfer these best-in-class mechanics:
- [REFERENCE 1]: [exact transferable mechanism];
- [REFERENCE 2]: [exact transferable mechanism];
- [REFERENCE 3]: [exact transferable mechanism].

Use short plausible Cyrillic-style headings or clean neutral placeholders. Do not rely on generated lettering for brand-critical meaning. Exact Russian copy, logo, numbers and legal text will be added later as HTML/vector layers.

Avoid:
- old PowerPoint or brochure aesthetics;
- generic walls of rounded cards;
- decorative SaaS dashboards;
- charts squeezed into small cards;
- glossy 3D, gradients and device mockups;
- fake statistics, diagnoses, results or credentials;
- atmosphere-only photography collages;
- unreadable paragraphs and generated gibberish.

Output: one 16:9 high-resolution interface moodboard showing the eight screens and the token/component strip as a professional design-system sheet.
```

## Divergent territory set

Generate 3–4 boards from the same screen list. Change at least two structural dimensions between territories:

- proof mechanism: documentary story, clinical measurement, personal working tool;
- composition: editorial asymmetry, technical grid, navigable application shell;
- surface rhythm: dark evidence-led, light working-document, photographic editorial;
- data grammar: annotated evidence, trajectory, comparison, timeline, editable plan.

Palette swaps and different photographs do not count as separate territories.

If Image2 returns an atmospheric photography board, palette collage, material swatch sheet or hero-image composition, classify the result as `wrong_artifact_type`. Do not show it as one of the 3–4 territories and do not infer an interface direction from it. Repair the prompt and regenerate the missing interface board.

## Proven territory patterns

### Editorial clinical journey

Use for trust, doctor/program explanation and patient cases. Combine an editorial cover, annotated functional assessment, physician proof, team map, visible progress, case sequence and editable next step.

### Kinetic clinical laboratory

Use for a differentiated, modern rehabilitation system. Combine condensed display typography, dark technical surfaces, movement trajectories, calibration marks, large charts, annotated anatomy or motion, expert credentials and X/Y/Z controls. Alternate with light evidence pages to preserve readability.

### Personal progress atlas

Use for personal plans and family-facing materials. Combine application navigation, personal goal, weekly schedule, responsibility map, observation diary, checkpoint comparison, chronological case atlas and editable next actions.

## QA before Human Gate

- [ ] The board contains 6–8 recognisable screens from the approved material.
- [ ] Every screen has a distinct information object.
- [ ] Charts have sufficient visual area and readable hierarchy.
- [ ] Editable fields and states are visible where the product requires them.
- [ ] The board demonstrates one system, not unrelated attractive screens.
- [ ] The complete set contains 3–4 materially distinct interface boards.
- [ ] No accepted board is an atmospheric photo, palette or texture moodboard.
- [ ] Exact logos, numbers and copy remain outside the generated image layer.
- [ ] The selected territory can be translated into HTML/CSS components.
- [ ] The Human Gate asks which territory should govern the anchor build.

## Learning receipt

Record after selection:

```markdown
Interface moodboards generated:
Reference mechanics used:
Selected territory:
Rejected territories and reason:
Screen types approved:
HTML component implications:
Logo / font / asset gaps:
Human Gate date and decision:
```
