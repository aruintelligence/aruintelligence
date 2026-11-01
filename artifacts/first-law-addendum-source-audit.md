# First Law Methods & Constants Addendum — deposited-source audit

**Source:** [DOI 10.5281/zenodo.17297181](https://doi.org/10.5281/zenodo.17297181), *The First Law of Inward Physics — Methods & Constants Addendum (2025)*, Daniel Jacob Read IV, ĀRU Intelligence Inc., October 2025. Reviewed 31 October 2026 Pacific. The two-page, 7,149-byte PDF matches public Zenodo MD5 `870683d06c9e33fadbd8774603703501`; reviewed SHA-256 `52303cd266c531f276725687494937d473cb92f55ff8e1ad022c1cc6b57d6fb4`.

## PDF contribution and exact boundary

Page 1 defines a dimensionless `μ=1−Φ/c²`, proposes mass by `M=κ_m∫μd³x`, chooses `κ_g=−c²` and `κ_t=1`, and writes a diffusion–relaxation–source equation `∂μ/∂t=D∇²μ−λ(μ−1)+S`. It outlines a shielded MRAM/gravimeter or atom-interferometer test, and paired-clock comparison. Page 2 specifies randomized on/off drives, environmental sensing, OSF preregistration, blinded analysis, independent replication and publication of null findings. It claims recovery of familiar gravity, weak-field clock and mass limits. No measurement, dataset, source coupling coefficient or expected device-scale effect is supplied.

The gravity and clock expressions are internally checkable **as algebra from the definition**:

```text
∇μ = −∇Φ/c²,  so  −κ_g∇μ = c²∇μ = −∇Φ
1/μ = 1/(1−Φ/c²) ≈ 1+Φ/c²  for |Φ|/c² ≪ 1.
```

That recovers the printed formulas under the chosen conventions but is not an independent observation of a memory substrate. The `S→0` limit alone does not force spatially uniform `μ=1`: a nonzero Newtonian potential gives `μ=1−Φ/c²`, and the evolution equation's stationary state depends on boundary data and initial conditions. If device writing or erasure creates `δμ` at fixed Φ, the author needs to specify whether `μ=1−Φ/c²` remains an exact definition, whether Φ itself changes, and where energy/field backreaction enters. Those distinctions lead to a discriminating test rather than mere recovery by construction.

The experimental outline is a useful starting protocol: shielded drive, matched clock, environmental sensors, randomization and null publication. A preregistration-ready version would state bit-pattern schedule, duty cycle, reservoir mass/energy/heat, source `S` units and transfer coefficient, predicted `δg` and `δτ` with uncertainty, sample size and duration, sensor calibration, leakage controls, sham drive and a primary endpoint. The Bayes-factor threshold on p. 2 needs a model, priors and decision rule before it can define a positive result.

## Public metadata status

The [public record](https://zenodo.org/records/17297181) was modified 20 October 2026 and already displays a source-scoped description that correctly notes the algebraic construction and reproducibility limits; creator `Read IV, Daniel Jacob`, Report, 5 October 2025, version `1.0 — Laboratory Edition`, eight separate subjects and CC BY-NC-ND 4.0 matching the PDF cover. The record says `Is supplement to` First Law DOI `17296987`, which the addendum title supports. Three more `Is supplement to` targets are Second Law `17297355`, Third Law `17314619` and Fourth Law `17317217`; inspect their direction separately rather than changing the whole relation set. The PDF gives an October 2025 date and does not itself print the record's version label; keep that provenance distinct. [Issue #38](https://github.com/aruintelligence/aruintelligence/issues/38) tracks the model and relations. No new Zenodo edit was made.
