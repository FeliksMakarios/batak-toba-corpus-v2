#!/usr/bin/env python3
"""Validator format CoNLL-U untuk korpus UD Batak Toba.

Memeriksa aturan struktural dasar (bukan validasi UD resmi penuh):
- Tepat 10 kolom per baris token.
- ID berurutan 1..n per kalimat.
- Tepat satu root (HEAD=0 dan DEPREL=root).
- Semua HEAD menunjuk ID yang ada atau 0.
- UPOS termasuk 17 tag UD (bila kolom terisi).
- Header # sent_id dan # text ada.
- Tidak ada siklus dependensi.

Keluar dengan kode 1 bila ada galat (dipakai di CI).

Pemakaian:
    python validate_conllu.py corpus/pilot/*.conllu
"""
import sys, glob, re

UPOS = {"ADJ","ADP","ADV","AUX","CCONJ","DET","INTJ","NOUN","NUM","PART",
        "PRON","PROPN","PUNCT","SCONJ","SYM","VERB","X"}

def has_cycle(heads):
    # heads: dict id->head (int). Telusuri sampai 0; deteksi loop.
    for start in heads:
        seen = set()
        cur = start
        while cur != 0:
            if cur in seen:
                return True
            seen.add(cur)
            cur = heads.get(cur, 0)
    return False

def validate_file(path):
    errs = []
    sid = None
    rows = []
    have_text = False
    line_no = 0

    def flush():
        if not rows:
            return
        ids = [r["id"] for r in rows]
        if ids != list(range(1, len(ids)+1)):
            errs.append(f"{sid}: ID tidak berurutan {ids}")
        roots = [r for r in rows if r["head"] == 0]
        if len(roots) != 1:
            errs.append(f"{sid}: jumlah HEAD=0 ada {len(roots)} (harus 1)")
        root_deprel = [r for r in rows if r["deprel"] == "root"]
        if len(root_deprel) != 1:
            errs.append(f"{sid}: deprel 'root' muncul {len(root_deprel)}x (harus 1)")
        for r in rows:
            if r["head"] != 0 and r["head"] not in ids:
                errs.append(f"{sid}: HEAD {r['head']} tak ada (token {r['form']})")
            if r["deprel"] == "root" and r["head"] != 0:
                errs.append(f"{sid}: DEPREL root tapi HEAD={r['head']}")
            if r["head"] == 0 and r["deprel"] != "root":
                errs.append(f"{sid}: HEAD=0 tapi DEPREL={r['deprel']} (harus root)")
            if r["upos"] != "_" and r["upos"] not in UPOS:
                errs.append(f"{sid}: UPOS tak sah '{r['upos']}' (token {r['form']})")
        if has_cycle({r["id"]: r["head"] for r in rows}):
            errs.append(f"{sid}: ada siklus dependensi")
        if not have_text:
            errs.append(f"{sid}: header '# text' tidak ada")

    for line in open(path, encoding="utf-8"):
        line_no += 1
        line = line.rstrip("\n")
        if line.startswith("# sent_id"):
            flush()
            sid = line.split("=",1)[1].strip() if "=" in line else f"L{line_no}"
            rows, have_text = [], False
        elif line.startswith("# text ") or line.startswith("# text="):
            have_text = True
        elif line.startswith("#"):
            continue
        elif line == "":
            flush()
            rows = []
            sid = sid  # keep until next sent_id
        else:
            c = line.split("\t")
            if len(c) != 10:
                errs.append(f"{sid} baris {line_no}: {len(c)} kolom (harus 10)")
                continue
            if "-" in c[0] or "." in c[0]:
                continue  # lewati token majemuk/kosong (multiword/empty node)
            if not c[0].isdigit():
                errs.append(f"{sid} baris {line_no}: ID bukan angka '{c[0]}'")
                continue
            try:
                head = int(c[6]) if c[6] not in ("_","") else -1
            except ValueError:
                errs.append(f"{sid} baris {line_no}: HEAD bukan angka '{c[6]}'")
                head = -1
            if head == -1:
                errs.append(f"{sid} baris {line_no}: HEAD kosong (token {c[1]})")
                head = 0
            rows.append({"id": int(c[0]), "form": c[1], "upos": c[3],
                         "head": head, "deprel": c[7]})
    flush()
    return errs

def main():
    paths = []
    for pat in sys.argv[1:]:
        paths.extend(glob.glob(pat))
    if not paths:
        print("Tidak ada file .conllu. Pemakaian: validate_conllu.py <glob>")
        sys.exit(0)
    total = 0
    for p in sorted(set(paths)):
        errs = validate_file(p)
        if errs:
            print(f"[GAGAL] {p}: {len(errs)} galat")
            for e in errs:
                print("   -", e)
            total += len(errs)
        else:
            print(f"[OK]    {p}")
    if total:
        print(f"\nTotal galat: {total}")
        sys.exit(1)
    print("\nSemua file valid.")

if __name__ == "__main__":
    main()
