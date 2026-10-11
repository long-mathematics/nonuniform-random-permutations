# Repository status and theorem dependency map

Last reconciled: 11 October 2026.

This note records repository organization and internal review status. It is not an independent referee report, a novelty certification, or a formal proof verification.

## Canonical repository split

The canonical editing location for the Luce/Tsetlin manuscript series is now [`long-mathematics/luce-tsetlin-permutations`](https://github.com/long-mathematics/luce-tsetlin-permutations). Its [theorem-status register](https://github.com/long-mathematics/luce-tsetlin-permutations/blob/main/THEOREM_STATUS.md) and [dependency map](https://github.com/long-mathematics/luce-tsetlin-permutations/blob/main/DEPENDENCIES.md) are authoritative for the migrated Luce papers and the later total-cycle results.

The Luce sources, PDFs, working notes, and provenance files in this repository are preserved snapshots of the collection at commit `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`. They remain available for historical comparison and reproducibility, but they are not independent editing targets. The riffle/shelf, LRU/caching, Thorp, and third-party Thorp materials remain maintained here.

No manuscript source, PDF, manifest entry, script, or historical audit file was changed as part of this documentation reconciliation.

## Current manuscript spine

Items 1--4 below describe the preserved local Luce snapshots. Their active focused counterparts are maintained in the dedicated Luce/Tsetlin repository.

1. `papers/01-luce-boundary-cycle-laws/` is the preserved comprehensive Luce/Tsetlin manuscript. Its open-problems section predates the later switching and total-cycle papers. The 139-page source is now an archival baseline for thematic extraction rather than an active monolithic editing target.
2. `papers/02-mesoscopic-luce-cycles/` is the preserved free-depth switching proof of the mesoscopic cycle process. Its dependency audit states that the proof is self-contained under rate comparability and does not import the macroscopic Poisson--Dirichlet theorem. The dedicated repository contains the current focused copy and an explicit truncation-uniform one-/two-root interface.
3. `papers/03-luce-erdos-turan/` is the preserved scalar paper importing the marked switching and finite-endpoint interfaces from item 2 and proving the qualitative Erdős--Turán theorem for arbitrary comparable-rate triangular arrays. Its active copy is maintained in the dedicated repository.
4. `papers/04-luce-edgeworth/` is the preserved quantitative logarithmic-order supplement. It uses the free-depth endpoint theorem and states the sharp Berry--Esseen rate and first Edgeworth term with exact-mean centering. Its active copy and current scope notes are maintained in the dedicated repository.
5. `papers/05-one-shuffle-universality/` is the stable functional theorem for riffle/shelf/major-index models. The later Edgeworth/optimality branch is kept separately under `notes/working/` and remains active in this repository.
6. `papers/06-radial-lru-extremality/` is the arXiv v1 paper on radial LRU extremality and move-to-front search-cost tails. It uses the same exponential-race/size-biased ordering mechanism as the Luce/Tsetlin work.
7. `papers/07-residual-mass-transform-order/` is the sequel that strengthens the radial first-moment theorem to a transform-order statement for residual miss mass and connects it to coupon collecting.
8. `papers/08-thorp-cycle-universality/` is the authored one-physical-shuffle cycle-universality manuscript, distinct from the externally authored independent-round mixing theorem. It proves fixed-order joint cycle moment asymptotics below every exponent two thirds, truncated functional Erdős--Turán laws, bounded-harmonic-mass Poisson approximations, and Dickman/truncated-max corollaries. The full one-shuffle order law and the two-thirds endpoint are not proved. See its local scope note and provenance records.

## Mesoscopic total-cycle branch

The historical `mesoscopic-total-cycle-resolution-candidate.tex` is not used as a dependency of either repository's current manuscript spine. The earlier audit `mesoscopic-audit-and-repair.tex` identified structural defects in that route. The later free-depth paper supplies an independent proof of Conjecture 13.1, but this repository does not mark the historical candidate's Conjecture 13.2 total-cycle expectation/CLT claim as established.

That verdict concerns the historical candidate only. A later functional manuscript uses a different Campbell--Stein and growing-dimensional product-Poisson argument. Following a scoped audit and integration, the dedicated Luce/Tsetlin repository records a total-cycle CLT and joint functional count/order law, together with a separate quantitative manuscript on exact-mean Poisson approximation, sharp Berry--Esseen bounds, and lattice Edgeworth expansions. These later proofs do not reinstate the rejected candidate's proposed sampled-profile expectation expansion. Their precise status and review boundaries are recorded in the dedicated repository's theorem-status register.

## Working branches

- `notes/working/functional-luce-erdos-turan.tex` is a preserved historical working snapshot. The current focused manuscript is `papers/functional-erdos-turan/functional-luce-erdos-turan.tex` in the dedicated Luce/Tsetlin repository.
- `notes/working/one-shuffle-edgeworth-optimality.tex` remains the active quantitative Edgeworth/optimality strengthening after one shuffle in this repository.

The local functional Luce file compiles and remains preserved for provenance; it is not the canonical editing copy. The one-shuffle branch remains a research branch rather than a silently promoted replacement.

## Third-party Thorp material

`third_party/openai-thorp/` is a pinned copy of OpenAI's 26 September 2026 preprint *Optimal-order mixing of the Thorp shuffle*. It is third-party material and is not represented as a Long-authored result. The exact finite program `scripts/thorp_moment_audit.cpp` checks a separate rooted cyclic-word identity for small dimensions; it is a finite consistency check, not a proof of the external asymptotic mixing theorem.

## Recovery audit

The repository sources were reconciled against the recovered Library copies used for this import.

- Papers I, V, and VII match the recovered canonical source bytes exactly.
- Papers II, III, and IV match the recovered canonical source after the single editorial change `\\author{} -> \\author{Christopher D. Long}`.
- Paper VI was imported from the arXiv v1 source for arXiv:2605.26107. Its deterministic repository build was compared against the official arXiv v1 PDF after removing the arXiv running stamp and page-number artifacts; the manuscript-body token sequence agrees exactly.
- The functional Luce working branch differs from its recovered source only by the same author-line insertion.
- The one-shuffle Edgeworth/optimality working branch matches its recovered source bytes exactly.
- The historical mesoscopic total-cycle candidate and its audit remain in `notes/provenance/` and are not dependencies of the established manuscript spine.
- The three OpenAI Thorp source files and Apache-2.0 license match the pinned upstream OpenAI commit exactly.

## Verification performed for this repository import

- All seven main Long manuscripts and both working branches compile with `latexmk` under TeX Live 2025 without undefined references, undefined citations, multiply defined labels, or overfull boxes. The residual-mass paper has two nonfatal underfull-box diagnostics.
- First-page renders of all eight Long documents were inspected for title-page clipping, missing glyphs, and obvious layout failures.
- The exact Thorp audit program verifies 156 identities for dimensions 2 through 5.
- README math is linted to use GitHub dollar delimiters; custom manuscript macros and alternative TeX math delimiters are forbidden in the README.
- Freshly compiled PDFs were compared with the recovered uploaded PDFs. Papers I, V, VI, and the one-shuffle Edgeworth working branch have identical extracted text; Papers II, III, IV, and the functional Luce branch differ only by the intentional author-line insertion described above.
- The GitHub Actions workflow rebuilds every committed PDF from a clean checkout and requires byte-for-byte equality with the committed snapshot. It also verifies source hashes, PDF hashes, local links, and README math syntax.

## Paper VIII integration (9 October 2026)

Added `papers/08-thorp-cycle-universality/` together with a deterministic compiled PDF, source hash in the build manifest, the standalone reproduction script and frozen finite audit provenance. The code checks finite identities; it is not a substitute for mathematical refereeing. The theorem statements and numerical regimes are distinguished from the external OpenAI Thorp mixing manuscript. The historical import validation section above describes the earlier seven-paper snapshot, not a new independent audit of Paper VIII.

## Canonical-link reconciliation (11 October 2026)

This documentation-only change identifies the dedicated Luce/Tsetlin repository as the canonical editing destination, distinguishes the rejected historical total-cycle candidate from the later functional and quantitative proofs, and leaves every historical source and compiled PDF unchanged. The local build and verification pipeline remains responsible for the preserved snapshots recorded in this repository.
