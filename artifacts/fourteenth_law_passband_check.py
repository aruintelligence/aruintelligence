"""Exact Gaussian-passband limit for DOI 10.5281/zenodo.18917411.

Illustrative spectral inputs only; no physical memory-field measurement.
Run: python3 artifacts/fourteenth_law_passband_check.py
"""

from math import erf, exp, isclose, pi, sqrt


def bandwidth(coherence: float, scale: float = 1.0) -> float:
    assert 0 <= coherence < 1 and scale > 0
    return scale * (1 - coherence)


def continuous_flux(coherence: float, gain: float = 0.8,
                    density: float = 2.0, half_width: float = 1.0) -> float:
    """PDF flux for S_E=density on Ω*±half_width, zero elsewhere."""
    assert 0 <= gain <= 1 and density >= 0 and half_width > 0
    sigma = bandwidth(coherence)
    return gain * density * sqrt(2 * pi) * sigma * erf(
        half_width / (sqrt(2) * sigma)
    )


def line_transmission(coherence: float, detuning: float, gain: float = 0.8) -> float:
    sigma = bandwidth(coherence)
    return gain * exp(-detuning**2 / (2 * sigma**2))


def main() -> None:
    fluxes = [(r, continuous_flux(r)) for r in (0.0, 0.5, 0.9, 0.99)]
    assert all(fluxes[i][1] > fluxes[i + 1][1] for i in range(len(fluxes) - 1))
    for r, flux in fluxes[-2:]:
        sigma = bandwidth(r)
        assert isclose(flux / sigma, 0.8 * 2.0 * sqrt(2 * pi), rel_tol=1e-8)
    assert isclose(line_transmission(0.5, 0.0), line_transmission(0.99, 0.0))
    assert line_transmission(0.99, 0.1) < line_transmission(0.5, 0.1)

    for r, flux in fluxes:
        print(f"R={r:.2f}: sigma={bandwidth(r):.6f}, continuous-band flux={flux:.9f}")
    print("R→1: continuous-band flux→0; exact R=1 Gaussian needs a definition")
    print("At carrier: fixed line transmission=0.8 for R<1 in this example")
    print("Checks passed: area limit and distinct line/continuous-spectrum behavior")


if __name__ == "__main__":
    main()
