
from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import shutil
import uuid

router = APIRouter()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/upload-resume", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/upload-resume")
async def handle_upload(request: Request, file: UploadFile = File(...), user_id: str = Form(...)):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["pdf", "docx"]:
        return templates.TemplateResponse("upload.html", {
            "request": request,
            "error": "Unsupported file type. Only PDF and DOCX are allowed."
        })

    filename = f"{uuid.uuid4().hex}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    
    # OPTIONAL: extract summary for GPT context
    from services.resume_service import extract_text_from_resume, summarize_resume_text

    try:
        text = extract_text_from_resume(filepath)
        summary = summarize_resume_text(text)
        request.session['resume_summary'] = summary  # assumes session middleware is active
    except Exception as e:
        print("Resume parsing failed:", e)
        request.session['resume_summary'] = ""

    return RedirectResponse(url="/resume", status_code=302)
    
