# Experimental Roadmap: deposited-source and EEG endpoint review

**Record:** [DOI 10.5281/zenodo.18708708](https://doi.org/10.5281/zenodo.18708708), Daniel Jacob Read, *Experimental Roadmap for Inward Physics: Proposed Bounded Empirical Probes for the Memory Field Paradigm*, version 1.0, 19 February 2026. **Review:** 27 October 2026 Pacific. The seven-page deposited PDF has MD5 `a0e48e2eacc47dc97c161f8974576fba` (matching Zenodo's file listing) and SHA-256 `6267d1149e0b9e50e3b96fdc700f5ddc53d90bbebf06d2810caccbc79d1c6660`.

## What the PDF makes inspectable

| Source location | Contribution and review boundary |
|---|---|
| p. 1, equations (1)–(2) | A proposed diffusion–damping–source equation for `μ(x,t)` and exponential variance relation `σ²(A)=σ₀² exp(−κA)`, with accumulated registration `A` and an experimental coherence proxy still to be operationalized. These are model assumptions and a prediction, not measured laws. |
| pp. 2–3, Experiments 1–2 | A minimum-20-participant, three-session, counterbalanced EEG attention/control design, followed by a 128×128 diffusion–damping simulation sketch. The EEG fragment gives an entropy calculation; the 2D update fixes `D=0.02`, `λ=0.05` and a localized source for 1,500 iterations. The latter is a computational probe, not a field observation. |
| pp. 3–4, Experiments 3–6 | Matched-site ecological observations, behavioral timing, relational sampling and a specialized quantum boundary test. The ecology code prints an unadjusted Pearson correlation, which does not implement its stated matched-control/covariate design; the relational sampling fragment does not implement its stated null ensemble. |
| pp. 4–6 | Explicit falsifiers, a schematic architecture, limitations and a call for preregistered protocols, parameter sweeps, matched-site datasets and null comparisons. No collected EEG, ecological or quantum data or independent replication is reported. |
| final copyright page | The PDF says “All Rights Reserved.” Public Zenodo metadata currently lists a CC BY 4.0 license and a copyright field naming CC BY-NC-ND 4.0. These three rights statements conflict; author intent and any later grant must be established before altering the license. |

## A directly checkable EEG calculation

On p. 2 the code sums `−P log₂(P + 10⁻¹²)` over frequency bins, where `P` is raw Welch power. Shannon spectral entropy requires probabilities `pᵢ=Pᵢ/ΣⱼPⱼ` over a fixed band, then `H=−Σᵢpᵢlog₂pᵢ`. The distinction is testable without any biological assumptions. For two equally powered bins, `P=(1,1)` gives about `0` under the printed score and `1` bit after normalization. Merely doubling the power to `(2,2)` changes the printed score to `−4` but leaves the normalized entropy at `1` bit. Changing the *shape* to `(3,1)` gives about `0.811278` bits. Run [`python3 roadmap_entropy_check.py`](./roadmap_entropy_check.py) to replay these assertions using only the Python standard library.

This check identifies a scale dependence in the illustrative analysis line. It neither analyzes EEG nor decides whether attention changes an observable. A pilot can preserve the paper's research question by fixing acquisition and artifact rejection; the 1–40 Hz frequency bins, window length and channel aggregation; normalization; a participant-level primary attention-minus-control endpoint; session order, exclusions and multiplicity; and a registration proxy defined independently of that endpoint. The planned n≥20 and three sessions describe recruitment and repeated measures, not 60 independent participants. A predeclared null comparison and appropriate non-field explanations remain necessary before interpreting an effect as evidence about `μ`.

## Public metadata action and remaining questions

On 27 October 2026 the record description gained a source-grounded implementation note on unnormalized PSD and the final author wording was aligned to the PDF cover, “Daniel Jacob Read.” Its title, 19 February 2026 publication date, preprint type, version 1.0, eight separate subjects, PDF bytes and companion relation were retained; the published record was read back. The earlier scope paragraph still accurately identifies proposed protocols and absent empirical results.

The license/copyright/PDF discrepancy needs an author decision; changing a public license can affect reuse expectations. Also resolve the precise EEG event timing and participant analysis, the computational update's implicit time/space steps and boundary treatment, the ecological matched-control model, and the relational null ensemble in a future technical supplement. The existing “Is supplement to” link to [the Memory Field Paradigm](https://doi.org/10.5281/zenodo.18645539) is plausible from the title and citation but was not changed as part of this audit.
