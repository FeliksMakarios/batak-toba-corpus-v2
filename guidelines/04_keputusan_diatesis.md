# Keputusan Anotasi 001: Pemetaan Argumen Diatesis

> **Catatan 2 Oktober 2026.** Keputusan ini diteruskan ke Pedoman Anotasi UD Batak Toba v1.0 pada [anotasi-ud/pedoman/](../anotasi-ud/pedoman/pedoman-anotasi-ud-v1.0.md): pivot tetap `nsubj` dan aktor tak bertanda tetap `obj:agent`. Pedoman v1.0 menambahkan `obl:agent` khusus untuk aktor bertanda *ni* pada pasif kompletif (-in-/ni-) dan promisif (-on). Pernyataan pada Bagian 1 bahwa `obl:agent` diganti berlaku untuk aktor tak bertanda.

Status: **DIPUTUSKAN (Opsi C)** oleh ketua tim, 20 Agustus 2026. Menunggu konfirmasi narasumber ahli bahasa untuk detail pelaksanaan, bukan untuk arah keputusan.

Dokumen ini adalah catatan keputusan (decision record) yang mengunci pilihan pemetaan argumen diatesis untuk pedoman anotasi UD Batak Toba, beserta dasar bukti dan konsekuensi teknisnya. Keputusan ini menentukan seluruh sisa pedoman.

---

## 1. Keputusan

Batak Toba dianotasi sebagai bahasa **diatesis simetris (symmetrical voice)**, bukan sebagai bahasa aktif-pasif gaya Indo-Eropa. Konsekuensinya:

| Konstruksi | Verba | Argumen pivot | Argumen non-pivot |
|------------|-------|---------------|-------------------|
| Diatesis aktor (maN-) | `Voice=Act` | aktor = `nsubj` | pasien = `obj` |
| Diatesis pasien (di-) | `Voice=Pass` | pasien = `nsubj` | aktor = `obj:agent` |

Tiga perubahan dari draf sebelumnya:

1. `nsubj:pass` **dihapus**. Pivot memakai `nsubj` polos di semua diatesis.
2. `obl:agent` **diganti** `obj:agent`. Aktor pada klausa di- adalah argumen inti, bukan oblique.
3. Nilai `Voice` tetap `Act` dan `Pass`, dengan catatan wajib di pedoman bahwa `Pass` di sini berarti diatesis pasien Austronesia, bukan pasif Indo-Eropa. Alasan teknis di Bagian 5.

---

## 2. Alasan (ringkasan argumen ketua tim)

Pada bahasa berdaya rendah setiap kalimat latih sangat berharga, dan model butuh pola yang ajek untuk menggeneralisasi. Memaksakan skema aktif-pasif pada bahasa berdiatesis simetris menciptakan inkonsistensi laten: melabeli aktor sebagai `obl` (yang menurut definisi UD bersifat opsional) padahal aktor itu terikat kuat pada verba akan membingungkan model dalam mengenali batas klausa yang sah. Opsi C memaksa model mempelajari hierarki argumen yang sebenarnya, bukan hierarki yang di-Indonesiakan.

---

## 3. Dasar bukti

### 3.1 Bukti internal Batak Toba (paling kuat, urutkan seperti ini di artikel)

**a. Konstituensi fonologis.** Emmorey (1984) menunjukkan bahwa DP non-pivot pasca-verba membentuk satu satuan fonologis bersama verba untuk keperluan penempatan tekanan. Ini bukti konstituensi, bukan sekadar kedekatan linear, dan merupakan bukti terkuat yang tersedia.

**b. Pembatasan adjacency.** Schachter (1984) mencatat DP non-pivot pada klausa transitif wajib bersebelahan dengan verba. Erlewine mengutip ini dan memberi contoh bahwa adverbia tidak bisa disisipkan antara verba dan DP non-pivot: `di-ida si Ria {*nantoari} si Torus`.

**c. Analisis struktural.** Erlewine (2018, *Language* 94(3)) memperlakukan pivot sebagai penghuni posisi khusus (spesifier VoiceP), dengan aktor non-pivot tetap internal terhadap VoiceP. Pola ekstraksi Batak Toba dibatasi oleh pelisensian nominal terbatas, dan hanya pivot yang bisa diekstraksi. Ini ciri bahasa bertipe Filipina.

**d. Ketiadaan penandaan preposisi.** Pada contoh Nababan (1981), aktor klausa di- muncul langsung setelah verba tanpa preposisi apa pun: *digarar ibana do utangna*, *ditongos nasida ma hepeng i*, *hujou hami do ibana*. Bandingkan dengan pasif Bahasa Indonesia yang menandai agen dengan *oleh*.

### 3.2 Bukti tipologis dan konsensus anotasi

**e.** Wouk & Ross (2002) mengklasifikasikan bahasa-bahasa Austronesia Barat, termasuk rumpun Batak, sebagai bersistem diatesis simetris, dengan konstruksi undergoer voice sebagai transitif penuh, bukan pasif yang mendemosikan aktor.

**f.** Dyer & O'Brien (2025) merekomendasikan penghentian `nsubj:pass` untuk bahasa diatesis simetris dengan alasan eksplisit: *"Non-pivot actors of a patient-voice sentence are not demoted to obliques the way they are in passive voice, but remain core arguments of the verb."*

**g.** Aquino, Miranda & Or (2025) menerapkan prinsip ini pada treebank Tagalog 15.600 pohon dengan memakai `nsubj` untuk pivot, `obj` untuk pasien non-pivot, dan `obj:agent` untuk aktor non-pivot.

---

## 4. Koreksi rujukan (WAJIB dibaca sebelum menulis artikel)

Tiga dari empat rujukan yang dipakai untuk mendasari keputusan ini bermasalah pada tingkat sitasi, meskipun kesimpulannya tetap benar. Kalau dibiarkan, ini akan jadi temuan reviewer.

### 4.1 Wouk & Ross (2002) — sitasi benar, cakupan perlu hati-hati

Rujukan asli: Wouk, F. & Ross, M. (peny.) (2002). *The History and Typology of Western Austronesian Voice Systems*. Pacific Linguistics 518, Australian National University. Tersedia akses terbuka di repositori ANU.

**Peringatan:** bab Batak dalam volume ini adalah Norwood, *Voice and valency alternations in Karo Batak*, yaitu **Batak Karo, bukan Batak Toba**. Kutip volume ini untuk kerangka tipologis Austronesia Barat, jangan untuk data Batak Toba secara spesifik. Kalau dikutip seolah memuat data Toba, reviewer yang paham akan menemukannya.

### 4.2 Schachter (1984) — substansi benar, judul dan tautan salah

Tautan yang diberikan mengarah ke Himmelmann (2008), *Lexical categories and voice in Tagalog*, di situs Universitas Köln. Itu karya lain sama sekali.

Rujukan yang benar: karya Schachter tentang Batak Toba terbit dalam Schachter, P. (peny.) (1984), *Studies in the Structure of Toba Batak*, UCLA Occasional Papers in Linguistics No. 5. Erlewine mengutipnya sebagai Schachter (1984a) untuk pembatasan adjacency DP non-pivot. Perlu dicek langsung di volume aslinya untuk memastikan judul bab persisnya sebelum masuk daftar pustaka.

**Catatan penting:** volume ini sudah ada di daftar pustaka proposal sebagai rujukan [15], yaitu Cumming (1984), *The Syntax and Pragmatics of Predicate Word Order in Toba Batak*, yang berada di volume yang sama. Jadi tinggal menambah entri dari volume yang sudah dikenal, bukan mencari sumber baru.

### 4.3 Musgrave (2001) — sitasi tercampur, dan berisiko kontraproduktif

Tiga masalah sekaligus:

1. Tautan yang diberikan adalah tautan Sci-Hub ke berkas `chung2017.pdf`, yaitu karya Sandra Chung, bukan Musgrave. Selain tidak cocok, jangan pernah mencantumkan tautan Sci-Hub dalam artikel ilmiah.
2. Dua judul tercampur. *Non-subject Arguments in Indonesian* adalah disertasi Musgrave (2001, University of Melbourne). *Voice and Grammatical Relations in Austronesian* adalah volume suntingan Austin & Musgrave (2008, CSLI). Keduanya karya berbeda.
3. **Masalah terbesar:** literatur LFG tentang Bahasa Indonesia justru bisa dipakai melawan argumen kita. Arka & Manning (1998), *Voice and Grammatical Relations in Indonesian: A New Perspective*, menyimpulkan bahwa dalam Bahasa Indonesia agen berupa **NP pasca-verba tetap oblique meskipun wajib bersebelahan dengan verba**, karena gagal pada uji binding refleksif dan topikalisasi. Hanya agen berupa enklitik *-nya* yang berstatus argumen inti.

Implikasi metodologis: **adjacency saja tidak membuktikan status argumen inti.** Reviewer yang menguasai literatur ini akan langsung menyerang argumen "aktor menempel pada verba, jadi argumen inti", karena ada preseden bahasa serumpun di mana justru tidak demikian.

**Cara memperbaikinya:** jangan pimpin argumen dengan adjacency. Pimpin dengan konstituensi fonologis Emmorey (1984) dan pola ekstraksi Erlewine (2018), lalu tempatkan adjacency sebagai bukti pendukung, bukan bukti utama. Bedakan juga Batak Toba dari Bahasa Indonesia secara eksplisit: Batak Toba mempertahankan sistem tipe Filipina yang lebih konservatif, sedangkan Bahasa Indonesia sudah bergeser. Justru perbedaan ini yang membuat Batak Toba menarik dan layak diteliti tersendiri.

### 4.4 Dyer & O'Brien (2025) — terverifikasi benar

Dyer, A. T. & O'Brien, C. A. (2025). *Towards Better Annotation Practices for Symmetrical Voice in Universal Dependencies*. Proceedings of the Universal Dependencies Workshop (UDW 2025). Tersedia di ACL Anthology.

---

## 5. Kendala teknis yang membatasi pelaksanaan

### 5.1 `Voice=Pat` belum sah di UD v2

Dyer & O'Brien mengusulkan `Voice=Pat` menggantikan `Voice=Pass`, dan `Ivoc` menggantikan `Ifoc`. **Usulan ini belum diadopsi UD.** Nilai `Voice` yang sah di UD v2 hanya sepuluh: Act, Mid, Rcp, Pass, Antip, Lfoc, Bfoc, Dir, Inv, Cau. Nilai `Pat` tidak ada di dalamnya dan akan ditolak validator resmi.

**Keputusan:** pakai `Voice=Pass` untuk korpus rintisan, dengan catatan wajib di pedoman bahwa nilai ini menandai diatesis pasien Austronesia dan bukan pasif Indo-Eropa. Ajukan `Voice=Pat` sebagai usulan saat treebank disubmit ke UD, dan jadikan bahan diskusi di artikel. Menyebut ketidaksesuaian ini di bagian Diskusi justru memperkuat artikel, karena menunjukkan kita paham batas kerangka yang dipakai.

Catatan: `Lfoc` dan `Bfoc` sudah sah dan dipakai Tagalog. Kalau nanti ditemukan konstruksi Batak Toba berdiatesis lokatif (sufiks -i) atau benefaktif (sufiks -hon) yang memenuhi kriteria diatesis penuh, kedua nilai ini bisa langsung dipakai tanpa masalah validator.

### 5.2 `obj:agent` perlu dideklarasikan

`obj:agent` adalah subtipe spesifik bahasa dan harus dideklarasikan dalam dokumentasi bahasa saat treebank disubmit. Dyer & O'Brien mengusulkan `obj:actor`, Aquino dkk. memakai `obj:agent`.

**Keputusan:** pakai `obj:agent`, dengan dua alasan. Pertama, sudah ada preseden pada treebank UD yang benar-benar dirilis (Tagalog NewsCrawl, 15.600 pohon), bukan sekadar usulan. Kedua, istilah agen lebih akrab bagi anotator berlatar Bahasa Indonesia.

### 5.3 Pivot memakai `nsubj` polos, bukan `nsubj:patient`

Dyer & O'Brien mengusulkan `nsubj:actor` dan `nsubj:patient`. Untuk korpus rintisan 250 kalimat dengan dua anotator, subtipe ini **tidak dipakai**, dengan alasan: peran semantik pivot sudah sepenuhnya bisa dipulihkan dari fitur `Voice` pada verba, sehingga subtipe hanya menduplikasi informasi sambil menggandakan peluang ketidaksepakatan antaranotator. Aquino dkk. juga memakai `nsubj` polos pada treebank berskala jauh lebih besar.

Catat pilihan ini di artikel sebagai keputusan sadar, bukan kelalaian.

---

## 6. Contoh anotasi setelah perubahan

Contoh diatesis pasien, dengan perubahan ditandai.

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

Perubahan dari versi lama: baris 3 dari `obl:agent` menjadi `obj:agent`, baris 5 dari `nsubj:pass` menjadi `nsubj`.

Diatesis aktor tidak berubah:

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

---

## 7. Uji yang tetap perlu dilakukan bersama narasumber

Arah keputusan sudah dikunci, tetapi tiga uji berikut tetap perlu dijalankan untuk memperkuat bagian Diskusi artikel dan menutup celah reviewer.

1. **Uji penyisipan.** Apakah adverbia benar-benar tidak bisa disisipkan antara verba di- dan aktor? Konfirmasi contoh Erlewine dengan penutur asli.
2. **Uji binding refleksif.** Apakah aktor pada klausa di- bisa mengikat refleksif? Ini uji pembeda yang dipakai Arka & Manning untuk memisahkan argumen inti dari oblique, dan menjawab langsung keberatan terkuat terhadap keputusan kita.
3. **Uji pelesapan.** Apakah aktor pada klausa di- bisa dilesapkan tanpa membuat kalimat janggal? Kalau tidak bisa, itu bukti tambahan status argumen inti, karena oblique menurut definisi opsional.

Jika ketiga uji ini mendukung, keputusan Opsi C berdiri di atas bukti internal Batak Toba sendiri, bukan sekadar analogi dari Tagalog.

---

## 8. Berkas yang harus diperbarui

| Berkas | Perubahan |
|--------|-----------|
| `guidelines/01_matriks_keputusan_anotasi.md` | Bagian 3: ganti baris obl:agent dan nsubj:pass. Hapus penyebutan Opsi A dan B. |
| `guidelines/02_pedoman_anotasi_v1.md` | Bagian 2.2 dan Contoh 3. Naikkan versi ke v0.2. |
| `guidelines/03_panduan_ringkas_anotator.md` | Tabel aturan kunci baris verba di-. |
| `corpus/pilot/btk_pilot.sample.conllu` | Kalimat btk_pilot-003. |
| `PROGRESS.md` | Coret isu terbuka nomor 1, ganti jadi terputuskan. |
| `paper/outline.md`, `paper/01` | Bagian 5 keputusan anotasi, plus koreksi rujukan Bagian 4 dokumen ini. |
| `scripts/validate_conllu.py` | **Tidak perlu diubah.** Sudah diperiksa: validator hanya membatasi nilai `root`, tidak membatasi deprel lain, jadi `obj:agent` lolos apa adanya. |

Berkas contoh `corpus/pilot/btk_pilot.sample.conllu` sudah diperbarui dan lolos validasi (8 kalimat, 43 token, `obj:agent` terbaca normal oleh `corpus_stats.py`).
