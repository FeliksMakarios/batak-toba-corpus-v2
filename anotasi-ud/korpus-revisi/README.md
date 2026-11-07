# Korpus Paralel Hasil Audit Penyelarasan v1

> **Status: sudah digantikan sebagai korpus paralel, tetap disimpan sebagai sumber kalimat pilot.**
> Korpus paralel final berisi 1.542 pasangan (182 divalidasi manusia) beserta laporan kesepakatan antaranotator kini ada di repositori tahap 1, yaitu [`batak-toba-korpus/data/btb_parallel_sentence.csv`](https://github.com/FeliksMakarios/batak-toba-korpus/blob/main/data/btb_parallel_sentence.csv). Berkas v1 di folder ini tidak diperbarui lagi. Berkas ini tetap disimpan karena 250 kalimat pilot di [`../pilot/`](../pilot/) dipilih darinya, sehingga `pair_id` kalimat pilot merujuk ke berkas ini.
>
> **Status: superseded as a parallel corpus, kept as the source of the pilot sentences.** The final parallel corpus (1,542 pairs, 182 human-validated) and its inter-annotator agreement report are in the Stage 1 repository at [`batak-toba-korpus/data/btb_parallel_sentence.csv`](https://github.com/FeliksMakarios/batak-toba-korpus/blob/main/data/btb_parallel_sentence.csv). The v1 file here is no longer updated. It is kept because the 250 pilot sentences in [`../pilot/`](../pilot/) were drawn from it.

Berkas `korpus_utama_revisi_penyelarasan_v1.csv` adalah korpus paralel Batak Toba dan Indonesia setelah audit penyelarasan pada 7 September 2026. Audit dilakukan sebelum pemilihan kalimat untuk anotasi UD.

## Ringkasan audit

| Ukuran | Nilai |
|---|---:|
| Baris asal | 1.494 |
| Baris hasil | 1.505 |
| Label lama dikoreksi tanpa mengubah teks | 122 |
| Baris asal dipecah | 10 (menjadi 21 unit, 2 tetap `unresolved`) |
| Unit berstatus `needs_review` (prioritas tinggi) | 89 |
| Unit prioritas menengah | 56 |
| Unit berstatus `candidate_1_1` | 1.275 |
| Unit berstatus `structural_1_1_reviewed` | 141 |

## Prinsip

1. Tidak ada kata atau tanda baca yang dibuang, ditambahkan, atau diterjemahkan ulang. Pemecahan hanya mengambil rentang karakter asli (kolom `toba_char_start` sampai `indo_char_end`).
2. Seluruh 1.494 ID asal terwakili dan dapat ditelusuri lewat `original_pair_id` dan `original_row_number`.
3. Kasus tanpa padanan lengkap dipertahankan dengan label `unresolved`.
4. Seluruh baris berstatus `translation_validation = pending_human`. Status `structural_1_1_reviewed` hanya menilai batas dan label penyelarasan, belum mengesahkan makna terjemahan.

## Kolom utama

`pair_id`, `doc_id`, `genre`, `sub_genre`, `method`, `alignment_type`, `toba_final`, `indo_final`, `source`, `original_pair_id`, `original_row_number`, `original_alignment_type`, `segment_index`, `alignment_status`, `revision_type`, `unit_type`, `boundary_confidence`, `translation_validation`, `review_priority`, `review_note`, serta rentang karakter `toba_char_start`, `toba_char_end`, `indo_char_start`, `indo_char_end`.

SHA-256: `b67e0841c874c7226f31f40db9873fb2812b09422caac973838a8abebccf3b08`
