import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

def send_resume_email(sender_email, sender_password, recipients, subject, body, attachment_path):
    try:
        # Create email
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.set_content(body)

        # Attach the resume PDF
        with open(attachment_path, 'rb') as file:
            file_data = file.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        print("✅ Resume sent successfully to:", recipients)

    except Exception as e:
        print("❌ Error sending resume:", str(e))

# ===== Usage Example =====
if __name__ == "__main__":
    load_dotenv()  # Load credentials from .env

    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

    recipients = [
        "sadiahameed1428@gmail.com"
    ]

    subject = "Application for QA Engineer Role – Sadia Hameed"
    body = (
        "Dear Hiring Manager,\n\n"
        "I am excited to apply for the QA Engineer position at your esteemed organization. "
        "With over 3 years of hands-on experience in both manual and automation testing, "
        "I bring strong expertise in ensuring software quality across web and API layers.\n\n"

        "My core skill set includes:\n"
        "- Web Automation: Selenium, Playwright, Cypress\n"
        "- Programming: Python, JavaScript, Java\n"
        "- API Testing: Postman, Python's requests library\n"
        "- Agile Collaboration: Jira for task tracking and bug management\n\n"

        "I have successfully led test automation initiatives and worked in agile teams to deliver high-quality software. "
        "Attached is my resume for your consideration. I would appreciate the opportunity to further discuss how I can contribute to your team.\n\n"

        "Thank you for your time and consideration.\n\n"
        "Best regards,\n"
        "Sadia Hameed\n"
        "Email: sadia.hameed@kinectro.com.au"
    )

    attachment_path = "/home/win-10/PycharmProject/sendBulkEmails.py/Sadia Hameed - Resume.pdf"  # <-- Your resume file path here

    send_resume_email(SENDER_EMAIL, SENDER_PASSWORD, recipients, subject, body, attachment_path)

