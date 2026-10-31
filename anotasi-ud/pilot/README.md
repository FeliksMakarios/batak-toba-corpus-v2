# Kalimat Pilot Anotasi UD (250 kalimat)

Kalimat dipilih dari `../korpus-revisi/korpus_utama_revisi_penyelarasan_v1.csv` (1.505 unit) untuk anotasi ganda oleh dua anotator penutur Batak Toba.

## Kriteria pemilihan

1. Hanya unit berpenyelarasan 1-1 dengan status `candidate_1_1` atau `structural_1_1_reviewed` dan prioritas pemeriksaan `routine`. Unit `needs_review`, `unresolved`, judul, fragmen, dan lanjutan kutipan tidak dipakai.
2. Satu kalimat utuh per unit, 5 sampai 20 kata (puisi dan umpasa 5 sampai 16 kata), dengan rasio panjang terjemahan 0,5 sampai 2,0.
3. Tidak memuat URL, angka panjang, persen, nominal uang, tanda kurung, titik dua, titik koma, atau butir daftar.
4. Berstrata menurut genre dan subgenre, dengan batas jumlah kalimat per dokumen.
5. Diprioritaskan kalimat yang memuat konstruksi inti pedoman: verba *di-/hu-/ta-*, verba *ma-/mang-/mar-*, partikel *do/ma*, negasi, penanda *na*, koordinasi, subordinasi, dan verba bantu.
6. Empat belas kandidat dikeluarkan setelah pembacaan manual karena terjemahan tidak sepadan, fragmen tanpa predikat, bahasa gaul, atau angka.

Setelah penyaringan tersisa 679 unit, lalu dipilih 250 kalimat.

## Sebaran

| Genre | Subgenre | Kalimat | Dokumen |
|---|---|---:|---:|
| Contemporary Media | Blog Articles | 45 | 7 |
| Contemporary Media | News Article | 29 | 6 |
| Contemporary Media | Wiki | 35 | 8 |
| Educational | Book Summary | 45 | 6 |
| Educational | News Article | 12 | 4 |
| Educational | Quotes | 6 | 1 |
| Historical/Traditional | Folktales | 50 | 2 |
| Literary | Peribahasa/Umpama | 6 | 6 |
| Literary | Poems | 10 | 4 |
| Religious | Prayers | 12 | 3 |
| **Total** | | **250** | **47** |

Rata-rata panjang 12,5 kata. Kalimat cerita rakyat hanya berasal dari dua dokumen karena korpus memuat sedikit dokumen genre itu.

## Berkas

1. `daftar-250-kalimat-pilot.csv`: kolom `pilot_id`, `batch`, `pair_id`, `doc_id`, `genre`, `sub_genre`, `kalimat_toba`, `terjemahan_indonesia`, `jumlah_kata`, `jumlah_token`, `indikasi_konstruksi`, `alasan_pemilihan`. Kolom `indikasi_konstruksi` dihitung otomatis dari pola huruf dan dapat keliru.
2. `btk_pilot_250_template.conllu`: 250 kalimat yang sudah ditokenisasi. Kolom ID, FORM, dan `SpaceAfter=No` terisi, kolom lain diisi anotator mengikuti pedoman. Setiap kalimat memuat komentar `sent_id`, `batch`, `source_pair_id`, `genre`, `text`, dan `text_id` (terjemahan Indonesia).
3. Urutan kalimat sudah diacak berstrata dan dibagi lima batch @50 kalimat.
