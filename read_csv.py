#!/usr/bin/env python3
"""
CSV Reader Script
Reads all CSV files from the csv/ directory and displays them in the console.
"""

import os
import csv
import sys
from pathlib import Path


def read_csv_file(file_path):
    """
    Read a single CSV file and return its contents.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        tuple: (headers, rows) or None if error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            rows = list(csv_reader)
            return headers, rows
    except Exception as e:
        print(f"❌ Error reading {file_path}: {str(e)}")
        return None


def display_csv_data(file_path, headers, rows):
    """
    Display CSV data in a formatted way in the console.
    
    Args:
        file_path (str): Path to the CSV file
        headers (list): Column headers
        rows (list): Data rows
    """
    file_name = os.path.basename(file_path)
    
    print("\n" + "="*80)
    print(f"📄 FILE: {file_name}")
    print("="*80)
    
    if not headers:
        print("⚠️  Empty file or no headers found")
        return
    
    # Calculate column widths
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print headers
    header_line = " | ".join(str(h).ljust(w) for h, w in zip(headers, col_widths))
    print(f"\n{header_line}")
    print("-" * len(header_line))
    
    # Print rows
    if rows:
        for row in rows:
            row_line = " | ".join(
                str(cell).ljust(col_widths[i]) if i < len(col_widths) else str(cell)
                for i, cell in enumerate(row)
            )
            print(row_line)
        print(f"\n📊 Total rows: {len(rows)}")
    else:
        print("⚠️  No data rows found")
    
    print("="*80)


def main():
    """
    Main function to read and display all CSV files from the csv/ directory.
    """
    print("\n" + "🚀 CSV READER SCRIPT STARTED" + "\n")
    print("="*80)
    
    # Get the csv directory path
    script_dir = Path(__file__).parent
    csv_dir = script_dir / 'csv'
    
    # Check if csv directory exists
    if not csv_dir.exists():
        print(f"❌ Error: CSV directory not found at {csv_dir}")
        sys.exit(1)
    
    # Find all CSV files
    csv_files = list(csv_dir.glob('*.csv'))
    
    if not csv_files:
        print(f"⚠️  No CSV files found in {csv_dir}")
        print("="*80)
        return
    
    print(f"✅ Found {len(csv_files)} CSV file(s) in the csv/ directory")
    print("="*80)
    
    # Process each CSV file
    for csv_file in sorted(csv_files):
        result = read_csv_file(csv_file)
        if result:
            headers, rows = result
            display_csv_data(csv_file, headers, rows)
    
    print("\n" + "✅ CSV READER SCRIPT COMPLETED" + "\n")


if __name__ == "__main__":
    main()
