# OpenDesign Adapter for Client Sales Materials

## Purpose

This adapter takes three useful OpenDesign mechanics and applies them to client-facing commercial materials. It keeps the client brand, buyer situation, source boundaries and approval gates in control.

Source mechanics reviewed in the local OpenDesign checkout:

- `plugins/_official/atoms/design-extract/SKILL.md`;
- `plugins/_official/atoms/direction-picker/SKILL.md`;
- `plugins/spec/examples/refine-critique-loop/SKILL.md`.

## Module 1. Style Extract

### Input

- current client website, logo files, brand guide, presentation, catalogue, proposal or screenshots;
- production constraints: screen, print, email, exhibition, tender, CRM or messenger;
- required recognisability and accessibility constraints.

### Method

Extract only visible and verifiable rules:

| Area | Capture |
| --- | --- |
| Logo | file, safe zone, placement, prohibited treatment |
| Colour | named values, contrast role, accent frequency |
| Typography | display, title, body, caption and numeric roles |
| Grid | margins, columns, reading density, alignment |
| Imagery | subject, location, camera, treatment, image quality, prohibited stock patterns |
| Diagram grammar | lines, nodes, cards, tables, data labels, numbering |
| Voice | client terms, tone, facts that require proof |

### Output: Style Receipt

```markdown
## Style receipt

Sources opened:
Retained codes:
Corrections for this channel:
Prohibited moves:
Unverified assumptions:
Reviewer:
```

### Acceptance criterion

A reviewer can locate every retained code in a named client source or approve it as a specific upgrade. The receipt never turns a guessed rule into a fact.

## Module 2. Territory Choice

### Input

- material brief and buyer situation;
- reference board with category, analog and current examples;
- style receipt and proof inventory;
- target output: one representative slide, page, catalogue spread, landing fragment or CRM card.

### Method

Create exactly 2–3 territories. Each contains:

| Field | Required content |
| --- | --- |
| Name | short, concrete visual name |
| Buyer job | what must become believable or easy to decide |
| Transfer mechanic | exact layout, proof, image, hierarchy or interaction rule |
| Image2 fragment | prompt-ready representative scene and aspect ratio |
| Retained client codes | logo, colour, typography or image rule |
| Do not transfer | category, cultural, legal, operational or proof risk |
| Production consequences | what assets, photos, data and formats the choice requires |

The three territories must offer distinct proof or visual mechanisms. Cosmetic variations fail this gate.

### Output: Direction Receipt

```markdown
## Direction receipt

Territories shown:
Selected territory:
Why it fits the buyer situation:
Reference mechanics adopted:
What is excluded:
Image2 fragment approved:
Decision maker and date:
```

### Acceptance criterion

One territory is selected before the next production wave. If the brief changes materially, return to this module and regenerate the choice set.

## Module 3. Render Critique

### Input

- actual rendered file or screenshot;
- asset brief, style receipt and direction receipt;
- latest client comment, if one exists.

### Method

Inspect five dimensions:

| Dimension | Test |
| --- | --- |
| Commercial use | buyer can find the proof and next action for the intended moment |
| Hierarchy | action title, evidence and visual object remain readable in sequence |
| Brand fit | retained codes and approved upgrades are visible; prohibited moves are absent |
| Visual accuracy | image resolution, equipment, logo, diagrams, spacing, crop and labels are credible |
| Surface quality | no overlap, clipping, broken asset, unreadable contrast, missing page number or internal note |

Patch the smallest defect. Re-render and inspect the same dimension again. After two cycles without a fresh observed improvement, return to the material brief or territory choice.

### Output: Render Receipt

```markdown
## Render receipt

Artifact and version:
Visual issue:
Evidence:
Patch applied:
Fresh observation:
Remaining risk:
Status: draft_for_review | client_ready | blocked_by_source_gap
```

### Acceptance criterion

The actual rendered surface meets the asset brief and contains no client-visible production debris. A render pass alone proves surface readiness; first-use evidence remains a separate commercial gate.

## Loop Route

| Observation | Route |
| --- | --- |
| Layout, copy, image or component defect in the accepted direction | `revise_current_iteration` |
| Accepted asset has a later-stage comment, such as a maintenance template | `advance_with_comment` |
| Buyer, source of truth, channel or client purpose changed | `replan_from_current_state` |
| Two directions have materially different commercial consequences and evidence is insufficient | `clarify_route` |

## Guardrails

- A reference gives transferable mechanics, never a ready-made client style.
- A generated image must serve a defined role in a material and pass image-quality inspection.
- A single client comment remains local until varied evidence supports a broader rule.
- Keep source receipts, direction receipts and render receipts outside client-visible pages.
