

# Project 2 — Excel workbooks and multi-sheet reports

##  Overview
See input files in this folder. Write a standalone Python script that performs the tasks described in the roadmap.
Provide output files matching the expected_* files where present.

## Objective
Read multi-sheet Excel files, normalize columns, produce a consolidated report in Excel.

## Key concepts / libraries
* pandas read_excel
* ExcelWriter 
* sheet handling
* column normalization

## Expected input / output
* Input: `employees.xlsx` (sheet: `employees`).
* Output: `dept_report.xlsx` with aggregated metrics (mean salary, total salary) and a small cover sheet describing the report.

## Deliverable / milestone (graded)
* Script proj2_excel_report.py that reads spreadsheet(s), normalizes header names, groups by dept, writes dept_report.xlsx.
* Include a cover sheet (title, generation date).
* README showing how to run locally.

### Grading rubric
| Criteria                                   | Percent |
|:-------------------------------------------|:-------:|
| Correct aggregation and output file        | 45%     |
| Cover sheet present and formatted          | 20%     |
| Robust loading from different sheet names  | 15%     |
| CLI and README                             | 20%     |

## Stretch goals
* Add optional worksheet per department with employee list.
* Add simple formatting (bold headers, autofit columns).

