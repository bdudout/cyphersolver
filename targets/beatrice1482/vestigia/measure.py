# One measurement: decode held-out pass-B transcription with frozen K_V, compare to reference; 200 within-class shuffles.
import sys, json, re, random
kv=json.load(open(sys.argv[1])); K=kv['key']; relabel=kv[sys.argv[4]] if len(sys.argv)>4 else {}
def norm(s):
    s=s.lower().replace('j','i').replace('v','u').replace('y','i').replace('k','c')
    return re.sub('[^a-z ]','',s)
runs=[]
for l in open(sys.argv[2],encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    runs.append([relabel.get(t,t) for t in l.split('|')[2].replace('/',' ').split()])
refs=[norm(l.rstrip('\n')) for l in open(sys.argv[3],encoding='utf-8')]
assert len(runs)==len(refs)
def lev_align(a,b):
    n,m=len(a),len(b); D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0]=i
    for j in range(m+1): D[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(a[i-1]!=b[j-1]))
    i,j=n,m; ok=[False]*m; ins_after=[0]*(m+1)
    while i>0 or j>0:
        if i>0 and j>0 and D[i][j]==D[i-1][j-1]+(a[i-1]!=b[j-1]):
            if a[i-1]==b[j-1]: ok[j-1]=True
            i-=1;j-=1
        elif i>0 and D[i][j]==D[i-1][j]+1: ins_after[j]+=1; i-=1
        else: j-=1
    return ok,ins_after
def score(key):
    M=R=Dl=0; wok=wn=0
    for toks,ref in zip(runs,refs):
        d=''.join(key.get(t,'?') for t in toks)
        r=ref.replace(' ','')
        ok,ins=lev_align(d,r); M+=sum(ok); R+=len(r); Dl+=len(d)
        p=0
        for w in ref.split():
            wn+=1; span=range(p,p+len(w))
            if all(ok[x] for x in span) and all(ins[x]==0 for x in range(p+1,p+len(w))): wok+=1
            p+=len(w)
    return M/max(R,1), M/max(Dl,1), wok/max(wn,1), R, Dl
real=score(K)
cls={c:[s for s in K if s in kv['classes'][c]] for c in ('nomen','multi')}
cls['single']=[s for s,v in K.items() if len(v)==1 and v!='?' and s not in cls['nomen']+cls['multi']]
rng=random.Random(20261114); ctrl=[]
for _ in range(200):
    k2=dict(K)
    for c,syms in cls.items():
        vals=[K[s] for s in syms]; rng.shuffle(vals); k2.update(zip(syms,vals))
    ctrl.append(score(k2))
best=max(c[0] for c in ctrl); ntok=sum(len(r) for r in runs)
print(f'signs={ntok} ref_chars={real[3]} decoded_chars={real[4]}')
print(f'REAL char={real[0]:.3f} precision={real[1]:.3f} words={real[2]:.3f}')
print(f'CONTROLS best char={best:.3f} mean={sum(c[0] for c in ctrl)/200:.3f} best words={max(c[2] for c in ctrl):.3f}')
print('PASS' if real[0]>=0.85 and real[0]>=best+0.30 else 'FAIL', 'thresholds: >=0.85 and >= best+0.30')
