# milan1494: Ridolfi (Milan, October 1494) and Alamanni (Vigevano, April 1494) to Piero de' Medici, in the key sheet MAP LXXII 183

Status: in progress. Read in part with the key sheet ASF Mediceo avanti il Principato LXXII doc. 183, matched and applied by Andrew Aymeloglu (issue #589, 14 Nov 2026; repository `aaymeloglu/unsolved-ciphers`, folder `milan-1494`, CC0, commit 579c487). Words with no ambiguous sign: 104 of 283 (36.7%) in Ridolfi's three letters, 37 of 91 (40.7%) in Alamanni's. No page yet: the open pieces below can still be worked.

Catalogue 2382 (Ridolfi) and 2381 (Alamanni). One key, one entry: all four letters are in the same key sheet, so they are one target.

## The documents

Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP), filza LXXIV:

- doc. 112, c. 256r: Giovan Battista Ridolfi, Florentine envoy, Milan, 16 October 1494, to Piero di Lorenzo de' Medici; three cipher blocks on the recto (the verso carries show-through only).
- doc. 113, c. 257r-v: the same, 21 October 1494; nine cipher lines in two blocks on the recto, two on the verso.
- doc. 115, c. 263r: the same, 30 October 1494; four short cipher runs within lines 5-12.
- doc. 96, cc. 220-221: Piero Alamanni, Vigevano, 26 April 1494, to Piero de' Medici; cipher from c. 220v line 6 to c. 221v.

The key sheet is MAP LXXII doc. 183 (image 79536; the verso, image 79537, is endorsed "Cifra con Paulantonio Soderini", by the contributor's reading): an alphabet with up to three signs a letter, signs for et, che, per, io, tu, voi, noi, quando, come and titles, nulls, and numbers from 10 for names (Papa 10, Re di Napoli 11 ...). The images are on the ASF MAP server at 1272 px at most; every image used is listed with its id and SHA-256 in `aaymeloglu/images.tsv`. None is copied here.

## The cipher and the key

A homophonic sign alphabet with a small set of word signs, nulls and name numbers. The contributor found the sheet by comparing the glossed word pairs of Ridolfi's letters LXXIV 107 and 110 (havendo, una volta, questo, stato, salvo, per venire) with the key sheets in filza LXXII: 183 reproduces them letter for letter (44 of 44, his figure; not held out, since the match was found on those pairs). Not on the sheet and added by him, each with its ground in `aaymeloglu/key.json`: six signs for doubled consonants (ss and tt from Ridolfi's interlinear glosses in 107 and 110; rr, nn, bb, cc fitted from the words they make) and the arch-with-dot sign read *non* from the gloss in 110 c. 250r, where the sheet's label reads *noi*.

Two things limit every reading in this key: the sheet gives the sign ÷ for both n and c, and Ridolfi writes his d and his l alike. At 1272 px several other signs cannot be told apart. The transcriptions therefore carry, for each ambiguous sign, the value chosen and the alternatives.

Name number 22: the sheet gives 22 = S. di Pesaro and 15 = S. Lodovico, but Ridolfi 107 c. 241r has the contemporary gloss "S. Lco" over 22, and the three passages with 22 in Alamanni's letter fit Lodovico. The contributor renders it "[22: probably S. Lodovico]" and grades it inferred. Open.

## What the letters say (the contributor's reading)

Ridolfi, 16 October: Charles VIII's arrival in the castle of Pavia, met by the Duchess Bona; a person written with an unglossed sign (the Duke or Lodovico) ill in bed; the citizens of Pavia protest against the milling duty. 21 October, the day the death of Gian Galeazzo was announced: the King spent about two hours at night with Bona; the Duchess Isabella would not appear, pleading illness; fra Lauro met on the road dressed as a courier; Lorenzo and Giovanni di Pierfrancesco at Modena. 30 October: opinion in Milan that Florence cannot resist the French and that they count on dissension in the city; the accord of Forlì and the promise of Faenza.

Alamanni, 26 April: he urges Piero privately that the King of Naples's plan to turn Genoa is the one remedy, must not be delayed and must be entered only with preparation enough to win; that name 22 will never trust the King; and that Piero must tell no one. On c. 221v, Lodovico's three threats: Genoa, France (unread), and closing the road of the Florentine merchants in the West.

Full Italian (clear and cipher) and English: `aaymeloglu/ridolfi-reading.md`, `aaymeloglu/alamanni-reading.md`. The contributor says of the connected text that it is a proposal whose secure parts are the words graded H or C in `aaymeloglu/reading.txt`.

## Counts

The contributor grades every cipher word by how its reading was chosen: strict (no ambiguous sign), forced (ambiguous signs, but only one choice gives a word), lenient (chosen by sense or a language model), doubtful, unread.

| Letters | Cipher words | Strict | Forced | Lenient | Doubtful | Unread |
|---|---|---|---|---|---|---|
| Ridolfi 112, 113, 115 | 283 | 104 (36.7%) | 90 (31.8%) | 85 (30.0%) | 2 | 2 |
| Alamanni 96 | 91 | 37 (40.7%) | 24 (26.4%) | 19 (20.9%) | 0 | 11 |

Read share by the README rule (sure words only; words chosen by sense are holes): the strict tier, 36.7% and 40.7%. With the forced words, which rest on a dictionary and not on the sense, 68.6% and 67.0%. The contributor's widest figure, every word with a proposed reading, is 98.6% and 87.9%; in his words it is how much has a proposed reading, not how much is right. His own calibration: with the gloss of Ridolfi 107 c. 241v masked, the reader got 28 of 38 glossed words right (74%) and 4 confidently wrong.

## Integration check (14 Nov 2026)

- An own decoder (`aaymeloglu/own_decode.py`), written from `key.json` and the two transcriptions, gives the key output column of `reading.txt` for all 283 and all 91 cipher words (1,092 and 371 signs), and the tier counts of the table above. The contributor's `verify.py` was read and not run (it needs his `cipherkit` package).
- Images: the ASF server answered from this session. The key sheet (image 79536) and Ridolfi 112 c. 256r (image 81807) were fetched; their SHA-256 are the ones in `images.tsv`. The sheet shows the alphabet as `key.json` gives it (a: +, two strokes, c; n and c both with ÷; names from Papa 10). Line 4 of c. 256r (13 units, about 45 signs: intendo che arrivando in Pava quando ... fu entrato in castelo) agrees with his transcription sign for sign. The other leaves were not compared.
- The Italian and the English were read as sentences: they hold together and fit the days (the King at Pavia, the Duke's death on 21 October, the march on Florence). The secure part is small, as the contributor says.
- Not repeated here: his key-shuffle control (z = 18.5 Ridolfi, 13.5 Alamanni), the second model's 70 spot checks (`aaymeloglu/audit/codex-review.md`), the blind second transcription.
- Catalogue corrections taken into entries 2382 and 2381 (cipher extent per leaf; the key is LXXII 183, not Alamanni's Naples sheet LXXII 178).

## A test by Brice Dudout on a held-out letter (comment on issue #589, 14 Nov 2026; his report, no files sent)

Brice Dudout applied the published `key.json` (commit 46dec7b) unchanged to Ridolfi's glossed letter MAP LXXIV doc. 114 (22 October 1494; 27 cipher lines, 865 signs, his own transcription frozen before he fetched the key), against the text printed by Desjardins, *Négociations diplomatiques de la France avec la Toscane*, I (1859), pp. 585-586. One measurement: character agreement 0.774 against 0.397 for the best of 200 shuffled keys. His bar was 0.85, so the test failed by his own rule; he puts the loss on the image resolution and on one shape choice of his own (the d/l class). 101 of 175 words exact. The key reads running Italian on a letter it was not built on; the test does not reach his bar. His own key, built from Niccolini's glosses of 1492-93 without the sheet, agrees on most values, also has ÷ for n and c, and reads 22 as Lodovico (his report).

He also points to P. D. Gabbrielli's copy book of the keys of the Dieci di Balìa (Ilardi microfilm reel 58, Yale Dataverse doi:10.60600/YU/XKVOWE; inventory in issue #610): no. 25 (Piero Alamanni, 1492) and no. 34 ("de Rydolfis", 1495) are the nearest to these letters. Not tested on them.

## Relation to rucellai1482 (pull request 617)

Bernardo Rucellai's letters of 1482 in the same fonds (MAP LXXII 196-211) are in another table: in Brice Dudout's key for them 6 is a, 7 is e and = is n, where the sheet LXXII 183 has 6 and 7 for i and ÷ for n and c. The two keys do not relate beyond the family of system (a sign alphabet with homophones, nulls and separate signs for doubled consonants, which both workers found independently for rr and tt).

## Remaining gaps

- 85 + 19 words chosen by sense and 90 + 24 forced words rest on ambiguous signs (÷ for n or c; d and l alike; b, 6 and others at 1272 px) - blocker: none yet; Ridolfi's glossed letters 101-110 and 114 give his letter forms with their values and have not been used to separate them, and doc. 114 with Desjardins's text is a ready test
- Two unread groups and two doubtful words in Ridolfi 113; 11 unread words in Alamanni (the second threat on c. 221v, a run after name 22 on c. 220v, a few signs) - blocker: none yet; not tried with Gabbrielli's keys nos. 25 and 34
- Name number 22 (sheet: S. di Pesaro; gloss in Ridolfi 107: S. Lodovico) and 15 - blocker: none yet; the other letters in this key have not been searched for 22 and 15
- Two person signs not on the sheet ([il Re], [Duca o Lodovico]) - blocker: none yet; the glossed siblings were not searched for them
- The clear text of the four letters was read from the same images and not collated - blocker: none yet
- Higher-resolution images - blocker: needs-physical-access; the ASF server serves 1272 px at most

## Escalation

- [x] siblings: Ridolfi 107 and 110 (glossed) used to find the key; 114 used by Brice Dudout as a test; 101-106, 108-109 not used
- [x] clear-pages: the clear passages of the four letters are transcribed in the reading files
- [x] known-keys: MAP LXXII 183 is the key; LXXII 178 (Alamanni's Naples sheet) saved by the contributor and not formally tested
- [ ] print: Desjardins I (1859) prints doc. 114; whether he or others print 112, 113, 115 or doc. 96 was searched by the contributor without result, and not re-searched here
- [ ] key-rebuild: the signs for doubled consonants and *non* were added; a letter-form table per writer from the glossed letters is not made
- [ ] retry: after the sign classes are separated

## Files

| File | Content |
|---|---|
| `aaymeloglu/key.json` | the key: every sign with its values, what the sheet gives, the grade and the ground |
| `aaymeloglu/ridolfi-transcription.tsv`, `aaymeloglu/alamanni-transcription.tsv` | one row per unit, with the chosen value and the alternatives of each ambiguous sign |
| `aaymeloglu/reading.txt` | key output against the editorial reading, word by word, with tier and grade |
| `aaymeloglu/ridolfi-reading.md`, `aaymeloglu/alamanni-reading.md` | Italian and English |
| `aaymeloglu/images.tsv` | the ASF images used, with their SHA-256 |
| `aaymeloglu/README_aaymeloglu.md`, `aaymeloglu/AUDIT.md`, `aaymeloglu/audit/` | the contributor's account, the history of the work and the second model's review |
| `aaymeloglu/own_decode.py` | the project's decoder and count |
