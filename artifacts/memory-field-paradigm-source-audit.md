# Memory Field Paradigm: deposited-source and exact limiting-case review

**Source:** [The Memory Field Paradigm, DOI 10.5281/zenodo.18645539](https://doi.org/10.5281/zenodo.18645539), Daniel Jacob Read IV, ĀRU Intelligence Inc. The three-page PDF is dated 14 February 2026; Zenodo records the public publication on 15 February and version 1.0. Reviewed 30 October 2026 Pacific. The reviewed PDF is 176,617 bytes, MD5 `5221fb2ef02f3fbe28b89a12364cd8ce` (matching Zenodo), SHA-256 `61c46932a97dafbc2ac227bcb275c5a991ca15d4eab248c9109756977dabbe51`.

## Page map

| PDF page | What is actually there |
|---|---|
| 1 | Cover, ORCID, abstract and series-level map from the First through Seventh Laws and later harmonics. The author calls the work an internally coherent synthesis and explicitly says no external validation is claimed. |
| 2 | A positive scalar density `μ(x,t)`, diffusion–relaxation–source equation (1), stipulated exponential variance relation (2), coherence definition, compact law equations for mass, gravity, time, reaction, amplification, intelligence and overlap, and an archive expression (3). Several cross-domain coefficients and observables are not calibrated here. |
| 3 | Ontological implications, proposed gravimetric/time-rate, biofeedback and focus probes, a discussion of null outcomes, conclusion, author contact and CC BY-NC-ND 4.0 license. No new observations, dataset, instrument calibration or independent replication appears in this synthesis. |

## Exact conditional check of equation (1)

Set the spatial Laplacian to zero and the source to a constant `S`. For `λ>0`, equation (1) becomes `dμ/dt=−λ(μ−μ₀)+S`, with the exact solution

`μ(t)=μ_eq+(μ(0)−μ_eq)exp(−λt),     μ_eq=μ₀+S/λ`.

If `μ(0)>0`, `μ₀≥0` and `S≥0`, this spatially uniform trajectory stays positive at every finite `t≥0`. Its accumulated registration is

`A(t)=μ_eq·t+(μ(0)−μ_eq)[1−exp(−λt)]/λ`,

where `μ_eq` is the equilibrium. If `κ≥0`, the PDF's *separately stipulated* equation (2) yields `σ²/σ₀²=exp(−κA)` and its coherence definition yields `C=1−exp(−κA)∈[0,1]`. This proves a conditional internal relationship for this limit; the linear field equation alone does not derive the exponential variance rule or establish a physical field.

The [standard-library exact check](./paradigm_homogeneous_check.py) uses illustrative `λ=0.15`, `μ₀=0.10`, `S=0.02`, `μ(0)=0.05`, `κ=0.5`. At `t=10`, it obtains `μ_eq=0.233333333`, `μ=0.192426137`, `A=1.383825751`, stipulated variance ratio `0.500617533` and `C=0.499382467`. These are chosen model values, not measurements or fitted parameters. As an off-domain challenge to an *unrestricted* source, `λ=μ₀=μ(0)=1` and `S=−2` gives `μ(t)=2exp(−t)−1`, crossing zero at `ln 2`. This shows why source, initial and boundary assumptions are needed to preserve `μ>0` for the full PDE and to use the PDF's inverse-`μ` time-rate expression. It does not assert that a negative source represents the author's intended attention input.

## Public record and research path

The record's description was expanded on 27 October 2026 with the homogeneous-limit result, its positivity assumptions, and the distinction between equations (1) and (2). Public readback on 30 October verified the note; title, creator `Read IV, Daniel Jacob`, ORCID, preprint type, 15 February public publication date, version 1.0, eight individual subjects, CC BY-NC-ND 4.0 rights, `Is supplemented by` link to the [Experimental Roadmap](https://doi.org/10.5281/zenodo.18708708), and PDF checksum remain. The roadmap contains six proposed probes and has a separate [PDF/EEG endpoint audit](./experimental-roadmap-source-audit.md).

A next technical edition can define units, source sign/range, boundary and initial conditions, a well-posed positive solution domain, a measured proxy for `μ` or a directly falsifiable alternative, calibrated coupling ranges, and a predeclared null bound that cannot be adjusted after seeing results. [Issue #25](https://github.com/aruintelligence/aruintelligence/issues/25) records that review path. The PDF's philosophical conclusions remain the author's propositions; this audit verifies only the specified mathematics in one limiting case.
