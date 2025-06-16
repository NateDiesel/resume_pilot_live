
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from services.stripe_service import create_checkout_session

router = APIRouter()

@router.post("/checkout")
async def checkout(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    tier = data.get("tier", "premium")

    if not user_id:
        return JSONResponse(status_code=400, content={"error": "Missing user_id"})

    try:
        session_url = create_checkout_session(user_id=user_id, tier=tier)
        return {"checkout_url": session_url}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
