# sinclair1923 - Sinclair Oil code telegrams, 1922-1924 (catalogue 1437)

Status: no write-up. Attempted, open: the four telegrams are transcribed and 23 code books ruled out; no code word is decoded, so there is no reading to write up. Catalogue 1437 stays, outcome "attempted, open".

Source: Rice University, Woodson Research Center, MS 1052 (Teapot Dome Scandal, Sinclair Oil, and related company records), on the Portal to Texas History: metapth1891750, metapth1891738, metapth1891736 (code words) and metapth1891648 (two code names glossed in pencil). Images opened with curl through the Portal's IIIF server (texashistory.unt.edu/iiif/ark:/67531/<id>/m1/<n>/full/full/0/default.jpg, native 1500 px), 14 Nov 2026. No image in this folder.

Lead vetted by Andrew Beling, 13 Nov 2026 (PR #580): open, code book not identified.

## What was done (14 Nov 2026, Brice Dudout with Claude Opus 5.5)
- Full transcription of the four telegrams, two passes by an AI agent, the second blind on enlarged crops; the passes agree; three typing overstrikes in metapth1891736 left as alternatives (`transcription.txt`). The vetting quoted parts; this is the full text with headers and checks. The word totals match the operators' counts in the checks (42, 96, 30).
- Code book screening with a criterion fixed beforehand (`codebook_screening.md`): 23 OCR texts of commercial codes on archive.org (Western Union 1901, ABC 5th, Lieber's 1896 and 1915, Bentley's 1906, Bedford McNeill 1908, McNeill 1895, Moreing & Neal 1905, Acme 1923, Universal Trade 1921, Broomhall 1913 and others). Best coverage 6 of 67 words for 1923-24 and 6 of 12 for 1922; none passes. Nothing decoded.
- Reading sheet (`reading.md`): clear words read, code words unresolved; 47% of the words read by sense, so not read.

## Observations
- The 1923 and 1924 telegrams share ANZUNDET; in 1924 it twice follows FOR after "left"/"leaving", so it is probably a place.
- The 1923 telegram is a quoted text (QUOTE ... UNQUOTE) with numbered paragraphs, sent to Zevely at the office of John W. Lacey in Cheyenne, Sinclair's counsel there.
- 1922: ordinary English words used as code; ARROGANCE follows a day or an hour three times (a time word by position).
- 1916: OUTSPARAL and OUTSPAPIN are glossed H. F. Sinclair and E. R. Kemp; they share OUTSPA-, as neighbouring entries of a private list would.

## Open
- Identify the book: ABC 6th ed. (1920), Western Union Universal, Marconi International (1919), Peterson, Lombard, Scott's, Wright's Codigo brasileiro universal (1902) and the Berne vocabulary itself are not on archive.org; HathiTrust full-text search not reachable by script. A private Sinclair code is possible.
- The overstrikes in metapth1891736 (CABI?NA, M??DEREBBE, ARDEN-TELLB) need a look at the original or a higher-resolution scan.

## Remaining gaps
- Code book not identified, 89 code words (0 decoded). Blocker: no key material in reach. Not screened: ABC 6th ed. (1920), Western Union Universal, Marconi International (1919), Peterson, Lombard, Scott's, Wright's Codigo brasileiro universal (1902); none is on archive.org and the Berne vocabulary is search-only on HathiTrust. A private Sinclair list is possible (the 1916 names OUTSPARAL / OUTSPAPIN look like one).
- Three typing overstrikes in metapth1891736 (CABI{U|V}NA, M{O|C}{N|D}DEREBBE, ARDEN-TELLB). Blocker: illegible at the 1500 px the Portal serves; they stay as alternatives.
- No human has compared the transcription with the images (two AI passes by the contributor, a third at integration).

## Escalation
- Siblings: the other five items the Portal tags 'telegraphic commercial code' are plain English (Andrew Beling's vetting, PR #580); no further coded telegram of the firm is known here. Not searched: the rest of MS 1052 beyond that tag.
- Clear copies: the 1923 telegram quotes a document with numbered paragraphs; the document itself (Zevely / Lacey papers, the Senate oil-lease hearings exhibits) was not looked for beyond the three hearing volumes of the vetting.
- Known keys / print: 23 commercial codes screened, none passes the 90% coverage criterion (`codebook_screening.md`).
- Retry when one of the unscreened books, or a Sinclair private code, becomes reachable.

## Integration check (14 Nov 2026)
- Images: the four Portal IIIF images were fetched again (curl, 1500 px, no bot check) and every word of the four transcriptions compared: 42, 96, 30 and 45 body words, all agree, with the overstrikes and the pencil glosses (H. F. Sinclair, E. R. Kemp) as described. The 1923 address line reads "CARE JOHN W LACEY CHEYENNE WYO".
- Counts recounted by hand from `transcription.txt`: 42 / 96 / 30 words (168), of which 15 / 56 / 18 code words (89) and 27 / 40 / 12 clear words (79, 47%), as stated; RECOMMIT (counted as code) and RESPONSE (counted as clear) are the contributor's judgment calls, stated in `reading.md`.
- Not re-run: the archive.org OCR downloads behind the coverage table, and the HathiTrust searches (made in the contributor's browser). The files named under "Frozen files" (PREREG.md, codecheck.py, screening_results.txt) are not in the folder; the hash of `transcription.txt` matches (39461eba...). The order of events (criterion before screening, with the declared deviation) is by the contributor's record.
- Outcome: not solved. `fraction_read` 0.47 is the share of clear words, not a reading; nothing is decoded.
