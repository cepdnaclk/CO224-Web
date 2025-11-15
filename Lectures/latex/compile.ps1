# LaTeX Compilation Script for CO224 Lecture Notes

Write-Host "`n" -NoNewline
Write-Host "=" -NoNewline; Write-Host ("=" * 59)
Write-Host "CO224 LaTeX Compilation"
Write-Host "=" -NoNewline; Write-Host ("=" * 59)
Write-Host ""

# Check if main.tex exists
if (-not (Test-Path "main.tex")) {
    Write-Host "✗ Error: main.tex not found!" -ForegroundColor Red
    Write-Host "  Make sure you're in the latex/ folder" -ForegroundColor Yellow
    exit 1
}

# Clean old output
Write-Host "Cleaning old files..." -ForegroundColor Cyan
Remove-Item -Path "main.pdf" -ErrorAction SilentlyContinue
Remove-Item -Path "*.aux" -ErrorAction SilentlyContinue
Remove-Item -Path "*.log" -ErrorAction SilentlyContinue
Remove-Item -Path "*.out" -ErrorAction SilentlyContinue
Remove-Item -Path "*.toc" -ErrorAction SilentlyContinue

# First compilation
Write-Host "`nFirst compilation pass..." -ForegroundColor Cyan
pdflatex -interaction=nonstopmode main.tex | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Compilation failed! Check main.log for errors" -ForegroundColor Red
    exit 1
}

# Second compilation (for TOC)
Write-Host "Second compilation pass (for TOC)..." -ForegroundColor Cyan
pdflatex -interaction=nonstopmode main.tex | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Compilation failed! Check main.log for errors" -ForegroundColor Red
    exit 1
}

# Check if PDF was created
if (Test-Path "main.pdf") {
    $pdfSize = (Get-Item "main.pdf").Length / 1MB
    Write-Host "`n" -NoNewline
    Write-Host "=" -NoNewline; Write-Host ("=" * 59)
    Write-Host "✓ SUCCESS!" -ForegroundColor Green
    Write-Host "=" -NoNewline; Write-Host ("=" * 59)
    Write-Host "`nGenerated: main.pdf ($([math]::Round($pdfSize, 2)) MB)" -ForegroundColor Green
    Write-Host "`nNext steps:" -ForegroundColor Cyan
    Write-Host "  1. Open main.pdf to check the output"
    Write-Host "  2. Copy to materials: Copy-Item main.pdf ../../materials/CO224-Complete-Notes.pdf"
    Write-Host "  3. Commit and push to deploy`n"
} else {
    Write-Host "`n✗ PDF was not created! Check main.log for errors" -ForegroundColor Red
    exit 1
}

# Clean temp files (optional)
$cleanup = Read-Host "`nClean temporary files? (y/n)"
if ($cleanup -eq 'y') {
    Remove-Item -Path "*.aux" -ErrorAction SilentlyContinue
    Remove-Item -Path "*.log" -ErrorAction SilentlyContinue
    Remove-Item -Path "*.out" -ErrorAction SilentlyContinue
    Remove-Item -Path "*.toc" -ErrorAction SilentlyContinue
    Write-Host "✓ Cleaned temporary files" -ForegroundColor Green
}
