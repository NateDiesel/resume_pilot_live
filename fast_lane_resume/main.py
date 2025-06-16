from typing import Optional, Dict
from utils.resume_generator import generate_pdf_resume
from utils.usage_tracker import check_and_update_limit
from utils.email_validator import is_valid_email

def generate_resume(job_description: str, email: str, tier: str, uploaded_resume: Optional[str] = None) -> Dict:
    if not job_description:
        return {"error": "Job description is required."}

    if not is_valid_email(email):
        return {"error": "Invalid email address."}

    usage_info = check_and_update_limit(email, tier)
    if not usage_info["allowed"]:
        return {"error": "limit reached", "upgrade_url": "/upgrade"}

    pdf_path, resume_text = generate_pdf_resume(job_description, uploaded_resume, tier, email)

    return {
        "pdf_path": pdf_path,
        "resume_text": resume_text,
        "usage_info": {
            "tier": tier,
            "resumes_remaining": usage_info["remaining"]
        }
    }
