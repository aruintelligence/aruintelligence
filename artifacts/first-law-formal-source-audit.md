# Formal First Law source audit — DOI 10.5281/zenodo.18159749

**Reviewed:** October 27, 2026 (Pacific). [Public record](https://zenodo.org/records/18159749). This audit checks a source-specific deterministic limit and maps what the three-page report actually discloses. It is not a reproduction of its reported stochastic simulations or an empirical field test.

## Deposited source and record

The three-page `The_First_Law_of_Inward_Physics__The_Law_of_Endogenous_Registration.pdf` is 140,637 bytes. Reviewed-copy MD5 `1327ab5c31663a309523cd2db49d7aa3` matches Zenodo's public listing; SHA-256 `62eb16ecc78b2f3fe28b921fdad8eff65b0af49a96c7e5521e6b75bb9b36129d`. Text was extracted and all three pages rendered. The cover reads Daniel Jacob Read IV, Independent Researcher (self-published), January 5, 2026. Page 3 gives version 1.0 and restrictive copyright.

The PDF defines accumulated registration `A(x,t)=∫₀ᵗ μ(x,τ)dτ` (equation 1), posits `σ²(x,t)=σ₀² exp(−κA(x,t))` (equation 2), and states stochastic reaction–diffusion dynamics `∂tμ=D∇²μ−V'(μ)+η` (equation 3). Equation 4 is `V(μ)=aμ²/2+bμ³/3+cμ⁴/4`. Equation 5 proposes a future-state term; equation 6 writes a cross-scale interaction. The prose reports three simulated regimes and approximately 32% ensemble-variance reduction with the anticipatory term. No executable code, raw trajectories, parameterized full solver, or figure is deposited with this record to reproduce that number. The [separate numerical-checks deposit](https://doi.org/10.5281/zenodo.18168723) has its own [source audit](./first-law-numerical-source-audit.md).

## Exact check of a stated potential choice

The numerical companion supplies `a=1, b=−3, c=1`. In the spatially uniform, noise-free limit with the future-state term absent, equation 3 becomes `dμ/dt=−V'(μ)=−μ+3μ²−μ³`. This is an allowed limiting case of the stated dynamics, not the complete model. The three stationary points solve `μ(μ²−3μ+1)=0`:

| Equilibrium μ | V(μ) | V''(μ) | Local drift behavior |
|---:|---:|---:|---|
| 0 | 0 | 1 | Attracting |
| (3−√5)/2 ≈ 0.381966 | ≈ 0.0225425 | ≈ −0.854102 | Repelling |
| (3+√5)/2 ≈ 2.618034 | ≈ −2.7725425 | ≈ 5.854102 | Attracting |

Because `dV/dt=V'(μ)·dμ/dt=−[V'(μ)]²≤0`, the deterministic homogeneous flow descends the potential. The positive basin threshold and two attracting equilibria are a genuine mathematical feature of this *chosen* quartic. The [standard-library replay](./first_law_potential_check.py) checks these roots and signs, then integrates three initial values for 20 time units with joint RK4 at `dt=0.01`. Starting at 0.1 tends to 0; starting at 1 tends to 2.618034; starting at −0.1 tends to 0 from below, with `A(20)≈−0.08723205`. Run `python3 artifacts/first_law_potential_check.py`. The replay also asserts non-increasing potential at each step. These are numerical examples of the analytic limiting equations, not deposited simulation outputs.

The two basins support a limited multistability statement for these coefficients. The same equations alone do not prove that registration never resets under every bounded perturbation: `dA/dt=μ`, so negative μ makes A decrease. Equation 2 is posited, rather than derived from equation 3. A claim about hysteresis under shocks or 32% variance reduction requires the full noise, shock, boundary, ensemble and anticipatory-term specification and a reproducible comparison. The future-state bracket in equation 5 requires an operational update rule before a no-retrocausality claim can be tested.

## Metadata status and technical next step

On October 27, the public record initially displayed creator `Read, Daniel Jacob` and resource type `Other`. A source-supported metadata edit was then published and read back: creator `Read IV, Daniel Jacob` now matches the deposited cover, retaining the existing ORCID 0009-0000-6133-1872, ĀRU Intelligence Inc. affiliation and Researcher role; resource type is `Publication / Report`, appropriate for this standalone research document. The description now foregrounds equations (1)–(6), the exact two-attractor limiting result tied to the numerical companion, and the distinct evidence needed for the reported stochastic result. Title, January 5, 2026 publication date, version 1.0, eight subjects, restrictive copyright, `Is supplemented by` relation to the numerical companion, and file MD5 were publicly verified unchanged. The PDF was not replaced. The cover says Independent Researcher (self-published), while the existing metadata affiliation remains ĀRU Intelligence Inc.; affiliation provenance can be reviewed separately.

A reviewable next edition should deposit the original complete simulator and environment; specify the future-state update, stochastic forcing and shock protocol; distinguish an imposed exponential variance relation from a derived one; and compare prespecified outcomes across seeds and controls. Define a positivity constraint or nonnegative registration rate if irreversibility is intended as a general invariant. An enterprise reviewer can reproduce the exact potential result immediately while reserving the wider physical claim for the [experimental roadmap](https://doi.org/10.5281/zenodo.18708708).
