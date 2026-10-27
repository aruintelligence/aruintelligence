#!/usr/bin/env python3
"""Small algebraic check of the EEG PSD summary in DOI 10.5281/zenodo.18708708.

Synthetic spectra only; this does not process EEG or test the proposed field.
"""

from math import isclose, isfinite, log2


def printed_score(power):
    """Numerical shape of the PDF's illustrative, unnormalized code line."""
    return -sum(p * log2(p + 1e-12) for p in power)


def spectral_entropy_bits(power):
    """Shannon entropy of power normalized over a fixed set of frequency bins."""
    if len(power) < 2 or any(not isfinite(p) or p < 0 for p in power):
        raise ValueError("At least two finite, nonnegative power bins are required")
    total = sum(power)
    if total <= 0:
        raise ValueError("Total power must be positive")
    fractions = (p / total for p in power)
    return -sum(q * log2(q) for q in fractions if q > 0)


def main():
    flat = (1.0, 1.0)
    scaled = (2.0, 2.0)
    shaped = (3.0, 1.0)

    raw_flat, raw_scaled = printed_score(flat), printed_score(scaled)
    h_flat = spectral_entropy_bits(flat)
    h_scaled = spectral_entropy_bits(scaled)
    h_shaped = spectral_entropy_bits(shaped)

    assert isclose(raw_flat, 0.0, abs_tol=1e-10)
    assert isclose(raw_scaled, -4.0, abs_tol=1e-10)
    assert isclose(h_flat, 1.0, abs_tol=1e-12)
    assert isclose(h_scaled, h_flat, abs_tol=1e-12)
    assert isclose(h_shaped, 0.8112781244591328, abs_tol=1e-12)
    assert h_shaped < h_flat  # Shape-change control responds as expected.

    print(f"flat PSD: raw score={raw_flat:.9f}; normalized H={h_flat:.9f} bits")
    print(f"scaled PSD: raw score={raw_scaled:.9f}; normalized H={h_scaled:.9f} bits")
    print(f"shape control: normalized H={h_shaped:.9f} bits")
    print("PASS: raw score varies with units; normalized entropy is scale invariant")


if __name__ == "__main__":
    main()
