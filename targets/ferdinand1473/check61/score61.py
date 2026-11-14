"""PREREG C05 scorer: key_1473 (Brackx, dec1473.py K) applied to BNE MSS/20211/61 cipher runs,
scored against the period interlinear gloss. Usage: python3 -I score61.py brackx_dec1473.py transcription.txt gloss.txt
transcription.txt: lines 'Rnn tok tok / tok ...' ; gloss.txt: lines 'Rnn group | group | ...'
"""
import re, sys, random, json

def load_key(path):
    src = open(path).read()
    m = re.search(r'K = dict\(pair\.split\("="\) for pair in """(.*?)"""', src, re.S)
    K = {}
    for pair in m.group(1).split():
        s, v = pair.split('=', 1)
        if v.startswith('{'):
            K[s] = ('set', v.strip('{}').split('|'))
        elif v == '[Barcelona]':
            K[s] = ('str', 'barcelona')
        elif v.startswith('['):
            K[s] = ('unk', None)
        else:
            K[s] = ('str', v)
    return K

def norm(s):
    s = s.lower()
    for a, b in (('v', 'u'), ('j', 'i'), ('y', 'i'), ('ç', 'c'), ('ñ', 'n'), ('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u')):
        s = s.replace(a, b)
    return re.sub(r'[^a-z]', '', s)

def expand(tokens, K):
    pos = []
    for t in tokens:
        t = t.rstrip('?')
        if t == '/' or t == '':
            continue
        kv = K.get(t)
        if kv is None or kv[0] == 'unk':
            pos.append(frozenset())
        elif kv[0] == 'set':
            pos.append(frozenset(norm(x) for x in kv[1] if norm(x)))
        else:
            for ch in norm(kv[1]):
                pos.append(frozenset(ch))
    return pos

def semiglobal(g, d):
    # g fully aligned, d free end gaps; cost = edits
    n, m = len(g), len(d)
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            sub = prev[j - 1] + (0 if g[i - 1] in d[j - 1] else 1)
            cur[j] = min(sub, prev[j] + 1, cur[j - 1] + 1)
        prev = cur
    return min(prev)

def score(runs, gloss, K):
    tot = cost = 0; words = found = 0
    for rid, groups in gloss.items():
        d = expand(runs[rid], K)
        for grp in groups:
            g = norm(grp)
            if not g:
                continue
            tot += len(g); cost += semiglobal(g, d)
            for w in grp.split():
                w = norm(w)
                if len(w) >= 2:
                    words += 1; found += (semiglobal(w, d) == 0)
    return 1 - cost / tot, found / max(words, 1), tot, words

def shuffled(K, seed):
    signs = [s for s, v in K.items() if v[0] != 'unk']
    vals = [K[s] for s in signs]
    random.Random(seed).shuffle(vals)
    K2 = dict(K); K2.update(zip(signs, vals)); return K2

if __name__ == '__main__':
    K = load_key(sys.argv[1])
    runs = {}
    for ln in open(sys.argv[2]):
        m = re.match(r'(R\d+[a-z]?)\s+(.*)', ln.strip())
        if m: runs[m.group(1)] = m.group(2).split()
    gloss = {}
    for ln in open(sys.argv[3]):
        m = re.match(r'(R\d+[a-z]?)\s+(.*)', ln.strip())
        if m: gloss[m.group(1)] = [x.strip() for x in m.group(2).split('|') if x.strip()]
    ntok = sum(len([t for t in runs[r] if t != '/']) for r in gloss if r in runs)
    acc, wf, tot, nw = score(runs, gloss, K)
    ctrl = [score(runs, gloss, shuffled(K, s)) for s in range(1, 201)]
    ca = sorted(c[0] for c in ctrl); cw = sorted(c[1] for c in ctrl)
    res = dict(cipher_tokens_in_glossed_runs=ntok, gloss_letters=tot, gloss_words=nw,
               char_acc=round(acc, 4), words_found=round(wf, 4),
               ctrl_char_max=round(ca[-1], 4), ctrl_char_mean=round(sum(ca) / 200, 4),
               ctrl_words_max=round(cw[-1], 4), ctrl_words_mean=round(sum(cw) / 200, 4),
               PASS=(acc >= 0.85 and acc >= ca[-1] + 0.30))
    print(json.dumps(res, indent=1))
