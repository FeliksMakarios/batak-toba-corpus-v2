# Evaluasi

Folder ini menampung laporan kesepakatan antaranotator (IAA) yang dihasilkan
`scripts/compute_iaa.py`, beserta analisis konstruksi yang paling sering tidak
disepakati. Laporan menjadi dasar revisi pedoman (Tahap 4) dan bahan bagian
Hasil pada artikel.

Contoh menjalankan:

    python ../scripts/compute_iaa.py --a anotator1.conllu --b anotator2.conllu \
        --report iaa_report.md

Laporan yang tersedia:

- [iaa_pilot_sementara.md](iaa_pilot_sementara.md): kesepakatan sementara pilot 250 kalimat pada 90 kalimat yang lengkap pada kedua anotator (26 November 2026).
