#!/usr/bin/env python3
"""Prove a sufficient no-clipping bound and sweep the disclosed 1D toy update.

Source model: DOI 10.5281/zenodo.18010911, section 4.1 / Appendix A.
This is a software-model calculation, not an empirical test.
"""

import json
import math

D = 0.05
DECAY = 0.15
BASELINE = 0.10
CEILING = 2.0
CELLS = 400
STEPS = 400
DX = 20.0 / (CELLS - 1)
DT = 0.45 * DX * DX / (2.0 * D)
XS = [-10.0 + i * DX for i in range(CELLS)]
INITIAL = [BASELINE + 1.2 * math.exp(-x * x / (2 * 0.9**2)) for x in XS]
SOURCE_SHAPE = [math.exp(-x * x / (2 * 0.8**2)) for x in XS]


def raw_update(values, a):
    return [u + DT * (D * (values[(i - 1) % CELLS] - 2 * u +
                             values[(i + 1) % CELLS]) / DX**2
                     - DECAY * (u - BASELINE) + a[i] * (1 - u / CEILING))
            for i, u in enumerate(values)]


def run(amplitude):
    a = [amplitude * shape for shape in SOURCE_SHAPE]
    # u_new = c_i*u_i + r*(u_left+u_right) + dt*(lambda*mu0+A_i).
    # c_i >= 0, 0 <= mu0 <= ceiling, A_i >= 0 make [0, ceiling]
    # invariant under the unclipped update, for every starting array in it.
    r = D * DT / DX**2
    c_min = 1 - 2 * r - DT * (DECAY + max(a) / CEILING)
    certified = c_min >= -1e-14
    values = INITIAL.copy()
    clipped_count = 0
    first_clip = None
    max_raw = float("-inf")
    min_raw = float("inf")
    for step in range(1, STEPS + 1):
        raw = raw_update(values, a)
        violations = sum(x < 0 or x > CEILING for x in raw)
        clipped_count += violations
        if violations and first_clip is None:
            first_clip = step
        min_raw = min(min_raw, min(raw))
        max_raw = max(max_raw, max(raw))
        values = [min(CEILING, max(0.0, x)) for x in raw]
    assert not certified or clipped_count == 0
    return {"source_peak_parameter": amplitude, "sampled_source_max": max(a),
            "coefficient_min": c_min, "sufficient_bound_holds": certified,
            "clipped_cells_over_400_steps": clipped_count,
            "first_clipped_step": first_clip, "raw_min": min_raw,
            "raw_max": max_raw, "final_mean": sum(values) / CELLS}


def compare_initial_states():
    """Evolve published Gaussian and flat baseline under the same fixed source."""
    a = [0.25 * shape for shape in SOURCE_SHAPE]
    first = INITIAL.copy()
    second = [BASELINE] * CELLS
    initial_distance = max(abs(x - y) for x, y in zip(first, second))
    q = 1 - DT * DECAY
    assert 0 <= q < 1
    checkpoints = []
    for step in range(1, 4001):
        first = raw_update(first, a)
        second = raw_update(second, a)
        if step in (400, 4000):
            distance = max(abs(x - y) for x, y in zip(first, second))
            upper_bound = initial_distance * q**step
            assert distance <= upper_bound + 1e-12
            checkpoints.append({"steps": step, "observed_max_distance": distance,
                                "analytic_upper_bound": upper_bound})
    return {"initial_max_distance": initial_distance,
            "per_step_contraction_upper_bound": q,
            "checkpoints": checkpoints,
            "source_peak_parameter": 0.25,
            "comparison": "published Gaussian versus uniform baseline, same fixed source"}


def main():
    assert min(INITIAL) >= 0 and max(INITIAL) <= CEILING
    threshold = CEILING * ((1 - 2 * D * DT / DX**2) / DT - DECAY) / max(SOURCE_SHAPE)
    cases = [run(amplitude) for amplitude in (0.0, 0.25, 50.0, 100.0, 1000.0)]
    assert abs(cases[1]["final_mean"] - 0.2154056632) < 1e-9
    assert not cases[3]["sufficient_bound_holds"] and cases[3]["clipped_cells_over_400_steps"] == 0
    assert cases[4]["clipped_cells_over_400_steps"] > 0
    result = {"source_doi": "10.5281/zenodo.18010911",
              "grid": "400 inclusive linspace coordinates treated as periodic cells",
              "parameters": {"D": D, "lambda": DECAY, "mu0": BASELINE,
                             "mu_max": CEILING, "cells": CELLS, "steps": STEPS,
                             "dx": DX, "dt": DT},
              "sufficient_bound": "2*D*dt/dx^2 + dt*(lambda + max(A_i)/mu_max) <= 1",
              "source_peak_parameter_threshold": threshold,
              "cases": cases,
              "initial_condition_contraction": compare_initial_states(),
              "scope": "Analytic sufficient bound and deterministic software sweep; not empirical validation."}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
