"""Reproduce a homogeneous check of Volume I's selected scalar action.

Source: https://doi.org/10.5281/zenodo.17851542, Sections 1-3.
For lambda = 0 and no spatial gradient, the stated equation becomes
mu_ddot + 4*alpha*mu*(mu**2 - mu0**2) = 0.
This checks one permitted theoretical case, not a measurement of memory.
"""
import json
import math

ALPHA = 1.0
MU0 = 1.0
DT = 0.001
STEPS = 10_000


def acceleration(mu):
    return -4.0 * ALPHA * mu * (mu * mu - MU0 * MU0)


def energy(mu, velocity):
    return 0.5 * velocity * velocity + ALPHA * (mu * mu - MU0 * MU0) ** 2


def advance(mu, velocity):
    def rhs(x, y):
        return y, acceleration(x)

    k1 = rhs(mu, velocity)
    k2 = rhs(mu + DT * k1[0] / 2, velocity + DT * k1[1] / 2)
    k3 = rhs(mu + DT * k2[0] / 2, velocity + DT * k2[1] / 2)
    k4 = rhs(mu + DT * k3[0], velocity + DT * k3[1])
    return (
        mu + DT * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6,
        velocity + DT * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6,
    )


def main():
    mu, velocity = 1.1, 0.0
    initial_energy = energy(mu, velocity)
    minimum = maximum = mu
    lower_turns = 0
    for _ in range(STEPS):
        old_velocity = velocity
        mu, velocity = advance(mu, velocity)
        minimum = min(minimum, mu)
        maximum = max(maximum, mu)
        if old_velocity < 0 <= velocity:
            lower_turns += 1

    drift = abs(energy(mu, velocity) - initial_energy) / initial_energy
    result = {
        "source_doi": "10.5281/zenodo.17851542",
        "case": "homogeneous lambda=0; alpha=mu0=1; mu(0)=1.1; mu_dot(0)=0",
        "time": STEPS * DT,
        "mu_final": round(mu, 8),
        "mu_min": round(minimum, 8),
        "mu_max": round(maximum, 8),
        "lower_turns": lower_turns,
        "initial_energy": initial_energy,
        "final_energy": energy(mu, velocity),
        "relative_energy_drift": drift,
        "linearized_angular_frequency": math.sqrt(8 * ALPHA * MU0 * MU0),
    }
    assert drift < 1e-8
    assert lower_turns >= 3
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
