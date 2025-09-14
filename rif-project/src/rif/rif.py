
import numpy as np

def rif_coherence(phases: np.ndarray, weights: np.ndarray | None = None, axis: int = 0) -> np.ndarray:
    """Compute RIF‑coherence (vector strength of phases).
    Parameters
    ----------
    phases : array, radians
        Shape (..., n_oscillators, ...). By default, we reduce along `axis`.
    weights : array or None
        Optional non‑negative weights broadcastable to `phases` without `axis`.
    axis : int
        Axis along which to average oscillators (default 0). If phases.shape[axis] == n_osc.
    Returns
    -------
    coherence : array
        Magnitude of the circular mean ∈ [0, 1].
    """
    phases = np.asarray(phases)
    z = np.exp(1j * phases)
    if weights is not None:
        w = np.asarray(weights)
        # Move axis to front for consistent broadcasting
        z = np.moveaxis(z, axis, 0)
        if w.ndim == 1 and w.shape[0] == z.shape[0]:
            w = w[:, None]
        z = z * w
        num = np.sum(z, axis=0)
        den = np.sum(w, axis=0)
        coh = np.abs(num) / np.maximum(den, 1e-12)
        return coh
    else:
        # Unweighted vector strength
        z = np.moveaxis(z, axis, 0)
        num = np.sum(z, axis=0)
        den = z.shape[0]
        return np.abs(num) / den


def ignition_probability(coherence: np.ndarray, beta: float = 10.0, threshold: float = 0.5) -> np.ndarray:
    """Map coherence ∈ [0,1] to an 'ignition probability' via logistic link.
    p = 1 / (1 + exp(-beta * (coherence - threshold)))
    """
    x = beta * (np.asarray(coherence) - threshold)
    return 1.0 / (1.0 + np.exp(-x))
