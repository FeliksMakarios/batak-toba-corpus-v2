# Template Pemilihan 250 Kalimat Berlapis Lintas Genre (Tahap 3)

> **Catatan.** Dokumen ini rencana awal (Juli 2026). Pemilihan 250 kalimat yang benar-benar dipakai memakai korpus revisi penyelarasan v1 dan lima genre korpus tahap 1. Kriteria dan sebarannya ada di [anotasi-ud/pilot/README.md](../../anotasi-ud/pilot/README.md).

Tujuan: memilih ~250 kalimat dari korpus mentah hibah 2025 secara berlapis (stratified) lintas genre agar variasi konstruksi terwakili, terutama diatesis dan predikat awal.

## 1. Strata genre (target proporsi)
Korpus tahap 1 berasal dari sumber tradisional, modern, dan lisan. Usulan pembagian 250 kalimat:

| Strata | Sumber | Target kalimat | Alasan |
|--------|--------|----------------|--------|
| Tradisional | umpama, turi-turian, teks adat | 85 | Kaya konstruksi diatesis & bentuk klasik |
| Modern | berita, artikel, media sosial | 85 | Struktur kontemporer, kata pinjaman |
| Lisan | transkrip percakapan/tutur | 80 | Partikel wacana (do/ma), imperatif, ellipsis |
| Total | | 250 | |

## 2. Kriteria seleksi (per kalimat)
- Panjang 4-25 token (hindari fragmen & kalimat sangat panjang pada tahap awal).
- Ada predikat jelas (verba/adjektiva/nomina).
- Utamakan variasi diatesis: pastikan ada contoh maN- (aktor) dan di- (pasien) dalam jumlah cukup.
- Sertakan kalimat dengan: partikel do/ma, demonstratif i/on, preposisi di/tu/sian, negasi ndang/dang, numeralia.
- Hindari duplikat & kalimat hampir identik.
- Buang kalimat campur kode berat (mayoritas Bahasa Indonesia/Inggris).

## 3. Kuota konstruksi minimum (lintas seluruh 250)
| Konstruksi | Target minimum |
|------------|----------------|
| Diatesis aktor (maN-) | 60 |
| Diatesis pasien (di-) | 50 |
| Predikat non-verbal (ADJ/NOUN) | 40 |
| Klausa dengan preposisi (obl) | 40 |
| Negasi | 20 |
| Kalimat dengan partikel do/ma | 120 |

## 4. Format daftar seleksi (CSV)
Kolom: sent_id, strata, sumber, teks_batak, teks_ind, panjang_token, konstruksi_target, catatan.
Contoh baris:
btk_pilot-001,tradisional,turi-turian,"Mangallang dengke do si Polan.","Si Polan makan ikan.",6,diatesis_aktor,-

## 5. Alur kerja
1. Ekstrak kalimat kandidat dari korpus mentah (segmentasi kalimat + hitung token).
2. Tandai otomatis kandidat per strata dan per konstruksi (regex prefiks maN-/di-, partikel).
3. Sampling acak berlapis hingga kuota strata & konstruksi terpenuhi.
4. Review manual, buang yang tidak layak, ganti dari cadangan.
5. Kunci daftar final 250 -> jadi input format CoNLL-U kosong untuk anotator.

## 6. Reproduktibilitas
- Simpan seed acak.
- Simpan skrip sampling + daftar kandidat penuh.
- Versikan daftar final (250_final_v1.csv) di repositori terbuka.
