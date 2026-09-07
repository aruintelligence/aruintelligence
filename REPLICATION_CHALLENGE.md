# ĀRU Independent Replication Challenge

ĀRU Intelligence invites independent engineers, researchers, students, accessibility specialists, and skeptical reviewers to test the public artifacts below.

The goal is not agreement. The goal is inspectable evidence.

## Replication tracks

| Project | Baseline procedure | Useful evidence |
|---|---|---|
| [ĀML Core](https://github.com/aruintelligence/aml-core) | Run `npm test`, then compile `examples/transmission-061.aml` | Environment, commit SHA, test result, generated artifacts, parser counterexamples |
| [ĀRU Remembrance Field](https://github.com/aruintelligence/aru-remembrance-field) | Open `index.html`; exercise input, persistence, and threshold transitions | Browser/version, steps, console output, accessibility findings |
| [Inward Mathematics Simulator](https://github.com/aruintelligence/inward-mathematics-simulator) | Open `index.html`; vary remembrance, shock, and observer parameters | Inputs, expected/actual behavior, screenshots, numerical anomalies |
| [Inward AGI Remembrance Engine](https://github.com/aruintelligence/inward-agi-remembrance-engine) | Open the v11 HTML; test persistence, deduplication, retrieval, and veto states | Browser/version, exact inputs, storage behavior, failures |
| [Kairos Echo](https://github.com/aruintelligence/kairos-echo-reflection-tool) | Run 500 steps with seed 42 twice | Python version, outputs, determinism result, edge cases |
| [Divine Whisper Ecosystem](https://github.com/aruintelligence/divine-whisper-ecosystem) | Review the lineage map against the linked repositories | Missing stages, incorrect claims, dependency gaps, runnable/non-runnable classifications |

## Submission standard

Include:

1. Repository and commit or release tested.
2. Operating system, browser, runtime, and dependency versions.
3. Exact commands, inputs, configuration, and seed.
4. Expected behavior.
5. Actual behavior.
6. Logs, output, screenshots, or minimal reproduction.
7. Interpretation limits and unresolved questions.

Open an issue in the tested repository. Negative findings and failed replications are welcome when documented carefully.

## What counts as progress

- A confirmed reproduction
- A reproducible failure
- A parser or numerical counterexample
- An accessibility defect
- A security report submitted privately
- An independently proposed evaluation method
- A documentation correction backed by the implementation

Independent participation must remain independent. ĀRU Intelligence will not manufacture endorsements, stars, citations, or validation.
