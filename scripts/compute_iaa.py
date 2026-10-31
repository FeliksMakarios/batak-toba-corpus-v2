#!/usr/bin/env python3
"""Hitung kesepakatan antaranotator (IAA) untuk dua file CoNLL-U paralel.

Metrik:
- UPOS agreement (proporsi token dengan UPOS sama).
- UAS agreement (proporsi token dengan HEAD sama).
- LAS agreement (proporsi token dengan HEAD dan DEPREL sama).
- Cohen's kappa untuk UPOS.

Kedua file harus berisi kalimat dengan sent_id sama dan tokenisasi identik.

Pemakaian:
    python compute_iaa.py --a anotator1.conllu --b anotator2.conllu \
        --report ../evaluation/iaa_report.md
"""
import argparse
from collections import defaultdict, Counter

def parse(path):
    sents = {}
    sid, toks = None, []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("# sent_id"):
            sid = line.split("=", 1)[1].strip()
        elif not line:
            if sid and toks:
                sents[sid] = toks
            sid, toks = None, []
        elif not line.startswith("#"):
            c = line.split("\t")
            if len(c) == 10 and c[0].isdigit():
                toks.append({"id": c[0], "form": c[1], "upos": c[3],
                             "head": c[6], "deprel": c[7]})
    if sid and toks:
        sents[sid] = toks
    return sents

def kappa(pairs):
    # Cohen's kappa untuk label kategori (UPOS)
    n = len(pairs)
    if n == 0:
        return float("nan")
    labels = set(x for p in pairs for x in p)
    po = sum(1 for a, b in pairs if a == b) / n
    ca = Counter(a for a, _ in pairs); cb = Counter(b for _, b in pairs)
    pe = sum((ca[l]/n) * (cb[l]/n) for l in labels)
    return (po - pe) / (1 - pe) if pe != 1 else 1.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--report", default=None)
    args = ap.parse_args()

    A, B = parse(args.a), parse(args.b)
    common = sorted(set(A) & set(B))
    upos_pairs, n_tok = [], 0
    uas_ok = las_ok = 0
    mismatch = defaultdict(int)  # deprel yang sering beda
    for sid in common:
        ta, tb = A[sid], B[sid]
        if len(ta) != len(tb):
            continue  # tokenisasi beda, lewati (idealnya identik)
        for wa, wb in zip(ta, tb):
            n_tok += 1
            upos_pairs.append((wa["upos"], wb["upos"]))
            if wa["head"] == wb["head"]:
                uas_ok += 1
                if wa["deprel"] == wb["deprel"]:
                    las_ok += 1
            if wa["deprel"] != wb["deprel"]:
                key = tuple(sorted((wa["deprel"], wb["deprel"])))
                mismatch[key] += 1

    upos_agr = sum(1 for a, b in upos_pairs if a == b) / n_tok if n_tok else 0
    lines = []
    lines.append(f"# Laporan IAA")
    lines.append(f"- Kalimat dibandingkan: {len(common)}")
    lines.append(f"- Token dibandingkan: {n_tok}")
    lines.append(f"- UPOS agreement: {upos_agr:.3f}")
    lines.append(f"- UPOS Cohen's kappa: {kappa(upos_pairs):.3f}")
    lines.append(f"- UAS agreement (HEAD): {uas_ok/n_tok:.3f}" if n_tok else "- UAS: NA")
    lines.append(f"- LAS agreement (HEAD+DEPREL): {las_ok/n_tok:.3f}" if n_tok else "- LAS: NA")
    lines.append("")
    lines.append("## Pasangan DEPREL paling sering tidak disepakati")
    for (x, y), c in sorted(mismatch.items(), key=lambda t: -t[1])[:15]:
        lines.append(f"- {x} vs {y}: {c}")
    out = "\n".join(lines)
    print(out)
    if args.report:
        open(args.report, "w", encoding="utf-8").write(out + "\n")
        print(f"\n-> ditulis ke {args.report}")

if __name__ == "__main__":
    main()
