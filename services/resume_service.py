
import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("templates"))

def format_lines(text):
    return [line.strip() for line in text.strip().split("\n") if line.strip()]

def generate_resume_pdf(name, email, phone, skills, experience, education, output_path, tier):
    template = env.get_template("resume_template.html")
    html_content = template.render(
        name=name,
        email=email,
        phone=phone,
        skills=format_lines(skills),
        experience=format_lines(experience),
        education=format_lines(education),
        tier=tier
    )
    HTML(string=html_content).write_pdf(output_path)
