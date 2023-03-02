#!/usr/bin/python3
"""Implements All User Related Functionalities."""
from models import storage
from models.user import User
from models.account import Account
from models.role import Role
from models.otp import OTP
from models.transaction import Transaction
from schemes.user import VerifyUser
from schemes.user import UserRequest, UserResponse, TransferData, CurrentUser, Login
from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from api.auth.jwt_auth import get_current_user, create_access_token
from utils.password_utils import hash_password, verify_password


user_view = APIRouter(prefix='/api/v1', tags=['USER'])
@user_view.get('/users', response_model=List[UserResponse])
def get_users(limit: int=25, user: User=Depends(get_current_user)):
    """Return list of user objects in storage base on limit parameter."""
    user_objs = storage.all(User, limit)
    users = []
    for _, user in user_objs.items():
        users.append(user.to_dict())
    return users


@user_view.post('/users', response_model=CurrentUser)
def create_user(user: UserRequest):
    """Create a new user in db storage."""
    user = User(**(user).dict())
    if (user.get_user_by_email()):
        raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail="user already exists!")
    account = Account(user_id=user.id, balance=1000)
    account.get_user_account_num()
    account.pin = hash_password(storage.env['DEFAULT_PIN'])
    user.password = hash_password(user.password)
    user.save()
    account.save()
    role = Role(user_id=user.id, role='user')
    role.save()
    otp = OTP(user_id=user.id, code=OTP.generate_otp())
    otp.save()
    account_info = {
            'user': user,
            'account': user.account
            }
    return account_info;

@user_view.get('/users/{id}', response_model=UserResponse)
def get_user(id: str, _=Depends(get_current_user)):
    """Return a user given its id."""
    user = storage.get(User, id)
    if not user:
        raise HTTPException(
                status.HTTP_404_NOT_FOUND, detail='user not found!')
    return user.to_dict()

@user_view.post('/verify_email')
def verify_email(data: VerifyUser):
    """Verify user account."""
    if not storage.verify_user(OTP, data.user_id, data.code):
        return HTTPException(
                status.HTTP_400_BAD_REQUEST, detail='Incorrect Code')
    return {
            'status': 'Verify Successfully'
            }

@user_view.post('/sign_in', tags=['AUTH'])
def sign_in(credential: OAuth2PasswordRequestForm=Depends()):
    """Return user access token."""
    credential_exception = HTTPException(
                status.HTTP_401_UNAUTHORIZED,
                detail='Invalid email or password',
                headers={'WWW-Authenticate': 'Bearer'})
    user = storage.get_user_by_email(User, credential.username)
    if not user:
        raise credential_exception

    if not verify_password(credential.password, user.password):
        raise credential_exception

    data = {
            'id': user.id,
            'email': user.email,
            'role': user.roles[0].role
            }
    token = create_access_token(data, storage.env)
    return {
            'access_token': token,
            'token_type': 'bearer'
            }


@user_view.get('/me', response_model=CurrentUser)
def get_me(user: User=Depends(get_current_user)):
    user_info = {
            'user': user,
            'account': user.account
            }
    return user_info


@user_view.post('/transfer')
def transfer(data: TransferData, user: User = Depends(get_current_user)):
    """Transfer money from the current user account to specific user."""
    amount, account_number = data.amount, data.account_number
    
    if amount < 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Amount can't be negative")
    if amount % 5 != 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Amount must be divisible by 5')
    if user.account.balance < amount:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Not enough fund')
    if user.account.account_number == account_number:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Can't send money to yourself")
    account = storage.get_account_by_number(Account, account_number)
    if not account:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Not a registered user')
    user_account = storage.get(Account, user.account.id)
    transaction = Transaction(user_id=user.id)
    transaction.balance_before_transaction=user.account.balance
    transaction.user_id=user.id
    transaction.amount=amount
    user_account.balance = user_account.balance - amount
    account.balance = account.balance + amount
    transaction.balance_after_transaction=user.account.balance
    transaction.action = "Transfer"
    transaction.message = f"You have transferred {amount} to {account.account_number}. Your new balance is {user.account.balance}"
    account.save()
    user_account.save()
    transaction.save()
    return {
            'Amount': amount,
            'type': 'transfer'
            }
