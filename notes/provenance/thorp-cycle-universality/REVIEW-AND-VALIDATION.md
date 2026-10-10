# Review and validation record for revision 2

## Analytical scope

This revision implements the supplied line-by-line comments and the proposed additions note. The core longest-last induction and multicycle bridge are retained. The substantive definition correction is that closing queries include values fixed earlier within the same closing segment. The re-rooting, reverse-query, and finite-measure arguments are made explicit.

The new Poisson-window theorem includes a finite inclusion–exclusion proof. Its order of limits is: fix the factorial truncation order, let the register width tend to infinity, and then let the truncation order grow. Bounded total harmonic mass is essential. The scale-invariant Poisson, Dickman, and truncated-maximum corollaries are proved from that theorem. The quantitative birthday-range theorem includes its separate proof; it is not represented as an immediate consequence of the fixed-order moment theorem.

The product-to-LCM sharpening uses Chebyshev's bound. In its elementary binomial-coefficient proof it is the product of the **primes** having a power in (n,2n], not the product of those prime powers, that divides the central binomial coefficient.

## Checks executed for this revision

1. The preserved multiscale cycle audit, multibridge audit, independently implemented feedback-switch audit, and equality-rank audit were rerun. All four JSON outputs matched the preserved results exactly. See `validation/core_rerun_summary.json` and the unchanged reviewed-v1 archive for the full counts and scripts.
2. The new additions audit checked 3,232 scalar inclusion–exclusion remainders, 6,987 selected-occurrence remainder inequalities, and 300 exact divisibility instances used in the Chebyshev argument.
3. The short-cycle marginals and the stated joint-independence range were verified by exhaustive feedback enumeration in widths 2 through 5: 65,812 environments in total. All probability comparisons use rational arithmetic.
4. A regression test at width 3 on the cyclic word 1011 verifies a repeated context that is first fixed during the closing segment. It has J = 0, K = 1, and m_new = 1; excluding earlier closing queries would violate the required identity.
5. The standalone LaTeX source was compiled from clean auxiliary directories twice, using the repository's fixed epoch and TeX Live 2025. The two PDFs were byte-for-byte identical. The source disables the output-directory-dependent PDF trailer ID so relocating a clean build does not alter the snapshot.
6. Static checks found no missing references, duplicate labels, unresolved citations, or known conversion debris. The final LaTeX logs contain no overfull boxes or undefined references/citations. One nonfatal epstopdf warning reports that shell escape is disabled; the paper has no EPS conversion requirement.
7. All 21 pages were rendered and inspected. Programmatic text-bound checks found no content outside the checked page margins.

The JSON build record gives source/PDF hashes and the tool versions. `reproduce.py` reruns the finite checks and deterministic build without modifying the frozen source material.

## Limits

Finite computations do not establish the asymptotic entropy tail, the induction for arbitrary register width, or the limiting probability laws. Those claims rest on the written analytic proofs. This package is a research manuscript with proof review and reproducibility checks, not independent peer review or proof-assistant certification. The bibliography has been checked for the cited statements and bibliographic data; no exhaustive novelty certification is claimed.

## Repository status

The destination repository was inspected at commit `be12714e68d87e11f1f3127d69500a7bab59fb83`. No remote file, branch, pull request, or commit was changed. This package prepares additive files and integration instructions. The full repository-wide build/CI suite has not been run against an integrated checkout; it should run on the eventual pull request.
