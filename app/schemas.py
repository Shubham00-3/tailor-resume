"""
Pydantic schemas for request/response validation
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., example="ok")


class TailorRequest(BaseModel):
    """Request schema for resume tailoring"""
    resume_text: str = Field(
        ...,
        description="The original resume text to be tailored",
        min_length=50,
        example="John Doe\\nSoftware Engineer\\n\\nExperience:\\n- 5 years in Python development..."
    )
    job_description: str = Field(
        ...,
        description="The job description to tailor the resume against",
        min_length=50,
        example="We are seeking a Senior Python Developer with experience in FastAPI..."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "resume_text": "John Doe\nSoftware Engineer\n\nExperience:\n- 5 years Python development\n- Built REST APIs with FastAPI\n- Worked with PostgreSQL databases",
                "job_description": "Senior Python Developer needed. Must have FastAPI, Docker, and cloud experience."
            }
        }


class TailorResponse(BaseModel):
    """Response schema for tailored resume"""
    tailored_resume: str = Field(
        ...,
        description="The tailored resume optimized for the job description"
    )
    summary: str = Field(
        ...,
        description="A professional summary highlighting key qualifications"
    )
    matched_skills: List[str] = Field(
        ...,
        description="Skills from the resume that match the job description"
    )
    missing_skills: List[str] = Field(
        ...,
        description="Skills mentioned in the job description but missing from the resume"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "tailored_resume": "John Doe\nSenior Software Engineer\n\nProfessional Summary:\nExperienced Python developer...",
                "summary": "5+ years of experience in Python development with expertise in FastAPI...",
                "matched_skills": ["Python", "FastAPI", "PostgreSQL"],
                "missing_skills": ["Docker", "AWS", "Kubernetes"]
            }
        }


class ErrorResponse(BaseModel):
    """Error response schema"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")

    class Config:
        json_schema_extra = {
            "example": {
                "error": "Processing failed",
                "detail": "Unable to connect to Groq API"
            }
        }

