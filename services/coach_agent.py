
def get_ai_response(history):
    last_question = history[-1]['content'].lower()

    # Mock logic for demonstration
    if "job" in last_question:
        return "What job are you applying for, and what excites you about it?"
    elif "skills" in last_question:
        return "List 3–5 core skills you want to highlight."
    elif "experience" in last_question:
        return "Tell me about one job or project you’ve done that’s relevant."
    elif "education" in last_question:
        return "What’s your highest level of education or training?"
    else:
        return "Great — tell me more about your background or goals!"

def resume_autopilot_chat(history, message):
    system_prompts = {
        "role": "system",
        "content": "You are a friendly and professional AI resume coach helping users create powerful resumes step-by-step. Ask for the job target, then guide them through skills, experience, and education. Keep messages short and helpful."
    }

    history = history or []
    history.append({"role": "user", "content": message})
    messages = [system_prompts] + history

    return messages
