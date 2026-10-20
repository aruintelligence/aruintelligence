# Receipt boundary challenge: two implementations, ten cases

This challenge replays the [Remembrance Field](https://github.com/aruintelligence/aru-remembrance-field) question receipt with the repository's existing [Node batch auditor](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/tools/audit-evidence-batch.cjs) and [independent Python batch auditor](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/tools/independent-evidence-batch.py). The synthetic inputs are derived locally from the public example; no private data is needed. This exercises receipt consistency, not the proposed physics.

## Reproduce

```sh
git clone https://github.com/aruintelligence/aru-remembrance-field.git
cd aru-remembrance-field
git checkout 6238cfdae41adbc6ec858161eaa965573be6114d
python3 /path/to/profile-checkout/artifacts/challenge_receipts.py "$PWD"
```

The [challenge script](./challenge_receipts.py) accepts only that pinned commit, never modifies its checkout, creates isolated temporary JSON copies, invokes both checkers, prints JSON, and exits nonzero if a verdict, exit code, or expected checkpoint rejection differs. The [recorded output](./challenge_receipts.json) is the run from 2026-10-20 UTC. Re-run it with a local checkout of this profile repository as `/path/to/profile-checkout`.

| Synthetic case | Node | Python | Meaning |
|---|---|---|---|
| Original receipt, baseline, checkpoint | MATCH | MATCH | The supplied example is consistent under both implementations. |
| Recorded answer `teal` → `blue` | FAIL | FAIL | Answer disagrees with the supplied assertion. |
| Citation `#1` → `#2` | FAIL | FAIL | Citation disagrees with recomputed sources. |
| Receipt source status active → superseded | FAIL | FAIL | Recorded answer no longer follows the supplied records. |
| Receipt source timestamp +1 | DIFFER | DIFFER | Answer still computes, but the full snapshot differs from the reference. |
| Duplicate top-level `version` name | FAIL | FAIL | Ambiguous JSON intake is rejected. |
| Baseline value changed without checkpoint | DIFFER | DIFFER | Full snapshot no longer equals the saved receipt. |
| Baseline changed with old checkpoint | Fatal checkpoint rejection | Fatal checkpoint rejection | The digest no longer matches the supplied reference. |
| Checkpoint digest changed | Fatal checkpoint rejection | Fatal checkpoint rejection | The digest no longer matches the supplied reference. |
| Receipt, baseline, and checkpoint consistently rewritten to `blue` | MATCH | MATCH | Consistency alone cannot determine whether the assertion is true or who made it. |

`FAIL` means an invalid receipt or ambiguous input; `DIFFER` means a valid receipt whose full snapshot differs from the supplied reference; “fatal checkpoint rejection” means the auditors stopped before producing a per-receipt report. The challenge captures both exit codes (0 for `MATCH`, 1 for the other cases), and the two fatal error messages in its JSON output. All 20 observed implementation/case verdicts and exit codes met the declared expectations at the pinned commit.

The coordinated rewrite is an intentional negative control on *provenance*. A hash can bind data to other supplied data. It cannot itself make the underlying claim true or establish independent custody. A commercial evaluation should specify its capture, identity, custody, privacy, and threat assumptions before treating an export as attestation. The [one-receipt guide](./receipt-review.md) shows the smallest manual replay; [issue #81](https://github.com/aruintelligence/aru-remembrance-field/issues/81) tracks remaining product review.
