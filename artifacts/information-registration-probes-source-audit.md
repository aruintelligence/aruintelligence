# Information-registration experimental probes — deposited-source audit

**Record:** [DOI 10.5281/zenodo.18091788](https://doi.org/10.5281/zenodo.18091788), publicly titled *Information Registration as a Physical Accumulation Mechanism*. **The deposited PDF is a different-titled companion:** *Experimental Probes of Information Registration and Variance Suppression*, by Daniel Jacob Read IV, ĀRU Intelligence Inc., December 2025. Reviewed 31 October 2026 Pacific. The five-page, 164,553-byte PDF matches Zenodo MD5 `27c74945eaf1d75171a01ed4976a7806`; reviewed SHA-256 `494acf00c6fc0f36c0ee5513707785823d94e2ee33d1aaa0e678d997ada9ad1d`.

## What each page actually contains

| PDF page | Deposit content |
|---|---|
| 1 | Abstract says this is an appendix of experimental probes for the parent paper, not the parent formulation, and explicitly says **no experimental results are claimed**. Defines purpose and three comparative objectives. |
| 2 | Defines registration rate `R(t)`, accumulated registration `A(T)=∫₀ᵀ R(t)dt`, and the hypothesized law `σ²(A)=σ₀²e^(−κA)`. Sets repeated low-intensity versus single high-power comparisons in optical lattices or condensates, hippocampal slice cultures, and a recurrent neural network. |
| 3 | Proposes variance-versus-accumulation plots, record-disruption probes, and state-space-contraction proxies. |
| 4 | States three interpretation criteria: monotonic scaling with A, weak peak-intensity dependence at fixed A, and increased variance after record disruption. |
| 5 | All Rights Reserved copyright and explicit statement that the archival preprint claims no empirical validation. |

## Exact model checks and experimental design

The exponential law gives a useful, falsifiable conditional prediction: **at fixed `A`, `κ` and baseline `σ₀²`, the endpoint variance is the same regardless of the time profile of `R`.** A [small standard-library check](./information_registration_probes_check.py) compares a ten-step low-rate schedule with a one-step high-rate pulse. Both have `A=10` and the same terminal `e^(−1)` variance for illustrative `κ=0.1`; an early high pulse reaches suppression earlier. The paper's Prediction 1 says repeated low-intensity input stabilizes *faster* than a high-power burst at equal total **energy**. Equal energy does not by itself imply equal registration `A`. To make the comparison discriminating, specify how registration is measured independently of the outcome, match or estimate A and energy, predeclare the time-to-stability endpoint, and control the pulse timing and medium.

The record-disruption prediction does not yet follow from `A(T)=∫₀ᵀR(t)dt` if `R≥0`: after the registered history reaches A, simply turning R off leaves A unchanged, so the printed law predicts no variance rebound. A model of erasure needs an effective-registration variable with loss, a reset intervention, or another explicit coupling and a testable distinction from ordinary damage or storage corruption. The state-space contraction claim likewise needs an operational map from a scalar variance to accessible states or entropy; a one-variable exponential does not alone supply it. These are constructive specifications for the experimental program, not observations or a rejection of its possible outcomes.

## Metadata correction prepared for the record owner

The public Zenodo record currently describes a broad *theoretical mechanism* as though this five-page file were the parent paper. It displays Preprint, 29 December 2025 publication, creator `Read, Daniel Jacob` with ORCID `0009-0000-6133-1872`, rendered `Version Version: v1.0 — Zenodo Archive Edition`, one comma-packed subject, restrictive copyright with no reuse license, and no related-work DOI. The deposited PDF names Daniel Jacob Read IV and is dated December 2025; its rights match the restrictive metadata. **The title and abstract should be corrected to identify the actual deposited appendix**, not silently replace the PDF.

Suggested source-grounded description for an owner-controlled Zenodo edit:

> This five-page preprint, *Experimental Probes of Information Registration and Variance Suppression* (Daniel Jacob Read IV, December 2025), is an experimental-design appendix to *Information Registration as a Physical Accumulation Mechanism*. It proposes matched comparisons in quantum, biological and recurrent-network systems to test whether variance suppression tracks accumulated physical registration `A(T)=∫₀ᵀR(t)dt` under the hypothesized relation `σ²(A)=σ₀²e^(−κA)`. It also proposes record-disruption and state-space-contraction tests. The PDF reports designs and expected outcomes, not collected measurements or empirical validation. Registration, energy matching, erasure dynamics, controls, and endpoints require operational definitions before a test.

The owner should set the title to the PDF's exact title, use a concise version value only after checking the intended edition, and split source-backed subjects. The separately reviewed [parent theory PDF, DOI 10.5281/zenodo.18091325](https://doi.org/10.5281/zenodo.18091325), has a distinct checksum and matching parent title; the source-backed relation candidate is this appendix `Is supplement to` that parent, with the reciprocal parent relation reviewed individually. The creator suffix is supported by the cover. Retain the deposited file and All Rights Reserved rights. [Issue #32](https://github.com/aruintelligence/aruintelligence/issues/32) tracks the correction and methods. No Zenodo field was edited in this signed-out review.

## Published correction · 1 November 2026 Pacific

The public title now matches the deposited appendix, *Experimental Probes of Information Registration and Variance Suppression*. The description explicitly scopes proposed experiments and no results; creator displays `Read IV, Daniel Jacob` with the preexisting ORCID, version `v1.0 — Zenodo Archive Edition`, eight separate subjects, and `Is supplement to` parent DOI `10.5281/zenodo.18091325`. Restrictive rights and PDF MD5 `27c74945eaf1d75171a01ed4976a7806` remain unchanged. The earlier signed-out status above is superseded by this public readback.
