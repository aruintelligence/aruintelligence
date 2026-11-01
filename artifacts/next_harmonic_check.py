"""Exact model checks for DOI 10.5281/zenodo.18334632.

The parameter values are illustrative and dimensionless. No AI, physiological,
or physical-field observation is modeled here.
Run: python3 artifacts/next_harmonic_check.py
"""

from math import exp, isclose, log


def cubic_rhs(c: float, kappa: float, threshold: float, epsilon: float = 0.0) -> float:
    return kappa * c * (1 - c) * (c - threshold + epsilon)


def printed_logistic(t: float, c0: float, kappa: float) -> float:
    return 1 / (1 + (1 / c0 - 1) * exp(-kappa * t))


def rk4(t: float, c0: float, dt: float, kappa: float, threshold: float) -> float:
    steps = round(t / dt)
    assert isclose(t, steps * dt)
    c = c0
    for _ in range(steps):
        k1 = cubic_rhs(c, kappa, threshold)
        k2 = cubic_rhs(c + dt * k1 / 2, kappa, threshold)
        k3 = cubic_rhs(c + dt * k2 / 2, kappa, threshold)
        k4 = cubic_rhs(c + dt * k3, kappa, threshold)
        c += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return c


def implicit_log_ratio(c: float, q: float) -> float:
    """Exact separated cubic solution for q<C<1, epsilon=0."""
    return log(c - q) - (1 - q) * log(c) - q * log(1 - c)


def main() -> None:
    kappa, q, c0 = 1.0, 0.4, 0.6
    assert cubic_rhs(0.2, kappa, q) < 0 < cubic_rhs(0.6, kappa, q)
    assert all(cubic_rhs(c, kappa, q) == 0 for c in (0, q, 1))
    cubic_at_start = cubic_rhs(c0, kappa, q)
    logistic_at_start = kappa * c0 * (1 - c0)
    assert not isclose(cubic_at_start, logistic_at_start)

    t = 5.0
    integrated = rk4(t, c0, 0.001, kappa, q)
    integrated_coarse = rk4(t, c0, 0.002, kappa, q)
    assert isclose(integrated, integrated_coarse, abs_tol=1e-11)
    implicit_change = implicit_log_ratio(integrated, q) - implicit_log_ratio(c0, q)
    assert isclose(implicit_change, kappa * q * (1 - q) * t, abs_tol=1e-11)

    # The PDF also defines A'=R and C=1-exp(-kappa*A). By differentiation,
    # C'=kappa*R*(1-C); matching the cubic requires R=C*(C-q) for epsilon=0.
    required_internal_registration = c0 * (c0 - q)
    assert isclose(kappa * required_internal_registration * (1 - c0), cubic_at_start)
    assert cubic_at_start > 0  # but R=0 would instead give C'=0.

    print(f"q={q:g}, C0={c0:g}, kappa={kappa:g}: cubic C'(0)={cubic_at_start:.9f}")
    print(f"printed logistic C'(0)={logistic_at_start:.9f}")
    print(f"at t=5: cubic C={integrated:.9f}, printed logistic C={printed_logistic(t,c0,kappa):.9f}")
    print(f"exact implicit log-ratio change={implicit_change:.9f}, expected={kappa*q*(1-q)*t:.9f}")
    print(f"registration R required at start={required_internal_registration:.9f}; R=0 fixes C")
    print("Checks passed: cubic threshold, formula residual, implicit solution, registration bridge")


if __name__ == "__main__":
    main()
