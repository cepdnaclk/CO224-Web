$mdDir = "D:\Academics\Projects\isuru sir\CO224-Web\Lectures\markdown\"
$latexDir = "D:\Academics\Projects\isuru sir\CO224-Web\Lectures\latex\"

# Create latex directory if it doesn't exist
New-Item -ItemType Directory -Force -Path $latexDir | Out-Null

# Get all markdown files
$lectures = Get-ChildItem $mdDir -Filter "*.md" | Sort-Object Name

foreach ($lecture in $lectures) {
    Write-Host "Processing: $($lecture.Name)"
    
    # Read markdown content
    $mdContent = Get-Content -Path $lecture.FullName -Raw -Encoding UTF8
    
    # Create LaTeX filename
    $latexName = $lecture.BaseName + ".tex"
    $latexPath = Join-Path $latexDir $latexName
    
    # Create LaTeX document with exact markdown content
    $latexContent = "\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{fancyvrb}
\usepackage{geometry}
\geometry{margin=1in}

\title{" + $lecture.BaseName + "}
\date{\today}

\begin{document}
\maketitle

\begin{Verbatim}[commandchars=\textbackslash{}\{\}]
" + $mdContent + "
\end{Verbatim}

\end{document}"
    
    # Write LaTeX file
    Set-Content -Path $latexPath -Value $latexContent -Encoding UTF8
    Write-Host "Created: $latexName"
}

Write-Host "`nAll 20 LaTeX files created in: $latexDir"
