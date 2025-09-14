
from __future__ import annotations
import numpy as np
from numpy.typing import ArrayLike

def _graph_laplacian(A: ArrayLike, normalized: bool = True) -> np.ndarray:
    A = np.asarray(A, dtype=float)
    d = np.sum(A, axis=1)
    L = np.diag(d) - A
    if normalized:
        with np.errstate(divide="ignore"):
            invsqrt = 1.0 / np.sqrt(d + 1e-12)
        Dm12 = np.diag(invsqrt)
        L = Dm12 @ L @ Dm12
    return L

def connectome_harmonics(A: ArrayLike, k: int | None = None, normalized: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """Compute Laplacian eigenvalues/vectors (connectome harmonics).
    Parameters
    ----------
    A : adjacency/structural connectivity (n x n)
    k : number of lowest‑frequency modes to return; None → all
    normalized : use normalized Laplacian
    Returns
    -------
    evals, evecs : (k,), (n,k)
    """
    L = _graph_laplacian(A, normalized=normalized)
    # eigh for symmetric matrices
    evals, evecs = np.linalg.eigh(L)
    if k is not None:
        idx = np.argsort(evals)[:k]
        return evals[idx], evecs[:, idx]
    return np.sort(evals), evecs[:, np.argsort(evals)]
