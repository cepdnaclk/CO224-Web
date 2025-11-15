# CO224 PDF Generator

This folder contains tools to convert the CO224 lecture markdown files into a professional PDF document.

## Prerequisites

### 1. Install Pandoc

Pandoc is required to convert markdown to LaTeX.

**Windows:**

```powershell
# Using Chocolatey
choco install pandoc

# Or download from: https://pandoc.org/installing.html
```

**Alternative:** Download installer from https://github.com/jgm/pandoc/releases

### 2. Install LaTeX Distribution

A LaTeX distribution is needed to compile the PDF.

**Windows - MiKTeX (Recommended):**

```powershell
# Using Chocolatey
choco install miktex

# Or download from: https://miktex.org/download
```

**Alternative:** Download installer from https://miktex.org/download

### 3. Verify Installations

```powershell
# Check pandoc
pandoc --version

# Check pdflatex
pdflatex --version
```

## Usage

### Option 1: Automatic Generation (Recommended)

Run the Python script to automatically convert all lectures to PDF:

```powershell
python generate_pdf.py
```

This will:

1. Convert all 20 lecture markdown files to LaTeX
2. Combine them into a single document with table of contents
3. Compile to PDF using pdflatex
4. Clean up temporary files

### Option 2: Manual LaTeX Compilation

If you want to edit the LaTeX file before compiling:

```powershell
# Generate LaTeX only (edit the script to skip PDF compilation)
python generate_pdf.py

# Then manually compile:
pdflatex CO224-Complete-Notes.tex
pdflatex CO224-Complete-Notes.tex  # Run twice for TOC
```

### Option 3: Using Pandoc Directly

For a simpler conversion without custom LaTeX template:

```powershell
# Navigate to project root
cd "d:\Academics\Projects\isuru sir\CO224-Web"

# Convert all lectures to PDF
pandoc Lectures/Lecture*.md -o pdf-generator/CO224-Notes-Simple.pdf --toc --number-sections
```

## Output Files

After successful generation:

- **CO224-Complete-Notes.tex** - LaTeX source file (editable)
- **CO224-Complete-Notes.pdf** - Final PDF document

## Deploying to Website

Once the PDF is generated, copy it to the materials folder:

```powershell
Copy-Item "CO224-Complete-Notes.pdf" "../materials/CO224-Complete-Notes.pdf"
```

Then commit and push:

```powershell
cd ..
git add materials/CO224-Complete-Notes.pdf
git commit -m "Add complete lecture notes PDF"
git push origin main
```

## Customization

### Editing the LaTeX Template

The LaTeX template is embedded in `generate_pdf.py`. You can customize:

- **Page layout**: Modify the `\geometry{}` settings
- **Fonts**: Add font packages like `\usepackage{times}`
- **Colors**: Change the color definitions
- **Chapter formatting**: Modify `\titleformat{}` commands

### Adding a Cover Image

To add a cover image to the title page:

1. Place image in the `pdf-generator` folder
2. Edit `generate_pdf.py` and add in title page section:
   ```latex
   \includegraphics[width=0.5\textwidth]{your-image.png}
   ```

## Troubleshooting

### Error: "pandoc not found"

- Install pandoc from https://pandoc.org/installing.html
- Restart your terminal after installation

### Error: "pdflatex not found"

- Install MiKTeX or another LaTeX distribution
- Add LaTeX to your PATH environment variable
- Restart your terminal

### Error: "Missing packages"

If MiKTeX prompts for missing packages:

- Click "Install" to automatically download them
- Or manually install: `mpm --install package-name`

### Images not showing in PDF

- Ensure image paths in markdown files are correct
- Images should be in `Lectures/img/` folder
- The script automatically adjusts paths for LaTeX

### PDF compilation errors

- Check the `.log` file for detailed error messages
- Ensure all special characters in markdown are properly escaped
- Try compiling the `.tex` file manually to see full error output

## Advanced Options

### Custom Pandoc Template

Create a custom pandoc template:

```powershell
# Get default template
pandoc -D latex > custom-template.tex

# Edit custom-template.tex as needed

# Use custom template
pandoc Lectures/Lecture*.md -o output.pdf --template=custom-template.tex
```

### Include Only Specific Lectures

Edit `generate_pdf.py` and modify the file selection:

```python
# Only lectures 1-10
lecture_files = sorted(
    [f for f in lectures_dir.glob('Lecture [1-9].md') or
     f for f in lectures_dir.glob('Lecture 10.md')],
    key=get_lecture_number
)
```

## Additional Resources

- [Pandoc Manual](https://pandoc.org/MANUAL.html)
- [LaTeX Documentation](https://www.latex-project.org/help/documentation/)
- [MiKTeX Documentation](https://miktex.org/docs)

---

**Need Help?** Check the error messages carefully and ensure all prerequisites are installed correctly.
