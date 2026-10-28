# Three synthetic phase arrangements

This demonstration calls the existing `rif_coherence` and `ignition_probability`
functions. The inputs are mathematical fixtures; no biological, personal or
human-subject data is used.

## Reproduce

From the repository root, in a Python 3.10+ environment:

```bash
python -m pip install ./rif-project
python scripts/readme_demo.py
```

The package depends on NumPy and SciPy. The demo imports the checked-out library
in `rif-project/src` and prints JSON. It makes no provider calls and starts no
service. To regenerate the committed JSON and SVG:

```bash
python scripts/readme_demo.py --write-assets
```

## Input and observed output

| Eight input phases, in radians | Coherence | Logistic output |
| --- | --- | --- |
| All zero | 1.000000 | 0.995504 |
| `linspace(-pi/2, pi/2, 8)` | 0.547661 | 0.492983 |
| `arange(8) * (2*pi/8)` | 0.000000 | 0.001359 |

The coherence is the magnitude of the mean of the unit phasors. The displayed
logistic output uses `beta=12` and `threshold=0.55`. Values are rounded to six
decimal places; floating-point cancellation in the evenly spaced case is
numerically close to zero. Phase angles in the JSON are rounded for display;
the calculation uses the full NumPy-generated values.

- [Actual JSON output](output.json)
- [Data-derived SVG](demo.svg)
- [Demo generator](../../scripts/readme_demo.py)
- [Unchanged numerical implementation](../../rif-project/src/rif/rif.py)

The SVG positions the phase vectors from the input angles and displays the
returned values. Eight aligned vectors overlap. This is a computational example,
not an observation of a body, brain, consciousness transition or clinical state.
The function name `ignition_probability` does not itself establish calibration,
causal meaning or scientific validity.

## Provenance

Observed with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0 on Linux. The source was
read from commit
[`ae51522058ccdfd117f014d10b08e2ad9a389229`](https://github.com/Albertito-AI/AlberTito-MasterMind/commit/ae51522058ccdfd117f014d10b08e2ad9a389229).
The numerical implementation's SHA-256 is
`17104a14a145ab58f9efb68c12b128b076c00ecf7d40caebeb2bdb3679d7fc51`.
The generator records the actual module digest in its output.

The runtime, existing examples, research claims and licence are unchanged by
this documentation demonstration. General performance or scientific validation
cannot be inferred from these three fixtures.
