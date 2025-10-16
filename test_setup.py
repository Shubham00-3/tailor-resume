"""
Quick setup verification script
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("Resume Tailor AI - Setup Verification")
print("=" * 60)

# Check API key
api_key = os.getenv("GROQ_API_KEY")
if api_key and api_key != "your_groq_api_key_here":
    print("[OK] GROQ_API_KEY: Configured")
    print(f"     Key preview: {api_key[:20]}...")
else:
    print("[ERROR] GROQ_API_KEY: Not configured")
    
# Check model
model = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
print(f"[OK] MODEL_NAME: {model}")

# Check port
port = os.getenv("PORT", "8000")
print(f"[OK] PORT: {port}")

# Try importing main components
print("\n" + "=" * 60)
print("Testing Imports")
print("=" * 60)

try:
    from app.graph.nodes import get_groq_client, get_model_name
    print("[OK] app.graph.nodes - Import successful")
except Exception as e:
    print(f"[ERROR] app.graph.nodes - {e}")

try:
    from app.graph.pipeline import create_resume_tailor_graph
    print("[OK] app.graph.pipeline - Import successful")
except Exception as e:
    print(f"[ERROR] app.graph.pipeline - {e}")

try:
    from app.main import app
    print("[OK] app.main (FastAPI) - Import successful")
except Exception as e:
    print(f"[ERROR] app.main - {e}")

print("\n" + "=" * 60)
print("Status")
print("=" * 60)

if api_key and api_key != "your_groq_api_key_here":
    print("[SUCCESS] All systems ready!")
    print("\nNext steps:")
    print("1. Start server: uvicorn app.main:app --reload")
    print("2. Visit: http://localhost:8000/docs")
    print("3. Test: python example_usage.py")
else:
    print("[WARNING] Please configure GROQ_API_KEY in .env file")
    print("          Get your key from: https://console.groq.com/keys")

print("=" * 60)

