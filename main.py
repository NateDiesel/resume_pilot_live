
from fastapi import FastAPI
from fastapi import Request, Form
from routers import tailor
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from routers import coach, resume, upload
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
app.include_router(tailor.router)
app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(coach.router)
app.include_router(resume.router)
app.include_router(upload.router)

@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse(url="/start")

@app.get("/start")
async def get_start():
    return templates.TemplateResponse("email_gate.html", {"request": {}})

@app.post("/start")
async def start_session(request: Request, email: str = Form(...)):
    user_id = email.strip().lower()
    request.session["user_id"] = user_id
    from services.user_db import set_user_tier
    set_user_tier(user_id, "free")  # Default to free tier
    return RedirectResponse(url=f"/coach?user_id={user_id}", status_code=302)
