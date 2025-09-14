
import numpy as np
from rif.harmonics import connectome_harmonics

def test_harmonics_shapes():
    A = np.array([[0,1,0],[1,0,1],[0,1,0]], dtype=float)
    evals, evecs = connectome_harmonics(A, k=2)
    assert evals.shape == (2,)
    assert evecs.shape == (3,2)
