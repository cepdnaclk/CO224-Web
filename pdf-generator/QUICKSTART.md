# 📚 CO224 PDF Generator - Quick Start Guide

## ✅ What You Have

A complete PDF generation system with **two options**:

1. **Simple Method** (Recommended) - Uses Pandoc only
2. **Advanced Method** - Full LaTeX control with custom formatting

## 🚀 Quick Start (Choose One)

### Option A: Simple PDF Generation (Easiest)

**Step 1: Install Pandoc**

Download and install Pandoc from: https://github.com/jgm/pandoc/releases/latest

- Download: `pandoc-3.x-windows-x86_64.msi`
- Run installer
- Restart your terminal

**Step 2: Install MiKTeX (LaTeX)**

Download and install MiKTeX from: https://miktex.org/download

- Download: `basic-miktex-24.x-x64.exe`
- Run installer (Basic MiKTeX is sufficient)
- During first use, allow it to install packages automatically

**Step 3: Generate PDF**

```powershell
cd "d:\Academics\Projects\isuru sir\CO224-Web\pdf-generator"
python generate_pdf_simple.py
```

**Done!** Your PDF will be: `CO224-Complete-Notes.pdf`

### Option B: Advanced PDF (Custom LaTeX Template)

Requires same prerequisites as Option A, then:

```powershell
python generate_pdf.py
```

This gives you:

- `CO224-Complete-Notes.tex` (editable LaTeX)
- `CO224-Complete-Notes.pdf` (final PDF)

## 📦 Installation Steps (Detailed)

### 1. Install Pandoc

**Method 1: Direct Download (Recommended)**

1. Go to: https://github.com/jgm/pandoc/releases/latest
2. Download: `pandoc-3.x-windows-x86_64.msi`
3. Run installer and follow prompts
4. Restart PowerShell

**Method 2: Using Chocolatey**

```powershell
choco install pandoc
```

**Verify Installation:**

```powershell
pandoc --version
```

### 2. Install MiKTeX (LaTeX Distribution)

**Method 1: Direct Download (Recommended)**

1. Go to: https://miktex.org/download
2. Download: `basic-miktex-24.x-x64.exe`
3. Run installer
4. Important: Enable "Install packages on-the-fly: Yes"

**Method 2: Using Chocolatey**

```powershell
choco install miktex
```

**Verify Installation:**

```powershell
pdflatex --version
```

### 3. Restart Your Terminal

After installing both tools, close and reopen PowerShell.

## 🎯 Usage

### Generate PDF from Markdown

```powershell
# Navigate to pdf-generator folder
cd "d:\Academics\Projects\isuru sir\CO224-Web\pdf-generator"

# Simple method (recommended for first time)
python generate_pdf_simple.py

# OR Advanced method (custom LaTeX)
python generate_pdf.py
```

### Deploy to Website

After generating the PDF:

```powershell
# Copy to materials folder
Copy-Item "CO224-Complete-Notes.pdf" "../materials/"

# Commit and push
cd ..
git add materials/CO224-Complete-Notes.pdf
git commit -m "Add complete lecture notes PDF"
git push origin main
```

## 📁 Files in This Folder

- **generate_pdf_simple.py** - Simple PDF generation using Pandoc
- **generate_pdf.py** - Advanced with custom LaTeX template
- **README.md** - Detailed documentation
- **QUICKSTART.md** - This file
- **.gitignore** - Keeps temp files out of git

## ❓ Troubleshooting

### "pandoc not found"

- Install Pandoc from: https://github.com/jgm/pandoc/releases
- Restart your terminal
- Run: `pandoc --version` to verify

### "pdflatex not found"

- Install MiKTeX from: https://miktex.org/download
- Restart your terminal
- Run: `pdflatex --version` to verify

### Missing LaTeX Packages

If MiKTeX shows a dialog asking to install packages:

- Click "Install" (recommended)
- Or: Enable automatic package installation in MiKTeX settings

### Images Not Showing

- Ensure `Lectures/img/` folder has all images
- Check that image paths in markdown are correct
- The scripts automatically adjust paths

### Python Error

Make sure you're in the correct folder:

```powershell
cd "d:\Academics\Projects\isuru sir\CO224-Web\pdf-generator"
```

## 🎨 Customization

### Edit LaTeX Template

For the advanced method, edit `generate_pdf.py`:

- **Line ~32**: Change document class, margins, fonts
- **Line ~125**: Modify title page content
- **Line ~135**: Customize table of contents

### Include Only Certain Lectures

Edit either script and modify:

```python
lecture_files = [
    lectures_dir / 'Lecture 1 - Computer Abstractions.md',
    lectures_dir / 'Lecture 2 - Technology Trends.md',
    # Add only the lectures you want
]
```

## 💡 Tips

1. **First Time Setup**: Allow 10-15 minutes for installations
2. **Package Downloads**: First PDF generation takes longer (downloading LaTeX packages)
3. **Editing**: Use the `.tex` file if you need to manually adjust formatting
4. **Preview**: Check the PDF before deploying to website

## 📚 What Gets Generated

The PDF includes:

- ✅ Professional title page with course info
- ✅ Table of contents with page numbers
- ✅ All 20 lectures in order
- ✅ All images and diagrams
- ✅ Code blocks with syntax highlighting
- ✅ Hyperlinks (clickable TOC)
- ✅ Page numbers and headers

## 🔗 Useful Links

- [Pandoc Documentation](https://pandoc.org/MANUAL.html)
- [MiKTeX Documentation](https://miktex.org/docs)
- [LaTeX Tutorial](https://www.overleaf.com/learn)

---

**Ready to start?** Install Pandoc and MiKTeX, then run `python generate_pdf_simple.py`! 🚀
