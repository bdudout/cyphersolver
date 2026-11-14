# Beatrice d'Aragona to Eleonora d'Aragona, Pozsony, May–June 1482 (DECODE R1140, R1141)

Status: found already in print (MDE III, 1877, nos. 10 and 12). See RESULT.md for verification limits. Since 14 Nov 2026 the
1482 key is rebuilt from the period clear copies (Brice Dudout, PR #620; `vestigia/`), and one run of R1141 that the print
leaves out is restored.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 160 grouped five DECODE
records by sender. This entry keeps the two 1482 letters (R1140, R1141), in the 1482 alphabet. The others now have
their own folders and pages (each a different cipher, or none, with its own page):
- R1142, Buda, 8 March 1486: [`targets/beatrice1486/`](../beatrice1486/NOTES.md). Its alphabet looks different from the
  1482 one, and the letter says it uses "the old cipher" and encloses a new one;
- R1143, Buda, 2 May 1486: [`targets/beatrice1486b/`](../beatrice1486b/NOTES.md). Two months after the new cipher was
  sent; not shown to share a key with R1142;
- R1154, Naples, 29 May 1505: [`targets/beatrice1505/`](../beatrice1505/NOTES.md). Plain Italian, not a cipher.

RESULT.md (the research report on all five), metadata.json, original_catalogue_entry.json and fetch_decode.py stay
here as shared material; the OCR extracts for R1142, R1143 and R1154 moved to the new folders' `readings/`.

Research begun 20 September 2026 from the user's goal-objective attachment.
No new cryptanalytic reading claimed. The table below preserves the starting DECODE metadata; corrections and primary-source evidence are in RESULT.md.

| Record | Date | From / to | Shelfmark suffix | Pages |
|---|---|---|---|---|
| R1140 | 31 May 1482 | Pozsony / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 4a | 1 |
| R1141 | 8 June 1482 | Pozsony / Eleonora | Cancelleria 1523 [name says 1623], b. 2/2, 2, 5a | 1 |
| R1142 | 8 March 1486 | Buda / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 10 | 5 |
| R1143 | 2 May 1486 | Buda / Eleonora | Carteggio Principi Esteri 1623, b. 2/2, 2, 18 | 5 |
| R1154 | 29 May 1504 | Naples / Ippolito | Carteggio Principi Esteri 1623, b. 2/7, 11 | 1 |

The attachment's umbrella shelfmark b. 2/2 and origin Pozsony do not apply to all five.
Metadata recovered from repository research/catalogue_harvest/decode/views*.jsonl.
DECODE images carry an archive-permission requirement for publication; images stay local and ignored.

## Prior work checked before cryptanalysis

- Tomokiyo, Cryptiana index https://cryptiana.web.fc2.com/code/crypto.htm: retrieved; no dedicated Beatrice entry found in the index. This does not establish absence throughout his publications.
- Berzeviczy, *Aragoniai Beatrix ... okiratok* (1914), https://archive.org/details/aragoniaibeatrix00berz, OCR saved as sources/berzeviczy1914.txt. No. LVI, pp. 81 onward, prints the 8 March 1486 letter, with explicit omissions of passages printed in *Matyas korabeli diplomacziai emlekek* III p. 67 and IV p. 367. Need compare to R1142 images before treating this as its decipherment.
- Vestigia public API accessible, but simple search does not search dates and quoted full-name search gave zero results. Search Beatrice returns 418 documents, 5 per page.
- User confirms an existing DECODE cookie is available. Located targets/bordeaux/decode/cookie.txt; use only as request header to de-crypt.org, never reproduce it in notes or logs.

## Completed source identification

See RESULT.md and readings/ for the record-by-record findings and earlier Italian texts. Eighteen images downloaded successfully. R1154 is 29 May 1505 and is plain Italian. R1143 has three written pages photographed five times, including views with slips moved. Four cipher letters have readings in MDE III (1877) and IV (1878); March 1486 editorial markers remain unexplained. Research write-up prepared in `.worktrees/beatrice1482/` on `codex/beatrice1482`. No manuscript images are included in the write-up.

## 14 Nov 2026: key rebuilt from the Vestigia cipher/clear pairs (Brice Dudout, Claude Opus 5.5)

Vestigia (https://www.vestigia.hu) publishes both letters with their period clear copies ("exemplum"): 1957 ↔ 1958
(R1140) and 1960 ↔ 1961 (R1141). Blind glyph transcriptions of both letters, a key rebuilt from R1140 only and one
pre-registered measurement on the whole of R1141 (648 signs): characters 0.900 against 0.290 for the best of 200 keys
shuffled within value classes. The alphabet is the one of matthias1482 (17 shared values; 9 = d and 2 = g here
against the figures in that key). R1141 has a cipher run the 1877 print leaves out, "Venetiani da sua offesa",
restored from the copy's margin and the key (readings/R1141_reading.md). Details: [`vestigia/README.md`](vestigia/README.md).

### Integration check (14 Nov 2026, PR #620)

- **Reproduction.** `vestigia/measure.py K_V.json R1141_V1960_transcription.txt ref_R1141_MDE.txt relabel_R1141`:
  648 signs, characters 0.900, precision 0.867, words 0.644; best of 200 within-class shuffled keys 0.290, mean
  0.166; pass. The fourth argument (the relabelling of the new shapes) is needed: without it the figure is 0.891.
  `train_key.py` on R1140 gives the values of `K_V.json`. SHA-256 of `PREREG.md` (3d7bc070...3229) and `K_V.json`
  (0ae0cdbe...32b5) match the README.
- **Second scorer.** A scorer written here (longest matching blocks instead of Levenshtein): K_V 0.901, 300
  shuffles of the single-letter values at most 0.346.
- **Order of events** (protocol, then key from R1140, then one measurement on R1141): by the contributor's record;
  one commit, the hashes prove the files are unchanged, not when they were written.
- **The key is seeded.** `train_key.py` aligns R1140 with a starting table (`SEED`) that already holds 9 = d and
  2 = g, so "33/33" and "10/10" are not independent counts. Re-run here with both removed from the seed: 2 = g
  10/10, 9 = d 29/33 (the other four are alignment slips onto *d* plus a neighbour). The values stand.
- **Images.** Vestigia's web images of 1960 (cipher) and 1961 (clear copy) were opened (not kept). 62 signs of
  R1141 compared with the transcription (line 2 *grande dispiacere*, the end of line 5 and line 6 *avari che per
  sparagnare ... lo ducato*): all agree. The margin of 1961 reads *et tale che non solamente havia tolto Venetiani
  da sua offesa ma li haria ridocti a carastia de defenderse*: the restored run is on the copy as stated.
- **Key state: partial.** Three shapes of R1141 have no value in `K_V.json` (ZIG 4 times, where the print has *x*;
  WEDGE twice; LAMBDAFLAG twice) and one sign is unread: 9 of 648 signs. Two values (round c = n, Λ = o) come from
  the matthias1482 key, not from R1140.
- **Outcome.** The text of both letters is still the printed decipherment of 1877 (method: read from existing
  decipherment). The key is a second part: key recovered based on plaintext from external sources (the period
  clear copy and the print), partial.
- **Prior art not checked.** Vestigia's records of 1960 and 1961 (R1141) list a later edition, "GUERRA 2010: 12"
  (the records were opened; the edition itself was not; the records of R1140 were not opened). Whether it already prints *Venetiani da sua offesa*
  from the clear copy is not checked: the run is new against the 1877 print only.
- **What the PR commits from Vestigia:** no image. Text only: the contributor's own shape transcriptions, reference
  lines taken from the 1877 print, and the quoted margin sentence of the clear copy. Vestigia states no licence;
  its documents are cited by number.

### The same alphabet as matthias1482 (one key, one entry: for the owner)

The king's letter to Ercole of the next day (R1156, Pozsony, 1 June 1482, `targets/matthias1482/`) has the same
values for a 8/V, b d, c ɔ, h 6, i 3, l σ, m ⊐, n ⊏/ϲ, o 7/Π/Λ, p ⊔, q =, r Ŧ, s L, t ⊥, u ⊤, tt ·ıı·, and a
looped q-sign for the King of Hungary. Seventeen shared values between two letters of the same court, the same
week and the same household at Ferrara are one key. Three values differ: d (9 here, 2 there), g (2 here, a hooked L
there), e (one ϟ/5-like sign here; 5, 4, 9, ς there); and the Venetians have another sign (×° here, a looped &
there). On R1141 the matthias values score lower: 9 = e with 2 = d gives 0.833, with 2 = i 0.843, against 0.900
(same scorer as above, 0.901 for K_V). matthias1482 keeps no sign-level transcription, so its side cannot be
re-checked from its files; recorded there as an open point, its key unchanged. **Not folded in this round**: both
targets have a page; the fold under the one-key rule is the owner's decision.
