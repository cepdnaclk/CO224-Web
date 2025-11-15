#!/usr/bin/env python3
"""
Convert CO224 Lecture Markdown files to a single LaTeX document and generate PDF.
Requires: pandoc, texlive (or similar LaTeX distribution)
"""

import os
import subprocess
import re
from pathlib import Path

def get_lecture_number(filename):
    """Extract lecture number from filename"""
    match = re.match(r'Lecture (\d+)', filename.name)
    return int(match.group(1)) if match else 0

def convert_md_to_latex():
    """Convert all lecture markdown files to a combined LaTeX document"""
    
    lectures_dir = Path('../Lectures')
    output_dir = Path('.')
    
    # Get all lecture files sorted by number
    lecture_files = sorted(
        [f for f in lectures_dir.glob('Lecture *.md')],
        key=get_lecture_number
    )
    
    print(f"Found {len(lecture_files)} lecture files")
    
    # Create LaTeX preamble
    latex_content = r'''\documentclass[12pt,a4paper]{book}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{tocloft}

% Page setup
\geometry{
    a4paper,
    left=2.5cm,
    right=2.5cm,
    top=2.5cm,
    bottom=2.5cm
}

% Header/Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\leftmark}
\fancyhead[R]{\thepage}
\fancyfoot[C]{CO224 - Computer Architecture}

% Colors
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

% Code listing style
\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}
\lstset{style=mystyle}

% Hyperlink setup
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=cyan,
    pdftitle={CO224 Computer Architecture - Complete Lecture Notes},
    pdfauthor={Dr. Isuru Nawinne},
}

% Title formatting
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{0pt}{40pt}

\begin{document}

% Title Page
\begin{titlepage}
    \centering
    \vspace*{2cm}
    
    {\Huge\bfseries CO224: Computer Architecture\par}
    \vspace{1cm}
    {\Large Complete Lecture Notes\par}
    \vspace{2cm}
    
    {\Large\itshape Dr. Isuru Nawinne\par}
    \vspace{0.5cm}
    {\large Senior Lecturer\par}
    {\large Department of Computer Engineering\par}
    {\large University of Peradeniya\par}
    
    \vfill
    
    {\large \today\par}
\end{titlepage}

% Table of Contents
\tableofcontents
\clearpage

'''
    
    # Process each lecture
    for i, lecture_file in enumerate(lecture_files):
        lecture_num = i + 1
        print(f"Processing: {lecture_file.name}")
        
        # Read markdown content
        with open(lecture_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Fix image paths for LaTeX
        md_content = re.sub(
            r'<img src="img/',
            r'<img src="../Lectures/img/',
            md_content
        )
        
        # Convert markdown to LaTeX using pandoc
        try:
            result = subprocess.run(
                ['pandoc', '-f', 'markdown', '-t', 'latex', '--wrap=preserve'],
                input=md_content,
                capture_output=True,
                text=True,
                check=True
            )
            
            latex_chapter = result.stdout
            
            # Add chapter marker
            latex_content += f"\n% Lecture {lecture_num}\n"
            latex_content += latex_chapter
            latex_content += "\n\\clearpage\n\n"
            
        except subprocess.CalledProcessError as e:
            print(f"Error converting {lecture_file.name}: {e}")
            continue
        except FileNotFoundError:
            print("ERROR: pandoc not found. Please install pandoc first.")
            print("Install: https://pandoc.org/installing.html")
            return False
    
    # Close LaTeX document
    latex_content += r'''
\end{document}
'''
    
    # Write combined LaTeX file
    output_file = output_dir / 'CO224-Complete-Notes.tex'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"\n✓ Created LaTeX file: {output_file}")
    return True

def compile_latex():
    """Compile LaTeX to PDF"""
    print("\nCompiling LaTeX to PDF...")
    
    tex_file = 'CO224-Complete-Notes.tex'
    
    try:
        # Run pdflatex twice for proper references and TOC
        for run in [1, 2]:
            print(f"\nPDFLaTeX run {run}/2...")
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', tex_file],
                capture_output=True,
                text=True,
                check=True
            )
            
            if run == 2:
                print("✓ PDF compilation successful!")
    
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LaTeX: {e}")
        print("\nLaTeX output:")
        print(e.stdout)
        return False
    except FileNotFoundError:
        print("ERROR: pdflatex not found. Please install a LaTeX distribution.")
        print("Options:")
        print("  - Windows: MiKTeX (https://miktex.org/)")
        print("  - Linux: sudo apt-get install texlive-full")
        print("  - Mac: MacTeX (https://www.tug.org/mactex/)")
        return False
    
    return True

def cleanup_temp_files():
    """Remove temporary LaTeX files"""
    print("\nCleaning up temporary files...")
    temp_extensions = ['.aux', '.log', '.out', '.toc', '.lof', '.lot']
    
    for ext in temp_extensions:
        temp_file = Path(f'CO224-Complete-Notes{ext}')
        if temp_file.exists():
            temp_file.unlink()
            print(f"  Removed {temp_file.name}")

def main():
    """Main function"""
    print("=" * 60)
    print("CO224 Lecture Notes - LaTeX/PDF Generator")
    print("=" * 60)
    
    # Convert markdown to LaTeX
    if not convert_md_to_latex():
        print("\n❌ Failed to convert markdown to LaTeX")
        return
    
    # Compile to PDF
    if not compile_latex():
        print("\n❌ Failed to compile PDF")
        print("You can still use the .tex file and compile it manually.")
        return
    
    # Clean up
    cleanup_temp_files()
    
    print("\n" + "=" * 60)
    print("✓ SUCCESS!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - CO224-Complete-Notes.tex (LaTeX source)")
    print("  - CO224-Complete-Notes.pdf (Final PDF)")
    print("\n💡 Copy the PDF to ../materials/ folder for website download")

if __name__ == '__main__':
    main()
