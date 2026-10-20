# Third Law equation check — reproducible toy case

This calculation audits the mathematical consequences of the equation printed in [DOI 10.5281/zenodo.17314619](https://doi.org/10.5281/zenodo.17314619). It is **not** evidence that a physical memory field, life, or consciousness arises from it. The [source audit](./third-law-source-audit.md) records the PDF and catalog corrections.

## Prescribed input and exact result

Take `μ(x,t)=1+A exp(-λt) cos(kx)` with `A=0.2`, `λ=0.4`, `k=1`, `β=1`, and `R(x,0)=1`. This is an illustrative prescribed field, not a solution of the addendum's coupled field equation. The Laplacian in one spatial dimension is `-Ak² exp(-λt) cos(kx)`. The proposed Third Law therefore has the exact solution

```text
R(x,t) = exp[-β A k² cos(kx) (1-exp(-λt))/λ]   (λ > 0).
```

At `λ=0`, replace `(1-exp(-λt))/λ` with `t`. The finite-time magnitude of `ln[R/R0]` is bounded by `|β| A k² (1-exp(-λt))/λ` for this chosen input. The bound comes from the decaying prescribed curvature, not an intrinsic saturation mechanism in the proposed law.

## Reproduce

From the repository root, run `python3 artifacts/third_law_check.py`. It uses only Python's standard library. Defaults: `A=0.2, β=1, λ=0.4, T=4, N=40`. The program compares the exact solution with explicit Euler using 40 and 80 steps. Options `--amplitude`, `--beta`, `--decay`, `--time`, and `--steps` allow sensitivity checks.

| Position and curvature | Exact R(4) | Euler 40 | Absolute error | Euler 80 | Absolute error |
|---|---:|---:|---:|---:|---:|
| x=0, negative | 0.670955985 | 0.663912483 | 0.007043501 | 0.667454232 | 0.003501753 |
| x=π/2, zero | 1.000000000 | 1.000000000 | 0 | 1.000000000 | 0 |
| x=π, positive | 1.490410732 | 1.498723590 | 0.008312858 | 1.494569218 | 0.004158486 |

A direct Python check confirmed all three Euler errors decrease when the step count doubles, `β=0` holds R at 1, and constant positive curvature (`λ=0`) yields `R(40)=exp(8)≈2980.96`. The latter is unbounded exponential amplification as time increases, absent additional dynamics. Numerical agreement with a solution of the equation checks the implementation of this toy case; it does not validate the equation against nature.

## What a stronger version needs

Define units and whether R is scalar or vector; specify initial and boundary conditions and a coupled evolution for μ; resolve the tensor index notation; introduce and justify bounded feedback if persistent stability is claimed; and predefine a measured outcome, null, controls, and parameter ranges that distinguish the hypothesis from existing models. Deposit any revised manuscript, code, and raw observations as a new version with an explicit change log.
