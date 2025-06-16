
from fastapi import APIRouter, Form
from services.tailor_service import tailor_resume_to_job

router = APIRouter()

@router.post("/tailor_resume")
async def tailor_resume(resume_text: str = Form(...), job_description: str = Form(...)):
    tailored = tailor_resume_to_job(resume_text, job_description)
    return {"tailored_resume": tailored}
