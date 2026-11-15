<!-- atlas-whitepaper:managed:v1 -->

# Resonant Inference Field: an ambitious hypothesis that must remain defeasible

Prepared for Albert Tan Sin Hon with AI assistance. Foundational paper: 2 November 2026. Documentation revision: 15 November 2026. This is a research design synthesis with a static implementation audit, not a new empirical result or independent peer review.

## Abstract

The Resonant Inference Field (RIF) project asks whether nested bodily rhythms and cortical connectome modes exhibit phase relationships associated with conscious access. The present repository supplies toy numerical utilities, synthetic demonstrations and research-governance templates. It supplies no participant evidence for that hypothesis. This paper separates mathematical definitions, implementation behaviour, statistical association and causal explanation; derives limiting examples; identifies a weighted-input defect in the inspected code; and proposes an evaluation that can reject the hypothesis. The intended contribution is a transparent research programme whose negative results are as informative as positive ones. No clinical conclusion, consciousness detector or intervention recommendation follows from the current software.

## Research question and conceptual commitments

The founding question concerns relationships between visceral rhythms and cortical modes, not whether any oscillation can be plotted attractively. **A phase** is an angular representation obtained under a specified signal-processing model. **Coherence**, as used by the current RIF function, is the magnitude of a circular average over supplied phases. **Conscious access** would require a separately defined, observable experimental outcome; it is not a variable measured by the current library.

Four propositions must be distinguished. A quantity may be computable. It may covary with a behavioural outcome. It may add predictive information beyond simpler explanations. Finally, it may form part of a causal mechanism. Evidence for the first proposition cannot establish the other three. The scientifically valuable outcome could be a supported association, a narrower hypothesis or a well-supported rejection.

The fixed implementation baseline is [215e12593b2b15b57fbfc164b944162ffb04d434](https://github.com/Albertito-AI/AlberTito-MasterMind/tree/215e12593b2b15b57fbfc164b944162ffb04d434). The [README](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/README.md) calls it an early research prototype. Its original code remains Apache-2.0; dependencies and datasets have separate terms. Human-subject records, identifiers, consent material and protected partner data remain outside the public repository.

## Quantities, assumptions and implementation limits

For non-negative finite weights with a strictly positive sum, the intended circular coherence is

$$
R(\phi,w)=\frac{\left|\sum_{j=1}^{n}w_j e^{i\phi_j}\right|}{\sum_{j=1}^{n}w_j}.
$$

Here $j$ indexes the oscillators being reduced, phases are in radians, and all quantities must describe the same defined observation. The triangle inequality gives $0\leq R\leq1$ under those assumptions. This bound does not establish valid phase extraction, meaningful biological coupling or consciousness.

The [implementation](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/src/rif/rif.py#L27-L41) requires a specific caution. Static inspection identifies a defect for one-dimensional phases with matching one-dimensional weights. For phases $[0,\pi]$, phasors have shape $(2,)$. Weights $[1,1]$ are expanded to $(2,1)$. Their product broadcasts to $(2,2)$; reduction along axis zero then yields a two-element result with magnitudes approximately $[1,1]$, instead of the intended scalar approximately zero. This is a derivation from the source, not a newly executed test. The current [tests](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/tests/test_rif.py) do not cover this weighted case. The mathematical definition above must not be mistaken for a claim that all supported-looking inputs implement it correctly.

The unweighted path computes an ordinary circular mean over the selected axis. Empty inputs, non-finite values, negative or zero-total weights, dimensional contracts and axis selection need explicit validation and regression coverage before research use. A correction to the weighted implementation is separate work from this documentation revision.

The function named `ignition_probability` applies

$$
s(R)=\frac{1}{1+\exp[-\beta(R-\theta)]}.
$$

Without an independently labelled outcome, fitted parameters, calibration assessment and held-out evaluation, $s$ is a logistic score. Its name does not make it a probability of conscious access. The [graph module](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/src/rif/harmonics.py) constructs a Laplacian eigensystem, while the [signal module](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/src/rif/signal.py) uses filtering and an analytic-signal phase. The repository does not supply comprehensive input-domain checks or a validated multimodal acquisition pipeline. Graph symmetry, connectivity, edge weights, signal sampling, filter edges and missing-data policy must be specified.

## Worked example and counterexamples

Take four equal, unweighted phase angles. For $[0,0,0,0]$, the phasors sum to four and $R=1$. For $[0,\pi/2,\pi,3\pi/2]$, they cancel and $R=0$, apart from numerical rounding. At $R=\theta$, the logistic score is $1/2$, for any finite $\beta$. These are mathematical checks, not biological findings.

The repository's separate eight-angle [synthetic demonstration](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/docs/demo/README.md) records coherence 1.000000 for alignment, 0.547661 for its specified half-circle arrangement and approximately zero for evenly spaced phases. With $\beta=12$, $\theta=0.55$, its recorded scores are 0.995504, 0.492983 and 0.001359. These are prior documented software outputs; this revision did not rerun them.

Two counterexamples constrain interpretation. First, duplicate a single synthetic oscillator across every channel. Their coherence can equal one without independent interacting processes or conscious access. A common clock, reference or source can similarly produce apparent alignment. Second, two perfectly phase-locked oscillators with a constant opposition of $\pi$ have zero instantaneous circular mean across the pair. Thus a small RIF value need not mean an absence of stable phase relationship. The present across-oscillator statistic is not interchangeable with a statistic that averages pairwise phase differences over time or trials.

## Evidence and reproduction

| Proposition | Evidence available | Boundary |
| --- | --- | --- |
| The unweighted toy function has aligned/opposed checks | [Numerical tests](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/tests/test_rif.py) | Narrow examples, not full domain validation |
| Harmonic outputs have basic shape coverage | [Harmonic test](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/tests/test_harmonics.py) | Not a validated connectome construction |
| A synthetic demo has recorded inputs, outputs and source hashes | [Demo record](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/docs/demo/README.md) | No participant or consciousness evidence |
| Weighted 1D broadcasting is inconsistent with the formula | [Source lines 27–41](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/rif-project/src/rif/rif.py#L27-L41), derivation above | Static finding; no execution in this audit |
| RIF predicts conscious access or explains its mechanism | No study result supplied by this repository | Research question only |

For a deliberate reproduction, inspect the fixed [quickstart](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/215e12593b2b15b57fbfc164b944162ffb04d434/README.md). In a checkout of the baseline, using Python 3.10 or later and an isolated environment:

~~~sh
cd rif-project
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev,analysis]'
pytest -q
cd ..
python scripts/readme_demo.py
~~~

The activation command is for a POSIX shell. Installation can retrieve dependencies. Record the commit, Python/NumPy/SciPy versions, resolved dependencies, command output and platform; compare with the prior demo's recorded environment rather than assuming numerical identity across versions. No repository code was executed for this documentation audit.

A useful first engineering gate is a dimension-aware contract with tests for scalar and multidimensional reductions, weight scaling, phase rotation, permutation, opposed phases and invalid data. Such tests would assess the numerical contract, not the biological hypothesis. Their absence must not be filled by inventing experimental evidence.

## Related work and precise relationship to RIF

Lachaux, Rodriguez, Martinerie and Varela, [“Measuring phase synchrony in brain signals”](https://pmc.ncbi.nlm.nih.gov/articles/PMC6873296/), *Human Brain Mapping* 8(4), 194–208 (1999), developed phase-locking statistics and used surrogate comparisons. Their discussion of volume conduction is relevant to common-source controls. Their measure and experimental setting are not identical to RIF's instantaneous circular mean; citing that work does not validate this implementation.

Atasoy, Donnelly and Pearson, [“Human brain networks function in connectome-specific harmonic waves”](https://pmc.ncbi.nlm.nih.gov/articles/PMC4735826/), *Nature Communications* 7, 10340 (2016), DOI [10.1038/ncomms10340](https://doi.org/10.1038/ncomms10340), introduced a connectome-harmonic representation and examined its relationship with resting-state networks. It provides a concrete antecedent for graph-based modes. It does not establish the RIF proposition about nested visceral rhythms, validate this toy graph code or supply missing participant evidence.

## Proposed discriminating study and limits

Before collecting data, define the conscious-access task and outcome independently of the candidate coherence statistic. Specify acquisition channels, sampling and synchronisation, phase extraction, time windows, exclusions and treatment of artefacts. Select outcomes and analysis windows before examining associations. Determine sample size from a justified design and sensitivity or power analysis, not a convenient recording total.

A proposed comparison would evaluate whether preregistered RIF features add held-out predictive information beyond behavioural variables, signal amplitude and simple phase-based baselines. Separate participants between development and evaluation where repeated observations otherwise permit leakage. Report discrimination and, if probabilities are claimed, calibration with uncertainty. Do not tune the logistic threshold on the evaluation set.

Use surrogate or time-shift controls chosen to preserve relevant signal properties while disrupting the particular relationship being tested. Examine common drivers, reference choice, motion, preprocessing alternatives and temporal leakage. A surrogate that destroys every property of the signal can create an artificially easy comparison. Specify what null result, instability across defensible preprocessing choices or absence of incremental predictive value would lead to narrowing or retiring the hypothesis. Association alone would still not establish causality.

Research involving people needs an appropriately reviewed protocol and lawful data governance. Existing templates are not evidence of approval. Real-time or stimulation-related ambitions are not present capabilities or permission to intervene. Independent replication, a public record of failed predictions and privacy-preserving reproducibility packages are later gates.

For teaching, derive the two phase examples by hand; trace the weighted broadcasting defect on paper; explain why duplicate channels can give high coherence; and propose a control that distinguishes common input from the relationship of interest. Ask students to state exactly what each successful numerical check would leave unknown. The project's value lies in making such distinctions and inviting tests that could show it is wrong.

