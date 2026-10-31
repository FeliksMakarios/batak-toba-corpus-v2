# Pelacak Progres Penelitian

Judul: Pengembangan Pedoman Anotasi UD untuk Bahasa Batak Toba dan Pengujian Awal pada Korpus Kecil
Durasi: 6 bulan (Juli-Desember 2026) | Target TKT: 2 -> 3

## Status tahap
- [x] Tahap 1: Sintesis keputusan anotasi (matriks) — draf ada di `guidelines/01`, masih perlu validasi ahli bahasa
- [x] Tahap 2: Pedoman versi awal — v1.0 selesai di `anotasi-ud/pedoman/` (berlaku mulai 5 Oktober 2026), draf v0.2 di `guidelines/02` menjadi arsip
- [ ] Tahap 3: Anotasi rintisan 250 kalimat — 250 kalimat dan templat CoNLL-U siap di `anotasi-ud/pilot/` (dipilih dari korpus revisi v1, `anotasi-ud/korpus-revisi/`), anotasi ganda mulai 5 Oktober 2026
- [ ] Tahap 4: Evaluasi IAA + revisi pedoman

## Luaran
- [ ] Artikel ilmiah (SINTA 2-4 / prosiding internasional) — kerangka `paper/outline.md`, draf pendahuluan+metode `paper/01`
- [x] Pedoman UD Batak Toba v1.0 (`anotasi-ud/pedoman/`), revisi v1.1 setelah evaluasi IAA
- [ ] Korpus 250 kalimat CoNLL-U + skor IAA
- [x] Repositori terbuka (repo ini)

## Milestone bulanan
| Bulan | Target | Status |
|-------|--------|--------|
| 1 (Jul) | Sintesis literatur + matriks keputusan | draf selesai |
| 2 (Agu) | Pedoman v1 + seleksi 250 kalimat | selesai: audit penyelarasan 7 Sep, pedoman v1.0 dan seleksi 250 kalimat 1 Okt |
| 3 (Sep) | Konsultasi ahli + pelatihan anotator | belum |
| 4 (Okt) | Anotasi rintisan (paruh 1) | mulai 5 Okt 2026 |
| 5 (Nov) | Anotasi selesai + hitung IAA | belum |
| 6 (Des) | Revisi pedoman + artikel + laporan akhir | belum |

## Isu terbuka menunggu narasumber (4 sesi)
1. Pemetaan actor pada di-: obl:agent vs subtipe spesifik bahasa.
2. Status naeng/boi: AUX vs VERB.
3. Nilai Voice untuk mar- dan tar-.
4. Status na (relativizer): PRON vs SCONJ.
5. Penanda takrif i/on: fitur Definite atau cukup det.
6. UPOS negator ndang/dang.

## Log kegiatan
| Tanggal | Kegiatan | Catatan |
|---------|----------|---------|
| 2026-07-03 | Inisialisasi repo; draf matriks keputusan, pedoman v1, kartu anotator, skrip, dokumentasi | oleh Feliks |
| 2026-08-20 | Tinjauan repo (Claude): validasi skrip lolos, docs/SETUP_CI.md disinkronkan dengan status CI aktif, hapus docs/github_actions_validate.yml.txt (duplikat) | belum ada progres Tahap 3 sejak 3 Juli |
| 2026-10-02 | Tambah `anotasi-ud/`: pedoman UD v1.0 (.md dan .docx), 250 kalimat pilot berstrata genre dan templat CoNLL-U, korpus revisi penyelarasan v1 (1.505 unit) | anotasi ganda mulai 5 Oktober 2026 |
