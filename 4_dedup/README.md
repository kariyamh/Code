Project 4 assignment brief.
See input files in this folder. Write a standalone Python script that performs the tasks described in the roadmap.
Provide output files matching the expected_* files where present.


Project 4 — Deduplication and fuzzy matching

Objective
Detect and merge duplicate records using exact and approximate matching with minimal dependencies.

Key concepts / libraries
String normalization, difflib.SequenceMatcher, pandas merge, heuristics for canonicalization.

Expected input / output
Input: contacts.csv.
Output: deduped.csv (one record per logical entity) and duplicates_report.txt describing merged rows.

Deliverable / milestone (graded)

Script proj4_dedup.py implementing at least two dedupe strategies: exact on email and fuzzy on name similarity (threshold).

Produce deduped.csv and duplicates_report.txt.

Configurable similarity threshold via CLI.

Grading rubric

Correct deduplication for provided sample 40

Clear merging logic and comments 20

CLI config for threshold 15

Duplicates report quality 25

Stretch goals

Implement canonicalization rules (strip punctuation, stopwords).

Produce provenance mapping file showing original→canonical.

Notes: Use stdlib difflib to avoid external fuzzy libs.
