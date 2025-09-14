
import numpy as np
from rif.rif import rif_coherence, ignition_probability

def test_coherence_all_aligned():
    phases = np.zeros((5, 100))
    c = rif_coherence(phases, axis=0)
    assert np.allclose(c, 1.0)

def test_coherence_opposed():
    # Two oscillators 0 and pi cancel → 0
    phases = np.vstack([np.zeros(100), np.pi * np.ones(100)])
    c = rif_coherence(phases, axis=0)
    assert np.allclose(c, 0.0)

def test_ignition_logistic_monotonic():
    x = np.linspace(0, 1, 101)
    p = ignition_probability(x, beta=10.0, threshold=0.5)
    assert np.all(np.diff(p) > 0)
