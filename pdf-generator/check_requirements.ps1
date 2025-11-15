# Quick Installation Checker for PDF Generation

Write-Host "=" -NoNewline; Write-Host ("=" * 59)
Write-Host "CO224 PDF Generator - Installation Checker"
Write-Host "=" -NoNewline; Write-Host ("=" * 59)
Write-Host ""

$allInstalled = $true

# Check Python
Write-Host "Checking Python..." -NoNewline
try {
    $pythonVersion = python --version 2>&1
    Write-Host " ✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host " ✗ Not found" -ForegroundColor Red
    Write-Host "  Install from: https://www.python.org/downloads/" -ForegroundColor Yellow
    $allInstalled = $false
}

# Check Pandoc
Write-Host "Checking Pandoc..." -NoNewline
try {
    $pandocVersion = pandoc --version 2>&1 | Select-Object -First 1
    Write-Host " ✓ Found: $pandocVersion" -ForegroundColor Green
} catch {
    Write-Host " ✗ Not found" -ForegroundColor Red
    Write-Host "  Install: choco install pandoc" -ForegroundColor Yellow
    Write-Host "  Or from: https://pandoc.org/installing.html" -ForegroundColor Yellow
    $allInstalled = $false
}

# Check pdflatex (LaTeX)
Write-Host "Checking pdflatex (LaTeX)..." -NoNewline
try {
    $latexVersion = pdflatex --version 2>&1 | Select-Object -First 1
    Write-Host " ✓ Found: $latexVersion" -ForegroundColor Green
} catch {
    Write-Host " ✗ Not found" -ForegroundColor Red
    Write-Host "  Install MiKTeX: choco install miktex" -ForegroundColor Yellow
    Write-Host "  Or from: https://miktex.org/download" -ForegroundColor Yellow
    $allInstalled = $false
}

Write-Host ""
Write-Host "=" -NoNewline; Write-Host ("=" * 59)

if ($allInstalled) {
    Write-Host "✓ All requirements installed! You can run: python generate_pdf.py" -ForegroundColor Green
} else {
    Write-Host "⚠ Some requirements missing. Please install them first." -ForegroundColor Yellow
}

Write-Host "=" -NoNewline; Write-Host ("=" * 59)
Write-Host ""
