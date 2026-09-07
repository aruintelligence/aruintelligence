# Reproducibility Framework

ĀRU Intelligence publishes public prototypes so others can inspect, run, challenge, and extend the work. This framework defines the evidence expected behind project-maturity language.

## Maturity ladder

| Level | Minimum evidence |
|---|---|
| **Concept** | Research question, scope, terminology, and explicit hypotheses |
| **Prototype** | Inspectable implementation, run instructions, dependencies, expected behavior, and known limitations |
| **Reproducible experiment** | Versioned environment, deterministic input or seed where possible, evaluation procedure, and recorded output |
| **Observed result** | Methods, conditions, raw or derived data, analysis, and uncertainty |
| **Independently replicated** | Reproduction by an unaffiliated party with attributable methods and results |
| **Production candidate** | Automated tests, security review, operational monitoring, change control, and deployment documentation |

No current maturity label should be read as a claim that a prototype is production-ready, conscious, clinically useful, or scientifically validated.

## Reproduction checklist

A strong reproduction record includes:

1. Repository, release, tag, or commit SHA.
2. Operating system, runtime, and dependency versions.
3. Exact command or interaction sequence.
4. Input values, configuration, and random seed.
5. Expected output and acceptance criteria.
6. Actual output, including failures.
7. Hardware or browser assumptions.
8. Known limitations and sources of uncertainty.

## Evidence boundaries

- **Implemented** means code exists; it does not mean the design is effective.
- **Simulated** means behavior occurred inside a defined model; it does not establish a real-world law.
- **Observed** requires recorded methods and results.
- **Validated** requires an appropriate validation process and should identify who performed it.
- Symbolic labels such as *remembrance*, *witness*, *guardian*, and *coherence* identify modeled concepts unless a publication explicitly defines and measures them.

## How to contribute evidence

Open an issue or pull request in the relevant repository with the commit tested, environment, procedure, result, and artifacts. Negative results, counterexamples, accessibility findings, and failed replications are welcome when documented carefully.

For security vulnerabilities, follow the [security policy](./SECURITY.md) instead of publishing exploit details.
