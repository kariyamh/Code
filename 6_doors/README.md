Project 6 assignment brief.
See input files in this folder. Write a standalone Python script that performs the tasks described in the roadmap.
Provide output files matching the expected_* files where present.


Project 6 — DOORS export handling and normalization

Objective
Ingest DOORS exports in CSV or simple XML and normalize into a canonical requirements CSV for downstream tools.

Key concepts / libraries
CSV/XML parsing (xml.etree.ElementTree), field mapping, text cleanup, encoding issues.

Expected input / output
Input: doors_export.csv and doors_export.xml.
Output: normalized_requirements.csv with columns id,title,text,source_file.

Deliverable / milestone (graded)

Script proj6_doors_normalize.py that accepts CSV or XML DOORS exports and writes normalized CSV.

Handle common quirks: BOMs, extra whitespace, duplicate IDs.

README explaining supported input formats and example invocations.

Grading rubric

Correct normalization 50

Robust handling of XML and CSV 20

Duplicate ID handling 15

README and CLI 15

Stretch goals

Support simple RTF export parsing (strip RTF control codes).

Produce a small traceability matrix mapping requirement IDs to source files.
