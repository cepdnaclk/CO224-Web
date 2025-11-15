#!/usr/bin/env python3
"""
Helper script to create LaTeX files from markdown lectures.
This creates skeleton files that you can manually edit.
"""

import re
from pathlib import Path

def get_lecture_number(filename):
    """Extract lecture number from filename"""
    match = re.match(r'Lecture (\d+)', filename.name)
    return int(match.group(1)) if match else 0

def get_lecture_title(filename):
    """Extract title from filename"""
    match = re.match(r'Lecture \d+ - (.+)\.md', filename.name)
    return match.group(1) if match else "Untitled"

def create_latex_skeleton(lecture_num, title, md_file):
    """Create a basic LaTeX file skeleton from markdown"""
    
    # Read markdown to extract structure
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Start LaTeX content
    latex_content = f"""% Lecture {lecture_num:02d}: {title}
% CO224 - Computer Architecture

\\chapter{{{title}}}

"""
    
    # Extract sections from markdown (## headers)
    sections = re.findall(r'^## (.+)$', md_content, re.MULTILINE)
    
    for section in sections:
        # Clean section title
        section_clean = section.strip()
        latex_content += f"\\section{{{section_clean}}}\n\n"
        latex_content += "% TODO: Add content from markdown\n\n"
    
    # Add placeholder if no sections found
    if not sections:
        latex_content += "\\section{Introduction}\n\n% TODO: Add content\n\n"
    
    latex_content += """% Note: Convert markdown content manually for best results
% Remember to:
% - Replace markdown images with \\includegraphics
% - Convert code blocks to \\begin{lstlisting}
% - Convert lists to \\begin{itemize} or \\begin{enumerate}
% - Convert bold/italic with \\textbf{} and \\textit{}
"""
    
    return latex_content

def main():
    """Create LaTeX skeleton files for all lectures"""
    
    markdown_dir = Path('../markdown')
    latex_dir = Path('.')
    
    # Get all markdown files
    md_files = sorted(
        [f for f in markdown_dir.glob('Lecture *.md')],
        key=get_lecture_number
    )
    
    print(f"Found {len(md_files)} markdown files\n")
    print("Creating LaTeX skeleton files...\n")
    
    for md_file in md_files:
        lecture_num = get_lecture_number(md_file)
        title = get_lecture_title(md_file)
        
        output_file = latex_dir / f"lecture-{lecture_num:02d}.tex"
        
        # Skip if file already exists
        if output_file.exists():
            print(f"⊗ Skipped {output_file.name} (already exists)")
            continue
        
        # Create LaTeX skeleton
        latex_content = create_latex_skeleton(lecture_num, title, md_file)
        
        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        print(f"✓ Created {output_file.name} - {title}")
    
    print(f"\n{'='*60}")
    print("✓ LaTeX skeleton files created!")
    print(f"{'='*60}\n")
    print("Next steps:")
    print("1. Edit each lecture-XX.tex file in the latex/ folder")
    print("2. Convert markdown content to LaTeX manually")
    print("3. Compile with: pdflatex main.tex")
    print("4. Run twice for table of contents")

if __name__ == '__main__':
    main()
