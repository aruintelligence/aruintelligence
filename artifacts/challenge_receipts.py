#!/usr/bin/env python3
"""Run bounded synthetic receipt mutations against two existing public checkers.

Usage: python3 artifacts/challenge_receipts.py /path/to/aru-remembrance-field
No network or third-party packages; the original checkout is never modified.
"""

import copy
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

PINNED = "6238cfdae41adbc6ec858161eaa965573be6114d"
CASES = {
    "original": "MATCH",
    "answer_changed": "FAIL",
    "citation_changed": "FAIL",
    "record_status_changed": "FAIL",
    "record_time_changed": "DIFFER",
    "duplicate_json_name": "FAIL",
    "baseline_changed": "DIFFER",
    "baseline_changed_with_old_checkpoint": "FATAL",
    "checkpoint_changed": "FATAL",
    "coordinated_rewrite": "MATCH",
}


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def checkpoint_digest(baseline):
    canonical = []
    for r in baseline["records"]:
        canonical.append([r["id"], r["key"], r["value"], r["time"], r["status"],
                          [r["imported"]] if "imported" in r else []])
    ledger = hashlib.sha256(compact(["aru-ledger-commitment-1", canonical])).hexdigest()
    return hashlib.sha256(compact(["aru-evidence-ledger-checkpoint-1", ledger,
                                   baseline["next_source_id"]])).hexdigest()


def run(checkout, temp, case, receipt, baseline, checkpoint, duplicate=False):
    root = pathlib.Path(temp)
    receipt_file, baseline_file, checkpoint_file = (root / (case + suffix) for suffix in
                                                    ("-receipt.json", "-baseline.json", "-checkpoint.json"))
    raw = compact(receipt)
    if duplicate:
        raw = raw.replace(b'"version":1,', b'"version":0,"version":1,', 1)
    receipt_file.write_bytes(raw)
    baseline_file.write_bytes(compact(baseline))
    if checkpoint is not None:
        checkpoint_file.write_bytes(compact(checkpoint))
    outputs = {}
    for implementation, command in (
        ("node", ["node", "tools/audit-evidence-batch.cjs"]),
        ("python", [sys.executable, "tools/independent-evidence-batch.py"]),
    ):
        argv = command + [str(baseline_file), str(receipt_file)]
        if checkpoint is not None:
            argv += ["--checkpoint", str(checkpoint_file)]
        argv += ["--json"]
        result = subprocess.run(argv, cwd=checkout, capture_output=True, text=True,
                                timeout=15, check=False)
        try:
            report = json.loads(result.stdout)
            verdict = report["receipts"][0]["verdict"]
        except (json.JSONDecodeError, KeyError, IndexError, TypeError):
            verdict = "FATAL"
        outputs[implementation] = {"verdict": verdict, "exit_code": result.returncode,
                                   "stderr": result.stderr.strip()[:240]}
    return outputs


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 artifacts/challenge_receipts.py /path/to/aru-remembrance-field")
    checkout = pathlib.Path(sys.argv[1]).resolve()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=checkout, text=True).strip()
    if revision != PINNED:
        raise SystemExit(f"Checkout must be pinned at {PINNED}; found {revision}")
    research = checkout / "research"
    original = [json.loads((research / filename).read_text(encoding="utf-8")) for filename in (
        "example-evidence-receipt.json", "example-evidence-reference-baseline.json",
        "example-evidence-ledger-checkpoint.json")]
    observations = {}
    with tempfile.TemporaryDirectory(prefix="receipt-challenge-") as temp:
        for name, expected in CASES.items():
            receipt, baseline, checkpoint = copy.deepcopy(original)
            if name == "answer_changed":
                receipt["answer"]["value"] = "blue"
            elif name == "citation_changed":
                receipt["answer"]["sources"] = [2]
            elif name == "record_status_changed":
                receipt["records"][0]["status"] = "superseded"
            elif name == "record_time_changed":
                receipt["records"][0]["time"] += 1
            elif name in ("baseline_changed", "baseline_changed_with_old_checkpoint"):
                baseline["records"][0]["value"] = "blue"
            elif name == "checkpoint_changed":
                checkpoint["sha256"] = "0" * 64
            elif name == "coordinated_rewrite":
                receipt["records"][0]["value"] = "blue"
                receipt["answer"]["value"] = "blue"
                baseline["records"][0]["value"] = "blue"
                checkpoint["sha256"] = checkpoint_digest(baseline)
            # The baseline-only variant omits the checkpoint, so it tests exact
            # snapshot comparison without making the earlier digest inconsistent.
            if name == "baseline_changed":
                checkpoint = None
            outputs = run(checkout, temp, name, receipt, baseline, checkpoint,
                          duplicate=name == "duplicate_json_name")
            observations[name] = {"expected": expected, **outputs}
    print(json.dumps({"format": "inward-receipt-boundary-challenge", "revision": revision,
                      "cases": observations}, indent=2))
    if any(out["verdict"] != case["expected"] or
           out["exit_code"] != (0 if case["expected"] == "MATCH" else 1) or
           (case["expected"] == "FATAL" and "checkpoint differs" not in out["stderr"])
           for case in observations.values()
           for key, out in case.items() if key in ("node", "python")):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
