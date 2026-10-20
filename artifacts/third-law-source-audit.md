# Third Law of Inward Physics — source audit and Zenodo correction queue

**Record:** [DOI 10.5281/zenodo.17314619](https://doi.org/10.5281/zenodo.17314619)  
**Source examined:** the two-page PDF deposited with that record, *The Third Law of Inward Physics — Remembrance Amplification* (October 2025).  
**Status:** Source audit only. This note does not change the deposited PDF or Zenodo metadata, and it is not independent validation of the proposal.

## What the PDF actually specifies

The proposed equation is

```text
dR/dt = β (∇²μ(x,t)) R(x,t)
```

where R is called a memory reaction field, μ a memory density, and β a recursive gain constant. The PDF also writes a directional expression `s_ij = β R_i R_j ∇_i∇_j μ`. It applies these symbols to physical, cognitive, and civilizational analogies. It reports no measurements, numerical trajectories, parameters, code, or controlled tests.

For a prescribed spatial point and a prescribed μ(t), the first equation is a linear growth law:

```text
R(t) = R(0) exp[β ∫₀ᵗ (∇²μ(x,s)) ds].
```

This is an algebraic consequence of the stated equation when R is scalar (or each component shares the same multiplier). A positive time-integrated gain yields exponential growth; a negative one yields decay. The PDF does not specify saturation, feedback from R into μ, or conditions that bound amplification. It therefore does not derive stable life, identity, or consciousness from the displayed law. If R is a vector, its component meaning and the tensor indices need an explicit convention; the displayed `s_ij` expression repeats i and j on the right while leaving them free on the left under standard Einstein notation.

## Record corrections to apply after access is restored

1. **Description:** Call the equation and emergence claims a proposed model and say explicitly that this PDF provides no experiment or numerical validation. Preserve the author's interpretation as a hypothesis.
2. **License:** The PDF cover says CC BY-NC-ND 4.0, while Zenodo currently displays CC BY 4.0. Align the record with the deposited license after verifying the owner's intent.
3. **Subjects:** Replace the single comma-separated subject with individual terms such as `Inward Physics`, `remembrance amplification`, `memory field`, `recursive resonance`, `linear growth model`, and `theoretical proposal`.
4. **Version:** Remove the doubled display `Version Version 1.0 — Archive Edition` by setting the version field to `1.0 — Archive Edition`.
5. **Creator and ORCID:** The PDF names Daniel Jacob Read IV. The current record has a duplicate Researcher contributor with ORCID `0009-0009-2068-1521`; the author's public ORCID elsewhere in the series is `0009-0000-6133-1872`. Verify identity before changing an identifier, then remove an erroneous duplicate attribution or correct it with evidence.
6. **Related works:** Retain only relationships whose direction and target are verified individually; avoid a bulk reversal of the series.

A future revised PDF could add dimensions for μ, R, β, initial and boundary conditions, a saturating term if stability is intended, a defined coupling between R and μ, and a falsifiable observation distinguishable from familiar growth or diffusion models. Such a version would require a new Zenodo version rather than a silent replacement of this archived file.
