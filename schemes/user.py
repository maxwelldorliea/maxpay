#!/usr/bin/python3
"""Handle All User Schemes."""
from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: EmailStr

class UserRequest(User):
    password: str

class UserResponse(User):
    id: str

    class Config:
        orm_mode=True

class VerifyUser(BaseModel):
    user_id: str
    code: int

class UserAcc(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode=True


class TransferData(BaseModel):
    account_number: str
    amount: int
    pin: str

class Account(BaseModel):
    account_number: str
    balance: int
    is_block: bool

    class Config:
        orm_mode=True

class Role(BaseModel):
    role: str

class CurrentUser(BaseModel):
    user: UserResponse
    account: Account

class Login(BaseModel):
    email: str
    password: str

class ChangePin(BaseModel):
    pin: str
    new_pin: str
