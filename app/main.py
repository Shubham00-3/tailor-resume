"""
FastAPI main application
Production-grade Resume Tailor AI backend
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from app.schemas import (
    HealthResponse,
    TailorRequest,
    TailorResponse,
    ErrorResponse
)
from app.graph.pipeline import run_resume_tailor_pipeline
from app.utils.logger import logger


# Load environment variables from .env file
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events
    """
    # Startup
    logger.info("Starting Resume Tailor AI application")
    
    # Validate environment variables
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        logger.warning("GROQ_API_KEY not found in environment variables")
    else:
        logger.info("GROQ_API_KEY configured successfully")
    
    model_name = os.getenv("MODEL_NAME", "llama-3.1-70b-versatile")
    logger.info(f"Using model: {model_name}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Resume Tailor AI application")


# Initialize FastAPI app
app = FastAPI(
    title="Resume Tailor AI",
    description="Production-grade AI backend for tailoring resumes to job descriptions using LangGraph and Groq API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)


# Configure CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Check if the API is running and healthy",
    tags=["Health"]
)
async def health_check():
    """
    Health check endpoint
    
    Returns:
        HealthResponse: Status of the API
    """
    logger.info("Health check requested")
    return HealthResponse(status="ok")


@app.post(
    "/tailor",
    response_model=TailorResponse,
    summary="Tailor Resume",
    description="Tailor a resume to match a job description using AI",
    responses={
        200: {
            "description": "Successfully tailored resume",
            "model": TailorResponse
        },
        400: {
            "description": "Bad request - invalid input",
            "model": ErrorResponse
        },
        500: {
            "description": "Internal server error",
            "model": ErrorResponse
        }
    },
    tags=["Resume Tailoring"]
)
async def tailor_resume(request: TailorRequest):
    """
    Tailor a resume to a job description
    
    This endpoint:
    1. Extracts keywords and skills from the job description
    2. Matches skills between the resume and job description
    3. Rewrites the resume to better align with the job
    4. Generates a professional summary
    
    Args:
        request: TailorRequest containing resume_text and job_description
    
    Returns:
        TailorResponse: Tailored resume with analysis
    
    Raises:
        HTTPException: If processing fails
    """
    logger.info("Resume tailoring request received")
    
    try:
        # Validate Groq API key
        if not os.getenv("GROQ_API_KEY"):
            logger.error("GROQ_API_KEY not configured")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="API configuration error: GROQ_API_KEY not set"
            )
        
        # Run the LangGraph pipeline
        result = run_resume_tailor_pipeline(
            resume_text=request.resume_text,
            job_description=request.job_description
        )
        
        # Validate result has required fields
        if not result.get("tailored_resume"):
            logger.error("Pipeline returned empty tailored_resume")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to generate tailored resume"
            )
        
        logger.info("Resume tailoring completed successfully")
        
        return TailorResponse(
            tailored_resume=result["tailored_resume"],
            summary=result.get("summary", ""),
            matched_skills=result.get("matched_skills", []),
            missing_skills=result.get("missing_skills", [])
        )
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    except Exception as e:
        logger.error(f"Unexpected error in tailor_resume: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing your request: {str(e)}"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler for unhandled exceptions
    """
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal server error", "detail": str(exc)}
    )


# For local development
if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    
    logger.info(f"Starting server on port {port}")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )

