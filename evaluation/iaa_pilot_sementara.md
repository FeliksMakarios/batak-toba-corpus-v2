# Kesepakatan Antaranotator Pilot 250 Kalimat (Sementara)

Laporan per 26 November 2026. Angka di sini **sementara** karena salah satu anotator belum menyelesaikan seluruh kalimat. Kesepakatan akan dihitung ulang pada 250 kalimat setelah anotasi lengkap, lalu diikuti adjudikasi dan revisi pedoman menjadi versi 2.0.

Berkas CoNLL-U per anotator tidak diterbitkan sebelum adjudikasi. Yang dirilis setelah adjudikasi adalah korpus hasil adjudikasi.

## Pelaksanaan

- Pedoman yang dipakai: [pedoman v1.2](../anotasi-ud/pedoman/pedoman-anotasi-ud-v1.2.md).
- 250 kalimat (3.519 token) dari lima genre, dibagi menjadi lima batch @50 kalimat ([daftar kalimat](../anotasi-ud/pilot/daftar-250-kalimat-pilot.csv)).
- Anotasi ganda dimulai 5 Oktober 2026, dan hasilnya diserahkan pada 21 November 2026. Hasil kedua anotator diperiksa oleh narasumber penutur asli Bahasa Batak Toba pada 24 November 2026.
- Kalimat lengkap: Anotator A 95 kalimat (38,0%), Anotator B 241 kalimat (96,4%).

| Batch | Kalimat | Lengkap, Anotator A | Lengkap, Anotator B |
|---|---|---:|---:|
| 1 | 001 sampai 050 | 36 | 47 |
| 2 | 051 sampai 100 | 0 | 49 |
| 3 | 101 sampai 150 | 0 | 48 |
| 4 | 151 sampai 200 | 9 | 49 |
| 5 | 201 sampai 250 | 50 | 48 |

## Kesepakatan pada 90 kalimat yang lengkap pada kedua anotator

Dihitung dengan `scripts/compute_iaa.py` pada 90 kalimat (1.247 token).

| Ukuran | Nilai |
|---|---:|
| Kesepakatan UPOS | 87,8% |
| Kappa Cohen UPOS | 0,864 |
| Kesepakatan DEPREL | 76,3% |
| Kappa Cohen DEPREL | 0,749 |
| UAS (HEAD sama) | 84,0% |
| LAS (HEAD dan DEPREL sama) | 68,5% |

Sebagai patokan, Bagian 10.3 pedoman merujuk treebank Tagalog UD-NewsCrawl dengan kappa 0,75 untuk kelas kata dan 0,68 untuk relasi dependensi (Aquino dkk., 2025). Kedua nilai kappa di atas sudah melampaui patokan itu, dengan catatan sampelnya baru 90 kalimat.

### Per genre

| Genre | Kalimat | Token | UPOS | UAS | LAS |
|---|---:|---:|---:|---:|---:|
| Media kontemporer | 40 | 550 | 87,8% | 83,8% | 68,7% |
| Pendidikan | 21 | 315 | 85,4% | 82,9% | 70,2% |
| Sejarah dan tradisi | 18 | 261 | 89,3% | 87,0% | 66,7% |
| Keagamaan | 5 | 70 | 87,1% | 84,3% | 71,4% |
| Sastra | 6 | 51 | 96,1% | 76,5% | 60,8% |
| **Total** | **90** | **1.247** | **87,8%** | **84,0%** | **68,5%** |

Genre sastra hanya diwakili 51 token sehingga angkanya belum stabil.

### Per relasi

Kesepakatan label DEPREL pada token yang diberi relasi tersebut oleh salah satu atau kedua anotator (20 relasi terbanyak).

| Relasi | Token | Kesepakatan | | Relasi | Token | Kesepakatan |
|---|---:|---:|---|---|---:|---:|
| advmod | 148 | 56,1% | | det | 59 | 84,7% |
| punct | 147 | 98,6% | | obj | 53 | 60,4% |
| nsubj | 119 | 57,1% | | cc | 53 | 92,5% |
| case | 112 | 86,6% | | conj | 53 | 79,2% |
| root | 104 | 75,0% | | advcl | 51 | 54,9% |
| mark | 92 | 83,7% | | acl:relcl | 38 | 50,0% |
| nmod | 83 | 54,2% | | aux | 30 | 60,0% |
| discourse | 80 | 12,5% | | advmod:emph | 26 | 0,0% |
| obl | 73 | 68,5% | | nsubj:pass | 25 | 0,0% |
| | | | | nmod:poss | 24 | 29,2% |

## Konstruksi yang paling sering tidak disepakati

Selisih 15,5 poin antara UAS dan LAS menunjukkan bahwa kedua anotator umumnya sepakat tentang kata induk tetapi berbeda label relasi. Delapan pasangan berikut mencakup 138 dari 295 token yang berbeda DEPREL.

| Pasangan relasi | Token | Ketentuan pedoman v1.2 |
|---|---:|---|
| advmod dan discourse | 41 | *do*, *ma*, *pe* diberi `PART` dengan `discourse` |
| advmod:emph dan discourse | 25 | `advmod:emph` tidak dipakai |
| nsubj dan nsubj:pass | 21 | pivot verba pasif diberi `nsubj`, `nsubj:pass` tidak dipakai |
| nmod dan nmod:poss | 15 | `nmod:poss` untuk pemilik bertanda *ni*, perlu adjudikasi |
| flat dan flat:name | 12 | `flat:name` tidak dipakai, nama majemuk diberi `flat` |
| nsubj dan obj | 9 | beda analisis argumen, perlu adjudikasi |
| acl dan acl:relcl | 8 | `acl` tidak dipakai, klausa relatif *na* diberi `acl:relcl` |
| nmod dan obl | 7 | beda analisis keterangan, perlu adjudikasi |

Pada UPOS, perbedaan terbesar adalah `PART` dengan `SCONJ` (31 token) dan `PART` dengan `PRON` (18 token), hampir seluruhnya pada penanda *na*.

Empat dari delapan pasangan di atas melibatkan label yang tidak ada di Lampiran A pedoman, dan satu lagi menyangkut aturan partikel *do*, *ma*, *pe*. Pola ini muncul secara sistematis pada salah satu anotator, yang cenderung mengikuti konvensi UD umum, misalnya memperlakukan verba *di-* sebagai pasif dengan `nsubj:pass`. Jika empat penyimpangan mekanis diselaraskan dengan pedoman (*do*, *ma*, *pe* menjadi `discourse`, `nsubj:pass` menjadi `nsubj`, `flat:name` menjadi `flat`, dan `acl` menjadi `acl:relcl`), LAS naik dari 68,5% menjadi 74,7%. Sebagian besar ketidaksepakatan tampaknya bisa diselesaikan lewat kalibrasi dan adjudikasi, dan tidak berasal dari konstruksi yang ambigu.

## Temuan pada lembar kerja anotasi

Daftar pilihan DEPREL pada lembar kerja Excel memuat 45 label UD umum, termasuk `nsubj:pass`, `advmod:emph`, `flat:name`, `acl`, `obl:tmod`, dan `cop` yang tidak ada di Lampiran A, tetapi tidak memuat `obj:agent`. Akibatnya `obj:agent` sama sekali tidak dipakai oleh kedua anotator. Daftar pilihan ini perlu diselaraskan dengan Lampiran A sebelum putaran anotasi berikutnya.

## Langkah berikutnya

1. Menyelesaikan 155 kalimat Anotator A dan memperbaiki galat format, lalu menghitung ulang kesepakatan pada 250 kalimat.
2. Menyelaraskan daftar pilihan DEPREL pada lembar kerja dan mengkalibrasi ulang anotator.
3. Adjudikasi bersama narasumber penutur asli, lalu revisi pedoman menjadi versi 2.0.
4. Rilis korpus 250 kalimat CoNLL-U hasil adjudikasi pada `anotasi-ud/`.

## Rujukan

Aquino, A., Miranda, L. J., & Or, E. (2025). The UD-NewsCrawl Treebank: Reflections and Challenges from a Large-scale Tagalog Syntactic Annotation Project. arXiv:2505.20428.
