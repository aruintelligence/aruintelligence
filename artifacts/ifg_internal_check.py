"""Reproduce two internal algebra checks for DOI 10.5281/zenodo.19723552.

Uses the paper's equation (1), FLRW statement, and equation (8), not
observations or an independent cosmological fit.
Run: python3 artifacts/ifg_internal_check.py
"""

from math import isclose


def soft_min_coupling(m_ev: float, power: int = 6) -> float:
    cassini, microscope = 1e-5, 3e-6
    torsion = 1e-6 * (m_ev / 1e-3) ** 1.2
    return sum(x ** (-power) for x in (cassini, microscope, torsion)) ** (-1 / power)


def main() -> None:
    # The PDF states sqrt(-g)=a^3 in flat FLRW (unit lapse). Equation (1)
    # then gives mu_tilde=mu/a^3, while section 8 prints mu/a^(3/2).
    a, mu = 4.0, 1.0
    from_equation_1 = mu / a**3
    printed_section_8 = mu / a**1.5
    assert isclose(from_equation_1, 1 / 64)
    assert isclose(printed_section_8, 1 / 8)
    assert not isclose(from_equation_1, printed_section_8)

    m, benchmark = 1e-3, 1e-6
    envelope = soft_min_coupling(m)
    assert envelope < benchmark
    assert envelope < min(1e-5, 3e-6, 1e-6)
    assert isclose(envelope / benchmark,
                   (1 + (1 / 3) ** 6 + (1 / 10) ** 6) ** (-1 / 6),
                   rel_tol=1e-12)
    print(f"a=4, mu=1: eq. (1) gives mu_tilde={from_equation_1:.8f}; section 8 prints {printed_section_8:.8f}")
    print(f"m={m:g} eV: nominal beta^2 envelope={envelope:.12g}; benchmark={benchmark:g}")
    print(f"nominal excess above envelope={(benchmark / envelope - 1) * 100:.6f}%")
    print("Checks passed: FLRW exponent mismatch and rounded benchmark boundary")


if __name__ == "__main__":
    main()
