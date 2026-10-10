# Thorp one-shuffle cycles: entropy audit and a refined near-birthday bound

## Scope and status

This note audits the uploaded `thorp_birthday_scale.md` and derives a quantitative refinement of its sparse/dense entropy argument. The entropy proof does not use the protected-cut extension of the Arratia–Canfield–Hales editing theorem. It therefore gives a separate route to the fixed-exponent range below one half. The full one-shuffle Erdős–Turán conjecture is not proved here.

For $N=2^d$, let $T_f(x,u)=(u,x\oplus f(u))$, where the feedback values are independent fair bits chosen once. Write $C_r$ for its number of $r$-cycles. Throughout the entropy calculation logarithms are base two; logarithms of permutation order are natural logarithms.

**Refined theorem.** There is an absolute constant $C$ such that, for all sufficiently large $d$ and $2d\le b\le\sqrt N$,

$$
d_{\mathrm{TV}}\!\left(\mathcal L((C_r)_{2d\le r\le b}),\bigotimes_{r=2d}^b\operatorname{Poisson}(1/r)\right)
\le C d^4(\log_2d)^4\frac{b^2}{N}.
$$

Thus the approximation tends to zero when $b=o(\sqrt N/[d^2(\log_2d)^2])$. In particular, it applies to $b=N^\alpha$ for every fixed $0<\alpha<1/2$.

The structural idea is the sparse/dense split in the uploaded note. The refinement below uses the fact that empirical block counts sum to the word length, improving the bound on the number of possible types.

## 1. Exact weighted-word and closing identities

For one rooted cyclic word of length $r$, or a distinguished ordered pair of lengths $r,s$, put $L=r$ or $L=r+s$. Let $A_d$ mean that all cyclic length-$d$ windows across the family are distinct. A context is a length-$(d-1)$ window. On $A_d$ a context occurs at most twice. Write $m=L-v$ for the number of repeated contexts, where $v$ is the number of distinct contexts.

If a context is repeated, distinctness of the preceding $d$-windows forces the preceding bits to differ. Distinctness of the succeeding $d$-windows forces the following bits to differ too. Hence the repeated prescriptions of the feedback bit agree. A valid family therefore occurs with probability $2^{-v}$.

Let $Q^{(m)}$ be its total normalized rooted-word weight. Then

$$Q^{(m)}=2^{m-L}\#\{\text{valid rooted families with parameter }m\}.$$

For one cycle, $Q_d(r)=\sum_mQ^{(m)}=r\mathbb EC_r$. For a pair restricted to individually context-simple cycles, the sum over $m\ge1$ is $rs\,\mathbb EX_{r,s}$, where $X_{r,s}$ counts ordered distinct context-simple cycles sharing a context.

In the forced experiment, explore $r-d$ open steps and prescribe the final $d$ output bits to equal the starting state. Sample unqueried feedback bits fairly during open steps; during closure assign fresh values to enforce the prescribed output. Never change an already queried value. Incompatible closures, premature closures, and intersections are rejected. For a pair explore the shorter cycle first.

Let $V$ be the number of already known closing queries. For a specified successful history with $v$ distinct feedback queries, ordinary probability is $N^{-k}2^{-v}$ and forced probability is

$$N^{-k}2^{-(v-(kd-V))}=2^{-v-V},\qquad k=1\text{ or }2.$$

Thus, writing $a(F)=\mathbb E_{\mathrm{roots}}2^{-V}$ for a fixed unrooted family,

$$\mathbb P_*(E_m)=\sum_{F\in E_m}\operatorname{weight}(F)\,a(F).$$

For one cycle $\mathbb E_{\mathrm{roots}}V\le2dm/r$. For a context-simple pair $r\le s$, the first cycle has no known closing queries and $\mathbb E_{\mathrm{roots}}V=dm/s\le2dm/L$. Jensen's inequality therefore gives

$$Q^{(m)}\le2^{2dm/L}\mathbb P_*(E_m).\tag{1}$$

Before the first repeated query the forced experiment agrees with independent fair cyclic seed words. Consequently,

$$\sum_{m\ge1}\mathbb P_*(E_m)\le\frac{r(r-1)}N\quad\text{for one cycle},\tag{2}$$

and

$$\sum_{m\ge1}\mathbb P_*(E_m)\le\frac{2rs}N\quad\text{for an intersecting context-simple pair}.\tag{3}$$

The assumptions $r,s\ge2d$ guarantee the needed collision probabilities. On one circle of length $r$ the equality constraints for contexts at displacement $a$ have rank $\min(d-1,r-\gcd(r,a))=d-1$. Across two independent circles each context is uniform, so an equality also has probability $2^{-(d-1)}$.

## 2. The type-counting and mixture steps

For a cyclic word $w$ of length $n$, let $H_h(w)$ be the empirical length-$h$ block entropy and $\delta_h(w)=H_h(w)-H_{h-1}(w)$.

For a prescribed $h$-type, its empirical transition probabilities give every word in the type probability at least $n^{-1}2^{-n\delta_h}$ under the associated Markov law: the initial block has mass at least $1/n$, and removing wraparound transition factors can only increase the product. Therefore

$$\#\{\text{rooted words of a fixed }h\text{-type}\}\le n2^{n\delta_h}.\tag{4}$$

For a valid one-cycle word, $H_d=\log_2L$ and $\delta_d=2m/L$. For a valid pair use the mixture obtained by choosing uniformly among all $L=r+s$ positions. The same equalities hold.

To justify the pair type bound, let $J$ identify the chosen circle, let $X$ be the preceding $h-1$ bits, and let $Y$ be the following bit. Then

$$\delta_h^{\rm mix}-\frac rL\delta_h(w_1)-\frac sL\delta_h(w_2)
=H(Y\mid X)-H(Y\mid X,J)=I(Y;J\mid X)\ge0.\tag{5}$$

Thus pairs in a fixed pair of types number at most

$$rs\,2^{r\delta_h(w_1)+s\delta_h(w_2)}\le rs\,2^{L\delta_h^{\rm mix}}.$$

This proves the concavity step for unequal lengths, without a computational hypothesis.

Stationarity makes the entropy increments nonincreasing. Therefore, in either case,

$$\delta_h\le\frac{H_h}{h}\le\frac1h\left(\log_2L-\frac{2m(d-h)}L\right).\tag{6}$$

These establish the substantive entropy lemmas in the uploaded note.

## 3. Counting types more tightly

Set $M=2^h$. A cyclic $h$-type consists of $M$ nonnegative integer counts summing to $n$. Ignoring the additional cyclic consistency constraints only enlarges their number, so

$$\#\{h\text{-types of length }n\}\le\binom{n+M-1}{M-1}\le\left[e\left(1+\frac nM\right)\right]^M.\tag{7}$$

For one or two words, each of length at most $L$, the logarithm of the number of type choices is at most

$$S=2M\log_2\!\left[e\left(1+\frac LM\right)\right].$$

Combining (4), (6), (7), and the rooted prefactor at most $L^2$ gives

$$\log_2Q^{(m)}\le\frac{Lt}{h}+S+2\log_2L-\kappa m,\qquad
t=\log_2L-h,\quad\kappa=\frac{2d-3h}{h}.\tag{8}$$

## 4. Dense families and the improved sparse penalty

Assume $d^4\le L\le2\sqrt N$. Put $q=\log_2d$ and

$$h=\left\lfloor\log_2L-\log_2d-\log_2q\right\rfloor.$$

For sufficiently large $d$,

$$2\le h\le d/2,\qquad\kappa\ge1,$$

and

$$q+\log_2q\le t<q+\log_2q+1,\qquad
\frac{L}{2dq}<M\le\frac{L}{dq}.$$

As $\log_2[e(1+2dq)]\le2q$ for sufficiently large $d$, we have

$$S\le\frac{4L}{d}.$$

Define

$$F=\frac{Lt}{h}+\frac{4L}{d}+2\log_2L,\qquad
m_0=\left\lceil\frac{F+L/d}{\kappa}\right\rceil.$$

Equation (8) yields the summable dense tail

$$\sum_{m\ge m_0}Q^{(m)}
\le\frac{2^{-L/d}}{1-2^{-\kappa}}
\le2^{1-L/d}\le2^{1-d^3}.\tag{9}$$

For the sparse part, (1) costs at most $\Pi=2^{2dm_0/L}$. Expanding its logarithm,

$$\log_2\Pi
\le\frac{2d}{2d-3h}\left(t+\frac{5h}{d}+\frac{2h\log_2L}{L}\right)+\frac{2d}{L}.$$

Here $2d/(2d-3h)\le4$, $5h/d\le5/2$, and $2h\log_2L/L\le1$. Also $2d/L\le1$. Hence

$$\log_2\Pi\le4t+15\le4\log_2d+4\log_2q+19.$$

In particular,

$$\Pi\le2^{20}d^4q^4.\tag{10}$$

Combining (2), (3), (9), and (10),

$$\mathbb EC_r^{\rm rep}\le\Pi\frac{r-1}{N}+\frac{2^{1-r/d}}r\qquad(r\ge d^4),\tag{11}$$

and

$$\mathbb EX_{r,s}\le\frac{2\Pi}{N}+\frac{2^{1-(r+s)/d}}{rs}
\qquad(r+s\ge d^4).\tag{12}$$

## 5. Small lengths and the Poisson-process transfer

The earlier closing estimates suffice below $d^4$:

$$\mathbb EC_r^{\rm rep}\le\frac{r(r-1)}N,\qquad
\mathbb EX_{r,s}\le\frac{4\sqrt{rs}}N.\tag{13}$$

For clarity, the second bound follows by mixing the two cycles with equal cycle weights, not equal position weights. Its block entropy is $1+\tfrac12\log_2(rs)$, while each shared context contributes at least $1/s$ to its final increment. Thus $a(F)\ge1/(2\sqrt{rs})$, and (3) gives (13). For one cycle the same entropy argument gives $a(F)\ge1/r$.

Using (13) only on the short ranges costs $O(d^4b^2/N)$: for one cycle bound $r^2\le d^4r$, and for a pair with $r+s<d^4$ use $\sqrt{rs}\le d^4/2$. This is important when sharpening the logarithmic factor; summing prematurely to $d^4$ would create an unnecessary standalone $d^{12}/N$ term.

For each potential context-simple necklace $\gamma$ of length $r$, its occurrence indicator has mean $2^{-r}$. Its dependency neighborhood consists of necklaces sharing a context. Indicators outside that neighborhood depend on a disjoint set of independent feedback bits, so the external-dependence term is zero.

The point-process Poisson approximation theorem of Arratia–Goldstein–Gordon bounds the total-variation error by a constant times $b_1+b_2$. Rooted-word counting gives $b_1\le2b^2/N$. Equations (12)–(13) give

$$b_2\le\sum_{r,s}\mathbb EX_{r,s}=O(d^4q^4b^2/N).$$

Equations (11)–(13) give the same bound for the probability that a non-context-simple cycle appears in the range.

If $\lambda_r$ is the mean of context-simple $r$-cycles and $\delta_d(r)$ is the unweighted cyclic-word context-collision probability, then

$$r\lambda_r=1-\delta_d(r),\qquad
0\le1/r-\lambda_r\le(r-1)/N.$$

The sum of the differences in Poisson means is $O(b^2/N)$. Dense-tail remainders sum to at most $O(d^2 2^{-d^3})$ and are absorbed. This proves the refined theorem.

## 6. Erdős–Turán consequences

For each fixed $0<\alpha<1/2$ and $b=\lfloor N^\alpha\rfloor$, the logarithmic order contributed by cycles of length at most $b$ has the classical normalization at scale $b$:

$$\frac{\log\operatorname{lcm}\{r\le b:C_r>0\}-\tfrac12(\log b)^2}
{\sqrt{(\log b)^3/3}}\Longrightarrow N(0,1).$$

The functional count/order theorem holds on every fixed interval $[0,\alpha]$, $\alpha<1/2$, by the same independent-Poisson coupling and product-to-LCM transfer as in the preceding notes.

For a cutoff approaching the birthday scale, take

$$b_d=\left\lfloor\frac{\sqrt N}{d^2(\log_2d)^3}\right\rfloor.$$

The approximation error is $O((\log_2d)^{-2})$. At this cutoff the scalar limit can also be written

$$\frac{\log\operatorname{lcm}\{r\le b_d:C_r>0\}-\tfrac18(\log N)^2}
{\sqrt{(\log N)^3/24}}\Longrightarrow N(0,1).$$

The centering change is $O((\log N)\log d)$, negligible relative to $(\log N)^{3/2}$.

These are truncated order laws, not the full one-shuffle order theorem.

## 7. A priori bound beyond the birthday scale

Fix $0<\beta<2/3$ and take $d^4\le r\le N^\beta$. The same choice of $h$ has $h\le\beta d$ and

$$\kappa\ge(2-3\beta)/\beta>0.$$

The dense tail is at most $C_\beta2^{-r/d}$. The sparse penalty satisfies

$$\log_2\Pi\le\frac{2}{2-3\beta}\bigl(\log_2d+\log_2\log_2d\bigr)+O_\beta(1).$$

Since forced success probability is at most one,

$$Q_d(r)\le C_\beta(d\log_2d)^{2/(2-3\beta)},\qquad
\mathbb EC_r\le\frac{C_\beta(d\log_2d)^{2/(2-3\beta)}}r.$$

This strengthens the logarithmic factor in the uploaded note's upper bound, but does not give $Q_d(r)\to1$.

## 8. An exact target for the next step

Let $S_d(r)=\mathbb P_*(\text{successful forced closure of length }r)$. Root averaging and $1-2^{-x}\le(\log 2)x$ give

$$0\le Q_d(r)-S_d(r)\le\frac{2d\log 2}{r}\sum_{m\ge0}mQ_d^{(m)}(r).$$

Therefore the two assertions

$$S_d(r)=1-o(1),\qquad\frac dr\sum_m mQ_d^{(m)}(r)=o(1)$$

would imply $Q_d(r)=1+o(1)$. Neither assertion is established here above the birthday scale. Moreover, first moments alone would still not prove the full Erdős–Turán theorem; joint correlations remain necessary.

## 9. Audit-code findings and independent checks

The uploaded script uses `Fraction` for weighted sums, but it converts the graded inequalities to floats, evaluates entropies with floating-point logarithms, and groups types by randomized integer keys. Therefore its description as entirely exact rational verification needs qualification. Some listed pair cases have no successful context-simple pair and hence test the graded pair bound vacuously.

The accompanying `thorp_entropy_independent_audit.py` instead exponentiates entropy inequalities into integer inequalities and uses exact type tuples. It checks:

- 24 cycle-intensity identities in dimensions 3 and 4 against all 16 and 256 feedback functions, respectively;
- 2,661 complete empirical type classes;
- single-word entropy deficits and root penalties;
- 4,840 valid ordered pairs of unrooted cycles, including 4,178 pairs sharing contexts;
- 29,022 exact conditional-entropy concavity comparisons and the same number of mixture-deficit comparisons.

All executed checks passed. These finite checks validate ingredients only; they are not a proof of an asymptotic theorem and do not certify the separate protected-cut claim.

## References and provenance

The sparse/dense method and original $d^{48}$ estimate are from the uploaded `thorp_birthday_scale.md`, Part II. The refined type count, the $d^4(\log d)^4$ bound, and the sharpened upper bound in Section 7 are derived in this note.

R. Arratia, L. Goldstein, and L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science 5 (1990), 403–434, Theorem 2 (point-process approximation). Section 4.6 also distinguishes the birthday-scale breakdown of microscopic cycle-indicator approximation from the larger range of cycle-count approximation for uniform permutations.
