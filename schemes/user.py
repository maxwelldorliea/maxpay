#!/usr/bin/python3
"""Handle All User Schemes."""
from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str

class UserRequest(User):
    password: str

class UserResponse(User):
    id: str

    class Config:
        orm_mode=True

class VerifyUser(BaseModel):
    user_id: str
    code: int

class TransferData(BaseModel):
    account_number: str
    amount: int

class Account(BaseModel):
    account_number: str
    balance: int

class Role(BaseModel):
    role: str

class CurrentUser(BaseModel):
    user: UserResponse
    account: Account
    role: List[Role]
