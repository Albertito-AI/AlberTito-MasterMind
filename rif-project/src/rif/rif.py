import numpy as np


def rif_coherence(
    phases: np.ndarray,
    weights: np.ndarray | None = None,
    axis: int = 0,
) -> np.ndarray:
    """Compute RIF coherence as the vector strength of phases.

    Parameters
    ----------
    phases:
        Phase values in radians. The function reduces the selected oscillator
        axis.
    weights:
        Optional non-negative weights broadcastable to the moved phase array.
    axis:
        Axis along which oscillators are averaged.

    Returns
    -------
    np.ndarray
        Magnitude of the circular mean, bounded between zero and one for
        non-negative weights.
    """
    phase_array = np.asarray(phases)
    phasors = np.exp(1j * phase_array)
    phasors = np.moveaxis(phasors, axis, 0)

    if weights is None:
        numerator = np.sum(phasors, axis=0)
        return np.abs(numerator) / phasors.shape[0]

    weight_array = np.asarray(weights)
    if weight_array.ndim == 1 and weight_array.shape[0] == phasors.shape[0]:
        weight_array = weight_array[:, None]
    weighted_phasors = phasors * weight_array
    numerator = np.sum(weighted_phasors, axis=0)
    denominator = np.sum(weight_array, axis=0)
    return np.abs(numerator) / np.maximum(denominator, 1e-12)


def ignition_probability(
    coherence: np.ndarray,
    beta: float = 10.0,
    threshold: float = 0.5,
) -> np.ndarray:
    """Map coherence values to a proposed ignition probability.

    The mapping uses ``1 / (1 + exp(-beta * (coherence - threshold)))``.
    """
    scaled = beta * (np.asarray(coherence) - threshold)
    return 1.0 / (1.0 + np.exp(-scaled))
