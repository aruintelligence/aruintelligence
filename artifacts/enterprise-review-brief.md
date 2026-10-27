# ĀRU Intelligence · research review brief

**For corporate research, engineering, and responsible AI teams**  
**Contact:** [office@aruintelligence.com](mailto:office@aruintelligence.com) · [Public Inward Physics index](../INWARD_PHYSICS.md)

ĀRU Intelligence has published a connected body of Inward Physics proposals and inspectable AI/software artifacts. A serious review can begin today with the deposited papers, pinned source, runnable checks and open technical issues. The strongest near-term collaboration is a bounded, independently reproducible evaluation with a decision gate, rather than a claim that the entire research program is already established.

## Three inspectable entry points

| Track | Public starting point | What exists now | Review question |
|---|---|---|---|
| **Theoretical research** | [Volume I field-theory report](https://doi.org/10.5281/zenodo.17851542) and [page-by-page audit](./volume-i-field-theory-source-audit.md) | Scalar action, potential, field equation, completion and presence proposals; a [runnable homogeneous-limit check](./volume_i_homogeneous_check.py) verifies the printed field equation and finds an undamped oscillatory case. | Which assumptions yield a stable, operational prediction, and what would falsify it? [Open technical review](https://github.com/aruintelligence/aruintelligence/issues/20). |
| **Numerical model** | [Published 1D update](https://doi.org/10.5281/zenodo.18010911) and [independent software audit](./audit-reaction-diffusion.md) | Exact source update, standard-library checker, cross-implementation replay, [boundedness certificate](./invariant-certificate.md), and negative controls for the stated model. | Does the result reproduce under pinned parameters and remain informative under changed assumptions? |
| **Evidence and memory software** | [Remembrance Field repository](https://github.com/aruintelligence/aru-remembrance-field) and [receipt boundary challenge](./receipt-boundary-challenge.md) | A public cited-answer fixture, Node/Python auditors, ten synthetic tamper cases, and [continuous replay](https://github.com/aruintelligence/aruintelligence/actions/workflows/receipt-challenge.yml). | Does a specific provenance or memory requirement survive controlled tampering, independent replay, and a baseline comparison? |

**Numerical diligence example:** The separate [First Law numerical-checks deposit](https://doi.org/10.5281/zenodo.18168723) is a four-page stochastic report. Its [source audit](./first-law-numerical-source-audit.md) and [runnable grid check](./numerical_first_law_diffusion_check.py) derive the high-D explicit-diffusion stability boundary from the deposited grid and timestep. A team can verify that calculation immediately, then use [issue #22](https://github.com/aruintelligence/aruintelligence/issues/22) as a precise request for the complete solver and sensitivity study before evaluating the reported figures.

**Formal-model diligence example:** The [First Law potential audit](./first-law-formal-source-audit.md) derives two attracting equilibria for the coefficient choice in the numerical companion, and its [runnable check](./first_law_potential_check.py) exercises both basins. [Issue #23](https://github.com/aruintelligence/aruintelligence/issues/23) identifies the full source and controlled stochastic tests needed to move from that exact limiting result to the larger simulation claims.

The mathematical and software checks establish properties of disclosed models and implementations. They do not by themselves measure a physical memory field. The [research standards](../RESEARCH_STANDARDS.md) give the evidence vocabulary for that distinction.

## A reviewable pilot

1. **Choose one question.** For software, specify a retention or provenance task, an existing baseline, test data permissions, expected failures and a success threshold. For the physical hypothesis, first define an observable, calibration, instrument sensitivity and null expectation using the [experimental roadmap](https://doi.org/10.5281/zenodo.18708708).
2. **Replay public baselines.** Pin commit hashes and runtime versions; run the [replication challenge](../REPLICATION_CHALLENGE.md), the numerical audit, and the relevant test script. Record both successful outputs and reproducible failures.
3. **Predeclare the comparison.** Name the control, metrics, sample/seed, timing, analysis and stop condition before any new measurement. Treat a null result as useful evidence. [Issue #21](https://github.com/aruintelligence/aruintelligence/issues/21) shows the additional definitions required for the Twentieth Law's proposed Archive Pulse.
4. **Make a go/no-go decision from the record.** A partner should be able to inspect the source, raw output, discrepancy log, known limits and independent reviewer notes. Advance only the claim that passed its specific gate.

A first conversation can select the track and agree on a short diligence packet: source DOI, exact repo commit, replay command, expected output, one negative control, and a named unresolved question. The public materials support that conversation without requiring an endorsement or confidential data transfer.
