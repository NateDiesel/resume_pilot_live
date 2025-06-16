
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.coach_agent import get_ai_response

router = APIRouter()
templates = Jinja2Templates(directory="templates")

session_history = {}

@router.get("/coach", response_class=HTMLResponse)
async def get_coach(request: Request, user_id: str = "demo"):
    history = session_history.get(user_id, [])
    return templates.TemplateResponse("coach_chat.html", {"request": request, "history": history, "user_id": user_id})

@router.post("/coach", response_class=HTMLResponse)
async def chat_with_coach(request: Request, user_id: str = Form(...), message: str = Form(...)):
    history = session_history.get(user_id, [])
    
    import re
    import requests
    from bs4 import BeautifulSoup

    # Detect job link
    if "linkedin.com/jobs" in message or "indeed.com/viewjob" in message:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            job_page = requests.get(message.strip(), headers=headers, timeout=10)
            soup = BeautifulSoup(job_page.text, "html.parser")
            if "linkedin.com" in message:
                desc = soup.find("div", {"class": "description__text"}).get_text(strip=True)
            elif "indeed.com" in message:
                desc = soup.find("div", {"id": "jobDescriptionText"}).get_text(strip=True)
            message = f"Job Description Extracted:\n{desc[:1500]}"
        except Exception as e:
            message = f"Could not fetch job description: {str(e)}"

    history.append({"role": "user", "content": message})
    response = get_ai_response(history)
    history.append({"role": "assistant", "content": response})
    session_history[user_id] = history
    return templates.TemplateResponse("coach_chat.html", {"request": request, "history": history, "user_id": user_id})

@router.get("/coach")
async def start_coach(request: Request):
    history = request.session.get("chat_history", [])
    if not history:
        history = [{"role": "coach", "content": "Hi there! I’m your AI Resume Coach. Let’s get you hired. What kind of role are you applying for?"}]
        request.session["chat_history"] = history
    return templates.TemplateResponse("coach.html", {"request": request, "history": history})
