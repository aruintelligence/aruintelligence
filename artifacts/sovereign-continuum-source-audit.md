# Sovereign Continuum (Document II): deposited-source and equivalence-class review

**Source:** [Thirteenth Law — Document II, DOI 10.5281/zenodo.18125773](https://doi.org/10.5281/zenodo.18125773), Daniel Jacob Read IV, ĀRU Intelligence Inc. The nine-page v1.1 PDF is dated October 2025; Zenodo publicly lists 1 January 2026. Reviewed 31 October 2026 Pacific against the deposit (323,410 bytes; MD5 `07a93c432ecd4617b5f17d619a346fcf`, matching Zenodo; SHA-256 `60cec717b1c412040377ed1f7b579124ead3ed8dfff1e15ee1c0d7507b426fba`).

## Page map

| PDF page | Deposited contribution |
|---|---|
| 1–2 | Cover, abstract, five constraints inherited from Document I, and contents. The cover calls this a rigorous definitional volume, not a measured identity experiment. |
| 3 | Defines a completed system and four conditions A1–A4 for admissible iteration: closure, no global time, unity, and no covert substitution. |
| 4 | Defines finite-chain A-reachability, mutual A-equivalence, Sovereign Continuum `Σ(M)=[M]∼A`, and an invariant representation tuple `S=(K,U,Π)`. Proposition 1 correctly makes mutual reachability an equivalence relation when zero-length chains and concatenation are allowed. |
| 5 | States Law XIII as class conservation under every admissible iteration. Proposition 2's proof sketch invokes reverse reachability from `I(M)` to `M`, while A1–A4 do not expressly require that reverse path. |
| 6 | Defines mismatch `D=1[S(M1)≠S(M2)]`, drift norm, substitution certificate and fragmentation condition. The text says identity holds iff `D=0` and the bridge is admissible. |
| 7 | Four-step audit protocol and explicit limits: no immortality, soul, consciousness doctrine, dualism or violation of known physics is claimed. |
| 8–9 | Terminal logical schematic and colophon with All Rights Reserved copyright. The schematic is a conceptual diagram, not measured evidence. |

## Exact logical boundary and a repair

The mutual-reachability definition has a useful formal core. If `M0→M1` is an A-admissible step, then `M0⇝A M1`. **Class conservation additionally needs** `M1⇝A M0`. A1–A4 on PDF p. 3 do not explicitly require an inverse or reverse path. The p. 5 proof supplies “reversibility at the identity level” in prose but does not state it as an admissibility condition. The [standard-library finite-graph check](./sovereign_continuum_check.py) constructs a forward-only pair with identity/zero-length chains. Their mutual-reachability equivalence classes differ even though a forward step exists; adding an admissible reverse edge makes the classes equal.

A clean technical revision could add a fifth admissibility axiom: for every admissible `I:M→M′`, there is an admissible reverse chain `M′⇝A M`. Then Proposition 2 follows immediately. Alternatively, the author could redefine the equivalence relation as the symmetric closure of admissible reachability, but that changes which one-way transformations count as identity-preserving and should be motivated explicitly. These are conditional mathematical choices within the author's proposed identity framework.

The p. 6 tuple mismatch has a separate boundary. Invariance of `S` along admissible steps implies `S(M1)≠S(M2)` is a valid certificate that the configurations are not in the same class. **Equality** of `S` does not prove equality of classes unless the tuple is also complete: `S(M1)=S(M2) ⇒ Σ(M1)=Σ(M2)`. The PDF says this holds “when complete” but does not prove completeness or give algorithms for `K,U,Π`. The same forward-only example assigns identical tuples to two distinct classes, so `D=0` is a false positive for the printed “iff” identity criterion. An audit-grade implementation needs a domain, computable signatures, collision analysis, and either a completeness proof or an explicit “inconclusive when D=0” result.

The model's three named failure modes are useful review categories; their stated exhaustiveness also needs a domain argument. For example, a failure of reverse reachability may occur without observed drift of the chosen tuple, substitution behavior or multiple claimant outputs in the definitions as written.

## Public metadata and next edition

Zenodo currently labels this a Report, version `v1.1 — Rigorous Canonical Edition`, creator `Read, Daniel Jacob` with ORCID `0009-0000-6133-1872`, one long comma-packed subject value, and restrictive copyright with no license listed. The PDF cover and colophon use `Daniel Jacob Read IV` and call the version `v1.1 (Rigorous Canonical Definition — Eternal Edition)`. The record description calls `Σ` a conserved observable and the audit criteria operational; those are goals of the formalism until reverse-admissibility and complete, computable signatures are supplied. The PDF names Document I as a predecessor, but no Zenodo related-work field is present; a relation should be reviewed one DOI at a time.

A source-grounded description would present this as a proposed equivalence-class identity definition, state the precise additional assumptions under which conservation follows, and describe the tuple as a proposed audit interface. The rights and deposited PDF should be retained. [Issue #30](https://github.com/aruintelligence/aruintelligence/issues/30) tracks the axiom, implementation and individual metadata choices. This audit checks the formal definitions and a finite counterexample, not a physical identity observable or an empirical AI continuity result.

## Published metadata readback · 1 November 2026 Pacific

The public record now scopes conservation to its stated formal conditions, displays creator `Read IV, Daniel Jacob` with existing ORCID, eight separate subjects and `Continues` Document I DOI `10.5281/zenodo.18113174`. Version `v1.1 — Rigorous Canonical Edition`, restrictive rights, publication date and PDF MD5 `07a93c432ecd4617b5f17d619a346fcf` remain unchanged. The PDF's longer colophon version wording remains a provenance question. The reverse-admissibility and tuple-completeness findings above remain open; this edit does not claim they were repaired in the PDF.
