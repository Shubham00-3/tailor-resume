"""
LangGraph nodes for resume tailoring pipeline
Each node performs a specific task in the workflow
"""

import json
import os
from typing import Dict, Any, List
from groq import Groq
from app.utils.logger import logger


# Initialize Groq client
def get_groq_client() -> Groq:
    """Get Groq client with API key from environment"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    return Groq(api_key=api_key)


def get_model_name() -> str:
    """Get model name from environment or use default"""
    return os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")


def call_groq_api(prompt: str, temperature: float = 0.3, max_tokens: int = 2000) -> str:
    """
    Call Groq API with retry logic
    
    Args:
        prompt: The prompt to send to the model
        temperature: Temperature for response generation
        max_tokens: Maximum tokens in response
    
    Returns:
        Generated text response
    """
    client = get_groq_client()
    model_name = get_model_name()
    
    try:
        logger.info(f"Calling Groq API with model: {model_name}")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert resume writer and career consultant. Provide accurate, professional, and actionable insights."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        response = chat_completion.choices[0].message.content
        logger.info("Groq API call successful")
        return response
        
    except Exception as e:
        logger.error(f"Groq API call failed: {str(e)}")
        raise


def extract_keywords_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Node A: Extract keywords and skills from job description
    
    Args:
        state: Current graph state containing job_description
    
    Returns:
        Updated state with extracted keywords and required skills
    """
    logger.info("Node A: Extracting keywords from job description")
    
    job_description = state.get("job_description", "")
    
    prompt = f"""
Analyze the following job description and extract:
1. Key technical skills (e.g., programming languages, frameworks, tools)
2. Soft skills (e.g., communication, leadership, teamwork)
3. Required qualifications and certifications
4. Important keywords that should appear in a tailored resume

Job Description:
{job_description}

Provide your response in the following JSON format:
{{
    "technical_skills": ["skill1", "skill2", ...],
    "soft_skills": ["skill1", "skill2", ...],
    "qualifications": ["qual1", "qual2", ...],
    "keywords": ["keyword1", "keyword2", ...]
}}

Return ONLY the JSON object, no additional text.
"""
    
    try:
        response = call_groq_api(prompt, temperature=0.2, max_tokens=1000)
        
        # Parse JSON response
        # Try to extract JSON from response if wrapped in markdown
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        response = response.strip()
        
        extracted_data = json.loads(response)
        
        state["jd_keywords"] = extracted_data
        state["all_required_skills"] = (
            extracted_data.get("technical_skills", []) +
            extracted_data.get("soft_skills", []) +
            extracted_data.get("qualifications", [])
        )
        
        logger.info(f"Extracted {len(state['all_required_skills'])} skills from job description")
        
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON response: {e}")
        # Fallback: basic extraction
        state["jd_keywords"] = {
            "technical_skills": [],
            "soft_skills": [],
            "qualifications": [],
            "keywords": []
        }
        state["all_required_skills"] = []
    except Exception as e:
        logger.error(f"Error in extract_keywords_node: {e}")
        raise
    
    return state


def match_skills_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Node B: Match resume skills against job requirements
    
    Args:
        state: Current graph state with resume_text and all_required_skills
    
    Returns:
        Updated state with matched and missing skills
    """
    logger.info("Node B: Matching skills between resume and job description")
    
    resume_text = state.get("resume_text", "")
    all_required_skills = state.get("all_required_skills", [])
    
    prompt = f"""
You are analyzing a resume against required skills for a job.

Resume:
{resume_text}

Required Skills from Job Description:
{", ".join(all_required_skills)}

Task:
1. Identify which required skills are present in the resume (matched_skills)
2. Identify which required skills are missing from the resume (missing_skills)
3. Be thorough - check for synonyms and related terms (e.g., "Python" and "Python programming" are the same)

Provide your response in the following JSON format:
{{
    "matched_skills": ["skill1", "skill2", ...],
    "missing_skills": ["skill1", "skill2", ...]
}}

Return ONLY the JSON object, no additional text.
"""
    
    try:
        response = call_groq_api(prompt, temperature=0.2, max_tokens=1000)
        
        # Parse JSON response
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        response = response.strip()
        
        skill_analysis = json.loads(response)
        
        state["matched_skills"] = skill_analysis.get("matched_skills", [])
        state["missing_skills"] = skill_analysis.get("missing_skills", [])
        
        logger.info(f"Found {len(state['matched_skills'])} matched skills and {len(state['missing_skills'])} missing skills")
        
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON response: {e}")
        state["matched_skills"] = []
        state["missing_skills"] = all_required_skills
    except Exception as e:
        logger.error(f"Error in match_skills_node: {e}")
        raise
    
    return state


def rewrite_resume_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Node C: Rewrite resume and generate professional summary
    
    Args:
        state: Current graph state with all previous analysis
    
    Returns:
        Updated state with tailored_resume and summary
    """
    logger.info("Node C: Rewriting resume and generating summary")
    
    resume_text = state.get("resume_text", "")
    job_description = state.get("job_description", "")
    matched_skills = state.get("matched_skills", [])
    missing_skills = state.get("missing_skills", [])
    jd_keywords = state.get("jd_keywords", {})
    
    prompt = f"""
You are an expert resume writer. Your task is to tailor the given resume to match the job description.

Original Resume:
{resume_text}

Job Description:
{job_description}

Matched Skills (emphasize these): {", ".join(matched_skills)}
Missing Skills (if the candidate has transferable skills, mention them): {", ".join(missing_skills[:5])}
Key Keywords to incorporate: {", ".join(jd_keywords.get('keywords', [])[:10])}

Instructions:
1. Rewrite the resume to better align with the job description
2. Emphasize matched skills and relevant experience
3. Incorporate keywords naturally throughout the resume
4. Maintain the original structure but optimize the content
5. Keep the tone professional and achievement-focused
6. Create a compelling professional summary (3-4 sentences) highlighting the candidate's fit for this role

Provide your response in the following JSON format:
{{
    "tailored_resume": "The complete rewritten resume text...",
    "professional_summary": "A 3-4 sentence summary highlighting key qualifications..."
}}

Return ONLY the JSON object, no additional text.
"""
    
    try:
        response = call_groq_api(prompt, temperature=0.4, max_tokens=3000)
        
        # Parse JSON response
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        response = response.strip()
        
        result = json.loads(response)
        
        state["tailored_resume"] = result.get("tailored_resume", resume_text)
        state["summary"] = result.get("professional_summary", "")
        
        logger.info("Resume rewriting completed successfully")
        
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON response: {e}")
        state["tailored_resume"] = resume_text
        state["summary"] = "Unable to generate summary. Please try again."
    except Exception as e:
        logger.error(f"Error in rewrite_resume_node: {e}")
        raise
    
    return state

