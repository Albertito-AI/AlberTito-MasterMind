<!-- atlas-whitepaper:managed:v1 -->

# Resonant Inference Field: an ambitious hypothesis that must remain defeasible

## The research question

The Resonant Inference Field project asks whether nested bodily rhythms and cortical connectome modes exhibit measurable phase relationships associated with conscious access. Its strongest possible contribution would be a reproducible, discriminating research programme. That contribution could be a supported relationship, a narrower reformulation or a convincing negative result. A theory becomes scientifically useful by exposing itself to failure, not by acquiring increasingly elaborate illustrations.

This AI-assisted design whitepaper was prepared for Albert Tan Sin Hon on 2 November 2026. It explains the public computational prototype and proposes a research direction. It supplies no biological finding, clinical conclusion, medical recommendation or evidence of a consciousness detector. The repository's historical name is AlberTito-MasterMind; its documented research identity is RIF.

## First principles: distinguish quantity, hypothesis and explanation

A measurable quantity is not a theory. A theory is not a validated predictor. A predictor is not automatically a causal explanation. RIF must keep these levels separate.

The implemented coherence quantity is circular vector strength. For supplied phases and suitable non-negative weights, its intended form is

\[
R=\frac{\left|\sum_j w_j e^{i\phi_j}\right|}{\sum_j w_j}.
\]

Aligned phases give a high value; phases distributed around the circle can cancel. This is a mathematical property of the representation. It does not show that any particular biological signals are meaningfully coupled or that a high value implies consciousness. Input validity, weighting and the treatment of degenerate data are part of the computational contract and need explicit tests.

The code also applies a logistic transform to coherence. Naming its output `ignition_probability` does not make it a calibrated probability. Calibration would require an operational outcome definition, data independent from parameter choice and comparison with observed frequencies. Until then it is a proposed numerical mapping.

## Fundamental logic of the computational model

The public library supplies phase-processing utilities, coherence calculations and graph-Laplacian eigenmodes of a supplied connectivity matrix. The latter provide mathematical basis functions determined by that matrix and the chosen normalisation. Choosing a basis does not establish that a brain uses it in the way a hypothesis suggests.

A credible chain of inference must therefore expose each bridge: recorded signal to preprocessing; preprocessing to phase estimate; phase estimate to coherence; connectivity assumptions to modes; and these quantities to a predeclared outcome. Filters, reference choices, artefacts, missing segments and analysis windows can affect the result. They belong in the method, not in an invisible preparatory step.

The existing demonstration uses synthetic phase arrangements. Its value is computational transparency: a reader can reproduce the calculation and test expected limiting cases. It supplies no participant evidence. The public/private boundary appropriately keeps participant data, consent records and protected research material outside the repository.

## What a decisive experiment would need to distinguish

An observed association could reflect the proposed mechanism, a common driver, task structure, preprocessing choices or another confound. The research programme should make these alternatives compete. A useful protocol would predefine the outcome, analysis windows, exclusions, baseline models and a smallest effect considered informative before examining results.

Negative controls should test whether apparent coherence persists when alignment is disrupted in ways that preserve relevant signal properties. Sensitivity analyses should vary justified preprocessing choices. Participant-level separation matters where repeated observations could otherwise leak information between fitting and evaluation. These are proposed design requirements, not completed experiments.

The hypothesis should earn complexity. If a simpler model predicts the chosen outcome as well, or if the claimed relationship disappears under reasonable controls, that should narrow the theory. A research programme that can reinterpret every possible result as confirmation has abandoned its central purpose.

## Aim and hope: a public discipline of inquiry

The immediate aim is an inspectable computational reference that others can criticise and reproduce. The larger hope is to improve understanding of the relationship between bodily dynamics, neural organisation and experience without confusing speculation with established knowledge.

Social benefit could come from better methods even if the original hypothesis fails. Open test fixtures, transparent analysis choices and reusable negative controls can help other researchers avoid errors. Clear public explanations can demonstrate how to investigate a profound question without selling certainty.

The corresponding responsibility is restraint. Unsupported claims about consciousness could be misused to assess people, justify interventions or imply clinical benefits. The project should not offer individual classifications or stimulation advice from toy simulations. Human research and any intervention require a separately reviewed protocol, appropriate expertise, ethics and data governance.

## Ideal progression and research wishlist

| Stage | Scientific purpose | Evidence gate |
| --- | --- | --- |
| Mathematical reference | Make definitions and assumptions executable | Numerical edge cases, shape/weight validation and independent implementations |
| Offline analysis pipeline | Bind preprocessing and outcomes to reproducible inputs | Permitted data, provenance, documented exclusions and complete run manifests |
| Discriminating study | Compare the hypothesis with serious alternatives | Predeclared analysis, controls, uncertainty and held-out evaluation |
| Independent replication | Test transport beyond the originating team | New investigators, appropriate data and preserved negative findings |
| Mechanistic investigation | Examine justified causal questions | Separate safety, ethics, design and domain-review approval |

The existing roadmap mentions multimodal pipelines and later real-time or stimulation-related research. Those are ambitions, not implementation or permission. The ideal wishlist includes stable data contracts, preregistered analyses, openly shareable synthetic benchmarks, privacy-preserving reproducibility packages, cross-laboratory replication and a public record of failed predictions. It should also include explicit retirement criteria for hypotheses that do not survive testing.

## What success would look like

Success is not a dramatic coherence plot. It is a result whose interpretation survives alternative explanations, transparent analysis and independent scrutiny. Report effect uncertainty, calibration where relevant, sensitivity, computational cost and exclusions. Avoid selecting favourable conditions after the fact or hiding null results behind a broad narrative.

A best-case RIF project would make intellectual ambition compatible with evidential humility. It would contribute methods and knowledge that remain useful even when a favoured explanation changes. That is how a speculative starting point can become a public research asset.

## Inspected foundation

Baseline: [`a358f62259714414fc9c76a3699beca9c747a2ff`](https://github.com/Albertito-AI/AlberTito-MasterMind/tree/a358f62259714414fc9c76a3699beca9c747a2ff). See [README](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/a358f62259714414fc9c76a3699beca9c747a2ff/README.md), [coherence implementation](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/a358f62259714414fc9c76a3699beca9c747a2ff/rif-project/src/rif/rif.py), [harmonics implementation](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/a358f62259714414fc9c76a3699beca9c747a2ff/rif-project/src/rif/harmonics.py) and [roadmap](https://github.com/Albertito-AI/AlberTito-MasterMind/blob/a358f62259714414fc9c76a3699beca9c747a2ff/rif-project/ROADMAP.md). The original code's Apache-2.0 licence does not grant rights over third-party datasets or participant records. No new scientific result is asserted here.
