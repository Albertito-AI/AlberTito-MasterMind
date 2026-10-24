[README.md](https://github.com/user-attachments/files/22319647/README.md)

# RIF — Resonant Inference Field (Bentov‑2.0)

[Albert Tan Sin Hon's website](https://www.alberttansinhon.com/)

**A research toolkit to operationalize the Resonant Inference Field hypothesis**: conscious access emerges when nested visceral pacers (heart, breath, stomach) phase‑align with eigenmodes of the cortical connectome, enabling a low‑energy, metastable global broadcast.

> Scientific, unemotional, falsifiable. No mysticism. Just signals, modes, and tests.

## TL;DR
- Compute **RIF‑coherence** (phase bundling) across viscera and cortical modes.
- Derive **connectome harmonics** (graph Laplacian eigenmodes) from structural connectivity.
- Run example simulations; extend to EEG/MEG/iEEG + ECG/RESP/EGG.
- Test predictions: PCI ↑, detection thresholds ↓ when RIF‑coherence ↑.

## Quickstart
```bash
# Clone your repo after creating it on GitHub, then:
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -U pip
pip install -e .[dev,analysis]
pytest -q
python examples/01_simulate_and_compute_rif.py
```

## Project Layout
```
rif-project/
  src/rif/               # Core library
  tests/                 # Pytest unit tests
  examples/              # Minimal runnable demos
  docs/                  # User & theory docs (MkDocs-ready)
  ethics/                # Data governance & IRB templates
  .github/workflows/     # CI (lint + tests)
  data/                  # (Empty) Use BIDS/EEG-BIDS; keep out of git
  notebooks/             # (Optional) Analysis notebooks
```

## Install (editable) with extras
- `analysis` → mne, matplotlib (optional heavy deps)
- `dev` → pytest, black, flake8, isort, mypy
- `docs` → mkdocs, mkdocs-material

## Minimal API
```python
from rif.rif import rif_coherence, ignition_probability
from rif.signal import bandpass_phase
from rif.harmonics import connectome_harmonics

# phases: shape (n_oscillators, n_time)
coh = rif_coherence(phases)
p_ign = ignition_probability(coh, beta=12.0, threshold=0.55)

# graph Laplacian eigenmodes
evals, evecs = connectome_harmonics(A, k=32)
```

## Datasets & Standards
- Use **BIDS / EEG‑BIDS** (anatomy, EEG/MEG/iEEG). Keep **PHI out of the repo**.
- Store raw data with Datalad/OSF/Zenodo. Track only *pointers* in git.

## Roadmap (high-level)
- **M0**: Core math + toy simulations (this repo).
- **M1**: Offline analysis pipeline for existing EEG/MEG + ECG/RESP/EGG.
- **M2**: Real‑time closed loop (LSL) for breath/heartbeat‑locked stimulation.
- **M3**: Hardware triggers (TMS, taVNS) + PCI (TMS‑EEG) endpoints.

## How to publish this on GitHub
1. Click **New repository** on GitHub. Name it `rif` or `rif-project`.
2. Locally:
   ```bash
   git init
   git add .
   git commit -m "chore: bootstrap RIF skeleton"
   git branch -M main
   git remote add origin https://github.com/<YOUR-ORG>/rif-project.git
   git push -u origin main
   ```
3. Enable **Actions**; CI runs on PRs and main.

## License
Apache‑2.0 (with patent grant). See `LICENSE`.

## Citation
See `CITATION.cff` and cite the concept as:
> Tan, A. & Contributors (2025). RIF — Resonant Inference Field (Bentov‑2.0). v0.1.0.

---

### Disclaimer
This is research code. **Not a medical device.** For human studies, obtain IRB/ethics approval and comply with data protection laws.
