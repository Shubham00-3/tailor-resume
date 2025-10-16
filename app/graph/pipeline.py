"""
LangGraph pipeline orchestration for resume tailoring
Defines the workflow graph and execution order
"""

from typing import Dict, Any, TypedDict
from langgraph.graph import StateGraph, END
from app.graph.nodes import (
    extract_keywords_node,
    match_skills_node,
    rewrite_resume_node
)
from app.utils.logger import logger


class GraphState(TypedDict):
    """Type definition for the graph state"""
    resume_text: str
    job_description: str
    jd_keywords: Dict[str, Any]
    all_required_skills: list
    matched_skills: list
    missing_skills: list
    tailored_resume: str
    summary: str


def create_resume_tailor_graph() -> StateGraph:
    """
    Create and configure the LangGraph workflow
    
    The workflow consists of three sequential nodes:
    1. Extract keywords from job description
    2. Match skills between resume and JD
    3. Rewrite resume and generate summary
    
    Returns:
        Configured StateGraph ready for compilation
    """
    logger.info("Creating resume tailor graph")
    
    # Initialize the graph with state schema
    workflow = StateGraph(GraphState)
    
    # Add nodes to the graph
    workflow.add_node("extract_keywords", extract_keywords_node)
    workflow.add_node("match_skills", match_skills_node)
    workflow.add_node("rewrite_resume", rewrite_resume_node)
    
    # Define the workflow edges (execution order)
    workflow.set_entry_point("extract_keywords")
    workflow.add_edge("extract_keywords", "match_skills")
    workflow.add_edge("match_skills", "rewrite_resume")
    workflow.add_edge("rewrite_resume", END)
    
    logger.info("Graph created with 3 nodes: extract_keywords -> match_skills -> rewrite_resume")
    
    return workflow


def run_resume_tailor_pipeline(resume_text: str, job_description: str) -> Dict[str, Any]:
    """
    Execute the complete resume tailoring pipeline
    
    Args:
        resume_text: Original resume content
        job_description: Target job description
    
    Returns:
        Dictionary containing tailored resume and analysis results
    
    Raises:
        Exception: If any step in the pipeline fails
    """
    logger.info("Starting resume tailor pipeline execution")
    
    try:
        # Create and compile the graph
        workflow = create_resume_tailor_graph()
        app = workflow.compile()
        
        # Initialize state
        initial_state = {
            "resume_text": resume_text,
            "job_description": job_description,
            "jd_keywords": {},
            "all_required_skills": [],
            "matched_skills": [],
            "missing_skills": [],
            "tailored_resume": "",
            "summary": ""
        }
        
        logger.info("Executing graph workflow")
        
        # Run the graph
        final_state = app.invoke(initial_state)
        
        logger.info("Pipeline execution completed successfully")
        
        # Extract results
        result = {
            "tailored_resume": final_state.get("tailored_resume", ""),
            "summary": final_state.get("summary", ""),
            "matched_skills": final_state.get("matched_skills", []),
            "missing_skills": final_state.get("missing_skills", [])
        }
        
        return result
        
    except Exception as e:
        logger.error(f"Pipeline execution failed: {str(e)}")
        raise Exception(f"Resume tailoring pipeline failed: {str(e)}")

