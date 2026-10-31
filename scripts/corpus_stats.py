#!/usr/bin/env python3
"""Statistik korpus CoNLL-U: jumlah kalimat, token, distribusi UPOS/DEPREL/Voice.

Pemakaian:
    python corpus_stats.py corpus/pilot/*.conllu --out ../evaluation/corpus_stats.md
"""
import sys, glob, argparse
from collections import Counter

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("globs", nargs="+")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    paths = []
    for g in a.globs:
        paths.extend(glob.glob(g))
    paths = sorted(set(paths))

    n_sent = n_tok = 0
    upos = Counter(); deprel = Counter(); voice = Counter()
    lens = []
    for p in paths:
        cur = 0
        for line in open(p, encoding="utf-8"):
            line = line.rstrip("\n")
            if line.startswith("# sent_id"):
                if cur: lens.append(cur)
                cur = 0; n_sent += 1
            elif line and not line.startswith("#"):
                c = line.split("\t")
                if len(c)==10 and c[0].isdigit():
                    n_tok += 1; cur += 1
                    if c[3]!="_": upos[c[3]] += 1
                    if c[7]!="_": deprel[c[7]] += 1
                    for feat in c[5].split("|"):
                        if feat.startswith("Voice="):
                            voice[feat.split("=")[1]] += 1
        if cur: lens.append(cur)

    avg = sum(lens)/len(lens) if lens else 0
    L = []
    L.append("# Statistik Korpus")
    L.append(f"- File: {len(paths)}")
    L.append(f"- Kalimat: {n_sent}")
    L.append(f"- Token: {n_tok}")
    L.append(f"- Rata-rata panjang kalimat: {avg:.1f} token")
    L.append(f"- Kalimat terpendek/terpanjang: {min(lens) if lens else 0}/{max(lens) if lens else 0}")
    L.append("\n## Distribusi UPOS")
    for k,v in upos.most_common():
        L.append(f"- {k}: {v} ({v/n_tok*100:.1f}%)")
    L.append("\n## Distribusi DEPREL (10 teratas)")
    for k,v in deprel.most_common(10):
        L.append(f"- {k}: {v}")
    L.append("\n## Distribusi Voice (diatesis)")
    for k,v in voice.most_common():
        L.append(f"- {k}: {v}")
    out = "\n".join(L)
    print(out)
    if a.out:
        open(a.out,"w",encoding="utf-8").write(out+"\n")
        print(f"\n-> {a.out}")

if __name__ == "__main__":
    main()
