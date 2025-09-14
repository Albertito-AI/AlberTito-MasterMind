"""RIF (Resonant Inference Field) core package."""
from .rif import rif_coherence, ignition_probability
from .harmonics import connectome_harmonics
__all__ = ["rif_coherence", "ignition_probability", "connectome_harmonics", "bandpass_phase"]

# Lazy import to keep base import light if SciPy is unavailable.
try:
    from .signal import bandpass_phase as bandpass_phase  # noqa: F401
except Exception as _e:
    _IMPORT_ERROR = _e
    def bandpass_phase(*args, **kwargs):  # type: ignore[misc]
        raise ImportError(
            "bandpass_phase requires SciPy. Install rif[analysis] and try again."
        ) from _IMPORT_ERROR
