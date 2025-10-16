"""
Example usage of the Resume Tailor API
Run this after starting the server with: uvicorn app.main:app --reload
"""

import requests
import json

# API endpoint
BASE_URL = "http://localhost:8000"

# Example resume
resume_text = """
John Doe
Senior Software Engineer

PROFESSIONAL SUMMARY
Experienced software engineer with 5+ years in full-stack development.

TECHNICAL SKILLS
- Programming: Python, JavaScript, Java
- Frameworks: Django, Flask, React
- Databases: PostgreSQL, MongoDB, Redis
- Tools: Git, Docker, Jenkins

EXPERIENCE

Senior Software Engineer | Tech Corp | 2020 - Present
- Developed RESTful APIs serving 1M+ daily requests
- Led team of 4 developers in agile environment
- Implemented CI/CD pipelines reducing deployment time by 40%
- Built microservices architecture using Docker and Kubernetes

Software Engineer | StartupXYZ | 2018 - 2020
- Created full-stack web applications using Python and React
- Optimized database queries improving performance by 60%
- Collaborated with cross-functional teams on product development

EDUCATION
Bachelor of Science in Computer Science
University of Technology | 2018
"""

# Example job description
job_description = """
Senior Backend Engineer - Python

We are seeking a talented Senior Backend Engineer to join our growing team.

REQUIREMENTS:
- 5+ years of Python development experience
- Expert knowledge of FastAPI or Django frameworks
- Strong experience with PostgreSQL and Redis
- Proficiency in Docker and containerization
- Experience with AWS or Google Cloud Platform
- Knowledge of microservices architecture
- Excellent problem-solving and communication skills

RESPONSIBILITIES:
- Design and implement scalable RESTful APIs
- Optimize application performance and database queries
- Collaborate with frontend developers and DevOps team
- Mentor junior developers
- Participate in code reviews and architecture discussions

NICE TO HAVE:
- Experience with Kubernetes
- Knowledge of GraphQL
- Contributions to open-source projects
"""


def test_health():
    """Test health endpoint"""
    print("\\n=== Testing Health Endpoint ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200


def test_tailor_resume():
    """Test resume tailoring endpoint"""
    print("\\n=== Testing Resume Tailor Endpoint ===")
    
    payload = {
        "resume_text": resume_text,
        "job_description": job_description
    }
    
    print("Sending request to /tailor endpoint...")
    print("(This may take 10-30 seconds depending on API response time)\\n")
    
    try:
        response = requests.post(
            f"{BASE_URL}/tailor",
            json=payload,
            timeout=60
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            print("\\n" + "="*80)
            print("TAILORED RESUME:")
            print("="*80)
            print(data["tailored_resume"])
            
            print("\\n" + "="*80)
            print("PROFESSIONAL SUMMARY:")
            print("="*80)
            print(data["summary"])
            
            print("\\n" + "="*80)
            print("MATCHED SKILLS:")
            print("="*80)
            for skill in data["matched_skills"]:
                print(f"  ✓ {skill}")
            
            print("\\n" + "="*80)
            print("MISSING SKILLS:")
            print("="*80)
            for skill in data["missing_skills"]:
                print(f"  ✗ {skill}")
            
            print("\\n" + "="*80)
            
            return True
        else:
            print(f"Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")
        print("Make sure the server is running: uvicorn app.main:app --reload")
        return False
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def main():
    """Run all examples"""
    print("="*80)
    print("Resume Tailor API - Example Usage")
    print("="*80)
    
    # Test health endpoint
    if not test_health():
        print("\\nHealth check failed. Make sure the server is running.")
        return
    
    # Test resume tailoring
    test_tailor_resume()


if __name__ == "__main__":
    main()

