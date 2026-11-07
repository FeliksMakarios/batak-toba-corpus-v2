# batak-toba-corpus-v2

Pengembangan pedoman anotasi **Universal Dependencies (UD)** untuk bahasa **Batak Toba** dan pengujian awal pada korpus kecil. Repositori ini adalah tahap kedua dari proyek jangka panjang pembangunan ekosistem NLP Batak Toba, salah satu bahasa daerah Indonesia yang berdaya rendah.

> Status: **work in progress** (Tahun 1, Semester 2). Semua pedoman dan anotasi masih draf dan wajib divalidasi penutur asli.
>
> Situs proyek: <https://nlptoba.org>

## Latar belakang

Batak Toba memiliki 1 juta+ penutur dan tata bahasa rujukan yang mapan (Nababan, 1981), tetapi belum memiliki treebank, anotasi kelas kata/dependensi, maupun pedoman anotasi. Ciri tipologis khasnya, yaitu **urutan predikat di awal** dan **sistem diatesis Austronesia** (prefiks maN- aktor, di- pasien), tidak otomatis terpetakan oleh kategori umum UD dan menuntut keputusan anotasi tambahan. Repositori ini menutup celah tersebut.

## Luaran proyek

1. Pedoman anotasi UD Batak Toba versi pertama.
2. Korpus kecil teranotasi 250 kalimat (format CoNLL-U) + skor kesepakatan antaranotator.
3. Artikel ilmiah (studi pedoman + validasi awal).

## Struktur repositori

```
guidelines/     Matriks keputusan anotasi + pedoman UD Batak Toba
corpus/pilot/   Contoh CoNLL-U dan rencana sampling awal (kalimat pilot yang dipakai ada di anotasi-ud/pilot/)
scripts/        Sampling, pembuat template CoNLL-U, penghitung IAA
evaluation/     Laporan kesepakatan antaranotator (IAA)
paper/          Kerangka & draf artikel
anotasi-ud/     Penelitian tahap 2: pedoman anotasi UD dan kalimat pilot
  pedoman/        Pedoman Anotasi UD Batak Toba v1.2 (v1.0 di arsip/)
  pilot/          250 kalimat pilot dan templat CoNLL-U
  korpus-revisi/  Korpus paralel hasil audit penyelarasan v1
```

## Penelitian tahap 2: anotasi Universal Dependencies (2026)

Penelitian lanjutan berjudul "Pengembangan Pedoman Anotasi Universal Dependencies untuk Bahasa Batak Toba dan Pengujian Awal pada Korpus Kecil" (Penelitian Dosen Pemula, Juli sampai Desember 2026) disimpan pada folder [anotasi-ud/](anotasi-ud/). Status per 7 November 2026:

| Luaran | Status |
|---|---|
| Pedoman anotasi UD Batak Toba | Versi 1.2 tersedia ([anotasi-ud/pedoman/](anotasi-ud/pedoman/)) |
| Korpus paralel hasil audit penyelarasan | Versi 1, 1.505 unit ([anotasi-ud/korpus-revisi/](anotasi-ud/korpus-revisi/)) |
| 250 kalimat pilot dalam format CoNLL-U | Anotasi ganda berjalan sejak 5 Oktober 2026 ([anotasi-ud/pilot/](anotasi-ud/pilot/)) |
| Skor kesepakatan antaranotator dan pedoman revisi | Dijadwalkan November 2026 |

## Stage 2 research: Universal Dependencies annotation (2026)

The follow-up project "Development of Universal Dependencies Annotation Guidelines for Batak Toba and Initial Testing on a Small Corpus" (Beginning Lecturer Research Scheme, July to December 2026) is kept in [anotasi-ud/](anotasi-ud/). Status as of 7 November 2026:

| Deliverable | Status |
|---|---|
| Batak Toba UD annotation guideline | Version 1.2 available ([anotasi-ud/pedoman/](anotasi-ud/pedoman/)), written in Indonesian |
| Parallel corpus after alignment audit | Version 1, 1,505 units ([anotasi-ud/korpus-revisi/](anotasi-ud/korpus-revisi/)) |
| 250 pilot sentences in CoNLL-U format | Double annotation in progress since 5 October 2026 ([anotasi-ud/pilot/](anotasi-ud/pilot/)) |
| Inter-annotator agreement and revised guideline | Scheduled for November 2026 |

## Alur kerja

1. **Pemilihan 250 kalimat pilot** (selesai). Kalimat dipilih dari korpus revisi penyelarasan v1 secara berstrata genre. Kriteria dan sebarannya ada di [anotasi-ud/pilot/README.md](anotasi-ud/pilot/README.md).
2. **Templat CoNLL-U** (selesai): [anotasi-ud/pilot/btk_pilot_250_template.conllu](anotasi-ud/pilot/btk_pilot_250_template.conllu).
3. **Anotasi ganda** oleh dua anotator secara terpisah, mengikuti [pedoman v1.2](anotasi-ud/pedoman/pedoman-anotasi-ud-v1.2.md) dan [kartu anotator](guidelines/03_panduan_ringkas_anotator.md) (berjalan).
4. **Validasi format** setiap berkas hasil anotasi:
   ```bash
   make validate
   ```
5. **Hitung IAA** dan susun lembar rekonsiliasi untuk adjudikasi:
   ```bash
   make iaa A=anotator_A.conllu B=anotator_B.conllu
   make reconcile A=anotator_A.conllu B=anotator_B.conllu
   ```
6. **Revisi pedoman** menjadi versi 2.0 berdasarkan temuan, lalu susun artikel.

Skrip `sample_250.py` dan `make_conllu_template.py` (target `make sample` dan `make template`) tetap tersedia untuk pemilihan kalimat berikutnya dari berkas CSV lain.

Semua skrip hanya memerlukan pustaka standar Python 3 (tanpa dependensi eksternal).

## Format anotasi

CoNLL-U, 10 kolom (`ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC`), mengikuti UD v2. Kolom XPOS dikosongkan (`_`) karena belum ada tagset khusus Batak Toba. Keputusan inti (diatesis, urutan predikat awal, partikel do/ma) dijelaskan di [pedoman v1.2](anotasi-ud/pedoman/pedoman-anotasi-ud-v1.2.md), dengan dasar keputusan diatesis di [guidelines/04_keputusan_diatesis.md](guidelines/04_keputusan_diatesis.md).

## Cara berkontribusi

Lihat `CONTRIBUTING.md`. Masukan penutur asli Batak Toba sangat diharapkan, terutama untuk isu terbuka yang tercatat di akhir dokumen pedoman.

## Sitasi

Lihat `CITATION.cff`. Bila memakai sumber daya ini, mohon sitasi repositori dan artikel terkait (bila sudah terbit).

## Lisensi

- Kode (folder `scripts/`): MIT (lihat `LICENSE`).
- Data & pedoman (`corpus/`, `guidelines/`, `anotasi-ud/`): CC BY-SA 4.0 (lihat `LICENSE-data`).

## Penghargaan

Penelitian ini didanai hibah internal 2026. Merupakan kelanjutan dari korpus mentah Batak Toba hibah 2025 (No. P-020-PDP-FTI/VII/2025).
