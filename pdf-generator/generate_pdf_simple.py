#!/usr/bin/env python3
"""
Simple PDF generator using Pandoc directly.
This is easier and requires fewer dependencies than the full LaTeX approach.
"""

import subprocess
import sys
from pathlib import Path
import re

def get_lecture_number(filename):
    """Extract lecture number from filename"""
    match = re.match(r'Lecture (\d+)', filename.name)
    return int(match.group(1)) if match else 0

def check_pandoc():
    """Check if pandoc is installed"""
    try:
        result = subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERROR: pandoc not found!")
        print("\nPlease install pandoc:")
        print("  Windows: choco install pandoc")
        print("  Or download from: https://pandoc.org/installing.html")
        return False

def generate_pdf_simple():
    """Generate PDF using pandoc directly"""
    
    if not check_pandoc():
        return False
    
    lectures_dir = Path('../Lectures')
    
    # Get all lecture files sorted by number
    lecture_files = sorted(
        [f for f in lectures_dir.glob('Lecture *.md')],
        key=get_lecture_number
    )
    
    print(f"\nFound {len(lecture_files)} lecture files")
    print("Generating PDF with Pandoc...\n")
    
    # Prepare file list
    file_list = [str(f) for f in lecture_files]
    
    # Pandoc command
    output_file = 'CO224-Complete-Notes.pdf'
    
    cmd = [
        'pandoc',
        *file_list,
        '-o', output_file,
        '--toc',                          # Table of contents
        '--toc-depth=3',                  # TOC depth
        '--number-sections',              # Number sections
        '--pdf-engine=xelatex',           # Use xelatex for better Unicode support
        '-V', 'geometry:margin=2.5cm',    # Page margins
        '-V', 'documentclass=book',       # Use book class
        '-V', 'fontsize=12pt',            # Font size
        '-V', 'papersize=a4',             # Paper size
        '-V', 'mainfont=Arial',           # Use Arial for Unicode support
        '--metadata', 'title=CO224: Computer Architecture - Complete Lecture Notes',
        '--metadata', 'author=Dr. Isuru Nawinne',
        '--metadata', 'date=' + subprocess.check_output(['date', '/T'], shell=True).decode().strip()
    ]
    
    try:
        # Run pandoc
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        print("✓ PDF generated successfully!")
        print(f"\nOutput file: {output_file}")
        print("\n💡 Copy to materials folder:")
        print(f"   Copy-Item '{output_file}' '../materials/'")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to generate PDF")
        print(f"\nError output:\n{e.stderr}")
        return False

def main():
    print("=" * 60)
    print("CO224 PDF Generator (Simple)")
    print("=" * 60)
    
    if generate_pdf_simple():
        print("\n" + "=" * 60)
        print("✓ SUCCESS!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("✗ FAILED")
        print("=" * 60)
        sys.exit(1)

if __name__ == '__main__':
    main()
