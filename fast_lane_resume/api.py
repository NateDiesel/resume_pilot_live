from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from main import generate_resume

app = FastAPI()

class ResumeRequest(BaseModel):
    job_description: str
    email: str
    tier: str
    uploaded_resume: Optional[str] = None

@app.post("/generate")
def generate(request: ResumeRequest):
    result = generate_resume(
        job_description=request.job_description,
        email=request.email,
        tier=request.tier,
        uploaded_resume=request.uploaded_resume
    )
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
