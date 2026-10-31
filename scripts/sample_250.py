#!/usr/bin/env python3
"""Sampling berlapis 250 kalimat lintas genre untuk anotasi UD Batak Toba.

Input : korpus mentah hibah 2025, satu kalimat per baris ATAU CSV berkolom
        teks (dan opsional teks_ind, sumber, strata).
Output: 250_final.csv siap dijadikan template CoNLL-U kosong.

Pemakaian:
    python sample_250.py --input korpus_2025.csv --text-col teks \
        --strata-col strata --seed 42 --out 250_final.csv

Jika file input belum ada, skrip mencetak instruksi dan berhenti.
Sesuaikan KUOTA_STRATA / KUOTA_KONSTRUKSI dengan komposisi nyata korpus.
"""
import argparse, csv, random, re, sys
from collections import defaultdict

KUOTA_STRATA = {"tradisional": 85, "modern": 85, "lisan": 80}
KUOTA_KONSTRUKSI = {
    "diatesis_aktor": 60, "diatesis_pasien": 50,
    "predikat_nonverbal": 40, "preposisi": 40, "negasi": 20,
}
MIN_TOK, MAX_TOK = 4, 25

# Deteksi konstruksi via pola morfologis kasar (untuk penandaan awal, bukan anotasi final)
RE_AKTOR   = re.compile(r"\b(mang|man|mam|manga|ma)[a-z]+", re.I)   # prefiks maN-
RE_PASIEN  = re.compile(r"\bdi[a-z]+", re.I)                         # prefiks di-
RE_PREP    = re.compile(r"\b(di|tu|sian|dohot)\b", re.I)
RE_NEG     = re.compile(r"\b(ndang|dang)\b", re.I)
RE_PART    = re.compile(r"\b(do|ma)\b", re.I)

def tag_konstruksi(teks):
    tags = []
    if RE_AKTOR.search(teks):  tags.append("diatesis_aktor")
    if RE_PASIEN.search(teks): tags.append("diatesis_pasien")
    if RE_PREP.search(teks):   tags.append("preposisi")
    if RE_NEG.search(teks):    tags.append("negasi")
    # predikat non-verbal: tidak ada prefiks verba terdeteksi
    if not RE_AKTOR.search(teks) and not RE_PASIEN.search(teks):
        tags.append("predikat_nonverbal")
    return tags

def n_tok(teks):
    return len(teks.split())

def load(path, text_col, ind_col, strata_col, src_col):
    rows = []
    if path.endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                t = (r.get(text_col) or "").strip()
                if not t:
                    continue
                rows.append({
                    "teks": t,
                    "teks_ind": (r.get(ind_col) or "").strip() if ind_col else "",
                    "strata": (r.get(strata_col) or "").strip().lower() if strata_col else "",
                    "sumber": (r.get(src_col) or "").strip() if src_col else "",
                })
    else:  # satu kalimat per baris
        with open(path, encoding="utf-8") as f:
            for line in f:
                t = line.strip()
                if t:
                    rows.append({"teks": t, "teks_ind": "", "strata": "", "sumber": ""})
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--text-col", default="teks")
    ap.add_argument("--ind-col", default="teks_ind")
    ap.add_argument("--strata-col", default="strata")
    ap.add_argument("--src-col", default="sumber")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="250_final.csv")
    a = ap.parse_args()

    import os
    if not os.path.exists(a.input):
        print(f"[!] File input '{a.input}' belum ada.")
        print("    Sediakan korpus 2025 sebagai CSV (kolom teks, opsional teks_ind, strata, sumber)")
        print("    atau file teks satu kalimat per baris, lalu jalankan ulang.")
        sys.exit(1)

    random.seed(a.seed)
    rows = load(a.input, a.text_col, a.ind_col, a.strata_col, a.src_col)

    # filter panjang & dedup
    seen, cand = set(), []
    for r in rows:
        t = n_tok(r["teks"])
        if MIN_TOK <= t <= MAX_TOK and r["teks"] not in seen:
            seen.add(r["teks"])
            r["panjang_token"] = t
            r["konstruksi"] = tag_konstruksi(r["teks"])
            cand.append(r)
    random.shuffle(cand)
    print(f"kandidat lolos filter: {len(cand)} dari {len(rows)}")

    # jika strata kosong, semua masuk satu pool tanpa kuota strata
    use_strata = any(r["strata"] for r in cand)
    picked, kons_count = [], defaultdict(int)
    strata_count = defaultdict(int)

    def kuota_konstruksi_ok(r):
        # dahulukan kalimat yang mengisi konstruksi yang masih kurang
        return any(kons_count[k] < KUOTA_KONSTRUKSI.get(k, 0) for k in r["konstruksi"])

    target_total = sum(KUOTA_STRATA.values())
    # putaran 1: penuhi konstruksi & strata
    for r in cand:
        if len(picked) >= target_total:
            break
        s = r["strata"] if use_strata else "all"
        cap = KUOTA_STRATA.get(s, target_total) if use_strata else target_total
        if strata_count[s] >= cap:
            continue
        if kuota_konstruksi_ok(r) or not use_strata:
            picked.append(r); strata_count[s] += 1
            for k in r["konstruksi"]:
                kons_count[k] += 1
    # putaran 2: isi sisa sampai 250
    for r in cand:
        if len(picked) >= target_total:
            break
        if r in picked:
            continue
        s = r["strata"] if use_strata else "all"
        cap = KUOTA_STRATA.get(s, target_total) if use_strata else target_total
        if strata_count[s] >= cap:
            continue
        picked.append(r); strata_count[s] += 1

    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sent_id", "strata", "sumber", "teks_batak", "teks_ind",
                    "panjang_token", "konstruksi_target", "catatan"])
        for i, r in enumerate(picked, 1):
            w.writerow([f"btk_pilot-{i:03d}", r["strata"], r["sumber"], r["teks"],
                        r["teks_ind"], r["panjang_token"], "|".join(r["konstruksi"]), ""])

    print(f"terpilih: {len(picked)} kalimat -> {a.out}")
    print("distribusi strata:", dict(strata_count))
    print("cakupan konstruksi:", dict(kons_count))

if __name__ == "__main__":
    main()
