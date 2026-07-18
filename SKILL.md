---
name: client-sales-materials-system
description: "Use when a client needs a system, portfolio, roadmap, audit, refresh or production program of sales-support materials across one or more channels and sales stages. Covers research, material selection, reference-backed visual direction, Image2 moodboards, copy, production handoffs, QA and learning from use. Use for requests such as 'материалы поддержки продаж', 'линейка материалов', 'пакет продаж', 'sales kit', 'что нужно менеджеру на каждом этапе', 'пересобрать все материалы', or 'сделать материалы в фирменном стиле'. Do not use as the owner of one already-defined КП, deck or file: route that asset to its genre/format owner after the programme brief is approved."
governance: "SS-10.7 GENRE"
metadata:
  version: "1.2.0"
  source_repository: "https://github.com/khdvkv/client-sales-materials-system"
---

# Client Sales Materials System

## Role

Own the commercial logic of a **portfolio of client sales-support materials**. The portfolio may contain one asset or hundreds, but every item must have a buyer situation, a user, a proof basis, a channel, a next action and a measurable job in the sale or service journey.

This skill produces the portfolio brief, material register, content and visual direction, production waves, and evidence of whether the materials work in use. It does not replace the skill that writes or builds a particular file.

## Trigger and Boundary

Use this skill when the request concerns a system, audit, roadmap, batch or renewal of materials across sales and service. It is the primary `GENRE` owner after `hudi-vault-deliverables` selects the route.

Route a single defined asset to its specialised primary owner:

| Asset or request | Primary owner after this skill defines its brief |
| --- | --- |
| Commercial proposal, tender pack, statement of work | `commercial-proposal-generator` |
| Positioning, message architecture, proof inventory | `paper-planes-positioning` |
| Public comparison or alternatives page | `competitor-alternatives` |
| Long-form HTML, white paper, one-pager | `paper-planes-html-documents` |
| HTML 16:9 slidument / PDF slide deck | `html-slidument-builder` |
| PPTX deck | `consulting-slides-creator` |
| Client Word document | `paper-planes-client-documents` |
| Interactive catalogue, selector, HTML showcase | `html-showcase-builder` |
| Single internal objection guide, talk track, demo script or ROI tool | `sales-enablement` |

Never create two primary owners for the same file. This skill owns the programme, the material register and cross-asset consistency; the specialised skill owns the concrete asset.

## Job Story

When a client has scattered, outdated or missing commercial materials, their team needs a usable set for real buyer situations, so that salespeople, experts and the buyer can move from first contact to decision with relevant proof, consistent language and a clear next action.

## Core Objects

Create and keep these objects in the project folder:

1. **Source register**: approved sources, dates, evidence status, proof gaps and client decisions needed.
2. **Material register**: one row per asset with its job, audience, stage, channel, owner, source basis, format, status and success measure.
3. **Visual direction**: existing brand audit or upgraded design-system brief; reference board; Image2 moodboard; approved visual rules.
4. **Production backlog**: asset waves, dependencies, formats, owners and review order.
5. **QA and effect log**: defects found before release and evidence from actual use after release.
6. **Process passport**: current phase, accepted inputs, human decision, fresh verification, protected invariants and next allowed action.
7. **Delivery cabinet**: client-world names, standalone HTML/PDF files, one self-contained review copy, publication link and update route.

## End-to-End Production Contract

Use [the operating cycle](references/end-to-end-operating-cycle.md) for every programme. It makes twelve phases mandatory: client evidence; material selection; best-in-class research; final copy; art direction; visual production; brand application; HTML/PDF production; cabinet and PP Pages delivery; QA; process control; Loop Engineering learning.

Do not skip a phase because an old deck, template or earlier client project looks reusable. Reuse supplies a tested mechanism or information object; it does not replace current-client evidence, current best-in-class research or a new Human Gate.

## Content and Voice Gate

Use [the content and voice gate](references/content-and-voice-gate.md) before visual production. Client-visible copy must be final copy for the target material, never a description of what the material should contain, a production memo or an internal methodological explanation.

`paper-planes-copy-chief` is the primary language gate for Russian client work. `balakhnin-voice` supplies density, direct thesis, mechanism, stable terms and proof discipline. Sergey hard writing lints override corpus markers that conflict with current rules. `text-deai-editor` performs the final AI-slop scan.

Use [the ABCD content logic](references/abcd-content-logic.md) for every buyer-facing material. It checks whether the reader recognises their situation, understands the client benefit, sees relevant reasons to believe and knows the next step plus what will happen after it. ABCD governs the reading path inside the same-job best-in-class genre sequence; it never substitutes a generic four-block template for genre research.

## Reproducible Quality Floor

Use [the reproducible quality floor](references/reproducible-quality-floor.md) for each new semantic material type and after every material correction. It preserves the Human Gate boundary, client-facing meaning, ABCD sequence, source and privacy rules, accepted visual proposition, typography, asset quality and parity between local, standalone and published surfaces.

## Visual Production and Brand Assets

Use [the visual production and brand-assets module](references/visual-production-and-brand-assets.md) for client photography, retouching, Image2 generation, logos, brand guides, typography, diagrams and asset rights. Real client images are preferred when they carry proof; retouching may improve crop, exposure, colour, noise and legibility while preserving factual reality.

## Delivery Cabinet and Release

Use [the delivery and QA module](references/delivery-portal-qa.md) for standalone HTML/PDF files, a self-contained review copy, the client cabinet, PP Pages publication, privacy checks and release verification. Internal material codes never appear in the client cabinet; use full client-world names.

## OpenDesign Adapter

Use [the adapter](references/open-design-adapter.md) as a supporting method for visual work. It adapts three OpenDesign mechanics to client-commercial materials:

1. `style-extract`: converts existing client files, pages and screenshots into an auditable brand-use receipt;
2. `territory-choice`: turns researched references into 2–3 materially distinct Image2 moodboard territories and records the selected direction;
3. `render-critique`: runs an evidence-led visual repair loop on the actual output surface.

The adapter supplies evidence and decision mechanics. `marcom-visual-intelligence` remains the owner of visual-reference logic; the relevant format skill remains the owner of the output file.

## Visual Benchmark 2026

Use [the visual benchmark](references/visual-benchmark-2026.md) for every anchor asset and for any client-facing portfolio that claims a renewed or upgraded visual language. A technically clean render is insufficient for `client_ready` status. The asset must meet the benchmark score and pass the sequence review.

## Art-Direction Loop

Use [the art-direction loop](references/art-direction-loop.md) whenever the brief asks for a new visual territory, a major style upgrade, a best-in-class result or a remedy for generic AI design. This loop extends the visual benchmark with reference evidence, deliberate divergence, independent critique and a learning receipt.

## Cumulative Deck Loop

Use [the cumulative deck loop](references/cumulative-deck-loop.md) when several presentation-based materials will be produced inside one growing master deck. It keeps buyer situations, sources, review states and exports isolated while allowing the visual system and components to improve cumulatively. It also adds a measured readability gate, a fresh-source check for evidence-led pages and a mandatory Human Gate before a new semantic material type is appended or used as a reference.

## MECE Material Stack

Use [the MECE material stack](references/mece-material-stack.md) for every anchor material before layouts, Image2 generation or production scaling. It separates nine layers that otherwise collapse into the vague instruction to "make it look better": commercial task; claims and proof; reading scenario; information objects; art direction; layout and typography; assets; components and behaviour; technical release.

Image2, photography and icons belong only to the asset layer. A strong render cannot compensate for a missing decision, weak evidence, an unreadable diagram, arbitrary layout or an unusable file. Every anchor asset needs a short receipt for each layer; the external loop then records version, approval, first use and observed effect.

## Material Catalogue

Select materials from buyer situations, not from a fixed list. The following catalogue is a starting set.

| Buyer situation | Typical materials | Job of the material |
| --- | --- | --- |
| First recognition | company profile, sector landing, short video, event panel, expert article, social post, industry one-pager | explain relevance and earn the next conversation |
| Discovery and diagnosis | discovery questionnaire, audit, checklist, calculator, requirements form, workshop canvas, diagnostic report | help the buyer describe the task and expose missing data |
| Trust and proof | casebook, reference list, certificates, expert/team profiles, site photo report, testimonials, compliance or safety pack | make competence and delivery capacity credible |
| Comparing options | product/service catalogue, selector, comparison table, technical note, FAQ, objection guide, competitor brief | help the buyer compare choices on meaningful criteria |
| Solution review | executive deck, product deck, demo script, use-case pack, scheme, prototype, visualisation, sample specification | show how the proposed solution works in the buyer's context |
| Commercial decision | proposal, estimate, ROI/TCO calculator, scope, implementation plan, responsibility matrix, contract annex, tender response | remove uncertainty around price, scope, risk and decision path |
| Implementation and handover | project passport, kickoff pack, timeline, technical documentation, training materials, acceptance checklist, support guide | align the client team before delivery and launch |
| Retention and advocacy | service report, renewal proposal, results dashboard, quarterly review, case-story template, referral kit | demonstrate delivered value and create the next commercial reason |

Add channel-specific variants when the journey requires them: email and CRM sequences, messenger scripts, website modules, bot messages, webinar scripts, exhibition materials, sales-room screens, printed leave-behinds, partner kits, onboarding videos and self-service knowledge pages.

## Standard Workflow

The numbered workflow below is governed by the twelve-phase operating cycle. Every transition needs its named receipt and next allowed action.

### 1. Admit the assignment and set the commercial frame

Record:

- client, offering and market;
- buyer roles and buying situation;
- sales/service stage, channel and real user of each material;
- desired business effect and available proof;
- existing materials and what is already approved;
- delivery deadline, legal, technical, budget and production constraints.

Do not treat an existing deck as permission to invent new facts. Mark each source as `confirmed_fact`, `working_hypothesis`, `proof_gap`, `client_decision_needed` or `implementation_constraint`.

### 2. Build the material register before producing files

For every proposed asset record:

| Field | Required content |
| --- | --- |
| Material | concrete name, version and format |
| Buyer situation | what is happening when it is used |
| Audience and user | buyer role and sender/presenter |
| Reader job | decision or action this asset enables |
| ABCD receipt | exact Attention, client Benefits, claim-linked Credentials and Destination route |
| Proof | cases, data, documents, people, photos, certifications or a stated gap |
| Channel | meeting, email, CRM, website, event, print, messenger, tender or service touchpoint |
| Next action | what recipient and sender do after use |
| Owner and cadence | who updates, sends or presents it |
| Success measure | use rate, response, meeting conversion, time-to-proposal, objection reduction, win rate, renewal or qualitative feedback |
| Status | backlog, briefed, sourced, visual direction approved, copy ready, produced, QA, reviewed, released, effect verified |

Prioritise with a transparent rule: buyer impact, proof readiness, frequency of use, commercial urgency, production effort and dependency on other materials.

### 3. Research and reference direction

Use `client-intel-agent`, `research-agent`, `paper-planes-positioning`, `reference-corpus-archivist` and `marcom-visual-intelligence` as supporting layers when their evidence is needed.

For an existing client style, audit the logo, colour, typography, layout, imagery, diagrams, accessibility, digital and print constraints. Preserve recognisable codes that fit the current business task.

For a style that needs strengthening, create a concise visual-system brief: typography roles, colour rules, grid, image treatment, diagram grammar, data display, page numbering, logo use, prohibited moves and accessibility limits.

Build a reference board from three layers:

1. direct category and competitor examples;
2. best-in-class analogs with a similar trust, complexity or buying mechanism;
3. current visual and interaction signals, checked for fit rather than copied for fashion.

Every reference row must say: exact source, freshness, transferable mechanic, what must not be copied, fit to this client, intended touchpoint and evidence status.

Before accepting a reference, name the actual job and primary surface of the planned asset. A decision brief is compared with decision briefs; an intake form with intake forms; a treatment plan with treatment plans; a progress report with progress reports. Adjacent clinical workflows may supply field logic, yet they cannot define the information hierarchy for a different document job. Record rejected archetypes and the reason for rejection.

For every selected material type, open at least three real complete examples in its primary format when they are available, preferably current PDF/HTML files from official organisations, studios, agencies or product teams. Search results, thumbnails and screenshots are discovery evidence only. Record the complete document sequence, page count, information objects, proof order, CTA, transferable mechanics, exclusions and source date. If complete examples cannot be opened, mark `reference_gap`; do not present adjacent document types as best-in-class proof.

Complete `style-extract` before choosing a territory. The resulting receipt separates retained client codes, corrections needed for the current channel and unverified assumptions.

### 4. Moodboard and Image2 gate

Use the reference board to write 2–3 distinct visual territories. Each territory includes a representative buyer-facing fragment: for example, one slide, page, catalogue spread, landing hero or CRM card.

When the target is a future HTML/PDF presentation, slidument, interactive catalogue or client cabinet, use [the Image2 interface-moodboard prompt](references/image2-interface-moodboard-prompt.md). Generate 3–4 materially distinct boards showing the future interface system: multiple real screen types, grid, typography, navigation, charts, forms, editable fields and component behaviour. A photography, palette or atmosphere collage does not satisfy an interface-moodboard request and must be rejected before the Human Gate.

Generate or edit the visual fragment with Image2 only after the territory specifies:

- the scene, object, location and people if applicable;
- client logo treatment and prohibited text in imagery;
- camera, light, material, palette and aspect ratio;
- brand codes to preserve;
- negative constraints: generic stock, repeated image, unreadable lettering, inaccurate equipment, foreign cultural context, visual overclaim;
- usage role in the material and accessibility needs.

The client or project lead approves one territory before a production wave. An image is never reused across adjacent or unrelated high-visibility assets without an explicit decision.

Use `territory-choice` for this approval. Three territories must differ in visual code or proof mechanism, rather than in decorative colour or crop.

### 5. Create the asset brief and route production

For each selected material, write a one-page brief:

- action title or reader promise;
- evidence, required facts and proof gap;
- narrative sequence and visual object;
- format, channel and adaptation variants;
- link to the approved visual territory;
- completed ABCD receipt with claim-to-proof links and Destination strength;
- acceptance criteria and reviewer.

Use the MECE material stack to make the acceptance criteria inspectable. The brief must name the commercial task, proof, reading scenario, principal information object, art-direction proposition, layout rule, asset needs, component set and actual release channel.

Then hand the item to one specialised production skill from the routing table. The production skill must keep the approved source boundaries and visual direction.

Write the complete client-facing text before layout. A content plan becomes `copy_ready` only when every page or section contains its final title, body, proof, caption, qualification and next action. Do not visualise labels such as “what goes here”, “production cycle”, “source policy” or another description of internal work unless that content is itself the client material.

### 6. Produce in waves

Start a new programme with one anchor asset or one representative fragment. After its review, produce the next wave:

- Wave 1: anchor material and visual-system proof;
- Wave 2: high-frequency materials that reuse approved mechanics;
- Wave 3: stage-specific and channel-specific variants;
- Wave 4: maintenance assets, templates and update instructions.

Use batches only after the visual language, copy register and QA standards have proved stable. A large requested quantity does not waive individual asset briefs and visual checks.

Before Wave 2, review three non-adjacent rendered assets and a contact sheet of the full sequence. Apply the visual benchmark. If the score is below the threshold or one dimension scores below `3 / 5`, revise the anchor asset and direction before scaling production.

Apply the visual-richness invariant before every expansion: the material must use purpose-led information objects and maintain the approved sequence rhythm. A batch fails when text is merely distributed across uniform cards, more than two neighbouring pages repeat the same composition grammar, high-value evidence remains prose although it can become a comparison, route, timeline, annotated photograph, table, map or decision object, or client imagery is reduced to decorative background. Stop scaling and repair the anchor when this invariant fails.

For high-art-direction work, run the full art-direction loop before Wave 2. A passing technical render without the atlas, critical review and a client-language uniqueness result stays at `draft_for_review`.

### 6a. Use one cumulative master deck when the programme requires it

When the client or project lead explicitly chooses one growing deck for several materials:

- keep a master manifest with one section per material, its buyer situation, reader decision, source boundary, current page range, status and export target;
- give every slide a stable material code and slide identifier;
- append only a reviewed section or a clearly marked prototype with named source gaps;
- export client-facing PDFs by material section, never as an accidental dump of the whole production deck;
- repeat the complete cycle for every section: current references, content admission, visualisation, art-direction critique, comments, repair and fresh render;
- when the reviewer explicitly requests one later review of the complete deck, record the complete-deck Human Gate, keep all new sections internal_prototype, preserve per-section best-in-class and QA receipts, and wait for the full-deck review before promoting them;
- integrate accepted standalone sections from their authoritative source and compare the first and last rendered page of every section with that source;
- after every three appended sections, inspect the first, middle and latest section plus the full contact sheet for typography, image reuse, claim drift and repeated layout grammar.

The master deck is a production object. It does not turn ten buyer situations into one undifferentiated client presentation.

### 7. Quality gates

Before release, apply these gates:

1. **Source and claim gate**: every commercial claim is evidenced or removed from client-visible copy.
2. **Buyer-situation gate**: the material has a named user, moment, decision and next action.
3. **ABCD gate**: the material passes the whole-sequence and page-level checks in `references/abcd-content-logic.md`; evidence is written for the recipient, every important benefit has relevant proof, and Destination describes the first step and what follows.
4. **Voice gate**: `paper-planes-copy-chief` and `text-deai-editor` remove generic AI language, internal labels and unsupported persuasion.
5. **Visual gate**: `marcom-visual-intelligence` checks reference fit; the production owner checks style, image quality, readability and brand use.
6. **Format gate**: the relevant builder renders and inspects the actual HTML, PDF, PPTX, DOCX, print or screen surface.
7. **Portfolio gate**: the register has no unexplained duplication, stage gap, conflicting message or unowned material.
8. **Visual benchmark gate**: the anchor assets pass the 2026 scorecard, anti-template checks and sequence review in `references/visual-benchmark-2026.md`.
9. **Art-direction gate**: where the brief requires best-in-class quality, the atlas, divergence set, two critique passes and learning receipt in `references/art-direction-loop.md` are complete.
10. **Material-stack gate**: every anchor asset has a result for all nine layers in `references/mece-material-stack.md`; image quality is assessed only as the asset layer, alongside information design, layout, components and technical release.
11. **Measured readability gate**: inspect computed type sizes and the rendered surface at intended viewing distance. For a 1280 × 720 HTML readout, use 12 px as the default floor for meaningful body copy; reserve 9–11 px for folios, short labels and source notes that do not carry the decision. Set a larger floor for a live-room deck. Do not transfer this number mechanically to print, mobile or other canvases.
12. **Fresh-source proof gate**: reopen drift-prone official sources before finalising evidence pages, statistics, contacts, prices, service formats and legal claims. A previously used number that is absent from the current source returns to `proof_gap` and leaves the client-visible file.
13. **Master-deck isolation gate**: when a cumulative deck is used, confirm stable section identifiers, correct export range, no cross-material facts without revalidation, and no internal manifest or production status in the client export.
14. **Master-deck integration gate**: compare the first and last rendered page of every section with its authoritative source; inspect every embedded A4 page; rerun page-count, contact, privacy and language checks on the complete export after the latest local repair.
15. **Final-copy gate**: every visible phrase belongs to the target client material; internal production notes, methodology labels and descriptions of future content are absent.
16. **Anti-slop and register gate**: `paper-planes-copy-chief`, `balakhnin-voice` in register mode and `text-deai-editor` have been applied in this order; source facts, client vocabulary and hard Russian lints remain intact.
17. **Visual-richness gate**: the sequence contains purpose-led information objects, client-specific visual proof and deliberate rhythm; uniform title-plus-card pages cannot receive `client_ready` status.
18. **Brand-and-assets gate**: every logo, font, photo, retouched image and generated visual has a source, allowed use, role, quality check and approved treatment.
19. **Cabinet-and-release gate**: each material opens independently, has a verified PDF, uses a full client-world name, and appears in a self-contained review HTML plus the approved publication surface.
20. **Privacy gate**: no Paper Planes employee contact, personal data, internal code, hidden review status, prompt, source ledger or unrelated project content remains in client-visible files.
21. **Reproducible-quality gate**: the bounded loop, protected-invariant recheck, Human Gate boundary and cross-surface checks in `references/reproducible-quality-floor.md` are recorded for every new semantic material type.

Run `render-critique` on each anchor asset and on every asset with a material visual correction. Compare the fresh render against its approved brief, client style receipt and selected territory; patch the smallest defect; re-render; then record the observed change.

Client-visible materials contain no production comments, placeholders, source ledgers or unverified metrics.

### 8. Verify use and improve

Release is different from verified usefulness. Collect a small set of evidence appropriate to the asset: usage count, seller feedback, buyer questions, response rate, meeting conversion, time saved, objection frequency, deal movement, renewal or win/loss note.

Update the material register after the first use cycle. Improve the asset, its brief or the visual system only when a real recurring pattern is observed.

## Loop Engineering Contract

Use `loop-engineer` as a supporting skill whenever this programme is created, repaired, expanded or reviewed.

1. State `Итерация X из Y`, scope, acceptance criterion and current programme stage.
2. Observe the actual register, sources, accepted visual reference, latest review and QA receipts.
3. Diagnose one primary divergence: missing proof, wrong material for the buyer moment, style drift, weak copy, unusable channel adaptation, or a production defect.
4. Choose one route: `revise_current_iteration`, `advance_with_comment`, `replan_from_current_state` or `clarify_route`.
5. Apply the smallest reversible correction, then obtain a fresh observation: render, live-file inspection, user review or first-use evidence.
6. Distinguish `produced`, `released` and `effect_verified`. Only the last state confirms that the material helped in its intended situation.
7. Treat one client correction as a local incident. Promote it to a reusable rule only after varied cases, counterexamples, a named scope and an eval fixture.
8. For a candidate shared improvement, record the rejected observation, repaired observation, task-family scope, counterexample, fresh effect check, rollback route and eval id. A clean render proves surface repair; human review or repeated use is still required for `effect_verified`.
9. When a master deck contains several semantic material types, human approval is section-scoped. Approval of an anchor slide, visual mood or earlier material does not approve the full new section. Keep unreviewed work `internal_prototype`, stop expansion after the current saved state and obtain a Human Gate before appending the next type.
10. Carry protected invariants after every repair: client Job Story, source boundary, final-copy status, accepted visual proposition, typography floor, client vocabulary, privacy, export boundaries and previously accepted decisions.
11. Use a visual quality ledger with observed defect, affected buyer outcome, repair, before/after render and reviewer result. Aesthetic preference becomes a shared rule only after varied projects, a counterexample and an eval.
12. Apply built-in quality before batch production: reference evidence, final copy, representative visual, art-direction score, privacy and real-surface QA all pass on the anchor. Kaizen improves a passing process from observed use; it never lowers a gate to preserve production speed.

The programme may add a project-local template or validator under A2 when it has a rollback route and an effect check. Changes to shared policy, a cross-project skill, global validator or registry require the user's explicit approval and must include an eval and rollback note.

## Output Contract

For a new programme, deliver:

1. a source and proof summary;
2. a material register with priority and owners;
3. a reference board and 2–3 Image2 visual territories;
4. an approved-direction receipt;
5. production waves and asset briefs;
6. links to produced materials and their QA receipts;
7. an effect log after use.
8. a self-contained client cabinet with standalone HTML/PDF materials, a local review copy and a publication receipt when requested.

Mark readiness precisely:

- `internal_plan`: materials and direction are still being selected;
- `draft_for_review`: a real file is ready for project review;
- `client_ready`: claims, voice, visual and format gates passed;
- `released`: sent or published;
- `effect_verified`: use evidence confirms the intended job;
- `blocked_by_source_gap`: missing fact, proof, permission or client decision prevents safe completion.

## Quality Checklist

- [ ] A buyer situation, user, proof and next action exist for every material.
- [ ] Every material has an exact ABCD receipt; Attention names the reader situation, Benefits name client outcomes, Credentials are linked to promises, and Destination shows the first step and what follows.
- [ ] Evidence pages present recipient-facing proof and its meaning; internal audit or production commentary appears only when that is the material's explicit job.
- [ ] The register covers the needed journey without filling it with decorative assets.
- [ ] Existing client brand assets were opened before any redesign.
- [ ] Current external references have URLs or screenshots and freshness status.
- [ ] The moodboard contains transfer mechanics and do-not-copy constraints.
- [ ] For HTML/PDF interface work, Image2 produced 3–4 materially distinct boards; each shows 6–8 representative screens and a token/component strip, with no atmosphere or photography collage substituted for the interface.
- [ ] Image2 images are specific to the asset role and do not repeat without a decision.
- [ ] The anchor material has passed all nine MECE material-stack layers, including information objects, layout, components and technical release.
- [ ] Client language uses concrete roles, documents, evidence, deadlines and decisions.
- [ ] Every production file was inspected in its real output format.
- [ ] Meaningful slide copy passes the intended-distance readability floor; small text is limited to labels, folios and source notes.
- [ ] Drift-prone facts on evidence pages were reopened at the current official source before handoff.
- [ ] A cumulative master deck, when used, has isolated material sections and verified client export ranges.
- [ ] The portfolio has a maintenance owner and an update rule.
- [ ] First-use evidence is planned before calling the programme complete.
- [ ] The fact register covers project files, meeting transcripts and current external sources with freshness and privacy status.
- [ ] Every material type has complete best-in-class examples performing the same reader job, or an explicit `reference_gap`.
- [ ] Final client copy exists before layout and has passed Paper Planes, Balakhnin-register and AI-slop checks.
- [ ] The contact sheet shows deliberate visual rhythm and no drift into uniform text cards.
- [ ] Real and generated visual assets have provenance, role, quality, rights and retouch/generation receipts.
- [ ] Standalone HTML and PDF files, the self-contained review copy and the published cabinet reproduce the same accepted content.
- [ ] Privacy and client-world naming checks remove internal codes, personal contacts and production debris.
- [ ] Every correction has a fresh observation and a protected-invariant recheck; automatic QA and Human Gate status are recorded separately.
