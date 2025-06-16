import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_resume_coach(history, tier="free"):
    try:
        messages = [{"role": "system", "content": _get_system_prompt(tier)}] + history

        model = "gpt-4" if tier == "elite" else "gpt-3.5-turbo"
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("GPT ERROR:", e)
        return f"GPT ERROR: {str(e)}"

def _get_system_prompt(tier):
    if tier == "elite":
        return (
            "You are a world-class career coach and resume strategist. "
            "Help users uncover ideal roles, extract resume content, and prep for interviews. "
            "Guide with empathy, clarity, and strategy."
        )
    elif tier == "premium":
        return (
            "You are a skilled resume coach. Help users shape effective resumes, suggest relevant roles, "
            "and provide brief job market advice. Ask smart follow-up questions to clarify work history and goals."
        )
    else:  # free tier
        return (
            "You are a helpful AI assistant focused on extracting resume information. "
            "Ask short follow-up questions to gather job titles, achievements, and skills. "
            "Be concise and professional."
        )
