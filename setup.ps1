# Resume Tailor AI - Windows Setup Script
# Run this script in PowerShell to set up the project

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Resume Tailor AI - Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# STEP 1: Check Python version
Write-Host "STEP 1: Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
    
    # Check if version is 3.11+
    $version = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
    if ([float]$version -lt 3.11) {
        Write-Host "⚠ Warning: Python 3.11+ is recommended. Current version: $version" -ForegroundColor Yellow
    }
} catch {
    Write-Host "✗ Python not found. Please install Python 3.11+." -ForegroundColor Red
    exit 1
}

Write-Host ""

# STEP 2: Create virtual environment
Write-Host "STEP 2: Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

Write-Host ""

# STEP 3: Activate virtual environment
Write-Host "STEP 3: Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

Write-Host ""

# STEP 4: Upgrade pip
Write-Host "STEP 4: Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet
Write-Host "✓ Pip upgraded" -ForegroundColor Green

Write-Host ""

# STEP 5: Install dependencies
Write-Host "STEP 5: Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet
Write-Host "✓ Dependencies installed" -ForegroundColor Green

Write-Host ""

# STEP 6: Check for .env file
Write-Host "STEP 6: Checking environment configuration..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "✓ .env file exists" -ForegroundColor Green
} else {
    Write-Host "⚠ Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "✓ .env file created" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠ IMPORTANT: Edit .env file and add your GROQ_API_KEY!" -ForegroundColor Red
    Write-Host "   Get your API key from: https://console.groq.com/keys" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Edit .env and add your GROQ_API_KEY" -ForegroundColor White
Write-Host "2. Run: uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "3. Visit: http://localhost:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "To test the API, run: python example_usage.py" -ForegroundColor Cyan
Write-Host ""

