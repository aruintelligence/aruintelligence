"""Exact schedule check for DOI 10.5281/zenodo.18091788 (proposed model).

This tests an algebraic implication of the PDF's stated exponential law.
It is not an experiment or a reproduction of any reported measurements.
Run: python3 artifacts/information_registration_probes_check.py
"""

from math import exp, isclose


def trajectory(rates: list[float], kappa: float = 0.1) -> list[float]:
    accumulated = 0.0
    variances = []
    for rate in rates:
        assert rate >= 0
        accumulated += rate  # one unit of time per step
        variances.append(exp(-kappa * accumulated))
    return variances


def main() -> None:
    low = trajectory([1.0] * 10)
    early_pulse = trajectory([10.0] + [0.0] * 9)
    late_pulse = trajectory([0.0] * 9 + [10.0])

    assert all(isclose(path[-1], exp(-1.0)) for path in (low, early_pulse, late_pulse))
    assert early_pulse[0] < low[0] < late_pulse[0]
    # Once the pulse has registered A=10, R=0 leaves A fixed; the printed
    # accumulation law has no erasure or rebound term.
    assert isclose(early_pulse[0], early_pulse[-1])

    print("equal A=10: all terminal variance ratios = e^-1")
    print("early burst suppresses sooner; late burst suppresses later")
    print("no R or loss after registration: no rebound in the printed law")
    print("Checks passed: timing and erasure boundaries of the proposed equation")


if __name__ == "__main__":
    main()
