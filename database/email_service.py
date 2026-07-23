import os
import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_otp(receiver, otp):
  try:
    msg = EmailMessage()
    msg["Subject"] = "Password Reset OTP"
    msg["From"] = EMAIL
    msg["To"] = receiver
    msg.set_content(
    f"""Your OTP is:
    {otp}
    This OTP is valid for 5 minutes.
    If you didn't request this, ignore this email.
    """
    )
    with smtplib.SMTP_SSL(
      "smtp.gmail.com",
      465
    ) as smtp:
      smtp.login(EMAIL,PASSWORD)
      smtp.send_message(msg)
    return True
  except Exception as e:
    print(e)
    return False
