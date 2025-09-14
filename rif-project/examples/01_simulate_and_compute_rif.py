
import numpy as np
from rif.rif import rif_coherence, ignition_probability

rng = np.random.default_rng(42)
n_osc, n_time = 8, 5000
# Simulate oscillator phases as biased random walks
phases = np.cumsum(0.02 * rng.standard_normal((n_osc, n_time)), axis=1)
# Inject a global phase‑locking window (time 2000..2800)
lock_idx = slice(2000, 2800)
phases[:, lock_idx] += np.linspace(0, np.pi/2, lock_idx.stop - lock_idx.start)

coh = rif_coherence(phases, axis=0)
p_ign = ignition_probability(coh, beta=12.0, threshold=0.55)

print(f"Coherence stats → min={coh.min():.3f}, max={coh.max():.3f}, mean={coh.mean():.3f}")
print(f"Ignition probability → min={p_ign.min():.3f}, max={p_ign.max():.3f}")
