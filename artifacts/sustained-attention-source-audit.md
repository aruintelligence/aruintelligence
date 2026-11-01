# Sustained Attention ecological model — deposited-source audit

**Source:** [DOI 10.5281/zenodo.18074036](https://doi.org/10.5281/zenodo.18074036), *Sustained Attention as a Stabilizing Resource: An Inward Physics–Inspired Model of Ecological Coherence and Regeneration*, Daniel Jacob Read IV, ĀRU Intelligence Inc. The five-page PDF is dated 27 December 2025; Zenodo lists 28 December 2025, version `v1.0`, Preprint. Reviewed 31 October 2026 Pacific. The 168,405-byte file matches Zenodo MD5 `582c31f51e83fe1029e246549d9e7b82`; reviewed SHA-256 `de1a3cb0ae07bd95db3eabe27a779fee7b4bed80d7b418d51cc2e96b332dc553`.

## Page map and contribution

| PDF page | Deposited content |
|---|---|
| 1 | Abstract and introduction propose an Attention–Coherence Hypothesis (ACH) for continuity of ecological stewardship. The author explicitly uses Inward Physics as a modeling language, not a measured field. |
| 2 | Defines cumulative on-site attention `A(t)=∫₀ᵗa(τ)dτ`, coherence proxy `C(t)`, and proposed law `dC/dt=kΦ(A(t))−λD(t)`; states episodic-gap claim and falsification conditions. Gives soil, vegetation and hydrology metrics. |
| 3 | Two matched plots over 90 days, logged attention dose, fixed photo stations and standardized rubrics; limits say attention does not replace material resources. References are listed. |
| 4 | Figure A1 is a conceptual feedback diagram, not field observations. |
| 5 | Daniel Jacob Read IV copyright and All Rights Reserved archival notice. |

## Exact gap between cumulative attention and episodic decay

The paper's ecological proposal has a valuable observable core: log monitoring and small corrective actions, then compare measurable soil, vegetation and hydrology outcomes against a matched control. But the **printed equation does not yet imply the episodic-gap prediction**. If `a(t)≥0` is integrable, `A(t)` is continuous and nondecreasing; when visits stop, it has a plateau rather than a discontinuity. During a gap with constant `A=A₀` and disturbance `D=D₀`, the printed law gives `dC/dt=kΦ(A₀)−λD₀`. The sign depends on the parameters: C can still rise during an arbitrarily long gap. The [standard-library check](./sustained_attention_gap_check.py) gives an illustrative positive-slope countercase with a stopped visit schedule.

To model the claimed importance of *recent* monitoring, the author could introduce a decaying active-attention state `H' = a(t)−ρH` and use `Φ(H)` for the feedback term, or condition equation (3) on `λD>kΦ(A₀)`. Either route requires units, a bounded-domain or saturation rule for C, and a prespecified observational endpoint. The first route changes the model and needs a future edition; the second narrows the existing claim. The finite two-plot protocol is a pilot design, not an estimate of effects across restoration sites. Separate monitoring from corrective work and match material inputs to test whether attention adds predictive power beyond intervention intensity; predeclare site pairing, baseline, seasonality, weather, observer effects and negative controls.

## Public metadata and precise next step

The public record title matches the PDF. Zenodo shows creator `Read, Daniel Jacob` without a visible ORCID icon, 28 December 2025 publication, `v1.0`, one comma-packed subject value, and restrictive copyright without a reuse license; no related-work DOI is displayed. The PDF author is Daniel Jacob Read IV, with 27 December authorship date. The record description accurately calls this a proposed model and a 90-day protocol, but the phrase “derives falsifiable predictions” should not imply that equation (3) has already been derived from (1)–(2). A source-grounded revision would say that episodic-gap decline is **hypothesized** and identify the additional decay or disturbance condition needed; align the creator suffix, split searchable subjects, and retain the PDF's rights. [Issue #34](https://github.com/aruintelligence/aruintelligence/issues/34) tracks the equation and pilot implementation. No Zenodo metadata was changed in this signed-out pass, and no ecological result was inferred.
