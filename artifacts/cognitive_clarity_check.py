"""Exact limiting-case checks for DOI 10.5281/zenodo.18912791.

Uses illustrative dimensionless parameters, not fitted or observed data.
Run: python3 artifacts/cognitive_clarity_check.py
"""

from math import exp, isclose, log


def attention(t: float, source: float, decay: float) -> float:
    """A(0)=0, A'=source-decay*A for constant source and positive decay."""
    return source / decay * (1 - exp(-decay * t))


def integrated_attention(t: float, source: float, decay: float) -> float:
    return source / decay * (t - (1 - exp(-decay * t)) / decay)


def threshold_time(
    source: float, decay: float, suppression: float,
    baseline_variance: float, target_variance: float,
) -> float | None:
    """First crossing of the PDF's stipulated variance threshold; None if unreachable."""
    critical = log(baseline_variance / target_variance) / suppression
    ceiling = source / decay
    if critical >= ceiling:
        return None  # Equality is only an asymptotic approach.
    return -log(1 - critical / ceiling) / decay


def main() -> None:
    source, decay, suppression = 0.2, 0.5, 2.0
    baseline, target = 1.0, 0.5
    critical = log(baseline / target) / suppression
    crossing = threshold_time(source, decay, suppression, baseline, target)
    assert crossing is not None
    assert isclose(attention(crossing, source, decay), critical, abs_tol=1e-12)
    assert isclose(baseline * exp(-suppression * attention(crossing, source, decay)), target, abs_tol=1e-12)
    assert threshold_time(0.1, decay, suppression, baseline, target) is None

    t = 2.0
    a = attention(t, source, decay)
    integral = integrated_attention(t, source, decay)
    printed_variance = baseline * exp(-suppression * a)
    # If D(0)^2=baseline and variance is identified with D^2, the PDF's
    # separate ODE D'=-suppression*A*D implies this variance instead.
    ode_variance = baseline * exp(-2 * suppression * integral)
    assert not isclose(printed_variance, ode_variance, rel_tol=1e-6)
    assert isclose(integral, source / decay * (t - a / source), abs_tol=1e-12)

    print(f"attention ceiling = {source / decay:.9f}")
    print(f"stipulated threshold A_c = {critical:.9f}; crossing t = {crossing:.9f}")
    print("lower constant source 0.1: no finite threshold crossing")
    print(f"at t=2: A={a:.9f}; integral A dt={integral:.9f}")
    print(f"printed variance law={printed_variance:.9f}; D-ODE squared={ode_variance:.9f}")
    print("Checks passed: threshold crossing, unreachable case, distinct variance laws")


if __name__ == "__main__":
    main()
