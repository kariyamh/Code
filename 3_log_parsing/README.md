Project 3 assignment brief.
See input files in this folder. Write a standalone Python script that performs the tasks described in the roadmap.
Provide output files matching the expected_* files where present.


Project 3 — Text log parsing and event extraction

Objective
Parse free-form logs, extract events, and emit filtered reports.

Key concepts / libraries
Text I/O, regex, datetime parsing, simple parsers, error extraction.

Expected input / output
Input: system.log.
Output: errors.txt (only ERROR lines), events.csv (timestamp,level,message).

Deliverable / milestone (graded)

Script proj3_log_parser.py that parses system.log, extracts structured rows and writes events.csv and errors.txt.

Handle malformed timestamps and produce parse_errors.log.

Grading rubric

Correct extraction 50

Correct error filtering 20

Robustness and logging 15

README and CLI 15

Stretch goals

Add time-window filtering.

Support ISO and non-ISO timestamp formats.

