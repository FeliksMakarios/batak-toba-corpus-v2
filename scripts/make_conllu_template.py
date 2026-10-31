#!/usr/bin/env python3
"""Ubah 250_final.csv menjadi file .conllu kosong siap anotasi.

Setiap kalimat ditulis dengan header (# sent_id, # text, # text[ind]) dan
baris token bertokenisasi kasar (pisah spasi + pisahkan tanda baca akhir).
Kolom LEMMA..DEPS diisi '_' agar anotator melengkapi.

Pemakaian:
    python make_conllu_template.py --input 250_final.csv \
        --out ../corpus/pilot/btk_pilot.blank.conllu
"""
import argparse, csv, re

def tokenize(teks):
    # pisahkan tanda baca yang menempel di akhir kata
    toks = []
    for w in teks.split():
        m = re.match(r"^(.*?)([.,!?;:]+)$", w)
        if m and m.group(1):
            toks.append((m.group(1), True))   # kata, lalu tanda baca menempel
            toks.append((m.group(2), False))
        else:
            toks.append((w, False))
    return toks

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    with open(a.input, newline="", encoding="utf-8") as f, \
         open(a.out, "w", encoding="utf-8") as g:
        for r in csv.DictReader(f):
            sid = r["sent_id"]; teks = r["teks_batak"].strip()
            ind = r.get("teks_ind", "").strip()
            g.write(f"# sent_id = {sid}\n")
            g.write(f"# text = {teks}\n")
            if ind:
                g.write(f"# text[ind] = {ind}\n")
            toks = tokenize(teks)
            n = sum(1 for _, _ in toks)
            for i, (tok, attach_next) in enumerate(toks, 1):
                misc = "SpaceAfter=No" if attach_next else "_"
                # ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC
                g.write(f"{i}\t{tok}\t_\t_\t_\t_\t_\t_\t_\t{misc}\n")
            g.write("\n")
    print(f"template CoNLL-U kosong ditulis -> {a.out}")

if __name__ == "__main__":
    main()
