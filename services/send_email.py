
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64

def send_email_with_attachment(to_email, subject, content, file_path):
    message = Mail(
        from_email='noreply@resume-gen.ai',
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    with open(file_path, 'rb') as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    attached_file = Attachment(
        FileContent(encoded),
        FileName(os.path.basename(file_path)),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    message.attachment = attached_file

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(f"SendGrid error: {e}")
        return None
