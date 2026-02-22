from crewai.tools import BaseTool
from dotenv import load_dotenv
from typing import Type
from pydantic import BaseModel, Field
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

load_dotenv(override=True)
MAIL_KEY = os.getenv("MAIL_KEY")


class mail(BaseModel):
    """A message to be sent to the user"""
    message: str = Field(..., description="The message to be sent to the user.")

class email_tool(BaseTool):

    name: str = "Send a Email to user"
    description: str = (
        "This tool is used to send an email to the user with the results."
    )
    args_schema: Type[BaseModel] = mail

    def _run(self, message: str) -> str:

        sender_email   = "agasthybot@gmail.com"
        receiver_email = "agasthynathgs@gmail.com"
        Subject        = "results of stock picker"
        app_password   = MAIL_KEY

        # Create message
        cred = MIMEMultipart()
        cred["From"] = sender_email
        cred["To"] = receiver_email
        cred["Subject"] = Subject
        body = message
        cred.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, cred.as_string())
        server.quit()

        return {"status" : "success"}

