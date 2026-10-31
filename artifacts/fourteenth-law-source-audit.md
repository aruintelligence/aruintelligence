# Fourteenth Law: deposited-source and Gaussian passband review

**Source:** [The Fourteenth Law of Inward Physics: Resonant Boundary Selection in Completed Systems, DOI 10.5281/zenodo.18917411](https://doi.org/10.5281/zenodo.18917411), Daniel Jacob Read IV, ĀRU Intelligence Inc. The four-page PDF is dated March 2026; Zenodo published it on 8 March 2026. Reviewed 30 October 2026 Pacific against the deposit (170,860 bytes; MD5 `90592de63e88376105d32ba140d0d42c`, matching Zenodo; SHA-256 `fa807ea1628914449261699fc8710459e73ed0be6cb23428df843f79843e4dfb`).

## Page map

| PDF page | Deposited contribution |
|---|---|
| 1 | Cover, ORCID, abstract and motivation: a completed system with an identity invariant needs a selective environmental boundary in the proposed framework. |
| 2 | Defines external spectral density `S_E(ω)`, carrier `Ω*`, coherence order parameter `R∈[0,1]`, transmission `T(ω)=Gρ f_R(ω−Ω*)`, Gaussian `f_R(Δ)=exp[−Δ²/(2σ_R²)]`, and bandwidth `σ_R∝(1−R)`. The PDF calls `B(ω)` a probability operator but does not equate or bound it against `T`. |
| 3 | Describes resonant passband, spectral coupling flux `Φ_eff=∫T(ω)S_E(ω)dω`, the assumed identity condition `dI/dτ=0`, and the Fourteenth Law statement. The flux formula alone does not derive identity conservation. |
| 4 | Qualitative failure modes, conclusion and references to the Memory Field Paradigm and Experimental Roadmap. No measurement, numerical settings, spectrum, fitted bandwidth, or independent physical validation is supplied. |

## Exact consequence of the printed filter

Set `σ_R=c(1−R)` with an illustrative positive proportionality constant `c` for `0≤R<1`. Let `S_E(ω)=S₀≥0` within the finite interval `Ω*−W≤ω≤Ω*+W`, and zero elsewhere. With constant nonnegative `Gρ`, the paper's flux integral evaluates exactly to

`Φ_eff=Gρ S₀ sqrt(2π) σ_R erf[W/(sqrt(2) σ_R)]`.

For `W>0`, this **continuous-spectrum** flux approaches zero as `R→1` because the Gaussian has unit peak but shrinking area; it is not an area-normalized kernel. In contrast, an ideal spectral line `S_E=Lδ(ω−Ω*)` contributes `Gρ L` at every `R<1`. A finite instrument bin has its own width and shape, so an experimental claim needs the spectral resolution and input normalization. The Gaussian expression itself is undefined at exactly `R=1` unless the model supplies a limiting convention.

The [standard-library exact check](./fourteenth_law_passband_check.py) uses illustrative dimensionless `c=W=1`, `Gρ=0.8`, `S₀=2`: `Φ_eff` falls from `2.737998054` at `R=0` to `0.040106052` at `R=0.99`; the aligned ideal-line transmission remains `0.8` for `R<1`. The script checks the analytic narrow-band limit and off-carrier attenuation. These are properties of the paper's stipulated filter, not measurements of a completed system or a memory field.

If `T` is to be interpreted as a coupling probability, `0≤Gρ≤1` and a definition of the input spectrum are sufficient for `0≤T≤1` in this simple formulation; the PDF does not specify the units or domain of `G` and `ρ`. An area-normalized passband would change the meaning and peak value of `T`, so normalization cannot be silently inserted. A technical edition can define the operator `B`, input units, bandwidth scale, limiting `R=1` rule, and an identity-update equation that states when filtering preserves `I`. A discriminating test can prespecify line-like and broadband inputs, matched total input power, bandwidth, controls, and a null outcome.

## Public record and relation scope

Zenodo already presents the creator as `Read IV, Daniel Jacob` with the PDF's ORCID, classifies the work as a preprint, has eight separate relevant subjects, and links `Is derived from` to the [Memory Field Paradigm](https://doi.org/10.5281/zenodo.18645539). Its 20 October description explicitly scopes the theoretical argument, the missing parameter/identity derivation and the `R=1` denominator. The license and copyright metadata state CC BY 4.0, whereas the four-page PDF has no explicit license section. This review retains those public metadata and relation fields; it does not infer a new link merely because the reference list names the Roadmap.

[Issue #27](https://github.com/aruintelligence/aruintelligence/issues/27) tracks the input-spectrum and identity-conservation specification. This exact limiting calculation is a way to sharpen the author's original boundary-selection proposal for review and a future controlled experiment.
