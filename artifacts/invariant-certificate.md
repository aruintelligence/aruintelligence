# A boundedness certificate for the disclosed 1D update

**Source:** [How Memory Fields Fix AI Forgetting](https://doi.org/10.5281/zenodo.18010911), §4.1 and Appendix A. This note proves a property of its explicit numerical update and checks a few synthetic source amplitudes. It is **not** a proof that the proposed scalar μ exists physically.

Let `M = μ_max`, `b = μ₀`, `λ` be relaxation, `D` diffusion, and `A_i ≥ 0` the fixed source. With periodic neighboring cells and `r = D·dt/dx²`, the *unclipped* update printed in the paper can be rearranged as

```text
u_i(next) = [1 - 2r - dt(λ + A_i/M)]·u_i
          + r·u_(i-1) + r·u_(i+1) + dt(λ·b + A_i).
```

If `0 ≤ b ≤ M`, `λ ≥ 0`, `D ≥ 0`, `A_i ≥ 0`, `dt ≥ 0`, and

```text
2D·dt/dx² + dt(λ + max_i A_i/M) ≤ 1,
```

then all coefficients of current cell values are nonnegative. The update is nonnegative when every current cell is nonnegative. For `u_i` and both neighbors at `M`, the next value is `M - dt·λ·(M-b) ≤ M`; the same nonnegative coefficients make this the upper bound for all states in `[0,M]`. Thus **every step remains in `[0,M]` for every initial array in that interval**, and the final `clip(0,M)` is redundant under these sufficient conditions. This is an induction on steps, not a statement about solutions outside the specified discretization.

For the PDF's inclusive `linspace(-10,10,400)` grid used as 400 periodic cells, `D=0.05`, `λ=0.15`, `b=0.10`, `M=2`, and `dt=0.45·dx²/(2D)`. Its source parameter `a=0.25` gives `A_i=a·exp(-x_i²/(2·0.8²))`. The minimum current-cell coefficient is about **0.5468914**, safely positive. The sampled-grid threshold for `a` is about **97.0371** with all other printed parameters fixed. The initial Gaussian is in `[0,2]`, so this certificate covers the published 400-step trajectory and any number of further steps under those fixed conditions.

The [standard-library sweep](./invariant_certificate.py) records [exact JSON output](./invariant_certificate.json):

| Source parameter `a` | Bound holds? | Clipped cell updates in 400 steps | Final mean |
|---:|:---:|---:|---:|
| 0 | Yes | 0 | 0.1684741182 |
| 0.25 (published) | Yes | 0 | 0.2154056632 |
| 50 | Yes | 0 | 0.5754078798 |
| 100 | No | 0 | 0.6109393709 |
| 1000 | No | 11,178 | 0.7130244232 |

Run `python3 artifacts/invariant_certificate.py` from the profile repository root. It checks the published mean against the separate [reference replay](./audit-reaction-diffusion.md), asserts no clipping whenever the sufficient bound holds, and includes one case beyond the bound with no observed clipping and one that clips. The bound is **sufficient, not necessary**: failure at `a=100` does not imply clipping. The `a=1000` count is cell-step events in a deliberately extreme synthetic variant; it is not an observation of any physical process. This certificate depends on the stated positivity and baseline assumptions; negative source or altered discretization needs a fresh analysis.

## What this fixed-source rule retains

Consider two initial arrays `u` and `v` in `[0,M]` evolving with **the same** printed source `A_i`. Their difference has no constant term:

```text
d_i(next) = [1 - 2r - dt(λ + A_i/M)]·d_i
          + r·d_(i-1) + r·d_(i+1).
```

Under the published parameter bound, all three coefficients are nonnegative. Their row sum is `1 - dt(λ + A_i/M) ≤ q = 1 - dt·λ = 0.9983040308 < 1`. Therefore `||u(n)-v(n)||∞ ≤ q^n ||u(0)-v(0)||∞`. With the source fixed, the update is a contraction on the invariant box and has a unique attracting fixed profile. **Differences due only to the initial condition decay**; the persistent spatial pattern is driven by the continuing source. This conclusion applies to this fixed-source toy rule, not to the separate browser animation or every proposed Inward Physics formulation.

The runnable check evolves the published Gaussian and a uniform `0.10` starting array under the same `a=0.25` source. Their maximum separation starts at `1.1995348037`; after 400 steps it is `0.2944123836` (bound `0.6083348588`), and after 4,000 steps it is `0.0000772554` (bound `0.0013499303`). Those finite runs illustrate the analytic result. A claim of persistent information about an initial state would need an additional mechanism, changed forcing, or different assumptions; the printed constant-source update alone does not supply it.
