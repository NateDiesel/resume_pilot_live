
from openai import OpenAI
import os

# Initialize OpenAI (uses OPENAI_API_KEY from env)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def tailor_resume_to_job(resume_text: str, job_description: str) -> str:
    prompt = f"""
    Given the following resume:
    {resume_text}

    And this job description:
    {job_description}

    Rewrite the resume to better match the job, focusing on aligning skills, experience, and keywords.
    Return the tailored resume text.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
