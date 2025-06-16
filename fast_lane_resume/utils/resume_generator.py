import os
from datetime import datetime

def generate_pdf_resume(job_desc: str, uploaded_resume: str, tier: str, email: str):
    content = f"<h1>Resume for {email}</h1><p><b>Tier:</b> {tier}</p><p><b>Job Description:</b><br>{job_desc}</p>"
    if uploaded_resume:
        content += f"<p><b>Existing Resume:</b><br>{uploaded_resume}</p>"
    output_path = f"/mnt/data/outputs/resume_{email.replace('@', '_')}_{int(datetime.utcnow().timestamp())}.pdf"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(content)
    return output_path, f"Generated resume for {email}"
