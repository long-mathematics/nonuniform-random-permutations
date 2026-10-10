# Proposed additions and corrections to the Thorp manuscript

**Basis:** `thorp_alpha_lt_two_thirds_reviewed_v1.md`, together with the earlier quantitative birthday-scale note. This document does not replace or modify the preserved version 1 manuscript. Results below labeled as corollaries are deductions from its main fixed-order moment theorem, with the closing-query definition corrected as specified in Section 1. They are not assertions that the full Erdős–Turán conjecture has been proved. Priority for their specific Thorp formulations has not been exhaustively researched.

Throughout, N=2^d, and C_r is the number of r-cycles of one physical Thorp shuffle. Logarithms are natural except where log_2 is written.

## 1. Necessary corrections and clarifications

### 1.1 Definition of the closing-query count

Replace the present definition of K in Section 5 by:

> K is the number of closing queries whose feedback value has already been fixed strictly before the query is made. This includes values fixed by earlier marked cycles, by the current open path, or by an earlier query in the current closing segment.

Place this definition before the density identity. In particular, an internal repeated context with both occurrences in the closing segment contributes one to K. The identity J+K=m_new and the atom weight 2^{-v-K} use this complete definition.

### 1.2 The integration step after (5.3)

Let A_sp be the sparse class, let mu=mu_{a,r}, nu=nu_{a;r}, and H=H_{k,beta}. The missing chain is

$$
\frac{a_r}{H}\int_{A_{\rm sp}}m_{\rm new}\,d\mu
\le \int_{A_{\rm sp}}J2^{-K}\,d\mu
=\int_{A_{\rm sp}}J\,d\nu
\le \mathbb E_{\mu_{\mathbf a},X}J.
$$

The sparse class and m_new are invariant under re-rooting the last cycle. The first inequality follows by integrating the root-averaged inequality (5.3). The last inequality uses the ordinary law of the open part and restricts to successful histories; no claim of ordinary law after forced closure is needed.

### 1.3 Reverse queries

A backward step from y=(u,z) has predecessor (z xor f(u),u), so it queries f(u), the same feedback entry as the forward step into y. Thus reverse-time reuse controls exactly the relevant forward-context contacts.

### 1.4 Scope and presentation

The lower bound's numerical constant depends on k, not beta; the size from which it holds depends on beta through the previously proved bound Q_d(h)<=2. The moment comparison is initially for lengths in [4d,b]; shorter lengths are removed using the upper bound and negligible expectations.

Remove conversion artifacts such as `cycle'$s$`, `Markov'$s$`, mixed text/math parentheses, and bare `kappa`. Move review labels, audit-history language, and the detailed computational appendix into the repository documentation. Keep a brief reproducibility remark and a precise statement of the mathematical scope in the paper.

## 2. Poisson approximation on sets of bounded harmonic mass

### Corollary A

Fix 0<alpha<2/3. Let I_d be any subset of the integers in [4d,N^alpha], and suppose

$$\lambda_d=\sum_{r\in I_d}\frac1r\le\Lambda<\infty.$$

Then

$$
 d_{\rm TV}\!\left(\mathcal L((C_r)_{r\in I_d}),
 \bigotimes_{r\in I_d}{\rm Poisson}(1/r)\right)\longrightarrow0.
$$

The number of coordinates |I_d| may tend to infinity. This is a qualitative result, with no rate claimed uniformly as the harmonic mass grows. In particular, it applies to a fixed finite union of multiplicative length windows, including windows above the birthday scale.

### 2.1 A finite inclusion-exclusion comparison

Here is a useful general lemma proving the corollary. Let X=(X_i) on a finite set I be a vector of nonnegative integers, let Y_i be independent Poisson variables of means lambda_i, and let lambda=sum lambda_i. Define the ordered factorial moment measures

$$
 \mu_j(i_1,\ldots,i_j)=\mathbb E\prod_{i\in I}(X_i)_{a_i},
 \qquad a_i=\#\{v:i_v=i\},
$$

and let pi_j(i_1,...,i_j)=prod_v lambda_{i_v}. Thus mu_0=pi_0=1. Write ||.||_1 for the total absolute mass of a signed measure. For every integer p>=1,

$$
 d_{\rm TV}(\mathcal L(X),\mathcal L(Y))
 \le
 \sum_{j=1}^{p-1}\frac{2^j}{j!}\|\mu_j-\pi_j\|_1
 +\frac{2^p}{p!}\left(\mu_p(I^p)+\lambda^p\right). \tag{A1}
$$

**Proof.** Put M=sum X_i. For a test function F on configurations with 0<=F<=1, decompose its expectation according to M=q. For q<p, use the symmetric test

$$F_q(i_1,\ldots,i_q)=F\!\left(\sum_{v=1}^q\delta_{i_v}\right).$$

On each ordered q-tuple of distinct occurrences, approximate the event that no unselected occurrences remain by

$$\sum_{j=0}^{p-q-1}\frac{(-1)^j}{j!}(M-q)_j.$$

For n=M-q>=0, the difference between this expression and 1_{n=0} has absolute value at most (n)_{p-q}/(p-q)!. After integrating and dividing by q!, the error is at most mu_p(I^p)/(q!(p-q)!). The omitted event M>=p has probability at most mu_p(I^p)/p!. Summing q=0,...,p-1 bounds the entire remainder by 2^p mu_p(I^p)/p!.

Do the same for the independent Poisson vector. The term of total factorial order j in the difference of the truncated expansions has coefficient bounded by

$$\sum_{q=0}^j\frac1{q!(j-q)!}=\frac{2^j}{j!}.$$

Taking the supremum over indicator tests F proves (A1).

### 2.2 Application to cycle counts

Choose alpha<beta<2/3. For each fixed j, the main theorem applies eventually to every ordered list of j lengths from I_d, since j N^alpha<=N^beta. Thus, with epsilon_{d,j}->0,

$$
 |Q_d(r_1,\ldots,r_j)-1|\le\varepsilon_{d,j}.
$$

For the factorial moment measures of the cycle vector,

$$
 \|\mu_j-\pi_j\|_1\le\varepsilon_{d,j}\lambda_d^j,
 \qquad
 \mu_j(I_d^j)\le(1+\varepsilon_{d,j})\lambda_d^j.
$$

Consequently (A1) gives

$$
 d_{\rm TV}\le
 \sum_{j=1}^{p-1}\frac{(2\Lambda)^j}{j!}\varepsilon_{d,j}
 +\frac{(2\Lambda)^p}{p!}(2+\varepsilon_{d,p}). \tag{A2}
$$

First send d to infinity with p fixed, then p to infinity. The result follows. This order of limits does not require a theorem uniform in moment order.

The scalar finite-binomial remainder used above was checked in 15,680 integer cases. This is only a check of the algebraic remainder inequality; the proof is the displayed finite inclusion-exclusion calculation.

## 3. Scale-invariant Poisson cycle process

### Corollary B

Suppose a_d/d tends to infinity and a_d<=N^alpha for a fixed alpha<2/3. Define

$$\Xi_d=\sum_{r=1}^N C_r\,\delta_{r/a_d}.$$

Then, vaguely in distribution as locally finite counting measures on (0,infinity),

$$\Xi_d\Longrightarrow\Xi,\qquad \Xi\sim{\rm PPP}(dx/x).$$

**Proof.** On a compact interval [c,C] subset (0,infinity), all relevant lengths exceed 4d eventually and are at most C N^alpha. Choose a slightly larger fixed exponent below 2/3 to apply Corollary A. The harmonic mass is bounded and

$$\sum_{r/a_d\in(c,C]}1/r\longrightarrow\log(C/c).$$

The independent discrete Poisson intensity measures converge vaguely to dx/x; their Laplace functionals, and hence their point processes, converge. Corollary A transfers this convergence on every compact interval. Tightness on compact intervals also follows from the bounded expected counts. This proves the claim.

For example, if b=floor(N^alpha), then

$$\sum_{b<r\le2b}C_r\Longrightarrow{\rm Poisson}(\log2).$$

For a fixed number of disjoint multiplicative windows, even on widely separated scales, the limiting counts are independent, with means equal to the logarithms of their endpoint ratios.

This corollary concerns moving mesoscopic windows, not the macroscopic regime r comparable to N. In particular, it does not apply to the top window (N/2,N], which contains at most one cycle.

## 4. A Dickman limit and a truncated maximum law

Fix 0<alpha<2/3 and b=floor(N^alpha). Let

$$T_d(b)=\frac1b\sum_{r\le b}rC_r.$$

### Corollary C

$$T_d(b)\Longrightarrow D,$$

where D is the standard Dickman variable specified unambiguously by

$$
 \mathbb E e^{-tD}
 =\exp\!\left\{\int_0^1\frac{e^{-tx}-1}{x}\,dx\right\},\qquad t\ge0.
$$

Equivalently D=sum_{x in Xi cap (0,1]} x for the Poisson process in Corollary B. The limit has mean 1 and variance 1/2.

**Proof.** For fixed epsilon>0, the contribution of cycle lengths in (epsilon b,b] converges by Corollary B and integration on a compact interval. For the omitted part, the all-positive-length one-cycle upper bound gives, for large d,

$$
 \mathbb E\frac1b\sum_{r\le\epsilon b}rC_r
 \le2\epsilon.
$$

The limiting process has expected omitted mass epsilon. Let epsilon decrease to zero, using Markov's inequality to remove the tails. The stated Laplace transform follows from the Poisson Laplace functional. Its first two cumulants are int_0^1 x dx/x=1 and int_0^1 x^2 dx/x=1/2.

### Corollary D

Let

$$R_d(b)=\max(\{r\le b:C_r>0\}\cup\{0\}).$$

Then

$$R_d(b)/b\Longrightarrow{\rm Uniform}(0,1).$$

Indeed, for 0<x<1,

$$
 \mathbb P\{R_d(b)/b\le x\}
 =\mathbb P\!\left\{\sum_{xb<r\le b}C_r=0\right\}
 \longrightarrow \exp[-\log(1/x)]=x.
$$

This is the largest cycle below the prescribed cutoff, not the largest cycle of the entire permutation.

The Poisson-to-Dickman relation is classical. What is derived here is its application to the one-Thorp-shuffle cycle field in the stated mesoscopic range.

## 5. Restore the earlier quantitative birthday-range theorem

The separate note `thorp_entropy_audit_and_refinement.md` contains an additional theorem not stated in reviewed version 1:

$$
 d_{\rm TV}\!\left(
 \mathcal L((C_r)_{2d\le r\le b}),
 \bigotimes_{r=2d}^b{\rm Poisson}(1/r)
 \right)
 \le C d^4(\log_2d)^4 b^2/N,
 \qquad 2d\le b\le\sqrt N.
$$

This is worth including as a distinct quantitative theorem. It controls the complete vector on a range whose harmonic mass diverges, and gives a rate. It is not obtained merely by optimizing the fixed-p argument in Section 2, whose constants are not uniform as p increases. Its proof must be imported explicitly: context-simple necklace indicators, shared-context dependency neighborhoods, one- and two-cycle repeat estimates, and the Arratia–Goldstein–Gordon point-process approximation theorem.

Corollary A and this earlier theorem are complementary. Corollary A gives a qualitative full-vector approximation on bounded-harmonic-mass sets beyond the birthday scale; the earlier theorem gives quantitative approximation on the much broader initial range below that scale.

## 6. Exact short-cycle statement

An optional short proposition can be placed next to Appendix A. Define

$$\eta_r=\frac1r\sum_{a\mid r}\mu(a)2^{r/a}.$$

Then

$$C_r\sim{\rm Binomial}(\eta_r,2^{-r}),\qquad 1\le r\le d-1,$$

and, for d>=2,

$$C_1,\ldots,C_{\lfloor(d+1)/2\rfloor}\quad\hbox{are mutually independent}.$$

**Proof.** For r<=d-1, every primitive necklace has r different contexts, so occurrence has probability 2^{-r}. Distinct necklaces of that same length have disjoint context sets. For two different lengths r,s<=b=floor((d+1)/2),

$$r+s-\gcd(r,s)\le2b-2\le d-1.$$

The wrapped-word comparison lemma in Appendix A therefore says that a common context would force the two periodic extensions to be the same, contradicting their different primitive periods. All relevant necklace indicators depend on disjoint feedback sets.

Credit Stark's published independent-binomial theorem, whose stated range is r<=(d-1)/3. Present the enlarged elementary range as a refinement obtained from the manuscript's periodic-word lemma, not as a newly discovered general binomial phenomenon. No comprehensive priority search for the enlarged endpoint was performed.

## 7. Consequences for the full permutation

Although the full Gaussian conjecture is not proved, monotonicity yields statements about the untruncated permutation. For every epsilon>0,

$$
 \mathbb P\!\left\{
 \log\operatorname{ord}(T_f)
 \ge(2/9-\epsilon)(\log N)^2
 \right\}\longrightarrow1,
$$

and

$$
 \mathbb P\!\left\{
 \sum_{r=1}^N C_r\ge(2/3-\epsilon)\log N
 \right\}\longrightarrow1.
$$

**Proof.** For each fixed alpha<2/3, the functional theorem implies that the normalized truncated logarithmic order tends in probability to alpha^2/2 and the normalized truncated count tends to alpha. Full order and full count dominate their truncated versions. For the given epsilon, choose a fixed alpha sufficiently close to 2/3. No estimate uniform as alpha approaches 2/3 is required.

The one-cycle theorem also gives the local root-length statement

$$N\mathbb P\{L_f(X)=r\}=r\mathbb EC_r=1+o(1)$$

uniformly in the theorem's range for an independent uniform root X. This is a direct restatement of the first-moment estimate, rather than a separate principal theorem.

## 8. General additive statistics and a sharper arithmetic bound

The argument in Section 8 already proves, for bounded piecewise-continuous g on [0,alpha],

$$
 \frac1{\sqrt\ell}\sum_{4d\le r\le N^\alpha}
 g\!\left(\frac{\log r}{\ell}\right)(C_r-1/r)
 \Longrightarrow
 \mathcal N\!\left(0,\int_0^\alpha g(t)^2dt\right),\qquad\ell=\log N.
$$

A fixed finite family of test functions has the corresponding joint Gaussian limit with covariance int g_i g_j. This is best presented as one short general corollary or as the organizing formulation of the Gaussian section, rather than a separate major theorem.

The product-to-LCM estimate can be sharpened to

$$\mathbb E(B_b-O_b)=O(\log b\,\log\log b).$$

Put t=log b and use the existing bound by min(O(t/m),O(t^2/m^2)). Chebyshev's bound psi(x)=sum_{m<=x}Lambda(m)=O(x) and partial summation give

$$
 \sum_{m\le t}\Lambda(m)/m=O(\log t),
 \qquad \sum_{m>t}\Lambda(m)/m^2=O(1/t).
$$

The two parts are O(t log t) and O(t), respectively. This is a quantitative improvement of the discrepancy estimate, not by itself a Berry–Esseen theorem.

## 9. Suggested integration

Keep the fixed-order moment theorem and functional Erdős–Turán theorem as the main results. Add one coherent section on bounded-harmonic-mass Poisson approximation, followed by the scale-invariant process, Dickman mass, and truncated-maximum corollaries. Add the previous quantitative birthday-range theorem in a separate subsection with its actual proof. Keep the exact short-cycle result and the full-order lower bound compact.

Revise the present broad disclaimer about growing-dimensional Poisson approximation: the bounded-harmonic-mass theorem is one such approximation beyond the birthday scale. The unproved claim is approximation of the entire initial vector through N^alpha when alpha>1/2 and its harmonic mass diverges. Do not claim a fixed-parameter theorem at alpha=2/3, a full-order CLT, general growing-order estimates, or tilted decorrelation outside the proved scope.

The preserved reviewed v1 manuscript remains unchanged.

## References to add or update

- R. A. Arratia, E. R. Canfield, and A. W. Hales, *Random feedback shift registers and the limit distribution for largest cycle lengths*, Combinatorics, Probability and Computing **32** (2023), 559–593, DOI 10.1017/S0963548323000020. Use this published citation in addition to the arXiv version where version-specific references are useful.
- D. Stark, *The small cycle counts of random feedback shift registers*, Australasian Journal of Combinatorics **86** (2023), 414–422.
- R. Arratia, *On the central role of scale invariant Poisson processes on (0,infinity)*, manuscript dated 1997, revised 1998; arXiv:1611.05572. This supplies standard context and the unambiguous Poisson-sum definition of the Dickman law.
- C. Bhattacharjee and I. Molchanov, *Convergence to scale-invariant Poisson processes and applications in Dickman approximation*, Electronic Journal of Probability **25** (2020), paper 79; arXiv:1911.06229.
- R. Arratia, L. Goldstein, and L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science **5** (1990), 403–434. Needed if the quantitative birthday-range theorem is included.
