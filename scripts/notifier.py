"""
Project : Price Scraper
Author : Tao Serveaux
Goal : Handle email and Telegram notifications
"""

from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv() # Load environment variables from .env file

def sendEmail(msg) :
    """
    Send a price alert notification via Gmail SMTP.

    Arg :
        - msg (str) : Email message content to send

    Return :
        - None
    """

    emailSender = os.getenv("EMAIL_SENDER")
    emailPassword = os.getenv("EMAIL_PASSWORD")
    emailReceiver = os.getenv("EMAIL_RECEIVER")

    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()
    session.login(emailSender, emailPassword)
    session.sendmail(emailSender, emailReceiver, msg)
    session.quit()

def sendTelegram(msg):
    """
    Send a price alert notification via Telegram bot.

    Arg :
        - msg (str) : Message content to send to the Telegram chat

    Return :
        - None
    """

    chatId = os.getenv("CHAT_ID")
    token = os.getenv("TOKEN")
    payload = {"chat_id" : chatId, "text" : msg}

    URL = f"https://api.telegram.org/bot{token}/sendMessage"

    response = requests.post(URL, data=payload)
    response.raise_for_status()

def sendAll(msgEmail,msgTelegram) :
    """
    Send a price alert notification via both email and Telegram.

    Args :
        - msgEmail (str) : Message content to send by email
        - msgTelegram (str) : Message content to send by Telegram

    Return :
        - None
    """

    sendTelegram(msgTelegram)
    sendEmail(msgEmail)

sendAll("Hello","Hello")