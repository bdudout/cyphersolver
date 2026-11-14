# The 1482 alphabet rebuilt from Vestigia's cipher/clear pairs (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Sources
Vestigia (open-access database of Hungarian-related documents in Italian archives; images from MNL OL X 8921,
originals in ASMo, Cancelleria, Carteggio principi esteri b. 1623, 2, fasc. 1) holds, for each 1482 letter, the
cipher original and a period clear copy ("exemplum", Vestigia format `simple-copy`, relation `decrypt`):

| letter | cipher original | period clear copy | print |
|---|---|---|---|
| R1140, Pozsony, 31 May 1482 | Vestigia 1957 (no. 4a, DF 295012) | Vestigia 1958 (no. 4b, DF 295013) | MDE III (1877) no. 10 |
| R1141, Pozsony, 8 June 1482 | Vestigia 1960 (no. 5a, DF 295015) | Vestigia 1961 (no. 5b, DF 295016) | MDE III (1877) no. 12 |
| R1142, Buda, 8 March 1486 | Vestigia 1967 (no. 10, DF 295022) | Vestigia 1998 (no. 10b, DF 295053) | MDE IV (1878) suppl. 45 |

URLs: https://www.vestigia.hu/documents/1957 (and 1958, 1960, 1961, 1967, 1998). No licence is stated on the
site, so no image is copied here; images were read from Vestigia's public web files only.

## Method
- Sign shapes transcribed blind (labels in `sign_inventory.md`, no values) by a separate agent for V1957 (852 signs,
  32 runs) and V1960 (648 signs, 27 runs); my own first pass of V1957 agrees with it wherever I read.
- Pre-registration `PREREG.md` (SHA-256 3d7bc070…3229) frozen before any decoding of V1960.
- Key K_V (`K_V.json`, SHA-256 0ae0cdbe…32b5) built from V1957 only (`train_key.py`, alignment against the
  print checked on the exemplum, `train_refs_R1140.txt`), completed for two shapes unseen in V1957 from the
  matthias1482 key (round c = n, Λ = o). Frozen before the measurement.
- One measurement (`measure.py`) on the whole of V1960, transcription taken as is, against MDE III no. 12
  between the same clear anchors (`ref_R1141_MDE.txt`), with 200 keys shuffled within value classes (single
  letters / multi-letter signs / nomenclator), seed 20261114.

## Result (held-out V1960, R1141)
| | char | precision | words |
|---|---|---|---|
| K_V | **0.900** | 0.867 | 0.644 |
| best of 200 shuffled keys | 0.290 | | 0.068 |
| mean of 200 shuffled keys | 0.166 | | |

Threshold (written before): char ≥ 0.85 and ≥ best control + 0.30 → **pass**. Most word misses are spelling
differences between the cipher and the 1877 print (lega/liga, con/cum, denari/dinari) and a sign read for
ss where V1957 has tt (see below). Decoded runs: `decoded_R1141_KV.txt`.

## The key (1482, Beatrice ↔ Eleonora)
a 8, V · b d · c ɔ · d 9 · e ϟ-like sign · f Ѣ-like sign · g 2 · h 6 · i 3 · l σ-like o- · m ⊐ · n ⊏, round c ·
o 7, Π, Λ · p ⊔ · q = · r ≠/Ŧ · s L · t ⊥ · u/v 1, ⊤ · x H · z Ɛ · tt ·ıı· · ss ※ and a trident sign · ff a curled
c-sign · ll ∃. Nomenclator: Ǥ = (Signor) Re de Hungaria; ×° = Venetiani. Homophones are few (a, o, u, n).

## Against matthias1482 (Matthias → Ercole, Pozsony, 1 June 1482)
Same alphabet: 17 letter values agree (a 8/V, b d, c ɔ, h 6, i 3, l σ, m ⊐, n ⊏/ϲ, o 7/Π/Λ, p ⊔, q =, r Ŧ, s L,
t ⊥, u ⊤, tt ·ıı·, e on the 5/ϟ shape) and both nomenclators name the King of Hungary and the Venetians.
Two disagreements, on shapes Daniel's key gives as figures: here **9 = d** (33/33 in V1957) where matthias1482
has 9 = e, and **2 = g** (10/10) where matthias1482 has 2 = d or i. Worth re-checking on R1156: its "2" in
*disposituros*, *diverti* may be this alphabet's 9.

## What it changes
1. R1140 and R1141 now have a glyph transcription and a key, validated on a held-out letter (0.900 vs 0.290).
2. **R1141, a passage missing from the 1877 print.** After "non solamente havia tolto" the cipher has a run
   that MDE III no. 12 does not print. The period copy V1961 adds it in the margin: "et tale che non solamente
   havia tolto Venetiani da sua offesa, ma li haria reducti a carastia de defenderse". K_V decodes the run as
   [Venetiani] da sua o…esa, and the next run as *defenderse* (print: *defenderle*). Other print readings the
   cipher corrects: *aitare* (print "vitare"), *emoli* (print "emidi"), *iocare de balla* confirmed.
3. R1142 (1486): the "old cipher" is **not** the 1482 alphabet: K_V on V1967 gives char 0.135 against a best
   control of 0.253 (211 signs, below the 300 needed for a "read" claim; identity test only). Its runs are made of
   Latin-looking letters (e, w, k, g, B, p, ee…). See `../../beatrice1486/vestigia/`.
