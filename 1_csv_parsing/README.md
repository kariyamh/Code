# Project 1 — CSV parsing and simple aggregation

This README clarifies the assignment and provides a sample usage. Update the example invocation to match your script's actual CLI and file names.


## Objective

Parse a CSV of sales records, validate data types, handle malformed rows, and produce a per-customer total report.

## Key concepts / libraries

- CSV I/O (Python's built-in `csv` module or `pandas 
`)
- Validation and error handling
- Grouping and aggregation (sum per customer)

## Repository files

- `sales.csv` — input sales data (orders)
- `expected_customer_totals.csv` — example/expected output for grading
- `README.md` — this file

If you add your script, place it in this folder (an example name used below: `proj1_csv_summary.py`).

## Expected input / output

- Input: `sales.csv` (rows of orders). Each row should include at minimum a customer identifier and an amount value.
- Output: `customer_totals.csv` — a CSV with columns like `customer,total_amount` containing one row per customer with the summed amount.
- Optional: `parse.log` — a plain text log listing skipped/malformed rows and reasons.


## Example CLI

An example script invocation might look like this:

```bash
python proj1_csv_summary.py sales.csv customer_totals.csv --log parse.log
```

Script expectations:

- Validate that amount values are numeric; skip or log rows that are malformed.
- Group by customer and write the summed amounts to the output CSV.

## Grading rubric (0–100)

| Criteria                                         | Points |
|--------------------------------------------------|--------|
| Correct grouping and sums                        |   40   |
| Handles malformed rows gracefully (and logs them)|   20   |
| Proper CLI args and README documentation         |   20   |
| Code style and comments                          |   20   |
| **Total**                                        | **100**|

## Stretch goals (optional)

- Add a date-range filter CLI option to include only orders within a given date window.
- Produce an Excel output with a chart (using `openpyxl` or `pandas.ExcelWriter`).