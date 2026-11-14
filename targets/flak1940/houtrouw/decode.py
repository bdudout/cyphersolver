"""Decode the nineteen days of issue #602 from the transcriptions and keys in this folder (the project's own decoder, 14 Nov 2026).

Double columnar transposition: the plain text is written in rows under key A and read off by columns in the order of the key
numbers; the result is written in rows under key B and read off the same way. Decoding undoes B, then A.
Usage: python decode.py            (prints letters, lost letters and the places that differ from the contributor's text, per day)
"""
import pathlib, re

HERE = pathlib.Path(__file__).parent


def undo(ct, key):
    n, w = len(ct), len(key)
    rows, rem = -(-n // w), n % w
    lens = [rows if (rem == 0 or c < rem) else rows - 1 for c in range(w)]
    cols, p = [None] * w, 0
    for num in range(1, w + 1):
        c = key.index(num)
        cols[c] = ct[p:p + lens[c]]
        p += lens[c]
    return ''.join(cols[c][r] for r in range(rows) for c in range(w) if r < len(cols[c]))


def keys():
    out, day = {}, None
    for line in (HERE / 'keys.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'(\d{4}-\d\d-\d\d)', line)
        if m:
            day = m.group(1)
            out[day] = {}
        m = re.match(r'([AB]) \(\d+\): ([\d ]+)', line)
        if m:
            out[day][m.group(1)] = [int(x) for x in m.group(2).split()]
    return out


def parts(day):
    """(heading, indicator length, lost letters, cipher letters, contributor's text) per part, from the two files of the day."""
    ct, head = {}, None
    for line in (HERE / f'{day}_transcription.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('['):
            head = line
            ct[head] = ''
        elif head and not line.startswith('#'):
            ct[head] += line.replace(' ', '')
    lines = [l for l in (HERE / f'{day}_decryption.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
    out = []
    for i, l in enumerate(lines):
        m = re.match(r'(\[.*?\]) ind=(\d+) letters=\d+ lost=(\d+)', l)
        if m:
            out.append((m.group(1), int(m.group(2)), int(m.group(3)), ct[m.group(1)], lines[i + 2]))
    return out


if __name__ == '__main__':
    tot = [0, 0, 0]
    for day, k in keys().items():
        n = lost = diff = 0
        for head, ind, nlost, c, theirs in parts(day):
            body = c[ind:]
            if nlost and '?' not in body:
                body += '?' * nlost          # letters lost at the end of a sheet whose back is not on the film
            dec = undo(undo(body, k['B']), k['A']).upper()
            assert len(dec) == len(theirs), (day, head)
            lost += dec.count('?')
            n += len(dec) - dec.count('?')
            diff += sum(1 for a, b in zip(dec, theirs) if a != b and a != '?')
        print(f'{day}  A {len(k["A"]):2d}  B {len(k["B"]):2d}  letters {n:5d}  lost {lost}  differing from the word {diff}')
        tot = [tot[0] + n, tot[1] + lost, tot[2] + diff]
    print('total letters %d, lost %d, differing %d' % tuple(tot))
