# Build K_V from R1140 only (pass B transcription aligned to the training references).
import sys, json, re, collections
NOMEN = {'G': 'signorredehungaria', 'W': 'venetiani'}
SEED = {'8':'a','V':'a','1':'u','2':'g','3':'i','Z':'z','E':'e','6':'h','7':'o','9':'d','o':'l','L':'s','T':'t',
        'n':'n','m':'m','C':'c','P':'p','U':'p','R':'r','F':'f','X':'x','K':'ss','TT':'tt','=':'q','3E':'ll',
        'PI':'o','d':'b','N1':'ss','N2':'ff','N3':'u'}
def norm(s):
    s=s.lower().replace('j','i').replace('v','u').replace('y','i').replace('k','c')
    return re.sub('[^a-z{}]','',s)
def runs(path):
    out=[]
    for l in open(path,encoding='utf-8'):
        if l.startswith('#') or '|' not in l: continue
        toks=l.split('|')[2].replace('/',' ').split()
        out.append(toks)
    return out
def align(toks, ref, key):
    # DP: each token consumes 0..2 ref letters; ref letters may be skipped
    n,m=len(toks),len(ref); INF=-1e9
    S=[[INF]*(m+1) for _ in range(n+1)]; B=[[None]*(m+1) for _ in range(n+1)]
    S[0][0]=0
    for i in range(n+1):
        for j in range(m+1):
            if S[i][j]==INF: continue
            if j<m and S[i][j]-1>S[i][j+1]: S[i][j+1]=S[i][j]-1; B[i][j+1]=(i,j,None)
            if i<n:
                for k in (0,1,2):
                    if j+k>m: continue
                    seg=ref[j:j+k]; v=key.get(toks[i])
                    sc = (2*max(1,len(seg)) if v==seg and k>0 else (-1 if k==0 else -0.5*k))
                    if S[i][j]+sc>S[i+1][j+k]: S[i+1][j+k]=S[i][j]+sc; B[i+1][j+k]=(i,j,seg)
    i,j=n,m; pairs=[]
    while (i,j)!=(0,0):
        pi,pj,seg=B[i][j]
        if pi!=i: pairs.append((toks[pi],seg))
        i,j=pi,pj
    return pairs[::-1]
toks_runs=runs(sys.argv[1]); refs=[norm(l) for l in open(sys.argv[2],encoding='utf-8')]
assert len(toks_runs)==len(refs),(len(toks_runs),len(refs))
cnt=collections.defaultdict(collections.Counter)
for t,r in zip(toks_runs,refs):
    # split on nomenclator: remove {G}/{W} from ref and G/W from tokens
    tt=[x for x in t if x not in NOMEN]; rr=re.sub(r'\{[GW]\}','',r)
    for tok,seg in align(tt,rr,SEED): cnt[tok][seg]+=1
key={}
for tok,c in sorted(cnt.items()):
    best,n=c.most_common(1)[0]
    print(f'{tok:4} -> {best!r:6} {n}/{sum(c.values())}  {dict(c)}')
    key[tok]=best
key.update(NOMEN)
json.dump(key,open(sys.argv[3],'w'),ensure_ascii=False,indent=0,sort_keys=True)
