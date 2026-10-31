#!/usr/bin/env python3
"""Bandingkan dua anotasi paralel dan buat lembar rekonsiliasi perbedaan.

Menghasilkan file .tsv berisi setiap token yang berbeda (UPOS/HEAD/DEPREL)
antara dua anotator, untuk didiskusikan dan diputuskan menjadi versi gold.

Pemakaian:
    python reconcile.py --a anotator1.conllu --b anotator2.conllu \
        --out ../evaluation/reconcile.tsv
"""
import argparse

def parse(path):
    sents = {}
    sid, toks = None, []
    text = {}
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("# sent_id"):
            sid = line.split("=",1)[1].strip()
        elif line.startswith("# text ") or line.startswith("# text="):
            text[sid] = line.split("=",1)[1].strip()
        elif not line:
            if sid and toks: sents[sid] = toks
            toks = []
        elif not line.startswith("#"):
            c = line.split("\t")
            if len(c)==10 and c[0].isdigit():
                toks.append(c)
    if sid and toks: sents[sid] = toks
    return sents, text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out", default="reconcile.tsv")
    args = ap.parse_args()

    A, tA = parse(args.a)
    B, tB = parse(args.b)
    common = sorted(set(A) & set(B))
    rows = [["sent_id","id","form","upos_A","upos_B","head_A","head_B",
             "deprel_A","deprel_B","jenis_beda","keputusan_gold"]]
    n_diff = 0
    for sid in common:
        ta, tb = A[sid], B[sid]
        if len(ta) != len(tb):
            rows.append([sid,"-","(tokenisasi beda)","","","","","","","TOKENISASI",""])
            continue
        for wa, wb in zip(ta, tb):
            diffs = []
            if wa[3]!=wb[3]: diffs.append("UPOS")
            if wa[6]!=wb[6]: diffs.append("HEAD")
            if wa[7]!=wb[7]: diffs.append("DEPREL")
            if diffs:
                n_diff += 1
                rows.append([sid, wa[0], wa[1], wa[3], wb[3], wa[6], wb[6],
                             wa[7], wb[7], "+".join(diffs), ""])
    with open(args.out,"w",encoding="utf-8") as f:
        for r in rows:
            f.write("\t".join(r)+"\n")
    print(f"kalimat dibandingkan: {len(common)} | token berbeda: {n_diff}")
    print(f"lembar rekonsiliasi -> {args.out} (isi kolom keputusan_gold)")

if __name__ == "__main__":
    main()
