
# Simulated in-memory user DB

user_tiers = {}

def set_user_tier(user_id: str, tier: str):
    user_tiers[user_id] = tier

def get_user_tier(user_id: str) -> str:
    return user_tiers.get(user_id, "free")


resume_history = {}

def add_resume_to_history(user_id: str, resume_data: str):
    if user_id not in resume_history:
        resume_history[user_id] = []
    resume_history[user_id].append(resume_data)

def get_resume_history(user_id: str):
    return resume_history.get(user_id, [])

def resume_limit_reached(user_id: str) -> bool:
    tier = get_user_tier(user_id)
    limit = {"free": 1, "premium": 10, "elite": 50}.get(tier, 1)
    return len(resume_history.get(user_id, [])) >= limit
