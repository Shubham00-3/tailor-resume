# STEP 1: Use official Python 3.11 slim image as base
FROM python:3.11-slim

# STEP 2: Set working directory in container
WORKDIR /app

# STEP 3: Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
# Pip configuration for better Docker builds
ENV PIP_NO_CLEAN_AFTER_INSTALL=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# STEP 4: Install system dependencies (if needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# STEP 5: Copy requirements file
COPY requirements.txt .

# STEP 6: Install Python dependencies with retry and optimizations
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --timeout=1000 --retries=5 -r requirements.txt

# STEP 7: Copy application code
COPY . .

# STEP 8: Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# STEP 9: Expose port 8000
EXPOSE 8000

# STEP 10: Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# STEP 11: Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

