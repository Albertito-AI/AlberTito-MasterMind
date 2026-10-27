from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def _graph_laplacian(A: ArrayLike, normalized: bool = True) -> np.ndarray:
    A = np.asarray(A, dtype=float)
    d = np.sum(A, axis=1)
    laplacian = np.diag(d) - A
    if normalized:
        with np.errstate(divide="ignore"):
            inverse_sqrt_degree = 1.0 / np.sqrt(d + 1e-12)
        scaling = np.diag(inverse_sqrt_degree)
        laplacian = scaling @ laplacian @ scaling
    return laplacian


def connectome_harmonics(
    A: ArrayLike, k: int | None = None, normalized: bool = True
) -> tuple[np.ndarray, np.ndarray]:
    """Compute Laplacian eigenvalues and eigenvectors.

    Parameters
    ----------
    A:
        Adjacency or structural-connectivity matrix with shape ``(n, n)``.
    k:
        Number of lowest-frequency modes to return. ``None`` returns all modes.
    normalized:
        Whether to use the normalized graph Laplacian.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Eigenvalues with shape ``(k,)`` and eigenvectors with shape ``(n, k)``
        when ``k`` is supplied, otherwise all sorted eigenpairs.
    """
    laplacian = _graph_laplacian(A, normalized=normalized)
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    indices = np.argsort(eigenvalues)
    if k is not None:
        indices = indices[:k]
    return eigenvalues[indices], eigenvectors[:, indices]
