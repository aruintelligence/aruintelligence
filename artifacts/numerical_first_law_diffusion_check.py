"""Fourier-mode stability check for the archived First Law 1D grid.

Checks only the linear explicit diffusion substep, not the unpublished full
stochastic solver or the physical memory-field proposal.
"""

L = 10.0
NX = 100
DT = 0.01
DX = L / NX


def step(values, diffusion):
    r = diffusion * DT / (DX * DX)
    return [
        value + r * (values[(i - 1) % NX] - 2 * value + values[(i + 1) % NX])
        for i, value in enumerate(values)
    ]


def check(diffusion):
    r = diffusion * DT / (DX * DX)
    amplification = 1 - 4 * r  # Nyquist / alternating periodic mode
    values = [1.0 if i % 2 == 0 else -1.0 for i in range(NX)]
    for n in range(1, 5):
        values = step(values, diffusion)
        assert max(abs(values[i] - ((-1) ** i) * amplification**n)
                   for i in range(NX)) < 1e-9
    print(f"D={diffusion:g} r={r:.12g} g={amplification:.12g} "
          f"amplitude_after_4={abs(values[0]):.12g} "
          f"stable_diffusion_substep={r <= 0.5}")


if __name__ == "__main__":
    check(0.1)
    check(3.0)
