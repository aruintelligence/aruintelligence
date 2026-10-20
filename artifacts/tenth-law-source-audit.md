# Tenth Law DOI source audit

**Record:** [10.5281/zenodo.18051629](https://zenodo.org/records/18051629) · **metadata republished and publicly read back:** 2026-10-20 Pacific  
**Deposited file:** `The_Tenth_Law_of_Inward_Physics.pdf` · 6 US-letter pages · 294,931 bytes  
**Integrity:** Zenodo MD5 `8409293a5bec1b731b179a6b12e4b7e6`; downloaded SHA-256 `7cb59b7bd9b3a362bfab881b6904a4138ba66798c19a4db6932325df0cf178de`. All six pages were rendered and checked. The PDF metadata names Daniel Jacob Read IV as author. The visible cover says “Archive Edition — October 2025”; Zenodo publication is December 24, 2025, technical creation December 25, and its inherited version label is `v1.0 — Archive Edition`. These are different fields, not evidence of a separate edition.

## Contribution in the deposited PDF

The paper supplies an explicit accounting question for the Eighth and Ninth Law orientation and commitment proposals. It defines a completed memory-density field `μ̂`, Presence `Ω`, path fidelity `Θ`, the local density `ρ_c(x)=|Ω(x)||μ̂(x)|`, and for each agent `I_i=∫_{V_i}ρ_{c,i}(x)dV+η∫_{S_i}|Θ_i(s)|^p ds` (`p>1, η>0`). It distinguishes an interaction parameter `τ` from physical time, postulates `d(Σ_i I_i)/dτ=0` for sealed interaction, and introduces `Φ_meaning` for open-system accounting. It then proposes an alignment-mediated pair exchange, a two-agent construction, a network form, symbolic pseudocode, and three proposed simulation/proxy checks. This is a concrete formal structure for a conservation model, with an especially clear two-agent baseline.

| PDF page | Source content | Evidential status |
|---|---|---|
| 1 | Title, Daniel Jacob Read IV, Archive Edition, abstract and framework. | The claims are a proposed model in the PDF. |
| 2 | Definitions and equations (1)–(3), including `ρ_c`, `I_i`, and sealed conservation. | Equation (3) states the accounting axiom in Definition 10; it is not separately derived from field dynamics. |
| 3 | No-free-coherence consequence, network exchange (5), claimed antisymmetry lemma, open flux (6). | The consequence follows from the axiom. The pair cancellation condition in the lemma needs correction below. |
| 4 | Two-agent equations (7)–(8), three-agent form (9), SymPy-ready pseudocode, diagram and series map. | The explicit opposite two-agent updates sum to zero algebraically. Pseudocode is printed; no execution output is reported. |
| 5 | Sealed, alignment-control and open-coupling test proposals; closure. | A falsifiability program, not completed simulation or proxy measurements. |
| 6 | Copyright and archival notice. | All rights reserved; no reuse license is supplied. |

## Pairwise exchange check

The printed general law (5)/(9) is `dI_i/dτ = Σ_{j≠i} κ A_ij (|Θ_j|−|Θ_i|)`. Set `T_i=|Θ_i|`. The sum of the two terms contributed by one pair `(i,j)` is

`κ A_ij(T_j−T_i) + κ A_ji(T_i−T_j) = κ(A_ij−A_ji)(T_j−T_i).`

It cancels for **symmetric coefficients** `A_ij=A_ji`, or whenever that pair's difference happens to vanish. The printed Lemma 1 instead offers `A_ij=−A_ji` as an example of antisymmetric *flux*; under (5) that makes the two fluxes equal, not opposite. A minimal direct check uses `κ=1, T_1=0, T_2=1, A_12=1, A_21=−1`: `dI_1/dτ=1`, `dI_2/dτ=1`, so `d(I_1+I_2)/dτ=2`. With `A_12=A_21=1`, the updates are `1` and `−1`, giving zero. This algebraic counterexample applies to the asserted general network condition, not to the separately specified two-agent equations (7)–(8), where the second rate is defined as the first rate's negative. One repair is to specify reciprocal/symmetric alignment coefficients in (5)/(9); another is to define a pair flux `F_ij=−F_ji` explicitly and derive each agent's rate from it.

A next revision can also state how the field/path definitions of `I_i` change with `τ` under the exchange rule, and define the measurable or simulated boundary flux `Φ_meaning` before the open-system comparison. These would connect the useful accounting axiom to a fully specified model. The test program on page 5 should be run after the exchange condition is reconciled, with a stated tolerance and negative control. No external physical validation is inferred from a symbolic identity.

## Public metadata correction and retained fields

The public description was republished on October 20, 2026 Pacific to lead with the functional, sealed/open accounting, two-agent algebra, network proposal, pseudocode, and test plan. It calls the conservation statement an axiom and names the network consistency check without claiming a completed simulation or measurement. The creator changed from `Read, Daniel Jacob` to `Read IV, Daniel Jacob`, matching cover, PDF author metadata, and copyright page; existing affiliation, Researcher role and ORCID `0009-0000-6133-1872` were retained. The single comma-joined keyword became twelve individually indexed source-grounded terms. The existing copyright field was already supported by page 6 and was retained.

Public readback confirmed description, creator, twelve subjects, rights, and October 20, 2026 modified date. The title, PDF and MD5, Report type, English, December 24 publication date, Zenodo publisher, version `v1.0 — Archive Edition`, concept DOI `10.5281/zenodo.18051628`, and empty related works remained. No link to Eighth or Ninth DOI was bulk-created, and no new license or observation was added.
