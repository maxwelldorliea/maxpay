#!/usr/bin/python3
"""Handle All User Schemes."""
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str

class UserRequest(User):
    password: str

class UserResponse(User):
    id: str
