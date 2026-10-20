# Reproduce the published one-dimensional field update

**Source:** [How Memory Fields Fix AI Forgetting](https://doi.org/10.5281/zenodo.18010911), §4.1 and Appendix A. This is a deterministic toy simulation of a proposed memory-density variable μ; its numbers are model output, not a measurement of a physical field.

The PDF prints the continuous ansatz `∂μ/∂t = D∇²μ − λ(μ − μ₀) + S(x,t)` and a saturated source `S = A(x)(1 − μ/μ_max)`. Its exact explicit update is:

```text
lap_i = (mu_(i-1) - 2*mu_i + mu_(i+1)) / dx^2
A_i = 0.25*exp(-x_i^2/(2*0.8^2))
S_i = A_i*(1 - mu_i/2.0)
mu_i <- clip(mu_i + dt*(0.05*lap_i - 0.15*(mu_i - 0.10) + S_i), 0, 2.0)
dt = 0.45*dx^2/(2*0.05)
```

The PDF uses `np.roll` for both neighbors, so the grid has **periodic boundary wrapping**. Its grid is `x = linspace(-10,10,400)`, starts at `0.10 + 1.2 exp(-x²/(2·0.9²))`, and runs 400 steps. The source is constant in time despite its “attention pulse” name. The update reads an entire old array before each step and then clips.

Run the [standalone transcription](./reproduce_reaction_diffusion.py) with `python -m pip install numpy` and `python artifacts/reproduce_reaction_diffusion.py` from the profile repository root. A local run with Python 3.12.14 and NumPy 2.3.5 printed `mean=0.2154056632`, `variance=0.0566952393`, and `integrated_mass=4.3189105397` (sum times `dx`). Floating-point details may change the final digits.

The [live Remembrance Field](https://aruintelligence.github.io/aru-remembrance-field/) has a separate stochastic **72 × 72 visual** update in [`index.html`, `SIM.step`](https://github.com/aruintelligence/aru-remembrance-field/blob/main/index.html#L1328-L1353): it replaces each cell with four-neighbor average times `(0.87 + 0.12·coherence)` plus `Math.random()` noise, in place as it scans. Its plasma layer uses `0.88·old + |grid|·(1.25 + 0.55·coherence)`, with occasional random impulses. This browser animation is not a replay of the one-dimensional PDF update.
