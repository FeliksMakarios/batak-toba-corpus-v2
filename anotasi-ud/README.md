# Anotasi Universal Dependencies Batak Toba (Tahap 2)

Folder ini memuat luaran penelitian tahap 2, *Pengembangan Pedoman Anotasi Universal Dependencies untuk Bahasa Batak Toba dan Pengujian Awal pada Korpus Kecil* (Penelitian Dosen Pemula, Universitas Pelita Harapan, Juli sampai Desember 2026). Tahap ini melanjutkan korpus paralel tahap 1 pada repositori [batak-toba-korpus](https://github.com/FeliksMakarios/batak-toba-korpus) menuju anotasi morfosintaksis berbasis Universal Dependencies (UD) versi 2.

This folder contains the outputs of the second research stage: a first Universal Dependencies v2 annotation guideline for Batak Toba and a 250-sentence pilot set for double annotation.

## Isi folder

```
anotasi-ud/
├── README.md
├── pedoman/
│   ├── pedoman-anotasi-ud-v1.2.md              Pedoman v1.2 (terbaca langsung di GitHub)
│   ├── Pedoman_Anotasi_UD_BatakToba_v1.2.docx  Pedoman v1.2 (Word)
│   └── arsip/                                  Versi sebelumnya (v1.0)
├── pilot/
│   ├── README.md                               Kriteria pemilihan dan sebaran kalimat
│   ├── daftar-250-kalimat-pilot.csv            250 kalimat pilot beserta terjemahan
│   └── btk_pilot_250_template.conllu           Templat CoNLL-U yang sudah ditokenisasi
└── korpus-revisi/
    ├── README.md                               Ringkasan audit penyelarasan v1
    └── korpus_utama_revisi_penyelarasan_v1.csv Korpus paralel hasil audit (1.505 unit), sumber kalimat pilot, sudah digantikan oleh korpus final di batak-toba-korpus
```

## Status per 28 Oktober 2026

| Tahap metode | Status |
|---|---|
| 1. Sintesis keputusan anotasi dari literatur | Selesai |
| 2. Perumusan pedoman versi awal | Selesai, versi 1.0 (5 Oktober 2026), diperbarui menjadi versi 1.2 (28 Oktober 2026) berdasarkan masukan anotator |
| 3. Anotasi rintisan 250 kalimat oleh dua anotator | Berjalan sejak 5 Oktober 2026 |
| 4. Evaluasi kesepakatan antaranotator dan revisi pedoman | Dijadwalkan November 2026 |

## Keputusan utama pedoman v1.2

Kelas kata dan konstruksi mengikuti *A Grammar of Toba-Batak* (Nababan, 1981).

1. Akar kalimat adalah predikator. Kalimat tanpa verba tetap tanpa kopula.
2. Verba berprefiks *di-*, *hu-*, *ta-* dan bentuk pasif lain diberi `Voice=Pass`.
3. Subjek klausa, termasuk subjek klausa pasif, diberi `nsubj`.
4. Aktor yang langsung mengikuti verba pasif (konstituen agentif menurut Nababan) diberi `obj:agent`. Aktor bertanda *ni* diberi `obl:agent`.
5. Partikel predikatif *do*, *ma*, *pe* diberi `PART` dengan relasi `discourse`.
6. Penanda atributif *na* diberi `PART` dengan relasi `mark`.
7. Sufiks pronominal (*-na*, *-mu*, *-hu/-ku*, dan lainnya) tidak dipisah dan dicatat dengan `Person[psor]` serta `Number[psor]`.
8. Kalimat majemuk setara dan kalimat kompleks tetap punya satu root. Isi setiap klausa menunjuk ke predikator klausanya sendiri (sejak versi 1.1).
9. *laos* selalu diberi `ADV` dengan relasi `advmod` ke predikator klausanya (sejak versi 1.1).

Versi 1.2 menambahkan daftar istilah bernomor I-01 sampai I-117, jembatan S-P-O-Pel-K ke label UD, dan indeks istilah, tanpa mengubah aturan label.

Isu yang masih terbuka dicatat pada Bagian 11 pedoman dan akan ditinjau setelah pengukuran kesepakatan.

## Rencana berikutnya

1. Anotasi ganda 250 kalimat dalam lima batch (Oktober sampai pertengahan November 2026).
2. Pengukuran kesepakatan antaranotator untuk UPOS, kappa Cohen, UAS, dan LAS, lalu adjudikasi.
3. Pedoman versi 2.0 dan rilis korpus kecil teranotasi dalam format CoNLL-U pada folder ini.

## Lisensi

Pedoman dan data pada folder ini berlisensi CC BY-SA 4.0, mengikuti berkas [LICENSE-data](../LICENSE-data).
