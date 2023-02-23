#!/usr/bin/python3
"""This Module Handle Hashing And Verifying Of Password."""
from passlib.context import CryptContext


password_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    """Hash the password pass using bcrypt."""
    return password_cxt.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a with hash password from db."""
    return password_cxt.verify(password, hashed_password)
