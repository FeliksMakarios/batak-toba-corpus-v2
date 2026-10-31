# Pedoman Anotasi Universal Dependencies Batak Toba - Versi Awal (v0.1)

Draf awal untuk anotasi rintisan korpus kecil. Semua contoh WAJIB divalidasi narasumber ahli bahasa Batak Toba sebelum dipakai melatih anotator. Rujukan: UD v2, UD Bahasa Indonesia [7][8][9], UD Tagalog-TRG [10], Cebuano [11], Nababan [1], Cumming [15], Erlewine [16].

## 1. Prinsip umum
1. Format: CoNLL-U, 10 kolom (ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC). XPOS dikosongkan (_), belum ada tagset khusus.
2. Satu kalimat satu pohon, satu root.
3. Root adalah predikat pertama (verba, adjektiva, atau nomina), sesuai tipologi predikat-awal Batak Toba.
4. LEMMA = bentuk dasar tanpa afiks diatesis (mangallang -> allang; diallang -> allang).
5. Anotasi ganda: dua anotator menganotasi kalimat yang sama secara paralel untuk pengukuran IAA.

## 2. Keputusan inti

### 2.1 Urutan predikat awal
Subjek muncul setelah predikat. Root tetap predikat pertama, subjek pasca-verba dianotasi nsubj (bukan dislokasi/parataxis).

### 2.2 Diatesis (Voice)
- Diatesis aktor, prefiks maN-: Voice=Act. Actor = nsubj, pasien = obj.
- Diatesis pasien, prefiks di-: Voice=Pass. Pasien = nsubj:pass, actor = obl:agent.
- Pilihan pemetaan actor pada di- (Opsi A: obl:agent selaras UD ID; Opsi B: subtipe spesifik bahasa selaras Tagalog-TRG). Pedoman ini memakai Opsi A secara default; catat bila ahli menyarankan Opsi B.

### 2.3 Predikat non-verbal tanpa kopula
Predikat nominal dan adjektival TIDAK memakai kopula. Predikat = root, subjek = nsubj.

### 2.4 Partikel do / ma
UPOS PART, relasi discourse ke root.

### 2.5 Artikel si dan demonstratif i/on
- si sebelum nama diri: DET, relasi det ke PROPN.
- i (itu) / on (ini) sebelum nomina: DET, FEATS PronType=Dem, relasi det ke NOUN.

## 3. Contoh berlabel (format CoNLL-U)

### Contoh 1 - Diatesis aktor, verba transitif (dari proposal, Tabel 1)
```conllu
# sent_id = btk_pilot-001
# text = Mangallang dengke do si Polan.
# text[ind] = Si Polan sedang makan ikan.
1	Mangallang	allang	VERB	_	Voice=Act	0	root	_	_
2	dengke	dengke	NOUN	_	_	1	obj	_	_
3	do	do	PART	_	_	1	discourse	_	_
4	si	si	DET	_	_	5	det	_	_
5	Polan	Polan	PROPN	_	_	1	nsubj	_	SpaceAfter=No
6	.	.	PUNCT	_	_	1	punct	_	_
```

### Contoh 2 - Predikat adjektival tanpa kopula (dari proposal, Tabel 1)
```conllu
# sent_id = btk_pilot-002
# text = Uli do jabu i.
# text[ind] = Rumah itu bagus.
1	Uli	uli	ADJ	_	_	0	root	_	_
2	do	do	PART	_	_	1	discourse	_	_
3	jabu	jabu	NOUN	_	_	1	nsubj	_	_
4	i	i	DET	_	PronType=Dem	3	det	_	SpaceAfter=No
5	.	.	PUNCT	_	_	1	punct	_	_
```

### Contoh 3 - Diatesis pasien (prefiks di-) [DRAF, validasi ahli]
```conllu
# sent_id = btk_pilot-003
# text = Diallang si Polan do dengke i.
# text[ind] = Ikan itu dimakan (oleh) si Polan.
1	Diallang	allang	VERB	_	Voice=Pass	0	root	_	_
2	si	si	DET	_	_	3	det	_	_
3	Polan	Polan	PROPN	_	_	1	obl:agent	_	_
4	do	do	PART	_	_	1	discourse	_	_
5	dengke	dengke	NOUN	_	_	1	nsubj:pass	_	_
6	i	i	DET	_	PronType=Dem	5	det	_	SpaceAfter=No
7	.	.	PUNCT	_	_	1	punct	_	_
```

### Contoh 4 - Predikat nominal tanpa kopula [DRAF, validasi ahli]
```conllu
# sent_id = btk_pilot-004
# text = Guru do inang.
# text[ind] = Ibu adalah guru.
1	Guru	guru	NOUN	_	_	0	root	_	_
2	do	do	PART	_	_	1	discourse	_	_
3	inang	inang	NOUN	_	_	1	nsubj	_	SpaceAfter=No
4	.	.	PUNCT	_	_	1	punct	_	_
```

### Contoh 5 - Keterangan lokatif berpreposisi [DRAF, validasi ahli]
```conllu
# sent_id = btk_pilot-005
# text = Modom do si Ucok di jabu.
# text[ind] = Si Ucok tidur di rumah.
1	Modom	modom	VERB	_	_	0	root	_	_
2	do	do	PART	_	_	1	discourse	_	_
3	si	si	DET	_	_	4	det	_	_
4	Ucok	Ucok	PROPN	_	_	1	nsubj	_	_
5	di	di	ADP	_	_	6	case	_	_
6	jabu	jabu	NOUN	_	_	1	obl	_	SpaceAfter=No
7	.	.	PUNCT	_	_	1	punct	_	_
```

### Contoh 6 - Negasi [DRAF, validasi ahli]
```conllu
# sent_id = btk_pilot-006
# text = Ndang ro si Ucok.
# text[ind] = Si Ucok tidak datang.
1	Ndang	ndang	PART	_	Polarity=Neg	2	advmod	_	_
2	ro	ro	VERB	_	_	0	root	_	_
3	si	si	DET	_	_	4	det	_	_
4	Ucok	Ucok	PROPN	_	_	2	nsubj	_	SpaceAfter=No
5	.	.	PUNCT	_	_	2	punct	_	_
```

Catatan Contoh 6: pilih konsisten UPOS negator ndang (PART vs ADV) dan relasi (advmod). Konfirmasi ahli.

## 4. Daftar periksa anotator (per kalimat)
- [ ] Root = predikat pertama.
- [ ] Voice terisi untuk verba maN-/di-.
- [ ] Argumen diatesis benar (obj vs nsubj:pass; nsubj vs obl:agent).
- [ ] do/ma = PART discourse.
- [ ] si = DET/det; i/on = DET/det + PronType=Dem.
- [ ] Preposisi = ADP/case; frasa preposisi = obl.
- [ ] Tidak ada kopula pada predikat non-verbal (kecuali diputuskan lain).
- [ ] LEMMA tanpa afiks diatesis.
- [ ] SpaceAfter=No sebelum tanda baca yang menempel.

## 5. Isu terbuka untuk validasi ahli (agenda 4 sesi narasumber)
1. Pemetaan actor pada di- : obl:agent (Opsi A) vs subtipe spesifik bahasa (Opsi B).
2. Status naeng/boi : AUX vs VERB.
3. Nilai Voice untuk mar- dan tar-.
4. Status na (relativizer) : PRON vs SCONJ; relasi acl:relcl.
5. Penanda takrif via i/on : fitur Definite atau cukup det.
6. UPOS negator ndang/dang.
