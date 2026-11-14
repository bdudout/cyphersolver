# neufville1779: Jean de Neufville's syllabic code with Baudouin, Sartine's secretary (Amsterdam-Paris, 1779-1780)

Status: in progress (read in part; folder only, no site page; Daniel is free to write the page or change anything here).

## What it is

The papers of the Amsterdam merchant Jean de Neufville (Jean de Neufville & fils), bound in the Department of State and now
in the Papers of the Continental Congress (National Archives, Record Group 360, microfilm M332 roll 4; free images in the
National Archives Catalog, file unit 464816476; see sources.md), hold a private correspondence in a numeric code:

- **de Neufville's drafts, April-May 1779** (pp.591-609), headed "Mad. d'Arras" or "Chaumont": plain French with code
  numbers written over the syllables (pp.599-603, 606, 608, 609), and one enciphered fair draft (pp.604-606) of the
  letter of 19 April 1779 whose plain text is on p.599;
- **letters from Paris, February 1779 to November 1781** (pp.487-590), addressed to "Monsieur Van Temmel chez Monsieur
  Jean de Neufville, négociant à Amsterdam", signed "Baudouin" and later "Dunoyer", with code groups inside clear
  French; de Neufville wrote the French over many of the groups (pp.516-548, 579), but not over all.

The code: numbers 1 to about 550, one number per letter, syllable, common word or name, with several numbers for common
units (re = 30, 229, 310; que = 22, 23, 278; les = 427, 428, 429). Names include 5 and 106 Le Ray de Chaumont, 529
Vergennes, 328 the Minister of Marine (Sartine), 444, 511 and 213 the Pensionary of Amsterdam, 508 the Stadholder, 500
Mr York (Sir Joseph Yorke), 550 the Ambassador and 417 La Vauguyon, 531 the Spaniards, 464 the States General, 103 the
Amsterdammers, 174 and 169 America, 346 and 347 France, 368 Martinique. key/key_entries.tsv gives every entry and its
source.

## Who read what

- **Who made which table.** On 7 March 1779 (p.499) Baudouin wrote: "je me depesche de faire le chiffre pour vous
  l'envoyer, en attendant, je vous en joins un petit icy, que vous entendrez aisement, ce n'est qu'un changement de
  noms", and that he would sign with "un des noms que je prends dans le petit chiffre cy joint". On 30 March 1779
  (p.516) he acknowledges "la lettre ... avec le chiffre qui y étoit joint et que j'ay trouvé à merveille".
  - So there were two tables: Baudouin's "petit chiffre", a list of cover names (not in the file), and a "chiffre" that
    reached Baudouin from de Neufville by 30 March.
  - The evidence makes it likely that the numeric code of the drafts is the one de Neufville sent. It does not show
    who composed it: Baudouin had said he was making one, and de Neufville may have sent his own instead or as well.
  - Neither table survives as a table; the numeric code is rebuilt here from its use.
- **Jean de Neufville** enciphered his own letters from his plain drafts, and wrote the plain French over many of
  Baudouin's groups. Those parts were read by him in 1779-1780.
- **Baudouin** read de Neufville's letters in the code (the sent letters are not in this file).
- **The Department of State's clerk** who bound and indexed the volume in the 19th century made the identification:
  his index (p.3) lists the correspondent as "Du Noyer, Bowdoin or Mad. D. Arras".
- **The Franklin Papers editors** cite the letter of 23 February 1779 (p.495) as "a cryptic note from Baudouin to an
  unknown recipient" (Papers of Benjamin Franklin 28:354 n.9). Fold3's indexers listed the drafts as "Letters from William Lee to John de Neufville and Son ...
  in French with cipher".
- **What this folder adds** (Andrew Beling, with AI agents, 13-14 Nov 2026):
  - the reconstruction of the code from de Neufville's drafts and the glosses;
  - the evidence on the leaves for the index-maker's identification of "Dunoyer" as Baudouin (the hand, the 7 March
    letter, the 30 March letter);
  - the reading of the bare passages that no one glossed (B573, B491, B492), each transcribed in two passes by the
    same agent (top-down and from the end backward).
  A second AI agent of ours, not a person, checked the folder independently on 13-14 Nov 2026. Its corrections are
  applied (key/corrections_post_test.tsv and below).

## Identification of the correspondent (made by the volume's index; the evidence on the leaves)

- pp.495-497, Paris 23 February 1779, and pp.498-499, Paris Monday 7 March 1779, are signed **"Baudouin"**. The second ends:
  "à l'avenir je signeray un des noms que je prends dans le petit chiffre cy joint".
- From 30 March 1779 the letters in the same hand are signed "Dunoyer"; the covers to "Van Temmel" are docketed "Baudouin".
- The volume's index (p.3, 19th-century hand) already makes the identification. It reads: "12. Thirty-five . . . Du Noyer, Bowdoin or Mad. D. Arras (Private
  news from Paris, for use U.S. 1779-81.)", folio 148.
- Baudouin is Sartine's secretary at the Ministry of Marine: Papers of Benjamin Franklin 29:5-7, note 4 to Dumas's letter of
  1 March 1779 ("'Baud——' for Sartine's secretary Baudouin"); Baudouin's own notes to Franklin, 5 and 25 May 1779 (PBF 29:438).
- "Mad. d'Arras" as a cover for the same man is an inference, from the index and from the same code being used in both
  directions. It is not stated on any leaf.

## The tests

The keys are in key/FREEZE.txt and the test plans in TEST_PLAN.md. Two limits on what the files can show:
- Each test script builds its key by majority vote from a pair file written earlier and scores it in the same run, so
  the file times cannot show that a key was frozen before its test. What is fixed beforehand is the pair file, not the
  key file.
- The full key key_full_r3.json was built after p.573 had already been decoded once with an earlier key. The entries it
  added for p.573 (158 aux, 100 ent, 136 au, 224) come from glosses and drafts on other pages, so the reading is not
  circular, but the key was not frozen before the first look at the passage.
- T2 is weak as a test, because its ten held-out pairs were chosen so that each number also occurs among the training
  pairs.

A second agent of ours took 183 pairs from the drafts pp.599 and 601 before seeing the key. It agreed on 87 of 94
numbers, confirmed 38 of 39 further key entries on the images, and reran the three tests with identical results.

| Test | Key | Result | 200 shuffled keys |
|---|---|---|---|
| T1: predict pp.604-605 from drafts pp.600-603, 609 only | K1, 139 numbers | 139 of 146 covered groups as in the writer's draft p.599 | mean 1.8, max 15 |
| T2: ten p.599 pairs held out | K1 + other p.599 pairs | 8 of 10 | mean 0.21, max 3 |
| T3: the whole 6 May 1779 draft (p.608) held out | K2, 170 numbers | 64 of 65 covered groups (the miss: 106 "Chaumont" for "M. de Ch.") | mean 0.6, max 7 |

The misses in T1 and T2 are the writer's own variants (86 ne/na, 263 i/j, and the word "ménagera", which p.599 glosses
96 86 36 92 = mé na ge ra while his other drafts use 36 = ra, 92 = la).

Corrections after the tests are in key/corrections_post_test.tsv; the frozen keys are unchanged. Each was checked
on the image: 224 is m in "compter" (p.600) and n in "l'emprunt" (p.573), so it is m/n; 381 "passe" is a misreading of 384;
9 is "deux" (p.600) and "da" (p.599); 71 is "on" (p.535 gloss) and "mme" (p.601). No reading in this folder changes.

Statistical validation (docs/_validate.py, validation.tsv: the drafts' own plain units plus the bare passages read with
key_full_r3): pass, z 9.1 against random keys, 4.1 against refits to shuffled text.

## Integration check (14 Nov 2026)

Done for the project at integration of pull request #587; the contributor's text above and below is unchanged.

| Claim | Contributor | At integration | How |
|---|---|---|---|
| T1, pp.604-605 from K1 | 139 of 146, shuffles max 15 | 139 of 146; 200 shuffles max 15; own 2,000 shuffles max 23 | scripts rerun; own scorer |
| T2, ten held-out pairs | 8 of 10, max 3 | 8 of 10, max 3 | script rerun |
| T3, p.608 held out | 64 of 65, max 7 | 64 of 65, max 7 | script rerun |
| Key hashes | key/FREEZE.txt | all three equal | sha256 |
| Full key | 204 numbers | 204, identical | own build from the pair files |
| Bare passages, numbers | 43 + 18 + 7 | 68 of 68 agree with the images | frames 0428, 0363, 0364a |
| B573 read share | 39 of 43 numbers, 91% | 13 of 18 words, 72% | strict rule, below |
| B491 read share | 12 of 18 numbers, 67% (86% without four nulls) | 10 of 16 units, 62% | strict rule |
| B492 read share | 5 of 7 numbers, 71% | 1 of 4 words, 25% | strict rule |

- **Tests.** All three reproduce, and the key files rebuild byte for byte. Each passes the bar its plan sets (T2 exactly
  at the bar). The order of events (plans written before the runs, keys frozen before scoring) is by the contributor's
  record; the contributor says the same above.
  - T1: K1 covers 146 of the 179 groups that have a unit in the draft, so 139 is 77.7% of all of them.
  - T3: the truth file holds 69 pairs. On the image of p.608 at least 13 further groups stand over the French and are
    not in it (313 in "connoisse", 32 290 85 60, 204 before "envie", 261 310 133, 88 74 61 230 248 164). T3 therefore
    scores the pairs that were aligned, not the whole page. One of the groups left out, 204 for "l'", would be a miss.
- **Second decoder.** A decoder written here from the pair files gives the same key and the same four decodes. One
  difference: 136 has one vote for "à" and one for "au"; the frozen key holds "à", and letters/B573_decode.txt prints
  "au". The reading needs "au", which the gloss on p.516 gives.
- **Images** (National Archives Catalog, `.../M332/004/<frame>.jp2`, fetched by plain download). Frames for the drafts:
  p.599 = 0449, p.600 = 0450, p.601 = 0451a, p.603 = 0452, p.604 = 0453, p.608 = 0455b.
  - The three bare passages: every number agrees with letters/B*_groups.txt (68 of 68). The last number of p.573 looks
    like 369.
  - Key sources: about 60 of the 69 pairs of p.608, 35 pairs of p.600 and 40 pairs of p.599 were compared with the
    numbers standing over the French; all agree. p.599 does carry the numbers over de Neufville's own words, and its
    lower block spells the units out under the numbers, so T1 is scored against pairs that are on the leaf.
  - On p.599 the number 30 stands over "re" in "encore" (47 30). "g" for 30 in "ar{g}ent" (B573) and "{G}rand" (B492) is
    therefore against the key in both places. Both words are counted as holes.
- **Identification.** Seen on the images: the index entry on p.3 ("12. Thirty-five ... Du Noyer, Bowdoin or Mad. D. Arras
  (Private news from Paris, for use U.S. 1779-81.)", folio 148); the letter of 23 February 1779 signed "Baudouin" (frames
  0366-0367b); the letter headed "A Paris le Lundy 7 mars 1779" (frames 0368-0369a) with "je me depesche de faire le
  chiffre ... je vous en joins un petit icy ... ce n'est qu'un changement de noms", signed "Baudouin", and "à l'avenir je
  signeray un des noms que je prends dans le petit chiffre cy joint"; the cover to "Monsieur Van Temmel chez Mr Jean de
  Neufville negociant à Amsterdam". The hand of these letters and of the letters of January 1780 looks the same; that
  was judged by eye, by an AI model, not by a person. 7 March 1779 was a Sunday, so "Lundy 7" is the writer's slip or
  the letter is of the 8th.
  - Not checked here: that Baudouin was Sartine's secretary, and the Franklin Papers notes (28:354 n.9; 29:5-7 n.4;
    29:438). Founders Online answered scripted requests with an empty response on 14 Nov 2026 (a bot check); it needs a
    browser.
- **Strict read shares** (sure words only; an open number, an unread number and a unit set by the word against the key
  are holes; counted in words carried by code numbers):
  - B573: 13 of 18. Read: les, États, Généraux, a, retiré, aux, l'emprunt, un, emprunt, son, au, crédit, du. Holes: [3],
    [58]rands, [227]er, ar{g}ent, [369/349]. "l'emprunt" reads exactly with 38 = ru (the p.526 gloss); "un emprunt"
    needs 352 and 394 as "un" where the key has "une", and 224 = m (key/corrections_post_test.tsv).
  - B491: 10 of 16. Read: Stadhouder (twice), à, la, cour, Monsieur, le, Pensionnaire, de, Amsterdammois. Not read: 507,
    501, 405, 387, 390, 447. That the last four are nulls is the contributor's suggestion, not shown.
  - B492: 1 of 4 ("ce"; [143], [162] and "{G}rand" are holes).
  - Together 24 of 38 = 63%. The contributor's figure, in numbers with a key value, is 56 of 68 = 83%.
- **Prior art and duplicates.** No entry for this file, de Neufville or Baudouin in `catalogue.json`, `research/leads.json`,
  the ledgers or any other target (the other "Neufville" entries are Villeroy and Bordeaux-Neufville). The contributor's
  searches were not repeated, except Founders Online, which was blocked as above. Not a DECODE record.
- **Corrections made in profile.json:** the three bare passages are "read in part" with the strict shares (they were
  "read" with 0.91, 0.67 and 0.71); the pooled share is 0.63; the system summary and one credit note no longer say that
  de Neufville made the code (who composed it is not shown, as stated above).
- **State.** Folder only, `Status: in progress`, as the contributor filed it. The open numbers have steps not yet tried
  (the glossed letters pp.516-548 in full, the rest of Baudouin's letters pp.487-590 for the numbers 3, 58, 143, 162,
  227, 501 and 507, and the value of 30 in Baudouin's own use), so no page is written yet.

## The bare passages

Decoded with key/key_full_r3.json (204 numbers). In the readings, [n] marks a hole and {x} a unit settled by the word, not
by the key.

**B573, "Dunoyer" (Baudouin) to "Van Temmel" (de Neufville), 24 January 1780 (p.573).** 43 numbers, 39 read (91%; 38 by the key as written, the 39th being 30 = g).
The last number is 369 or 349: the middle digit could be this hand's 6 or its looped 4 (our first pass and the second
agent read 369). Either way it is a hole.
"Il est certain que le patriarche et la bande joyeuse feront tous leurs efforts pour faire avaler la dernière pilule,
mais ... cela couvrira **les États Généraux** d'opprobre et de ridicule. Il y a longtemps que [3] **a retiré aux
[58]rands** l'affaire de **l'emprunt** ... d'ouvrir **un emprunt** où personne ne se soucie de **[227]er son ar{g}ent**,
cela ne peut que faire beaucoup de tort **au crédit du [369/349]**." He then advises de Neufville to speak to "M. du Fresne".
- In English, as close as the French allows: the patriarch and the merry band will do all they can to make [them]
  swallow the last pill, but this will cover the States General with shame and ridicule. It is long since [3] took "the
  loan business" away from the [58]rands, and he has given it up since de Neufville met obstacles there. To open a loan
  in which nobody cares to [227] his money can only do much harm to the credit of the [369/349].
  - That "the loan" is the American loan de Neufville was trying to raise is inference; the letter says only "l'affaire
    de l'emprunt".
- Open numbers and candidates (holes in the text):
  - 3: a person. The only gloss of 3 is the numeral 3 (p.529), which does not parse here.
  - 58: an initial. "Grands" fits if 58 = G, and so does 30 = g in B492 "{G}rand". The Grand family of bankers is
    meant if so; Dumas calls Georges Grand "le ch—— G——" (PBF 29:5-7 n.4).
  - 227: "plac-", "hasard-" or "risqu-".
  - 369/349: "Congrès" (context only).
- 30 is read "g" here because the word "argent" forces it; in de Neufville's drafts 30 is "re". So 30 is either a homophone
  or a writer's slip; a slip for 33 (= ge) is the simpler explanation.

**B491, the same to the same, 18 January [1780] (p.491).** 18 numbers, 12 read (67%; 86% if the four likely nulls are left out).
"Je pense absolument comme M. Leerding sur le compte du **Stadhouder** [507] [501] [405 387 390 447] **Stadhouder** ...
il se pare **à la cour** de son savoir-faire et de ses succès, qu'il ne doit qu'à **Monsieur le Pensionnaire des
Amsterdammois**."
- Pass 2 (from the end backward) corrected one number of pass 1 (206 to 204, "le").
- 405, 387, 390 and 447 are probably nulls. Each occurs in de Neufville's fair draft pp.604-605 only at places where his
  cipher has a number with no counterpart in his own plain draft, and none has a reading anywhere in the file. This is
  evidence, not proof.
- 507 also heads both unglossed lines of p.527, struck through by the writer each time, and 501 is unglossed on p.529.
  Both are open.

**B492, second page of the same letter (p.492).** 7 numbers, 5 read (71%; one unit by the word only).
"On a déjà proposé plusieurs fois à ma tante d'acheter son [143] ... il y a certainement du tripotage au sujet de **ce**
[162] entre V. Vort et **{G}rand**."
- The gloss over 143 on p.534 may read "vaisseau(x)", but it is too faint to enter in the key; 143 stays a hole.
- "Ma tante", "le saint homme", "V. Vort", "le patriarche", "l'ami du cœur" and "M. du Fresne" are covers used in clear.
  Du Fresne is Chaumont: de Neufville glossed "Mr de Fresne" with "Chaumont" on p.579. The others are not identified.

**B527, two unglossed lines in the letter of 9 April 1779 (p.527).** Decoded to syllables but not read.
- Line 1: "[327] [441] ca do s s", followed in clear by "sucre brut et blanc, caffé &c.". "cadeaux" is possible but not
  forced.
- Line 2: "Vergennes [400] fi su ca in in s ta", followed by "au surplus". It does not parse.

## Inventory of the file (all 808 images checked at readable size)

Code numbers occur only on pp.487-609. Classes:
- (a) de Neufville's drafts with numbers over the French: pp.599, 600-603, 604-606, 608, 609. About 1,100 numbers.
- (b) Baudouin's letters glossed by de Neufville: pp.516, 526-528, 529, 530-531, 534-535, 547-548, 579. About 380 numbers.
- (c) Bare: pp.491-492, the two lines on p.527, p.573. About 90 numbers.

What this folder contains of each:
- the (a) items as aligned pairs: transcriptions/p604-606_cipher_with_p599_draft.tsv, key/heldout_p608_truth.tsv,
  key/key_source_pairs_pp600-603_609.tsv;
- the (b) glosses as pairs: key/key_pairs_classB_glosses.tsv. The glossed letters are not transcribed in full, and
  doubtful glosses were left out;
- every (c) passage in full: letters/B*.

p.504 is de Neufville's list of four signal numbers. 7, 8, 14 and 15 mean "Spain will declare the independence of America",
"... will go to war with England", "... will make the general peace" and "Spain will stay quiet".

## History and significance

Kept apart: what the letters say; established history, with the reference checked in this work; and inference.

**What the letters say.**
- De Neufville was passing Paris news to the Pensionary of Amsterdam. Baudouin was asking about Spanish intentions, the
  Amsterdam Pensionary and the French ambassador, and he advised on de Neufville's dealings with Chaumont ("M. du Fresne").
- In January 1780 Baudouin wrote that opening a loan nobody would put money into could only harm "the credit of
  [369/349]". That this is the American loan is inference. He also wrote that the patriarch and the merry band would make
  [them] swallow the last pill, to the shame of the States General.
- De Neufville's draft of 19 April 1779 reports that he passed news of Spain to the Pensionary and could not yet sound
  him about a direct correspondence.

**Established history (checked here).**
- In September 1778, at Aix-la-Chapelle, de Neufville negotiated a plan of a treaty of amity and commerce with William Lee,
  acting for the Pensionary and burgomasters of Amsterdam. His 1792 petition to Congress for compensation was rejected on
  Jefferson's report of 26 November 1792 (Papers of Thomas Jefferson 24:664-667, which cites Schulte Nordholt, *The Dutch
  Republic and American Independence*, 1982, pp.64-69).
- The pro-American Pensionary of Amsterdam was Engelbert François van Berckel ("notre ami" in Dumas's letters). The
  French ambassador at The Hague was the duc de La Vauguyon, the British ambassador Sir Joseph Yorke, and the Stadholder
  William V was generally pro-British (PBF 29:5-7 n.4).
- John Paul Jones's squadron lay in the Texel in October-December 1779. Yorke demanded the Serapis, and de Neufville & fils
  supplied the squadron. This file holds the letters (pp.127-345, among them Yorke's memorial of 8 October 1779 at p.299).

**Background not checked in this work.**
- Spain entered the war in June 1779.
- The British seizure of the Dutch convoy under Bylandt on 31 December 1779 - 1 January 1780 is very probably the "last
  pill" of B573.
- De Neufville's loan for Congress in 1780-81 failed. Van Winter's *American Finance and Dutch Investment* was not
  consulted.

**Inference.** A merchant's private code channel into the office of the Minister of Marine shows the French ministry
using an Amsterdam banker to work on the Amsterdam regents beside, and perhaps around, its ambassador. The letters'
worry about La Vauguyon's "confidences" (p.526 glosses) points that way. This is a reading of a few letters, not a
finding of the literature.

## Provenance (how the papers reached the government)

- **Documented:** the volume, with the index page "Diplomatic Letters" cross-referenced to "Dep. Correspondence Vol. II", was
  bound with the Continental Congress papers in the Department of State. Jefferson's 1792 report says he "examined the
  records of the Department of State". The National Archives Catalog gives no accession note. Butler's *Index to the
  Papers of the Continental Congress* (1978) indexes "Van Temmel".
- **Conjecture:** the papers came in with de Neufville's own claims, his 1792 petition or his widow's of 1797. They may
  also have been handed over earlier as intelligence "for use U.S.", as the index puts it. Neither route is documented
  here. The Journals of Congress and the American State Papers (Claims) were not searched.

## In print

One letter is cited, none is printed:
- Papers of Benjamin Franklin 28:354, note 9 (Founders Online, Franklin/01-28-02-0286) cites "a cryptic note from Baudouin
  to an unknown recipient, Feb. 23, 1779, mentioning that Stürler had arrived in Paris and had been in contact with
  someone named Montaigu. National Archives." That is p.495 of this file. The editors did not identify the recipient and
  do not mention the code.
- Nothing was found that prints the letters' text, their content or the code.

Searches made:
- Founders Online: "Neufville Baudouin" finds only Dumas's letters with the abbreviation note; "Dunoyer" and "Temmel" find
  nothing relevant.
- HathiTrust full text: "Van Temmel" Neufville finds only Butler's index. Wharton's *Revolutionary Diplomatic
  Correspondence* is full text there, and it does not match.
- Schulte Nordholt, *The Dutch Republic and American Independence*, and van Winter, *American Finance and Dutch
  Investment*: no hits for Baudouin, Dunoyer, Van Temmel or Sartine in HathiTrust's search-only view. One hit for
  "Arras" in van Winter vol. 2, probably the town, was not seen.
- Cryptiana: nothing found.

## Remaining gaps

- Numbers 3, 58, 227, 369/349, 507, 501, 143 and 162, the two lines of p.527, and the likely nulls 405, 387, 390 and 447 - blocker: open-codes; not glossed or drafted in the pairs taken so far.
- The glossed letters pp.516-548 are transcribed as pairs only - blocker: not-attempted; workable, and the place to look for the open numbers.
- Baudouin's letters of February 1779 to November 1781 (pp.487-590) contain more clear intelligence that is not summarised here - blocker: not-attempted.

## Escalation

Checklist added at integration (14 Nov 2026), from the contributor's list below:
- [x] siblings: all 808 images of the file paged; code numbers only on pp.487-609
- [x] clear-pages: de Neufville's plain drafts and glosses are the key source; no plain text of the bare passages found
- [x] known-keys: neither table survives as a table; no other key of this correspondence is known
- [x] print: Founders Online, HathiTrust full text, Cryptiana (see "In print")
- [x] key-rebuild: three rounds (K1, K2, full key), each from more drafts and glosses
- [ ] retry: the glossed letters in full and the rest of Baudouin's letters have not been worked for the open numbers

Tried for the open numbers:
- every glossed letter and draft in the file (all 808 images paged);
- the code's own thematic neighbours (names sit at 500-550, but there is no alphabetical run that settles 3, 58, 227 or 369/349);
- Founders Online, HathiTrust full text and Cryptiana.

Not tried:
- the Archives nationales Marine series (B4, B7) or Sartine's papers, where Baudouin's office copies or de Neufville's
  sent letters may survive;
- Dutch archives (the Stadsarchief Amsterdam's van Berckel papers).
