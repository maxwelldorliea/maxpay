#!/usr/bin/python3
"""This Utility Module Handles Everything Related To Mail."""
import requests

URL = f"https://api.mailgun.net/v3"

def send_verification_mail(domain: str, api_key: str, code: str, user_mail: str, system_mail: str) -> None:
    """This function send user verification mail."""
    message = f"<h3>Your verification code is <span style='color: #ffffff; background-color: rgba(40, 40, 40, 0.4); padding: 4px; font-size: 30px; border-radius: 4px;'>{code}</span></h3>"
    req = requests.post(f'{URL}/{domain}/messages', auth=('api', api_key), data={
        "from": f"MAXPAY <{system_mail}>",
        "to": user_mail,
        "subject": "User Verification",
        "html": message
        })

    return req
