import numpy as np

from rif.harmonics import connectome_harmonics


def test_harmonics_shapes():
    adjacency = np.array(
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
        dtype=float,
    )
    eigenvalues, eigenvectors = connectome_harmonics(adjacency, k=2)
    assert eigenvalues.shape == (2,)
    assert eigenvectors.shape == (3, 2)
