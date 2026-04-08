# Lab 8 TODO

## Setup & Data

- [x] Choose and clean the source CSV file (≥100 rows, ≥5 columns, with header)
- [x] Verify `cities_living_cost.csv` in `HoweLab8/` meets requirements (224 data rows, 57 columns)

## Reading & Validation

- [x] Read the CSV into a list of lists (separate header and data rows) — `HoweLab8_main.py`
- [x] Validate row and column counts (≥100 rows, ≥5 columns)
- [x] Add full validation: skip completely empty rows; validate cost index is a real number

## Processing

- [x] Generate the `City_Cost_Summary` column from city and cost index (e.g. `Turin - Index 65.63`)
- [x] Add the `Review_Flag` column with value `-1` for every row
- [x] Update the header to include both new columns (`City_Cost_Summary`, `Review_Flag`)

## Output

- [x] Create a new output subdirectory (`HoweLab8/processed_data`)
- [x] Write the updated data to `cities_living_cost_updated.csv` in the subdirectory

## Exception Handling

- [x] Wrap file open/read in `try/except` (catches `FileNotFoundError`, `PermissionError`, `Exception`)
- [x] Wrap row processing in `try/except` (catches `IndexError`, `ValueError`)
- [x] Wrap subdirectory creation and file write in `try/except` (catches `PermissionError`, `OSError`)

## Code Quality & Submission

- [x] Add file header comment (name, course, lab title, date, description)
- [x] Add resource disclosure comment block below the file header
- [x] Review and clean up variable names and code organization
- [x] Test the full program end-to-end — 175 rows written (49 removed with Cost_index 0.0), `City_Cost_Summary` and `Review_Flag` confirmed correct
- [ ] Submit all script files and source CSV on Canvas (do not submit generated CSV)

## Extra Credit (optional, +20 pts)

- [x] Add a data-cleaning step that removes rows/columns with empty or invalid values
- [x] Document the cleaning algorithm in comments or a design doc
