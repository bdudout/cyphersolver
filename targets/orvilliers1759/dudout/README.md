# D'Orvilliers to the Navy minister, Cayenne, 10 June 1761 (ANOM C14 25 fol. 36): read (Brice Dudout, 28 Oct 2026)

Status: read (Brice Dudout, 28 Oct 2026; about 247 of 250 words read in their sense, 3 groups open).

Write-up: https://bdudout.github.io/europe-chiffree/en/documents.html#cayenne-1761

## Access

Brice Dudout opened the C14 24 and C14 25 volumes in an ordinary browser on IREL (recherche-anom.culture.gouv.fr, after the
automatic Anubis page) and saved the views: the C14 volumes are online at volume level (`.../images/MINISTERES/SEM/C14/C14_025/FRANOM34_C14_025_NNN.jpg`),
even though the item notices carry no digital object. No image is included here (no reuse licence).

## The code

A numerical Navy nomenclator of about 500 numbers for letters, syllables and words (215 de, 307 nous, 136 la, 112 garnison,
91 troupes, 355 pour, 375 sans), with homophones (458 and 290 = t; 185 and 170 = d) and words left in clear. It is the same from
1757 to 1762, and it is not the Windward Islands code of mercier1761 (key1761.tsv / key1765_ennery.tsv do not fit: 136 = la,
311 = est here). The Martinique letters of 1744 use another table (C8 A 56 f. 13: "nous avons reçu la" = 165 304 386 491 215 301 302 456 229).

## Key and check held out

Method (protocol written before computing, cryptanalysis/c04/PROTOCOL.md): (1) full transcription of the glossed letters of 1759 (C14 24 fols. 25–29, 32v–33: about 2,500 numbers with their contemporary interlinear decipherment); (2) number ↔ plain alignment by maximum likelihood (EM, respecting word boundaries), key K1 frozen (SHA-256 fca8fcce…) before any validation; (3) validation on a glossed letter held out, d’Orvilliers 10 June 1761, fols. 39–40 (618 numbers, 314 words): 0.955 of the letters recovered (controls with permuted values, 200 draws: p99 = 0.405) and 0.638 of the words exactly (p99 = 0.103) — the code is the same from 1759 to 1761; (4) key K2 retrained on all glossed letters, then K3 = K2 + six values corrected from the context of the target letters, frozen (SHA-256 6469d776…); (5) reading of the letter of 10 June 1761. Files in our research folder.

## Reading

First published decipherment, to our knowledge. 489 cipher numbers, about 250 words. Published under Daniel Bourdeau’s rule: 95% of the words read in their sense. Here: ≈ 247 of 250 words read in their sense (≈ 99%), of which ≈ 236 certain (≈ 94%); 10 words restored from the sense [x] (numbers used only once), 1 probable, 3 unresolved (‹150›, ‹351›, ‹347›).

- The Des Essarts plan. The joint letter of the same day (C14 25 fol. 171, glossed at the time) sets out “M. Desessars’s plan”: to write to his correspondent so as to be understood without risking the secret, and to bring clothing, provisions and even munitions to Cayenne by a foreign route. A year later (20 August 1762, fol. 65) d’Orvilliers reports a purchase of piastres in Holland “through the widow Hamilton of Rotterdam, for Des Essarts”: the channel announced here did work. Surinam, the neighbouring Dutch colony, served as the declared destination of neutral ships supplying Cayenne.
- Restored words. Ten numbers occur only once in the letter and in our training letters; their value follows from the sense and the shape of the sentence: 34 [preuve] and 269 [zèle] (“une … du … de M. Desessars”), 353 [particulier] (against “en commun”; this is the governor’s private “1st” letter), 492 [prompt] (“un … secours”), 192 [dernière] (“dans la … misère”), 95 [Surinam] (twice: “ils enverront à …”, “sucreries de …”), 247 [projet] (twice: “les effets propres au …”, “accomplir ce …”), 493 [moindre] (“le défaut du … sol”). In “{pro}pres”, number 485 is not attested elsewhere with this value.
- The three unresolved numbers. ‹150› (“feront passer par les ‹150›x”: a plural in -x, perhaps “vaisseaux”); ‹351› (“cet ‹351› est dangereux”: “accident”, “état”?); ‹347› (“si je dois être ‹347›”: the first digit is overwritten; “tranquille” or “content” fit the sense).
- Values corrected from context (key K3, see method): 297 = i (“possib·i·lité”), 296 = al (“roy·al”, as in “al·lumée” and “mort·al·ités” in other letters of 1760), 360 = ta (“re·ta·rdement”), 164 = éb (“éb·oulement”), 239 = cl (“obsta·cl·e”), 163 = telle. Two encipherer slips: 290 (t) for u in “par une muraille”.
- Prior work. The office note at the top reads “le triplicata déchiffré”; that decipherment is not filed with the letter, and the ANOM entry says “entirely in cipher and not translated”. Daniel Bourdeau’s repository (folder orvilliers1759) noted on 28 October 2026 that the images were not accessible; no published reading found.

## Other letters (not in this PR)

Read with the same key but not yet written up: 27 Sep 1760 (fols. 11-12v) and 20 Dec 1760 (fols. 14-17), both with
"passages chiffrés non traduits". In C14 24 (1757-1759) every cipher passage we saw is glossed or a duplicate of a glossed copy.

Files: `transcription.txt`, `decryption.txt`, `key.tsv`, `reading.md`.
