import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import sys

def send_email(subject):
    message = Mail(
        from_email=os.environ.get('SENDGRID_EMAIL'),
        to_emails='cs396group@gmail.com',
        subject=subject,
        plain_text_content='Check the GitHub Actions for more details.'
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)
        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_email.py <subject>")
    else:
        send_email(sys.argv[1])
