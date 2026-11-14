# flak1940/houtrouw: the keys of nineteen more days, 9 April to 1 June 1940 (issue #602)

Contributed by Jacob Houtrouw (writing as Jake Tschakka; GitHub TheLightningCount) in issue #602, posted 14 Nov 2026 as text: the issue body carries 23 May, eighteen comments carry the other days. He directed the work, designed the tests and verified; AI models read the frame images, made the cribs, wrote and ran the search and wrote the readings (which model on which day is in his text, `<day>_issue.md`). No human has compared the transcriptions with the images. The plain texts are on the reel as clear copies, so no unknown text was read: what is new is each day's pair of keys.

## Files

| File | Content |
|---|---|
| `keys.txt` | the nineteen pairs of keys, as he gives them |
| `<day>_transcription.txt` | his transcription of the cipher sheets, as corrected after the key was known |
| `<day>_decryption.txt` | what the key gives from that transcription (the project's decoder), with his text beneath and the differing places marked |
| `<day>_reading.md`, `<day>_translation.md` | his radio text with word division and German, and his English, copied from the issue |
| `<day>_issue.md` | his whole text for the day as posted (documents, method, sealed plan, checks, prior work) |
| `decode.py` | the project's decoder; `python decode.py` re-runs the check below |

## The nineteen days, as the project's decoder counts them

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

13,215 letters read, 8 lost from the film, 79 that do not make their words as transcribed: the counts and the places are the ones he lists day by day. Four pairs of days have the same pair of key lengths (9 April and 8 May, 6 and 29 May, 10 and 15 May, 11 and 21 May); the keys themselves differ.

Indicator groups: the first five-letter group of each part is left out, except that parts 2 onward of 6, 10 and 11 May have none (their first group is text), and part 3 of 9 May has an indicator written with six letters.

## What he reports that the project did not check

- The search itself (second key annealed first on the crib made from the clear copy, then the first key) and its scores against decoys.
- The sealed plans: a SHA-256 per day with the time of sealing, RFC 3161 timestamps for the plans from 13 Nov 05:18 UTC on, and OpenTimestamps anchors. No plan or timestamp file was sent, so the order of plan and run is by the contributor's record.
- The agreement of each radio text with the clear copy (the project opened one, frame 1112 of 2 May, which carries the text of his reading) and with NARA's machine reading of the sheets.
- His attempts that found no key: 3 May (frames 1100-1105), the second message of 9 April (frames 1120-1121) and 28 May (frames 905-906), two sealed attempts each; and the first attempts on 11 and 12 May, the first run on 29 May and the first framing of part 2 of 6 May.
