"""
Basic tests for the Resume Tailor API
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_check_response_model():
    """Test health check returns correct structure"""
    response = client.get("/health")
    data = response.json()
    assert "status" in data
    assert isinstance(data["status"], str)


def test_tailor_endpoint_requires_resume_text():
    """Test that tailor endpoint validates resume_text"""
    response = client.post("/tailor", json={
        "job_description": "Python developer needed"
    })
    assert response.status_code == 422  # Validation error


def test_tailor_endpoint_requires_job_description():
    """Test that tailor endpoint validates job_description"""
    response = client.post("/tailor", json={
        "resume_text": "John Doe, Software Engineer"
    })
    assert response.status_code == 422  # Validation error


def test_tailor_endpoint_minimum_length_validation():
    """Test minimum length validation for inputs"""
    response = client.post("/tailor", json={
        "resume_text": "Too short",
        "job_description": "Also too short"
    })
    assert response.status_code == 422  # Validation error


# Note: Full integration tests require a valid GROQ_API_KEY
# Uncomment and add your API key to run integration tests

# @pytest.mark.integration
# def test_tailor_endpoint_full_flow():
#     """Test complete resume tailoring flow"""
#     response = client.post("/tailor", json={
#         "resume_text": "John Doe\\nSoftware Engineer\\n\\nExperience:\\n- 5 years in Python development\\n- Built REST APIs with FastAPI\\n- Worked with PostgreSQL databases",
#         "job_description": "Senior Python Developer needed. Must have FastAPI, Docker, and cloud experience."
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert "tailored_resume" in data
#     assert "summary" in data
#     assert "matched_skills" in data
#     assert "missing_skills" in data

