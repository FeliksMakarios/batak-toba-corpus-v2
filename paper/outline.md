# Kerangka Artikel Ilmiah: Pedoman Anotasi UD Batak Toba

Target: jurnal nasional terakreditasi SINTA 2-4 atau prosiding internasional bereputasi. Jenis: studi pedoman anotasi + validasi awal (annotation guideline / resource paper).

Judul usulan: "Merancang Pedoman Anotasi Universal Dependencies untuk Bahasa Batak Toba: Keputusan Diatesis, Urutan Predikat Awal, dan Validasi Awal pada Korpus Kecil"
(versi Inggris bila prosiding internasional: "Towards Universal Dependencies for Toba Batak: Annotation Guidelines for Voice and Predicate-Initial Order with a Pilot Inter-Annotator Study")

## Abstrak (150-250 kata)
Urgensi (bahasa berdaya rendah tanpa treebank), tujuan (pedoman UD + uji awal), metode (4 tahap), hasil utama (skor IAA + temuan konstruksi bermasalah), kontribusi (pedoman terbuka + korpus 250 kalimat).

## 1. Pendahuluan
- Konteks Batak Toba: 1 juta+ penutur, tata bahasa mapan (Nababan) tapi minim sumber komputasi (NusaWrites, NusaX berhenti di korpus mentah/sentimen).
- Masalah: belum ada treebank, tag kelas kata/dependensi, maupun pedoman anotasi.
- Celah: adaptasi UD diatesis Austronesia baru untuk bahasa Filipina (Tagalog, Cebuano), belum Austronesia Sumatra.
- Kontribusi (3 poin): pedoman UD pertama untuk Batak Toba; keputusan eksplisit diatesis & predikat-awal; validasi empiris via IAA.

## 2. Latar Belakang & Karya Terkait
- Kerangka UD (Nivre dkk; de Marneffe dkk).
- UD Bahasa Indonesia (Alfina dkk): fitur morfologis, arah kepala frasa.
- Adaptasi diatesis Austronesia: UD Tagalog-TRG, Cebuano.
- Metodologi treebank bahasa berdaya rendah: Occitan, Uzbek, Ho (anotasi agile, prapemrosesan otomatis, mulai dari korpus kecil).
- Deskripsi linguistik Batak Toba: Nababan, Cumming (urutan predikat), Erlewine (ekstraksi & licensing).

## 3. Ciri Linguistik Batak Toba yang Relevan untuk UD
- Urutan predikat awal.
- Sistem diatesis (aktor maN- / pasien di-), morfologi verba.
- Predikat non-verbal tanpa kopula, partikel do/ma, artikel si, demonstratif i/on.

## 4. Metode Penyusunan Pedoman
- Tahap 1: sintesis keputusan dari literatur -> matriks keputusan.
- Tahap 2: perumusan pedoman v1 + contoh berlabel.
- Tahap 3: anotasi rintisan 250 kalimat, 2 anotator, format CoNLL-U, prapemrosesan pengurai delexicalized.
- Tahap 4: evaluasi IAA + revisi.
- (Sertakan diagram alir = Gambar 3 proposal.)

## 5. Keputusan Anotasi Utama
- Pemetaan diatesis ke relasi inti (nsubj/obj vs nsubj:pass/obl:agent); justifikasi Opsi A vs B.
- Penanganan urutan predikat awal (subjek pasca-verba = nsubj).
- Partikel, artikel, demonstratif, negasi.
- Subtipe spesifik bahasa bila diperlukan.

## 6. Pengujian & Hasil
- Statistik korpus (jumlah kalimat/token per strata genre).
- Metrik IAA: kesepakatan UPOS, UAS/LAS agreement antaranotator, kappa per lapis.
- Tabel konstruksi paling sering tidak disepakati.
- Analisis kualitatif contoh ketidaksepakatan.

## 7. Diskusi
- Konstruksi tersulit dianotasi & sebabnya.
- Revisi pedoman yang dipicu temuan.
- Perbandingan dengan adaptasi diatesis Tagalog/Cebuano.
- Keterbatasan (ukuran korpus, 2 anotator, genre).

## 8. Kesimpulan & Kerja Lanjut
- Ringkas kontribusi; TKT 2 -> 3.
- Rencana treebank skala penuh (peta jalan Tahun II-V).

## Ketersediaan Data
Pedoman, korpus 250 kalimat (CoNLL-U), dan skrip di repositori terbuka (GitHub/repo UD).

## Referensi
Gunakan 16 rujukan proposal sebagai basis; tambah rujukan metrik IAA (mis. Cohen/Krippendorff, evaluasi parsing).

---
## Peta luaran -> bagian artikel
| Luaran proyek | Masuk ke bagian |
|---------------|-----------------|
| Matriks keputusan (Tahap 1) | Bagian 5 + tabel lampiran |
| Pedoman v1 & revisi | Bagian 4, 5, 7 |
| Korpus 250 kalimat CoNLL-U | Bagian 6 (statistik) + Ketersediaan Data |
| Skor IAA | Bagian 6 (hasil utama) |
