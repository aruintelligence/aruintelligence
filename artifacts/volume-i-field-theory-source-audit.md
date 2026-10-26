# Volume I field-theory source audit

**Record:** [10.5281/zenodo.17851542](https://doi.org/10.5281/zenodo.17851542) · **Deposit:** `Foundations_of_Memory_Field_Physics__A_Field_Theoretic_Model_of_Inward_Time.pdf` · 16 PDF pages · 133,084 bytes · Zenodo MD5 `6056bd7909cb2f40a9b21acf8ebe3421` · SHA-256 of the matching reviewed copy `142bf70488d5d0043598d9a35b5b0c94c8a6572ac622ca2ba045583c020d8ded`.

**Identity and provenance.** The cover names *The Book of Inward Physics · Volume I: Foundations of Memory-Field Physics — A Field-Theoretic Model of Inward Time*, Daniel Jacob Read IV, ĀRU Intelligence Inc., December 2025. The seal page calls it a first edition. Zenodo's longer title and December 8, 2025 publication date are retained as record provenance. The record's separate Created date says December 7 and calls that the first archival publication; the date and wording should be reconciled against a dated source before being changed. The PDF carries an all-rights-reserved notice; open file access is not a reuse license.

## What the PDF contributes

| PDF page | Inspectable content |
|---|---|
| 1 | Cover, field premise, and three schematic previews: potential minima, temporal-collapse manifold, presence versus variance. |
| 2–3 | Section 1 defines a real scalar `μ(x,t)` on flat Minkowski spacetime, the action `S[μ]`, kinetic term, `V(μ)=α(μ²−μ₀²)²`, and the gradient-coupled recursion term `Ω=λμ(∂μ μ)(∂^μ μ)`. |
| 4–6 | Section 2 states the nonlinear field equation, stationary configurations, the proposed collapse trajectory and temporal-momentum conditions, `C(x)=|∂t μ|+β|∂t π|→0`, and a first `R[μ]` notation for a recursion contribution. The effective kinetic prefactor is restricted in the text by `|2λμ|<1`. |
| 6–8 | Section 3 defines another recursion map `R[μ]=μ−λ δS/δμ`, a spatial-coherence quotient `P[μ]`, and a linear stability discussion around `±μ₀`. |
| 8–11 | Section 4 supplies explicitly qualitative diagrams of the field landscape, collapse, iterative map, and presence threshold. |
| 11–14 | Sections 5–8 discuss interpretation, relation to scalar fields and gravitational time dilation, limitations and future work. Section 7 explicitly calls for coupling to geometry, quantization, and an observable interpretation. |
| 15 | Appendix A gives alternative local/nonlocal recursion functionals, a `δ` collapse tolerance and a regularized presence denominator `ε+∫|∇μ|²d³x`, `ε>0`. |
| 16 | Memory-field seal, first-edition date and copyright. |

The main text is an original **classical field-theory proposal** with equations and schematic figures. The PDF does not provide a measured `μ` observable, a numerical simulation, or an empirical validation; those are separate research stages.

## Precise follow-up for a technical edition

1. **Select a recursion formalism.** Page 5 writes `R[μ]≡−λ(∂μ μ)(∂^μ μ)` for a term in the equation. Page 6 uses `R[μ]=μ−λδS/δμ` for an iterative map. Appendix A then offers local and nonlocal `Ω` choices distinct from the gradient coupling in Section 1. A future edition should distinguish the symbol names and state which action, equation, and fixed-point argument belong together.
2. **Specify collapse and stability assumptions.** The double-well minima establish stationary homogeneous candidates, but a general monotone approach and decay of perturbations need boundary/initial conditions and a stability or dissipation argument. Identify the region where the kinetic prefactor stays positive and the sign convention in the linearized equation.
3. **Define the presence domain and threshold.** Section 3 uses an unregularized quotient with numerator `∫μ d³x` and describes divergence when its gradient denominator tends to zero. Appendix A instead uses `∫μ² d³x` over `ε+∫|∇μ|²d³x`, with `ε>0`, so both numerator and denominator differ. The regularized expression does not diverge solely because a finite-domain gradient denominator tends to zero. State the spatial domain, boundary behavior, normalization and intended operational threshold.
4. **Align provenance and relations.** Reconcile the Created-date description with the public publication date; examine any proposed formal Zenodo relation to the narrative Part I and other laws individually, rather than treating related topics as a verified series dependency.

## Independent equation and homogeneous-limit check

Write `X=(∂ₐμ)(∂ᵃμ)` and `K(μ)=1−2λμ`. The main-text density is `L=½KX−α(μ²−μ₀²)²`. Direct differentiation gives `∂L/∂μ=−λX−4αμ(μ²−μ₀²)` and `∂L/∂(∂ₐμ)=K∂ᵃμ`. The Euler–Lagrange equation is therefore `K□μ−λX+4αμ(μ²−μ₀²)=0`, matching the equation printed in Section 2. This validates that algebraic step for the selected main-text action.

A separate allowed limit tests the claimed generic relaxation: set `λ=0`, suppress spatial gradients, and choose `α=μ₀=1`. Then `μ̈+4μ(μ²−1)=0` conserves `E=½μ̇²+(μ²−1)²`. Linearizing about `μ=+μ₀` gives `η̈+8αμ₀²η=0`, an oscillatory mode; the minus sign in Section 3's displayed `□η−U″η` expression does not follow from this limit. This result tests the model's mathematical scope: it does not rule out convergence under additional conditions or terms, but those conditions must be specified.

The [standard-library replay](./volume_i_homogeneous_check.py) uses RK4 with `Δt=0.001`, `μ(0)=1.1`, `μ̇(0)=0` for `t∈[0,10]`. It gives four lower turning points, `μ_min≈0.88881944`, `μ_max=1.1`, `μ(10)≈0.89127345`, and relative energy drift `4.39×10⁻¹³`. These numbers document the specified undamped model computation, not a physical measurement or a general claim about all parameter regimes.

**Published metadata correction, October 25, 2026 Pacific.** The creator now reads `Read IV, Daniel Jacob`, matching the deposited cover. The description names the 16-page first edition, scalar action, potential, gradient coupling, field equation, completion criterion, presence functional, qualitative figures, Appendix A alternatives and Section 7's classical-model limits. The former comma-packed subject is now ten separate links: `Inward Physics`, `memory-density field`, `scalar field theory`, `Lorentz-invariant action`, `inward time`, `symmetry-breaking potential`, `recursion`, `completion manifolds`, `presence functional`, and `field-theoretic model`. Public readback confirmed these fields and the unchanged PDF MD5. The title, Report type, December 8, 2025 publication date, v1.0.0 version, affiliation, Researcher role and all-rights-reserved notice were retained. The conflicting Created-date wording remains in issue #20 for provenance review; no DOI relation, ORCID, rights change, result, or measured validation was inferred.
