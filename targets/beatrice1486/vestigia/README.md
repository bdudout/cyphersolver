# R1142: the "old cipher" and the Virtus / Fortis / M. markers (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

Sources: Vestigia 1967 (cipher original, ASMo CPE b. 1623, 2, fasc. 1, no. 10, DF 295022) and Vestigia 1998
(period clear copy, no. 10b, DF 295053), https://www.vestigia.hu/documents/1967 and /1998. No licence stated on the
site: no image copied.

## The markers are decoy words written in the cipher, and the period decipherer flagged them
- The blind transcription of V1967 p. 1 (`R1142_V1967_transcription.txt`, 5 runs, 211 signs) finds whole words in
  Latin letters inside the cipher runs: *wrnſ* (3 times), *focns / fornſ / fortſ / forts* (5 times, one word),
  *fer*, and a capital *M* closing several runs; the word *dealſ* stands just before two runs.
- The period copy V1998 copies these words into the clear text and **underlines** them: "per lo M.co
  <u>Virtus</u> andriolo <u>fortis</u> <u>M.</u>", "che voglia <u>decus</u> confortare", "qua <u>M.</u> <u>fortis</u>";
  in line 2 the copyist wrote and struck through the word before "preposta".
- So the 1878 print's "Virtus", "Fortis", "M." and "decus" (MDE IV suppl. 45) are these decoy words (nulls), which
  the editor printed from the exemplum. They carry no sense and can be dropped from the reading, as the
  underlining of the period decipherer already implies.

## The old cipher is not the 1482 alphabet
Identity test registered before decoding (`../../beatrice1482/vestigia/PREREG.md`, P2): the 1482 key K_V applied to
V1967 gives char 0.135, precision 0.114, words 0 against MDE IV (`ref_R1142_MDE4.txt`, markers removed); the best of
200 within-class shuffled keys gives 0.253. The 1486 runs use Latin-looking signs (e, ee, w, k, g, B, p, s, x) that the
1482 alphabet does not have. 211 signs is below the 300 required for a reading claim; this is an identity test only.
The old cipher's own key is not rebuilt here (one short letter, no held-out portion).
