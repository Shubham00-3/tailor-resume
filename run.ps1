# Quick run script for Resume Tailor AI
# Run this after setup.ps1

Write-Host "Starting Resume Tailor AI..." -ForegroundColor Cyan

# Check if virtual environment exists
if (-not (Test-Path "venv\Scripts\Activate.ps1")) {
    Write-Host "Error: Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run setup.ps1 first to create the virtual environment" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Run this command:" -ForegroundColor Cyan
    Write-Host "  .\setup.ps1" -ForegroundColor White
    exit 1
}

# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Check if .env exists
if (-not (Test-Path ".env")) {
    Write-Host "Error: .env file not found!" -ForegroundColor Red
    Write-Host "Please run setup.ps1 first and configure your GROQ_API_KEY" -ForegroundColor Yellow
    exit 1
}

# Check if GROQ_API_KEY is set
$envContent = Get-Content .env -Raw
if ($envContent -match "GROQ_API_KEY=your_groq_api_key_here" -or $envContent -notmatch "GROQ_API_KEY=\S+") {
    Write-Host "Error: GROQ_API_KEY not configured in .env file!" -ForegroundColor Red
    Write-Host "Please edit .env and add your API key from https://console.groq.com/keys" -ForegroundColor Yellow
    exit 1
}

Write-Host "Starting FastAPI server..." -ForegroundColor Green
Write-Host "API will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Interactive docs at: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

