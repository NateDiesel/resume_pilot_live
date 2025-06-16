
import os
import stripe

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_123")

YOUR_DOMAIN = "http://localhost:8000"

def create_checkout_session(user_id: str, tier: str) -> str:
    price_lookup = {
        "premium": "price_123_premium",
        "elite": "price_456_elite"
    }

    if tier not in price_lookup:
        raise ValueError("Invalid tier")

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": price_lookup[tier],
            "quantity": 1,
        }],
        mode="payment",
        success_url=f"{YOUR_DOMAIN}/success?user_id={user_id}&tier={tier}",
        cancel_url=f"{YOUR_DOMAIN}/cancel"
    )
    return session.url
