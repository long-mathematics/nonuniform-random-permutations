#!/usr/bin/env python3
"""Exact finite checks for the additions; not a proof of asymptotic claims."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path
import json

def scalar_remainders() -> int:
    tests=0
    for n in range(101):
        for k in range(1,33):
            value=sum((-1)**j*comb(n,j) for j in range(min(n,k-1)+1))
            target=int(n==0)
            remainder=comb(n,k) if n>=k else 0
            assert abs(value-target)<=remainder
            tests+=1
    return tests

def selected_remainders() -> int:
    tests=0
    for M in range(51):
        for p in range(1,18):
            for q in range(min(M,p-1)+1):
                n=M-q
                approx=sum((-1)**j*comb(n,j) for j in range(min(n,p-q-1)+1))
                selected=comb(M,q)
                lhs=selected*abs(approx-int(n==0))
                # (M)_p/[q!(p-q)!] = binom(M,p) binom(p,q)
                rhs=comb(M,p)*comb(p,q) if M>=p else 0
                assert lhs<=rhs
                tests+=1
    return tests

def primitive_necklaces(r: int) -> int:
    primitive=0
    for word in range(1<<r):
        bits=tuple((word>>(r-1-j))&1 for j in range(r))
        if all(any(bits[j]!=bits[(j+a)%r] for j in range(r)) for a in range(1,r)):
            primitive+=1
    assert primitive%r==0
    return primitive//r

def short_cycles() -> list[dict]:
    results=[]
    for d in range(2,6):
        N=1<<d; nctx=N//2; mask=nctx-1; b=(d+1)//2
        envs=1<<nctx
        marginals={r:Counter() for r in range(1,d)}
        joint=Counter()
        for f in range(envs):
            seen=bytearray(N); cycles=Counter()
            for x in range(N):
                if seen[x]: continue
                y=x; length=0
                while not seen[y]:
                    seen[y]=1; length+=1
                    u=y&mask
                    y=(u<<1)|((y>>(d-1))^((f>>u)&1))
                cycles[length]+=1
            for r in marginals:marginals[r][cycles[r]]+=1
            joint[tuple(cycles[r] for r in range(1,b+1))]+=1
        expected={}
        for r in marginals:
            eta=primitive_necklaces(r); denom=1<<r
            pmf={j:Fraction(comb(eta,j)*(denom-1)**(eta-j),denom**eta) for j in range(eta+1)}
            assert {j:Fraction(c,envs) for j,c in marginals[r].items()}==pmf
            expected[r]=pmf
        joint_checked=0
        for vals in product(*(range(len(expected[r])) for r in range(1,b+1))):
            p=Fraction(1)
            for r,j in enumerate(vals,1):p*=expected[r][j]
            assert Fraction(joint.get(vals,0),envs)==p
            joint_checked+=1
        assert sum(joint.values())==envs
        results.append({'d':d,'feedback_environments':envs,'marginals_checked':d-1,'independent_lengths':b,'joint_atoms_checked':joint_checked})
    return results

def chebyshev_products() -> int:
    maxn=300
    primes=[]
    for p in range(2,2*maxn+1):
        if all(p%q for q in primes if q*q<=p):primes.append(p)
    for n in range(1,maxn+1):
        prime_product=1
        for p in primes:
            if p>2*n:break
            v=p; cnt=0
            while v<=2*n:
                cnt+=int(v>n);v*=p
            assert cnt<=1
            if cnt:prime_product*=p
        assert comb(2*n,n)%prime_product==0
    return maxn

def closing_only_regression() -> dict:
    d=3
    word=(1,0,1,1);r=len(word)
    windows=[tuple(word[(i+j)%r] for j in range(d)) for i in range(r)]
    contexts=[tuple(word[(i+1+j)%r] for j in range(d-1)) for i in range(r)]
    assert len(set(windows))==r
    seen=set();J=K=closing_only=0
    open_contexts=set(contexts[:r-d])
    for i,u in enumerate(contexts):
        repeated=u in seen
        if i<r-d:J+=repeated
        else:
            K+=repeated
            closing_only+=repeated and u not in open_contexts
        seen.add(u)
    m=r-len(seen)
    assert J+K==m and K==1 and closing_only==1
    return {'d':d,'word':''.join(map(str,word)),'open_repeats_J':J,'closing_repeats_K':K,'repeats_known_only_from_earlier_closing_query':closing_only,'total_repeated_contexts':m}

if __name__=='__main__':
    report={
      'status':'passed',
      'scope':'Exact finite identities for the newly added statements; no asymptotic theorem is inferred from these checks.',
      'scalar_inclusion_exclusion_cases':scalar_remainders(),
      'selected_occurrence_remainder_cases':selected_remainders(),
      'short_cycle_checks':short_cycles(),
      'chebyshev_prime_product_cases':chebyshev_products(),
      'closing_query_definition_regression':closing_only_regression(),
    }
    print(json.dumps(report,indent=2))
