# CO224 LaTeX Lecture Notes

This folder contains the LaTeX source files for generating the complete CO224 lecture notes PDF.

## 📁 Folder Structure


Lectures/
├── markdown/          # Original markdown lecture files
├── html/              # HTML versions for website
├── latex/             # LaTeX source files (YOU EDIT THESE)
│   ├── main.tex      # Main document (includes all lectures)
│   ├── lecture-01.tex # Individual lecture files
│   ├── lecture-02.tex
│   ├── ...
│   └── lecture-20.tex
└── img/               # Images used in all formats


## 🚀 Quick Start

### Step 1: Create LaTeX Skeleton Files

Run this to create basic LaTeX files from markdown:

bash
cd Lectures/latex
python create_skeletons.py


This creates `lecture-01.tex` through `lecture-20.tex` with basic structure.

### Step 2: Edit LaTeX Files

Edit each `lecture-XX.tex` file to convert markdown content to LaTeX:

- Replace markdown images: `![](img/file.jpg)` → `\includegraphics{../img/file.jpg}`
- Convert code blocks → `\begin{lstlisting}...\end{lstlisting}`
- Convert lists → `\begin{itemize}` or `\begin{enumerate}`
- Convert **bold** → `\textbf{bold}`
- Convert _italic_ → `\textit{italic}`

### Step 3: Compile PDF

bash
cd Lectures/latex
pdflatex main.tex
pdflatex main.tex    # Run twice for TOC and references


Or use the provided script:

bash
.\compile.ps1


## 📝 File Descriptions

### `main.tex`

The main LaTeX document that:

- Sets up the document class and packages
- Defines styling and formatting
- Includes the title page
- Includes all lecture files
- Organizes lectures into 5 parts

### `lecture-XX.tex`

Individual lecture files. Each should contain:

- Chapter title
- Sections and subsections
- Content, images, code blocks
- Examples and exercises

### `lecture-template.tex`

A template for creating new lecture files.

### `create_skeletons.py`

Python script to generate basic LaTeX files from markdown.

## 🔧 Compilation Options

### Method 1: Command Line (Recommended)

bash
cd Lectures/latex
pdflatex main.tex
pdflatex main.tex


### Method 2: PowerShell Script

powershell
cd Lectures/latex
.\compile.ps1


### Method 3: LaTeX Editor

Open `main.tex` in:

- TeXstudio
- Overleaf
- TeXworks
- VS Code with LaTeX Workshop extension

## 📦 Output Files

After compilation:

- **main.pdf** - Your complete lecture notes
- main.aux, main.log, main.toc - Temporary files (ignored by git)

## 🎨 Customization

### Colors

Edit `main.tex` around line 35:

latex
\definecolor{primaryblue}{RGB}{37,99,235}
\definecolor{darkblue}{RGB}{30,64,175}


### Page Layout

Edit `main.tex` around line 25:

latex
\geometry{
    left=3cm,
    right=2.5cm,
    top=2.5cm,
    bottom=2.5cm
}


### Chapter/Section Formatting

Edit `main.tex` around line 100-120.

## 📚 LaTeX Tips

### Including Images

latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{../img/your-image.jpg}
    \caption{Your caption}
    \label{fig:your-label}
\end{figure}


### Code Blocks

latex
\begin{lstlisting}[language=C, caption={Example}]
// Your code here
int main() {
    return 0;
}
\end{lstlisting}


### Lists

latex
\begin{itemize}
    \item First item
    \item Second item
\end{itemize}

\begin{enumerate}
    \item Numbered item
    \item Another item
\end{enumerate}


### Tables

latex
\begin{table}[H]
\centering
\begin{tabular}{|l|c|r|}
\hline
\textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
\hline
Data 1 & Data 2 & Data 3 \\
\hline
\end{tabular}
\caption{Your table caption}
\end{table}


### Cross-References

latex
See Figure~\ref{fig:your-label} on page~\pageref{fig:your-label}.
See Section~\ref{sec:your-section}.


## 🔄 Workflow

1. **Create skeletons**: `python create_skeletons.py`
2. **Edit lecture files**: Convert markdown to LaTeX
3. **Compile**: `pdflatex main.tex` (twice)
4. **Check output**: Open `main.pdf`
5. **Iterate**: Edit and recompile as needed
6. **Deploy**: Copy `main.pdf` to `../../materials/CO224-Complete-Notes.pdf`

## 📖 Resources

- [LaTeX Documentation](https://www.latex-project.org/help/documentation/)
- [Overleaf Learn LaTeX](https://www.overleaf.com/learn)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [CTAN Package Documentation](https://ctan.org/)

## ⚠️ Common Issues

### Missing packages

Run: `tlmgr install <package-name>` or let MiKTeX auto-install

### Images not found

Check paths: Use `../img/` relative to latex/ folder

### Compilation errors

- Check for special characters (%, $, &, #, \_)
- Escape them with backslash: `\%, \$, \&, \#, \_`

### TOC not updating

Run pdflatex twice

## 💡 Pro Tips

1. **Compile often** - Don't wait until the end
2. **One section at a time** - Comment out other \include statements
3. **Use labels** - For cross-references
4. **Backup** - Git commit regularly
5. **Preview** - Check PDF after each lecture

---

**Need help?** Check the LaTeX template and existing examples!
