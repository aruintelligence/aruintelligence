"""Independent numerical audit of the 1D update in DOI 10.5281/zenodo.18010911.

This checks a disclosed toy model, not whether a physical memory field exists.
Run with Python 3.9+; NumPy is optional for a cross-implementation comparison.
"""

import json
import math
import platform


D = 0.05
DECAY = 0.15
BASELINE = 0.10
CEILING = 2.0
CELLS = 400
STEPS = 400
DX = 20.0 / (CELLS - 1)  # np.linspace(-10, 10, 400) includes both ends.
DT = 0.45 * DX * DX / (2.0 * D)


def grid():
    return [-10.0 + i * DX for i in range(CELLS)]


def initial(xs):
    return [BASELINE + 1.2 * math.exp(-x * x / (2.0 * 0.9**2)) for x in xs]


def forcing(xs):
    return [0.25 * math.exp(-x * x / (2.0 * 0.8**2)) for x in xs]


def laplacian(values, dx=DX):
    n = len(values)
    return [(values[(i - 1) % n] - 2.0 * values[i] + values[(i + 1) % n]) / dx**2
            for i in range(n)]


def step(values, amplitudes, dt=DT, dx=DX):
    """Read the whole old state, apply the PDF's explicit Euler step, then clip."""
    lap = laplacian(values, dx)
    raw = [value + dt * (D * curvature - DECAY * (value - BASELINE)
                         + amp * (1.0 - value / CEILING))
           for value, curvature, amp in zip(values, lap, amplitudes)]
    return [min(CEILING, max(0.0, value)) for value in raw], sum(
        value < 0.0 or value > CEILING for value in raw
    )


def replay(values, amplitudes, steps=STEPS, dt=DT, dx=DX):
    clipped = 0
    for _ in range(steps):
        values, count = step(values, amplitudes, dt, dx)
        clipped += count
    return values, clipped


def measures(values, dx=DX):
    mean = sum(values) / len(values)
    return {
        "mean": mean,
        "variance": sum((value - mean)**2 for value in values) / len(values),
        "integrated_mass": sum(values) * dx,
    }


def audit():
    xs = grid()
    start = initial(xs)
    amps = forcing(xs)
    lap = laplacian(start)
    one, one_clip = step(start, amps)
    source = [a * (1.0 - u / CEILING) for a, u in zip(amps, start)]
    expected_mass_change = DT * DX * sum(
        -DECAY * (u - BASELINE) + s for u, s in zip(start, source)
    )
    mass_residual = (sum(one) - sum(start)) * DX - expected_mass_change

    final, clip_count = replay(start, amps)
    reference = measures(final)
    half, half_clip = replay(start, amps, steps=2 * STEPS, dt=DT / 2.0)
    half_difference = max(abs(a - b) for a, b in zip(final, half))

    uniform = [BASELINE + 0.5] * CELLS
    relaxed, relaxed_clip = step(uniform, [0.0] * CELLS)
    expected_relaxed = BASELINE + 0.5 * (1.0 - DECAY * DT)
    uniform_error = max(abs(u - expected_relaxed) for u in relaxed)

    checks = {
        "periodic_laplacian_sum_zero": abs(sum(lap) * DX) < 1e-10,
        "unclipped_first_step_mass_balance": one_clip == 0 and abs(mass_residual) < 1e-11,
        "uniform_relaxation_one_step": relaxed_clip == 0 and uniform_error < 1e-12,
        "source_zero_at_ceiling": all(a * (1.0 - CEILING / CEILING) == 0.0 for a in amps),
        "published_transcription_regression": abs(reference["mean"] - 0.2154056632) < 1e-9
        and abs(reference["variance"] - 0.0566952393) < 1e-9
        and abs(reference["integrated_mass"] - 4.3189105397) < 1e-8,
    }

    numpy_comparison = {"available": False}
    try:
        import numpy as np
    except ImportError:
        pass
    else:
        nx = np.linspace(-10.0, 10.0, CELLS)
        nu = BASELINE + 1.2 * np.exp(-nx**2 / (2.0 * 0.9**2))
        na = 0.25 * np.exp(-nx**2 / (2.0 * 0.8**2))
        ndx = nx[1] - nx[0]
        ndt = 0.45 * ndx * ndx / (2.0 * D)
        for _ in range(STEPS):
            nlap = (np.roll(nu, 1) - 2.0 * nu + np.roll(nu, -1)) / ndx**2
            nu = np.clip(nu + ndt * (D * nlap - DECAY * (nu - BASELINE)
                                     + na * (1.0 - nu / CEILING)), 0.0, CEILING)
        error = float(max(abs(a - b) for a, b in zip(final, nu)))
        numpy_comparison = {"available": True, "version": np.__version__,
                            "max_absolute_difference": error}
        checks["independent_loop_matches_numpy"] = error < 1e-10

    return {
        "source_doi": "10.5281/zenodo.18010911",
        "python_version": platform.python_version(),
        "model": "1D periodic explicit Euler with saturated source and clipping",
        "grid_convention": "400 inclusive linspace coordinates; endpoints are distinct periodic cells",
        "parameters": {"D": D, "lambda": DECAY, "mu0": BASELINE,
                       "mu_max": CEILING, "cells": CELLS, "steps": STEPS,
                       "dx": DX, "dt": DT},
        "reference_replay": reference,
        "clipped_cells_over_all_steps": clip_count,
        "half_step_same_time": {"steps": 2 * STEPS, "clipped_cells": half_clip,
                                "max_absolute_difference": half_difference,
                                "integrated_mass": measures(half)["integrated_mass"]},
        "diagnostics": {"periodic_laplacian_integral": sum(lap) * DX,
                        "first_step_mass_balance_residual": mass_residual,
                        "uniform_relaxation_max_error": uniform_error},
        "numpy_comparison": numpy_comparison,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scope": "Software and discretization checks only; no empirical physical validation.",
    }


if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["all_checks_pass"] else 1)
