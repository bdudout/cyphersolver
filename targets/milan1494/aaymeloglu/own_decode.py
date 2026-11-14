"""Own decoder for the Milan 1494 files (the project's check of issue #589, 14 Nov 2026).

Reads key.json and the two transcriptions in this folder, decodes every cipher word (the chosen value where the
transcription gives one, the single value of the sign otherwise), compares with the key output column of reading.txt
and counts the tiers. It imports nothing from the contributor's code.   python own_decode.py
"""
import collections, json, pathlib, re, unicodedata

HERE = pathlib.Path(__file__).parent
TOK = re.compile(r"^(\^?)([^=\{\?]+|\?)(?:=([^\{\?]*))?(?:\{([^}]*)\})?(\?)?$")


def norm(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c))
    return s.lower().replace("'", '').replace('v', 'u').replace(' ', '')


def main():
    key = json.loads((HERE / 'key.json').read_text(encoding='utf-8'))['signs']
    ref, sec = {}, None
    for line in (HERE / 'reading.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):
            sec = line[3:].strip()
        elif line.strip() and not line.startswith('#'):
            f = line.split('\t')
            ref[(sec, f[0])] = f
    for name in ('ridolfi', 'alamanni'):
        tiers, same, signs = collections.Counter(), 0, 0
        for line in (HERE / f'{name}-transcription.tsv').read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#') or line.startswith('id\t'):
                continue
            r = line.split('\t') + [''] * 8
            if r[3] != 'word':
                continue
            tiers[r[5]] += 1
            out = ''
            for t in r[4].split():
                _, lab, chosen, _alts, _low = TOK.match(t).groups()
                signs += 1
                vals = key[lab]['values']
                assert chosen is None or chosen in vals, (r[0], t)
                out += chosen if chosen is not None else (vals[0] if len(vals) == 1 else '(' + '/'.join(vals) + ')')
            same += norm(ref[(name, r[0])][1]) == norm(out)
        n = sum(tiers.values())
        print(f'{name}: {n} cipher words, {signs} signs; decode equals reading.txt on {same}; ' +
              ', '.join(f'{k} {tiers[k]} ({tiers[k] / n:.1%})' for k in ('strict', 'forced', 'lenient', 'doubt', 'unread')))


if __name__ == '__main__':
    main()
