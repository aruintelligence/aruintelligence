# Inward Fixed-Point Gravity: deposited-source and internal algebra review

**Source:** [Inward Fixed-Point Gravity, DOI 10.5281/zenodo.19723552](https://doi.org/10.5281/zenodo.19723552), Daniel Jacob Read, ĀRU Intelligence Inc. The PDF cover is dated 24 April 2026; Zenodo displays 23 April publication and version field `Version: 1.0`. Reviewed 30 October 2026 Pacific against the five-page deposit (624,208 bytes; MD5 `a01e0baac2a024b3e7c1d9afcc398499`, matching Zenodo; SHA-256 `658062c70092e480977bf2234ca05350db9772f3991bd3d1dec296bcbe360ed5`). Two additional image files are in the record; this audit checks the PDF and its embedded figures, not independent measurements.

## Page map

| PDF page | Deposited contribution |
|---|---|
| 1 | Defines `μ̃≡μ/√(−g)` (equation 1), action (2), Einstein and scalar equations (3–5), and asserts an automatic cosmological tracker and local-gravity compatibility in the abstract. |
| 2 | Static GR limit; conformal matter-coupling/Yukawa expression (6), approximate post-Newtonian bound (7), soft-min experimental envelope (8), FLRW equation and energy density/pressure, reported `w₀≈−0.85`, `wₐ≈−0.21`, and nominal benchmark `m≈10⁻³ eV`, `ℓ≈0.2 mm`, `β²≈10⁻⁶`. It does not print a cosmological solver, initial-condition range, covariance analysis or likelihood. |
| 3 | Figure 1 plots the author’s constructed envelope and benchmark; discussion, conclusion and six references. The graph is an authored model/constraint illustration, not a new experimental dataset. |
| 4 | Figure 2 plots numerical background trajectories and a CPL fit. The visible legend names `IC 1` and `IFG fiducial`; the footer gives `M̃=1.0`, `Ṽ₀=2.869e+00`, `w₀=−0.850`, `wₐ=−0.210`. The PDF does not specify a full parameter table, units, background cosmology, numerical code, scan bounds or fit procedure. |
| 5 | Appendix A states `μ̃` is the fundamental dynamical variable with a canonical kinetic term; `μ=μ̃√(−g)` is a composite object without independent assumed dynamics. |

## Two reproducible internal checks

**FLRW normalization.** Equation (1) says `μ̃=μ/√(−g)`. Section 8 explicitly says `√(−g)=a³` in flat FLRW, then prints `μ̃=μ/a^(3/2)`. Under those two stated premises with unit lapse, equation (1) instead gives `μ̃=μ/a³`. At `a=4`, `μ=1`, these are `1/64` and `1/8` respectively. An intended `a^(3/2)` denominator would correspond to a different definition, such as the square root of the stated volume factor, and needs to be reconciled in the next edition.

**Nominal constraint benchmark.** At `m=10⁻³ eV`, the paper sets `β²_T=10⁻⁶`, `β²_M=3×10⁻⁶`, `β²_C=10⁻⁵`, and `n=6`. Equation (8) gives

`β²_max=10⁻⁶[1+(1/3)⁶+(1/10)⁶]^(−1/6)=9.99771392674×10⁻⁷`.

The displayed `β²≈10⁻⁶` benchmark is **0.022866% above** that strict nominal soft-min value. It is appropriately described as *approximately on the boundary* at the precision printed, rather than a strictly interior point. This small rounding difference alone says nothing about the real experimental limits, which require source-specific analysis. The [standard-library check](./ifg_internal_check.py) reproduces both calculations from the PDF’s stated numbers and asserts the direction of the strict inequality.

## What would establish the mechanism and fit

Appendix A makes `μ̃` fundamental and assigns it the canonical scalar kinetic term. In those variables, the printed homogeneous Klein–Gordon equation is the usual scalar equation with a chosen exponential potential `U(μ̃)=V₀exp(−μ̃/M)`. The PDF does not show a separate term in that equation that follows specifically from dividing a different independently dynamical `μ` by `√(−g)`. A technical derivation can state exactly which choice causes the tracker, give conditions on potential slope, background fluid and initial data, and compare against an otherwise matched ordinary scalar model. The Figure 2 energy-fraction curve is close to zero over much of the plotted early interval; demonstrating tracking requires a quantitative scaling diagnostic, not the caption alone.

Reproduction of `w₀,wₐ`, the reported initial-condition robustness and the Figure 1 constraint curve would require code, numerical tolerances, initial ranges, potential normalization, survey likelihood and conversions of the cited Cassini, MICROSCOPE and torsion-balance limits. The PDF provides an original proposed geometric framing, explicit equations, a constructed bound and plotted trajectories; the current audit verifies only two internal algebraic consequences. It does not independently establish a solution to the cosmological coincidence problem or confirm current experimental compatibility.

## Public metadata review

The live Zenodo title and description use strong result language from the paper and report its numerical values, but the PDF lacks the settings to replay its claimed wide scan. The cover says `Daniel Jacob Read`, matching the creator `Read, Daniel Jacob` and ORCID `0009-0000-6133-1872`; the record also lists a same-named Researcher contributor. The record has one comma-packed eighteen-phrase subject, a `Version: 1.0` version string that displays as “Version Version: 1.0,” CC BY 4.0 license/copyright metadata, and no related-work relation. The PDF itself has no explicit license section. These fields were observed, not changed. No relation should be inferred from the broader research program without a specific source.

A source-grounded description clarification would identify equations (1), (8) and the two authored plots as proposed model work, state that the figures are not independently reproduced from deposited code, and flag the FLRW exponent for a technical correction. [Issue #28](https://github.com/aruintelligence/aruintelligence/issues/28) tracks that derivation, numerical release, constraint provenance and metadata cleanup. The five-page original PDF remains the authoritative deposited source for this review.
