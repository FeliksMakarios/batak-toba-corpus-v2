# Pedoman Anotasi Universal Dependencies v2 untuk Bahasa Batak Toba

Versi 1.0 untuk anotasi rintisan 250 kalimat. Berlaku mulai 5 Oktober 2026.

Penelitian Dosen Pemula 2026, *Pengembangan Pedoman Anotasi Universal Dependencies untuk Bahasa Batak Toba dan Pengujian Awal pada Korpus Kecil*, Program Studi Informatika, Universitas Pelita Harapan.

Versi Word: [Pedoman_Anotasi_UD_BatakToba_v1.0.docx](Pedoman_Anotasi_UD_BatakToba_v1.0.docx)

| **Butir**        | **Keterangan**                                                                                                                          |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Dasar linguistik | P. W. J. Nababan (1981), A Grammar of Toba-Batak, Pacific Linguistics D-37. Nomor pasal (§) dalam pedoman ini merujuk ke buku tersebut. |
| Kerangka anotasi | Universal Dependencies versi 2 (universaldependencies.org), format CoNLL-U                                                              |
| Pemakai          | Anotator A dan Anotator B (penutur Batak Toba), ketua tim sebagai adjudikator                                                           |
| Status           | Versi 1.0. Direvisi menjadi versi 1.1 setelah evaluasi kesepakatan antaranotator                                                        |

## 1. Tujuan dan Prinsip Dasar

Pedoman ini menjelaskan cara memberi label kelas kata, fitur morfologis, dan relasi dependensi pada kalimat Batak Toba dalam format CoNLL-U. Pedoman dipakai untuk menganotasi 250 kalimat rintisan secara ganda oleh dua anotator. Hasilnya dipakai untuk mengukur seberapa konsisten pedoman ini dapat diterapkan, lalu pedoman direvisi.

Lima prinsip berikut berlaku untuk seluruh keputusan.

1.  **Struktur Batak Toba menjadi dasar label.** Terjemahan Indonesia hanya membantu memahami makna. Jangan memberi label karena kata Indonesianya berkelas kata tertentu. Contoh: *dibuat ibana* diterjemahkan "dia mengambil", tetapi verbanya tetap verba pasif menurut Nababan.

2.  **Kelas kata dan konstruksi mengikuti Nababan (1981).** Bila pedoman ini merujuk § tertentu, pembagian dan istilahnya berasal dari buku tersebut.

3.  **Label UD v2 dipakai apa adanya.** Pedoman ini hanya menentukan label UD mana yang dipakai untuk konstruksi Batak Toba. Nama label tidak diterjemahkan.

4.  **Teks tidak boleh diubah.** Kolom FORM dan baris \# text tidak diedit, termasuk bila ada salah ketik. Kesalahan dicatat di kolom MISC (lihat Bagian 4.4).

5.  **Kerja mandiri.** Anotator A dan B tidak berdiskusi tentang kalimat yang sedang dianotasi. Pertanyaan diajukan ke ketua tim (Bagian 10). Perbedaan antaranotator justru yang ingin diukur.

> **Ringkasan keputusan utama versi 1.0**
>
> 1. Akar kalimat (root) adalah predikator (§5.1.2.2). Kalimat tanpa verba tetap tanpa kopula. Predikat nomina, adjektiva, numeralia, atau frasa preposisi menjadi root.
>
> 2. Verba berprefiks di-, hu-, ta- dan bentuk pasif lain diberi Voice=Pass, sesuai istilah Nababan (§4.2.3.1, §4.2.4.2).
>
> 3. Subjek klausa, termasuk subjek klausa pasif, diberi nsubj.
>
> 4. Aktor yang langsung mengikuti verba pasif tanpa penanda (konstituen agentif, §5.1.2.1.2) diberi obj:agent. Aktor bertanda ni diberi obl:agent dengan ni sebagai case.
>
> 5. Objek verba aktif transitif (konstituen objektif) diberi obj.
>
> 6. Partikel predikatif do, ma, pe diberi PART dengan relasi discourse. Negasi dang, ndang, ndada, so, unang diberi PART dengan Polarity=Neg dan relasi advmod.
>
> 7. Penanda atributif na diberi PART dengan relasi mark pada pewatas yang ditandainya.
>
> 8. Sufiks pronominal (-hu/-ku, -mu, -na, -nami, -ta, -muna, -nasida) tidak dipisah dari kata dasarnya. Informasinya dicatat di FEATS.

## 2. Alur Kerja Anotator

### 2.1 Berkas yang diterima

1.  *btk_pilot_250_anotator_A.conllu* atau *btk_pilot_250_anotator_B.conllu*. Berkas sudah berisi 250 kalimat yang sudah ditokenisasi. Kolom ID, FORM, dan MISC (SpaceAfter=No) sudah terisi. Kolom lain bertanda \_ dan menunggu diisi.

2.  *Daftar_250_Kalimat_Pilot_UD_BatakToba.xlsx*. Lembar Daftar_250 memuat kalimat, terjemahan, dan genre. Lembar Log_Waktu dipakai untuk mencatat waktu dan kasus sulit.

3.  Pedoman ini, kamus paralel Batak Toba dan Indonesia berlabel UPOS sebagai alat bantu, dan salinan tata bahasa Nababan (1981).

### 2.2 Urutan kerja per kalimat

1.  Baca \# text dan \# text_id sampai makna kalimat jelas.

2.  Tentukan predikator utama kalimat. Kata itu diberi HEAD 0 dan DEPREL root (Bagian 6.1).

3.  Tentukan subjek predikator itu (nsubj), lalu argumen inti lain (obj, obj:agent).

4.  Beri label pewatas dan kata fungsi: partikel, negasi, preposisi, penanda na, determiner, dan tanda baca.

5.  Isi UPOS untuk setiap token (Bagian 5), lalu LEMMA (Bagian 4.3), lalu FEATS minimal (Bagian 7).

6.  Periksa bahwa setiap token punya satu HEAD, tepat satu token ber-HEAD 0, dan tidak ada lingkaran.

7.  Catat menit pengerjaan dan tingkat ragu (0 yakin, 1 agak ragu, 2 sangat ragu) di Log_Waktu. Bila ragu, tambahkan Ragu=Ya di kolom MISC token yang bersangkutan.

### 2.3 Batch dan jadwal

Kalimat sudah diacak berstrata genre dan dibagi lima batch @50 kalimat (komentar \# batch). Kerjakan berurutan dari batch 1. Setiap batch yang selesai diserahkan ke ketua tim untuk diperiksa dengan validator UD. Ketua tim hanya memeriksa kesalahan format, lalu mengembalikan daftar kesalahan format tanpa mengubah pilihan label anotator.

| **Batch** | **Kalimat**                                                | **Target selesai**      |
|-----------|------------------------------------------------------------|-------------------------|
| Pelatihan | 10 kalimat latihan bersama ketua tim (di luar 250 kalimat) | 5 sampai 6 Oktober 2026 |
| 1         | btk_pilot-001 sampai 050                                   | 16 Oktober 2026         |
| 2         | btk_pilot-051 sampai 100                                   | 23 Oktober 2026         |
| 3         | btk_pilot-101 sampai 150                                   | 30 Oktober 2026         |
| 4         | btk_pilot-151 sampai 200                                   | 6 November 2026         |
| 5         | btk_pilot-201 sampai 250                                   | 13 November 2026        |

*Tabel 2.1. Jadwal batch anotasi. Tanggal dapat disesuaikan ketua tim.*

### 2.4 Alat kerja

Berkas CoNLL-U adalah teks biasa dengan pemisah tab. Anotator boleh memakai penyunting teks yang menampilkan tab, atau alat anotasi CoNLL-U berbasis peramban yang ditetapkan ketua tim saat pelatihan. Apa pun alatnya, simpan kembali dalam format CoNLL-U UTF-8 dengan nama berkas yang sama.

## 3. Format CoNLL-U

Setiap kalimat terdiri atas baris komentar yang diawali \# dan satu baris per token. Satu baris token berisi sepuluh kolom dipisah tab. Kalimat dipisah satu baris kosong.

| **Kolom** | **Isi**                                                         | **Diisi oleh anotator?**                         |
|-----------|-----------------------------------------------------------------|--------------------------------------------------|
| ID        | Nomor urut token, mulai 1                                       | Tidak, sudah terisi                              |
| FORM      | Kata sebagaimana tertulis                                       | Tidak, jangan diubah                             |
| LEMMA     | Bentuk dasar (Bagian 4.3)                                       | Ya                                               |
| UPOS      | Kelas kata universal (Bagian 5)                                 | Ya                                               |
| XPOS      | Kelas kata khusus bahasa                                        | Tidak, biarkan \_                                |
| FEATS     | Fitur morfologis, dipisah \| dan diurutkan alfabetis (Bagian 7) | Ya, bila ada. Bila tidak ada, \_                 |
| HEAD      | ID kata induk, 0 untuk root                                     | Ya                                               |
| DEPREL    | Relasi ke induk (Bagian 6)                                      | Ya                                               |
| DEPS      | Dependensi tambahan                                             | Tidak, biarkan \_                                |
| MISC      | Catatan: SpaceAfter=No, Ragu=Ya, CorrectForm, Aktor             | Ya, hanya menambah. SpaceAfter=No jangan dihapus |

*Tabel 3.1. Kolom CoNLL-U dan pembagian tugas.*

Baris komentar yang sudah ada (# sent_id, \# batch, \# source_pair_id, \# genre, \# annotator, \# text, \# text_id) tidak diubah. Anotator boleh menambah satu baris *\# note = ...* di bawah \# text_id untuk catatan bebas tentang kalimat itu.

Beberapa nilai MISC dipakai bersama dan dipisah dengan \|, misalnya *SpaceAfter=No\|Ragu=Ya*.

## 4. Token, Ejaan, dan Lema

### 4.1 Tokenisasi sudah ditetapkan

Tokenisasi sudah dilakukan ketua tim. Aturannya: kata dipisah menurut spasi, tanda baca menjadi token sendiri, dan kata bertanda hubung tetap satu token (*pasu-pasu*, *di-si*, *mar-goar*). Anotator tidak menambah atau menghapus baris token.

### 4.2 Sufiks pronominal tidak dipisah

Nababan memperlakukan sufiks posesif dan sufiks aktor sebagai infleksi (§4.2.2.1, §4.2.2.2), sehingga kata seperti *jabuna* ‘rumahnya’, *anakna*, *rohangku*, *hepengmu*, *jolotta* tetap satu token. Pemilik dicatat di FEATS dengan Person\[psor\] dan Number\[psor\] (Bagian 7.3).

| **Sufiks**               | **Arti**               | **FEATS pada nomina**                                         |
|--------------------------|------------------------|---------------------------------------------------------------|
| -hu / -ku / -ngku / -kku | milikku                | Number\[psor\]=Sing\|Person\[psor\]=1                         |
| -mu / -m                 | milikmu                | Number\[psor\]=Sing\|Person\[psor\]=2                         |
| -na                      | miliknya               | Number\[psor\]=Sing\|Person\[psor\]=3                         |
| -nami                    | milik kami (eksklusif) | Number\[psor\]=Plur\|Person\[psor\]=1 dan MISC Klusivitas=Eks |
| -ta / -tta               | milik kita (inklusif)  | Number\[psor\]=Plur\|Person\[psor\]=1 dan MISC Klusivitas=Ink |
| -muna                    | milik kalian           | Number\[psor\]=Plur\|Person\[psor\]=2                         |
| -nasida                  | milik mereka           | Number\[psor\]=Plur\|Person\[psor\]=3                         |

*Tabel 4.1. Sufiks posesif (§4.4.1.1) dan fiturnya.*

> **Membedakan -na dan na**
>
> Sufiks -na menempel pada kata (*anakna*) dan berarti ‘-nya’. Kata na yang berdiri sendiri adalah penanda atributif (*halak na roa* ‘orang yang jahat’). Tokenisasi sudah membedakan keduanya karena keduanya ditulis berbeda.
>
> Bila penulis keliru memisah sufiks (*omak na* ‘ibunya’ ditulis terpisah), terapkan aturan goeswith di Bagian 4.4.

### 4.3 Lema

Lema adalah bentuk dasar kata. Prinsipnya mengikuti pembedaan Nababan antara infleksi (dilepas dari lema) dan derivasi (dipertahankan dalam lema).

1.  **Afiks infleksi dilepas.** Prefiks diatesis dan modus maN-, di-, hu-, ta-, tar- (potensial), sisipan -in-/ni- (kompletif), um- (kompletif aktif), akhiran -on (promisif), serta sufiks posesif dan sufiks aktor. Contoh: *manuhor* → tuhor, *ditongos* → tongos, *huida* → ida, *binuat* → buat, *tuhoron* → tuhor, *tarbuat* → buat, *jabuna* → jabu, *buatokku* → buat.

2.  **Afiks derivasi dipertahankan.** Prefiks mar- dan maN- pembentuk verba taktransitif (§4.6.4.1), pa- kausatif, par-...-an, pa-, ha-...-on pembentuk nomina, dan sufiks -hon serta -i tetap menjadi bagian lema. Contoh: *mardalan* → mardalan, *marsiajar* → marsiajar, *manortor* → manortor, *pangiranan* → pangiranan, *dipasahat* → pasahat, *dipatorus* → patorus.

3.  **Peleburan bunyi maN- dikembalikan** (§3.3.2, kaidah IIS1): maN- + t atau s → man- dengan konsonan awal luluh (*manuhor* → tuhor, *manurat* → surat), maN- + p → mam- (*mamio* → pio), maN- + r, l, n → manga- (*mangalehon* → lehon). Akar berawal b biasanya tetap (*mamboan* → boan), kecuali beberapa akar seperti bunu, buri, bereng, bodil (*mamereng* → bereng). Bila ragu, cari bentuk dasar di kamus paralel dan tandai Ragu=Ya.

4.  **Nama diri** memakai bentuk tertulisnya: *Butet*, *Santiago*.

5.  **Tanda baca** memakai dirinya sendiri sebagai lema.

6.  **Verba taktransitif sederhana** seperti *mangan* ‘makan’ dan *modom* ‘tidur’ memakai bentuk itu sendiri sebagai lema, karena Nababan memperlakukannya sebagai batang taktransitif (§4.6.4.1.3 butir 13).

### 4.4 Salah ketik dan kata yang terpisah

1.  **Salah ketik dalam satu kata.** Biarkan FORM apa adanya. Isi FEATS dengan Typo=Yes dan MISC dengan CorrectForm=bentuk_benar. Contoh: *Jesus Kristis*, token Kristis diberi Typo=Yes dan CorrectForm=Kristus.

2.  **Satu kata yang ditulis terpisah** (misalnya *omak na* untuk omakna). Token pertama memikul seluruh label kata itu (LEMMA, UPOS, FEATS, HEAD, DEPREL). Token berikutnya diberi UPOS X, LEMMA \_, HEAD ke token pertama, dan DEPREL goeswith. Token pertama diberi MISC CorrectForm=omakna.

3.  **Dua kata yang ditulis menyatu** (misalnya *ibanamangoli*). Jangan memecah token. Beri label menurut kata yang paling menentukan fungsi sintaksisnya, tambahkan Typo=Yes dan Ragu=Ya, lalu catat di \# note.

## 5. Kelas Kata (UPOS)

Nababan membagi kata menjadi kata isi (contentives) dan kata fungsi (functors) (§4.1). Tabel 5.1 memetakan pembagian itu ke 17 UPOS. Tabel 5.2 memuat daftar kata fungsi yang paling sering muncul.

| **Kelas Nababan (§)**                              | **UPOS**                                                       | **Contoh dan catatan**                                                                              |
|----------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Nomina umum (§4.3.1)                               | NOUN                                                           | jabu, dengke, jolma, hata, ari                                                                      |
| Nomina diri orang, tempat, marga, tekonim (§4.3.1) | PROPN                                                          | Butet, Samosir, Sitorus, Nai Badia. Marga berawalan si- (Sihombing) tetap satu PROPN                |
| Verba taktransitif, transitif, resiprokal (§4.3.2) | VERB                                                           | modom, mardalan, manuhor, dibuat, masijouan, adong ‘ada’                                            |
| Adjektiva (§4.3.3)                                 | ADJ                                                            | denggan, balga, uli, timbo. Tetap ADJ saat menjadi predikat                                         |
| Adjung waktu, adverbia, adjung klausa (§4.3.4)     | ADV                                                            | annon, tongtong, nattoari, ra ‘mungkin’, tottu ‘pasti’                                              |
| Interjeksi (§4.3.5)                                | INTJ                                                           | horas, beta, bohai, ale (seruan sapaan)                                                             |
| Pronomina persona (§4.4.1.1)                       | PRON                                                           | ahu/au, ho, ibana, hami, hita, hamu, nasida, iba                                                    |
| Pronomina demonstratif sebagai argumen             | PRON                                                           | *On* do ... ‘ini ...’, *i* ma ... saat berdiri sendiri                                              |
| Demonstratif sebagai pewatas nomina                | DET                                                            | jabu *on*, buku *i*, dolok *an*                                                                     |
| Pronomina tanya (§4.4.1.1)                         | PRON                                                           | ise, aha, dia, sadia                                                                                |
| Pronomina inklusif, partitif, taktentu             | DET bila mewatasi nomina, PRON bila berdiri sendiri            | sude, deba, saotik, si anu                                                                          |
| Numeralia pokok (§4.4.1.1)                         | NUM                                                            | sada, dua, sappulu, ratus                                                                           |
| Numeralia tingkat (§4.2.6)                         | ADJ                                                            | paduahon, parjolo, paitolu                                                                          |
| Pro-verba (§4.4.1.2)                               | VERB                                                           | marhua, mahua                                                                                       |
| Pro-adjektiva (§4.4.1.3)                           | ADJ                                                            | beha                                                                                                |
| Pro-adjung (§4.4.1.4)                              | ADV                                                            | dison, disi, tusi, tusan, andigan, nandigan                                                         |
| Pro-klausa (§4.4.1.5)                              | INTJ untuk olo, daong. ADV untuk boasa, jadi, asa, ipe, attong | Jadi ... ‘maka ...’ di awal klausa                                                                  |
| Preposisi (§4.4.2.1)                               | ADP                                                            | di, tu, sian, dohot ‘dengan’, marhite, songon, gabe, ala ni, ni                                     |
| Konjungsi subordinatif (§4.4.2.2)                  | SCONJ                                                          | molo, anggo, aut, nang, agia, tikki, dung, paima, asa, ala, ai, sotung, manang ‘apakah’, ia ‘bahwa’ |
| Penanda atributif na (§4.4.2.1.3)                  | PART                                                           | halak *na* roa, jabu *na* di huta                                                                   |
| Partikel modal predikatif (§4.4.3.1)               | PART                                                           | do, ma, pe, dope                                                                                    |
| Negasi (§4.4.3.1, §4.4.3.2)                        | PART                                                           | dang, ndang, ndada, dada, so, unang, sotung (larangan)                                              |
| Partikel kompletif (§4.4.3.1)                      | ADV                                                            | nunga ‘sudah’, naung, dung (kompletif)                                                              |
| Partikel imperatif (§4.4.3.2)                      | PART                                                           | jolo, ma, nanggo                                                                                    |
| Konektor (§4.4.4)                                  | CCONJ                                                          | dungi, alai, hape, jala, huhut, manang ‘atau’, dohot ‘dan’                                          |
| Auxiliari predikator modal (§4.4.5.1)              | AUX                                                            | naeng, ingkon/ikkon, boi, gabe (bila mendahului predikator lain)                                    |
| Auxiliari predikator lain (§4.4.5.1)               | ADV                                                            | pittor, sor, sai, be, muse, hian, tar ‘pura-pura’                                                   |
| Auxiliari nomina (§4.4.5.2)                        | DET                                                            | angka/akka (jamak), nasa, ganup. Partikel si sebelum nama orang juga DET                            |
| Auxiliari nomina holan, apala                      | ADV                                                            | holan ‘hanya’, apala ‘benar-benar’                                                                  |
| Auxiliari adjektiva (§4.4.5.3)                     | ADV                                                            | mansai/matcai, sahali, situtu, tung, lobi, lam, hian                                                |
| Auxiliari numeralia (§4.4.5.5.1)                   | ADV                                                            | nari, nanggo, hirahira                                                                              |
| Partikel sikap penutur (§4.4.5.7)                  | PART                                                           | tung ... do, ua, tahe, nian, maon, attong                                                           |
| Tanda baca                                         | PUNCT                                                          | . , ? ! " “ ”                                                                                       |
| Simbol                                             | SYM                                                            | %, Rp, + (jarang dalam 250 kalimat)                                                                 |
| Kata asing tak terserap                            | Menurut fungsinya, dengan Foreign=Yes                          | founder, twist, coding. Bila fungsinya tidak jelas, X                                               |

*Tabel 5.1. Pemetaan kelas kata Nababan ke UPOS.*

### 5.1 Kasus kelas kata yang sering membingungkan

1.  **dohot.** Bila menghubungkan dua unsur setara (*jabu dohot hauma* ‘rumah dan sawah’), CCONJ dengan relasi cc. Bila menandai alat atau penyerta (*dilitsing ibana dohot balobas* ‘dipukul dengan penggaris’), ADP dengan relasi case.

2.  **di.** Biasanya ADP lokatif ‘di’. Dalam *manukkun ma au di ho* ‘aku bertanya kepadamu’, di menandai sasaran yang tidak langsung mengikuti verba (§4.4.2.1.5) dan tetap ADP. Jangan tertukar dengan prefiks di- yang menempel pada verba.

3.  **ni.** Selalu ADP. Setelah nomina, ni menandai pemilik (*tarup ni jabu*). Setelah verba kompletif atau promisif, ni menandai aktor (*tuhoron ni si Ondo*) (§4.4.2.1.4).

4.  **ma.** Setelah predikator dalam kalimat berita, PART naratif (discourse). Dalam kalimat perintah, PART imperatif santun (discourse). Dalam *i ma* ‘itulah, yaitu’, tetap PART discourse.

5.  **i.** Sebagai pewatas nomina (*buku i*) DET. Berdiri sendiri sebagai argumen (*dang hubotoi*, *i ma* ...) PRON. Sebagai bagian dari ma i, songon i, ala ni i, tetap PRON.

6.  **gabe.** Sebelum predikator lain (*gabe guru do ibana* ‘ia menjadi guru’), AUX. Sebagai preposisi ‘sebagai, untuk’ (*ditodo nasida gabe kapala*), ADP. Bila menjadi satu-satunya predikat verbal, VERB.

7.  **godang.** Sebagai predikat (*Godang do jolma na ...* ‘banyak orang yang ...’), ADJ. Sebelum nomina tanpa na, DET.

8.  **laho.** Bila bermakna ‘pergi’, VERB. Bila mengantar klausa tujuan ‘untuk’ sebelum verba (*laho mangalehon barita*), SCONJ dengan relasi mark. Tandai Ragu=Ya bila tidak jelas.

9.  **adong.** VERB eksistensial ‘ada’. Hal yang ada menjadi nsubj.

## 6. Relasi Dependensi

### 6.1 Akar kalimat: predikator

Nababan menganalisis klausa sebagai konstruksi predikatif yang terdiri atas predikator (P), partikel modal (Mp) bila ada, subjek (S), dan komplemen (C). Urutan langsungnya P ± Mp + S ± C (§5.2.1.1). Predikator menjadi root.

1.  **Predikator verbal** (§5.1.2.2.1): verba menjadi root. *Modom do ibana.* ‘Dia tidur.’ → modom root.

2.  **Predikator nonverbal tanpa kopula** (§5.1.2.2.2): nomina, adjektiva, numeralia, frasa preposisi, atau pro-adjung menjadi root. *Guru do ibana.* → guru root. *Tolu do hodana.* → tolu root. *Di bilut do nasida.* → bilut root, di case.

3.  **Klausa ekuasional nomina-nomina** (§5.2.1.2): dalam urutan langsung, unsur sebelum partikel do adalah predikator dan unsur sesudahnya subjek. Pada kalimat tanya dengan pronomina tanya, pronomina tanya itulah predikator: *Aha do on?* → aha root, on nsubj.

4.  **Adjektiva atau adverbia di posisi predikator sebelum verba.** Nababan menyebut *hatop* dalam *hatop do ibana mardalan* ‘dia berjalan cepat’ sebagai predikator (§5.2.1.1). Dalam UD, inti klausa adalah predikat isi. Versi 1.0 memakai verba sebagai root dan adjektiva atau adverbia sebagai advmod. Keputusan ini diuji pada pilot dan dicatat sebagai isu terbuka.

5.  **Auxiliari tidak menjadi root.** *Naeng modom do ibana.* → modom root, naeng aux.

### 6.2 Subjek

1.  Subjek klausa diberi **nsubj**, termasuk subjek klausa pasif. *Ditongos nasida ma hepeng i.* → hepeng nsubj.

2.  Subjek berupa klausa diberi **csubj**. Nababan mencatat predikator agentif dengan subjek verba (§5.1.2.2.1 butir 2): *dimulai nasida ma marende* ‘bernyanyi dimulai oleh mereka’ → marende csubj.

3.  Pada urutan terbalik emfatik (§5.2.1.2), relasi tidak berubah walaupun subjek berada di depan. *Ibana do marpesta nattoari.* → marpesta tetap root, ibana nsubj.

4.  Subjek yang dilesapkan tidak ditambahkan sebagai token.

### 6.3 Diatesis: aktif, pasif, dan resiprokal

Verba transitif Batak Toba berinfleksi aktif (maN- dan seterusnya), pasif (di- dan seterusnya), atau resiprokal (masi-...-an) (§4.2.3.1). Tabel 6.1 memetakan setiap bentuk ke label UD.

| **Bentuk verba (§)**                        | **Contoh**          | **FEATS verba**                | **Pelaku**                         | **Sasaran** |
|---------------------------------------------|---------------------|--------------------------------|------------------------------------|-------------|
| Aktif sederhana maN- (§4.2.4.1)             | manuhor buku        | Voice=Act                      | nsubj                              | obj         |
| Aktif kompletif um- (§4.2.4.1)              | jumou dongan        | Aspect=Perf\|Voice=Act         | nsubj                              | obj         |
| Aktif distributif masi- (§4.2.4.1)          | masigarar utangna   | Voice=Act                      | nsubj                              | obj         |
| Imperatif tanpa afiks (§4.2.4.1)            | buat i              | Mood=Imp                       | nsubj bila ada                     | obj         |
| Pasif sederhana di- (§4.2.4.2)              | dibuat halak i      | Voice=Pass                     | obj:agent (langsung setelah verba) | nsubj       |
| Pasif sederhana hu- (aktor ‘aku/kami’)      | hubuat, hubuat hami | Voice=Pass dan MISC Aktor=1Eks | obj:agent bila ada kata aktor      | nsubj       |
| Pasif sederhana ta- (aktor ‘kita’)          | tabuat              | Voice=Pass dan MISC Aktor=1Ink | tanpa token aktor                  | nsubj       |
| Pasif kompletif -in-/ni- (§4.2.4.2)         | binuat ni halak i   | Aspect=Perf\|Voice=Pass        | obl:agent dengan case ni           | nsubj       |
| Pasif promisif -on (§4.2.4.2)               | tuhoron ni si Ondo  | Aspect=Prosp\|Voice=Pass       | obl:agent dengan case ni           | nsubj       |
| Pasif potensial tar- (§4.2.4.2)             | tarbuat ibana       | Mood=Pot\|Voice=Pass           | obj:agent                          | nsubj       |
| Resiprokal masi-...-an (§4.2.3.1)           | masijouan nasida    | Voice=Rcp                      | nsubj (para pelaku)                | tidak ada   |
| Taktransitif turunan mar-, maN-₁ (§4.6.4.1) | mardalan, manortor  | tanpa Voice                    | nsubj                              | tidak ada   |

*Tabel 6.1. Pemetaan bentuk verba ke fitur dan relasi.*

> **Mengapa aktor pasif diberi obj:agent**
>
> Nababan menganalisis verba pasif dan aktornya sebagai satu konstituen agentif, sejajar dengan verba aktif dan objeknya yang membentuk konstituen objektif (§5.1.2.1.2). Aktor itu ditempatkan langsung setelah verba tanpa preposisi (§4.2.2.2). Contoh: *hujou hami do ibana* ‘ia dipanggil oleh kami’, *ditongos nasida ma hepeng i* ‘uang itu dikirim oleh mereka’.
>
> Karena aktor itu bagian inti dari konstituen verba dan tidak bertanda preposisi, relasinya obj:agent. Bila aktor ditandai ni (bentuk kompletif dan promisif), relasinya obl:agent dengan ni sebagai case, karena kehadiran penanda menjadikannya argumen bertanda.
>
> Subjek klausa pasif tetap nsubj sesuai istilah Nababan, sedangkan Voice=Pass mencatat bentuk pasif pada verba.

### 6.4 Objek dan komplemen

1.  **obj** untuk sasaran verba aktif transitif yang tidak bertanda preposisi (§5.1.2.1.2 butir 2): *manuan eme do inatta* → eme obj.

2.  **obl** untuk argumen atau keterangan bertanda preposisi: *tu huta*, *di jabu*, *sian Jerman*, *dohot balobas*. Preposisinya diberi case pada nomina.

3.  **obl** juga untuk nomina keterangan waktu tanpa preposisi: *nattoari*, *sadari*, *di na sadari*.

4.  **advmod** untuk adverbia dan pro-adjung: *dison*, *annon*, *tongtong*.

5.  **xcomp** untuk verba kedua yang subjeknya dikendalikan argumen verba pertama: *disuru inana ma anakna i mangoli* → mangoli xcomp dari disuru.

6.  **ccomp** untuk klausa pelengkap, biasanya setelah ia ‘bahwa’ atau setelah verba berkata dan mengetahui: *huboto ia ro ibana* → ro ccomp, ia mark.

### 6.5 Kata fungsi pada klausa

| **Kata**                                              | **UPOS** | **DEPREL** | **Induk**                   |
|-------------------------------------------------------|----------|------------|-----------------------------|
| do, ma, pe, dope                                      | PART     | discourse  | predikator (root klausa)    |
| dang, ndang, ndada, so, unang, sotung                 | PART     | advmod     | predikator yang dinegasikan |
| nunga, naung, dung (kompletif)                        | ADV      | advmod     | predikator                  |
| naeng, ingkon, boi, gabe                              | AUX      | aux        | predikator utama            |
| pittor, sai, muse, hian, sor, be                      | ADV      | advmod     | predikator                  |
| molo, asa, ala, ai, dung, tikki, nang, laho (‘untuk’) | SCONJ    | mark       | predikator klausa bawahan   |
| jala, alai, dungi, hape, manang, dohot (‘dan’)        | CCONJ    | cc         | unsur setara sesudahnya     |
| jadi, asa (‘maka’), ipe                               | ADV      | advmod     | predikator klausa           |
| tanda baca                                            | PUNCT    | punct      | predikator klausa terdekat  |

*Tabel 6.2. Kata fungsi pada tingkat klausa.*

### 6.6 Frasa nomina

Frasa nomina Batak Toba berinti di depan (§5.1.1.1.1). Urutan pewatas sesudah inti: verba tak bertanda, nomina tak bertanda, frasa ni, frasa na, demonstratif, kuantor.

1.  **Nomina + nomina tak bertanda.** Bila keduanya membentuk satu satuan leksikal (*kapal habang* ‘pesawat’, *guru kapala*), compound. Bila nomina kedua menerangkan bahan, asal, atau jenis (*hudon tano* ‘periuk tanah’), nmod.

2.  **Frasa ni (pemilik).** *tarup ni jabu* → jabu nmod:poss dari tarup, ni case dari jabu.

3.  **Frasa na.** Penanda na diberi PART dan mark, menempel pada pewatas. Pewatas adjektiva diberi amod (*halak na roa* → roa amod, na mark). Pewatas verba atau klausa diberi acl:relcl (*halak na manuhor buku i* → manuhor acl:relcl). Pewatas numeralia diberi nummod. Pewatas frasa preposisi diberi nmod (*jabu na di huta* → huta nmod, di case, na mark).

4.  **Demonstratif** on, i, an, adu sebagai pewatas → DET, det.

5.  **Numeralia** → nummod, termasuk kuantor yang mendahului nomina (*dua makkuk kopi*).

6.  **Auxiliari nomina** angka/akka, nasa, ganup → det. si sebelum nama orang → det pada nama itu.

7.  **Nama diri lebih dari satu kata** (*Mortua Rajadoli*, *Ferdinand Lumban Tobing*) → kata pertama menjadi inti, sisanya flat.

8.  **Aposisi** (*si Pittor, anak ni Amadjaluk*) → appos. Nama geografis berpola nomina umum + nama (*Tao Toba*, *Pulo Samosir*) → nama menjadi flat dari nomina umum.

9.  **Klausa relatif tanpa inti** (*na mangolu* ‘yang hidup’) mengambil relasi yang semestinya dimiliki inti yang tidak hadir, misalnya nsubj atau obj. Penanda na tetap mark.

### 6.7 Koordinasi dan klausa majemuk

1.  Unsur setara pertama menjadi inti. Unsur berikutnya diberi **conj** ke unsur pertama. Konektor diberi **cc** ke unsur setara yang mengikutinya.

2.  Klausa yang digabung jala, alai, dungi, hape diberi conj ke klausa pertama.

3.  Dua klausa yang dijajarkan tanpa konektor, misalnya pasangan berimbang dalam umpasa (§5.2.2.2), diberi **parataxis** pada klausa kedua.

4.  Klausa keterangan yang diawali konjungsi subordinatif diberi **advcl** ke predikator klausa utama, dan konjungsinya diberi mark.

### 6.8 Relasi lain

| **Relasi** | **Dipakai untuk**                           | **Contoh**                                                               |
|------------|---------------------------------------------|--------------------------------------------------------------------------|
| vocative   | sapaan                                      | inang, amang, Tuhan dalam doa                                            |
| discourse  | partikel modal dan interjeksi dalam kalimat | do, ma, pe, horas                                                        |
| fixed      | gabungan kata fungsi yang membeku           | ala ni ‘karena’, taringot tu ‘tentang’: kata kedua fixed ke kata pertama |
| goeswith   | bagian kata yang salah dipisah              | omak na (Bagian 4.4)                                                     |
| dep        | hanya bila tidak ada relasi lain yang cocok | wajib disertai Ragu=Ya                                                   |

*Tabel 6.3. Relasi lain yang dipakai.*

Daftar lengkap relasi yang diizinkan dalam versi 1.0 ada di Lampiran A. Relasi di luar daftar itu tidak dipakai.

## 7. Fitur Morfologis (FEATS)

Versi 1.0 memakai sekumpulan fitur minimal. Fitur ditulis Nama=Nilai, dipisah tanda \|, dan diurutkan alfabetis menurut nama fitur (huruf kapital dan kecil diabaikan). Bila tidak ada fitur, isi \_.

### 7.1 Verba

| **Fitur** | **Nilai** | **Kapan dipakai**                                  |
|-----------|-----------|----------------------------------------------------|
| Voice     | Act       | verba transitif aktif maN-, um-, masi-             |
| Voice     | Pass      | verba di-, hu-, ta-, -in-/ni-, -on, tar- potensial |
| Voice     | Rcp       | verba resiprokal masi-...-an                       |
| Aspect    | Perf      | bentuk kompletif um- dan -in-/ni-                  |
| Aspect    | Prosp     | bentuk promisif -on (‘akan di-’, ‘harus di-’)      |
| Mood      | Imp       | verba imperatif (perintah)                         |
| Mood      | Pot       | verba potensial tar- (‘dapat di-’)                 |

*Tabel 7.1. Fitur verba.*

### 7.2 Pronomina

| **Kata**                       | **FEATS**                                                      |
|--------------------------------|----------------------------------------------------------------|
| ahu, au                        | Number=Sing\|Person=1\|PronType=Prs                            |
| hami                           | Clusivity=Ex\|Number=Plur\|Person=1\|PronType=Prs              |
| hita                           | Clusivity=In\|Number=Plur\|Person=1\|PronType=Prs              |
| ho                             | Number=Sing\|Person=2\|PronType=Prs                            |
| hamu                           | Number=Plur\|Person=2\|PronType=Prs (juga untuk sapaan hormat) |
| ibana                          | Number=Sing\|Person=3\|PronType=Prs                            |
| nasida                         | Number=Plur\|Person=3\|PronType=Prs (juga untuk sapaan hormat) |
| on, i, an, adu (PRON atau DET) | PronType=Dem                                                   |
| ise, aha, dia                  | PronType=Int                                                   |
| sude, nasa, ganup              | PronType=Tot                                                   |
| deba, saotik, si anu           | PronType=Ind                                                   |

*Tabel 7.2. Fitur pronomina dan determiner.*

### 7.3 Nomina dan kelas lain

1.  Nomina bersufiks posesif: Number\[psor\] dan Person\[psor\] (Tabel 4.1).

2.  Numeralia pokok: NumType=Card. Numeralia tingkat (ADJ): NumType=Ord.

3.  Adjektiva komparatif um- atau -an (*tumimbo*, *balgaan*): Degree=Cmp.

4.  Negasi: Polarity=Neg.

5.  Kata asing tak terserap: Foreign=Yes. Salah ketik: Typo=Yes.

6.  Fitur Number untuk nomina tidak diisi. Kejamakan ditandai kata angka/akka, bukan infleksi.

## 8. Contoh Anotasi Lengkap

Contoh 1 sampai 9 diambil dari proposal dan dari contoh Nababan. Contoh 10 adalah potongan kalimat korpus. Kolom XPOS dan DEPS tidak ditampilkan karena selalu \_. Contoh dibahas ulang pada sesi pelatihan sebelum anotasi dimulai.

**Contoh 1. Verba aktif transitif (contoh proposal)**

*Mangallang dengke do si Polan.* ‘Si Polan sedang makan ikan.’

| **ID** | **FORM**   | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC**      |
|--------|------------|-----------|----------|-----------|----------|------------|---------------|
| 1      | Mangallang | allang    | VERB     | Voice=Act | 0        | root       | \_            |
| 2      | dengke     | dengke    | NOUN     | \_        | 1        | obj        | \_            |
| 3      | do         | do        | PART     | \_        | 1        | discourse  | \_            |
| 4      | si         | si        | DET      | \_        | 5        | det        | \_            |
| 5      | Polan      | Polan     | PROPN    | \_        | 1        | nsubj      | SpaceAfter=No |
| 6      | .          | .         | PUNCT    | \_        | 1        | punct      | \_            |

**Contoh 2. Predikat adjektiva tanpa kopula (contoh proposal)**

*Uli do jabu i.* ‘Rumah itu bagus.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**    | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|--------------|----------|------------|---------------|
| 1      | Uli      | uli       | ADJ      | \_           | 0        | root       | \_            |
| 2      | do       | do        | PART     | \_           | 1        | discourse  | \_            |
| 3      | jabu     | jabu      | NOUN     | \_           | 1        | nsubj      | \_            |
| 4      | i        | i         | DET      | PronType=Dem | 3        | det        | SpaceAfter=No |
| 5      | .        | .         | PUNCT    | \_           | 1        | punct      | \_            |

**Contoh 3. Pasif di- dengan aktor (Nababan §5.1.2.1.2)**

*Ditongos nasida ma hepeng i.* ‘Uang itu dikirim oleh mereka.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                           | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|-------------------------------------|----------|------------|---------------|
| 1      | Ditongos | tongos    | VERB     | Voice=Pass                          | 0        | root       | \_            |
| 2      | nasida   | nasida    | PRON     | Number=Plur\|Person=3\|PronType=Prs | 1        | obj:agent  | \_            |
| 3      | ma       | ma        | PART     | \_                                  | 1        | discourse  | \_            |
| 4      | hepeng   | hepeng    | NOUN     | \_                                  | 1        | nsubj      | \_            |
| 5      | i        | i         | DET      | PronType=Dem                        | 4        | det        | SpaceAfter=No |
| 6      | .        | .         | PUNCT    | \_                                  | 1        | punct      | \_            |

**Contoh 4. Pasif hu- dengan aktor jamak (Nababan §5.1.2.2.1)**

*Hujou hami do ibana.* ‘Ia dipanggil oleh kami.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                                         | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|---------------------------------------------------|----------|------------|---------------|
| 1      | Hujou    | jou       | VERB     | Voice=Pass                                        | 0        | root       | Aktor=1Eks    |
| 2      | hami     | hami      | PRON     | Clusivity=Ex\|Number=Plur\|Person=1\|PronType=Prs | 1        | obj:agent  | \_            |
| 3      | do       | do        | PART     | \_                                                | 1        | discourse  | \_            |
| 4      | ibana    | ibana     | PRON     | Number=Sing\|Person=3\|PronType=Prs               | 1        | nsubj      | SpaceAfter=No |
| 5      | .        | .         | PUNCT    | \_                                                | 1        | punct      | \_            |

**Contoh 5. Negasi dan pasif hu- tanpa kata aktor (Nababan §4.4.3.1)**

*Dang huida ibana.* ‘Aku tidak melihatnya.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                           | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|-------------------------------------|----------|------------|---------------|
| 1      | Dang     | dang      | PART     | Polarity=Neg                        | 2        | advmod     | \_            |
| 2      | huida    | ida       | VERB     | Voice=Pass                          | 0        | root       | Aktor=1Eks    |
| 3      | ibana    | ibana     | PRON     | Number=Sing\|Person=3\|PronType=Prs | 2        | nsubj      | SpaceAfter=No |
| 4      | .        | .         | PUNCT    | \_                                  | 2        | punct      | \_            |

**Contoh 6. Aktor bertanda ni pada verba promisif (Nababan §4.4.2.1.4)**

*Tuhoron ni si Ondo do i.* ‘Itu akan dibeli oleh si Ondo.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|--------------------------|----------|------------|---------------|
| 1      | Tuhoron  | tuhor     | VERB     | Aspect=Prosp\|Voice=Pass | 0        | root       | \_            |
| 2      | ni       | ni        | ADP      | \_                       | 4        | case       | \_            |
| 3      | si       | si        | DET      | \_                       | 4        | det        | \_            |
| 4      | Ondo     | Ondo      | PROPN    | \_                       | 1        | obl:agent  | \_            |
| 5      | do       | do        | PART     | \_                       | 1        | discourse  | \_            |
| 6      | i        | i         | PRON     | PronType=Dem             | 1        | nsubj      | SpaceAfter=No |
| 7      | .        | .         | PUNCT    | \_                       | 1        | punct      | \_            |

**Contoh 7. Auxiliari modal (Nababan §4.4.5.1)**

*Naeng modom do ibana.* ‘Ia hendak tidur.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                           | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|-------------------------------------|----------|------------|---------------|
| 1      | Naeng    | naeng     | AUX      | \_                                  | 2        | aux        | \_            |
| 2      | modom    | modom     | VERB     | \_                                  | 0        | root       | \_            |
| 3      | do       | do        | PART     | \_                                  | 2        | discourse  | \_            |
| 4      | ibana    | ibana     | PRON     | Number=Sing\|Person=3\|PronType=Prs | 2        | nsubj      | SpaceAfter=No |
| 5      | .        | .         | PUNCT    | \_                                  | 2        | punct      | \_            |

**Contoh 8. Klausa relatif dengan na (Nababan §4.4.2.1.3), frasa nomina**

*halak na manuhor buku i* ‘orang yang membeli buku itu’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**    | **HEAD** | **DEPREL** | **MISC** |
|--------|----------|-----------|----------|--------------|----------|------------|----------|
| 1      | halak    | halak     | NOUN     | \_           | 0        | root       | \_       |
| 2      | na       | na        | PART     | \_           | 3        | mark       | \_       |
| 3      | manuhor  | tuhor     | VERB     | Voice=Act    | 1        | acl:relcl  | \_       |
| 4      | buku     | buku      | NOUN     | \_           | 3        | obj        | \_       |
| 5      | i        | i         | DET      | PronType=Dem | 1        | det        | \_       |

**Contoh 9. Predikat nomina dan sufiks posesif**

*Guru do amana.* ‘Ayahnya seorang guru.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                             | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|---------------------------------------|----------|------------|---------------|
| 1      | Guru     | guru      | NOUN     | \_                                    | 0        | root       | \_            |
| 2      | do       | do        | PART     | \_                                    | 1        | discourse  | \_            |
| 3      | amana    | ama       | NOUN     | Number\[psor\]=Sing\|Person\[psor\]=3 | 1        | nsubj      | SpaceAfter=No |
| 4      | .        | .         | PUNCT    | \_                                    | 1        | punct      | \_            |

**Contoh 10. Kalimat korpus: pasif dengan aktor dan verba terkendali (btk_pilot, Folktales)**

*jadi disuru inana ma anakna i mangoli.* ‘lalu ibunya menyuruh anaknya menikah.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS**                             | **HEAD** | **DEPREL** | **MISC**      |
|--------|----------|-----------|----------|---------------------------------------|----------|------------|---------------|
| 1      | jadi     | jadi      | ADV      | \_                                    | 2        | advmod     | \_            |
| 2      | disuru   | suru      | VERB     | Voice=Pass                            | 0        | root       | \_            |
| 3      | inana    | ina       | NOUN     | Number\[psor\]=Sing\|Person\[psor\]=3 | 2        | obj:agent  | \_            |
| 4      | ma       | ma        | PART     | \_                                    | 2        | discourse  | \_            |
| 5      | anakna   | anak      | NOUN     | Number\[psor\]=Sing\|Person\[psor\]=3 | 2        | nsubj      | \_            |
| 6      | i        | i         | DET      | PronType=Dem                          | 5        | det        | \_            |
| 7      | mangoli  | oli       | VERB     | Voice=Act                             | 2        | xcomp      | SpaceAfter=No |
| 8      | .        | .         | PUNCT    | \_                                    | 2        | punct      | \_            |

## 9. Kasus Sulit dan Aturan Saat Ragu

| **Situasi**                                                                                                      | **Aturan versi 1.0**                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kalimat tanpa predikator jelas (fragmen judul, seruan)                                                           | Kata isi terpenting menjadi root. Catat di \# note.                                                                                                             |
| Verba di- tanpa kata aktor                                                                                       | Tetap Voice=Pass. Tidak ada token obj:agent.                                                                                                                    |
| Aktor dan subjek sama-sama pronomina sehingga urutan meragukan                                                   | Kata yang langsung mengikuti verba adalah aktor (obj:agent). Kata sesudah partikel do atau ma adalah subjek (nsubj).                                            |
| Partikel do atau ma setelah subjek (urutan terbalik)                                                             | Tetap discourse ke predikator, bukan ke subjek.                                                                                                                 |
| Nomina tak bertanda setelah verba aktif yang tampak sebagai bagian predikat (*mangan indahan*, inkorporasi semu) | Tetap obj. Tambahkan Ragu=Ya bila nomina itu tidak merujuk benda tertentu.                                                                                      |
| Reduplikasi (*pasu-pasu*, *tureture*)                                                                            | Satu token. LEMMA bentuk dasar tanpa pengulangan bila jelas (pasu-pasu → pasu-pasu bila bentuk ulang adalah kata kamus). Tidak ada fitur khusus pada versi 1.0. |
| naeng, boi, ingkon tanpa verba lain                                                                              | Bila menjadi satu-satunya predikat, VERB dan root.                                                                                                              |
| Klausa kutipan langsung                                                                                          | Klausa kutipan menjadi ccomp dari verba berkata. Tanda kutip punct ke predikator kutipan.                                                                       |
| Kalimat tanya dengan pronomina tanya di depan                                                                    | Pronomina tanya menjadi root bila kalimat ekuasional (*Ise do ho?*). Bila pronomina tanya menjadi argumen verba (*Ise manuhor on?*), verba root dan ise nsubj.  |
| Kata pinjaman Indonesia atau Inggris                                                                             | Label menurut fungsi sintaksis. Foreign=Yes hanya untuk kata yang belum terserap ke ejaan Batak Toba.                                                           |
| Tidak yakin antara dua label                                                                                     | Pilih label yang paling sesuai Nababan, tambahkan Ragu=Ya, catat alternatifnya di Log_Waktu.                                                                    |

*Tabel 9.1. Kasus sulit.*

## 10. Pertanyaan, Pemeriksaan, dan Kesepakatan

### 10.1 Mengajukan pertanyaan

1.  Pertanyaan tentang aturan dikirim tertulis ke ketua tim, bukan ke anotator lain.

2.  Jawaban ketua tim dikirim ke kedua anotator sekaligus sebagai Catatan Pedoman bernomor (CP-01, CP-02, dan seterusnya). Catatan ini berlaku sebagai tambahan pedoman versi 1.0.

3.  Ketua tim tidak menjawab pertanyaan tentang label satu kalimat tertentu selama batch itu belum diserahkan kedua anotator.

### 10.2 Daftar periksa sebelum menyerahkan batch

1.  Setiap token punya LEMMA, UPOS, HEAD, dan DEPREL. Tidak ada \_ di keempat kolom itu, kecuali LEMMA untuk token goeswith.

2.  Setiap kalimat punya tepat satu root dengan HEAD 0.

3.  Tidak ada lingkaran dependensi dan tidak ada HEAD yang menunjuk ke ID yang tidak ada.

4.  PUNCT selalu berelasi punct. Relasi punct tidak dipakai untuk kelas kata lain.

5.  FEATS memakai nama dan nilai dari Bagian 7 dan diurutkan alfabetis.

6.  SpaceAfter=No yang sudah ada tidak terhapus.

7.  Log_Waktu batch itu terisi.

### 10.3 Pengukuran kesepakatan

Setelah seluruh batch selesai, ketua tim menghitung kesepakatan antaranotator untuk UPOS (persentase dan kappa Cohen), kepala (UAS), serta kepala dan relasi (LAS), dengan tokenisasi yang sama untuk kedua anotator. Kesepakatan juga dihitung per relasi dan per genre untuk menemukan konstruksi yang paling sering tidak disepakati. Sebagai patokan, treebank Tagalog UD-NewsCrawl melaporkan kappa 0,75 untuk kelas kata dan 0,68 untuk relasi dependensi (Aquino dkk., 2025). Perbedaan diselesaikan melalui adjudikasi, lalu pedoman direvisi menjadi versi 1.1.

## 11. Isu Terbuka untuk Versi 1.1

Keputusan berikut sengaja ditetapkan sederhana untuk pilot dan akan ditinjau berdasarkan hasil kesepakatan.

1.  Adjektiva atau adverbia di posisi predikator sebelum verba (Bagian 6.1 butir 4). Nababan menyebutnya predikator, versi 1.0 memakai verba sebagai root.

2.  Status gabe, boi, dan naeng sebagai AUX atau VERB dengan xcomp.

3.  Fitur untuk aktor yang tersandi pada verba (hu-, ta-, sufiks promisif). Versi 1.0 mencatatnya di MISC.

4.  Relasi untuk sasaran bertanda di setelah verba (§4.4.2.1.5). Versi 1.0 memakai obl.

5.  Perlakuan laho sebagai penanda tujuan.

6.  Representasi reduplikasi dan inkorporasi nomina semu.

7.  Pendaftaran subtipe obj:agent ke daftar relasi Batak Toba di UD sebelum treebank dirilis.

Konvensi lain untuk diatesis Austronesia (misalnya label Voice=Pat atau nsubj:pass dengan obl:agent) tidak dipakai dalam pilot ini dan dicatat untuk kajian lanjutan.

## Lampiran A. Daftar Relasi yang Dipakai

| **Relasi** | **Arti singkat**                 | **Relasi** | **Arti singkat**                    |
|------------|----------------------------------|------------|-------------------------------------|
| root       | akar kalimat                     | amod       | pewatas adjektiva                   |
| nsubj      | subjek nominal                   | nummod     | pewatas numeralia                   |
| csubj      | subjek klausa                    | det        | determiner                          |
| obj        | objek verba aktif                | nmod       | pewatas nomina                      |
| obj:agent  | aktor pasif tak bertanda         | nmod:poss  | pemilik dengan ni                   |
| obl        | argumen atau keterangan bertanda | acl:relcl  | klausa relatif na                   |
| obl:agent  | aktor pasif bertanda ni          | case       | preposisi                           |
| xcomp      | pelengkap terkendali             | mark       | penanda klausa dan na               |
| ccomp      | klausa pelengkap                 | cc         | konektor koordinasi                 |
| advcl      | klausa keterangan                | conj       | unsur koordinasi                    |
| advmod     | adverbia, negasi                 | parataxis  | klausa berjajar                     |
| aux        | auxiliari modal                  | flat       | nama majemuk                        |
| discourse  | partikel modal, interjeksi       | compound   | nomina majemuk                      |
| vocative   | sapaan                           | appos      | aposisi                             |
| fixed      | ungkapan beku                    | goeswith   | bagian kata terpisah                |
| punct      | tanda baca                       | dep        | tidak tergolongkan (dengan Ragu=Ya) |

## Lampiran B. Rujukan

1.  Nababan, P. W. J. (1981). A Grammar of Toba-Batak. Pacific Linguistics, Series D, No. 37. Canberra: Australian National University.

2.  de Marneffe, M.-C., Manning, C. D., Nivre, J., & Zeman, D. (2021). Universal Dependencies. Computational Linguistics, 47(2), 255-308.

3.  Nivre, J., dkk. (2020). Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection. Proceedings of LREC 2020, 4034-4043.

4.  Panduan resmi Universal Dependencies v2: https://universaldependencies.org/guidelines.html

5.  Alfina, I., Yuliawati, A., Tanaya, D., Dinakaramani, A., & Zeman, D. (2024). A Gold Standard Dataset for Javanese Tokenization, POS Tagging, Morphological Feature Tagging, and Dependency Parsing. Forum for Linguistic Studies, 6(5). https://doi.org/10.30564/fls.v6i5.6957

6.  Aquino, A., Miranda, L. J., & Or, E. (2025). The UD-NewsCrawl Treebank: Reflections and Challenges from a Large-scale Tagalog Syntactic Annotation Project. arXiv:2505.20428.

7.  Dyer, A., & O’Brien, J. (2025). Towards better annotation practices for symmetrical voice in Universal Dependencies. Proceedings of the Eighth Workshop on Universal Dependencies (UDW 2025), 137-142. https://aclanthology.org/2025.udw-1.15/

8.  Erlewine, M. Y. (2018). Extraction and Licensing in Toba Batak. Language, 94(3), 662-697. https://doi.org/10.1353/lan.2018.0039
