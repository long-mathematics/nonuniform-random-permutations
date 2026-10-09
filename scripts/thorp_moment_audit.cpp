// Exact finite verification of the rooted cyclic-word factorial-moment identity
// for one physical Thorp shuffle, dimensions d=2,3,4,5.
//
// Compile and run:
//   g++ -std=c++17 -O2 thorp_moment_audit.cpp -o thorp_moment_audit
//   ./thorp_moment_audit
//
// For cycle lengths r_1,...,r_k with multiplicities a_r, the identity checked is
//   (product r_j) * sum_f product_r (C_r(T_f))_{a_r}
//       = sum_valid_words 2^(2^(d-1) - number_of_distinct_contexts).
// A word assignment is valid exactly when all cyclic d-bit windows are distinct.
// Both sides count rooted, distinguished cycle configurations and feedback
// functions; all comparisons use exact integer arithmetic.
//
// The dimension and test-length limits below are intentional: exhaustive
// enumeration grows doubly exponentially with d. These finite checks do not
// establish any asymptotic distributional theorem.

#include <cstdint>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
struct Test{std::vector<int> r;};
int main(){
unsigned total=0;
for(int d=2;d<=5;++d){
 int n=1<<d,m=n/2;uint64_t nf=1ULL<<m;
 std::vector<std::vector<int>> counts(nf,std::vector<int>(n+1));
 for(uint64_t f=0;f<nf;++f){uint64_t seen=0;for(int x=0;x<n;++x){if((seen>>x)&1)continue;int y=x,r=0;do{seen|=1ULL<<y;++r;int v=y&(m-1);y=2*v+((y/m)^((f>>v)&1));}while(y!=x);++counts[f][r];}}
 std::vector<Test> ts;
 for(int r=1;r<=std::min(n,16);++r)ts.push_back({{r}});
 for(int r=1;r<=6;++r)for(int s=r;s<=6;++s)if(r+s<=n)ts.push_back({{r,s}});
 for(int r=1;r<=4;++r)for(int s=r;s<=4;++s)for(int t=s;t<=4;++t)if(r+s+t<=std::min(n,10))ts.push_back({{r,s,t}});
 for(const auto& test:ts){int L=0;uint64_t rootfactor=1;std::map<int,int> multi;for(int r:test.r){L+=r;rootfactor*=r;++multi[r];}
  uint64_t fs=0;for(const auto& c:counts){uint64_t v=1;for(auto [r,a]:multi){if(c[r]<a){v=0;break;}for(int j=0;j<a;++j)v*=c[r]-j;}fs+=v;}
  uint64_t ws=0;
  for(uint64_t w=0;w<(1ULL<<L);++w){uint64_t states=0,contexts=0;bool ok=true;int offset=0;for(int r:test.r){for(int j=0;j<r;++j){int v=0;for(int t=0;t<d;++t)v=2*v+((w>>(offset+(j+t)%r))&1);if((states>>v)&1){ok=false;break;}states|=1ULL<<v;contexts|=1ULL<<(v&(m-1));}offset+=r;if(!ok)break;}if(ok)ws+=1ULL<<(m-__builtin_popcountll(contexts));}
  if(ws!=rootfactor*fs){std::cerr<<"FAIL d="<<d<<" L="<<L<<" words="<<ws<<" functions="<<rootfactor*fs<<"\n";return 1;}++total;
 }
 std::cout<<"d="<<d<<": "<<nf<<" functions, "<<ts.size()<<" moment identities verified exactly\n";
}
std::cout<<"Total exact checks: "<<total<<"\n";
}
