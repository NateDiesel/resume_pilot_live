
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.responses import JSONResponse
import stripe
import os

router = APIRouter()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Stripe Webhook Endpoint
@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session.get("customer_email")
        print(f"✅ Subscription successful for {customer_email}")
        # Here you can unlock premium/elite access in DB or session
    return JSONResponse(status_code=status.HTTP_200_OK, content={"success": True})
