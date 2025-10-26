Project 8 assignment brief.
See input files in this folder. Write a standalone Python script that performs the tasks described in the roadmap.
Provide output files matching the expected_* files where present.


Project 8 — Packaging, CLI, and unit tests for internal tools

Objective
Produce a small reusable module, a CLI wrapper, and unit tests. Demonstrate packaging and test automation.

Key concepts / libraries
Module design, argparse CLI, unittest or simple test runner, basic packaging layout.

Expected input / output
Input: none required besides test files.
Output: test output (console) showing pass/fail. Optionally produce a small artifact like results.txt.

Deliverable / milestone (graded)

Module mymodule.py with at least two functions (e.g., add, dedupe_rows).

CLI proj8_cli.py that uses the module.

Unit tests test_mymodule.py and a script to run them producing test_results.txt.

README with instructions to run tests and CLI.

Grading rubric

Tests pass for provided cases 40

CLI functions work and handle bad input 25

Code organization and docstrings 20

README and run instructions 15

Stretch goals

Provide a simple setup.py or packaging notes to create an installable wheel for offline use.

Add CI-style local script run_all_tests.sh.
