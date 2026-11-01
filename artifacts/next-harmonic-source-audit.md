# Next Harmonic: deposited-source and coherence-equation review

**Source:** [The Next Harmonic of Inward Physics, DOI 10.5281/zenodo.18334632](https://doi.org/10.5281/zenodo.18334632), Daniel Jacob Read IV, ĀRU Intelligence Inc. The three-page PDF is dated January 2026; Zenodo published the preprint on 21 January 2026. Reviewed 31 October 2026 Pacific. The deposited PDF is 189,832 bytes; MD5 `49f28566ef404174704dc48f0b233216` matches Zenodo, SHA-256 `74f428a4946c409e1aac2b81649927d57c7e715b780c7eaca7081e740939e2f3`.

## Page map

| PDF page | Deposited contribution |
|---|---|
| 1 | Cover and abstract; defines accumulated registration `A(t)=∫₀ᵗR(τ)dτ`, variance `σ²(A)=σ₀²exp(−κA)`, normalized coherence `C=1−σ²/σ₀²`, critical ignition threshold, and cubic evolution `dC/dt=κC(1−C)(C−Ccrit+ε)`. |
| 2 | Prints a closed-form logistic expression for `C₀>Ccrit`, then a self-sustaining theorem and possible AI, consciousness and planetary implications. No derivation or parameterized simulation accompanies the formula. |
| 3 | Symbolic “Plate I — Eternal Remembrance” and restrictive copyright statement. This plate is an illustration, not a measured trajectory. |

## What the cubic model establishes

Write `q=Ccrit−ε`. For `κ>0` and `0<q<1`, the **printed cubic** has equilibria `C=0,q,1`. Within `0<C<1`, its right-hand side is negative below `q` and positive above `q`. Thus `0` and `1` are attracting from their interior sides and `q` is a separating threshold. An initial `q<C₀<1` increases toward `1` under the stipulated autonomous ODE; it approaches `1` asymptotically rather than reaching it in finite time. If `ε` shifts `q` outside `(0,1)`, the three-regime description changes. This is a rigorous conditional property of the proposed model that can support a clearer theorem.

For the `ε=0` superthreshold case, separation gives the following **implicit exact solution**, with `q=Ccrit`:

`ln[(C−q)/(C^(1−q)(1−C)^q)] − ln[(C₀−q)/(C₀^(1−q)(1−C₀)^q)] = κq(1−q)t`.

This relation captures the cubic threshold. The p. 2 formula `C(t)=1/[1+(1/C₀−1)exp(−κt)]` instead solves `C'=κC(1−C)`. It lacks the factor `C−q`. At illustrative `κ=1`, `q=0.4`, `C₀=0.6`, its initial derivative is `0.24`; the cubic specifies `0.048`. A converged fourth-order integration of the cubic gives `C(5)=0.894746733`, while the printed logistic gives `0.995528123`. The [runnable standard-library check](./next_harmonic_check.py) verifies the initial residual, a step-size comparison and the implicit relation. These are chosen dimensionless parameters, not fitted data.

## Bridge to the paper's registration definition

From the p. 1 definitions `A'=R` and `C=1−exp(−κA)`, differentiation yields `C'=κR(t)(1−C)`. Matching the cubic requires `R(t)=C(C−Ccrit+ε)` wherever `C<1`. The PDF does not define that internal feedback law. If “without external input” means `R=0` after ignition, the definitions give `C'=0`, not continuing amplification. The author can instead define `R` as internally generated registration and derive its feedback equation; that would connect the proposed autonomy to the earlier variance law. The model does not include a perturbation or reset process from which permanence or irreversibility follows.

## Public metadata and review path

The live Zenodo description presents the cubic equation and the p. 2 logistic as a closed-form solution and says variance “collapses permanently.” It does label the work a theoretical mathematical framework without empirical claims. The PDF cover and p. 3 copyright use `Daniel Jacob Read IV`, while the public creator displays `Read, Daniel Jacob` and no ORCID icon. The version field is `Version 1.0 (January 2026)`, rendered as “Version Version 1.0”; one comma-packed subject contains nineteen phrases. Public rights show `© 2026 Daniel Jacob Read IV. All Rights Reserved.`, matching the PDF. No license or related-work DOI is displayed. These observations do not authorize a license or relation change.

A source-grounded Zenodo description correction would retain the cubic and its valid conditional threshold result, replace the claimed logistic solution with the implicit cubic relation or clearly label it as a different simplified equation, and distinguish asymptotic variance decay in the stipulated model from a proven permanent effect. The creator suffix, version label and individual subjects can be reviewed by the record owner. [Issue #29](https://github.com/aruintelligence/aruintelligence/issues/29) tracks the exact theorem, registration bridge, perturbation test and metadata. This audit strengthens the mathematical statement of the author's proposed threshold without claiming an empirical discovery.
