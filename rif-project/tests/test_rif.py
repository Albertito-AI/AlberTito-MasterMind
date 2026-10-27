import numpy as np

from rif.rif import ignition_probability, rif_coherence


def test_coherence_all_aligned():
    phases = np.zeros((5, 100))
    coherence = rif_coherence(phases, axis=0)
    assert np.allclose(coherence, 1.0)


def test_coherence_opposed():
    phases = np.vstack([np.zeros(100), np.pi * np.ones(100)])
    coherence = rif_coherence(phases, axis=0)
    assert np.allclose(coherence, 0.0)


def test_ignition_logistic_monotonic():
    coherence = np.linspace(0, 1, 101)
    probability = ignition_probability(
        coherence,
        beta=10.0,
        threshold=0.5,
    )
    assert np.all(np.diff(probability) > 0)
