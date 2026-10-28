"""Run the existing RIF API on three exact, entirely synthetic phase arrangements."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "rif-project" / "src"))
from rif.rif import ignition_probability, rif_coherence


def run_demo() -> dict:
    inputs = (
        ("Aligned", np.zeros(8)),
        ("Spread over half a circle", np.linspace(-np.pi / 2, np.pi / 2, 8)),
        ("Evenly spaced around a circle", np.arange(8) * (2 * np.pi / 8)),
    )
    cases = []
    for label, phases in inputs:
        coherence = float(rif_coherence(phases))
        mapped = float(ignition_probability(coherence, beta=12.0, threshold=0.55))
        cases.append({
            "case": label,
            "phases_radians": [round(float(x), 8) for x in phases],
            "coherence": round(coherence, 6),
            "logistic_output": round(mapped, 6),
        })
    module = ROOT / "rif-project" / "src" / "rif" / "rif.py"
    return {
        "fixture": "eight synthetic phase angles per case; no biological data",
        "source_module_sha256": hashlib.sha256(module.read_bytes()).hexdigest(),
        "mapping": {"beta": 12.0, "threshold": 0.55, "status": "unvalidated mathematical transform, not a measured probability"},
        "cases": cases,
    }


def diagram(result: dict) -> str:
    cards = []
    for i, case in enumerate(result["cases"]):
        left = 38 + i * 390
        cx, cy, radius = left + 175, 222, 67
        vectors = []
        for phase in case["phases_radians"]:
            x, y = cx + radius * math.cos(phase), cy - radius * math.sin(phase)
            vectors.append(f'<path d="M{cx} {cy} L{x:.3f} {y:.3f}" stroke="#2e729e" stroke-width="2" opacity="0.65"/><circle cx="{x:.3f}" cy="{y:.3f}" r="4" fill="#2e729e"/>')
        heading = ("All 8 aligned", "Spread across 180°", "Evenly spaced over 360°")[i]
        cards.append(f'''<rect x="{left}" y="109" width="365" height="289" rx="12" fill="white" stroke="#d7e1eb"/>
<text x="{left+182}" y="142" text-anchor="middle" font-size="22" font-weight="bold" fill="#203b53">{heading}</text>
<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#d3dde7" stroke-width="1.5"/>
{''.join(vectors)}<circle cx="{cx}" cy="{cy}" r="3" fill="#64748b"/>
<text x="{left+23}" y="329" font-size="20" fill="#475569">Coherence</text><text x="{left+340}" y="329" text-anchor="end" font-size="26" font-weight="bold" fill="#0f172a">{case['coherence']:.6f}</text>
<text x="{left+23}" y="368" font-size="18" fill="#64748b">Logistic output</text><text x="{left+340}" y="368" text-anchor="end" font-size="22" fill="#334155">{case['logistic_output']:.6f}</text>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="470" viewBox="0 0 1200 470" role="img" aria-labelledby="title desc">
<title id="title">RIF: actual outputs for three synthetic phase arrangements</title>
<desc id="desc">Eight aligned phases give coherence 1.000000; eight angles spread across half a circle give 0.547661; eight evenly spaced angles around a circle give 0.000000. The displayed logistic outputs are mathematical transformations, not validated probabilities of conscious access.</desc>
<rect width="1200" height="470" rx="14" fill="#f4f7fb"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="40" y="47" font-size="16" letter-spacing="2" fill="#46627d">RUNNABLE DEMO · NO BIOLOGICAL DATA</text>
<text x="38" y="86" font-size="30" font-weight="bold" fill="#0f172a">Phase angles in → circular coherence out</text>
{''.join(cards)}
<text x="40" y="432" font-size="18" fill="#334155">The logistic transform uses beta = 12 and threshold = 0.55; it is an unvalidated model choice.</text>
<text x="40" y="459" font-size="17" fill="#64748b">This demonstrates numerical code behaviour, not a theory of consciousness or a clinical result.</text>
</g></svg>\n'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-assets", action="store_true", help="Regenerate the tracked documentation output and SVG.")
    args = parser.parse_args()
    result = run_demo()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write_assets:
        out = ROOT / "docs" / "demo"
        out.mkdir(parents=True, exist_ok=True)
        (out / "output.json").write_text(text, encoding="utf-8")
        (out / "demo.svg").write_text(diagram(result), encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
