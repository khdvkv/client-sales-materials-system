# Client Sales Materials System

Codex skill for managing the complete production cycle of a client sales-support materials portfolio.

It covers:

1. client evidence from project files, meetings and current external sources;
2. material selection by buyer situation and decision;
3. complete best-in-class research for every material type;
4. final client copy with source, Paper Planes, Balakhnin-register and AI-slop checks;
5. art direction, built-in visual quality and Loop Engineering improvement;
6. real-image retouching and Image2 generation;
   for future HTML/PDF materials, Image2 produces 3–4 interface boards with real screens, grids, charts, forms and navigation rather than an atmospheric photo collage;
7. client brand, logo, typography and asset application;
8. standalone HTML and verified PDF production;
9. client cabinet, self-contained review HTML and PP Pages publication;
10. source, copy, visual, format, privacy and functional QA;
11. visible phase-by-phase process passports and Human Gates;
12. bounded Loop Engineering learning with evals and rollback.

The entry point is [`SKILL.md`](SKILL.md). Detailed operating modules are in [`references/`](references/), and regression scenarios are in [`evals/evals.json`](evals/evals.json).

## Install

Copy or symlink this directory into the Codex skills directory as `client-sales-materials-system`.

## Validation

```bash
python3 scripts/validate_skill.py
```

## Status

The method is reusable across medical and non-medical client projects. Project-specific facts, visual choices and learning stay local until varied evidence and evals support a shared rule.
