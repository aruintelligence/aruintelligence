"""Check the deterministic homogeneous limit of First Law equations (3)-(4).

The archived report's parameter choice a=1, b=-3, c=1 is printed in its
numerical companion. This checks the resulting quartic potential only; no
stochastic run, future-state constraint, or physical measurement is modeled.
"""

from math import sqrt

A, B, C = 1.0, -3.0, 1.0
ROOTS = (0.0, (3.0 - sqrt(5.0)) / 2.0, (3.0 + sqrt(5.0)) / 2.0)


def potential(mu):
    return A * mu**2 / 2 + B * mu**3 / 3 + C * mu**4 / 4


def drift(mu):
    return -(A * mu + B * mu**2 + C * mu**3)


def curvature(mu):
    return A + 2 * B * mu + 3 * C * mu**2


def advance(mu, reg, dt):
    # Joint RK4 for dmu/dt=-V'(mu), d(reg)/dt=mu.
    k1, a1 = drift(mu), mu
    k2, a2 = drift(mu + dt * k1 / 2), mu + dt * k1 / 2
    k3, a3 = drift(mu + dt * k2 / 2), mu + dt * k2 / 2
    k4, a4 = drift(mu + dt * k3), mu + dt * k3
    return (mu + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6,
            reg + dt * (a1 + 2 * a2 + 2 * a3 + a4) / 6)


def main():
    for root in ROOTS:
        assert abs(drift(root)) < 1e-13
        print(f"equilibrium={root:.12f} V={potential(root):.12f} "
              f"Vpp={curvature(root):.12f} "
              f"attracting={curvature(root) > 0}")
    assert curvature(ROOTS[0]) > 0 > curvature(ROOTS[1])
    assert curvature(ROOTS[2]) > 0

    dt, steps = 0.01, 2000
    for start, expected in ((0.1, ROOTS[0]), (1.0, ROOTS[2]),
                            (-0.1, ROOTS[0])):
        mu, reg = start, 0.0
        last_v = potential(mu)
        for _ in range(steps):
            mu, reg = advance(mu, reg, dt)
            now_v = potential(mu)
            assert now_v <= last_v + 1e-12
            last_v = now_v
        assert abs(mu - expected) < 1e-6
        if start < 0:
            assert reg < 0  # The printed integral need not increase.
        print(f"initial={start:.1f} mu_at_20={mu:.12f} "
              f"registration_at_20={reg:.12f}")


if __name__ == "__main__":
    main()
