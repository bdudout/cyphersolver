# PREREG — beatrice-vestigia, held-out measurement (frozen 14/11/2026, before any decoding of R1141 or R1142)

## Hypothesis
H1: the cipher runs of Beatrice's letter of 8 June 1482 (Vestigia V1960 = DECODE R1141) use the same graphic
alphabet as her letter of 31 May 1482 (V1957 = R1140), and that alphabet is the one of King Matthias's letter of
1 June 1482 (matthias1482, Daniel's key).
H2 (secondary, identity test): the "old cipher" of 8 March 1486 (V1967 = R1142) is the same alphabet.

## Training (the only material used to build the key K_V)
- V1957 cipher runs (two transcription passes: A by me, B blind by a sub-agent; arbitration on the image),
  aligned to the period clear copy V1958 ("exemplum") and the 1877 print (MDE III no. 10, italics).
- Key rule: each sign label -> the letter (or string, for multi-letter signs and nomenclator) it stands for most
  often in the R1140 alignment. Signs NOT attested in R1140 receive the matthias1482 value (targets/matthias1482/
  texts/key.md) when that key gives exactly one shape-match; otherwise they decode to "?".
- The key is frozen as JSON and its SHA-256 written in MESURE.md BEFORE the measurement is run.

## Held-out portions (never aligned, never decoded before the measurement)
- P1 (primary): all cipher runs of V1960 recto (R1141). Transcription for the measurement = pass B (blind
  sub-agent, given only INVENTAIRE-SIGNES.md, no key, no clear) taken AS IS. My pass A, if made, is reported
  as a sensitivity figure only.
- Reference clear for P1 = for each run, the words of MDE III no. 12 (1877) between the same clear anchor words
  (anchors read on the image, plain text only), checked against the period copy V1961 where the print is
  doubtful. Length must be >= 300 cipher signs; if not, P1 is "not measurable".
- P2 (secondary, H2): cipher runs of V1967 p. 1 (R1142), pass B taken as is; reference = MDE IV suppl. 45 text
  between the same anchors, with the printed words "Virtus", "Fortis", "M." removed. If < 300 signs, P2 is
  reported as an identity test only (no "read" claim either way).

## Normalisation
Lowercase; letters only; j->i, v->u, y->i, k->c; spaces and punctuation removed; doubled letters kept.
Nomenclator signs decode to their training string (normalised the same way). Unknown signs decode to "?"
(counts as a wrong character).

## Metric (one run of the script per portion)
- Per run: global alignment (Levenshtein, unit costs) between decoded string D and reference R.
  char = sum over runs of matched characters / sum of |R|.
  precision = matched / sum of |D|.
  words = share of reference words all of whose characters are matched with no insertion inside the word span.
- Controls: 200 shuffled keys, seed 20261114. Shuffle WITHIN value classes only: (a) single-letter signs among
  themselves, (b) multi-letter signs (tt, ss, ll…) among themselves, (c) nomenclator signs among themselves,
  (d) nulls among themselves. Never across the whole key. Same metric on each.
- Success threshold (written now): char >= 0.85 AND char >= best control + 0.30. Words and precision reported,
  not thresholded.
- One measurement per portion. A measured portion is burnt.
