# Panduan Ringkas Anotator (Kartu Cepat, Revisi 3)

Cetak halaman ini. Kartu ini ringkasan dari [Pedoman Anotasi UD Batak Toba v1.2](../anotasi-ud/pedoman/pedoman-anotasi-ud-v1.2.md). Bila kartu dan pedoman berbeda, ikuti pedoman.

## PERUBAHAN PENTING dari kartu versi lama

| Kartu lama | Sekarang (pedoman v1.2) |
|---------|---------|
| ~~pasien pada di- = `nsubj:pass`~~ | pasien pada di- = **`nsubj`** |
| ~~aktor pada di- = `obl:agent`~~ | aktor tak bertanda pada di- = **`obj:agent`** |
| ~~`obl:agent` tidak boleh dipakai~~ | `obl:agent` **dipakai** untuk aktor bertanda ***ni*** (verba kompletif dan promisif) |
| ~~status *na* belum diputuskan~~ | *na* atributif = **`PART`** dengan relasi **`mark`** |
| (belum diatur) | ***laos*** = **`ADV`** dengan relasi **`advmod`** |
| (belum diatur) | kalimat majemuk tetap **satu root**, klausa kedua = `conj` |

Alasannya: Batak Toba bukan bahasa aktif-pasif seperti Bahasa Indonesia. Aktor tak bertanda pada verba di- adalah argumen inti, bukan keterangan tambahan.

## Langkah per kalimat

1. Baca kalimat dan terjemahan Indonesianya.
2. Tentukan predikator sebagai root (HEAD=0). Predikator biasanya di awal, tetapi bisa didahului unsur emfatik.
3. Tandai UPOS tiap kata.
4. Tentukan HEAD dan DEPREL tiap kata.
5. Isi FEATS bila perlu, terutama Voice pada verba.
6. Cek dengan daftar periksa di bawah.

## Aturan kunci (paling sering salah)

| Situasi | Keputusan |
|---------|-----------|
| Verba maN- (mangallang) | `Voice=Act`, aktor = `nsubj`, pasien = `obj` |
| Verba di- (diallang) | `Voice=Pass`, pasien = `nsubj`, aktor tak bertanda = **`obj:agent`** |
| Verba hu- dan ta- (huida, tabuat) | `Voice=Pass`, aktor dicatat di MISC (`Aktor=1Eks` atau `Aktor=1Ink`), kata aktor bila ada = `obj:agent` |
| Aktor bertanda *ni* (tuhoron ni si Ondo) | aktor = **`obl:agent`**, *ni* = ADP dengan relasi `case` |
| Subjek muncul setelah predikator | tetap `nsubj`, bukan dislokasi |
| Subjek dipindah ke depan untuk penekanan | tetap `nsubj`, root tetap predikator |
| Predikat adjektiva atau nomina | root, TANPA kopula, subjek = `nsubj` |
| do, ma, pe | UPOS=PART, DEPREL=discourse, HEAD=predikator |
| na atributif (halak na manuhor) | UPOS=PART, DEPREL=mark menuju pewatas yang ditandainya |
| laos | UPOS=ADV, DEPREL=advmod menuju predikator klausanya |
| si + nama | si=DET, DEPREL=det menuju PROPN |
| i dan on (itu/ini) | DET, FEATS=PronType=Dem, DEPREL=det |
| di, tu, sian, hu + nomina | preposisi=ADP/case, frasanya=`obl` |
| dang, ndang, ndada, so, unang | UPOS=PART, `Polarity=Neg`, DEPREL=advmod menuju predikator, termasuk predikat nomina |
| Sufiks pronominal (-na, -mu, -hu/-ku) | tidak dipisah, dicatat dengan `Number[psor]` dan `Person[psor]` |
| LEMMA | bentuk dasar tanpa afiks (mangallang menjadi allang) |

## Membedakan obl, obj:agent, dan obl:agent

Ketiganya sama-sama nomina yang muncul setelah verba. Bedanya:

- **Ada preposisi** (di, tu, sian, dohot) di depannya. Maka nomina itu **`obl`**, preposisinya `case`.
  Contoh: *Modom do si Ucok **di jabu***. Jabu = obl.
- **Tidak ada preposisi**, menempel langsung setelah verba di-, hu-, atau ta-, dan maknanya pelaku. Maka nomina itu **`obj:agent`**.
  Contoh: *Diallang **si Polan** do dengke i*. Polan = obj:agent.
- **Ditandai *ni*** setelah verba kompletif (-in-/ni-) atau promisif (-on), dan maknanya pelaku. Maka nomina itu **`obl:agent`**, *ni* = `case`.
  Contoh: *Tuhoron **ni si Ondo** do i*. Ondo = obl:agent.

Uji cepat untuk `obj:agent`: coba sisipkan kata lain antara verba dan nomina itu. Kalau terasa janggal dan tidak bisa, kemungkinan besar `obj:agent`.

## Kalimat majemuk dan kalimat kompleks

1. Tetap satu root, yaitu predikator klausa utama.
2. Predikator klausa kedua menunjuk ke root dengan relasi `conj`. Konektor (*jala*, *alai*, *dungi*) = CCONJ dengan relasi `cc` menuju predikator klausa kedua.
3. Semua kata lain menunjuk ke predikator klausanya sendiri, bukan ke root.
4. Verba kedua tanpa subjek sendiri (disuru ... mangoli) = `xcomp`.

Lihat Contoh 11 pada pedoman.

## 17 UPOS

NOUN PROPN PRON VERB ADJ ADV AUX ADP DET NUM PART CCONJ SCONJ INTJ SYM PUNCT X

## Relasi yang JANGAN dipakai

`nsubj:pass`. Pivot pada kedua diatesis selalu `nsubj`.

## Daftar periksa akhir

- [ ] Tepat satu root.
- [ ] Semua HEAD valid, tidak ada lingkaran.
- [ ] Voice terisi untuk verba maN-, di-, hu-, dan ta-.
- [ ] Pivot = `nsubj` di kedua diatesis.
- [ ] Aktor tak bertanda pada verba di- = `obj:agent`, aktor bertanda *ni* = `obl:agent`.
- [ ] do, ma, pe = PART/discourse.
- [ ] Pada kalimat majemuk, isi tiap klausa menunjuk ke predikator klausanya sendiri.
- [ ] Tanda baca = PUNCT/punct, SpaceAfter=No yang sudah ada tidak terhapus.

## Bila ragu

1. Pilih label yang paling sesuai dengan Nababan (1981), tambahkan `Ragu=Ya` di kolom MISC, lalu catat alternatifnya di Log_Waktu.
2. Pertanyaan tentang aturan dikirim tertulis ke ketua tim. Jawabannya dikirim ke kedua anotator sebagai Catatan Pedoman (CP-01, CP-02, dan seterusnya).
3. Jangan berdiskusi dengan anotator lain tentang kalimat yang sedang dianotasi.
