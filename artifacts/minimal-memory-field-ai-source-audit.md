# Minimal memory-field AI simulator DOI source audit

**Record:** [10.5281/zenodo.18006990](https://zenodo.org/records/18006990) · **metadata republished and publicly read back:** 2026-10-20 Pacific (Zenodo technical modified date: 2026-10-21 UTC)  
**Deposited file:** `A_Minimal_Memory_Field_AI_Simulator_with_Self_Archiving_Stability.pdf` · 5 US-letter pages · 148,289 bytes  
**Integrity:** Zenodo MD5 `f6e1988b7eea25379225d216997e9cf9`; downloaded SHA-256 `5ea2bfdbb42b9beb2f24503385f2c4fbefbd25101698b8f2ecb5dd9e20b17a20`. All five pages were rendered and checked. PDF author metadata and cover name Daniel Jacob Read IV.

## What this deposit contributes

The report makes the proposed memory-density field operational as a small, inspectable one-dimensional numerical rule. Page 2 states `∂μ/∂t = D∇²μ − λ(μ−μ₀)+S(x,t)` and proposes a saturation factor `1−μ/μ_max`. Its Appendix A specifies the grid, parameters, periodic neighbor update, Gaussian initial state, fixed Gaussian source, 400 explicit steps and final plot. This is a reproducible computational baseline for exploring bounded dynamics. The prose also describes an unstable preliminary regime and a coherence-threshold self-archiving mechanism, which are separate research targets because their code and run data are absent from this deposited appendix.

| PDF page | Content | Checkable scope |
|---|---|---|
| 1 | Title, Daniel Jacob Read IV, Independent Research, December 2025; computational-prototype motivation and abstract. | The author and month are visible; no external AI benchmark is given. |
| 2 | One-dimensional scalar-field equation; diffusion, relaxation, attention source; prose on intermittent pulses, an archive trigger, preliminary instability, and saturation. | These prose scenarios are not the Appendix A implementation. |
| 3 | Claims about stabilized results, limitations, future directions and conclusion. | No numerical table or raw unstable/archiving run accompanies these claims. The report explicitly says one dimension and no learning or adaptive parameters. |
| 4 | Reference Python/NumPy code: `D=.05, λ=.15, μ₀=.10, μ_max=2`; `linspace(-10,10,400)`; Gaussian starting peak; `dt=.45 dx²/(2D)`; `A(x)=.25 exp[-x²/(2·.8²)]`; saturated `S=A(1−μ/2)`; periodic `np.roll`; 400 steps; clamp to `[0,2]`; final plot. | The source amplitude is fixed spatially in this code, despite the prose's intermittent-pulse description. It contains no variance calculation, archive threshold, archive write, or unstable-run branch. |
| 5 | All-rights-reserved copyright, research/exploratory purpose and no consciousness claim. | No open reuse license is inferred. |

A fresh NumPy 2.3.5 replay of page 4's update produced final mean `0.2154056632`, population variance `0.0566952393`, integrated mass `4.3189105397` (sum times `dx`), minimum `0.1000000000`, maximum `0.9505216074`, and **zero cell-step clipping events** over 400 steps. These are independently computed toy-model diagnostics, not numbers printed in the PDF and not physical or AI-performance measurements. They match the [existing source transcription](./reproducible-demo.md) and [independent software audit](./audit-reaction-diffusion.md) associated with the separate related DOI [10.5281/zenodo.18010911](https://zenodo.org/records/18010911), because this deposit's Appendix A specifies the same numerical update and parameters. The [boundedness and contraction certificate](./invariant-certificate.md) applies to this fixed-source rule under its stated assumptions. The two reports remain distinct deposited documents; no byte identity of their PDFs or version lineage is asserted.

## Next source-specific refinements

1. Archive the preliminary unstable-run parameters, initial condition, code, diagnostics and negative controls separately from the stabilized run if the instability claim is to be independently repeated.
2. Specify the archive metric, threshold, decision frequency, saved state, and a reproducible trigger/no-trigger comparison. The current reference script does not implement self-archiving.
3. State whether “attention” is fixed spatial forcing (as on page 4) or intermittent pulses (as in the prose), and define an AI-memory task and baseline before evaluating continual learning or forgetting. The fixed-source rule has an attracting profile under the documented certificate; persistent pattern with ongoing forcing does not by itself show retained initial information.
4. Confirm the intended affiliation and research identifier if desired. The visible PDF says “Independent Research”; the inherited Zenodo creator affiliation is “ĀRU Intelligence Inc.” and its creator identifier is blank. The PDF alone does not settle whether both descriptions apply.

## Public metadata correction and retained fields

The record had already received a careful scope correction dated October 20, 2026, plus eight separate subjects, an author/year copyright notice, and an `Is supplemented by` relation to DOI `10.5281/zenodo.18010911`. This review retained those supported fields and their relation direction. The description was republished to lead with the executable model and exact Appendix A structure while keeping the distinction between implemented code and proposed archiving/AI outcomes. The creator changed from `Read, Daniel Jacob` to `Read IV, Daniel Jacob`, matching the cover, PDF metadata and copyright page; inherited affiliation and Researcher role stayed, with no ORCID invented. The editable version changed from `Version 1.0 December 2025` to `1.0 December 2025`, removing the duplicate Zenodo display prefix while preserving the inherited numeric label and PDF's month. Public display now reads `Version 1.0 December 2025`.

Public readback verified description, creator, version, the eight separately indexed subjects, rights and relation. Title, PDF and checksum, Report type, English, December 21, 2025 publication date, Zenodo publisher, concept DOI `10.5281/zenodo.18006989`, and the previously documented companion DOI correction remained. No new license, physical result, performance benchmark, or relationship was inferred.
