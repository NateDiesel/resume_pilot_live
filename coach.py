import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_resume_coach(history, tier="free"):
    try:
        messages = [{"role": "system", "content": _get_system_prompt(tier)}] + history
        response = client.chat.completions.create(
            model="gpt-4" if tier == "elite" else "gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print("GPT ERROR:", e)
        return f"GPT ERROR: {str(e)}"

def _get_system_prompt(tier):
    if tier == "elite":
        return (
            "You are a world-class career coach and resume expert. "
            "Guide users toward ideal roles and strategic pivots."
        )
    elif tier == "premium":
        return (
            "You're a top-tier resume writer and job-matching assistant. "
            "Generate tailored, compelling resumes that win interviews."
        )
    return (
        "You are an expert resume builder. "
        "Help create strong, clean resumes based on user input."
    )
