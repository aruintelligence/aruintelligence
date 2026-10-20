"""Reproduce the discrete update printed in Zenodo DOI 10.5281/zenodo.18010911."""
import numpy as np

D = 0.05
lam = 0.15
mu0 = 0.10
mu_max = 2.0
N = 400
x = np.linspace(-10, 10, N)
dx = x[1] - x[0]
mu = mu0 + 1.2 * np.exp(-x**2 / (2 * 0.9**2))

def laplacian(u):
    return (np.roll(u, 1) - 2 * u + np.roll(u, -1)) / dx**2

dt = 0.45 * dx * dx / (2 * D)
for t in range(400):
    A = 0.25 * np.exp(-x**2 / (2 * 0.8**2))
    S = A * (1 - mu / mu_max)
    dmu = D * laplacian(mu) - lam * (mu - mu0) + S
    mu += dt * dmu
    mu = np.clip(mu, 0, mu_max)

print(f"mean={np.mean(mu):.10f}")
print(f"variance={np.var(mu):.10f}")
print(f"integrated_mass={np.sum(mu) * dx:.10f}")
