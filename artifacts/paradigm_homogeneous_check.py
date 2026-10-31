#!/usr/bin/env python3
"""Exact homogeneous-limit check for DOI 10.5281/zenodo.18645539.

Uses illustrative parameters, not measured memory density or EEG observations.
"""

from math import exp, expm1, isclose, log


def state_and_registration(t, *, rate, baseline, source, initial):
    """Solve dμ/dt = -rate(μ-baseline)+source and A(t)=∫₀ᵗμ(s)ds."""
    if rate <= 0 or t < 0:
        raise ValueError("This closed form assumes rate > 0 and t >= 0")
    equilibrium = baseline + source / rate
    delta = initial - equilibrium
    state = equilibrium + delta * exp(-rate * t)
    registration = equilibrium * t - delta * expm1(-rate * t) / rate
    return equilibrium, state, registration


def main():
    parameters = dict(rate=0.15, baseline=0.10, source=0.02, initial=0.05)
    kappa = 0.5
    equilibrium, state, registration = state_and_registration(10.0, **parameters)
    ratio = exp(-kappa * registration)
    coherence = 1.0 - ratio

    assert isclose(equilibrium, 0.23333333333333334, abs_tol=1e-14)
    assert isclose(state, 0.1924261373061212, abs_tol=1e-14)
    assert isclose(registration, 1.3838257512925254, abs_tol=1e-14)
    assert 0 < state < equilibrium and 0 < ratio < 1 and 0 < coherence < 1
    assert isclose(ratio, 0.5006175334907509, abs_tol=1e-14)
    _, start, area0 = state_and_registration(0.0, **parameters)
    assert isclose(start, parameters["initial"]) and isclose(area0, 0.0)

    # A sign-unrestricted source is a mathematical off-domain challenge.
    # It is not asserted to represent attention or any physical source.
    adverse = dict(rate=1.0, baseline=1.0, source=-2.0, initial=1.0)
    zero_time = log(2.0)
    _, at_zero, _ = state_and_registration(zero_time, **adverse)
    _, later, later_area = state_and_registration(5.0, **adverse)
    assert isclose(at_zero, 0.0, abs_tol=1e-14)
    assert later < 0 and later_area < 0

    print(f"positive-source equilibrium μ* = {equilibrium:.9f}")
    print(f"at t=10: μ={state:.9f}, A={registration:.9f}")
    print(f"stipulated variance ratio={ratio:.9f}, coherence={coherence:.9f}")
    print(f"unrestricted negative-source example crosses μ=0 at t=ln(2)={zero_time:.9f}")
    print("PASS: exact conditional behavior and positivity boundary")


if __name__ == "__main__":
    main()
