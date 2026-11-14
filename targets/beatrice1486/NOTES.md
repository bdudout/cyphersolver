# Beatrice d'Aragona to Eleonora d'Aragona, Buda, 8 March 1486 (DECODE R1142)

Status: found already in print. The cipher passages are deciphered in Nagy–Nyáry, *Magyar Diplomácziai Emlékek* IV
(1878), supplement no. 45, pp. 367–368; the closing paragraph is MDE III (1877) no. 54, p. 67; the plain body is
Berzeviczy (1914) no. LVI, pp. 81–84. Matched to the images; no key applied or recovered.

Split on 14 Oct 2026 from `beatrice1482` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter was
filed with Beatrice's other letters to Ferrara (catalogue item 160). Its alphabet looks different from the 1482 one
(RESULT.md), and the letter itself says it is written in the old cipher and encloses a new one, so it is not grouped
with the 1482 letters ([`targets/beatrice1482/`](../beatrice1482/NOTES.md)) or with the May 1486 letter
([`targets/beatrice1486b/`](../beatrice1486b/NOTES.md)), each a different cipher with its own page; the plain letter of
1505 is [`targets/beatrice1505/`](../beatrice1505/NOTES.md).

Research report on all five records of catalogue item 160, with the verification limits:
[`../beatrice1482/RESULT.md`](../beatrice1482/RESULT.md) (20 Sept 2026, GPT-6). DECODE metadata in
`../beatrice1482/metadata.json`; images (git-ignored; DECODE notice: publication needs the archive's permission) in the
main checkout's `targets/beatrice1482/img/`. Work date: 2026-09-20.

## The letter

ASMo, Carteggio Principi Esteri, 1623, b. 2/2, 2, 10; DECODE R1142 (five photographs). Only the first written page
carries graphic cipher; the next three are plain text on Ippolito's appointment to Esztergom and Cardinal Ascanio's
opposition; the fifth image continues the fourth.

- Cipher passages (MDE IV suppl. no. 45): bringing Andriolo to Hungary, paying his travel, honouring the king's
  promises. The editor's heading ties the negotiation to the Djem (Cem) affair; that identification is his.
- The printed reading keeps "Virtus", "Fortis" and repeated "M." in awkward places. They are on the printed page, not
  OCR errors; their role in the cipher is not established and they are not dropped as nulls.
- Closing (MDE III no. 54): "Con la cyfra havemo antiquamente con Vostra Signoria … ne li mandamo qui alligata un altra
  nova": the old cipher is used here and a new one is enclosed for later letters. MDE III no. 53 is a related
  same-date letter, not this manuscript.

## Open

- The old cipher's key is not rebuilt. It is not the 1482 alphabet of beatrice1482 (tested 14 Nov 2026, below).
- The Virtus/Fortis/M. markers of the 1878 print: explained 14 Nov 2026 (decoy words, below).

## Files

- `readings/r1142_mde4_ocr.txt`, `r1142_closing_mde3_ocr.txt`, `r1142_body_berzeviczy_ocr.txt`: uncorrected OCR extracts
  of the printed sources.

## 14 Nov 2026: the markers and the old cipher (Brice Dudout, Claude Opus 5.5)

Vestigia 1967 (cipher) and 1998 (period clear copy). The printed "Virtus", "Fortis", "M." and "decus" are decoy words
written in Latin letters inside the cipher runs (wrnſ, forts…, M, dealſ); the period decipherer copied them and
underlined them, so they are nulls. The 1482 key of beatrice1482 does not read these runs (characters 0.135 against
0.253 for the best shuffled key; 211 signs, identity test only): the old cipher is a different alphabet, still to be
rebuilt. Details: [`vestigia/README.md`](vestigia/README.md).

### Integration check (14 Nov 2026, PR #620)

- `../beatrice1482/vestigia/measure.py` on `vestigia/R1142_V1967_transcription.txt` against `ref_R1142_MDE4.txt`:
  211 signs, characters 0.135, precision 0.114, words 0; best of 200 shuffled keys 0.253. Reproduced. The test is
  weak by construction: 105 of the 211 signs have no value in the 1482 key (86 of them are labelled as Latin letters or
  words, `l:e`, `l:p`, `{wrnſ}` ...). It shows that the 1482 key does not read the letter; several shapes (9, V, 6, 3, Π, the ϟ-sign) occur in
  both, so a related alphabet is not excluded.
- Vestigia's web image of 1998 (the clear copy) was opened (not kept): lines 1-5 read *per lo M.co Virtus andriolo
  fortis M.*, *che voglia decus confortare ... andriolo fortis ad venire qua M. fortis*, with *Virtus*, *fortis*,
  *M.* and *decus* underlined, and a struck word before *preposta*. As stated. The cipher image 1967 was not
  sampled.
- So the words of the 1878 print come from the letter itself, through the copy: they are not the editor's. That
  they are nulls (decoy words) is the simplest reading of the underlining and is the contributor's; a code word
  with a meaning the decipherer did not have is not excluded.
- Vestigia's record of 1998 lists Berzeviczy 1908 and Cremonini 2015 and 2018 as publications: not opened. Whether
  they discuss these words or the old cipher is not checked.
- Open and workable: the key of the old cipher could be rebuilt from the pair 1967 / 1998 (211 signs with their
  clear text). Not done in the PR or here. The text of the letter is in print, so the class is unchanged.
- No image is committed; the shape transcription is the contributor's, the reference lines are from the 1878 print.
