# Matriks Keputusan Anotasi UD Batak Toba (Revisi 2, 20 Agustus 2026)

Status: draf untuk divalidasi narasumber ahli bahasa Batak Toba. **Keputusan diatesis sudah dikunci** lewat `04_keputusan_diatesis.md` (Opsi C, diatesis simetris). Rujukan: UD v2; UD Bahasa Indonesia [7][8][9]; UD Tagalog-TRG [10] dan UD-NewsCrawl [17]; Cebuano [11]; Nababan [1]; Cumming [15]; Erlewine [16]; Schachter [18]; Emmorey [19]; Wouk & Ross [20]; Dyer & O'Brien [21].

Konvensi: baris bertanda (?) adalah keputusan yang paling perlu dikonfirmasi ahli. Contoh kata bersifat ilustratif dan wajib dicek ejaan serta maknanya.

---

## Bagian 1 - Kelas Kata (UPOS, 17 tag)

| UPOS | Kriteria di Batak Toba | Contoh | Catatan keputusan |
|------|------------------------|--------|-------------------|
| NOUN | Nomina umum | jabu (rumah), dengke (ikan), huta (kampung) | Nomina hasil nominalisasi par-/-on tetap NOUN |
| PROPN | Nama diri (orang, tempat) | Polan, Toba, Samosir | Didahului artikel si; si dianotasi terpisah sebagai DET |
| PRON | Pronomina bebas | au (saya), ho (kamu), ibana (dia), hami/hita (kami/kita) | Enklitik posesif -ku/-mu/-na: lihat Bagian 3 |
| VERB | Predikat verbal berafiks diatesis | mangallang (makan, AV), diallang (dimakan, PV), ro (datang) | Prefiks maN-/mar-/di-/tar- menentukan fitur Voice |
| ADJ | Predikat/atribut sifat | uli (bagus), balga (besar), metmet (kecil) | Sering jadi root predikat tanpa kopula |
| ADV | Keterangan | nunga (sudah), nangkin (tadi), sai (selalu) | Penanda aspek/temporal |
| AUX | Verba bantu/modalitas | naeng (akan/mau), boi (bisa) | Nababan §5.1.2.2.1 menunjukkan satu predikator kompleks, bukan verba matriks. Relasi `aux` ke predikator utama. Konfirmasi ahli. |
| ADP | Preposisi | di (di), tu (ke), sian (dari), dohot (dengan) | di preposisi lokatif, beda dari di- prefiks diatesis pasien |
| DET | Artikel & demonstratif | si (artikel nama), i (itu), on (ini), an (itu jauh) | si = det pada PROPN; i/on = demonstratif |
| NUM | Numeralia | sada (satu), dua, tolu (tiga) | Penggolong (classifier) sebagai NOUN + relasi terpisah |
| PART | Partikel non-inti | do, ma, ba, pe, nama | do & ma paling sering; lihat Bagian 4 |
| CCONJ | Konjungsi koordinatif | jala (dan), alai (tetapi), manang (atau) | |
| SCONJ | Konjungsi subordinatif | molo (jika), ai (karena), asa (agar), tingki (ketika) | |
| PRON/SCONJ (?) | Penghubung relatif na | na | (?) Rujuk metode rotasi pohon Alfina dkk [9] untuk arah kepala frasa relatif |
| INTJ | Interjeksi | ba, ah, ampun | |
| SYM | Simbol | %, Rp | |
| PUNCT | Tanda baca | . , ? ! | |
| X | Tak terklasifikasi/asing | (kata pinjaman tak teradaptasi) | |

Prioritas keputusan UPOS yang khas: (a) status si sebagai DET, (b) do/ma sebagai PART, (c) naeng/boi sebagai AUX, (d) na sebagai relativizer, (e) negator ndang/dang.

Catatan tambahan: Sagala dkk. (2023) memperlakukan reduplikasi sebagai kategori kelas kata tersendiri dalam Batak Toba. UD tidak menyediakan UPOS untuk reduplikasi. Reduplikasi ditangani lewat relasi, bukan lewat UPOS. Lihat Bagian 3.

---

## Bagian 2 - Fitur Morfologis (FEATS)

| Fitur | Nilai | Pemicu morfologis | Contoh |
|-------|-------|-------------------|--------|
| Voice | Act | prefiks maN- (mang-, man-, mam-, ma-, manga-) | mangallang = Voice=Act |
| Voice | Pass | prefiks di- | diallang = Voice=Pass |
| Voice | Lfoc (?) | sufiks -i (lokatif), bila memenuhi kriteria diatesis penuh | (?) cek korpus. Nilai ini sah di UD v2. |
| Voice | Bfoc (?) | sufiks -hon (benefaktif), bila memenuhi kriteria diatesis penuh | (?) cek korpus. Nilai ini sah di UD v2. |
| Voice | Mid atau Rcp (?) | prefiks mar- (intransitif/medial), masi-...-an (resiprokal) | Nababan mencatat tipe resiprokal tersendiri. Usul: mar- = Mid, masi- = Rcp. |
| Voice | (?) | prefiks tar- (potensial/tak sengaja) | (?) Tidak ada nilai Voice yang pas. Pertimbangkan tanpa Voice, atau fitur terpisah. |
| PronType | Prs | pronomina persona | au, ho, ibana |
| PronType | Dem | demonstratif | i, on, an |
| Number | Sing/Plur | reduplikasi / konteks | dakdanak (anak-anak) |
| Person | 1,2,3 | pronomina & enklitik posesif | -ku (1), -mu (2), -na (3) |
| Poss | Yes | enklitik posesif | jabu-na (rumahnya) |
| Definite | Def | demonstratif i/on sebagai penanda takrif (?) | jabu i (rumah itu) |
| Polarity | Neg | negator | ndang, dang |
| Aspect (?) | Perf/Prog | nunga (perfektif), manga- progresif (?) | nunga ro |

**Peringatan wajib dibaca anotator:** nilai `Voice=Pass` di sini menandai **diatesis pasien Austronesia**, bukan pasif Indo-Eropa. Aktor pada konstruksi ini tetap argumen inti, bukan keterangan opsional. Nilai `Pass` dipakai semata karena UD v2 belum menyediakan nilai `Pat` yang lebih tepat. Lihat `04_keputusan_diatesis.md` Bagian 5.1.

Kolom XPOS dikosongkan (belum ada tagset khusus Batak Toba), sesuai Tabel 1 proposal.

Fitur `Polite` tidak dipakai untuk sementara. Bahasa Jawa memakainya [22], tetapi Batak Toba tidak punya sistem tingkat tutur setara. Pantau korpus lisan. Bila muncul variasi sapaan sistematis terkait Dalihan Na Tolu, pertimbangkan ulang.

---

## Bagian 3 - Relasi Dependensi (DEPREL) untuk fenomena Batak Toba

| Relasi | Pemakaian di Batak Toba | Contoh konstruksi |
|--------|-------------------------|-------------------|
| root | Predikat awal kalimat (verba/adjektiva/nomina) | Mangallang ... ; Uli ... ; Guru ... |
| nsubj | **Pivot pada SEMUA diatesis.** Muncul setelah predikat. | Mangallang dengke do si **Polan** / Diallang si Polan do **dengke** i |
| obj | Pasien non-pivot pada diatesis aktor | Mangallang **dengke** ... |
| **obj:agent** | **Aktor non-pivot pada diatesis pasien (di-).** Argumen inti, bukan oblique. | Diallang si **Polan** do dengke i |
| obl | Keterangan berpreposisi (lokatif, dsb.) | ... di jabu |
| iobj | Objek tak langsung (jika ada) | - |
| det | Artikel si + PROPN; demonstratif i/on + NOUN | si Polan; jabu i |
| case | Preposisi di/tu/sian + nomina | di jabu, tu huta |
| discourse | Partikel do, ma sebagai penanda wacana/afirmasi | ... do ... |
| advmod | Keterangan & negasi ndang/dang | Ndang ro ... |
| aux | naeng/boi | naeng ro |
| nmod:poss | Posesif enklitik & posesor nominal | jabu-na; jabu ni si Polan |
| amod | Adjektiva atributif | jabu na uli (rumah yang bagus) |
| nummod | Numeralia atributif | tolu jabu |
| compound:redup (?) | Reduplikasi penuh, ablaut, dan parsial | boru-boru. Mengikuti UD Cebuano [11]. Konfirmasi ahli. |
| flat | Nama majemuk | Danau Toba |
| mark | Konjungsi subordinatif molo/ai/asa | molo ro ... |
| cc / conj | Koordinasi jala/alai | ... jala ... |
| punct | Tanda baca | . , ? |

**Relasi yang DIHAPUS dari draf sebelumnya:** `nsubj:pass` dan `obl:agent`. Jangan dipakai. Lihat `04_keputusan_diatesis.md`.

**Subtipe yang perlu dideklarasikan saat submit ke UD:** `obj:agent`, `nmod:poss`, `compound:redup`, `acl:relcl`.

Dua keputusan struktural terpenting:

1. **Urutan predikat awal.** Root adalah predikat pertama. Subjek pasca-predikat tetap `nsubj`, bukan dislokasi. Berlaku juga pada urutan terbalik emfatik (Nababan §5.2.1.2): posisi linear berubah, relasi gramatikal tidak.
2. **Diatesis simetris.** Aktor (maN-): pivot aktor = `nsubj`, pasien = `obj`, `Voice=Act`. Pasien (di-): pivot pasien = `nsubj`, aktor = `obj:agent`, `Voice=Pass`. Tidak ada demosi aktor menjadi oblique.

---

## Bagian 4 - Partikel do dan ma (keputusan khusus)

| Partikel | Fungsi | UPOS | DEPREL | Kepala |
|----------|--------|------|--------|--------|
| do | Penanda afirmasi/asertif setelah predikat | PART | discourse | ke predikat (root) |
| ma | Penanda imperatif/aspektual (?) | PART | discourse (?) | ke predikat |
| pe, ba, nama | Partikel wacana | PART | discourse | ke unsur relevan |

Konsisten dengan Tabel 1 proposal: do dianotasi PART dengan relasi discourse ke root. Nababan §5.2.1.1 mengonfirmasi posisi partikel modal tepat setelah predikator dan sebelum subjek.

---

## Bagian 5 - Isu terbuka untuk narasumber

Isu diatesis (sebelumnya nomor 1) **sudah diputuskan** dan dipindahkan ke `04_keputusan_diatesis.md`. Sisa isu:

1. Nilai Voice untuk mar- dan tar-.
2. Status na (relativizer): PRON vs SCONJ, dan arah kepala frasa relatif.
3. Penanda takrif i/on: fitur Definite atau cukup det.
4. UPOS negator ndang/dang: PART vs ADV.
5. Relasi untuk reduplikasi: konfirmasi `compound:redup`.
6. **Baru:** pseudo noun incorporation. Sitorus & Mulyadi (2026) menunjukkan Batak Toba punya konstruksi nomina objek yang menempel ketat pada verba, kehilangan kespesifikan, dan menolak modifikasi. Usulan awal: tetap `obj` dengan catatan, sampai ada keputusan ahli.
7. Konfirmasi status AUX naeng/boi (sudah cenderung jelas, tinggal validasi).

---

## Rujukan tambahan pada revisi ini

- [17] A. A. Aquino, L. J. V. Miranda, dan E. M. T. Or, "The UD-NewsCrawl Treebank: Reflections and Challenges from a Large-scale Tagalog Syntactic Annotation Project," arXiv:2505.20428, 2025.
- [18] P. Schachter (peny.), *Studies in the Structure of Toba Batak*, UCLA Occasional Papers in Linguistics No. 5, 1984. (Judul bab persis perlu diverifikasi di volume asli.)
- [19] K. Emmorey, dalam *Studies in the Structure of Toba Batak*, 1984. (Bukti konstituensi fonologis. Detail perlu diverifikasi.)
- [20] F. Wouk dan M. Ross (peny.), *The History and Typology of Western Austronesian Voice Systems*, Pacific Linguistics 518, ANU, 2002.
- [21] A. T. Dyer dan C. A. O'Brien, "Towards Better Annotation Practices for Symmetrical Voice in Universal Dependencies," dalam Proc. UDW, 2025.
- [22] I. Alfina, A. Yuliawati, D. Tanaya, dkk., "A Gold Standard Dataset for Javanese Tokenization, POS Tagging, Morphological Feature Tagging, and Dependency Parsing," *Forum for Linguistic Studies*, vol. 6, no. 5, 2024.
