# Remembrance Field receipt review

This is a ten-minute, local software review of the [public Remembrance Field](https://github.com/aruintelligence/aru-remembrance-field). It checks a source-cited answer against the supplied ledger and a separately supplied digest. It does **not** establish that the user's original claim is true, that the ledger came from a particular person, or that the proposed scalar field μ is physical.

## Replay the public example

The observations below used repository commit [`6238cfdae41adbc6ec858161eaa965573be6114d`](https://github.com/aruintelligence/aru-remembrance-field/commit/6238cfdae41adbc6ec858161eaa965573be6114d), Node `v24.19.0`, and the repository's [verifier](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/tools/verify-evidence-receipt.cjs), [example receipt](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/research/example-evidence-receipt.json), [reference baseline](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/research/example-evidence-reference-baseline.json), and [ledger checkpoint](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/research/example-evidence-ledger-checkpoint.json). The verifier loads its answer model from `index.html` in that checkout; pinning the commit holds those rules fixed.

```sh
git clone https://github.com/aruintelligence/aru-remembrance-field.git
cd aru-remembrance-field
git checkout 6238cfdae41adbc6ec858161eaa965573be6114d
node tools/verify-evidence-receipt.cjs \
  research/example-evidence-receipt.json \
  research/example-evidence-reference-baseline.json \
  research/example-evidence-ledger-checkpoint.json
```

Observed exit code `0`:

```text
MATCH: known; 1 supplied records; 1 cited sources; scope full-supplied-snapshot; reference exact-full-snapshot
CHECKPOINT MATCH: the supplied reference ledger matches the separately provided digest.
Local model SHA-256: 35a50422c5655d47a1e6c8a16e58847a33dbed84f9f3bfa53738b4af61fdadb7
This checks supplied records or the explicit matching baseline, not their origin or factual truth.
```

## Change the answer and check rejection

The public synthetic fixture says the favorite color is `teal`. Change only the *recorded answer* to `blue` in a copy, leaving the underlying assertion, baseline, and checkpoint untouched:

```sh
python3 -c 'import json,pathlib; p=pathlib.Path("research/example-evidence-receipt.json"); x=json.loads(p.read_text()); x["answer"]["value"]="blue"; pathlib.Path("/tmp/inward-receipt-tampered.json").write_text(json.dumps(x))'
node tools/verify-evidence-receipt.cjs \
  /tmp/inward-receipt-tampered.json \
  research/example-evidence-reference-baseline.json \
  research/example-evidence-ledger-checkpoint.json
```

Observed exit code `1` and stderr:

```text
FAIL: Invalid receipt: recorded answer does not match the local model and supplied records
```

The positive run checks an answer against the local rules and the complete supplied snapshot, then checks the reference ledger against the separately supplied digest. The negative run shows this specific answer substitution is caught. A digest supplied alongside a ledger is a consistency check, not a trusted external attestation; both can be replaced together. Real deployments would need a trusted capture and key or independent custody if origin matters. Neither run tests private user data, general security, or physical predictions.

## A buyer's next review

| Review question | Public inspection point | What remains to establish |
|---|---|---|
| Can a user inspect cited local answers? | [Live field](https://aruintelligence.github.io/aru-remembrance-field/) and [evidence ledger README](https://github.com/aruintelligence/aru-remembrance-field#evidence-memory-recall-with-sources) | Usability with representative tasks and users. |
| Does an exported receipt replay? | The pinned verifier and commands above. | A separate implementation and larger adversarial fixture set. |
| Is local state handled as described? | [README storage disclosure](https://github.com/aruintelligence/aru-remembrance-field/blob/6238cfdae41adbc6ec858161eaa965573be6114d/README.md#L108-L115) and source. | Browser and device threat review; privacy tests for an intended product. |
| Are the rights clear? | [MIT license](https://github.com/aruintelligence/aru-remembrance-field/blob/main/LICENSE) and [README marks notice](https://github.com/aruintelligence/aru-remembrance-field#license). | Confirm rights to any brand, data, and bundled dependencies before commercial use. |

The receipt workflow is an inspectable software feature. It is separate from the [reaction–diffusion numerical audit](./audit-reaction-diffusion.md) and the [experimental roadmap](https://doi.org/10.5281/zenodo.18708708), which have different questions and evidence standards.
