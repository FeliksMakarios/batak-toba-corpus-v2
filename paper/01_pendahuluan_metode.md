# Draf: Pendahuluan dan Metode

Draf awal untuk diisi dengan hasil setelah anotasi. Bagian ini mengikuti kerangka di `outline.md`. Rujukan dalam kurung siku merujuk daftar pustaka proposal.

## 1. Pendahuluan

Bahasa Batak Toba dituturkan oleh lebih dari satu juta orang di Sumatra Utara dan memiliki deskripsi tata bahasa rujukan yang mapan [1]. Meski demikian, sumber daya komputasi untuk bahasa ini masih sangat terbatas. Upaya terkini pada bahasa daerah Indonesia, seperti korpus paralel dan tolok ukur multitugas, umumnya berhenti pada teks mentah atau anotasi tingkat kalimat, dan belum menyediakan anotasi morfosintaksis. Sampai saat ini Batak Toba belum memiliki treebank, tag kelas kata dan dependensi, maupun pedoman anotasi yang dirancang khusus.

Kerangka Universal Dependencies (UD) menyediakan skema anotasi lintas bahasa yang konsisten [2][3], tetapi penerapannya pada Batak Toba tidak langsung. Dua ciri tipologis menuntut keputusan tambahan. Pertama, urutan predikat di awal kalimat, sehingga subjek gramatikal muncul setelah predikat [15][16]. Kedua, sistem diatesis Austronesia dengan pemarkahan morfologis pada verba (prefiks maN- untuk diatesis aktor dan di- untuk diatesis pasien), yang tidak otomatis terpetakan ke relasi inti UD. Tantangan serupa telah ditangani untuk bahasa Filipina seperti Tagalog dan Cebuano [10][11], tetapi belum untuk bahasa Austronesia di Sumatra.

Penelitian ini menyusun pedoman anotasi UD pertama untuk Batak Toba dan mengujinya pada korpus kecil. Kontribusi kami ada tiga: (1) pedoman anotasi UD Batak Toba yang terbuka, dengan keputusan eksplisit untuk diatesis dan urutan predikat awal; (2) korpus rintisan 250 kalimat teranotasi dalam format CoNLL-U; dan (3) evaluasi empiris kualitas pedoman melalui skor kesepakatan antaranotator beserta analisis konstruksi yang paling sulit dianotasi.

## 2. Metode

Penelitian dijalankan dalam empat tahap.

**Tahap 1: Sintesis keputusan anotasi.** Kami menelaah pedoman UD resmi [2][3], adaptasi UD Bahasa Indonesia [7][8][9], adaptasi diatesis Austronesia pada UD Tagalog dan Cebuano [10][11], serta deskripsi tata bahasa Batak Toba [1][15][16]. Hasilnya adalah matriks keputusan yang memetakan 17 tag UPOS, fitur morfologis relevan, dan relasi dependensi ke fenomena Batak Toba, dengan penekanan pada pemarkahan argumen diatesis dan urutan predikat awal.

**Tahap 2: Perumusan pedoman versi awal.** Berdasarkan matriks tersebut kami menyusun pedoman anotasi versi pertama, dilengkapi contoh kalimat berlabel dalam format CoNLL-U. Keputusan inti mencakup pemetaan diatesis secara simetris (Opsi C): pivot diberi nsubj pada kedua diatesis, sehingga pada diatesis aktor (Voice=Act) aktor menjadi nsubj dan pasien menjadi obj, sedangkan pada diatesis pasien (Voice=Pass) pasien menjadi nsubj dan aktor tak bertanda menjadi obj:agent karena tetap berstatus argumen inti. Aktor bertanda ni pada verba kompletif dan promisif diberi obl:agent. Relasi nsubj:pass tidak dipakai. Keputusan lain mencakup penanganan subjek pasca-predikat sebagai nsubj, predikat non-verbal tanpa kopula, serta anotasi partikel do dan ma sebagai PART dengan relasi discourse.

**Tahap 3: Anotasi rintisan.** Kami memilih 250 kalimat secara berlapis lintas genre (tradisional, modern, lisan) dari korpus mentah tahap sebelumnya, dengan kendali panjang kalimat dan kuota konstruksi agar variasi diatesis terwakili. Dua anotator terlatih menganotasi seluruh kalimat secara paralel (anotasi ganda) mengikuti pedoman, dengan prapemrosesan otomatis untuk meringankan beban awal.

**Tahap 4: Evaluasi dan revisi.** Kami mengukur kesepakatan antaranotator pada tiga tingkat: kesepakatan UPOS beserta Cohen's kappa, kesepakatan HEAD (setara UAS), dan kesepakatan HEAD+DEPREL (setara LAS). Konstruksi dengan tingkat ketidaksepakatan tertinggi dianalisis secara kualitatif, dan temuan tersebut menjadi dasar revisi pedoman menjadi versi final.

_(Bagian Hasil, Diskusi, dan Kesimpulan diisi setelah anotasi selesai.)_
