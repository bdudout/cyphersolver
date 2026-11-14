# ferdinand1473: Ferdinand of Aragon to John II, cipher letters of 1473 and 1474 (BNE MSS/20211/64 and /73)

Catalogue #857. Contributed by Michael Brackx (work done with Claude Code under his direction), 29 Oct 2026.

Both cipher passages read: 1473 except two signs, 1474 with two doubtful words; the 1470 sibling /56 transcribed
only. Every remaining gap has an outside blocker (see Remaining gaps).

## Status

- **d64**, MSS/20211/64 (bdh0000186643), Ferdinand, king of Sicily, to his father John II, Hostalric, 5 June
  1473 (catalogue #857): the cipher passage, nine lines of the recto (201 signs), is read except two signs. Key
  rebuilt from the interlinear notes of a second hand (words and single letters) and extended by sense.
- **d73**, MSS/20211/73 (bdh0000186628), the same to the same, Zaragoza, 3 Nov 1474 (not in the catalogue): the
  cipher passage (eleven lines, 310 signs, a different cipher) is read. Its plaintext is the clear paragraph at
  the foot of the same page; the key was first read from the interlinear letters, then aligned on that paragraph.
- **d56**, MSS/20211/56 (bdh0000186631), Dueñas, 12 Nov 1470: a third cipher (numbers and signs, probably
  syllabic) with a faint modern pencil decipherment; transcribed (`transcription/d56_transcription.md`), not
  attacked. Not in `profile.json` documents.
- **d61**, MSS/20211/61, the same to the same, Alcalá, 13 March 1473: a sibling in the 1473 cipher of /64, found
  by Brice Dudout (PR #619, 14 Nov 2026). Eighteen runs (279 signs) under interlinear notes; the 1473 key recovers
  0.68 of the note letters against at most 0.40 for shuffled keys, under the 0.85 set beforehand, so the key is
  not validated by it and no reading is claimed (see d61). Not in `profile.json` documents.

Prior work: Galende Díaz, "La escritura cifrada durante el reinado de los Reyes Católicos y Carlos V", *Cuadernos
de Estudios Medievales y Ciencias y Técnicas Historiográficas* 18-19 (1994) 159-178, lists /56 and /73 as ciphered
letters of Ferdinand to John II, with no key; /64 is not in his list. The web search of 29 Oct 2026 found no edition or
decipherment of /64 or /73, but it did not reach the two sources below.

**Corrected 2 Nov 2026: this may not be a first reading.** Both sources were found after the reading and neither was used.

- DECODE has all three letters, created 26 Aug 2019 with status Decrypted: R1183 (/64), R1177 (/73), and /56 twice (R1174,
  R9530). R1183 and R1177 were opened: no document is listed on the record view, and both say Inline Plaintext: Yes, so the
  status may only reflect the interlinear notes. Not settled.
- Tomokiyo, "Spanish Ciphers before Accession of King Ferdinand: 1470-1479" (Academia.edu, Nov 2018, file ferdinand1470.pdf):
  his abstract and blog say he reconstructed several ciphers Ferdinand used in letters to John II in the 1470s, two of them
  "rather complex". **Not read**: Academia offers it only as a paid download and it is not at that filename on his own site. So
  whether it treats /64 and /73, and whether its keys agree with `key_1473.md` and `key_1474.md`, is open.

## Sources

BNE Digital (images CC BY 4.0, Biblioteca Nacional de España). The "high" PDF of each record holds one JPEG per
page: /64 1085 x 1187 px, /73 1114 x 1510 px, /56 1117 x 1485 px. Read in the pdf.js viewer at 4-16x and on a
re-rendering of the page cut into line strips. BNE Digital blocks a client that requests many records quickly:
fetch one record at a time.

## d64 (1473)

**System.** Homophonic letter substitution, 39 kinds of sign as transcribed (about 30 with a value), set inside
the clear text: several signs for each vowel and for *c*; one place sign (`FI`, long s and i joined, with a
cross-bar), noted *barçna*, Barcelona. No other nomenclator sign. Signs that looked alike were separated at 12x
(`3` *h* / `3-` *y*; `-o-` *i*, `o-` *a*, `ooo` *ll*; `T` *r* in 8 of 8, `TT` *s* in 13 of 13). Key: `key_1473.md`.

**Decode.** `python3 dec1473.py transcription/d64_transcription.md` (no hand corrections; where a sign has two
values both are printed) -> `decryption/d64_decode.txt`. Reading `decryption/d64_reading.md`, English
`decryption/d64_en.md`.

**Content.** Ferdinand reports the troops he brings for the relief of Perpignan: his *continos* and men from
Castile, more than 500 horse from Aragon, the Valencians (some already at Barcelona, the rest within the week),
800 horse in all with 100 men-at-arms.

## d73 (1474)

**System.** Homophonic letter substitution of its own (not d64's alphabet): bar signs (`-o-`, `-+-`, `o-`),
dotted signs, a null (`A` without dots), a sign for *qu* (`me`). The `4` sign gives *a*, *r* and *c*: probably
three look-alike signs. Key: `key_1474.md` (counts per sign).

**How it was read.** A 19-sign key read from the interlinear letters alone decoded *no res menos se*, *…matrimoni…
in / fanta mi hermana no se*, *mossen s…*, *se fa..na…*; the same words begin the clear paragraph at the foot of
the recto ("No res menos senyor yo he sabido…", `decryption/d73_clear.md`). `align1474.py` then aligns the 310
signs with the paragraph's 325 letters and re-estimates the key (`decryption/d73_alignment.txt`); `dec1474.py`
decodes with it (`decryption/d73_decode.txt`). Reading `decryption/d73_reading.md`, English
`decryption/d73_en.md`.

**Content.** Ferdinand is astonished that the marriage of the infanta Juana, his sister, "no se es rompido" as
negotiated, and asks that if anyone is sent to Naples on the matter it be Mossèn Santcliment, so that his own
affairs are handled with the others. (Juana married Ferrante I of Naples in 1476-77.)

## d61 (Alcalá, 13 March 1473): a sibling in the 1473 cipher (added 14 Nov 2026, Brice Dudout's session)

**Letter.** MSS/20211/61, Ferdinand to John II, Alcalá, 13 March 1473 (BNE record notes: "Notas interlineales"; not in
Galende 1994, not in the sibling list below). Eighteen cipher runs in lines 7-18 of the recto (279 signs), set in the
clear text, most of them under contemporary interlinear notes: *el duque nos ha enviado*, *luego*, *la ciudad*,
*marques*, *de tomar la dicha ciudad*, *quatro galeras*, *e sin ellas ninguna cosa*, *aquella ciudad*, *el dicho
duque*, *al dicho duque*, *un mes*. The verso has no cipher. Image 1 of 3, 1088 x 1456 px (about 120 ppi), CC BY 4.0.

**Test of the 1473 key.** Written down before the decode: the runs were transcribed blind (a second agent with the
shape table of `d64_transcription.md` only, no values, notes not used), the notes read separately and kept to words
legible without the cipher, and `dec1473.py`'s key applied unchanged. Score: letters of each note matched to the
best place in its run's decode (semi-global edit distance), against 200 keys made by shuffling the key's values
among its signs. Result (`check61/result.json`): **0.68** of 166 note letters, shuffled keys at most **0.40** (mean
0.31); 11 of 36 note words found exactly (shuffled at most 5). So /61 is in the cipher of /64 (`4` d, `1` e, `+` l,
`m` t, `x` q, `O` u, `d` e, `b` r all give the note letters: `R07a` decodes *i el duqve nor ha ...*, `R13a` *hauer
aqvelaciudat*, `R16a` *... al d chva duqve*). It does not reach the 0.85 set beforehand for a validation, and the
glossed runs (232 signs) are under 300, so this is a sibling identification, not a validation of the key. The
misses are mostly the 120-ppi transcription (`q`/`qo`, `O` against `o + + o`, `T`/`b`) and signs absent from the
key.

**Not done.** No reading of /61 is claimed: the notes are a contemporary decipherment (existing), and a reading
would need a better image to settle the signs. The sign transcribed `FI?` in `R10a` (decoded *barcelona*) stands
where a struck note seems to read *cadiz* after `p 2 + h` (*cal...*), next to *marques* (the marqués de Cádiz?):
open. /56 (1470): only 95 of its 372 transcribed signs have a value in the 1473 key (0.26, numbers 8-93 absent), so
the key does not apply; not decoded.

Files: `transcription/d61_transcription.md` (runs and notes), `decryption/d61_decode.txt` (machine decode, not a
reading), `check61/` (runs, notes, `score61.py`, result).

### Integration check (14 Nov 2026, PR #619)

- `check61/score61.py` re-run on the committed runs and notes with `dec1473.py` unchanged: 0.6807 of 166 note
  letters, 11 of 36 words, shuffled keys at most 0.3976 (mean 0.307), `PASS: false`; the figures of `result.json`
  reproduce exactly. A second control with 1,000 other shuffles: at most 0.404, mean 0.309. Per run the score runs
  from 0.55 (`R10b`, `R12b`) to 0.86 (`R09a`).
- A second decoder written from the key string of `dec1473.py` gives the same decode for all 18 runs (279 signs).
- **The test set beforehand as a validation failed**: 0.68 against the bar of 0.85 (the margin over the controls,
  +0.28, is also under the +0.30 the script asks). It is published as failed. What stands is the identification:
  the decode is far above every shuffled key and gives *el duque*, *quatro ... galeras*, *aquela ciudat*, *duque*
  under the notes that say so. The key of /64 is Michael Brackx's (PR #195) and is unchanged; the identification of
  /61 and the test are Brice Dudout's (PR #619, with AI agents).
- The order of events (protocol and blind transcription before the decode) is by the contributor's record: one
  commit, no protocol file with an outside time stamp.
- **Image not seen at integration**: BNE Digital answered 403 (its security block) to the one request made, so the
  18 runs were not sampled against the image. The transcription is the contributor's blind pass, kept as made.
- /61 is not added as a document of the profile and has no reading; the class and the read share of the target are
  unchanged.

## Tried and ruled out (do not repeat)

- The 1473 key on /73 and /56: different alphabets.
- A `p` split by shape (hooked top = *o*, plain = *c*) in d64: the plain p also stands for *o* (*ochocientos*,
  *ciento*); dropped.
- *complido* for *rompido* in d73 on the strength of the cipher's first sign (`2`, *c* elsewhere): the clear text
  and the interlinear letter both give *r*; kept *rompido*.

## Remaining gaps

- d64 L05, two signs `H C` in `P H C qo` after *de Castilla* (*c-m-?-o*; `C` occurs only here) - blocker: open-codes; sense wants *con migo* or similar
- d64, the σ-like `6` (*a* in four words, *i/j* in *mios* and *juntos*) and the plain `p` (*c*, *o*, once *a*): values chosen by sense - blocker: illegible; the 1085-px scan does not separate the forms
- d73, *rompido* (cipher first sign `2`, *c* elsewhere) and *promendo* (so in both texts; sense not settled) - blocker: illegible; a better image would settle the letters
- d73, the place sign `fi` near *a Napols* (Barcelona in d64) and the signs met once or twice - blocker: too-short
- d61 (MSS/20211/61), the 18 cipher runs: decoded by machine with the 1473 key, not read; the sign taken as `FI` in `R10a` under a struck note (*cadiz*?) - blocker: illegible; the 120-ppi image does not settle the signs (0.68 of the note letters recovered), and the notes above the runs are a decipherment of the time

## Escalation

- [x] siblings: /56 and /73 (Galende 1994) found and transcribed; /73 read
- [x] clear-pages: /73's clear paragraph found to be the plaintext; /64 has no clear copy on its three images
- [ ] known-keys: none in Galende 1994 or the BNE records, but Tomokiyo 2018 reconstructs ciphers of this series and is not yet read
- [ ] print: Galende 1994 checked, no edition found; Tomokiyo 2018 not read (paid download)
- [x] key-rebuild: d64 from the notes; d73 aligned on the clear text
- [x] retry: transcription re-read at 8-16x after each round; decodes re-run without hand corrections
- [ ] other Ferdinand -> John II letters in MSS/20211 (/57 1471, /80, /82 1475, /99 1476, /105 1477, /120,
  /123 1478) not checked for cipher; /61 (13 Mar 1473) found in the 1473 cipher (14 Nov 2026, see d61); /54, /55,
  /58-60, /62, /63, /66-72, /75 look clear at 45 ppi (contact sheets, not read in full)

## Next steps (ranked)

0. Obtain Tomokiyo 2018 and compare its keys and letter list with this reading; open R1183 and R1177 logged in on DECODE.
1. Ask BNE for better images of /64 (L05 and the σ- and p-signs) and /73 (*rompido*, *promendo*).
2. Check the other MSS/20211 letters for cipher in the d64 or d73 alphabet.
3. /56 (not part of this target's reading): read its pencil decipherment on a better image and rebuild its key.

## Files

`transcription/d64_transcription.md`, `d73_transcription.md`, `d56_transcription.md` (sign tables and the
interlinear notes); `key_1473.md`, `key_1474.md`; `dec1473.py`, `dec1474.py`, `align1474.py`;
`decryption/` (decodes, alignment, clear paragraph, readings, translations); `transcription/d61_transcription.md`,
`decryption/d61_decode.txt`, `check61/` (the /61 sibling test).
`validation.tsv`: the d73 pairs from `align1474.py` for `docs/_validate.py` (verdict "not applicable": polyphony
0.2, the `4` and `q` signs carry more than one value).

## Checker output (29 Oct 2026)

- `docs/_check_profile.py ferdinand1473`: valid (4 unknown fields: homophones per letter, nomenclator size, nulls).
- `docs/_check_reading.py ferdinand1473`: d64 reading 7/8 sentences clean, holes 0.11; d73 reading 3/7 sentences
  clean, holes 0.19 (probably the Catalan-Aragonese spellings *senyor*, *fechos*, *facan*, *bueltas* against
  the Spanish model; not checked). Both translated.
- `docs/_check_writeup.py ferdinand1473`: INCOMPLETE. Missing: the docs/ write-up surfaces (page, manifest, README
  row, portrait, snip, reveal, keys.json), which are for the maintainer on merge, and the `reading_review` of each
  reading, which is the reviewer's.
