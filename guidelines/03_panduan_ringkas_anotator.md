# Panduan Ringkas Anotator (Kartu Cepat, Revisi 2)

Cetak halaman ini. Rujukan lengkap: `02_pedoman_anotasi_v2.md`.

## PERUBAHAN PENTING dari kartu versi lama

Kalau kamu pernah memakai kartu versi lama, dua aturan berikut **sudah dicabut**:

| Dicabut | Diganti |
|---------|---------|
| ~~pasien pada di- = `nsubj:pass`~~ | pasien pada di- = **`nsubj`** |
| ~~aktor pada di- = `obl:agent`~~ | aktor pada di- = **`obj:agent`** |

Alasannya: Batak Toba bukan bahasa aktif-pasif. Batak Toba punya dua diatesis yang sama-sama transitif penuh. Aktor pada verba di- adalah argumen inti, bukan keterangan tambahan.

## Langkah per kalimat

1. Baca kalimat dan terjemahan Indonesianya.
2. Tentukan predikat utama sebagai root (HEAD=0). Predikat biasanya di awal, tetapi bisa didahului unsur emfatik.
3. Tandai UPOS tiap kata.
4. Tentukan HEAD dan DEPREL tiap kata.
5. Isi FEATS bila perlu, terutama Voice pada verba.
6. Cek dengan daftar periksa di bawah.

## Aturan kunci (paling sering salah)

| Situasi | Keputusan |
|---------|-----------|
| Verba maN- (mangallang) | `Voice=Act`, aktor = `nsubj`, pasien = `obj` |
| Verba di- (diallang) | `Voice=Pass`, pasien = `nsubj`, aktor = **`obj:agent`** |
| Subjek muncul setelah predikat | tetap `nsubj`, bukan dislokasi |
| Subjek dipindah ke depan untuk penekanan | tetap `nsubj`, root tetap predikator |
| Predikat adjektiva atau nomina | root, TANPA kopula, subjek = `nsubj` |
| do dan ma | UPOS=PART, DEPREL=discourse, HEAD=root |
| si + nama | si=DET, DEPREL=det menuju PROPN |
| i dan on (itu/ini) | DET, FEATS=PronType=Dem, DEPREL=det |
| di, tu, sian + nomina | preposisi=ADP/case, frasanya=`obl` |
| ndang dan dang (tidak/bukan) | Polarity=Neg, DEPREL=advmod menuju predikat, termasuk predikat nomina |
| LEMMA | bentuk dasar tanpa afiks (mangallang menjadi allang) |

## Membedakan obl dan obj:agent (sumber kesalahan nomor satu)

Keduanya sama-sama nomina yang muncul setelah verba. Bedanya:

- **Ada preposisi** (di, tu, sian, dohot) di depannya, dan verbanya bukan di-. Maka nomina itu **`obl`**, preposisinya `case`.
  Contoh: *Modom do si Ucok **di jabu*** . Jabu = obl.
- **Tidak ada preposisi**, menempel langsung setelah verba berawalan **di-**, dan maknanya pelaku. Maka nomina itu **`obj:agent`**.
  Contoh: *Diallang **si Polan** do dengke i*. Polan = obj:agent.

Uji cepat: coba sisipkan kata lain antara verba dan nomina itu. Kalau terasa janggal dan tidak bisa, kemungkinan besar `obj:agent`.

## 17 UPOS

NOUN PROPN PRON VERB ADJ ADV AUX ADP DET NUM PART CCONJ SCONJ INTJ SYM PUNCT X

## Relasi yang JANGAN dipakai

`nsubj:pass` dan `obl:agent`. Kalau kamu menuliskannya, validator akan menandainya sebagai kesalahan.

## Daftar periksa akhir

- [ ] Tepat satu root.
- [ ] Semua HEAD valid.
- [ ] Voice terisi untuk verba maN- dan di-.
- [ ] Pivot = `nsubj` di kedua diatesis.
- [ ] Aktor pada verba di- = `obj:agent`.
- [ ] do dan ma = PART/discourse.
- [ ] Tanda baca = PUNCT/punct, SpaceAfter=No bila menempel.

## Bila ragu

Beri komentar `# TODO: <alasan>` di atas kalimat dan lanjutkan. Jangan menebak diam-diam. Kumpulkan keraguan untuk sesi konsultasi narasumber.
