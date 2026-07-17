#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
required_references = [
    "end-to-end-operating-cycle.md",
    "content-and-voice-gate.md",
    "visual-production-and-brand-assets.md",
    "delivery-portal-qa.md",
    "art-direction-loop.md",
    "visual-benchmark-2026.md",
    "cumulative-deck-loop.md",
    "open-design-adapter.md",
    "mece-material-stack.md",
    "image2-interface-moodboard-prompt.md",
]
required_terms = [
    "balakhnin-voice",
    "Image2",
    "PP Pages",
    "self-contained",
    "Visual-richness",
    "Loop Engineering",
    "Privacy gate",
]

for name in required_references:
    path = ROOT / "references" / name
    assert path.exists(), f"missing reference: {name}"
    assert f"references/{name}" in skill, f"reference not linked from SKILL.md: {name}"

for term in required_terms:
    assert term in skill, f"required term missing from SKILL.md: {term}"

data = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
assert data["skill_name"] == "client-sales-materials-system"
ids = [item["id"] for item in data["evals"]]
assert len(ids) == len(set(ids)), "duplicate eval ids"
assert len(ids) >= 21, "expected at least 21 evals"

print(json.dumps({"ok": True, "references": len(required_references), "evals": len(ids)}, ensure_ascii=False))
