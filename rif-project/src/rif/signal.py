
from __future__ import annotations
import numpy as np
from scipy.signal import butter, filtfilt, hilbert

def bandpass_phase(x: np.ndarray, fs: float, f_lo: float, f_hi: float, order: int = 4) -> tuple[np.ndarray, np.ndarray]:
    """Bandpass filter then compute Hilbert phase.
    Parameters
    ----------
    x : array (time,) or (n_signals, time)
    fs : sampling rate (Hz)
    f_lo, f_hi : band edges (Hz)
    order : Butterworth order
    Returns
    -------
    phase : array, radians
    x_filt : array, band‑passed signal
    """
    x = np.asarray(x)
    nyq = fs * 0.5
    wn = [f_lo / nyq, f_hi / nyq]
    b, a = butter(order, wn, btype="bandpass")
    if x.ndim == 1:
        xf = filtfilt(b, a, x, axis=0)
        phase = np.angle(hilbert(xf))
    else:
        xf = filtfilt(b, a, x, axis=-1)
        phase = np.angle(hilbert(xf, axis=-1))
    return phase, xf
