# Pedoman Anotasi Universal Dependencies Batak Toba - Versi 0.2

> **Catatan 2 Oktober 2026.** Anotasi rintisan 250 kalimat mulai 5 Oktober 2026 memakai Pedoman Anotasi UD Batak Toba v1.0 pada [anotasi-ud/pedoman/arsip/](../anotasi-ud/pedoman/arsip/pedoman-anotasi-ud-v1.0.md), yang sejak 28 Oktober 2026 digantikan oleh [v1.2](../anotasi-ud/pedoman/pedoman-anotasi-ud-v1.2.md). Dokumen v0.2 ini dipertahankan sebagai arsip rancangan. Perbedaan utama pada v1.0:
>
> 1. Aktor bertanda *ni* pada pasif kompletif (-in-/ni-) dan promisif (-on) diberi `obl:agent` dengan *ni* sebagai `case`. Aktor tak bertanda tetap `obj:agent`.
> 2. Penanda atributif *na* diberi `PART` dengan relasi `mark`.
> 3. Kelas kata dan konstruksi dirujuk langsung ke pasal Nababan (1981).

Perubahan dari v0.1: pemetaan argumen diatesis diganti mengikuti keputusan Opsi C (diatesis simetris). Relasi `nsubj:pass` dan `obl:agent` dihapus. Lihat `04_keputusan_diatesis.md` untuk dasar buktinya.

Semua contoh WAJIB divalidasi narasumber ahli bahasa Batak Toba sebelum dipakai melatih anotator.

## 1. Prinsip umum

1. Format CoNLL-U, 10 kolom (ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC). XPOS dikosongkan.
2. Satu kalimat satu pohon, satu root.
3. Root adalah predikat pertama (verba, adjektiva, atau nomina), sesuai tipologi predikat-awal Batak Toba.
4. LEMMA = bentuk dasar tanpa afiks diatesis (mangallang menjadi allang, diallang menjadi allang).
5. Anotasi ganda: dua anotator menganotasi kalimat yang sama secara paralel untuk pengukuran IAA.

## 2. Keputusan inti

### 2.1 Urutan predikat awal

Subjek muncul setelah predikat. Root tetap predikat pertama, subjek pasca-predikat dianotasi `nsubj`, bukan dislokasi atau parataxis.

Pada urutan terbalik untuk penekanan (Nababan §5.2.1.2), unsur yang dipindahkan ke depan **tidak berubah relasinya**. Posisi linear berubah, relasi gramatikal tetap. Root tetap predikator.

### 2.2 Diatesis: Batak Toba adalah bahasa diatesis simetris

Ini keputusan paling penting dalam pedoman ini, dan paling sering salah kalau anotator terbawa kebiasaan Bahasa Indonesia.

**Batak Toba TIDAK punya pasangan aktif-pasif seperti Bahasa Indonesia.** Batak Toba punya dua diatesis yang sama-sama transitif penuh. Perbedaannya hanya pada argumen mana yang menjadi pivot, bukan pada argumen mana yang didemosikan.

| | Verba | Pivot | Non-pivot |
|---|---|---|---|
| Diatesis aktor (maN-) | `Voice=Act` | aktor = `nsubj` | pasien = `obj` |
| Diatesis pasien (di-) | `Voice=Pass` | pasien = `nsubj` | aktor = `obj:agent` |

Tiga hal yang harus dipahami anotator:

1. **`nsubj` dipakai untuk pivot pada kedua diatesis.** Tidak ada `nsubj:pass`.
2. **Aktor pada klausa di- adalah argumen inti, bukan keterangan.** Karena itu `obj:agent`, bukan `obl:agent`. Aktor ini terikat ketat pada verba: tidak bisa disisipi adverbia, tidak ditandai preposisi, dan membentuk satu satuan fonologis bersama verba.
3. **Nilai `Voice=Pass` di sini berarti diatesis pasien, bukan pasif.** Nilai `Pass` dipakai semata karena UD v2 belum menyediakan nilai `Pat`. Jangan terjemahkan ke intuisi pasif Bahasa Indonesia.

Cara cepat membedakan `obl` dari `obj:agent`: kalau ada preposisi (di, tu, sian, dohot), itu `obl` dengan preposisi ber-`case`. Kalau nomina menempel langsung ke verba di- tanpa preposisi, itu `obj:agent`.

### 2.3 Predikat non-verbal tanpa kopula

Predikat nominal dan adjektival tidak memakai kopula. Predikat menjadi root, subjek menjadi `nsubj`.

### 2.4 Partikel do dan ma

UPOS `PART`, relasi `discourse` ke root. Posisinya tepat setelah predikator dan sebelum subjek.

### 2.5 Artikel si dan demonstratif i/on

- si sebelum nama diri: `DET`, relasi `det` ke PROPN.
- i (itu) atau on (ini) sebelum nomina: `DET`, FEATS `PronType=Dem`, relasi `det` ke NOUN.

### 2.6 Negasi

Negator ndang dan dang mendahului predikator, dan berlaku untuk predikat verbal maupun non-verbal. Relasi `advmod` ke predikat.

## 3. Contoh berlabel (format CoNLL-U)

### Contoh 1 - Diatesis aktor, verba transitif

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

### Contoh 2 - Predikat adjektival tanpa kopula

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

### Contoh 3 - Diatesis pasien (DIUBAH pada v0.2)

```conllu
# sent_id = btk_pilot-003
# text = Diallang si Polan do dengke i.
# text[ind] = Ikan itu dimakan si Polan.
1	Diallang	allang	VERB	_	Voice=Pass	0	root	_	_
2	si	si	DET	_	_	3	det	_	_
3	Polan	Polan	PROPN	_	_	1	obj:agent	_	_
4	do	do	PART	_	_	1	discourse	_	_
5	dengke	dengke	NOUN	_	_	1	nsubj	_	_
6	i	i	DET	_	PronType=Dem	5	det	_	SpaceAfter=No
7	.	.	PUNCT	_	_	1	punct	_	_
```

Perhatikan: `si Polan` adalah `obj:agent` (dulu `obl:agent`), dan `dengke` adalah `nsubj` (dulu `nsubj:pass`).

### Contoh 4 - Predikat nominal tanpa kopula

```conllu
# sent_id = btk_pilot-004
# text = Guru do inang.
# text[ind] = Ibu adalah guru.
1	Guru	guru	NOUN	_	_	0	root	_	_
2	do	do	PART	_	_	1	discourse	_	_
3	inang	inang	NOUN	_	_	1	nsubj	_	SpaceAfter=No
4	.	.	PUNCT	_	_	1	punct	_	_
```

### Contoh 5 - Keterangan lokatif berpreposisi

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

Bandingkan Contoh 5 dengan Contoh 3. Di sini `jabu` punya preposisi `di` ber-`case`, jadi `obl`. Di Contoh 3, `si Polan` tanpa preposisi dan menempel pada verba, jadi `obj:agent`.

### Contoh 6 - Negasi predikat verbal

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

### Contoh 7 - Negasi predikat nominal (BARU pada v0.2)

Nababan §5.1.2.2 menunjukkan negasi juga berlaku pada predikat non-verbal.

```conllu
# sent_id = btk_pilot-007
# text = Dang karani ibana.
# text[ind] = Dia bukan pegawai.
1	Dang	dang	PART	_	Polarity=Neg	2	advmod	_	_
2	karani	karani	NOUN	_	_	0	root	_	_
3	ibana	ibana	PRON	_	PronType=Prs|Person=3	2	nsubj	_	SpaceAfter=No
4	.	.	PUNCT	_	_	2	punct	_	_
```

### Contoh 8 - Urutan terbalik emfatik (BARU pada v0.2)

Nababan §5.2.1.2. Subjek dipindah ke depan untuk penekanan. Relasi tidak berubah.

```conllu
# sent_id = btk_pilot-008
# text = Ibana do marpesta nantoari.
# text[ind] = DIA yang berpesta kemarin.
1	Ibana	ibana	PRON	_	PronType=Prs|Person=3	3	nsubj	_	_
2	do	do	PART	_	_	3	discourse	_	_
3	marpesta	pesta	VERB	_	_	0	root	_	_
4	nantoari	nantoari	ADV	_	_	3	advmod	_	SpaceAfter=No
5	.	.	PUNCT	_	_	3	punct	_	_
```

Root tetap predikator `marpesta` meskipun muncul di posisi ketiga. `Ibana` tetap `nsubj` meskipun ada di awal kalimat.

## 4. Daftar periksa anotator (per kalimat)

- [ ] Root = predikat pertama (walau ada unsur emfatik di depannya).
- [ ] Voice terisi untuk verba maN- dan di-.
- [ ] Pivot = `nsubj` pada kedua diatesis. **Tidak ada `nsubj:pass`.**
- [ ] Aktor pada verba di- = `obj:agent`. **Tidak ada `obl:agent`.**
- [ ] Pasien pada verba maN- = `obj`.
- [ ] do dan ma = PART discourse.
- [ ] si = DET/det; i dan on = DET/det + PronType=Dem.
- [ ] Preposisi = ADP/case; frasa preposisi = obl.
- [ ] Tidak ada kopula pada predikat non-verbal.
- [ ] Negasi = advmod ke predikat, termasuk predikat nominal.
- [ ] LEMMA tanpa afiks diatesis.
- [ ] SpaceAfter=No sebelum tanda baca yang menempel.

## 5. Isu terbuka untuk validasi ahli

Isu diatesis sudah diputuskan. Sisa isu:

1. Nilai Voice untuk mar- dan tar-.
2. Status na (relativizer): PRON vs SCONJ, relasi acl:relcl, dan arah kepala.
3. Penanda takrif i/on: fitur Definite atau cukup det.
4. UPOS negator ndang/dang: PART vs ADV.
5. Relasi reduplikasi: konfirmasi compound:redup.
6. Pseudo noun incorporation: apakah nomina yang menyatu dengan verba tetap obj.
7. Konfirmasi AUX naeng/boi.

Tiga uji khusus untuk memperkuat keputusan diatesis (lihat `04_keputusan_diatesis.md` Bagian 7): uji penyisipan adverbia, uji binding refleksif, dan uji pelesapan aktor.
