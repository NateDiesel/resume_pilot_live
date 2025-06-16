
import os
import stripe
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def check_subscription(user_email):
    # Example stub — real version would check DB or Stripe API
    return True

def send_resume_email(to_email, subject, content, pdf_data, filename="resume.pdf"):
    message = Mail(
        from_email=os.getenv("FROM_EMAIL", "noreply@example.com"),
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    encoded_file = pdf_data.encode("base64") if isinstance(pdf_data, str) else pdf_data
    attachment = Attachment()
    attachment.file_content = FileContent(encoded_file)
    attachment.file_type = FileType("application/pdf")
    attachment.file_name = FileName(filename)
    attachment.disposition = Disposition("attachment")
    message.attachment = attachment

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print("SendGrid Error:", str(e))
        return None
