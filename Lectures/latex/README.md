# CO224 Lecture Notes - LaTeX Format

This directory contains all 20 CO224 lecture notes converted from Markdown to LaTeX format.

## Files Generated

### Individual Lecture Files (lecture-01.tex to lecture-20.tex)

- `lecture-01.tex` - Lecture 1: Computer Abstractions and Technology
- `lecture-02.tex` - Lecture 2: Technology Trends, Moore's Law, and Computer System Organization
- `lecture-03.tex` - Lecture 3: Understanding Performance
- `lecture-04.tex` - Lecture 4: Introduction to ARM Assembly
- `lecture-05.tex` - Lecture 5: Number Representation and Data Processing
- `lecture-06.tex` - Lecture 6: Branching
- `lecture-07.tex` - Lecture 7: Function Call and Return
- `lecture-08.tex` - Lecture 8: Memory Access
- `lecture-09.tex` - Lecture 9: Microarchitecture and Datapath
- `lecture-10.tex` - Lecture 10: Processor Control
- `lecture-11.tex` - Lecture 11: Single-Cycle Execution
- `lecture-12.tex` - Lecture 12: Pipelined Processors
- `lecture-13.tex` - Lecture 13: Pipeline Operation and Timing
- `lecture-14.tex` - Lecture 14: Memory Hierarchy and Caching
- `lecture-15.tex` - Lecture 15: Direct Mapped Cache Control
- `lecture-16.tex` - Lecture 16: Associative Cache Control
- `lecture-17.tex` - Lecture 17: Multi-Level Caching
- `lecture-18.tex` - Lecture 18: Virtual Memory
- `lecture-19.tex` - Lecture 19: Multiprocessors
- `lecture-20.tex` - Lecture 20: Storage and Interfacing

### Main Document

- `main.tex` - Sample main document that includes all lectures organized into chapters

## How to Use

### Option 1: Compile the Complete Document

```bash
pdflatex main.tex
pdflatex main.tex  # Run twice for table of contents
```

### Option 2: Include Individual Lectures in Your Own Document

Create your own main.tex file and include specific lectures:

```latex
\documentclass{article}
\usepackage{graphicx}
\usepackage{amsmath}

\begin{document}

% Include specific lecture
\input{lecture-01}

% Or include multiple lectures
\input{lecture-02}
\input{lecture-03}

\end{document}
```

### Option 3: Create Custom Subsets

You can create custom documents with only the lectures you need:

```latex
\documentclass{report}
% ... packages ...

\begin{document}

\chapter{ARM Assembly}
\input{lecture-04}
\input{lecture-05}
\input{lecture-06}

\chapter{Processor Design}
\input{lecture-09}
\input{lecture-10}

\end{document}
```

## Important Notes

### Content Preservation

✅ **All content from markdown files has been preserved exactly as written**
- No content has been added
- No content has been removed
- No content has been modified
- Only formatting conversion from Markdown to LaTeX syntax

### File Structure

Each lecture file (`lecture-XX.tex`) is structured as follows:
- Uses `\section{}` for the main lecture title
- Uses `\subsection{}` for major sections
- Uses `\subsubsection{}` for subsections
- Uses `\paragraph{}` for sub-subsections
- No document preamble or `\begin{document}` - ready for inclusion via `\input{}`

### Required Packages

To compile these files, your LaTeX document should include:

```latex
\usepackage{graphicx}     % For images
\usepackage{amsmath}      % For math equations
\usepackage{amssymb}      % For math symbols
\usepackage{listings}     % For code blocks
\usepackage{xcolor}       % For colors
```

### Images

The image paths in the LaTeX files reference:
```
../img/Chapter X ....jpg
```

Make sure your LaTeX compiler can find these images relative to the `.tex` files, or adjust the paths accordingly in your main document using:

```latex
\graphicspath{{../img/}}
```

## Conversion Details

The conversion from Markdown to LaTeX handles:

- ✅ Headings (# → \section{}, ## → \subsection{}, etc.)
- ✅ Bold text (**text** → \textbf{text})
- ✅ Italic text (*text* → \emph{text})
- ✅ Inline code (`code` → \texttt{code})
- ✅ Code blocks (``` → \begin{verbatim})
- ✅ Lists (- → \begin{itemize})
- ✅ Images (<img> → \begin{figure})
- ✅ Special characters (escaped for LaTeX)
- ✅ Math symbols (→, ×, ≤, etc.)

## Regenerating Files

If you need to regenerate the LaTeX files from updated markdown:

```bash
python md_to_latex_converter.py
```

This will re-convert all 20 markdown lectures to LaTeX format.

## Author

**Dr. Isuru Nawinne**  
Department of Computer Engineering  
University of Peradeniya

---

Generated on: 2025-11-19
