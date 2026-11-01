"""Finite counterexample and repair for DOI 10.5281/zenodo.18125773.

This checks the logical relation in the deposited definitions, not a physical
or AI identity measurement. Run: python3 artifacts/sovereign_continuum_check.py
"""

from collections import deque


def reachable(start: str, goal: str, edges: set[tuple[str, str]]) -> bool:
    seen = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        for source, target in edges:
            if source == node and target not in seen:
                seen.add(target)
                queue.append(target)
    return False


def equivalent(a: str, b: str, edges: set[tuple[str, str]]) -> bool:
    """Document II's mutual A-reachability, definitions 3–4."""
    return reachable(a, b, edges) and reachable(b, a, edges)


def equivalence_class(node: str, nodes: set[str], edges: set[tuple[str, str]]) -> frozenset[str]:
    return frozenset(other for other in nodes if equivalent(node, other, edges))


def main() -> None:
    nodes = {"M0", "M1"}
    # One admissible forward re-expression; identity maps / zero-length chains
    # are available. A1–A4 do not state that its reverse is admissible.
    forward = {("M0", "M1")}
    assert reachable("M0", "M1", forward)
    assert not reachable("M1", "M0", forward)
    assert not equivalent("M0", "M1", forward)
    assert equivalence_class("M0", nodes, forward) != equivalence_class("M1", nodes, forward)

    # S is invariant along the forward edge, as required on PDF p. 4, but it
    # need not be a complete index of mutual-reachability classes.
    signature = {"M0": ("same-K", "same-U", "same-Pi"),
                 "M1": ("same-K", "same-U", "same-Pi")}
    mismatch = int(signature["M0"] != signature["M1"])
    assert mismatch == 0
    assert not equivalent("M0", "M1", forward)

    # An explicit reverse-admissibility condition repairs this example.
    reversible = forward | {("M1", "M0")}
    assert equivalent("M0", "M1", reversible)
    assert equivalence_class("M0", nodes, reversible) == equivalence_class("M1", nodes, reversible)

    print("forward only: M0→M1, M1↛M0; Sigma(M0) != Sigma(M1)")
    print("same invariant tuple: D(M0,M1)=0 although Sigma classes differ")
    print("with admissible reverse: mutual reachability and class conservation hold")
    print("Checks passed: reverse-reachability and signature-completeness boundaries")


if __name__ == "__main__":
    main()
