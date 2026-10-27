from __future__ import annotations

import numpy as np
from scipy.signal import butter, filtfilt, hilbert


def bandpass_phase(
    x: np.ndarray,
    fs: float,
    f_lo: float,
    f_hi: float,
    order: int = 4,
) -> tuple[np.ndarray, np.ndarray]:
    """Band-pass a signal and compute its Hilbert phase.

    Parameters
    ----------
    x:
        One-dimensional time series or two-dimensional ``(signals, time)``
        array.
    fs:
        Sampling rate in hertz.
    f_lo, f_hi:
        Lower and upper band edges in hertz.
    order:
        Butterworth filter order.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Phase in radians and the filtered signal.
    """
    signal_array = np.asarray(x)
    nyquist = fs * 0.5
    normalized_band = [f_lo / nyquist, f_hi / nyquist]
    numerator, denominator = butter(order, normalized_band, btype="bandpass")

    if signal_array.ndim == 1:
        filtered = filtfilt(numerator, denominator, signal_array, axis=0)
        phase = np.angle(hilbert(filtered))
    else:
        filtered = filtfilt(numerator, denominator, signal_array, axis=-1)
        phase = np.angle(hilbert(filtered, axis=-1))
    return phase, filtered
