"""
Project Name:   HoweLab8_read_csv.py
Purpose:        Quick inspection utility — reads the source CSV and
                prints the header row and first data row to verify
                the file loaded correctly before running the main program.
Description:    Opens cities_living_cost.csv using csv.reader, reads the
                header and all data rows into memory, then prints the
                header and first row for a quick sanity check.
Created Date:   2026-03-29
Author:         Daniel Howe
Version:        1.0
"""

# Resource Disclosure:
# Dataset source: The lab required a CSV from data.gov, but every dataset
# I found there was far too large (tens of thousands of rows) to verify
# results by hand. I switched to a Kaggle cost-of-living dataset
# (cities_living_cost.csv) which has a manageable 224 rows and 57 columns
# and still meets the lab requirements of ≥100 rows and ≥5 columns.
# No AI tools were used in this utility script.

import csv

source_file = 'cities_living_cost.csv'

with open(source_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = list(reader)

print(f'Header: {header}')
print(f'First row: {rows[0]}')
