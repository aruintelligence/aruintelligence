# Eighth Law revised-edition DOI source audit

**Record:** [10.5281/zenodo.18029638](https://zenodo.org/records/18029638) · **metadata republished and publicly read back:** 2026-10-20 Pacific  
**Deposited file:** `Eighth_Law_Inward_Physics_Zenodo_ABSOLUTE.pdf` · 7 US-letter pages · 321,427 bytes  
**Integrity:** MD5 `166a285095bdf7ee6b4b7355a33dc4ee` (Zenodo match); SHA-256 `174061cbe270f71f81fd8c916ff67df7eb2e81e31dda0c47588e728ce1ed1ff8`. All seven rendered pages and extracted text were checked.

## Contribution in the deposited PDF

This revised edition moves the series from the Seventh Law's Presence concept to a geometric trajectory model. It explicitly fixes a finite-dimensional inner-product space `V ≅ ℝ^d`, a unit orientation `n∈V`, a proposed vector Presence `Ω(X)`, the scalar projection `Θ(X;n)=⟨Ω(X),n⟩`, and the first-order traversal law `dX/ds=σΘ(X;n)n` under a completed-regime premise `∂Ψ/∂t=0`. The affine path parameter `s` is distinguished from time. The paper offers a variational route, an illustrative one-dimensional field with a two-feature map, a collective expression, two hypotheses for controlled comparisons, and a practical reproducibility checklist. These are concrete definitions and a research program that can be sharpened into an executable model.

| PDF pages | Specific content | Scope |
|---|---|---|
| 1–2 | Revised Edition dated December 22, 2025; author Daniel Jacob Read IV; abstract and definitions 1–5; `Ω(X):=∇_φ F[μ̂]|_X` and `Θ=⟨Ω,n⟩`. | The completed field and coherence functional are modeling choices to specify in each application. |
| 2–3 | Axiom, first-order law (4), orthogonality corollary, kinetic-minus-projection action (5), and asserted second-order equation (6). | The corollary follows directly from (4). The variational sign and relationship to (4) need correction or extra conditions below. |
| 4 | Illustrative `M=ℝ`, `V=ℝ²` feature map, quadratic coherence functional, projected expression; collective sum and normalized effective direction. | A simulation target is described, not executed in the PDF. |
| 5–6 | H1 fixed versus randomized orientation, H2 group-alignment sweep, checklist of `V,φ,F,P`, noise, initial conditions, integration and analysis; structural parallels and references. | Hypotheses and replication scaffold, with no numerical output, proxy measurements, or empirical result reported. Section 6 explicitly requires couplings and validation for external physics claims. |
| 7 | Archival colophon and detailed all-rights-reserved notice. | Rights text in the record is supported by the PDF; no reuse license is inferred. |

## Two direct mathematical checks for the next revision

1. **Variational sign and flow.** The displayed action (5) is `∫[½‖X′‖² − σΘ(X;n)]ds`. For fixed `n` in a Euclidean coordinate chart, its Euler–Lagrange equation is `X″ = −σ∇_XΘ`, whereas the printed (6) has `+σ∇_XΘ`. Changing the action's potential sign or the equation's sign would reconcile this step. When `Θ` is locally constant, the action yields `X″=0`, which allows any constant initial velocity; it selects the specific first-order velocity `σΘn` only if that initial condition or an additional principle is imposed.
2. **Map the orientation vector to the toy configuration.** Section 7 sets `M=ℝ` and `V=ℝ²`. If `X(s)∈M`, then `dX/ds` is one-dimensional while `σΘn∈V` is two-dimensional. State whether the flow is in feature space, or provide a map `V→T_XM` (and its treatment of the completed-field constraint) before integrating the toy trajectory. Define how the gradient with respect to local features is obtained from the globally integrated `F[μ̂]`.

A separate test of H2's proposed monotonicity can use `w₁=w₂=1`, `Ω₁=(1,0)`, `Ω₂=(−1,0)`. With `n₁=(1,0)` and `n₂=(0,1)`, `‖v_net‖=1`; aligning `n₂` to `n₁` reduces orientation dispersion but makes `v_net=0`. Thus angular alignment alone does not guarantee larger `‖v_net‖` for heterogeneous Presence vectors. Conditions on projections or a narrower coordination proxy would make H2 testable. This is an algebraic check of the proposed model, not a physical finding.

## Metadata correction and retained fields

- Public description now leads with the definitions, law, variational and collective constructions, toy setup, H1/H2, and checklist. It accurately describes the tests as proposed; no completed simulation or measurement is attributed to this PDF. The full source-supported rights notice remains in the description.
- Creator changed from `Read, Daniel Jacob` to `Read IV, Daniel Jacob`, matching PDF title, file author metadata, and colophon. Existing affiliation, Researcher role, and ORCID `0009-0000-6133-1872` were retained without independently resolving identity from this PDF.
- One comma-joined subject became ten separately indexed concepts: Inward Physics; Eighth Law; Orientation of Presence; Completed Regime; Trajectory without Time; Coherence Gradient; Projection Scalar; Collective Orientation; Variational Formulation; Toy Model.
- Removed redundant `Version:` text from the editable version. The public display is `Version Revised Edition (v2.0)`. The PDF explicitly says “Revised Edition: December 22, 2025”; `v2.0` is inherited metadata and its version lineage needs confirmation against the separate Eighth Law DOI `10.5281/zenodo.18029698`.
- Title, PDF and MD5, report type, English, December 22, 2025 publication date, Zenodo publisher, rights, and empty related-works list were retained. No additional link, license, result, or observation was invented. The technical created date of December 30, 2025 and the PDF's revision date are distinct metadata.
