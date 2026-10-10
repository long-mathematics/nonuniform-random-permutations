# Cycle Universality for a Single Thorp Shuffle

**Author:** Christopher D. Long  
**Revision:** expanded manuscript, version 2  
**Manuscript date:** 9 October 2026

[Read the paper](../../output/pdf/thorp-cycle-universality.pdf) · [LaTeX source](thorp-cycle-universality.tex)

## Results and scope

The manuscript studies one physical Thorp shuffle on a dyadic state space, equivalently a uniformly random binary noncoalescing feedback shift register. The feedback function is sampled once and reused.

For every fixed number of cycles, it proves uniform joint factorial-moment asymptotics at all length ratios, provided the total length is below a fixed exponent less than two thirds of the state-space size and each component in the two-sided estimate is at least four times the register width. It derives the truncated functional Erdős–Turán law, Poisson approximation on sets of bounded harmonic mass, a scale-invariant Poisson process, Dickman truncated mass, and a uniform limit for the largest cycle below the cutoff.

A separate quantitative theorem approximates the entire initial cycle-count vector below the birthday scale. The appendix records exact short-cycle binomial laws and an elementary joint-independence range. Lower bounds are also given for the untruncated permutation order and total number of cycles.

The full one-shuffle Erdős–Turán conjecture, the exponent endpoint two thirds, unrestricted growing-order moments, and full-initial-vector Poisson approximation above the birthday scale are not asserted.

## Relationship to other material

This is a Christopher D. Long manuscript, proposed as Paper VIII. It is separate from the externally authored OpenAI mixing paper in `third_party/openai-thorp/`. No independent-round mixing theorem or macroscopic Poisson–Dirichlet theorem is used as an input to its proofs. Paper V in this repository supplies related one-shuffle context, not an unproved dependency.

## Build and checks

The LaTeX source is standalone and includes its bibliography. After registering it in the repository build list, the normal `make pdf` and `make check` commands apply.

The supplementary checks can also be run from the repository root:

```sh
python3 scripts/thorp-cycle-universality/reproduce.py
```

This replays the preserved finite audits, tests the additions, and checks a deterministic rebuild of this manuscript. It requires Python 3, a C++17 compiler, `latexmk`, and the repository's TeX dependencies. No shell escape is needed.

[Revision history](../../notes/provenance/thorp-cycle-universality/CHANGELOG.md) · [Review and validation record](../../notes/provenance/thorp-cycle-universality/REVIEW-AND-VALIDATION.md)

The computations check finite identities and reproducibility. They are not substitutes for the analytic proofs, independent peer review, formal verification, or a comprehensive novelty review. The author's manuscript copyright is retained.
