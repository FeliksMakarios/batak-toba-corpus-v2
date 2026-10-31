# Pedoman Anotasi Universal Dependencies v2 untuk Bahasa Batak Toba

Versi 1.2 untuk anotasi rintisan 250 kalimat. Berlaku mulai 5 Oktober 2026, pembaruan terakhir 28 Oktober 2026.

Penelitian Dosen Pemula 2026, *Pengembangan Pedoman Anotasi Universal Dependencies untuk Bahasa Batak Toba dan Pengujian Awal pada Korpus Kecil*, Program Studi Informatika, Universitas Pelita Harapan.

Versi Word: [Pedoman_Anotasi_UD_BatakToba_v1.2.docx](Pedoman_Anotasi_UD_BatakToba_v1.2.docx). Versi sebelumnya tersimpan di folder [arsip](arsip/).

| **Butir** | **Keterangan** |
|----|----|
| Dasar linguistik | P. W. J. Nababan (1981), A Grammar of Toba-Batak, Pacific Linguistics D-37. Nomor pasal (§) dalam pedoman ini merujuk ke buku tersebut. |
| Kerangka anotasi | Universal Dependencies versi 2 (universaldependencies.org), format CoNLL-U |
| Pemakai | Anotator A dan Anotator B (penutur Batak Toba), ketua tim sebagai adjudikator |
| Status | Versi 1.2. Direvisi menjadi versi 2.0 setelah evaluasi kesepakatan antaranotator. Riwayat perubahan ada di halaman Riwayat Versi. |

## Riwayat Versi

| **Versi** | **Tanggal** | **Perubahan utama** | **Dampak pada label** |
|----|----|----|----|
| **1.0** | 5 Oktober 2026 | Versi awal untuk anotasi rintisan 250 kalimat: format CoNLL-U, tokenisasi, lema, pemetaan kelas kata Nababan ke UPOS, relasi dependensi, fitur minimal, contoh 1 sampai 10, kasus sulit, dan prosedur kesepakatan. | Aturan awal. |
| **1.1** | 27 Oktober 2026 | Bagian 6.7 diperluas untuk kalimat majemuk setara dan kalimat kompleks (prinsip, langkah kerja, Tabel 6.3), istilah disesuaikan dengan Nababan §5.3, Contoh 11 (btk_pilot-001), aturan *laos*, butir daftar periksa 10.2. Format dokumen dan daftar isi dirapikan ketua tim. | Aturan baru untuk *laos* (selalu ADV advmod). Aturan lain diperjelas tanpa diubah. |
| **1.2** | 28 Oktober 2026 | Tabel daftar istilah di awal Bagian 3 sampai 7 (I-01 sampai I-117) dengan baris pengingat, penjelasan sederhana, contoh Indonesia dan Batak Toba, dan catatan beda dengan bahasa Indonesia. Jembatan S-P-O-Pel-K ke label UD (Bagian 6.4). Nomor istilah pada Ringkasan dan Bagian 2.2. Indeks istilah (Lampiran C). Riwayat Versi. Penomoran Ringkasan diperbaiki. | Tidak ada perubahan aturan label. |
| **2.0 (rencana)** | Setelah evaluasi kesepakatan | Revisi berdasarkan hasil kesepakatan antaranotator, adjudikasi, Catatan Pedoman (CP), dan isu terbuka Bagian 11. | Aturan dapat berubah. |

Aturan penomoran: perubahan yang tidak mengubah aturan label, atau hanya menambah aturan kecil, menaikkan angka di belakang titik (1.1, 1.2, dan seterusnya). Revisi menyeluruh setelah evaluasi kesepakatan antaranotator menjadi versi 2.0. Anotator selalu memakai versi terbaru, dan versi yang dipakai dicatat di Log_Waktu.

## 1. Tujuan dan Prinsip Dasar

Pedoman ini menjelaskan cara memberi label kelas kata, fitur morfologis, dan relasi dependensi pada kalimat Batak Toba dalam format CoNLL-U. Pedoman dipakai untuk menganotasi 250 kalimat rintisan secara ganda oleh dua anotator. Hasilnya dipakai untuk mengukur seberapa konsisten pedoman ini dapat diterapkan, lalu pedoman direvisi.

Lima prinsip berikut berlaku untuk seluruh keputusan.

1.  **Struktur Batak Toba menjadi dasar label.** Terjemahan Indonesia hanya membantu memahami makna. Jangan memberi label karena kata Indonesianya berkelas kata tertentu. Contoh: *dibuat ibana* diterjemahkan "dia mengambil", tetapi verbanya tetap verba pasif menurut Nababan.

2.  **Kelas kata dan konstruksi mengikuti Nababan (1981).** Bila pedoman ini merujuk § tertentu, pembagian dan istilahnya berasal dari buku tersebut.

3.  **Label UD v2 dipakai apa adanya.** Pedoman ini hanya menentukan label UD mana yang dipakai untuk konstruksi Batak Toba. Nama label tidak diterjemahkan.

4.  **Teks tidak boleh diubah.** Kolom FORM dan baris \# text tidak diedit, termasuk bila ada salah ketik. Kesalahan dicatat di kolom MISC (lihat Bagian 4.4).

5.  **Kerja mandiri.** Anotator A dan B tidak berdiskusi tentang kalimat yang sedang dianotasi. Pertanyaan diajukan ke ketua tim (Bagian 10). Perbedaan antaranotator justru yang ingin diukur.

**Cara memakai daftar istilah.** Istilah teknis dijelaskan dengan bahasa sederhana pada tabel Daftar istilah di awal Bagian 3 sampai 7. Setiap istilah bernomor I-01 sampai I-117 dan dijelaskan lengkap satu kali, di tempat istilah itu pertama kali dibutuhkan. Di bagian berikutnya istilah yang sama hanya muncul sebagai baris pengingat berwarna abu-abu dengan nomor rujukannya. Baris pengingat berwarna biru muda menandai istilah yang dibahas lebih rinci di bagian itu. Nomor istilah juga dicantumkan pada Ringkasan di bawah ini dan pada Bagian 2.2. Indeks alfabetis semua istilah ada di Lampiran C.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Ringkasan keputusan utama</strong></p>
<ol type="1">
<li><p>Akar kalimat (root) adalah predikator (§5.1.2.2). Kalimat tanpa verba tetap tanpa kopula. Predikat nomina, adjektiva, numeralia, atau frasa preposisi menjadi root. (Istilah: I-56, I-57, I-59)</p></li>
<li><p>Verba berprefiks di-, hu-, ta- dan bentuk pasif lain diberi Voice=Pass, sesuai istilah Nababan (§4.2.3.1, §4.2.4.2). (Istilah: I-69, I-109)</p></li>
<li><p>Subjek klausa, termasuk subjek klausa pasif, diberi nsubj. (Istilah: I-64)</p></li>
<li><p>Aktor yang langsung mengikuti verba pasif tanpa penanda (konstituen agentif, §5.1.2.1.2) diberi obj:agent. Aktor bertanda ni diberi obl:agent dengan ni sebagai case. (Istilah: I-73)</p></li>
<li><p>Objek verba aktif transitif (konstituen objektif) diberi obj. (Istilah: I-76)</p></li>
<li><p>Partikel predikatif do, ma, pe diberi PART dengan relasi discourse. Negasi dang, ndang, ndada, so, unang diberi PART dengan Polarity=Neg dan relasi advmod. (Istilah: I-81, I-53, I-82)</p></li>
<li><p>Penanda atributif na diberi PART dengan relasi mark pada pewatas yang ditandainya. (Istilah: I-20, I-54)</p></li>
<li><p>Sufiks pronominal (-hu/-ku, -mu, -na, -nami, -ta, -muna, -nasida) tidak dipisah dari kata dasarnya. Informasinya dicatat di FEATS. (Istilah: I-15, I-18)</p></li>
<li><p>Kalimat majemuk setara dan kalimat kompleks tetap punya satu root. Isi setiap klausa menunjuk ke predikator klausanya sendiri (Bagian 6.7). (Istilah: I-102, I-56)</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 2. Alur Kerja Anotator

### 2.1 Berkas yang diterima

1.  *btk_pilot_250_anotator_A.conllu* atau *btk_pilot_250_anotator_B.conllu*. Berkas sudah berisi 250 kalimat yang sudah ditokenisasi. Kolom ID, FORM, dan MISC (SpaceAfter=No) sudah terisi. Kolom lain bertanda \_ dan menunggu diisi.

2.  *Daftar_250_Kalimat_Pilot_UD_BatakToba.xlsx*. Lembar Daftar_250 memuat kalimat, terjemahan, dan genre. Lembar Log_Waktu dipakai untuk mencatat waktu dan kasus sulit.

3.  Pedoman ini, kamus paralel Batak Toba dan Indonesia berlabel UPOS sebagai alat bantu, dan salinan tata bahasa Nababan (1981).

### 2.2 Urutan kerja per kalimat

1.  Baca \# text dan \# text_id sampai makna kalimat jelas. (Istilah: I-03)

2.  Tentukan predikator utama kalimat. Kata itu diberi HEAD 0 dan DEPREL root (Bagian 6.1). (Istilah: I -57, I-10, I-56)

3.  Tentukan subjek predikator itu (**nsubj**), lalu argumen inti lain (**obj**, **obj:agent**). (Istilah: I-64, I-74, I-76, I-73)

4.  Beri label pewatas dan kata fungsi: partikel, negasi, preposisi, penanda *na*, determiner, dan tanda baca. (Istilah: I-45, I-82, I-43, I-20, I-40, I-48)

5.  Isi UPOS untuk setiap token (Bagian 5), lalu LEMMA (Bagian 4.3), lalu FEATS minimal (Bagian 7). (Istilah: I-07, I-06, I-09)

6.  Periksa bahwa setiap token punya satu HEAD, tepat satu token ber-HEAD 0, dan tidak ada lingkaran. (Istilah: I-10, I-56)

7.  Catat menit pengerjaan dan tingkat ragu (**0** yakin, **1** agak ragu, **2** sangat ragu) di **Log_Waktu**. Bila ragu, tambahkan **Ragu=Ya** di kolom **MISC** token yang bersangkutan. (Istilah: I-12)

### 2.3 Batch dan jadwal

Kalimat sudah diacak berstrata genre dan dibagi lima batch @50 kalimat (komentar \# batch). Kerjakan berurutan dari batch 1. Setiap batch yang selesai diserahkan ke ketua tim untuk diperiksa dengan validator UD. Ketua tim hanya memeriksa kesalahan format, lalu mengembalikan daftar kesalahan format tanpa mengubah pilihan label anotator.

| **Batch** | **Kalimat** | **Target selesai** |
|----|----|----|
| Pelatihan | 10 kalimat latihan bersama ketua tim (di luar 250 kalimat) | 5 sampai 6 Oktober 2026 |
| 1 | btk_pilot-001 sampai 050 | 16 Oktober 2026 |
| 2 | btk_pilot-051 sampai 100 | 23 Oktober 2026 |
| 3 | btk_pilot-101 sampai 150 | 30 Oktober 2026 |
| 4 | btk_pilot-151 sampai 200 | 6 November 2026 |
| 5 | btk_pilot-201 sampai 250 | 13 November 2026 |

*Tabel 2.1. Jadwal batch anotasi. Tanggal dapat disesuaikan ketua tim.*

### 2.4 Alat kerja

Berkas CoNLL-U adalah teks biasa dengan pemisah tab. Anotator boleh memakai penyunting teks yang menampilkan tab, atau alat anotasi CoNLL-U berbasis peramban yang ditetapkan ketua tim saat pelatihan. Apa pun alatnya, simpan kembali dalam format CoNLL-U UTF-8 dengan nama berkas yang sama.

## 3. Format CoNLL-U

**Daftar istilah Bagian 3**

| **No.** | **Istilah dan label UD** | **Arti sederhana** | **Contoh (Indonesia dan Batak Toba)** |
|----|----|----|----|
| **I-01** | **CoNLL-U** | Format berkas teks untuk menyimpan hasil anotasi. Satu token menempati satu baris, dan setiap baris punya sepuluh kolom yang dipisah tab. | Mirip lemba1r Excel dengan sepuluh kolom: satu kalimat menjadi beberapa baris, satu baris untuk satu kata. Berkas pilot: btk_pilot_250_anotator_A.conllu. |
| **I-02** | **token** | Satuan terkecil yang diberi label. Biasanya satu kata, tetapi satu tanda baca juga satu token. | *Rumah itu bagus.* = 4 token (Rumah, itu, bagus, titik). *Uli do jabu i.* = 5 token (*Uli*, *do*, *jabu*, *i*, titik). |
| **I-03** | **baris komentar (#)** | Baris berawalan \# yang memuat keterangan tentang kalimat, bukan kata. Anotator tidak mengubahnya, tetapi boleh menambah \# note. | \# sent_id (nomor kalimat), \# text (kalimat Batak Toba), \# text_id (terjemahan Indonesia), \# note (catatan anotator). |
| **I-04** | **ID** | Nomor urut token dalam kalimat, mulai dari 1. Nomor ini menjadi alamat kata saat mengisi HEAD. | *Uli do jabu i.* → *Uli* 1, *do* 2, *jabu* 3, *i* 4, titik 5. |
| **I-05** | **FORM** | Kata persis seperti tertulis di kalimat, termasuk salah ketiknya. Kolom ini tidak boleh diubah. | Bila tertulis *mengalu*, FORM tetap *mengalu* walaupun bentuk bakunya *mangalu*. |
| **I-06** | **LEMMA (lema)** | Bentuk dasar kata, seperti bentuk yang dicari di kamus. Cara menentukannya ada di Bagian 4.3. | *membeli* → *beli*. *manuhor* → *tuhor*, *jabuna* → *jabu*. |
| **I-07** | **UPOS** | Kelas kata universal. UD memakai 17 label yang sama untuk semua bahasa (Bagian 5). | Kata benda *rumah* = NOUN. *jabu* NOUN, *modom* VERB, *uli* ADJ. |
| **I-08** | **XPOS dan DEPS** | XPOS adalah kelas kata khusus bahasa. DEPS adalah dependensi tambahan. Keduanya tidak dipakai dalam pilot. | Selalu diisi \_. |
| **I-09** | **FEATS (fitur morfologis)** | Keterangan tata bahasa yang melekat pada bentuk kata, misalnya pasif, tunggal atau jamak, orang pertama. Ditulis Nama=Nilai (Bagian 7). | *dikirim* berbentuk pasif → Voice=Pass. *ditongos* → Voice=Pass. *ibana* → Number=Sing\|Person=3\|PronType=Prs. |
| **I-10** | **HEAD (induk)** | ID kata yang diterangkan atau dilengkapi oleh token ini. Setiap token punya tepat satu induk. Predikator utama diberi HEAD 0 karena tidak punya induk (lihat root, I-56). | Dalam *rumah bagus*, kata *bagus* menerangkan *rumah*, jadi induk *besar* adalah *rumah*. *Uli do jabu i.* → *jabu* (ID 3) diberi HEAD 1 karena menjadi subjek *uli*. *uli* diberi HEAD 0. |
| **I-11** | **DEPREL (relasi dependensi)** | Nama hubungan antara token dan induknya, misalnya subjek, objek, atau keterangan (Bagian 6). | Dalam *Dia tidur*, *Dia* adalah subjek *tidur*. *Modom do ibana.* → *ibana* nsubj ke *modom*. |
| **I-12** | **MISC** | Kolom catatan tambahan. Isinya hanya boleh ditambah. Nilai yang dipakai: SpaceAfter=No (tidak ada spasi sesudah token), Ragu=Ya, CorrectForm, dan Aktor. | SpaceAfter=No\|Ragu=Ya (dua catatan dipisah tanda \|). |

Setiap kalimat terdiri atas baris komentar yang diawali \# dan satu baris per token. Satu baris token berisi sepuluh kolom dipisah tab. Kalimat dipisah satu baris kosong.

| **Kolom** | **Isi** | **Diisi oleh anotator?** |
|----|----|----|
| ID | Nomor urut token, mulai 1 | Tidak, sudah terisi |
| FORM | Kata sebagaimana tertulis | Tidak, jangan diubah |
| LEMMA | Bentuk dasar (Bagian 4.3) | Ya |
| UPOS | Kelas kata universal (Bagian 5) | Ya |
| XPOS | Kelas kata khusus bahasa | Tidak, biarkan \_ |
| FEATS | Fitur morfologis, dipisah \| dan diurutkan alfabetis (Bagian 7) | Ya, bila ada. Bila tidak ada, \_ |
| HEAD | ID kata induk, 0 untuk root | Ya |
| DEPREL | Relasi ke induk (Bagian 6) | Ya |
| DEPS | Dependensi tambahan | Tidak, biarkan \_ |
| MISC | Catatan: SpaceAfter=No, Ragu=Ya, CorrectForm, Aktor | Ya, hanya menambah. SpaceAfter=No jangan dihapus |

*Tabel 3.1. Kolom CoNLL-U dan pembagian tugas.*

Baris komentar yang sudah ada (# sent_id, \# batch, \# source_pair_id, \# genre, \# annotator, \# text, \# text_id) tidak diubah. Anotator boleh menambah satu baris *\# note = ...* di bawah \# text_id untuk catatan bebas tentang kalimat itu.

Beberapa nilai MISC dipakai bersama dan dipisah dengan **\|**, misalnya *SpaceAfter=No\|Ragu=Ya*.

## 4. Token, Ejaan, dan Lema

### 4.1 Tokenisasi sudah ditetapkan

**Daftar istilah Bagian 4.1**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Istilah dan label UD</strong></th>
<th><strong>Arti sederhana</strong></th>
<th><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>→ I-02</em></td>
<td>token</td>
<td colspan="2"><strong>Pengingat:</strong> Satuan terkecil yang diberi label: satu kata atau satu tanda baca.</td>
</tr>
<tr>
<td><strong>I-13</strong></td>
<td><strong>tokenisasi</strong></td>
<td>Pemenggalan kalimat menjadi token. Dalam pilot ini tokenisasi sudah dikerjakan ketua tim, sehingga anotator tidak menambah atau menghapus baris.</td>
<td><em>pasu-pasu</em> tetap satu token karena bertanda hubung. Titik pada akhir kalimat menjadi token sendiri.</td>
</tr>
</tbody>
</table>

Tokenisasi sudah dilakukan ketua tim. Aturannya:

- kata dipisah menurut spasi,

- tanda baca menjadi token sendiri, dan

- kata bertanda hubung tetap satu token (*pasu-pasu*, *di-si*, *mar-goar*).

Anotator **tidak** menambah atau menghapus baris token.

### 4.2 Sufiks pronominal tidak dipisah

**Daftar istilah Bagian 4.2**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 43%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Istilah dan label UD</strong></th>
<th><strong>Arti sederhana</strong></th>
<th><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I-14</strong></td>
<td><strong>sufiks (akhiran)</strong></td>
<td>Bagian kata yang menempel di belakang kata dasar.</td>
<td><em>rumah</em> + <em>-nya</em> → <em>rumahnya</em>. <em>jabu</em> + <em>-na</em> → <em>jabuna</em>.</td>
</tr>
<tr>
<td><strong>I-15</strong></td>
<td><strong>sufiks posesif (sufiks pronominal)</strong></td>
<td><p>Akhiran yang menyatakan pemilik: <em>-hu/-ku, -mu, -na, -nami, -ta, -muna, -nasida</em>. Kata bersufiks tetap satu token.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Bahasa Indonesia hanya punya <em>-ku, -mu, -nya</em>. Batak Toba juga punya sufiks pemilik jamak <em>(-nami, -ta, -muna, -nasida</em>), sehingga FEATS mencatat jumlah pemilik.</p></td>
<td><em>rumahku</em>, <em>rumahmu</em>. <em>rohangku</em>, <em>hepengmu</em>, <em>jabuna</em>.</td>
</tr>
<tr>
<td><strong>I-16</strong></td>
<td><strong>sufiks aktor</strong></td>
<td>Akhiran pada verba pasif yang menyatakan pelaku. Sufiks ini juga tidak dipisah dari kata dasarnya.</td>
<td><em>buatokku</em> (lema <em>buat</em>) memuat pelaku orang pertama. Padanan terdekat dalam bahasa Indonesia: <em>kuambil</em>.</td>
</tr>
<tr>
<td><strong>I-17</strong></td>
<td><strong>infleksi</strong></td>
<td><p>Perubahan bentuk kata yang tidak membentuk kata baru. Infleksi hanya menambah keterangan tata bahasa seperti pasif atau pemilik. Afiks infleksi dilepas dari lema (Bagian 4.3).</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Tata bahasa sekolah jarang menyebut <em>me-</em> dan <em>di-</em> sebagai infleksi. Nababan memakai istilah ini untuk prefiks diatesis Batak Toba (§4.2).</p></td>
<td><em>membeli</em> dan <em>dibeli</em> tetap kata <em>beli</em>. <em>manuhor</em> dan <em>tuhoron</em> tetap kata <em>tuhor</em>.</td>
</tr>
<tr>
<td><strong>I-18</strong></td>
<td><strong>Person[psor] dan Number[psor]</strong></td>
<td>Fitur pemilik. Person[psor] menyatakan orang ke berapa pemiliknya (1, 2, 3). Number[psor] menyatakan pemilik tunggal (Sing) atau jamak (Plur).</td>
<td><em>jabuna</em> ‘rumahnya’ → Number[psor]=Sing|Person[psor]=3. Sufiks <em>-nasida</em> ‘milik mereka’ → Number[psor]=Plur|Person[psor]=3.</td>
</tr>
<tr>
<td><strong>I-19</strong></td>
<td><strong>eksklusif dan inklusif (klusivitas)</strong></td>
<td>Pembedaan ‘kami’ (tanpa pendengar) dan ‘kita’ (bersama pendengar). Pada pronomina dicatat dengan Clusivity, pada sufiks dicatat di MISC dengan Klusivitas.</td>
<td><em>kami</em> (eksklusif), <em>kita</em> (inklusif). <em>hami</em> dan <em>-nami</em> eksklusif (Clusivity=Ex), <em>hita</em> dan <em>-ta</em> inklusif (Clusivity=In).</td>
</tr>
<tr>
<td><strong>I-20</strong></td>
<td><strong>na (penanda atributif)</strong></td>
<td><p>Kata <em>na</em> yang berdiri sendiri dan mengantar pewatas nomina, mirip <em>yang</em>. Diberi PART dengan relasi mark (Bagian 6.6). Berbeda dari sufiks <em>-na</em> ‘-nya’.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> UD bahasa Indonesia biasanya memberi <em>yang</em> label PRON atau SCONJ. Pedoman ini memberi <em>na</em> label PART dengan relasi mark.</p></td>
<td><em>orang yang jahat</em> = <em>halak na roa</em>. Bandingkan <em>anakna</em> ‘anaknya’ (sufiks, satu token).</td>
</tr>
<tr>
<td><em>→ I-09</em></td>
<td>FEATS</td>
<td colspan="2"><strong>Pengingat:</strong> Pemilik pada sufiks dicatat di FEATS, bukan dengan memecah token.</td>
</tr>
</tbody>
</table>

Nababan memperlakukan **sufiks posesif** dan **sufiks aktor** sebagai **infleksi** (§4.2.2.1, §4.2.2.2), sehingga kata seperti *jabuna* ‘rumahnya’, *anakna*, *rohangku*, *hepengmu*, *jolotta* tetap satu token. Pemilik dicatat di **FEATS** dengan Person\[psor\] dan Number\[psor\] (Bagian 7.3).

| **Sufiks** | **Arti** | **FEATS pada nomina** |
|----|----|----|
| -hu / -ku / -ngku / -kku | milikku | Number\[psor\]=Sing\|Person\[psor\]=1 |
| -mu / -m | milikmu | Number\[psor\]=Sing\|Person\[psor\]=2 |
| -na | miliknya | Number\[psor\]=Sing\|Person\[psor\]=3 |
| -nami | milik kami (eksklusif) | Number\[psor\]=Plur\|Person\[psor\]=1 dan MISC Klusivitas=Eks |
| -ta / -tta | milik kita (inklusif) | Number\[psor\]=Plur\|Person\[psor\]=1 dan MISC Klusivitas=Ink |
| -muna | milik kalian | Number\[psor\]=Plur\|Person\[psor\]=2 |
| -nasida | milik mereka | Number\[psor\]=Plur\|Person\[psor\]=3 |

*Tabel 4.1. Sufiks posesif (§4.4.1.1) dan fiturnya.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Membedakan <em>-na</em> dan <em>na</em></strong></p>
<p>Sufiks <em>-na</em> menempel pada kata (<em>anakna</em>) dan berarti ‘-nya’. Kata <em>na</em> yang berdiri sendiri adalah penanda atributif (<em>halak na roa</em> ‘orang yang jahat’). Tokenisasi sudah membedakan keduanya karena keduanya ditulis berbeda.</p>
<p>Bila penulis keliru memisah sufiks (<em>omak na</em> ‘ibunya’ ditulis terpisah), terapkan aturan <strong>goeswith</strong> pada Bagian 4.4.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 4.3 Lema

**Daftar istilah Bagian 4.3**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Istilah dan label UD</strong></th>
<th><strong>Arti sederhana</strong></th>
<th><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>→ I-06</em></td>
<td>LEMMA (lema)</td>
<td colspan="2"><strong>Pengingat, dibahas lebih rinci di sini:</strong> Bagian ini membahas lema secara rinci. Lema ditentukan dengan dua langkah: lepaskan afiks infleksi (I-17), lalu pertahankan afiks derivasi (I-22). Peleburan bunyi maN- dikembalikan (I-27). Bila ragu, cari bentuk dasar di kamus paralel dan tandai Ragu=Ya.</td>
</tr>
<tr>
<td><em>→ I-17</em></td>
<td>infleksi</td>
<td colspan="2"><strong>Pengingat:</strong> Afiks infleksi dilepas dari lema.</td>
</tr>
<tr>
<td><em>→ I-15</em></td>
<td>sufiks posesif</td>
<td colspan="2"><strong>Pengingat:</strong> Ikut dilepas dari lema: <em>jabuna</em> → <em>jabu</em>.</td>
</tr>
<tr>
<td><strong>I-21</strong></td>
<td><strong>afiks (imbuhan)</strong></td>
<td>Bagian yang ditambahkan pada kata dasar: prefiks (awalan), sisipan (infiks), dan sufiks (akhiran).</td>
<td><em>me-</em>, <em>-el-</em> (<em>telunjuk</em>), <em>-kan</em>. Prefiks <em>maN-</em>, <em>di-</em>, <em>tar-</em>, sisipan <em>-in-</em> (<em>binuat</em>), akhiran <em>-on</em> (<em>tuhoron</em>).</td>
</tr>
<tr>
<td><strong>I-22</strong></td>
<td><strong>derivasi</strong></td>
<td><p>Pembentukan kata baru dari kata dasar sehingga makna atau kelas katanya berubah. Afiks derivasi tetap menjadi bagian lema.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Banyak kamus dan alat pengolah bahasa Indonesia memakai <em>jalan</em> sebagai lema <em>berjalan</em>. Di pedoman ini <em>mardalan</em> tetap <em>mardalan</em> karena Nababan menggolongkan <em>mar-</em> sebagai derivasi.</p></td>
<td><em>jalan</em> → <em>berjalan</em>, <em>ajar</em> → <em>pelajaran</em>. <em>mardalan</em> → lema <em>mardalan</em>, <em>pangiranan</em> → lema <em>pangiranan</em>.</td>
</tr>
<tr>
<td><strong>I-23</strong></td>
<td><strong>diatesis</strong></td>
<td>Hubungan antara bentuk verba dan peran pelaku. Batak Toba punya tiga diatesis: aktif, pasif, dan resiprokal (Bagian 6.3).</td>
<td><em>membeli</em> (aktif), <em>dibeli</em> (pasif). <em>manuhor</em> (aktif), <em>ditongos</em> (pasif), <em>masijouan</em> (resiprokal).</td>
</tr>
<tr>
<td><strong>I-24</strong></td>
<td><strong>kompletif</strong></td>
<td>Bentuk verba yang menyatakan perbuatan sudah selesai. Ditandai <em>um-</em> (aktif) atau <em>-in-/ni-</em> (pasif) dan dicatat Aspect=Perf.</td>
<td>Mirip makna <em>sudah di-</em> atau <em>telah</em>. <em>jumou dongan</em>, <em>binuat</em> (lema <em>buat</em>).</td>
</tr>
<tr>
<td><strong>I-25</strong></td>
<td><strong>promisif</strong></td>
<td>Bentuk verba berakhiran <em>-on</em> yang berarti ‘akan di-’ atau ‘harus di-’. Dicatat Aspect=Prosp.</td>
<td><em>akan dibeli</em> = <em>tuhoron</em> (lema <em>tuhor</em>).</td>
</tr>
<tr>
<td><strong>I-26</strong></td>
<td><strong>potensial</strong></td>
<td><p>Bentuk verba <em>tar-</em> yang berarti ‘dapat di-’. Dicatat Mood=Pot.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Prefiks <em>ter-</em> bahasa Indonesia juga bisa berarti ‘paling’ atau ‘tidak sengaja’. Mood=Pot hanya untuk <em>tar-</em> potensial menurut Nababan (§4.2.4.2).</p></td>
<td><em>dapat dibuat</em> = <em>tarbuat</em> (lema <em>buat</em>).</td>
</tr>
<tr>
<td><strong>I-27</strong></td>
<td><strong>peleburan bunyi maN-</strong></td>
<td>Perubahan bunyi saat prefiks maN- bertemu konsonan awal kata dasar. Konsonan awal bisa luluh, sehingga lema harus dikembalikan ke bentuk asalnya.</td>
<td><em>me-</em> + <em>tulis</em> → <em>menulis</em> (t luluh). <em>manuhor</em> → <em>tuhor</em>, <em>manurat</em> → <em>surat</em>, <em>mamio</em> → <em>pio</em>.</td>
</tr>
<tr>
<td><strong>I-28</strong></td>
<td><strong>verba transitif dan taktransitif</strong></td>
<td>Verba transitif membutuhkan sasaran (objek). Verba taktransitif tidak membutuhkannya.</td>
<td><em>membeli buku</em> (transitif), <em>tidur</em> (taktransitif). <em>manuhor buku</em> (transitif), <em>modom</em>, <em>mardalan</em> (taktransitif).</td>
</tr>
</tbody>
</table>

Lema adalah bentuk dasar kata. Prinsipnya mengikuti pembedaan Nababan antara infleksi (dilepas dari lema) dan derivasi (dipertahankan dalam lema).

1.  **Afiks infleksi dilepas.** Prefiks diatesis dan modus *maN-*, *di-*, *hu-*, *ta-*, *tar-* (potensial), sisipan *-in-/ni-* (kompletif), *um-* (kompletif aktif), akhiran *-on* (promisif), serta sufiks posesif dan sufiks aktor. Contoh: *manuhor* → tuhor, *ditongos* → tongos, *huida* → ida, *binuat* → buat, *tuhoron* → tuhor, *tarbuat* → buat, *jabuna* → jabu, *buatokku* → buat.

2.  **Afiks derivasi dipertahankan.** Prefiks *mar-* dan *maN-* pembentuk verba taktransitif (§4.6.4.1), pa- kausatif, *par-...-an*, *pa-*, *ha-...-on* pembentuk nomina, dan sufiks *-hon* serta *-i* tetap menjadi bagian lema. Contoh: *mardalan* → mardalan, *marsiajar* → marsiajar, *manortor* → manortor, *pangiranan* → pangiranan, *dipasahat* → pasahat, *dipatorus* → patorus.

3.  **Peleburan bunyi maN- dikembalikan** (§3.3.2, kaidah IIS1): *maN-* + *t* atau *s* → *man-* dengan konsonan awal luluh (*manuhor* → tuhor, *manurat* → surat), *maN-* + *p* → *mam-* (*mamio* → pio), *maN-* + *r*, *l*, *n* → *manga-* (*mangalehon* → lehon). Akar berawal *b* biasanya tetap (*mamboan* → boan), kecuali beberapa akar seperti *bunu*, *buri*, *bereng*, *bodil* (*mamereng* → bereng). Bila ragu, cari bentuk dasar di kamus paralel dan tandai **Ragu=Ya**.

4.  **Nama diri** memakai bentuk tertulisnya: *Butet*, *Santiago*.

5.  **Tanda baca** memakai dirinya sendiri sebagai lema.

6.  **Verba taktransitif sederhana** seperti *mangan* ‘makan’ dan *modom* ‘tidur’ memakai bentuk itu sendiri sebagai lema, karena Nababan memperlakukannya sebagai batang taktransitif (§4.6.4.1.3 butir 13).

### 4.4 Salah ketik dan kata yang terpisah

**Daftar istilah Bagian 4.4**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Istilah dan label UD</strong></th>
<th><strong>Arti sederhana</strong></th>
<th><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I-29</strong></td>
<td><strong>Typo=Yes dan CorrectForm</strong></td>
<td>Penanda kata yang salah tulis. FORM dibiarkan, FEATS diberi Typo=Yes, dan MISC diberi CorrectForm berisi bentuk yang benar.</td>
<td><em>Jesus Kristis</em> → token <em>Kristis</em>: Typo=Yes dan CorrectForm=Kristus.</td>
</tr>
<tr>
<td><strong>I-30</strong></td>
<td><strong>goeswith</strong></td>
<td>Relasi untuk potongan kata yang salah dipisah spasi. Potongan kedua diberi UPOS X, lema _, dan menunjuk ke potongan pertama.</td>
<td><em>rumah nya</em> untuk <em>rumahnya</em>. <em>omak na</em> untuk <em>omakna</em> → <em>na</em> X goeswith ke <em>omak</em>.</td>
</tr>
<tr>
<td><em>→ I-12</em></td>
<td>MISC</td>
<td colspan="2"><strong>Pengingat:</strong> Tempat CorrectForm dan Ragu=Ya.</td>
</tr>
<tr>
<td><em>→ I-03</em></td>
<td>baris komentar (#)</td>
<td colspan="2"><strong>Pengingat:</strong> Kata yang ditulis menyatu dicatat di # note.</td>
</tr>
</tbody>
</table>

1.  **Salah ketik dalam satu kata.** Biarkan FORM apa adanya. Isi FEATS dengan Typo=Yes dan MISC dengan CorrectForm=bentuk_benar. Contoh: *Jesus Kristis*, token Kristis diberi Typo=Yes dan CorrectForm=Kristus.

2.  **Satu kata yang ditulis terpisah** (misalnya *omak na* untuk omakna). Token pertama memikul seluruh label kata itu (LEMMA, UPOS, FEATS, HEAD, DEPREL). Token berikutnya diberi UPOS X, LEMMA \_, HEAD ke token pertama, dan DEPREL goeswith. Token pertama diberi MISC CorrectForm=omakna.

3.  **Dua kata yang ditulis menyatu** (misalnya *ibanamangoli*). Jangan memecah token. Beri label menurut kata yang paling menentukan fungsi sintaksisnya, tambahkan Typo=Yes dan Ragu=Ya, lalu catat di \# note.

## 5. Kelas Kata (UPOS)

**Daftar istilah Bagian 5**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah dan label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-07</em></td>
<td style="text-align: left;">UPOS</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat, dibahas lebih rinci di sini:</strong> Bab ini membahas ke-17 label UPOS. Labelnya mengikuti kelas kata Nababan, bukan kelas kata terjemahan Indonesia.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-20</em></td>
<td style="text-align: left;">na</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Penanda atributif <em>na</em> diberi PART.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-31</strong></td>
<td style="text-align: left;"><strong>kata isi</strong></td>
<td style="text-align: left;">Kata yang membawa makna leksikal: nomina, verba, adjektiva, dan adjung (§4.1).</td>
<td style="text-align: left;"><em>rumah</em>, <em>tidur</em>, <em>bagus</em>. <em>jabu</em>, <em>modom</em>, <em>uli</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-32</strong></td>
<td style="text-align: left;"><strong>kata fungsi</strong></td>
<td style="text-align: left;">Kata yang terutama membawa hubungan tata bahasa: preposisi, konjungsi, partikel, auxiliari.</td>
<td style="text-align: left;"><em>di</em>, <em>dan</em>, <em>-lah</em>, <em>akan</em>. <em>di</em>, <em>jala</em>, <em>do</em>, <em>naeng</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-33</strong></td>
<td style="text-align: left;"><strong>NOUN</strong></td>
<td style="text-align: left;">Nomina umum: nama benda, orang, tempat, atau waktu secara umum.</td>
<td style="text-align: left;"><em>rumah</em>, <em>ikan</em>. <em>jabu</em>, <em>dengke</em>, <em>jolma</em>, <em>ari</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-34</strong></td>
<td style="text-align: left;"><strong>PROPN</strong></td>
<td style="text-align: left;">Nomina diri: nama orang, tempat, marga, dan tekonim.</td>
<td style="text-align: left;"><em>Medan</em>. <em>Butet</em>, <em>Samosir</em>, <em>Sitorus</em>, <em>Nai Badia</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-35</strong></td>
<td style="text-align: left;"><strong>VERB</strong></td>
<td style="text-align: left;"><p>Verba: kata yang menyatakan perbuatan atau keadaan, termasuk <em>adong</em> ‘ada’.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Label mengikuti bentuk Batak Toba. <em>dibuat ibana</em> diterjemahkan ‘dia mengambil’ (aktif), tetapi <em>dibuat</em> tetap verba pasif.</p></td>
<td style="text-align: left;"><em>makan</em>, <em>dikirim</em>. <em>modom</em>, <em>manuhor</em>, <em>dibuat</em>, <em>adong</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-36</strong></td>
<td style="text-align: left;"><strong>ADJ</strong></td>
<td style="text-align: left;">Adjektiva (kata sifat). Tetap ADJ saat menjadi predikat. Numeralia tingkat juga ADJ.</td>
<td style="text-align: left;"><em>bagus</em>, <em>besar</em>. <em>uli</em>, <em>balga</em>, <em>denggan</em>, <em>parjolo</em> ‘pertama’.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-37</strong></td>
<td style="text-align: left;"><strong>ADV</strong></td>
<td style="text-align: left;">Adverbia: kata keterangan waktu, cara, kepastian, termasuk auxiliari predikator seperti <em>laos</em>.</td>
<td style="text-align: left;"><em>nanti</em>, <em>selalu</em>, <em>mungkin</em>. <em>annon</em>, <em>tongtong</em>, <em>ra</em>, <em>laos</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-38</strong></td>
<td style="text-align: left;"><strong>INTJ</strong></td>
<td style="text-align: left;">Interjeksi: seruan atau sapaan yang berdiri sendiri.</td>
<td style="text-align: left;"><em>wah</em>, <em>halo</em>. <em>horas</em>, <em>bohai</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-39</strong></td>
<td style="text-align: left;"><strong>PRON</strong></td>
<td style="text-align: left;">Pronomina: kata ganti orang, kata tanya, dan demonstratif yang berdiri sendiri sebagai argumen.</td>
<td style="text-align: left;"><em>dia</em>, <em>apa</em>, <em>ini</em> dalam <em>Ini apa?</em>. <em>ibana</em>, <em>aha</em>, <em>on</em> dalam <em>Aha do on?</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-40</strong></td>
<td style="text-align: left;"><strong>DET</strong></td>
<td style="text-align: left;"><p>Determiner: kata yang mewatasi nomina, seperti demonstratif sesudah nomina dan penanda jamak.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Dalam bahasa Indonesia <em>si</em> hanya sapaan akrab. Di pedoman ini <em>si</em> sebelum nama orang selalu DET.</p></td>
<td style="text-align: left;"><em>itu</em> dalam <em>rumah itu</em>, <em>para</em> dalam <em>para guru</em>. <em>i</em> dalam <em>buku i</em>, <em>angka</em>, <em>si</em> sebelum nama orang.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-41</strong></td>
<td style="text-align: left;"><strong>NUM</strong></td>
<td style="text-align: left;">Numeralia pokok. Numeralia tingkat diberi ADJ.</td>
<td style="text-align: left;"><em>dua</em>, <em>sepuluh</em>. <em>sada</em>, <em>dua</em>, <em>sappulu</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-42</strong></td>
<td style="text-align: left;"><strong>pro-bentuk</strong></td>
<td style="text-align: left;">Kata pengganti untuk satu jenis unsur, seperti pronomina menggantikan nomina. Nababan membedakan pro-verba, pro-adjektiva, pro-adjung, dan pro-klausa. UPOS-nya mengikuti unsur yang diganti.</td>
<td style="text-align: left;"><em>di sini</em>, <em>bagaimana</em>, <em>ya</em>. <em>marhua</em> VERB, <em>beha</em> ADJ, <em>dison</em> ADV, <em>olo</em> INTJ, <em>jadi</em> ADV.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-43</strong></td>
<td style="text-align: left;"><strong>ADP</strong></td>
<td style="text-align: left;"><p>Preposisi: kata depan yang menandai nomina sesudahnya. Relasinya case (I-52).</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> <em>ni</em> tidak punya padanan kata depan Indonesia. <em>tarup ni jabu</em> = <em>atap rumah</em>, tanpa kata depan.</p></td>
<td style="text-align: left;"><em>di</em>, <em>ke</em>, <em>dari</em>. <em>di</em>, <em>tu</em>, <em>sian</em>, <em>ni</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-44</strong></td>
<td style="text-align: left;"><strong>SCONJ</strong></td>
<td style="text-align: left;">Konjungsi subordinatif: kata yang membuka klausa bawahan (anak kalimat).</td>
<td style="text-align: left;"><em>kalau</em>, <em>karena</em>, <em>bahwa</em>. <em>molo</em>, <em>ala</em>, <em>ia</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-45</strong></td>
<td style="text-align: left;"><strong>PART</strong></td>
<td style="text-align: left;"><p>Partikel: kata fungsi kecil yang bukan preposisi dan bukan konjungsi. Di pedoman ini meliputi partikel modal <em>do, ma, pe</em>, negasi, penanda <em>na</em>, dan partikel sikap.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> <em>-lah</em> menempel pada kata, sedangkan <em>ma</em> dan <em>do</em> adalah token sendiri.</p></td>
<td style="text-align: left;"><em>-lah</em>, <em>-kah</em>, <em>tidak</em>. <em>do</em>, <em>ma</em>, <em>dang</em>, <em>na</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-46</strong></td>
<td style="text-align: left;"><strong>CCONJ</strong></td>
<td style="text-align: left;">Konektor (konjungsi koordinatif): kata yang menghubungkan unsur setara.</td>
<td style="text-align: left;"><em>dan</em>, <em>tetapi</em>, <em>lalu</em>. <em>jala</em>, <em>alai</em>, <em>dungi</em>, <em>dohot</em> ‘dan’.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-47</strong></td>
<td style="text-align: left;"><strong>AUX</strong></td>
<td style="text-align: left;"><p>Auxiliari predikator modal: kata bantu di depan predikator yang menyatakan kehendak, keharusan, atau kemampuan.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> <em>menjadi</em> biasa dianggap verba. Di pedoman ini <em>gabe</em> diberi AUX bila mendahului predikator lain.</p></td>
<td style="text-align: left;"><em>hendak</em>, <em>harus</em>, <em>bisa</em>. <em>naeng</em>, <em>ingkon</em>, <em>boi</em>, <em>gabe</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-48</strong></td>
<td style="text-align: left;"><strong>PUNCT</strong></td>
<td style="text-align: left;">Tanda baca. Relasinya selalu punct (I-86).</td>
<td style="text-align: left;">. , ? ! dan tanda petik.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-49</strong></td>
<td style="text-align: left;"><strong>SYM</strong></td>
<td style="text-align: left;">Simbol yang bukan tanda baca.</td>
<td style="text-align: left;">%, Rp, +.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-50</strong></td>
<td style="text-align: left;"><strong>X dan Foreign=Yes</strong></td>
<td style="text-align: left;">X untuk kata yang kelasnya tidak dapat ditentukan, termasuk potongan kata goeswith. Kata asing yang fungsinya jelas diberi kelas menurut fungsinya dan Foreign=Yes (I-117).</td>
<td style="text-align: left;"><em>na</em> dalam <em>omak na</em> (I-30). Kata asing: <em>founder</em>, <em>coding</em>.</td>
</tr>
</tbody>
</table>

Nababan membagi kata menjadi kata isi *(contentives)* dan kata fungsi *(functors)* (§4.1). Tabel 5.1 memetakan pembagian itu ke 17 UPOS. Tabel 5.2 memuat daftar kata fungsi yang paling sering muncul.

| **Kelas Nababan (§)** | **UPOS** | **Contoh dan catatan** |
|:---|:---|:---|
| Nomina umum (§4.3.1) | NOUN | jabu, dengke, jolma, hata, ari |
| Nomina diri orang, tempat, marga, tekonim (§4.3.1) | PROPN | Butet, Samosir, Sitorus, Nai Badia. Marga berawalan si- (Sihombing) tetap satu PROPN |
| Verba taktransitif, transitif, resiprokal (§4.3.2) | VERB | modom, mardalan, manuhor, dibuat, masijouan, adong ‘ada’ |
| Adjektiva (§4.3.3) | ADJ | denggan, balga, uli, timbo. Tetap ADJ saat menjadi predikat |
| Adjung waktu, adverbia, adjung klausa (§4.3.4) | ADV | annon, tongtong, nattoari, ra ‘mungkin’, tottu ‘pasti’ |
| Interjeksi (§4.3.5) | INTJ | horas, beta, bohai, ale (seruan sapaan) |
| Pronomina persona (§4.4.1.1) | PRON | ahu/au, ho, ibana, hami, hita, hamu, nasida, iba |
| Pronomina demonstratif sebagai argumen | PRON | *On* do ... ‘ini ...’, *i* ma ... saat berdiri sendiri |
| Demonstratif sebagai pewatas nomina | DET | jabu *on*, buku *i*, dolok *an* |
| Pronomina tanya (§4.4.1.1) | PRON | ise, aha, dia, sadia |
| Pronomina inklusif, partitif, taktentu | DET bila mewatasi nomina, PRON bila berdiri sendiri | sude, deba, saotik, si anu |
| Numeralia pokok (§4.4.1.1) | NUM | sada, dua, sappulu, ratus |
| Numeralia tingkat (§4.2.6) | ADJ | paduahon, parjolo, paitolu |
| Pro-verba (§4.4.1.2) | VERB | marhua, mahua |
| Pro-adjektiva (§4.4.1.3) | ADJ | beha |
| Pro-adjung (§4.4.1.4) | ADV | dison, disi, tusi, tusan, andigan, nandigan |
| Pro-klausa (§4.4.1.5) | INTJ untuk olo, daong. ADV untuk boasa, jadi, asa, ipe, attong | Jadi ... ‘maka ...’ di awal klausa |
| Preposisi (§4.4.2.1) | ADP | di, tu, sian, dohot ‘dengan’, marhite, songon, gabe, ala ni, ni |
| Konjungsi subordinatif (§4.4.2.2) | SCONJ | molo, anggo, aut, nang, agia, tikki, dung, paima, asa, ala, ai, sotung, manang ‘apakah’, ia ‘bahwa’ |
| Penanda atributif na (§4.4.2.1.3) | PART | halak *na* roa, jabu *na* di huta |
| Partikel modal predikatif (§4.4.3.1) | PART | do, ma, pe, dope |
| Negasi (§4.4.3.1, §4.4.3.2) | PART | dang, ndang, ndada, dada, so, unang, sotung (larangan) |
| Partikel kompletif (§4.4.3.1) | ADV | nunga ‘sudah’, naung, dung (kompletif) |
| Partikel imperatif (§4.4.3.2) | PART | jolo, ma, nanggo |
| Konektor (§4.4.4) | CCONJ | dungi, alai, hape, jala, huhut, manang ‘atau’, dohot ‘dan’ |
| Auxiliari predikator modal (§4.4.5.1) | AUX | naeng, ingkon/ikkon, boi, gabe (bila mendahului predikator lain) |
| Auxiliari predikator lain (§4.4.5.1) | ADV | pittor, sor, sai, be, muse, hian, tar ‘pura-pura’, laos ‘lalu, lantas, segera’ |
| Auxiliari nomina (§4.4.5.2) | DET | angka/akka (jamak), nasa, ganup. Partikel si sebelum nama orang juga DET |
| Auxiliari nomina holan, apala | ADV | holan ‘hanya’, apala ‘benar-benar’ |
| Auxiliari adjektiva (§4.4.5.3) | ADV | mansai/matcai, sahali, situtu, tung, lobi, lam, hian |
| Auxiliari numeralia (§4.4.5.5.1) | ADV | nari, nanggo, hirahira |
| Partikel sikap penutur (§4.4.5.7) | PART | tung ... do, ua, tahe, nian, maon, attong |
| Tanda baca | PUNCT | . , ? ! " “ ” |
| Simbol | SYM | %, Rp, + (jarang dalam 250 kalimat) |
| Kata asing tak terserap | Menurut fungsinya, dengan Foreign=Yes | founder, twist, coding. Bila fungsinya tidak jelas, X |

*Tabel 5.1. Pemetaan kelas kata Nababan ke UPOS.*

### 5.1 Kasus kelas kata yang sering membingungkan

**Daftar istilah Bagian 5.1**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah dan label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-43</em></td>
<td style="text-align: left;">ADP</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>di</em>, <em>ni</em>, dan <em>dohot</em> ‘dengan’ diberi ADP.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-46</em></td>
<td style="text-align: left;">CCONJ</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>dohot</em> ‘dan’ dan <em>dungi</em> diberi CCONJ.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-51</strong></td>
<td style="text-align: left;"><strong>cc</strong></td>
<td style="text-align: left;">Relasi untuk konektor. Konektor menunjuk ke unsur setara yang mengikutinya.</td>
<td style="text-align: left;">Dalam <em>rumah dan sawah</em>, <em>dan</em> menunjuk ke <em>sawah</em>. <em>jabu dohot hauma</em> → <em>dohot</em> cc ke <em>hauma</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-52</strong></td>
<td style="text-align: left;"><strong>case</strong></td>
<td style="text-align: left;"><p>Relasi untuk preposisi. Preposisi menunjuk ke nomina yang ditandainya, bukan ke verba.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Tata bahasa sekolah menganggap <em>di rumah</em> satu keterangan. Dalam UD, nomina <em>jabu</em> menjadi intinya, dan <em>di</em> bergantung padanya.</p></td>
<td style="text-align: left;">Dalam <em>di rumah</em>, <em>di</em> menunjuk ke <em>rumah</em>. <em>di jabu</em> → <em>di</em> case ke <em>jabu</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-53</strong></td>
<td style="text-align: left;"><strong>discourse</strong></td>
<td style="text-align: left;">Relasi untuk partikel modal (<em>do, ma, pe</em>) dan interjeksi di dalam kalimat. Menunjuk ke predikator.</td>
<td style="text-align: left;"><em>-lah</em> dalam <em>Pergilah</em>. <em>ma</em> dalam <em>Ditongos nasida ma hepeng i</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-54</strong></td>
<td style="text-align: left;"><strong>mark</strong></td>
<td style="text-align: left;">Relasi untuk penanda klausa (konjungsi subordinatif, <em>laho</em> ‘untuk’) dan penanda <em>na</em>. Menunjuk ke predikator atau pewatas yang ditandainya.</td>
<td style="text-align: left;">Dalam <em>kalau dia datang</em>, <em>kalau</em> menunjuk ke <em>datang</em>. <em>molo ro ibana</em> → <em>molo</em> mark ke <em>ro</em>. <em>halak na roa</em> → <em>na</em> mark ke <em>roa</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-55</strong></td>
<td style="text-align: left;"><strong>advmod</strong></td>
<td style="text-align: left;">Relasi untuk adverbia dan negasi yang menerangkan predikator.</td>
<td style="text-align: left;"><em>tidak</em> dalam <em>tidak datang</em>. <em>dang</em>, <em>laos</em>, <em>annon</em> diberi advmod.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-64</em></td>
<td style="text-align: left;">nsubj</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Subjek. Dijelaskan lengkap di Bagian 6.2 (dipakai pada butir <em>adong</em>).</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-101</em></td>
<td style="text-align: left;">conj</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Unsur atau klausa setara. Dijelaskan lengkap di Bagian 6.7 (dipakai pada butir <em>laos</em>).</td>
</tr>
</tbody>
</table>

1.  ***dohot*.** Bila menghubungkan dua unsur setara (*jabu dohot hauma* ‘rumah dan sawah’), ditulis CCONJ dengan relasi cc. Bila menandai alat atau penyerta (*dilitsing ibana dohot balobas* ‘dipukul dengan penggaris’), ditulis ADP dengan relasi case.

2.  ***di*.** Biasanya ditulis ADP lokatif *‘di’*. Dalam *manukkun ma au di ho* ‘aku bertanya kepadamu’, *di* menandai sasaran yang tidak langsung mengikuti verba (§4.4.2.1.5) dan tetap ADP. Jangan tertukar dengan prefiks *di-* yang menempel pada verba.

3.  ***ni*.** Selalu ditulis ADP. Setelah nomina, *ni* menandai pemilik (*tarup ni jabu*). Setelah verba kompletif atau promisif, *ni* menandai aktor (*tuhoron ni si Ondo*) (§4.4.2.1.4).

4.  ***ma*.** Setelah predikator dalam kalimat berita, PART naratif (discourse). Dalam kalimat perintah, PART imperatif santun (discourse). Dalam *i ma* ‘itulah, yaitu’, tetap PART discourse.

5.  ***i*.** Sebagai pewatas nomina (*buku i*) DET. Berdiri sendiri sebagai argumen (*dang hubotoi*, *i ma* ...) PRON. Sebagai bagian dari ma i, songon i, ala ni i, tetap PRON.

6.  ***gabe*.** Sebelum predikator lain (*gabe guru do ibana* ‘ia menjadi guru’), AUX. Sebagai preposisi ‘sebagai, untuk’ (*ditodo nasida gabe kapala*), ADP. Bila menjadi satu-satunya predikat verbal, VERB.

7.  ***godang*.** Sebagai predikat (*Godang do jolma na ...* ‘banyak orang yang ...’), ADJ. Sebelum nomina tanpa na, DET.

8.  ***laho*.** Bila bermakna ‘pergi’, VERB. Bila mengantar klausa tujuan ‘untuk’ sebelum verba (*laho mangalehon barita*), SCONJ dengan relasi mark. Tandai Ragu=Ya bila tidak jelas.

9.  ***adong*.** VERB eksistensial ‘ada’. Hal yang ada menjadi nsubj.

10. **laos.** Selalu ADV dengan relasi advmod ke predikator klausanya, baik berarti ‘lalu’ maupun ‘lantas, segera’. *laos* berperilaku seperti auxiliari predikator *pittor* ‘segera’ (§4.4.5.1) dan dapat muncul bersama konektor yang sebenarnya, sehingga bukan konektor. Contoh: *Dungi, laos terpodom ma ibana di jolo jabu i* ‘kemudian, segera tertidurlah dia di depan rumah itu’ → *dungi* CCONJ cc ke *terpodom*, *laos* ADV advmod ke *terpodom*. Bila *laos* menjadi satu-satunya penghubung dua klausa (*masuk ma ibana tu bilut, laos modom ma ibana*), klausa kedua tetap conj tanpa token cc (§5.3).

## 6. Relasi Dependensi

### 6.1 Akar kalimat: predikator

**Daftar istilah Bagian 6.1**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>I-56</strong></td>
<td style="text-align: left;"><strong>root</strong></td>
<td style="text-align: left;">Relasi untuk predikator utama kalimat. Satu kalimat punya tepat satu root, dan HEAD-nya 0.</td>
<td style="text-align: left;">Dalam <em>Adik tidur</em>, <em>tidur</em> adalah root. <em>Modom do ibana.</em> → <em>modom</em> root.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-57</strong></td>
<td style="text-align: left;"><strong>predikator</strong></td>
<td style="text-align: left;"><p>Inti klausa menurut Nababan, yaitu unsur yang menyatakan apa yang dikatakan tentang subjek. Predikator bisa verba atau bukan verba.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Sama dengan predikat (P) dalam tata bahasa sekolah.</p></td>
<td style="text-align: left;"><em>tidur</em>, <em>guru</em> dalam <em>Ayahnya guru</em>. <em>modom</em>, <em>guru</em> dalam <em>Guru do amana</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-58</strong></td>
<td style="text-align: left;"><strong>klausa</strong></td>
<td style="text-align: left;">Satuan yang punya satu predikator beserta subjek dan unsur lain yang menyertainya. Kalimat bisa terdiri atas satu klausa atau lebih.</td>
<td style="text-align: left;"><em>Ia diundang mereka, tetapi ia tidak datang</em> = dua klausa. <em>dipio nasida do ibana, alai dang ro ibana</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-59</strong></td>
<td style="text-align: left;"><strong>kopula dan predikat nonverbal</strong></td>
<td style="text-align: left;"><p>Kopula adalah kata penghubung seperti <em>adalah</em>. Batak Toba tidak memakainya, sehingga nomina, adjektiva, numeralia, atau frasa preposisi langsung menjadi predikator dan root.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Bila terjemahan memakai <em>adalah</em>, jangan mencari token kopula. Relasi cop tidak dipakai.</p></td>
<td style="text-align: left;"><em>Ayahnya (adalah) guru</em>. <em>Guru do amana</em> → <em>guru</em> root. <em>Tolu do hodana</em> → <em>tolu</em> root.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-60</strong></td>
<td style="text-align: left;"><strong>komplemen (C)</strong></td>
<td style="text-align: left;">Unsur yang melengkapi predikator selain subjek, misalnya objek (Nababan §5.2.1.1).</td>
<td style="text-align: left;"><em>ikan</em> dalam <em>Si Polan makan ikan</em>. <em>dengke</em> dalam <em>Mangallang dengke do si Polan</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-61</strong></td>
<td style="text-align: left;"><strong>urutan langsung</strong></td>
<td style="text-align: left;"><p>Urutan dasar klausa Batak Toba: predikator, partikel modal bila ada, subjek, lalu komplemen (P ± Mp + S ± C).</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Dalam bahasa Indonesia subjek biasanya di depan. Dalam Batak Toba kata pertama sering predikator, bukan subjek.</p></td>
<td style="text-align: left;"><em>Modom</em> (P) <em>do</em> (Mp) <em>ibana</em> (S). Dalam bahasa Indonesia: <em>Dia</em> (S) <em>tidur</em> (P).</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-62</strong></td>
<td style="text-align: left;"><strong>klausa ekuasional</strong></td>
<td style="text-align: left;">Klausa nomina-nomina yang menyamakan dua hal. Unsur sebelum <em>do</em> adalah predikator. Dalam kalimat tanya, pronomina tanya menjadi predikator.</td>
<td style="text-align: left;"><em>Ini apa?</em> = <em>Aha do on?</em> → <em>aha</em> root, <em>on</em> nsubj.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-63</strong></td>
<td style="text-align: left;"><strong>aux</strong></td>
<td style="text-align: left;">Relasi untuk auxiliari (AUX). Auxiliari menunjuk ke predikator yang dibantunya dan tidak pernah menjadi root.</td>
<td style="text-align: left;"><em>hendak</em> dalam <em>Ia hendak tidur</em>. <em>Naeng modom do ibana</em> → <em>naeng</em> aux ke <em>modom</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-10</em></td>
<td style="text-align: left;">HEAD</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Predikator utama diberi HEAD 0.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-45</em></td>
<td style="text-align: left;">PART</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Partikel modal (Mp) <em>do, ma, pe</em> diberi PART.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-52</em></td>
<td style="text-align: left;">case</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>di</em> dalam <em>Di bilut do nasida</em> diberi case ke <em>bilut</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-55</em></td>
<td style="text-align: left;">advmod</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Adjektiva atau adverbia sebelum verba (butir 4) diberi advmod.</td>
</tr>
</tbody>
</table>

Nababan menganalisis klausa sebagai konstruksi predikatif yang terdiri atas predikator (P), partikel modal (Mp) bila ada, subjek (S), dan komplemen (C). Urutan langsungnya P ± Mp + S ± C (§5.2.1.1). Predikator menjadi root.

1.  **Predikator verbal** (§5.1.2.2.1): verba menjadi root. *Modom do ibana.* ‘Dia tidur.’ → modom root.

2.  **Predikator nonverbal tanpa kopula** (§5.1.2.2.2): nomina, adjektiva, numeralia, frasa preposisi, atau pro-adjung menjadi root. *Guru do ibana.* → guru root. *Tolu do hodana.* → tolu root. *Di bilut do nasida.* → bilut root, di case.

3.  **Klausa ekuasional nomina-nomina** (§5.2.1.2): dalam urutan langsung, unsur sebelum partikel do adalah predikator dan unsur sesudahnya subjek. Pada kalimat tanya dengan pronomina tanya, pronomina tanya itulah predikator: *Aha do on?* → aha root, on nsubj.

4.  **Adjektiva atau adverbia di posisi predikator sebelum verba.** Nababan menyebut *hatop* dalam *hatop do ibana mardalan* ‘dia berjalan cepat’ sebagai predikator (§5.2.1.1). Dalam UD, inti klausa adalah predikat isi. Pedoman ini memakai verba sebagai root dan adjektiva atau adverbia sebagai advmod. Keputusan ini diuji pada pilot dan dicatat sebagai isu terbuka.

5.  **Auxiliari tidak menjadi root.** *Naeng modom do ibana.* → modom root, naeng aux.

### 6.2 Subjek

**Daftar istilah Bagian 6.2**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-57</em></td>
<td style="text-align: left;">predikator</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Subjek menunjuk ke predikator klausanya.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-64</strong></td>
<td style="text-align: left;"><strong>nsubj</strong></td>
<td style="text-align: left;"><p>Relasi untuk subjek berupa kata atau frasa, termasuk subjek klausa pasif.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> UD bahasa Indonesia memakai nsubj:pass untuk subjek pasif. Pedoman ini tetap memakai nsubj.</p></td>
<td style="text-align: left;">Dalam <em>Uang itu dikirim mereka</em>, subjeknya <em>uang itu</em>. <em>Ditongos nasida ma hepeng i</em> → <em>hepeng</em> nsubj.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-65</strong></td>
<td style="text-align: left;"><strong>csubj</strong></td>
<td style="text-align: left;">Relasi untuk subjek berupa klausa.</td>
<td style="text-align: left;"><em>Bernyanyi dimulai oleh mereka</em>. <em>dimulai nasida ma marende</em> → <em>marende</em> csubj.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-66</strong></td>
<td style="text-align: left;"><strong>urutan terbalik emfatik</strong></td>
<td style="text-align: left;">Urutan dengan subjek di depan untuk memberi penekanan. Relasi tidak berubah.</td>
<td style="text-align: left;"><em>Dialah yang berpesta tadi malam</em>. <em>Ibana do marpesta nattoari</em> → <em>marpesta</em> root, <em>ibana</em> nsubj.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-67</strong></td>
<td style="text-align: left;"><strong>subjek lesap</strong></td>
<td style="text-align: left;">Subjek yang tidak ditulis tetapi dipahami. Tidak ditambahkan sebagai token.</td>
<td style="text-align: left;"><em>(Kamu) belilah buku itu</em>. <em>Tuhor ma buku i</em>: subjek ‘kamu’ tidak tertulis.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-61</em></td>
<td style="text-align: left;">urutan langsung</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Dalam urutan langsung subjek berada sesudah predikator dan partikel.</td>
</tr>
</tbody>
</table>

1.  Subjek klausa diberi **nsubj**, termasuk subjek klausa pasif. *Ditongos nasida ma hepeng i.* → hepeng nsubj.

2.  Subjek berupa klausa diberi **csubj**. Nababan mencatat predikator agentif dengan subjek verba (§5.1.2.2.1 butir 2): *dimulai nasida ma marende* ‘bernyanyi dimulai oleh mereka’ → marende csubj.

3.  Pada urutan terbalik emfatik (§5.2.1.2), relasi tidak berubah walaupun subjek berada di depan. *Ibana do marpesta nattoari.* → marpesta tetap root, ibana nsubj.

4.  Subjek yang dilesapkan tidak ditambahkan sebagai token.

### 6.3 Diatesis: aktif, pasif, dan resiprokal

**Daftar istilah Bagian 6.3**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-23</em></td>
<td style="text-align: left;">diatesis</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat, dibahas lebih rinci di sini:</strong> Bagian ini membahas diatesis secara rinci. Bentuk verba menentukan siapa pelaku dan siapa sasaran, lalu Tabel 6.1 menentukan FEATS dan relasinya.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-68</strong></td>
<td style="text-align: left;"><strong>aktif</strong></td>
<td style="text-align: left;">Bentuk verba dengan pelaku sebagai subjek. Prefiks <em>maN-</em>, <em>um-</em>, <em>masi-</em>. Dicatat Voice=Act.</td>
<td style="text-align: left;"><em>Ia membeli buku</em>. <em>manuhor buku</em>, <em>manuan eme do inatta</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-69</strong></td>
<td style="text-align: left;"><strong>pasif</strong></td>
<td style="text-align: left;"><p>Bentuk verba dengan sasaran sebagai subjek. Prefiks <em>di-</em>, <em>hu-</em>, <em>ta-</em>, <em>tar-</em>, sisipan <em>-in-</em>, akhiran <em>-on</em>. Dicatat Voice=Pass.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Terjemahan Indonesia sering aktif (<em>Dang huida ibana</em> ‘aku tidak melihatnya’), tetapi label mengikuti bentuk Batak Toba: <em>huida</em> tetap pasif.</p></td>
<td style="text-align: left;"><em>Buku dibeli</em>. <em>ditongos</em>, <em>hujou</em>, <em>tuhoron</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-70</strong></td>
<td style="text-align: left;"><strong>resiprokal</strong></td>
<td style="text-align: left;">Bentuk verba berbalasan (saling). <em>masi-...-an</em>. Dicatat Voice=Rcp.</td>
<td style="text-align: left;"><em>saling memanggil</em> = <em>masijouan nasida</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-71</strong></td>
<td style="text-align: left;"><strong>pelaku (aktor) dan sasaran</strong></td>
<td style="text-align: left;">Pelaku adalah pihak yang berbuat. Sasaran adalah pihak yang dikenai perbuatan. Keduanya peran makna, bukan relasi. Relasinya bergantung pada diatesis.</td>
<td style="text-align: left;">Dalam <em>Mereka mengirim uang</em>, pelakunya <em>mereka</em> dan sasarannya <em>uang</em>. <em>Ditongos nasida ma hepeng i</em>: pelaku <em>nasida</em>, sasaran <em>hepeng</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-72</strong></td>
<td style="text-align: left;"><strong>konstituen agentif dan objektif</strong></td>
<td style="text-align: left;">Istilah Nababan (§5.1.2.1.2). Verba pasif dan aktornya membentuk konstituen agentif. Verba aktif dan objeknya membentuk konstituen objektif.</td>
<td style="text-align: left;"><em>hujou hami</em> (agentif), <em>manuhor buku</em> (objektif).</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-73</strong></td>
<td style="text-align: left;"><strong>obj:agent dan obl:agent</strong></td>
<td style="text-align: left;"><p>obj:agent untuk aktor pasif yang langsung mengikuti verba tanpa penanda. obl:agent untuk aktor yang ditandai <em>ni</em>, dengan <em>ni</em> sebagai case.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Pelaku pasif bahasa Indonesia biasanya ditandai <em>oleh</em>. Aktor Batak Toba langsung mengikuti verba tanpa kata depan, sehingga relasinya obj:agent, bukan obl.</p></td>
<td style="text-align: left;"><em>Ia dipanggil oleh kami</em>. <em>Hujou hami do ibana</em> → <em>hami</em> obj:agent. <em>Tuhoron ni si Ondo do i</em> → <em>Ondo</em> obl:agent, <em>ni</em> case.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-09</em></td>
<td style="text-align: left;">FEATS</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Voice, Aspect, dan Mood pada Tabel 6.1 dijelaskan di Bagian 7.1.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-24, I-25, I-26</em></td>
<td style="text-align: left;">kompletif, promisif, potensial</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Tiga bentuk verba yang menambah Aspect atau Mood.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-64</em></td>
<td style="text-align: left;">nsubj</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Subjek klausa pasif tetap nsubj.</td>
</tr>
</tbody>
</table>

Verba transitif Batak Toba berinfleksi aktif (maN- dan seterusnya), pasif (di- dan seterusnya), atau resiprokal (masi-...-an) (§4.2.3.1). Tabel 6.1 memetakan setiap bentuk ke label UD.

| **Bentuk verba (§)** | **Contoh** | **FEATS verba** | **Pelaku** | **Sasaran** |
|----|----|----|----|----|
| Aktif sederhana maN- (§4.2.4.1) | *manuhor buku* | Voice=Act | nsubj | obj |
| Aktif kompletif um- (§4.2.4.1) | *jumou dongan* | Aspect=Perf\|Voice=Act | nsubj | obj |
| Aktif distributif masi- (§4.2.4.1) | *masigarar utangna* | Voice=Act | nsubj | obj |
| Imperatif tanpa afiks (§4.2.4.1) | *buat i* | Mood=Imp | nsubj bila ada | obj |
| Pasif sederhana di- (§4.2.4.2) | *dibuat halak i* | Voice=Pass | obj:agent (langsung setelah verba) | nsubj |
| Pasif sederhana hu- (aktor ‘aku/kami’) | *hubuat, hubuat hami* | Voice=Pass dan MISC Aktor=1Eks | obj:agent bila ada kata aktor | nsubj |
| Pasif sederhana ta- (aktor ‘kita’) | *tabuat* | Voice=Pass dan MISC Aktor=1Ink | tanpa token aktor | nsubj |
| Pasif kompletif -in-/ni- (§4.2.4.2) | *binuat ni halak i* | Aspect=Perf\|Voice=Pass | obl:agent dengan case ni | nsubj |
| Pasif promisif -on (§4.2.4.2) | *tuhoron ni si Ondo* | Aspect=Prosp\|Voice=Pass | obl:agent dengan case ni | nsubj |
| Pasif potensial tar- (§4.2.4.2) | *tarbuat ibana* | Mood=Pot\|Voice=Pass | obj:agent | nsubj |
| Resiprokal masi-...-an (§4.2.3.1) | *masijouan nasida* | Voice=Rcp | nsubj (para pelaku) | tidak ada |
| Taktransitif turunan mar-, maN-₁ (§4.6.4.1) | *mardalan, manortor* | tanpa Voice | nsubj | tidak ada |

*Tabel 6.1. Pemetaan bentuk verba ke fitur dan relasi.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>Mengapa aktor pasif diberi obj:agent</strong></p>
<ul>
<li><p>Nababan menganalisis verba pasif dan aktornya sebagai satu konstituen agentif, sejajar dengan verba aktif dan objeknya yang membentuk konstituen objektif (§5.1.2.1.2). Aktor itu ditempatkan langsung setelah verba tanpa preposisi (§4.2.2.2). Contoh: <em>hujou hami do ibana</em> ‘ia dipanggil oleh kami’, <em>ditongos nasida ma hepeng i</em> ‘uang itu dikirim oleh mereka’.</p></li>
<li><p>Karena aktor itu bagian inti dari konstituen verba dan tidak bertanda preposisi, relasinya obj:agent. Bila aktor ditandai ni (bentuk kompletif dan promisif), relasinya obl:agent dengan ni sebagai case, karena kehadiran penanda menjadikannya argumen bertanda.</p></li>
<li><p>Subjek klausa pasif tetap nsubj sesuai istilah Nababan, sedangkan Voice=Pass mencatat bentuk pasif pada verba.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 6.4 Objek dan komplemen

**Daftar istilah Bagian 6.4**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-60</em></td>
<td style="text-align: left;">komplemen (C)</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Bagian ini menentukan relasi untuk komplemen: obj, obl, xcomp, atau ccomp.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-74</strong></td>
<td style="text-align: left;"><strong>argumen inti</strong></td>
<td style="text-align: left;">Unsur yang dibutuhkan predikator tanpa penanda: subjek, objek, dan aktor pasif tak bertanda.</td>
<td style="text-align: left;">Dalam <em>Ia membeli buku</em>, <em>ia</em> dan <em>buku</em>. <em>ibana</em> dan <em>buku</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-75</strong></td>
<td style="text-align: left;"><strong>keterangan</strong></td>
<td style="text-align: left;">Unsur tambahan yang menyatakan tempat, waktu, cara, atau alat. Klausa tetap utuh bila keterangan dihilangkan.</td>
<td style="text-align: left;"><em>di rumah</em>, <em>tadi malam</em>. <em>di jabu</em>, <em>nattoari</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-76</strong></td>
<td style="text-align: left;"><strong>obj</strong></td>
<td style="text-align: left;">Relasi untuk sasaran verba aktif transitif yang tidak bertanda preposisi.</td>
<td style="text-align: left;"><em>padi</em> dalam <em>menanam padi</em>. <em>manuan eme do inatta</em> → <em>eme</em> obj.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-77</strong></td>
<td style="text-align: left;"><strong>obl</strong></td>
<td style="text-align: left;">Relasi untuk nomina bertanda preposisi dan nomina keterangan waktu tanpa preposisi.</td>
<td style="text-align: left;"><em>ke kampung</em>, <em>tadi malam</em>. <em>tu huta</em>, <em>sian Jerman</em>, <em>nattoari</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-78</strong></td>
<td style="text-align: left;"><strong>xcomp</strong></td>
<td style="text-align: left;">Relasi untuk verba kedua yang tidak punya subjek sendiri. Subjeknya dipahami dari argumen verba pertama.</td>
<td style="text-align: left;"><em>Ibunya menyuruh anaknya menikah</em>: <em>anaknya</em> yang menikah. <em>disuru inana ma anakna i mangoli</em> → <em>mangoli</em> xcomp ke <em>disuru</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-79</strong></td>
<td style="text-align: left;"><strong>kontrol (subjek terkendali)</strong></td>
<td style="text-align: left;">Keadaan ketika subjek verba kedua sama dengan salah satu argumen verba pertama dan tidak ditulis ulang. Kontrol menjadi ciri xcomp.</td>
<td style="text-align: left;">Pada contoh I-78, <em>anakna</em> adalah subjek <em>mangoli</em> walaupun tidak ditulis lagi.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-80</strong></td>
<td style="text-align: left;"><strong>ccomp</strong></td>
<td style="text-align: left;">Relasi untuk klausa pelengkap yang punya subjek sendiri, biasanya sesudah verba berkata, mengetahui, atau melihat.</td>
<td style="text-align: left;"><em>Aku tahu bahwa dia datang</em>. <em>huboto ia ro ibana</em> → <em>ro</em> ccomp, <em>ia</em> mark.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-52</em></td>
<td style="text-align: left;">case</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Preposisi pada obl diberi case ke nomina.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-42, I-55</em></td>
<td style="text-align: left;">pro-adjung, advmod</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>dison</em>, <em>annon</em>, <em>tongtong</em> diberi advmod.</td>
</tr>
</tbody>
</table>

1.  **obj** untuk sasaran verba aktif transitif yang tidak bertanda preposisi (§5.1.2.1.2 butir 2): *manuan eme do inatta* → eme obj.

2.  **obl** untuk argumen atau keterangan bertanda preposisi: *tu huta*, *di jabu*, *sian Jerman*, *dohot balobas*. Preposisinya diberi case pada nomina.

3.  **obl** juga untuk nomina keterangan waktu tanpa preposisi: *nattoari*, *sadari*, *di na sadari*.

4.  **advmod** untuk adverbia dan pro-adjung: *dison*, *annon*, *tongtong*.

5.  **xcomp** untuk verba kedua yang subjeknya dikendalikan argumen verba pertama: *disuru inana ma anakna i mangoli* → mangoli xcomp dari disuru.

6.  **ccomp** untuk klausa pelengkap, biasanya setelah ia ‘bahwa’ atau setelah verba berkata dan mengetahui: *huboto ia ro ibana* → ro ccomp, ia mark.

**Jembatan dari tata bahasa sekolah ke label UD**

Tabel berikut membantu anotator yang terbiasa dengan analisis S-P-O-Pel-K. Gunakan sebagai titik awal saja. Label akhir tetap ditentukan oleh bentuk Batak Toba dan aturan Bagian 6.

| **Fungsi (tata bahasa sekolah)** | **Contoh Indonesia** | **Label UD** | **Contoh Batak Toba** | **Catatan** |
|:---|:---|:---|:---|:---|
| **S (subjek)** | *Uang itu* dikirim mereka. | nsubj. csubj bila berupa klausa. | *hepeng* dalam *Ditongos nasida ma hepeng i* | Subjek pasif tetap nsubj. |
| **P (predikat)** | *tidur*, *guru*, *bagus* | root untuk klausa utama. Predikat klausa lain: conj, advcl, ccomp, xcomp, acl:relcl. | *modom*, *Guru do amana*, *Uli do jabu i* | Tanpa kopula (I-59). |
| **O (objek)** | Ia membeli *buku*. | obj | *eme* dalam *manuan eme do inatta* | Hanya pada verba aktif. |
| **Pelaku pasif (*oleh ...*)** | dikirim *oleh mereka* | obj:agent. obl:agent bila bertanda *ni*. | *ditongos nasida*, *tuhoron ni si Ondo* | Tidak ada kata depan seperti *oleh*. |
| **Pel (pelengkap)** | menjadi *guru*, menyuruh anaknya *menikah*, tahu *bahwa ia datang* | Bergantung bentuk: predikat nonverbal sebagai root, xcomp, atau ccomp. | *gabe guru do ibana* → *guru* root, *gabe* aux. *disuru ... mangoli* → xcomp. | Pel tidak punya satu label UD tunggal. |
| **K (keterangan)** | *di rumah*, *tadi malam*, *nanti*, *kalau dia datang* | obl (nomina), advmod (adverbia), advcl (klausa). | *di jabu*, *nattoari*, *annon*, *molo ro ibana* | Preposisi diberi case ke nomina. |
| **Kata tugas** | *dan*, *kalau*, *di*, *-lah* | cc, mark, case, discourse | *jala*, *molo*, *di*, *ma* | Bukan fungsi kalimat, tetapi tetap diberi relasi. |

*Jembatan S-P-O-Pel-K ke label UD (tidak bernomor agar nomor tabel lain tetap).*

### 6.5 Kata fungsi pada klausa

**Daftar istilah Bagian 6.5**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 41%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-45</em></td>
<td style="text-align: left;">PART</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat, dibahas lebih rinci di sini:</strong> Partikel modal dan negasi sama-sama PART, tetapi relasinya berbeda: partikel modal discourse (I-53), negasi advmod (I-55).</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-81</strong></td>
<td style="text-align: left;"><strong>partikel predikatif (partikel modal)</strong></td>
<td style="text-align: left;">Partikel sesudah predikator yang memberi nuansa penegasan atau urutan cerita: <em>do, ma, pe, dope</em>. Selalu PART discourse ke predikator.</td>
<td style="text-align: left;">Mirip <em>-lah</em> dan <em>pun</em>. <em>Modom do ibana</em>, <em>Ditongos nasida ma hepeng i</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-82</strong></td>
<td style="text-align: left;"><strong>negasi</strong></td>
<td style="text-align: left;">Kata penyangkal. Diberi PART dengan Polarity=Neg dan relasi advmod ke predikator yang disangkal.</td>
<td style="text-align: left;"><em>tidak</em>, <em>jangan</em>. <em>dang</em>, <em>ndang</em>, <em>unang</em>. <em>Dang huida ibana</em> → <em>dang</em> advmod ke <em>huida</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-83</strong></td>
<td style="text-align: left;"><strong>auxiliari predikator</strong></td>
<td style="text-align: left;">Kata seperti <em>pittor, sai, muse, hian, laos</em> yang menempel pada predikator untuk menyatakan cara atau urutan waktu. Diberi ADV advmod, berbeda dari auxiliari modal (AUX, I-47).</td>
<td style="text-align: left;"><em>segera</em>, <em>lalu</em>, <em>lagi</em>. <em>pittor</em>, <em>laos terpodom ma ibana</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-84</strong></td>
<td style="text-align: left;"><strong>klausa utama dan klausa bawahan</strong></td>
<td style="text-align: left;"><p>Klausa utama dapat berdiri sendiri dan memuat root. Klausa bawahan bergantung pada klausa lain dan biasanya diawali konjungsi subordinatif.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Tata bahasa sekolah menyebutnya induk kalimat dan anak kalimat.</p></td>
<td style="text-align: left;"><em>Belilah buku itu, kalau uangmu cukup</em>. <em>tuhor ma buku i, molo sae hepengmu</em>: klausa <em>molo ...</em> adalah klausa bawahan.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-85</strong></td>
<td style="text-align: left;"><strong>unsur setara</strong></td>
<td style="text-align: left;">Dua kata, frasa, atau klausa yang kedudukannya sama dan dapat dihubungkan konektor.</td>
<td style="text-align: left;"><em>rumah dan sawah</em>. <em>jabu dohot hauma</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-86</strong></td>
<td style="text-align: left;"><strong>punct</strong></td>
<td style="text-align: left;">Relasi untuk tanda baca. Tanda baca menunjuk ke predikator klausa terdekat.</td>
<td style="text-align: left;">Titik pada <em>Uli do jabu i.</em> → punct ke <em>uli</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-53, I-54, I-51</em></td>
<td style="text-align: left;">discourse, mark, cc</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Relasi untuk partikel modal, penanda klausa, dan konektor pada Tabel 6.2.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-63</em></td>
<td style="text-align: left;">aux</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>naeng, ingkon, boi, gabe</em> diberi aux.</td>
</tr>
</tbody>
</table>

| **Kata** | **UPOS** | **DEPREL** | **Induk** |
|----|----|----|----|
| *do, ma, pe, dope* | PART | discourse | predikator (root klausa) |
| *dang, ndang, ndada, so, unang, sotung* | PART | advmod | predikator yang dinegasikan |
| *nunga, naung, dung (kompletif)* | ADV | advmod | predikator |
| *naeng, ingkon, boi, gabe* | AUX | aux | predikator utama |
| *pittor, sai, muse, hian, sor, be, laos* | ADV | advmod | predikator |
| *molo, asa, ala, ai, dung, tikki, nang, laho (‘untuk’)* | SCONJ | mark | predikator klausa bawahan |
| *jala, alai, dungi, hape, manang, dohot (‘dan’)* | CCONJ | cc | unsur setara sesudahnya |
| *jadi, asa (‘maka’), ipe* | ADV | advmod | predikator klausa |
| tanda baca | PUNCT | punct | predikator klausa terdekat |

*Tabel 6.2. Kata fungsi pada tingkat klausa.*

### 6.6 Frasa nomina

**Daftar istilah Bagian 6.6**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 36%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>I-87</strong></td>
<td style="text-align: left;"><strong>frasa nomina</strong></td>
<td style="text-align: left;">Kelompok kata dengan nomina sebagai inti.</td>
<td style="text-align: left;"><em>rumah besar itu</em>. <em>buku i</em>, <em>jabu na di huta</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-88</strong></td>
<td style="text-align: left;"><strong>inti</strong></td>
<td style="text-align: left;">Kata utama dalam frasa. Kata lain dalam frasa menunjuk ke inti. Inti frasa nomina Batak Toba berada di depan.</td>
<td style="text-align: left;"><em>rumah</em> dalam <em>rumah besar</em>. <em>halak</em> dalam <em>halak na roa</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-89</strong></td>
<td style="text-align: left;"><strong>pewatas</strong></td>
<td style="text-align: left;">Kata atau frasa yang menerangkan inti.</td>
<td style="text-align: left;"><em>besar</em> dalam <em>rumah besar</em>. <em>roa</em> dalam <em>halak na roa</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-90</strong></td>
<td style="text-align: left;"><strong>compound</strong></td>
<td style="text-align: left;">Relasi untuk dua nomina yang membentuk satu satuan makna.</td>
<td style="text-align: left;"><em>kapal terbang</em>. <em>kapal habang</em> ‘pesawat’, <em>guru kapala</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-91</strong></td>
<td style="text-align: left;"><strong>nmod</strong></td>
<td style="text-align: left;">Relasi untuk nomina yang menerangkan nomina lain (bahan, asal, jenis), atau frasa preposisi pewatas nomina.</td>
<td style="text-align: left;"><em>periuk tanah</em>. <em>hudon tano</em>. <em>jabu na di huta</em> → <em>huta</em> nmod.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-92</strong></td>
<td style="text-align: left;"><strong>nmod:poss</strong></td>
<td style="text-align: left;"><p>Relasi untuk pemilik dalam frasa <em>ni</em>.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Bahasa Indonesia tidak memakai kata penanda pemilik. Dalam Batak Toba <em>ni</em> hadir dan tetap diberi ADP case.</p></td>
<td style="text-align: left;"><em>atap rumah</em> = <em>tarup ni jabu</em> → <em>jabu</em> nmod:poss, <em>ni</em> case.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-93</strong></td>
<td style="text-align: left;"><strong>amod</strong></td>
<td style="text-align: left;">Relasi untuk adjektiva pewatas nomina.</td>
<td style="text-align: left;"><em>orang jahat</em>. <em>halak na roa</em> → <em>roa</em> amod.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-94</strong></td>
<td style="text-align: left;"><strong>acl:relcl (klausa relatif)</strong></td>
<td style="text-align: left;">Relasi untuk klausa yang mewatasi nomina dan diantar <em>na</em>.</td>
<td style="text-align: left;"><em>orang yang membeli buku itu</em> = <em>halak na manuhor buku i</em> → <em>manuhor</em> acl:relcl.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-95</strong></td>
<td style="text-align: left;"><strong>det</strong></td>
<td style="text-align: left;">Relasi untuk determiner (DET).</td>
<td style="text-align: left;"><em>itu</em> dalam <em>buku itu</em>. <em>i</em> dalam <em>buku i</em>, <em>angka</em>, <em>si</em> sebelum nama orang.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-96</strong></td>
<td style="text-align: left;"><strong>nummod</strong></td>
<td style="text-align: left;">Relasi untuk numeralia yang mewatasi nomina.</td>
<td style="text-align: left;"><em>dua cangkir kopi</em> = <em>dua makkuk kopi</em> → <em>dua</em> nummod.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-97</strong></td>
<td style="text-align: left;"><strong>flat</strong></td>
<td style="text-align: left;">Relasi untuk nama yang terdiri atas beberapa kata. Kata pertama menjadi inti.</td>
<td style="text-align: left;"><em>Danau Toba</em>. <em>Mortua Rajadoli</em>, <em>Tao Toba</em>.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-98</strong></td>
<td style="text-align: left;"><strong>appos</strong></td>
<td style="text-align: left;">Relasi untuk aposisi, yaitu frasa nomina kedua yang menjelaskan frasa nomina pertama.</td>
<td style="text-align: left;"><em>si Pittor, anak Amadjaluk</em>. <em>si Pittor, anak ni Amadjaluk</em> → <em>anak</em> appos.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-99</strong></td>
<td style="text-align: left;"><strong>klausa relatif tanpa inti</strong></td>
<td style="text-align: left;">Frasa <em>na</em> tanpa nomina inti. Frasa itu mengambil relasi milik inti yang tidak hadir.</td>
<td style="text-align: left;"><em>yang hidup</em> = <em>na mangolu</em> → nsubj atau obj sesuai fungsinya, <em>na</em> tetap mark.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-20, I-54</em></td>
<td style="text-align: left;">na, mark</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>na</em> diberi PART mark ke pewatas yang ditandainya.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-52</em></td>
<td style="text-align: left;">case</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>ni</em> dan preposisi dalam frasa diberi case.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-40, I-41</em></td>
<td style="text-align: left;">DET, NUM</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Kelas kata untuk det dan nummod.</td>
</tr>
</tbody>
</table>

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

### 6.7 Koordinasi, kalimat majemuk setara, dan kalimat kompleks

**Daftar istilah Bagian 6.7**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 39%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Istilah &amp; label UD</strong></th>
<th><strong>Arti sederhana</strong></th>
<th><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>→ I-56</em></td>
<td>root</td>
<td colspan="2"><strong>Pengingat, dibahas lebih rinci di sini:</strong> Bagian ini memakai root berulang kali. Satu kalimat tetap punya satu root walaupun ada banyak predikator. Predikator lain menunjuk ke induknya dengan relasi pada Tabel 6.3.</td>
</tr>
<tr>
<td><strong>I-100</strong></td>
<td><strong>koordinasi</strong></td>
<td>Penggabungan unsur setara, dengan atau tanpa konektor. Unsur pertama menjadi inti.</td>
<td><em>rumah dan sawah</em>. <em>jabu dohot hauma</em>.</td>
</tr>
<tr>
<td><strong>I-101</strong></td>
<td><strong>conj</strong></td>
<td>Relasi untuk unsur setara kedua dan seterusnya. Unsur itu menunjuk ke unsur pertama. Juga dipakai untuk klausa setara.</td>
<td><em>Ia diundang mereka, tetapi ia tidak datang</em>. <em>dipio nasida do ibana, alai dang ro ibana</em> → <em>ro</em> conj ke <em>dipio</em>.</td>
</tr>
<tr>
<td><strong>I-102</strong></td>
<td><strong>kalimat tunggal, kalimat kompleks, kalimat majemuk setara</strong></td>
<td><p>Tiga jenis kalimat menurut Nababan (§5.3). Kalimat tunggal: satu klausa. Kalimat kompleks: klausa utama dan klausa bawahan. Kalimat majemuk setara: dua klausa setara atau lebih.</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> Tata bahasa sekolah menyebut kalimat kompleks sebagai kalimat majemuk bertingkat. Kalimat majemuk setara bernama sama.</p></td>
<td><em>Modom do ibana</em> (tunggal). <em>tuhor ma buku i, molo sae hepengmu</em> (kompleks). <em>dipio nasida do ibana, alai dang ro ibana</em> (majemuk setara).</td>
</tr>
<tr>
<td><strong>I-103</strong></td>
<td><strong>advcl</strong></td>
<td>Relasi untuk klausa keterangan waktu, syarat, sebab, atau tujuan.</td>
<td><em>Aku pergi kalau dia datang</em>. <em>lao do au, molo ro ibana</em> → <em>ro</em> advcl ke <em>lao</em>.</td>
</tr>
<tr>
<td><strong>I-104</strong></td>
<td><strong>parataxis dan umpasa</strong></td>
<td>parataxis untuk dua klausa yang dijajarkan tanpa konektor dalam pasangan berimbang umpasa (ungkapan berpantun Batak Toba). Klausa naratif tanpa konektor tetap conj.</td>
<td>Dua larik pantun yang dijajarkan. Pasangan berimbang dalam umpasa (§5.2.2.2).</td>
</tr>
<tr>
<td><em>→ I-51, I-54</em></td>
<td>cc, mark</td>
<td colspan="2"><strong>Pengingat:</strong> Konektor diberi cc, konjungsi subordinatif diberi mark, ke predikator klausa yang dibukanya.</td>
</tr>
<tr>
<td><em>→ I-78, I-80, I-94, I-65</em></td>
<td>xcomp, ccomp, acl:relcl, csubj</td>
<td colspan="2"><strong>Pengingat:</strong> Relasi lain untuk kalimat kompleks pada Tabel 6.3.</td>
</tr>
<tr>
<td><em>→ I-84</em></td>
<td>klausa utama dan klausa bawahan</td>
<td colspan="2"><strong>Pengingat:</strong> Klausa utama memuat root.</td>
</tr>
</tbody>
</table>

1.  Unsur setara pertama menjadi inti. Unsur berikutnya diberi **conj** ke unsur pertama. Konektor diberi **cc** ke unsur setara yang mengikutinya.

2.  Klausa yang digabung jala, alai, dungi, hape diberi conj ke klausa pertama.

3.  Pasangan berimbang dalam umpasa (§5.2.2.2) yang dijajarkan tanpa konektor diberi **parataxis** pada klausa kedua. Dua klausa naratif yang berurutan tanpa konektor tetap diberi **conj**, sesuai contoh kalimat majemuk setara Nababan *masuk ma ibana tu bilut, laos modom ma ibana* (§5.3).

4.  Klausa keterangan yang diawali konjungsi subordinatif diberi **advcl** ke predikator klausa utama, dan konjungsinya diberi mark.

Nababan (§5.3) membedakan tiga jenis kalimat. **Kalimat tunggal** terdiri atas satu klausa. **Kalimat kompleks** terdiri atas satu klausa utama dan klausa lain yang menerangkannya atau menjadi bagiannya (*tuhor ma buku i, molo sae hepengmu* ‘belilah buku itu, kalau uangmu cukup’). **Kalimat majemuk setara** terdiri atas dua klausa setara atau lebih (*dipio nasida do ibana, alai dang ro ibana* ‘ia diundang mereka, tetapi ia tidak datang’). Kalimat majemuk setara memakai relasi conj. Kalimat kompleks memakai advcl, ccomp, xcomp, acl:relcl, atau csubj. Aturan berikut berlaku untuk keduanya.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Prinsip kalimat majemuk setara dan kalimat kompleks</strong></p>
<ol type="1">
<li><p>Setiap kalimat hanya punya <strong>satu root</strong> (HEAD 0), yaitu predikator klausa utama. Predikator lain tidak pernah diberi root.</p></li>
<li><p>Setiap klausa punya predikator sendiri. Subjek, aktor, objek, keterangan, dan partikel klausa itu menunjuk ke <strong>predikator klausanya sendiri</strong>, bukan ke root.</p></li>
</ol>
<ol start="4" type="1">
<li><p>Predikator klausa lain menunjuk ke predikator yang menjadi induknya dengan salah satu relasi pada Tabel 6.3.</p></li>
<li><p>Kata penghubung menunjuk ke predikator klausa yang dibukanya: konektor (<em>jala</em>, <em>alai</em>, <em>dungi</em>, <em>hape</em>) dengan <strong>cc</strong>, konjungsi subordinatif (<em>molo</em>, <em>asa</em>, <em>ala</em>, <em>dung</em>, <em>ia</em>) dengan <strong>mark</strong>.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Langkah mengerjakan kalimat majemuk setara dan kalimat kompleks**

1.  Tandai semua predikator dalam kalimat, yaitu verba atau predikat nonverbal (Bagian 6.1).

2.  Tentukan klausa utama, biasanya klausa yang tidak diawali konjungsi subordinatif. Predikatornya diberi HEAD 0 dan DEPREL root.

3.  Untuk setiap predikator lain, pilih relasinya dari Tabel 6.3, lalu isi HEAD dengan ID predikator induknya.

4.  Kerjakan isi setiap klausa seperti kalimat tunggal: nsubj, obj, obj:agent, obl, advmod, discourse, semuanya ke predikator klausa itu.

5.  Pasang kata penghubung ke predikator klausa yang dibukanya.

6.  Periksa hasilnya: setiap kata di klausa kedua menunjuk ke predikator klausa kedua atau ke kata lain di dalam klausa itu. Bila ada yang menunjuk ke root, kemungkinan HEAD-nya salah.

| **Relasi** | **Kapan dipakai** | **Penanda** | **Contoh** |
|----|----|----|----|
| conj | Klausa setara dengan klausa induk | *jala, alai, dungi, hape, dohot* (cc) | *mengalu ... jala disuru* (Contoh 11) |
| xcomp | Verba kedua tanpa subjek sendiri, subjeknya dikendalikan argumen verba pertama | tanpa penanda | *disuru ... mangoli* (Contoh 10), *disuru ... lau* (Contoh 11) |
| ccomp | Klausa pelengkap dengan subjek sendiri, setelah verba berkata, mengetahui, melihat | *ia* ‘bahwa’ (mark) atau tanpa penanda | *huboto ia ro ibana* |
| advcl | Klausa keterangan waktu, syarat, sebab, atau tujuan | *molo, dung, ala, ai, asa, tikki, nang, laho* (mark) | *lao do au, molo ro ibana* |
| acl:relcl | Klausa yang mewatasi nomina | *na* (mark) | *halak na manuhor buku i* (Contoh 8) |
| csubj | Klausa yang menjadi subjek | tanpa penanda | *dimulai nasida ma marende* (Bagian 6.2) |
| parataxis | Pasangan berimbang umpasa tanpa konektor | tanpa penanda | pasangan berimbang dalam umpasa |

*Tabel 6.3. Relasi untuk predikator selain root.*

Contoh lengkap kalimat majemuk setara yg juga memuat pelengkap (xcomp) ada pada Contoh 11 (Bag. 8).

### 6.8 Relasi lain

**Daftar istilah Bagian 6.8**

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 43%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>I-105</strong></td>
<td style="text-align: left;"><strong>vocative</strong></td>
<td style="text-align: left;">Relasi untuk sapaan kepada lawan bicara.</td>
<td style="text-align: left;"><em>Bu, ...</em>. <em>inang</em>, <em>amang</em>, <em>Tuhan</em> dalam doa.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-106</strong></td>
<td style="text-align: left;"><strong>fixed</strong></td>
<td style="text-align: left;">Relasi untuk gabungan kata fungsi yang membeku dan bermakna sebagai satu kesatuan. Kata kedua menunjuk ke kata pertama.</td>
<td style="text-align: left;"><em>oleh karena</em>. <em>ala ni</em> ‘karena’, <em>taringot tu</em> ‘tentang’.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-107</strong></td>
<td style="text-align: left;"><strong>dep</strong></td>
<td style="text-align: left;">Relasi cadangan bila tidak ada relasi lain yang cocok. Wajib disertai Ragu=Ya.</td>
<td style="text-align: left;">Jarang dipakai.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-53</em></td>
<td style="text-align: left;">discourse</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Untuk partikel modal dan interjeksi.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-30</em></td>
<td style="text-align: left;">goeswith</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Untuk potongan kata yang salah dipisah.</td>
</tr>
</tbody>
</table>

| **Relasi** | **Dipakai untuk** | **Contoh** |
|----|----|----|
| vocative | sapaan | *inang*, *amang*, Tuhan dalam doa |
| discourse | partikel modal dan interjeksi dalam kalimat | *do, ma, pe, horas* |
| fixed | gabungan kata fungsi yang membeku | *ala ni* ‘karena’, *taringot* tu ‘tentang’: kata kedua fixed ke kata pertama |
| goeswith | bagian kata yang salah dipisah | *omak na* (Bagian 4.4) |
| dep | hanya bila tidak ada relasi lain yang cocok | wajib disertai Ragu=Ya |

*Tabel 6.4. Relasi lain yang dipakai.*

Daftar lengkap relasi yang diizinkan dalam pedoman ini ada di Lampiran A. Relasi di luar daftar itu tidak dipakai.

## 7. Fitur Morfologis (FEATS)

**Daftar istilah Bagian 7**

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 42%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><em>→ I-09</em></td>
<td style="text-align: left;">FEATS</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat, dibahas lebih rinci di sini:</strong> Bab ini menentukan isi FEATS. Tulis Nama=Nilai, pisahkan dengan |, urutkan alfabetis menurut nama fitur. Bila tidak ada fitur, isi _.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-108</strong></td>
<td style="text-align: left;"><strong>nama fitur dan nilai fitur</strong></td>
<td style="text-align: left;">Nama fitur adalah jenis keterangan (Voice, Number). Nilai fitur adalah isinya (Pass, Sing).</td>
<td style="text-align: left;"><em>ibana</em> → Number=Sing|Person=3|PronType=Prs: tiga fitur, urut N, P, P.</td>
</tr>
</tbody>
</table>

Pedoman ini memakai sekumpulan fitur minimal. Fitur ditulis Nama=Nilai, dipisah tanda \|, dan diurutkan alfabetis menurut nama fitur (huruf kapital dan kecil diabaikan). Bila tidak ada fitur, isi \_.

### 7.1 Verba

**Daftar istilah Bagian 7.1**

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 37%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>I-109</strong></td>
<td style="text-align: left;"><strong>Voice</strong></td>
<td style="text-align: left;">Fitur diatesis: Act (aktif), Pass (pasif), Rcp (resiprokal).</td>
<td style="text-align: left;"><em>manuhor</em> Voice=Act, <em>ditongos</em> Voice=Pass, <em>masijouan</em> Voice=Rcp.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-110</strong></td>
<td style="text-align: left;"><strong>Aspect</strong></td>
<td style="text-align: left;">Fitur aspek: Perf (kompletif), Prosp (promisif).</td>
<td style="text-align: left;"><em>binuat</em> Aspect=Perf|Voice=Pass, <em>tuhoron</em> Aspect=Prosp|Voice=Pass.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-111</strong></td>
<td style="text-align: left;"><strong>Mood</strong></td>
<td style="text-align: left;">Fitur modus: Imp (imperatif, perintah), Pot (potensial).</td>
<td style="text-align: left;"><em>Ambillah!</em> (perintah). <em>buat i</em> Mood=Imp, <em>tarbuat</em> Mood=Pot|Voice=Pass.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-68, I-69, I-70</em></td>
<td style="text-align: left;">aktif, pasif, resiprokal</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Dasar nilai Voice.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-24, I-25, I-26</em></td>
<td style="text-align: left;">kompletif, promisif, potensial</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Dasar nilai Aspect dan Mood.</td>
</tr>
</tbody>
</table>

| **Fitur** | **Nilai** | **Kapan dipakai**                                  |
|:----------|:----------|:---------------------------------------------------|
| Voice     | Act       | verba transitif aktif maN-, um-, masi-             |
| Voice     | Pass      | verba di-, hu-, ta-, -in-/ni-, -on, tar- potensial |
| Voice     | Rcp       | verba resiprokal masi-...-an                       |
| Aspect    | Perf      | bentuk kompletif um- dan -in-/ni-                  |
| Aspect    | Prosp     | bentuk promisif -on (‘akan di-’, ‘harus di-’)      |
| Mood      | Imp       | verba imperatif (perintah)                         |
| Mood      | Pot       | verba potensial tar- (‘dapat di-’)                 |

*Tabel 7.1. Fitur verba.*

### 7.2 Pronomina

**Daftar istilah Bagian 7.2**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 39%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>No.</strong></th>
<th style="text-align: left;"><strong>Istilah &amp; label UD</strong></th>
<th style="text-align: left;"><strong>Arti sederhana</strong></th>
<th style="text-align: left;"><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>I-112</strong></td>
<td style="text-align: left;"><strong>Person dan Number</strong></td>
<td style="text-align: left;"><p>Person: orang pertama (1), kedua (2), ketiga (3). Number: tunggal (Sing) atau jamak (Plur).</p>
<p><strong>Beda dengan bahasa Indonesia:</strong> <em>hamu</em> dan <em>nasida</em> juga dipakai sebagai sapaan hormat untuk satu orang, tetapi tetap Number=Plur.</p></td>
<td style="text-align: left;"><em>aku</em> orang pertama tunggal. <em>ahu</em> Number=Sing|Person=1, <em>nasida</em> Number=Plur|Person=3.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>I-113</strong></td>
<td style="text-align: left;"><strong>PronType</strong></td>
<td style="text-align: left;">Jenis pronomina dan determiner: Prs (persona), Dem (demonstratif), Int (tanya), Tot (menyeluruh), Ind (taktentu).</td>
<td style="text-align: left;"><em>ibana</em> Prs, <em>on</em> Dem, <em>aha</em> Int, <em>sude</em> Tot, <em>deba</em> Ind.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-19</em></td>
<td style="text-align: left;">eksklusif dan inklusif</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> <em>hami</em> Clusivity=Ex, <em>hita</em> Clusivity=In.</td>
</tr>
<tr>
<td style="text-align: left;"><em>→ I-39, I-40</em></td>
<td style="text-align: left;">PRON, DET</td>
<td colspan="2" style="text-align: left;"><strong>Pengingat:</strong> Kelas kata yang memakai fitur ini.</td>
</tr>
</tbody>
</table>

| **Kata** | **FEATS** |
|----|----|
| *ahu, au* | Number=Sing\|Person=1\|PronType=Prs |
| *hami* | Clusivity=Ex\|Number=Plur\|Person=1\|PronType=Prs |
| *hita* | Clusivity=In\|Number=Plur\|Person=1\|PronType=Prs |
| *ho* | Number=Sing\|Person=2\|PronType=Prs |
| *hamu* | Number=Plur\|Person=2\|PronType=Prs (juga untuk sapaan hormat) |
| *ibana* | Number=Sing\|Person=3\|PronType=Prs |
| *nasida* | Number=Plur\|Person=3\|PronType=Prs (juga untuk sapaan hormat) |
| *on, i, an, adu* (PRON atau DET) | PronType=Dem |
| *ise, aha, dia* | PronType=Int |
| *sude, nasa, ganup* | PronType=Tot |
| *deba, saotik, si anu* | PronType=Ind |

*Tabel 7.2. Fitur pronomina dan determiner.*

### 7.3 Nomina dan kelas lain

**Daftar istilah Bagian 7.3**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 39%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Istilah &amp; label UD</strong></th>
<th><strong>Arti sederhana</strong></th>
<th><strong>Contoh (Indonesia dan Batak Toba)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>→ I-18</em></td>
<td>Person[psor] dan Number[psor]</td>
<td colspan="2"><strong>Pengingat:</strong> Fitur pemilik pada nomina bersufiks (Tabel 4.1).</td>
</tr>
<tr>
<td><strong>I-114</strong></td>
<td><strong>NumType</strong></td>
<td>Jenis numeralia: Card (pokok), Ord (tingkat).</td>
<td><em>sada</em> NumType=Card, <em>parjolo</em> NumType=Ord.</td>
</tr>
<tr>
<td><strong>I-115</strong></td>
<td><strong>Degree</strong></td>
<td>Tingkat perbandingan adjektiva. Bentuk komparatif dicatat Degree=Cmp.</td>
<td><em>lebih tinggi</em>. <em>tumimbo</em>, <em>balgaan</em> Degree=Cmp.</td>
</tr>
<tr>
<td><strong>I-116</strong></td>
<td><strong>Polarity</strong></td>
<td>Fitur kutub kalimat. Kata negasi diberi Polarity=Neg.</td>
<td><em>dang</em>, <em>unang</em> Polarity=Neg.</td>
</tr>
<tr>
<td><strong>I-117</strong></td>
<td><strong>Foreign</strong></td>
<td>Penanda kata asing yang tidak terserap: Foreign=Yes.</td>
<td><em>founder</em>, <em>coding</em>.</td>
</tr>
<tr>
<td><em>→ I-29</em></td>
<td>Typo=Yes</td>
<td colspan="2"><strong>Pengingat:</strong> Penanda salah ketik.</td>
</tr>
<tr>
<td><em>→ I-82</em></td>
<td>negasi</td>
<td colspan="2"><strong>Pengingat:</strong> Kata yang diberi Polarity=Neg.</td>
</tr>
</tbody>
</table>

1.  Nomina bersufiks posesif: Number\[psor\] dan Person\[psor\] (Tabel 4.1).

2.  Numeralia pokok: NumType=Card. Numeralia tingkat (ADJ): NumType=Ord.

3.  Adjektiva komparatif um- atau -an (*tumimbo*, *balgaan*): Degree=Cmp.

4.  Negasi: Polarity=Neg.

5.  Kata asing tak terserap: Foreign=Yes. Salah ketik: Typo=Yes.

6.  Fitur Number untuk nomina tidak diisi. Kejamakan ditandai kata angka/akka, bukan infleksi.

## 8. Contoh Anotasi Lengkap

Contoh 1 sampai 9 diambil dari proposal dan dari contoh Nababan. Contoh 10 dan 11 adalah kalimat korpus. Contoh 11 memperlihatkan kalimat majemuk setara (Bagian 6.7). Kolom XPOS dan DEPS tidak ditampilkan karena selalu \_. Contoh dibahas ulang pada sesi pelatihan sebelum anotasi dimulai. Istilah yang dipakai di Bagian 8 sampai 11 dapat dicari di indeks Lampiran C.

**Contoh 1. Verba aktif transitif (contoh proposal)**

*Mangallang dengke do si Polan.* ‘Si Polan sedang makan ikan.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Mangallang | allang | VERB | Voice=Act | 0 | root | \_ |
| 2 | dengke | dengke | NOUN | \_ | 1 | obj | \_ |
| 3 | do | do | PART | \_ | 1 | discourse | \_ |
| 4 | si | si | DET | \_ | 5 | det | \_ |
| 5 | Polan | Polan | PROPN | \_ | 1 | nsubj | SpaceAfter=No |
| 6 | . | . | PUNCT | \_ | 1 | punct | \_ |

**Contoh 2. Predikat adjektiva tanpa kopula (contoh proposal)**

*Uli do jabu i.* ‘Rumah itu bagus.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Uli | uli | ADJ | \_ | 0 | root | \_ |
| 2 | do | do | PART | \_ | 1 | discourse | \_ |
| 3 | jabu | jabu | NOUN | \_ | 1 | nsubj | \_ |
| 4 | i | i | DET | PronType=Dem | 3 | det | SpaceAfter=No |
| 5 | . | . | PUNCT | \_ | 1 | punct | \_ |

**Contoh 3. Pasif di- dengan aktor (Nababan §5.1.2.1.2)**

*Ditongos nasida ma hepeng i.* ‘Uang itu dikirim oleh mereka.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Ditongos | tongos | VERB | Voice=Pass | 0 | root | \_ |
| 2 | nasida | nasida | PRON | Number=Plur\|Person=3\|PronType=Prs | 1 | obj:agent | \_ |
| 3 | ma | ma | PART | \_ | 1 | discourse | \_ |
| 4 | hepeng | hepeng | NOUN | \_ | 1 | nsubj | \_ |
| 5 | i | i | DET | PronType=Dem | 4 | det | SpaceAfter=No |
| 6 | . | . | PUNCT | \_ | 1 | punct | \_ |

**Contoh 4. Pasif hu- dengan aktor jamak (Nababan §5.1.2.2.1)**

*Hujou hami do ibana.* ‘Ia dipanggil oleh kami.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Hujou | jou | VERB | Voice=Pass | 0 | root | Aktor=1Eks |
| 2 | hami | hami | PRON | Clusivity=Ex\|Number=Plur\|Person=1\|PronType=Prs | 1 | obj:agent | \_ |
| 3 | do | do | PART | \_ | 1 | discourse | \_ |
| 4 | ibana | ibana | PRON | Number=Sing\|Person=3\|PronType=Prs | 1 | nsubj | SpaceAfter=No |
| 5 | . | . | PUNCT | \_ | 1 | punct | \_ |

**Contoh 5. Negasi dan pasif hu- tanpa kata aktor (Nababan §4.4.3.1)**

*Dang huida ibana.* ‘Aku tidak melihatnya.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Dang | dang | PART | Polarity=Neg | 2 | advmod | \_ |
| 2 | huida | ida | VERB | Voice=Pass | 0 | root | Aktor=1Eks |
| 3 | ibana | ibana | PRON | Number=Sing\|Person=3\|PronType=Prs | 2 | nsubj | SpaceAfter=No |
| 4 | . | . | PUNCT | \_ | 2 | punct | \_ |

**Contoh 6. Aktor bertanda ni pada verba promisif (Nababan §4.4.2.1.4)**

*Tuhoron ni si Ondo do i.* ‘Itu akan dibeli oleh si Ondo.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Tuhoron | tuhor | VERB | Aspect=Prosp\|Voice=Pass | 0 | root | \_ |
| 2 | ni | ni | ADP | \_ | 4 | case | \_ |
| 3 | si | si | DET | \_ | 4 | det | \_ |
| 4 | Ondo | Ondo | PROPN | \_ | 1 | obl:agent | \_ |
| 5 | do | do | PART | \_ | 1 | discourse | \_ |
| 6 | i | i | PRON | PronType=Dem | 1 | nsubj | SpaceAfter=No |
| 7 | . | . | PUNCT | \_ | 1 | punct | \_ |

**Contoh 7. Auxiliari modal (Nababan §4.4.5.1)**

*Naeng modom do ibana.* ‘Ia hendak tidur.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Naeng | naeng | AUX | \_ | 2 | aux | \_ |
| 2 | modom | modom | VERB | \_ | 0 | root | \_ |
| 3 | do | do | PART | \_ | 2 | discourse | \_ |
| 4 | ibana | ibana | PRON | Number=Sing\|Person=3\|PronType=Prs | 2 | nsubj | SpaceAfter=No |
| 5 | . | . | PUNCT | \_ | 2 | punct | \_ |

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

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Guru | guru | NOUN | \_ | 0 | root | \_ |
| 2 | do | do | PART | \_ | 1 | discourse | \_ |
| 3 | amana | ama | NOUN | Number\[psor\]=Sing\|Person\[psor\]=3 | 1 | nsubj | SpaceAfter=No |
| 4 | . | . | PUNCT | \_ | 1 | punct | \_ |

**Contoh 10. Kalimat korpus: pasif dengan aktor dan verba terkendali (btk_pilot, Folktales)**

*jadi disuru inana ma anakna i mangoli.* ‘lalu ibunya menyuruh anaknya menikah.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | jadi | jadi | ADV | \_ | 2 | advmod | \_ |
| 2 | disuru | suru | VERB | Voice=Pass | 0 | root | \_ |
| 3 | inana | ina | NOUN | Number\[psor\]=Sing\|Person\[psor\]=3 | 2 | obj:agent | \_ |
| 4 | ma | ma | PART | \_ | 2 | discourse | \_ |
| 5 | anakna | anak | NOUN | Number\[psor\]=Sing\|Person\[psor\]=3 | 2 | nsubj | \_ |
| 6 | i | i | DET | PronType=Dem | 5 | det | \_ |
| 7 | mangoli | oli | VERB | Voice=Act | 2 | xcomp | SpaceAfter=No |
| 8 | . | . | PUNCT | \_ | 2 | punct | \_ |

**Contoh 11. Kalimat korpus: kalimat majemuk setara (conj) yang memuat pelengkap (xcomp) (btk_pilot-001, Folktales)**

*Dunggi laos mengalu ma Sisamosir hu omak na jala disuru omak nai ma imana lau hu gunung paling timbo.* ‘Kemudian si Samosir mengadu pada ibunya, dan ia disuruh ibunya naik ke gunung paling tinggi.’

| **ID** | **FORM** | **LEMMA** | **UPOS** | **FEATS** | **HEAD** | **DEPREL** | **MISC** |
|----|----|----|----|----|----|----|----|
| 1 | Dunggi | dungi | CCONJ | \_ | 3 | cc | \_ |
| 2 | laos | laos | ADV | \_ | 3 | advmod | \_ |
| 3 | mengalu | mangalu | VERB | Typo=Yes | 0 | root | CorrectForm=mangalu |
| 4 | ma | ma | PART | \_ | 3 | discourse | \_ |
| 5 | Sisamosir | Sisamosir | PROPN | \_ | 3 | nsubj | \_ |
| 6 | hu | hu | ADP | \_ | 7 | case | \_ |
| 7 | omak | omak | NOUN | Number\[psor\]=Sing\|Person\[psor\]=3 | 3 | obl | CorrectForm=omakna |
| 8 | na | \_ | X | \_ | 7 | goeswith | \_ |
| 9 | jala | jala | CCONJ | \_ | 10 | cc | \_ |
| 10 | disuru | suru | VERB | Voice=Pass | 3 | conj | \_ |
| 11 | omak | omak | NOUN | \_ | 10 | obj:agent | \_ |
| 12 | nai | i | DET | PronType=Dem\|Typo=Yes | 11 | det | Ragu=Ya |
| 13 | ma | ma | PART | \_ | 10 | discourse | \_ |
| 14 | imana | imana | PRON | Number=Sing\|Person=3\|PronType=Prs | 10 | nsubj | \_ |
| 15 | lau | lau | VERB | \_ | 10 | xcomp | \_ |
| 16 | hu | hu | ADP | \_ | 17 | case | \_ |
| 17 | gunung | gunung | NOUN | \_ | 15 | obl | \_ |
| 18 | paling | paling | ADV | \_ | 19 | advmod | \_ |
| 19 | timbo | timbo | ADJ | \_ | 17 | amod | SpaceAfter=No |
| 20 | . | . | PUNCT | \_ | 3 | punct | \_ |

Catatan untuk Contoh 11:

1.  Kalimat ini punya tiga predikator: *mengalu* (klausa utama, root), *disuru* (klausa kedua, conj ke ID 3), dan *lau* (pelengkap *disuru*, xcomp ke ID 10).

2.  Semua isi klausa kedua (*omak*, *nai*, *ma*, *imana*, *lau*) menunjuk ke *disuru* (ID 10) atau ke kata lain di dalam klausa itu. Tidak satu pun menunjuk ke root.

3.  *jala* membuka klausa kedua, sehingga HEAD-nya 10 (*disuru*), bukan 3. *Dunggi* di awal kalimat menghubungkan kalimat ini dengan kalimat sebelumnya, sehingga diberi cc ke root.

4.  *disuru* berbentuk pasif di-. Orang yang disuruh (*imana*) menjadi nsubj, dan *omak* yang langsung mengikuti verba menjadi obj:agent (Tabel 6.1). Terjemahan Indonesia yang aktif tidak mengubah label.

5.  *omak na* ditulis terpisah untuk *omakna* sehingga memakai aturan goeswith (Bagian 4.4 butir 2). Token *nai* (diduga *na* + *i*) ditandai Ragu=Ya dan diajukan sebagai Catatan Pedoman.

6.  *hu* adalah ragam *tu* ‘ke’ dan diberi ADP dengan relasi case ke nomina sesudahnya.

7.  *laos* diberi ADV advmod ke *mengalu* sesuai aturan Bagian 5.1 butir 10. Penghubung dengan kalimat sebelumnya sudah dipikul *Dunggi*.

## 9. Kasus Sulit dan Aturan Saat Ragu

| **Situasi** | **Aturan** |
|:---|:---|
| Kalimat tanpa predikator jelas (fragmen judul, seruan) | Kata isi terpenting menjadi root. Catat di \# note. |
| Verba di- tanpa kata aktor | Tetap Voice=Pass. Tidak ada token obj:agent. |
| Aktor dan subjek sama-sama pronomina sehingga urutan meragukan | Kata yang langsung mengikuti verba adalah aktor (obj:agent). Kata sesudah partikel do atau ma adalah subjek (nsubj). |
| Partikel do atau ma setelah subjek (urutan terbalik) | Tetap discourse ke predikator, bukan ke subjek. |
| Nomina tak bertanda setelah verba aktif yang tampak sebagai bagian predikat (*mangan indahan*, inkorporasi semu) | Tetap obj. Tambahkan Ragu=Ya bila nomina itu tidak merujuk benda tertentu. |
| Reduplikasi (*pasu-pasu*, *tureture*) | Satu token. LEMMA bentuk dasar tanpa pengulangan bila jelas (pasu-pasu → pasu-pasu bila bentuk ulang adalah kata kamus). Tidak ada fitur khusus. |
| naeng, boi, ingkon tanpa verba lain | Bila menjadi satu-satunya predikat, VERB dan root. |
| Klausa kutipan langsung | Klausa kutipan menjadi ccomp dari verba berkata. Tanda kutip punct ke predikator kutipan. |
| Kalimat tanya dengan pronomina tanya di depan | Pronomina tanya menjadi root bila kalimat ekuasional (*Ise do ho?*). Bila pronomina tanya menjadi argumen verba (*Ise manuhor on?*), verba root dan ise nsubj. |
| Kata pinjaman Indonesia atau Inggris | Label menurut fungsi sintaksis. Foreign=Yes hanya untuk kata yang belum terserap ke ejaan Batak Toba. |
| Tidak yakin antara dua label | Pilih label yang paling sesuai Nababan, tambahkan Ragu=Ya, catat alternatifnya di Log_Waktu. |

*Tabel 9.1. Kasus sulit.*

## 10. Pertanyaan, Pemeriksaan, dan Kesepakatan

### 10.1 Mengajukan pertanyaan

1.  Pertanyaan tentang aturan dikirim tertulis ke ketua tim, bukan ke anotator lain.

2.  Jawaban ketua tim dikirim ke kedua anotator sekaligus sebagai Catatan Pedoman bernomor (CP-01, CP-02, dan seterusnya). Catatan ini berlaku sebagai tambahan pedoman versi yang sedang berlaku.

3.  Ketua tim tidak menjawab pertanyaan tentang label satu kalimat tertentu selama batch itu belum diserahkan kedua anotator.

### 10.2 Daftar periksa sebelum menyerahkan batch

1.  Setiap token punya LEMMA, UPOS, HEAD, dan DEPREL. Tidak ada \_ di keempat kolom itu, kecuali LEMMA untuk token goeswith.

2.  Setiap kalimat punya tepat satu root dengan HEAD 0.

3.  Pada kalimat majemuk setara dan kalimat kompleks, setiap kata menunjuk ke predikator klausanya sendiri atau ke kata di dalam klausanya. Hanya predikator klausa lain yang menunjuk ke klausa utama (Bagian 6.7).

4.  Tidak ada lingkaran dependensi dan tidak ada HEAD yang menunjuk ke ID yang tidak ada.

5.  PUNCT selalu berelasi punct. Relasi punct tidak dipakai untuk kelas kata lain.

6.  FEATS memakai nama dan nilai dari Bagian 7 dan diurutkan alfabetis.

7.  SpaceAfter=No yang sudah ada tidak terhapus.

8.  Log_Waktu batch itu terisi.

### 10.3 Pengukuran kesepakatan

Setelah seluruh batch selesai, ketua tim menghitung kesepakatan antaranotator untuk UPOS (persentase dan kappa Cohen), kepala (UAS), serta kepala dan relasi (LAS), dengan tokenisasi yang sama untuk kedua anotator. Kesepakatan juga dihitung per relasi dan per genre untuk menemukan konstruksi yang paling sering tidak disepakati. Sebagai patokan, treebank Tagalog UD-NewsCrawl melaporkan kappa 0,75 untuk kelas kata dan 0,68 untuk relasi dependensi (Aquino dkk., 2025). Perbedaan diselesaikan melalui adjudikasi, lalu pedoman direvisi menjadi versi 2.0.

## 11. Isu Terbuka untuk Versi 2.0

Keputusan berikut sengaja ditetapkan sederhana untuk pilot dan akan ditinjau berdasarkan hasil kesepakatan.

1.  Adjektiva atau adverbia di posisi predikator sebelum verba (Bagian 6.1 butir 4). Nababan menyebutnya predikator, pedoman ini memakai verba sebagai root.

2.  Status *gabe*, *boi*, dan *naeng* sebagai AUX atau VERB dengan xcomp.

3.  Fitur untuk aktor yang tersandi pada verba (*hu-*, *ta-*, sufiks promisif). Pedoman ini mencatatnya di MISC.

4.  Relasi untuk sasaran bertanda di setelah verba (§4.4.2.1.5). Pedoman ini memakai obl.

5.  Perlakuan laho sebagai penanda tujuan.

6.  Representasi reduplikasi dan inkorporasi nomina semu.

7.  Pendaftaran subtipe obj:agent ke daftar relasi Batak Toba di UD sebelum treebank dirilis.

Konvensi lain untuk diatesis Austronesia (misalnya label Voice=Pat atau nsubj:pass dengan obl:agent) tidak dipakai dalam pilot ini dan dicatat untuk kajian lanjutan.

## Lampiran A. Daftar Relasi yang Dipakai

| **Relasi** | **Arti singkat** | **Relasi** | **Arti singkat** |
|----|----|----|----|
| root | akar kalimat | amod | pewatas adjektiva |
| nsubj | subjek nominal | nummod | pewatas numeralia |
| csubj | subjek klausa | det | determiner |
| obj | objek verba aktif | nmod | pewatas nomina |
| obj:agent | aktor pasif tak bertanda | nmod:poss | pemilik dengan ni |
| obl | argumen atau keterangan bertanda | acl:relcl | klausa relatif na |
| obl:agent | aktor pasif bertanda ni | case | preposisi |
| xcomp | pelengkap terkendali | mark | penanda klausa dan na |
| ccomp | klausa pelengkap | cc | konektor koordinasi |
| advcl | klausa keterangan | conj | unsur koordinasi |
| advmod | adverbia, negasi | parataxis | klausa berjajar |
| aux | auxiliari modal | flat | nama majemuk |
| discourse | partikel modal, interjeksi | compound | nomina majemuk |
| vocative | sapaan | appos | aposisi |
| fixed | ungkapan beku | goeswith | bagian kata terpisah |
| punct | tanda baca | dep | tidak tergolongkan (dengan Ragu=Ya) |

## Lampiran B. Rujukan

1.  Nababan, P. W. J. (1981). A Grammar of Toba-Batak. Pacific Linguistics, Series D, No. 37. Canberra: Australian National University.

2.  de Marneffe, M.-C., Manning, C. D., Nivre, J., & Zeman, D. (2021). Universal Dependencies. Computational Linguistics, 47(2), 255-308.

3.  Nivre, J., dkk. (2020). Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection. Proceedings of LREC 2020, 4034-4043.

4.  Panduan resmi Universal Dependencies v2: https://universaldependencies.org/guidelines.html

5.  Alfina, I., Yuliawati, A., Tanaya, D., Dinakaramani, A., & Zeman, D. (2024). A Gold Standard Dataset for Javanese Tokenization, POS Tagging, Morphological Feature Tagging, and Dependency Parsing. Forum for Linguistic Studies, 6(5). https://doi.org/10.30564/fls.v6i5.6957

6.  Aquino, A., Miranda, L. J., & Or, E. (2025). The UD-NewsCrawl Treebank: Reflections and Challenges from a Large-scale Tagalog Syntactic Annotation Project. arXiv:2505.20428.

7.  Dyer, A., & O’Brien, J. (2025). Towards better annotation practices for symmetrical voice in Universal Dependencies. Proceedings of the Eighth Workshop on Universal Dependencies (UDW 2025), 137-142. https://aclanthology.org/2025.udw-1.15/

8.  Erlewine, M. Y. (2018). Extraction and Licensing in Toba Batak. Language, 94(3), 662-697. https://doi.org/10.1353/lan.2018.0039

## Lampiran C. Indeks Istilah

Indeks ini memuat semua istilah pada tabel Daftar istilah, termasuk nama lain istilah itu. Kolom No. menunjuk nomor istilah, dan kolom Bagian menunjuk bagian tempat istilah dijelaskan lengkap.

| **Istilah** | **No.** | **Bagian** | **Istilah** | **No.** | **Bagian** |
|----|----|----|----|----|----|
| acl:relcl | **I-94** | 6.6 | acl:relcl (klausa relatif) | **I-94** | 6.6 |
| ADJ | **I-36** | 5 | adjektiva | **I-36** | 5 |
| ADP | **I-43** | 5 | ADV | **I-37** | 5 |
| advcl | **I-103** | 6.7 | adverbia | **I-37** | 5 |
| advmod | **I-55** | 5.1 | afiks (imbuhan) | **I-21** | 4.3 |
| akar kalimat | **I-56** | 6.1 | akhiran | **I-14** | 4.2 |
| aktif | **I-68** | 6.3 | aktor | **I-71** | 6.3 |
| Aktor (MISC) | **I-12** | 3 | amod | **I-93** | 6.6 |
| anak kalimat | **I-84** | 6.5 | aposisi | **I-98** | 6.6 |
| appos | **I-98** | 6.6 | argumen inti | **I-74** | 6.4 |
| Aspect | **I-110** | 7.1 | AUX | **I-47** | 5 |
| auxiliari | **I-47** | 5 | auxiliari predikator | **I-83** | 6.5 |
| awalan | **I-21** | 4.3 | baris komentar (#) | **I-03** | 3 |
| bentuk dasar | **I-06** | 3 | case | **I-52** | 5.1 |
| cc | **I-51** | 5.1 | ccomp | **I-80** | 6.4 |
| CCONJ | **I-46** | 5 | Clusivity | **I-19** | 4.2 |
| compound | **I-90** | 6.6 | conj | **I-101** | 6.7 |
| CoNLL-U | **I-01** | 3 | CorrectForm | **I-29** | 4.4 |
| csubj | **I-65** | 6.2 | Degree | **I-115** | 7.3 |
| dep | **I-107** | 6.8 | DEPREL (relasi dependensi) | **I-11** | 3 |
| DEPS | **I-08** | 3 | derivasi | **I-22** | 4.3 |
| DET | **I-40** | 5 | determiner | **I-40** | 5 |
| diatesis | **I-23** | 4.3 | discourse | **I-53** | 5.1 |
| eksklusif | **I-19** | 4.2 | eksklusif dan inklusif (klusivitas) | **I-19** | 4.2 |
| FEATS (fitur morfologis) | **I-09** | 3 | fitur morfologis | **I-09** | 3 |
| fixed | **I-106** | 6.8 | flat | **I-97** | 6.6 |
| Foreign | **I-117** | 7.3 | Foreign=Yes | **I-117** | 7.3 |
| FORM | **I-05** | 3 | frasa nomina | **I-87** | 6.6 |
| goeswith | **I-30** | 4.4 | HEAD (induk) | **I-10** | 3 |
| ID | **I-04** | 3 | imbuhan | **I-21** | 4.3 |
| imperatif | **I-111** | 7.1 | induk | **I-10** | 3 |
| induk kalimat | **I-84** | 6.5 | infiks | **I-21** | 4.3 |
| infleksi | **I-17** | 4.2 | inklusif | **I-19** | 4.2 |
| interjeksi | **I-38** | 5 | inti | **I-88** | 6.6 |
| INTJ | **I-38** | 5 | jembatan tata bahasa sekolah | **tabel** | 6.4 |
| kalimat kompleks | **I-102** | 6.7 | kalimat majemuk bertingkat | **I-102** | 6.7 |
| kalimat majemuk setara | **I-102** | 6.7 | kalimat tunggal | **I-102** | 6.7 |
| kalimat tunggal, kalimat kompleks, kalimat majemuk setara | **I-102** | 6.7 | kata asing | **I-117** | 7.3 |
| kata fungsi | **I-32** | 5 | kata isi | **I-31** | 5 |
| kelas kata | **I-07** | 3 | keterangan | **I-75** | 6.4 |
| klausa | **I-58** | 6.1 | klausa bawahan | **I-84** | 6.5 |
| klausa ekuasional | **I-62** | 6.1 | klausa keterangan | **I-103** | 6.7 |
| klausa pelengkap | **I-80** | 6.4 | klausa relatif | **I-94** | 6.6 |
| klausa relatif tanpa inti | **I-99** | 6.6 | klausa utama | **I-84** | 6.5 |
| klausa utama dan klausa bawahan | **I-84** | 6.5 | klusivitas | **I-19** | 4.2 |
| komparatif | **I-115** | 7.3 | komplemen | **I-60** | 6.1 |
| komplemen (C) | **I-60** | 6.1 | kompletif | **I-24** | 4.3 |
| konektor | **I-46** | 5 | konjungsi koordinatif | **I-46** | 5 |
| konjungsi subordinatif | **I-44** | 5 | konstituen agentif | **I-72** | 6.3 |
| konstituen agentif dan objektif | **I-72** | 6.3 | konstituen objektif | **I-72** | 6.3 |
| kontrol | **I-79** | 6.4 | kontrol (subjek terkendali) | **I-79** | 6.4 |
| koordinasi | **I-100** | 6.7 | kopula | **I-59** | 6.1 |
| kopula dan predikat nonverbal | **I-59** | 6.1 | lema | **I-06** | 3 |
| LEMMA (lema) | **I-06** | 3 | luluh | **I-27** | 4.3 |
| maN- | **I-27** | 4.3 | mark | **I-54** | 5.1 |
| MISC | **I-12** | 3 | Mood | **I-111** | 7.1 |
| na (penanda atributif) | **I-20** | 4.2 | nama diri | **I-34** | 5 |
| nama fitur dan nilai fitur | **I-108** | 7 | negasi | **I-82** | 6.5 |
| nilai fitur | **I-108** | 7 | nmod | **I-91** | 6.6 |
| nmod:poss | **I-92** | 6.6 | nomina | **I-33** | 5 |
| \# note | **I-03** | 3 | NOUN | **I-33** | 5 |
| nsubj | **I-64** | 6.2 | NUM | **I-41** | 5 |
| Number | **I-112** | 7.2 | Number\[psor\] | **I-18** | 4.2 |
| numeralia | **I-41** | 5 | nummod | **I-96** | 6.6 |
| NumType | **I-114** | 7.3 | obj | **I-76** | 6.4 |
| obj:agent | **I-73** | 6.3 | obj:agent dan obl:agent | **I-73** | 6.3 |
| objek | **I-76** | 6.4 | obl | **I-77** | 6.4 |
| obl:agent | **I-73** | 6.3 | parataxis | **I-104** | 6.7 |
| parataxis dan umpasa | **I-104** | 6.7 | PART | **I-45** | 5 |
| partikel | **I-45** | 5 | partikel modal | **I-81** | 6.5 |
| partikel predikatif | **I-81** | 6.5 | partikel predikatif (partikel modal) | **I-81** | 6.5 |
| pasif | **I-69** | 6.3 | pelaku | **I-71** | 6.3 |
| pelaku (aktor) dan sasaran | **I-71** | 6.3 | peleburan bunyi maN- | **I-27** | 4.3 |
| pelesapan | **I-67** | 6.2 | penanda atributif | **I-20** | 4.2 |
| Person | **I-112** | 7.2 | Person dan Number | **I-112** | 7.2 |
| Person\[psor\] | **I-18** | 4.2 | Person\[psor\] dan Number\[psor\] | **I-18** | 4.2 |
| pewatas | **I-89** | 6.6 | Polarity | **I-116** | 7.3 |
| potensial | **I-26** | 4.3 | predikat | **I-57** | 6.1 |
| predikat nonverbal | **I-59** | 6.1 | predikator | **I-57** | 6.1 |
| prefiks | **I-21** | 4.3 | preposisi | **I-43** | 5 |
| pro-adjektiva | **I-42** | 5 | pro-adjung | **I-42** | 5 |
| pro-bentuk | **I-42** | 5 | pro-klausa | **I-42** | 5 |
| pro-verba | **I-42** | 5 | promisif | **I-25** | 4.3 |
| PRON | **I-39** | 5 | pronomina | **I-39** | 5 |
| PronType | **I-113** | 7.2 | PROPN | **I-34** | 5 |
| PUNCT | **I-48** | 5 | Ragu=Ya | **I-12** | 3 |
| relasi dependensi | **I-11** | 3 | resiprokal | **I-70** | 6.3 |
| root | **I-56** | 6.1 | S-P-O-Pel-K (jembatan) | **tabel** | 6.4 |
| salah ketik | **I-29** | 4.4 | sapaan | **I-105** | 6.8 |
| sasaran | **I-71** | 6.3 | SCONJ | **I-44** | 5 |
| simbol | **I-49** | 5 | sisipan | **I-21** | 4.3 |
| SpaceAfter=No | **I-12** | 3 | subjek | **I-64** | 6.2 |
| subjek lesap | **I-67** | 6.2 | sufiks (akhiran) | **I-14** | 4.2 |
| sufiks aktor | **I-16** | 4.2 | sufiks posesif (sufiks pronominal) | **I-15** | 4.2 |
| sufiks pronominal | **I-15** | 4.2 | SYM | **I-49** | 5 |
| taktransitif | **I-28** | 4.3 | tanda baca | **I-48** | 5 |
| \# text | **I-03** | 3 | token | **I-02** | 3 |
| tokenisasi | **I-13** | 4.1 | transitif | **I-28** | 4.3 |
| Typo=Yes | **I-29** | 4.4 | Typo=Yes dan CorrectForm | **I-29** | 4.4 |
| umpasa | **I-104** | 6.7 | unsur setara | **I-85** | 6.5 |
| UPOS | **I-07** | 3 | urutan langsung | **I-61** | 6.1 |
| urutan terbalik | **I-66** | 6.2 | urutan terbalik emfatik | **I-66** | 6.2 |
| VERB | **I-35** | 5 | verba | **I-35** | 5 |
| verba transitif dan taktransitif | **I-28** | 4.3 | vocative | **I-105** | 6.8 |
| Voice | **I-109** | 7.1 | X | **I-50** | 5 |
| X dan Foreign=Yes | **I-50** | 5 | xcomp | **I-78** | 6.4 |
| XPOS | **I-08** | 3 | XPOS dan DEPS | **I-08** | 3 |
