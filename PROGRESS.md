# Pelacak Progres Penelitian

Judul: Pengembangan Pedoman Anotasi UD untuk Bahasa Batak Toba dan Pengujian Awal pada Korpus Kecil
Durasi: 6 bulan (Juli-Desember 2026) | Target TKT: 2 -> 3

## Status tahap
- [x] Tahap 1: Sintesis keputusan anotasi (matriks) — draf ada di `guidelines/01`, masih perlu validasi ahli bahasa
- [x] Tahap 2: Pedoman versi awal — v1.0 (5 Oktober 2026), kini v1.2 (28 Oktober 2026) di `anotasi-ud/pedoman/`, v1.0 di `anotasi-ud/pedoman/arsip/`, draf v0.2 di `guidelines/02` menjadi arsip
- [ ] Tahap 3: Anotasi rintisan 250 kalimat — 250 kalimat dan templat CoNLL-U siap di `anotasi-ud/pilot/` (dipilih dari korpus revisi v1, `anotasi-ud/korpus-revisi/`), anotasi ganda mulai 5 Oktober 2026
- [ ] Tahap 4: Evaluasi IAA + revisi pedoman

## Luaran
- [ ] Artikel ilmiah (SINTA 2-4 / prosiding internasional) — kerangka `paper/outline.md`, draf pendahuluan+metode `paper/01`
- [x] Pedoman UD Batak Toba v1.2 (`anotasi-ud/pedoman/`), revisi v2.0 setelah evaluasi IAA
- [ ] Korpus 250 kalimat CoNLL-U + skor IAA
- [x] Repositori terbuka (repo ini)

## Milestone bulanan
| Bulan | Target | Status |
|-------|--------|--------|
| 1 (Jul) | Sintesis literatur + matriks keputusan | draf selesai |
| 2 (Agu) | Pedoman v1 + seleksi 250 kalimat | selesai: audit penyelarasan 7 Sep, pedoman v1.0 dan seleksi 250 kalimat 1 Okt |
| 3 (Sep) | Konsultasi ahli + pelatihan anotator | selesai: konsultasi ahli secara informal, pelatihan anotator sebelum anotasi dimulai |
| 4 (Okt) | Anotasi rintisan (paruh 1) | mulai 5 Okt 2026 |
| 5 (Nov) | Anotasi selesai + hitung IAA | belum |
| 6 (Des) | Revisi pedoman + artikel + laporan akhir | belum |

## Isu terbuka untuk pedoman v2.0

Mengikuti Bagian 11 [pedoman v1.2](anotasi-ud/pedoman/pedoman-anotasi-ud-v1.2.md), ditinjau setelah pengukuran kesepakatan.

1. Adjektiva atau adverbia di posisi predikator sebelum verba.
2. Status *gabe*, *boi*, dan *naeng*: AUX atau VERB dengan xcomp.
3. Fitur untuk aktor yang tersandi pada verba (*hu-*, *ta-*, sufiks promisif), saat ini dicatat di MISC.
4. Relasi untuk sasaran bertanda *di* setelah verba, saat ini obl.
5. Perlakuan *laho* sebagai penanda tujuan.
6. Representasi reduplikasi dan inkorporasi nomina semu.
7. Pendaftaran subtipe obj:agent ke daftar relasi Batak Toba di UD sebelum treebank dirilis.

Isu lama yang sudah diputuskan: aktor pada di- (Opsi C, `guidelines/04`), status *na* (PART dengan relasi mark), dan negator *dang/ndang* (PART dengan Polarity=Neg dan relasi advmod).

## Log kegiatan
| Tanggal | Kegiatan | Catatan |
|---------|----------|---------|
| 2026-07-03 | Inisialisasi repo; draf matriks keputusan, pedoman v1, kartu anotator, skrip, dokumentasi | oleh Feliks |
| 2026-08-20 | Tinjauan repo (Claude): validasi skrip lolos, docs/SETUP_CI.md disinkronkan dengan status CI aktif, hapus docs/github_actions_validate.yml.txt (duplikat) | belum ada progres Tahap 3 sejak 3 Juli |
| 2026-10-02 | Tambah `anotasi-ud/`: pedoman UD v1.0 (.md dan .docx), 250 kalimat pilot berstrata genre dan templat CoNLL-U, korpus revisi penyelarasan v1 (1.505 unit) | anotasi ganda mulai 5 Oktober 2026 |
| 2026-10-28 | Pedoman v1.2 berdasarkan masukan anotator: perluasan Bagian 6.7 (kalimat majemuk setara dan kompleks), aturan *laos*, Contoh 11, daftar istilah I-01 sampai I-117, indeks istilah | v1.0 dipindah ke `anotasi-ud/pedoman/arsip/` |
| 2026-11-07 | Selaraskan kartu anotator, draf artikel, daftar isu terbuka, README, dan CI dengan pedoman v1.2 | kartu lama melarang obl:agent, padahal v1.2 memakainya untuk aktor bertanda *ni* |
