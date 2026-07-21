import pandas as pd
import numpy as np
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
import sys

class DataValidator:
    def __init__(self, input_file):
        self.df = pd.read_csv(input_file) if input_file.endswith('.csv') else pd.read_excel(input_file)
        self.issues = []
    
    def check_missing_values(self):
        """Detect NULL and empty cells"""
        for col in self.df.columns:
            missing_rows = self.df[self.df[col].isna()].index.tolist()
            if missing_rows:
                for row in missing_rows:
                    self.issues.append({
                        'row': row + 2,  # +2 for header
                        'column': col,
                        'issue_type': 'missing_value',
                        'severity': 'high'
                    })
    
    def check_duplicates(self):
        """Identify duplicate rows"""
        dupes = self.df[self.df.duplicated(keep=False)]
        for idx, row in dupes.iterrows():
            self.issues.append({
                'row': idx + 2,
                'column': 'all',
                'issue_type': 'duplicate_row',
                'severity': 'medium'
            })
    
    def generate_report(self, output_file):
        """Generate Excel error report"""
        if not self.issues:
            print("✅ No issues found!")
            return
        
        report_df = pd.DataFrame(self.issues)
        report_df.to_excel(output_file, index=False, sheet_name='Issues')
        print(f"✅ Report generated: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python data_validator.py <input_file> <output_file>")
        sys.exit(1)
    
    validator = DataValidator(sys.argv[1])
    validator.check_missing_values()
    validator.check_duplicates()
    validator.generate_report(sys.argv[2])
