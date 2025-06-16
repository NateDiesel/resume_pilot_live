import json
import os

USAGE_FILE = os.path.join(os.path.dirname(__file__), "..", "usage.json")
USAGE_FILE = os.path.abspath(USAGE_FILE)

def load_usage():
    if os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_usage(data):
    with open(USAGE_FILE, "w") as f:
        json.dump(data, f)

def check_and_update_limit(email: str, tier: str):
    usage = load_usage()
    today = "2025-06-06"
    key = f"{email}_{today}"
    current = usage.get(key, 0)

    limits = {"free": 1, "premium": 10, "elite": float('inf')}
    allowed_limit = limits.get(tier, 1)

    if current >= allowed_limit:
        return {"allowed": False, "remaining": 0}

    usage[key] = current + 1
    save_usage(usage)
    return {"allowed": True, "remaining": allowed_limit - usage[key]}
