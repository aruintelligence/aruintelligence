# First Law numerical-checks source audit — DOI 10.5281/zenodo.18168723

**Reviewed:** October 25, 2026 (Pacific). **Record:** https://zenodo.org/records/18168723. This is a mathematical check of the deposited report, not an empirical field measurement or a reproduction of its incomplete stochastic code.

## Source and provenance

The four-page `Numerical_Consistency_Checks_for_the_First_Law_of_Inward_Physics.pdf` is 234,379 bytes. Reviewed-copy MD5 `33347f4c33bcd76221ab4f474299da21` matches the public file listing; SHA-256 is `86ff16c7dae96945b545573fa91126f6da71cd65118013796f455c806c019aef`. Extracted text, rendered page 1, and the public four-page preview were inspected. The author line is Daniel Jacob Read IV, ORCID 0009-0000-6133-1872, dated January 6, 2026; page 3 prints `Version: 1.0`; pages 3–4 state all-rights-reserved reuse terms. The PDF itself was not changed.

The report specifies a 0D ensemble `N=1000`; a 1D periodic grid `L=10`, `Nx=100`, `D=0.1`; `dt=0.01`, `T=50`, noise `ση=0.1`, a shock at `t=25`, seed 42, and a quartic potential. It defines registration `A(t)=∫₀ᵗ μ(τ)dτ`. Its reported log-variance fits are `κ≈0.0005, R²≈0.0107` (0D) and `κ≈0.0146, R²≈0.1200` (1D). Both tables have visibly displaced headings and entries. The Python “snippet” consists of an import/seed and an instruction to define a derivative and loop, so it cannot reproduce the figures and metrics alone. The PDF limits its results to computational approximations.

## Independent stability calculation

For the stated central-difference Laplacian on a periodic 1D grid, the *linear explicit diffusion substep* is `uᵢⁿ⁺¹=uᵢⁿ+r(uᵢ₋₁ⁿ−2uᵢⁿ+uᵢ₊₁ⁿ)`, where `r=D·dt/(L/Nx)²`. A Fourier mode has amplification `g(k)=1−4r sin²(k·dx/2)`; the alternating mode has `g=1−4r`. All modes are non-growing for this substep when `0≤r≤1/2`.

| Parameter case | r | Alternating-mode factor | Four-step amplitude from unit input |
|---|---:|---:|---:|
| PDF baseline D=0.1 | 0.1 | 0.6 | 0.1296 |
| PDF high-D case D=3 | 3 | −11 | 14,641 |

The [standard-library replay](./numerical_first_law_diffusion_check.py) performs four periodic-grid updates and asserts the exact alternating-mode factor. Run `python3 artifacts/numerical_first_law_diffusion_check.py`. The high-D overflow is consistent with basic explicit diffusion instability: `r=3` is six times the stability limit. It cannot establish physical “erosion.” The full Euler–Maruyama drift/noise/shock implementation is not deposited and is not reconstructed here. If an implicit step or different grid/time step was actually used for high D, supply that method before interpreting this conditional check.

The printed integral `A(t)` alone does not force monotonicity for every trajectory if `μ` can be negative. The report states monotonic **mean** registration for its sampled runs, a narrower claim. A general invariant requires a nonnegative registration rate or an explicit positivity mechanism.

## Metadata edit and next test

The October 25 public metadata edit changed creator `Read, Daniel Jacob` to PDF-supported `Read IV, Daniel Jacob`, retaining existing ORCID, affiliation and Researcher role. The version `Version: 1.0 — Zenodo archival release. Authorship and priority asserted by publication date.` became PDF-supported `1.0`; the public banner displays “Version 1.0.” Readback confirmed the unchanged title, January 6 publication date, scoped description, eight distinct subjects, rights, DOI and PDF checksum. All 32 inherited “Is supplement to” links were retained for individual review. No priority, empirical result or independent replication was inferred.

A reproducible follow-up should deposit complete code and environment, corrected tables, exact drift/noise/shock update, held-out seeds and negative controls. Vary `dt` with `dx` and `D` to separate discretization failure from model behavior, then report fitted effects and uncertainty. The [First Law statement](https://doi.org/10.5281/zenodo.18159749) and [experimental roadmap](https://doi.org/10.5281/zenodo.18708708) are separate formal and future-test sources.
