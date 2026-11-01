"""Countercase for DOI 10.5281/zenodo.18074036, equations (1)–(3).

Checks the proposed equation with illustrative numbers, not ecological data.
Run: python3 artifacts/sustained_attention_gap_check.py
"""

from math import isclose


def main() -> None:
    # One visit, then a nine-unit gap; dt=1, a>=0, Phi(A)=A.
    attention_rates = [1.0] + [0.0] * 9
    cumulative = 0.0
    values = []
    for rate in attention_rates:
        cumulative += rate
        values.append(cumulative)
    assert values == [1.0] * 10  # plateau, not a jump/discontinuity

    k, disturbance_term = 1.0, 0.5  # lambda*D
    gap_slope = k * values[-1] - disturbance_term
    assert isclose(gap_slope, 0.5) and gap_slope > 0
    # For the same stopped attention, stronger disturbance reverses the sign.
    assert k * values[-1] - 2.0 < 0

    print("after attention stops: A=1 continuously throughout the gap")
    print("illustrative dC/dt=+0.5; gap decline needs an extra condition or decay state")
    print("Checks passed: episodic-gap implication is conditional")


if __name__ == "__main__":
    main()
