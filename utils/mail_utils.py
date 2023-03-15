#!/usr/bin/python3
"""This Utility Module Handles Everything Related To Mail."""
import requests

URL = f"https://api.mailgun.net/v3"

def send_verification_mail(domain: str, api_key: str, code: str, user_mail: str, system_mail: str, username: str):
    """This function send user verification mail."""
    message = f"<h3>Hi {username}, <br>Your verification code is <span style='color: #ffffff; background-color: rgba(40, 40, 40, 0.4); padding: 4px; font-size: 30px; border-radius: 4px;'>{code}</span>. <br> Your pin is <b>7777</b>.<br><b>Note</b>: Please don't share this information with anyone.</h3>"
    req = requests.post(f'{URL}/{domain}/messages', auth=('api', api_key), data={
        "from": f"MAXPAY <{system_mail}>",
        "to": user_mail,
        "subject": "User Verification",
        "html": message
        })

    return req


def send_transaction_alert(domain: str, api_key: str, user_mail: str, system_mail: str, message: str):
    """This function send transaction alert to user."""
    req = requests.post(f'{URL}/{domain}/messages', auth=('api', api_key), data={
        "from": f"MAXPAY <{system_mail}>",
        "to": user_mail,
        "subject": "Transaction Alert",
        "html": message
        })

    return req
