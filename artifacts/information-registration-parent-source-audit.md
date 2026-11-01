# Information Registration cross-scale parent — deposited-source audit

**Source:** [DOI 10.5281/zenodo.18091325](https://doi.org/10.5281/zenodo.18091325), *Information Registration as a Physical Accumulation Mechanism: A Cross-Scale Model from Quantum Measurement to Biological Memory*, Daniel Jacob Read IV, ĀRU Intelligence Inc. The six-page PDF is dated December 2025; Zenodo publicly lists 29 December 2025, Preprint. Reviewed 31 October 2026 Pacific. The 57,150-byte deposited PDF matches public Zenodo MD5 `3b24fe3db974a3a8338bd9dbbab60dfd`; reviewed SHA-256 `267f821a65191d40b528f0fcd1074eb541ac7778b676a3f62959e8b7bfc199a2`.

## Deposited contribution

| PDF page | Source content |
|---|---|
| 1 | Title, abstract and proposed mechanism: irreversible registration into physical media produces an accumulated constraint. The introduction does not assign a role to conscious observers. |
| 2 | Figure 1 sketches registration → accumulation → constraint → stability. Sections 2–3 define measurement as record-bearing physical interaction and propose a coupling between system state and a record-bearing subsystem. |
| 3 | Figure 2 depicts narrowing accessible trajectories. Section 4 defines `A(T)=∫₀ᵀR(t)dt` and posits `dσ²/dA=−κσ²` with `κ>0`, yielding `σ²(A)=σ₀²e^(−κA)`. |
| 4 | Figure 3 plots illustrative exponential curves for different κ values. Sections 5–7 propose a physical-memory definition and compare quantum, classical, biological and computational domains. No empirical points or fitted coefficients are given. |
| 5 | Figure 4 is a conceptual cross-scale diagram. Section 8 gives predictions about repeated low-energy registration, artificial forgetting, record disruption and monotonic scaling; section 9 closes the theory argument. |
| 6 | All Rights Reserved notice and author/affiliation/edition colophon. |

## Exact implication and a useful test boundary

The ODE has a clear conditional mathematical result. For `κ>0`, `σ₀²>0` and nonnegative registration rate `R(t)`, `A(T)` is nondecreasing and the stipulated variance law is nonincreasing: `dσ²/dT=−κR(T)σ²(T)≤0`. At **fixed accumulated registration**, schedules with different peaks predict the same final variance. The [companion five-page experimental-probes PDF](https://doi.org/10.5281/zenodo.18091788) proposes the physical comparisons, and its [exact schedule check](./information_registration_probes_check.py) makes this implication inspectable.

The variance law is introduced as a phenomenological assumption, not derived from the displayed system/record mapping or from established decoherence, synaptic or machine-learning equations. To assess the cross-scale claim, each domain needs a registration measure independent of the variance outcome, a definition of accessible state-space and measured `σ²`, units for R and κ, a matched baseline, and a comparison with alternative decay laws. The conceptual Figures 1–4 and the plotted formula are model illustrations, not measured evidence.

One prediction spans a distinct process: if `R≥0`, the printed accumulation law does not reduce A when a record is erased, so it cannot by itself predict variance rebound after disruption. A loss term, effective-registration state or specified intervention is needed. The companion audit treats that and the energy-versus-registration comparison in more detail. These conditions make the author's proposed cross-domain mechanism testable without assigning results to unrun experiments.

## Public metadata and individual relation

The public record's title matches the deposited parent paper. It shows creator `Read, Daniel Jacob` without a visible ORCID icon, rendered `Version Version 1.0 — Initial Archival Release`, a single comma-packed subject, and a restrictive copyright field with no reuse license; no related-work DOI is displayed. The PDF cover and colophon support the suffix `Read IV, Daniel Jacob`, the December 2025 document date, Archive/Preprint edition and All Rights Reserved rights. The displayed version should be a concise edition value after author review. The deposited appendix itself expressly names this parent paper, and the two public records have distinct MD5 values; an individual `Is supplemented by` relation from this parent to appendix DOI `10.5281/zenodo.18091788` is a source-backed candidate, with the inverse `Is supplement to` from the appendix after checking the record-owner's intended schema. This is not a bulk relation change.

A corrected description would call `A` and the exponential law a proposed cross-scale model, identify Figures 1–4 as schematics/model curves, and link the separately deposited experimental design. Keep the PDF and rights intact. [Issue #33](https://github.com/aruintelligence/aruintelligence/issues/33) tracks calibration, controls and the record-specific metadata decisions. No Zenodo metadata was edited in this signed-out pass.
