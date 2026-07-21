# Data Validation Script

Automated Python script for detecting and reporting data quality issues in CSV/Excel files.

## Features
- Detects missing values (NULL/empty cells)
- Identifies duplicate rows across all columns or specific keys
- Validates data type consistency (int, float, string, date)
- Flags format inconsistencies (date formats, phone numbers, email patterns)
- Generates automated error report in Excel/HTML

## Usage
```bash
python3 data_validator.py --input data.csv --output report.xlsx
```

## Input
- CSV or Excel file with structured data

## Output
- Structured error report with:
  - Row number
  - Column name
  - Issue type (missing, duplicate, format)
  - Suggested fix

## Technologies
- Python 3.8+
- Pandas, Openpyxl, Numpy

## Author
Vitalie Turcanu
