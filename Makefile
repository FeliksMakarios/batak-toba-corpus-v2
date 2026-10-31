# Alur kerja korpus UD Batak Toba
# Sesuaikan INPUT dengan file korpus mentah 2025 Anda.
INPUT ?= corpus_2025.csv
SEED  ?= 42
PILOT  = corpus/pilot

.PHONY: help sample template validate stats iaa reconcile clean

help:
	@echo "Target:"
	@echo "  make sample     - sampling 250 kalimat berlapis dari INPUT=$(INPUT)"
	@echo "  make template   - buat CoNLL-U kosong dari 250_final.csv"
	@echo "  make validate   - validasi semua file CoNLL-U"
	@echo "  make stats       - statistik korpus"
	@echo "  make iaa A=.. B=..       - hitung kesepakatan antaranotator"
	@echo "  make reconcile A=.. B=.. - lembar rekonsiliasi perbedaan"

sample:
	python scripts/sample_250.py --input $(INPUT) --seed $(SEED) --out $(PILOT)/250_final.csv

template:
	python scripts/make_conllu_template.py --input $(PILOT)/250_final.csv --out $(PILOT)/btk_pilot.blank.conllu

validate:
	python scripts/validate_conllu.py "$(PILOT)/*.conllu"

stats:
	python scripts/corpus_stats.py "$(PILOT)/*.conllu" --out evaluation/corpus_stats.md

iaa:
	python scripts/compute_iaa.py --a $(A) --b $(B) --report evaluation/iaa_report.md

reconcile:
	python scripts/reconcile.py --a $(A) --b $(B) --out evaluation/reconcile.tsv

clean:
	find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
