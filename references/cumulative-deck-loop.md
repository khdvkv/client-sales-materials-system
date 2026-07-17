# Cumulative master-deck production loop

## Purpose

Use one growing presentation file for a portfolio without collapsing different buyer situations into one story. The master deck accumulates approved visual grammar, components and reviewed sections. Every client-facing material still has its own job, source boundary and export.

## Trigger

Apply this module when:

- two or more presentation-based materials share a client, visual system and production team;
- the project lead explicitly wants one fillable master deck;
- later sections should reuse verified components from earlier sections;
- the team needs section-level exports and cumulative quality checks.

## Counterexamples

Do not apply the master-deck contract automatically to:

- one defined presentation;
- an A4 report, mobile card or interactive form whose primary surface is not 16:9;
- unrelated clients or products that merely share a template;
- materials whose confidentiality rules prohibit a common source file.

Such assets may reuse components while retaining separate production files.

## Required objects

### Master manifest

For every section record:

| Field | Required value |
| --- | --- |
| Material code | stable portfolio identifier |
| Buyer situation | moment in which the material is used |
| Reader decision | action or choice enabled by the section |
| Source boundary | approved sources, freshness date and gaps |
| Slide range | current section pages in the master deck |
| Export target | client PDF, meeting deck, print adaptation or prototype |
| Status | internal plan, draft, reviewed, client ready, released or effect verified |
| Last review | reviewer, date and material comment |

### Slide identity

Every slide has a stable section code and slide id. In HTML, prefer `data-material` and `data-slide-id`. Identifiers support section exports, review receipts and regression checks; they stay outside visible client copy.

## Per-section cycle

Run the full cycle for every new material section:

1. **Best current solutions.** First name the document job and primary surface: decision brief, intake form, treatment plan, progress report, referral card, presentation or another observable artifact. Open direct references that perform that same job, then comparable trust/complexity references and current visual references. Record exact mechanics, exclusions and why adjacent workflow documents were rejected.
2. **Content admission.** Confirm buyer situation, conclusion, proof, source status, decision and next action. Reopen facts that can drift.
3. **Representative visualisation.** Build one real slide or bounded group with actual copy length and intended assets.
4. **Art-direction review.** Score the rendered surface using the visual benchmark and run a separate buyer-and-brand critique.
5. **Comment routing.** Use `revise_current_iteration`, `advance_with_comment`, `replan_from_current_state` or `clarify_route` according to the failed or changed criterion.
6. **Fresh observation.** Re-render, inspect at 100%, inspect the section inside the contact sheet and compare it with the accepted reference.
7. **Human Gate.** Show the complete rendered section and its contact-sheet position to the named reviewer. Record what was reviewed, what was accepted and what remains automatically checked only. An accepted mood, cover or anchor slide does not approve the rest of the semantic type. The reviewer may explicitly move the gate to the complete-deck level; record that authorization, keep every section at internal_prototype, run the full per-section reference and QA cycle, and promote sections only after the complete deck is reviewed.
8. **Append and export.** Add only the human-reviewed section to the accepted layer of the master deck, update its manifest range and verify the section-only client export. Unreviewed work may remain in a reversible internal-prototype layer, clearly excluded from client exports and reference status.

## Expansion stop rule

Stop adding semantic material types when the latest completed type lacks a Human Gate. Preserve the current saved state, label the new section `internal_prototype`, and return a review receipt with these fields:

- full section range and section-only export;
- exact surfaces seen by the reviewer;
- decisions explicitly accepted by the reviewer;
- copy, visual and source decisions transferred without human approval;
- next allowed action.

Resume expansion only after the reviewer accepts the complete section or provides a bounded repair list. Approval never propagates automatically from one material type to another.

## Accepted-source integration

Treat a reviewed section or standalone A4 document as an authoritative source. When the master deck is assembled:

1. embed or merge from the accepted source through a controlled route;
2. keep its page count and stable identity;
3. render the first and last page of every section plus both pages of every embedded A4;
4. compare the rendered pages with the authoritative export;
5. rerun full-deck text, privacy, contact and page-count checks after any local repair.

An iframe, query filter or page-offset mechanism requires a rendered regression fixture. Source presence in HTML does not prove that the intended page appeared in the exported PDF.

## Measured readability gate

Spatial fill does not prove legibility. Before review and before export:

1. collect computed font sizes for meaningful text roles;
2. separate decision-bearing copy from folios, source notes and short labels;
3. inspect the rendered page at intended viewing distance;
4. repair the smallest roles first, then rebalance rows, columns or copy length;
5. repeat overflow, contact-sheet and 100% checks after the change.

For a 1280 × 720 HTML readout, 12 px is the default floor for meaningful body copy. A live-room presentation normally needs a larger floor. Print, mobile and large-format surfaces require their own physical-size and distance rule.

## Fresh-source evidence gate

Evidence pages receive a second source pass immediately before handoff:

- reopen official statistics, prices, contacts, service formats, licences and legal statements;
- record the current source and check date;
- compare the visible claim with the current wording;
- remove or downgrade a claim when the current source no longer supports it;
- re-render the page after the evidence change because revised numbers alter hierarchy and layout.

## Cumulative review

After every three appended sections:

- inspect the first, middle and latest section at intended size;
- review the full contact sheet;
- check repeated photographs and repeated composition grammar;
- check typography floors and heading rhythm;
- check whether a fact crossed into another material without source revalidation;
- verify each client export begins and ends at the intended section boundary.

## Loop Engineering learning receipt

Record a reusable candidate only when the defect recurs or has evidence beyond one isolated preference:

```markdown
Rejected observation:
Affected outcome:
Local repair:
Fresh effect observation:
Task-family scope:
Counterexample:
Confidence:
Eval id:
Rollback:
Human review:
```

The rule remains a candidate until a fresh human review or use observation confirms the effect.

## Regression fixture

The initial fixture for this module covers two failures:

1. a slide deck passes fill measurements while decision-bearing copy remains 9–11 px;
2. an evidence page retains previously used statistics that are absent from the current official source.

Passing behavior measures type roles, enlarges meaningful copy, reopens the source, removes unsupported claims, re-renders the affected pages and preserves section export boundaries.

## Rollback

If this module creates unnecessary overhead or fails its evals:

1. remove the `Cumulative Deck Loop` link and the related additions in steps 6, 7, the Loop Engineering contract and the checklist;
2. remove this reference file;
3. remove the corresponding eval fixtures;
4. keep project-local manifests and slide identifiers, because they do not depend on the shared rule.
