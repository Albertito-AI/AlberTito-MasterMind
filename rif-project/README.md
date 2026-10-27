# RIF: Resonant Inference Field

This directory contains the installable RIF research package. The repository-level [README](../README.md) explains the project, its research limits and the public/private boundary.

## Install and test

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e '.[dev,analysis]'
pytest -q
python examples/01_simulate_and_compute_rif.py
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## API sketch

```python
from rif.rif import rif_coherence, ignition_probability
from rif.signal import bandpass_phase
from rif.harmonics import connectome_harmonics
```

The package supplies computational research utilities and synthetic demonstrations. It does not verify source-data provenance, prove the RIF hypothesis, provide a diagnosis or constitute a medical device.

## Data rule

Do not commit human-subject data, protected health information, participant identifiers, consent records, private ethics material, credentials or unpublished partner data. Use approved external storage and retain only non-sensitive pointers where permitted. See [the repository boundary](../PUBLIC_PRIVATE_BOUNDARY.md).

## Licence

Original project code is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
