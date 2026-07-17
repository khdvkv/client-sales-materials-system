# Delivery Cabinet, HTML/PDF and QA

## Standalone outputs

Every approved material receives:

- an authoritative editable source;
- a standalone HTML or appropriate editable file;
- a verified PDF with the intended page range;
- a client-world filename and visible title;
- a source/format/version receipt outside the client-visible file.

The PDF is rendered from the accepted source and visually compared with it. A successful export command is insufficient.

## Client cabinet

The cabinet contains full material names, audience-oriented grouping, open, edit when requested, download HTML and download PDF. Internal codes such as A1, B1 or C3 stay in the machine manifest and never appear in client-visible navigation.

Every material must open independently and remain understandable outside the master deck. Remove production slides, reference research, QA methodology, source ledgers, internal statuses and personal Paper Planes contacts.

## Self-contained review copy

Create one local HTML file containing the cabinet, all material HTML, images, fonts required for faithful rendering and downloadable PDF copies when size permits. It must:

- work without the project folder and network;
- contain no `file:///`, `assets/...`, `materials/...` or other unresolved local dependencies;
- reproduce navigation, editing and downloads;
- be checked in a clean browser context;
- stay below the target publication/upload limit.

## PP Pages

Use `pp-pages-manager` and the current official PP Pages instruction. For a protected client publication use the shared document password `pplanes2026` unless Sergey explicitly sets another one. The administrative PP Pages password remains separate and secret.

For an existing project: download and back up the current Edit HTML, compare manual changes, merge, create a preview deployment, run full QA, then promote the verified deployment. Preserve the slug and public key.

## QA matrix

| Gate | Checks |
| --- | --- |
| Structure | material count, page count, names, section boundaries, numbering, navigation |
| Copy | final client text, source support, client vocabulary, no internal labels, no AI slop |
| Visual | benchmark score, rhythm, typography floor, image fidelity/resolution, logo/brand treatment |
| Function | open, edit, save/download HTML, PDF download, print, search/filter and independent opening |
| Cross-surface | standalone source, PDF, cabinet, self-contained copy, preview and public page match |
| Privacy | no personal contact, medical/personal data, unrelated client data, prompts, tokens or production metadata |
| Accessibility | contrast, reading order, alt text where relevant, keyboard use and responsive/mobile behavior |
| Publication | HTTP 200, HTML content type, expected title/text, protected entry, stable public URL |

## Release receipt

```markdown
Project and cabinet version:
Materials and page counts:
Authoritative sources:
Standalone HTML/PDF checked:
Self-contained copy checked:
PP Pages preview checked:
Public deployment checked:
Editing and downloads checked:
Privacy and client-world naming checked:
Known limitations:
Internal readiness:
Client readiness:
```
