# Repository status and theorem dependency map

Last reconciled: 9 October 2026.

This note records repository organization and internal review status. It is not an independent referee report, a novelty certification, or a formal proof verification.

## Current manuscript spine

1. `papers/01-luce-boundary-cycle-laws/` is the comprehensive Luce/Tsetlin manuscript. Its open-problems section predates the later switching paper, so its mesoscopic conjecture should be read together with item 2 below.
2. `papers/02-mesoscopic-luce-cycles/` is the free-depth switching proof of the mesoscopic cycle process. Its dependency audit states that the proof is self-contained under rate comparability and does not import the macroscopic Poisson--Dirichlet theorem.
3. `papers/03-luce-erdos-turan/` imports the marked switching and finite-endpoint interfaces from item 2 and proves the qualitative Erdős--Turán theorem for arbitrary comparable-rate triangular arrays.
4. `papers/04-luce-edgeworth/` is the quantitative supplement. It uses the free-depth endpoint theorem and proves the sharp Berry--Esseen rate and first Edgeworth term with exact-mean centering.
5. `papers/05-one-shuffle-universality/` is the stable functional theorem for riffle/shelf/major-index models. The later Edgeworth/optimality branch is kept separately under `notes/working/`.
6. `papers/06-residual-mass-transform-order/` is an adjacent Plackett--Luce/LRU/coupon-collector paper sharing the same size-biased ordering mechanism.

## Mesoscopic total-cycle branch

The historical `mesoscopic-total-cycle-resolution-candidate.tex` is not used as a dependency of the current manuscript spine. The earlier audit `mesoscopic-audit-and-repair.tex` identified structural defects in that route. The later free-depth paper supplies an independent proof of Conjecture 13.1, but the repository does not mark the candidate's Conjecture 13.2 total-cycle expectation/CLT claim as established without a fresh dedicated audit.

## Working branches

- `notes/working/functional-luce-erdos-turan.tex`: functional/multivariate Luce order strengthening.
- `notes/working/one-shuffle-edgeworth-optimality.tex`: quantitative Edgeworth/optimality strengthening after one shuffle.

They compile and are retained as research branches, not silently promoted over the stable manuscripts.

## Third-party Thorp material

`third_party/openai-thorp/` is a pinned copy of OpenAI's 26 September 2026 preprint *Optimal-order mixing of the Thorp shuffle*. It is third-party material and is not represented as a Long-authored result. The exact finite program `scripts/thorp_moment_audit.cpp` checks a separate rooted cyclic-word identity for small dimensions; it is a finite consistency check, not a proof of the external asymptotic mixing theorem.

## Recovery audit

The repository sources were reconciled against the recovered Library copies used for this import.

- Papers I, V, and VI match the recovered canonical source bytes exactly.
- Papers II, III, and IV match the recovered canonical source after the single editorial change `\\author{} -> \\author{Christopher D. Long}`.
- The functional Luce working branch differs from its recovered source only by the same author-line insertion.
- The one-shuffle Edgeworth/optimality working branch matches its recovered source bytes exactly.
- The historical mesoscopic total-cycle candidate and its audit remain in `notes/provenance/` and are not dependencies of the established manuscript spine.
- The three OpenAI Thorp source files and Apache-2.0 license match the pinned upstream OpenAI commit exactly.

## Verification performed for this repository import

- All six main Long manuscripts and both working branches compile with `latexmk` under TeX Live 2025 without undefined references, undefined citations, multiply defined labels, or overfull boxes. The residual-mass paper has two nonfatal underfull-box diagnostics.
- First-page renders of all eight Long documents were inspected for title-page clipping, missing glyphs, and obvious layout failures.
- The exact Thorp audit program verifies 156 identities for dimensions 2 through 5.
- README math is linted to use GitHub dollar delimiters; custom manuscript macros and alternative TeX math delimiters are forbidden in the README.
- Freshly compiled PDFs were compared with the recovered uploaded PDFs. Papers I, V, VI, and the one-shuffle Edgeworth working branch have identical extracted text; Papers II, III, IV, and the functional Luce branch differ only by the intentional author-line insertion described above.
- The GitHub Actions workflow rebuilds every committed PDF from a clean checkout and requires byte-for-byte equality with the committed snapshot. It also verifies source hashes, PDF hashes, local links, and README math syntax.
