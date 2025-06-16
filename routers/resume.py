
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from services.resume_service import generate_resume_pdf
from services.user_db import get_user_tier
import os
import uuid

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def resume_form(request: Request):
    
    summary = request.session.get("resume_summary", "")
    return templates.TemplateResponse("resume_template.html", {
        "request": request,
        "resume_summary": summary
    })
    

@router.post("/generate", response_class=FileResponse)
async def generate_resume(
    request: Request,
    user_id: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    skills: str = Form(...),
    experience: str = Form(...),
    education: str = Form(...)
):
    user_tier = get_user_tier(user_id)
    filename = f"{uuid.uuid4().hex}_{name.replace(' ', '_')}.pdf"
    path = os.path.join("static", filename)

    generate_resume_pdf(
        name=name,
        email=email,
        phone=phone,
        skills=skills,
        experience=experience,
        education=education,
        output_path=path,
        tier=user_tier
    )

    
    from services.send_email import send_email_with_attachment
    send_email_with_attachment(
        to_email=email,
        subject="Your Generated Resume",
        content="Attached is your resume from Resume SaaS.",
        file_path=path
    )
    return FileResponse(path, media_type="application/pdf", filename=filename)
    
