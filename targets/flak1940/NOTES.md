# flak1940: radio messages of Flugabwehrkommando Schwarzwald, 17 May 1940, and the key of the day (NARA RG 242, T405 roll 9)

Status: read (9 Nov 2026; the message of 4 June added 12 Nov, nineteen more days added 14 Nov 2026, see the two Contribution sections). Contributed by Harumi-Matsuba (issue #364; repository `Harumi-Matsuba/flak1940-public`, commit a181cd7, per the contributor's licence file), who worked with AI agents (one a blind second reader, another for image judgements). **No human has checked the transcriptions**; the project has seen no 17 May image, and of the 4 June message only frame 0863 was compared with the NARA image (parts 2-5 not); what the project checked is the keys against the contributor's own transcriptions (`VERIFICATION.md`).

## The documents

NARA RG 242, microfilm publication T405 "German Air Force Records: Luftgaukommandos, Flak, Deutsche Luftwaffenmission in Rumänien", roll 9 (NAID 332033680). Two radio messages of 17 May 1940, both in five-letter groups of a double columnar transposition:

- Frame 0993: a teleprinter copy (SMU 0113 17/5 1500, "G-KDOS- 4 TEILE") of a message from Luftgaukommando VII to Flugabwehrkommando Schwarzwald, four parts of 179, 178, 167 and 130 letters. The recipient's hand-written fair copy is on frames 0994-0995.
- Frames 1025-1027: a hand-written radio form of a message sent by Flugabwehrkommando Schwarzwald Ic, two parts of 205 and 194 letters (frame 1026 is the back of the sheet with the last group); its teleprinter original is on frame 1024.

Catalogue 704 listed the reel as a test bed of Luftwaffe radio traffic, daily-keyed double transposition, with the 1939 key card at frame 350 and clear teleprinter messages on neighbouring frames as possible cribs. The first five-letter group of each part is the indicator group and is not text; without them the two messages have 634 and 389 letters, 1,023 in all.

`ciphertext_0993.txt` and `ciphertext_1025_1027.txt` are the contributor's transcriptions, `plaintext.txt` the letter strings his keys give, `key.txt` the two keys, `contributor_reading.md` the division into words and the spelling conventions, `contributor_method.md`, `contributor_open.md`, `contributor_prior_check.md`, `contributor_readme.md` and `contributor_sources.md` his documents.

## The cipher

A double columnar transposition: the plaintext is written in rows in a grid 24 columns wide, read off column by column in the order of the key numbers, and the result written in a grid 28 wide and read off the same way. The keys for 17 May 1940 (`key.txt`) are 15 12 20 8 17 4 22 9 19 2 16 11 5 21 10 3 14 24 7 13 1 6 18 23 and 24 17 10 21 6 18 27 1 22 16 7 25 11 2 20 23 4 8 13 19 28 14 5 9 15 3 26 12. The second key is 28 long, outside the 15-25 range suggested by the catalogue page. In the plaintext, X separates words and names, CH is written Q, numbers are spelled digit by digit, brackets are KLAMMER, the slash STRIQ and roman numerals follow ROEM (`contributor_reading.md`).

## How the keys were found

The contributor fixed the plaintext of parts 3 and 4 of frame 0993 from the recipient's fair copy (frames 0994-0995) by fitting spellings to the letter counts (a transposition does not change them), then ran two known-plaintext searches of his own (`src/kpa.c`, `src/kpb.c`, not in this folder) that gave the key lengths and the keys, from part 4 of frame 0993. The tools were first tested on the 1939 exercise message and its key card (frames 349-350). The final rotation of the columns was confirmed by parts 1, 2 and 4 becoming readable; parts 1 and 2 and the whole of frames 1025-1027 were not used and decrypt as they stand. In part 3, lines 2 and 3 (50 letters each) are interchanged on the page, and letter 113 is read T.

## What they say

Frame 0993: Flakgruppe Friedrichshafen hands over to Flugabwehrkommando Schwarzwald the 1st and 3rd platoons of the 3rd battery of Reserve Light Flak Battalion 932 (Herbertingen), to be transported by the Flugabwehrkommando and employed as arranged by telephone, and employs the 3rd platoon of Anti-aircraft Machine-gun Reserve Company 304 (Sigmaringen) at the protected object Herbertingen; the new positions and readiness to fire are to be reported. Frames 1025-1027: on 16 May 1940 the 1st platoon of 2./932 (2 cm) of Flakgruppe Friedrichshafen was assigned to Flugabwehrkommando Schwarzwald; the platoon has been ready to fire since 22.30 hrs in position 3031 west of Tüllingen and is subordinated to Battalion 942. The plaintexts survive in the same file in their contemporary form (the fair copy of 0993 and the teleprinter message on frame 1024), so no previously unknown text was read; what is new is the key of the day.

## Remaining gaps

- Seven of the 1,023 letters are wrong as plaintext (BATBERIE, TRANSPORTIWRT, FERNNUENDLIQER, the X and Q of part 4 of frame 0993, VIENULL and the final H of frame 1027); the contributor takes five of them for errors of the sender or the relay, since they are in the typed cipher text, and has no way to check - blocker: illegible; the typed text is the only witness here and the hand-written ones (e or R, h or k) cannot be settled from the handwriting
- A human check of both transcriptions against the NARA frame images - blocker: needs-physical-access; NARA is not reachable from the project
- How the key follows from the indicator group (the first five letters of each part) - blocker: no-key-material; the 1939 key card lists four three-letter Kenngruppen but no rule for this day is known
- 79 of the 13,215 letters of the nineteen days of issue #602 do not make their words as transcribed, and 8 letters are lost (2 on 21 May, 3 on 23 May, 3 on 24 May) - blocker: illegible; the contributor judged the 79 slips of the sheets from the images after the key was known, and the lost letters are on sheet backs that were not filmed
- A human check of the nineteen days' transcriptions against the NARA frames (84 cipher frames; the project compared frames 1114 and 0931) - blocker: needs-physical-access; no human reader of the frames is available to the project
- 3 May (frames 1100-1105), the second message of 9 April (frames 1120-1121) and 28 May (frames 905-906): the contributor's sealed attempts with the clear copies as cribs found no key - blocker: no-key-material; these and the other unread days are other keys and stay with catalogue 704

## Escalation

- [x] siblings: the recipient's fair copy (frames 0994-0995), the teleprinter original of the second message (frame 1024) and the 1939 exercise message with its key card (frames 349-350) used; the other days of the reel are other keys; 4 June was added on 12 Nov and nineteen more days on 14 Nov 2026 (sections below), and 3 May, the second message of 9 April and 28 May were tried by Jacob Houtrouw without a key
- [x] clear-pages: the fair copy and the teleprinter original are the plaintexts beside the ciphertext, and were used for the key
- [x] known-keys: the 1939 key card gave the system and tested the tools; its keys (21 and 19 long) do not apply to 1940
- [x] print: the contributor searched this ledger (all issues and pull requests at the time), Cryptiana, Cryptoole, Schmeh's blog, GitHub and the web (`contributor_prior_check.md`): nothing on the key or the messages
- [x] key-rebuild: the keys were recovered by known-plaintext search from part 4 and confirmed on the other five parts
- [n/a] retry: all parts decrypt; what is left is the transcription of a few letters

## Files

| File | Content |
|---|---|
| `ciphertext_0993.txt`, `ciphertext_1025_1027.txt` | the contributor's transcriptions, five-letter groups |
| `plaintext.txt` | the letter strings the keys give, six parts |
| `key.txt` | the two keys of 17 May 1940 |
| `contributor_*.md` | the contributor's reading, method, open points, prior-art search, README and sources |
| `VERIFICATION.md` | what the project re-checked |
| `houtrouw/` | the nineteen days of issue #602: keys, transcriptions, decryptions, readings, the contributor's text and the project's decoder |
| `profile.json` | the target profile |

## Contribution: the message of 4 June 1940 (Brice Dudout, 12 Nov 2026)

The five-part radio message of 4 June 1940 on frames 0863-0867 (179, 190, 194, 186 and 204 letters with indicator groups) decrypts in full with the key of that day, K1 (19) 9 14 17 1 12 6 18 3 16 10 4 8 19 13 7 2 11 15 5 and K2 (22) 19 22 9 17 1 12 7 16 21 13 10 20 4 18 2 15 6 3 8 11 5 14; its plaintext is the teleprinter message on frame 0862 (Flak units moved into position on 3-4 June 1940 to protect army unloadings in the Black Forest). Harumi-Matsuba published this key first, in a comment on issue #364 and in his repository (11 Nov 2026). Brice Dudout recovered the same keys independently the same day, from his own transcription of the images (28 Oct 2026, made before any key was known), by a known-plaintext search on parts 1 and 2, and tested them once on part 4, held out, under a pre-registered protocol (quadgrams -4.993 against -6.643 for the best of 400 controls; agreement with the predicted plaintext 0.989 against 0.227). Six doubtful letters were checked on the images; 129 of 129 words read as sense, 5 of them probable. Transcription, decryption, reading, translation, key, solver code and the frozen test are in `dudout/` (`dudout/README.md`).

### Integration check (12 Nov 2026)

- An own decoder written from `dudout/key_0604.txt` decrypts all five parts to the contributor's strings, letter for letter (928 letters). The SHA-256 values of the frozen files match. All 179 letters of frame 0863 (part 1) agree with the NARA image (catalog.archives.gov, reachable); parts 2-5 were not compared with the images.
- The read share is recounted by the README rule: the five probable words are guessed words, so 124 of 129 words read (96.1%), still over the bar. The contributor's own figure is 129 of 129 words read as sense.
- The key was public before the contributor's test (Harumi-Matsuba, 11 Nov 2026, 08:28 UTC; issue comment 10:41 UTC), and the K2 search uses the idea of his public `kpb.c`. That the search and the test came first, and that the comment was found only on 12 Nov, rests on the contributor's record (a single commit of 12 Nov 00:25 +0100, self-declared times). The 'held-out' agreement of 0.989 is a comparison with the text of the teleprinter copy on frame 0862, so it shows that the key is right and does not read a new text. Credit for the key of 4 June stays with Harumi-Matsuba (prior solution); this is a same-day re-derivation.

## Contribution: the keys of nineteen more days, 9 April to 1 June 1940 (Jacob Houtrouw, issue #602, 14 Nov 2026)

Jacob Houtrouw (writing as Jake Tschakka), working with AI models that read the images, made the cribs, ran the search and wrote the readings, posted in issue #602 the keys of nineteen more days of the reel with, for each day, the transcription of the cipher sheets, the two keys, the plain text, a reading and an English translation: 9 April, 2, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 23, 24, 26 and 29 May and 1 June 1940 (21 messages, 78 parts). Each key was found by a known-plaintext search with the clear copy of the message on the reel as the crib, the second key first as in Harumi-Matsuba's method; by his record each run followed a plan hashed beforehand. The messages are reports of Flak units changing position and the hour from which each was ready to fire, one order of Luftgaukommando VII to raise readiness (9 April) and one list of new reference points (23 May). The texts were known from the clear copies; the keys are the new result. Everything is in `houtrouw/` (`houtrouw/README.md`), copied from the issue; Brice Dudout's earlier attempts on six of these messages had found no key (`dudout/README.md`).

| Day (1940) | Frames | Messages | Letters read | Letters that do not make their words | Keys A / B | Trigram control (real / best of 300 shuffled) |
|---|---|---|---|---|---|---|
| 9 April | 1186-1187 | 1 msg, 5 parts | 874 | 7 | 23 / 27 | 90 / 22 |
| 2 May | 1112-1114 | 1 msg, 2 parts | 258 | 6 | 19 / 24 | 46 / 10 |
| 6 May | 1091-1092 | 1 msg, 2 parts | 349 | 1 | 18 / 22 | 60 / 12 |
| 8 May | 1084-1085 | 1 msg, 2 parts | 364 | 1 | 23 / 27 | 56 / 12 |
| 9 May | 1077-1081 | 1 msg, 4 parts | 714 | 8 | 17 / 20 | 119 / 20 |
| 10 May | 1069-1071 | 1 msg, 3 parts | 472 | 1 | 29 / 26 | 61 / 12 |
| 11 May | 1062-1065 | 1 msg, 4 parts | 653 | 2 | 25 / 21 | 101 / 18 |
| 12 May | 1055-1057 | 1 msg, 2 parts | 363 | 3 | 24 / 28 | 65 / 12 |
| 13 May | 1051-1054 | 1 msg, 3 parts | 505 | 0 | 23 / 19 | 79 / 15 |
| 14 May | 1048-1050 | 1 msg, 2 parts | 347 | 1 | 22 / 27 | 52 / 11 |
| 15 May | 1038-1040 | 1 msg, 2 parts | 316 | 1 | 29 / 26 | 50 / 13 |
| 16 May | 1028-1035 | 1 msg, 7 parts | 1,159 | 2 | 20 / 25 | 210 / 33 |
| 20 May | 0977-1003 | 2 msg, 11 parts | 1,954 | 7 | 27 / 23 | 321 / 41 |
| 21 May | 0963-0970 | 1 msg, 6 parts | 1,070 + 2 lost | 9 | 25 / 21 | 172 / 23 |
| 23 May | 0925-0937 | 2 msg, 8 parts | 1,435 + 3 lost | 10 | 26 / 22 | 179 / 28 |
| 24 May | 919-923 | 1 msg, 3 parts | 513 + 3 lost | 1 | 25 / 29 | 97 / 13 |
| 26 May | 916-918 | 1 msg, 2 parts | 283 | 1 | 27 / 21 | 44 / 10 |
| 29 May | 0898-0901 | 1 msg, 4 parts | 683 | 1 | 18 / 22 | 95 / 15 |
| 1 June | 0888-0894 | 1 msg, 6 parts | 903 | 17 | 21 / 26 | 138 / 23 |

He also reports the attempts that found no key: 3 May (frames 1100-1105), the second message of 9 April (frames 1120-1121) and 28 May (frames 905-906), two sealed attempts each, and inside the nineteen days the first attempts on 11 and 12 May, the first run on 29 May and the first framing of part 2 of 6 May.

### Integration check (14 Nov 2026)

- An own decoder, written from the keys and transcriptions in the issue (`houtrouw/decode.py`), gives his plain text for all nineteen days: 13,215 letters, 8 lost from the film and 79 that do not make their words as transcribed, at the places and in the numbers he lists for each day. The indicator rule is not uniform: parts 2 onward of 6, 10 and 11 May have no indicator group, and part 3 of 9 May has one of six letters.
- Control: on 30 common German trigrams the real keys score 44 to 321 per day; the best of 300 shuffled key pairs per day scores 10 to 41 (table above).
- Images (catalog.archives.gov, reachable): frame 1114 (2 May, part 2) agrees with his transcription in 98 of 98 letters; frame 0931 (23 May, message 1, part 5) in 89 of 90, the other being a letter he changed from i to c after the key was known and that looks like i on the sheet, so it is rather a slip of the sheet than a misreading; frame 1112, the clear copy of 2 May, carries the text of his reading (4./R 321 (Eisb.), Bad Krozingen, 2.5.1940 05.00 Uhr, F 96/40 g.Kdos.). The other 82 cipher frames and the other clear copies were not compared.
- Read share by letters, the measure this target uses: per day 0.977 (2 May) to 1.000 (13 May), counting a letter that does not make its word and a lost letter as holes; every day is over the bar. For the whole target, 15,074 of 15,174 letters (99.3%).
- By the contributor's record only: the sealed plans and their times (no plan or timestamp file was sent), the search and its scores, the agreement with the clear copies and with NARA's machine reading, and which model worked which day.
- The four pairs of days with the same key lengths (9 April and 8 May, 6 and 29 May, 10 and 15 May, 11 and 21 May) have different keys.
- `python docs/_check_reading.py flak1940` grades these files like the earlier ones of this target (spelled-out radio text is not what it measures).
