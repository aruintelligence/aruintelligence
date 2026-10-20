# Ninth Law DOI source audit

**Record:** [10.5281/zenodo.18049220](https://zenodo.org/records/18049220) · **metadata republished and publicly read back:** 2026-10-20 Pacific  
**Deposited file:** `Ninth_Law_Toy_Model_HighTech_5000yr_Edition.pdf` · 8 US-letter pages · 385,563 bytes  
**Integrity:** Zenodo MD5 `0c6fd4c7a2ce40c28b88c2a4185ba945`; downloaded SHA-256 `131c0eeed11d87f62907ffab21377deaa861c14ba3bb6c478431170c2dc3496b`. All eight pages were rendered and checked. “5000-Year Tech Edition” is the edition title, not a 5,000-year observation.

## Contribution and page provenance

The deposit turns the Ninth Law's commitment idea into an inspectable three-branch numerical example. Page 2 defines `C_b = ∫ w(s)|Θ_b(s)|^p ds`, a crystallization condition `C_b ≥ C₀`, and `b* = argmax_b C_b`. It calls `s` a sealed path index rather than physical time. Page 3 specifies a 100-point grid on `[0,10]`, `w=1`, `p=2`, `C₀=5`, and sustained, wavering, and decaying orientation-fidelity paths. Page 4 plots the paths and commitment scores. Page 5 plots a nonlinearity sweep, while page 6 illustrates a localized structural weight as an extension; the primary numerical run does not apply that plotted weight. Page 7 prints a short NumPy reference implementation. Page 8 closes with the author's all-rights-reserved notice.

| Branch | Page 3 input | Page 4 reported `C` | Independent replay of the page 7 rule |
|---|---|---:|---:|
| Sustained | `Θ₁(s)=1` | 10.000 | 10.000000000000002 |
| Wavering | `Θ₂(s)=0.5+0.5 sin(2πs/5)` | 3.750 | 3.75 |
| Decaying | `Θ₃(s)=exp(-s/3)` | 1.499 | 1.4986571207263326 |

The independent check used NumPy 2.3.5, `linspace(0,10,100)`, `trapz(w*abs(Θ)**p,s)`, and the three printed paths. To three decimal places it reproduces all three deposited values. With `C₀=5`, the crystallization flags are true, false, false, and `argmax` selects branch 1. At `p=1,2,3,4` the replay gives `C₂=5,3.75,3.125,2.734375` and `C₃≈2.893251,1.498657,1.000805,0.751132`; `C₁=10` throughout. This agrees with the plotted decreasing trend. The page 7 `np.trapz` call still computes the example in NumPy 2.3.5, with a deprecation warning; `np.trapezoid` is the current equivalent for a future code edition. These checks establish numerical reproducibility under the stated toy assumptions, not an observed physical branch selection.

## Next precise refinements

1. **Threshold and selection together.** The prose says the realized branch exceeds a threshold and dominates alternatives. The printed code computes the threshold flags but returns `argmax(Cs)+1` unconditionally. State what happens when no branch reaches `C₀`, and whether selection is over all branches or only eligible branches. Define tie handling. At `p=1` on the printed paths, branch 2 exactly meets `C₀=5`; the `≥` sign admits it but branch 1 still has the maximum.
2. **Structural-weight extension.** Page 6 gives a useful visual lever but no weighted commitment values or exact plotted weight function. Publish its formula or underlying data, run the three branches with that weight, and show sensitivity to normalization and `p`. That would make the extension as reproducible as the primary run.
3. **Bridge to a testable interpretation.** Define how an orientation-fidelity path and the threshold would be obtained independently of an outcome, and specify a null or competing model before treating a selected branch as an external observation. The present artifact is a transparent numerical construction; the phrases “recognition” and “sealed field” are conceptual premises in it.

## Public metadata correction and retained fields

On October 20, 2026 Pacific the record description was republished to foreground the law, exact primary inputs and outputs, p-sweep, structural-weight illustration, and embedded Python reference. It distinguishes the computed toy scores from external measurements. The creator was corrected from `Read, Daniel Jacob` to `Read IV, Daniel Jacob`, matching the visible cover and page 8; the existing affiliation, Researcher role, and ORCID `0009-0000-6133-1872` were retained. One comma-joined subject was replaced with eleven individually indexed terms tied to the pages: Inward Physics; Ninth Law; Commitment Integral; Worldline Selection; Crystallization Threshold; Non-Temporal Path; Orientation Fidelity; Structural Weighting; Coherence Amplification; Nonlinearity Sweep; Python Toy Model. The generic copyright placeholder became `© 2025 Daniel Jacob Read IV. All Rights Reserved.`, supported by page 8. The description also preserves the file's no-reproduction notice, without inferring an open license.

Public readback showed all four corrected areas and modified date October 20, 2026. The title, deposited PDF and checksum, Report type, English, December 24, 2025 publication date, Zenodo publisher, blank editable version (public `v1`), concept DOI `10.5281/zenodo.18049219`, and empty related-works list were retained. No physical result, license, or relation to adjacent Law DOIs was added.
