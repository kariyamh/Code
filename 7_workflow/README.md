Project 7 assignment brief.
See input files in this folder. Write a standalone Python script that performs the tasks described in the roadmap.
Provide output files matching the expected_* files where present.


Project 7 — Repeatable automation: config-driven workflow

Objective
Build a small framework that reads a JSON config and applies transformations to data files to produce outputs reproducibly.

Key concepts / libraries
CLI parsing (argparse), JSON config, modular ops, logging, reproducibility.

Expected input / output
Input: raw.csv and config.json.
Output: results.csv with operations applied per config.

Deliverable / milestone (graded)

Script proj7_workflow.py that reads config.json and performs operations (add, multiply, filter, rename).

Provide parameter validation and a dry-run mode.

Include unit tests or sample runs in README.

Grading rubric

Correct operations application 40

Robust config validation and error messages 25

Dry-run mode works 15

README and reproducibility notes 20

Stretch goals

Support chaining of operations and simple templating for filenames.

Provide a simple job-run log with timestamps.
