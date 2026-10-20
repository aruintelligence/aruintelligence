#!/usr/bin/env python3
"""Source-grounded analytic check of DOI 10.5281/zenodo.17314619.

This checks the mathematical consequences of the proposed law for prescribed
mu. It does not test whether a physical memory field exists.
"""

import argparse
import json
import math


def exact_response(r0, beta, amplitude, wavenumber, decay, x, time):
    """Solve dR/dt = beta * laplacian(mu) * R for a decaying cosine mu."""
    integral = time if decay == 0 else -math.expm1(-decay * time) / decay
    exponent = -beta * amplitude * wavenumber**2 * math.cos(wavenumber * x) * integral
    return r0 * math.exp(exponent)


def euler_response(r0, beta, amplitude, wavenumber, decay, x, time, steps):
    dt = time / steps
    r = r0
    for n in range(steps):
        t = n * dt
        laplacian = -amplitude * wavenumber**2 * math.cos(wavenumber * x) * math.exp(-decay * t)
        r += dt * beta * laplacian * r
    return r


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--amplitude", type=float, default=0.2)
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument("--decay", type=float, default=0.4)
    parser.add_argument("--time", type=float, default=4.0)
    parser.add_argument("--steps", type=int, default=40)
    args = parser.parse_args()
    if args.amplitude < 0 or args.amplitude > 1 or args.decay < 0 or args.time < 0 or args.steps < 1:
        parser.error("require 0 <= amplitude <= 1, decay and time >= 0, steps >= 1")
    k, r0 = 1.0, 1.0
    cases = []
    for label, x in (("negative curvature / decay", 0.0), ("zero curvature", math.pi / 2), ("positive curvature / growth", math.pi)):
        exact = exact_response(r0, args.beta, args.amplitude, k, args.decay, x, args.time)
        coarse = euler_response(r0, args.beta, args.amplitude, k, args.decay, x, args.time, args.steps)
        fine = euler_response(r0, args.beta, args.amplitude, k, args.decay, x, args.time, 2 * args.steps)
        cases.append({"case": label, "x": x, "exact": exact, "euler_steps": coarse,
                      "euler_2x_steps": fine, "error_steps": abs(coarse - exact),
                      "error_2x_steps": abs(fine - exact)})
    bound_integral = args.time if args.decay == 0 else -math.expm1(-args.decay * args.time) / args.decay
    output = {"model": "mu(x,t)=1+A exp(-lambda*t) cos(x), R'=beta*laplacian(mu)*R",
              "parameters": {"A": args.amplitude, "beta": args.beta, "lambda": args.decay,
                             "time": args.time, "steps": args.steps, "R0": r0, "k": k},
              "log_response_absolute_bound": abs(args.beta) * args.amplitude * k**2 * bound_integral,
              "cases": cases}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
