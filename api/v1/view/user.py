#!/usr/bin/python3
"""Implements All User Related Functionalities."""
from models import storage
from models.user import User
from models.account import Account
from models.role import Role
from models.otp import OTP
from models.transaction import Transaction
from schemes.user import VerifyUser
from schemes.user import (
        UserRequest, UserResponse,TransferData,
        CurrentUser, Login, UserAcc, ChangePin)
from fastapi import HTTPException, status, Depends, APIRouter, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from api.auth.jwt_auth import get_current_user, create_access_token, is_admin
from utils.password_utils import hash_password, verify_password
from utils.mail_utils import send_verification_mail, send_transaction_alert


user_view = APIRouter(prefix='/api/v1', tags=['USER'])
@user_view.get('/users', response_model=List[UserResponse], tags=['ADMIN'])
def get_users(limit: int=25, offset: int=0, user: User=Depends(is_admin)):
    """Return list of user objects in storage base on limit parameter."""
    user_objs = storage.all(User, limit, offset)
    users = []
    for _, user in user_objs.items():
        users.append(user.to_dict())
    return users


@user_view.post('/users', response_model=CurrentUser)
def create_user(user: UserRequest, background_tasks: BackgroundTasks):
    """Create a new user in db storage."""
    user = User(**(user).dict())
    if (user.get_user_by_email()):
        raise HTTPException(
                status.HTTP_400_BAD_REQUEST, detail="user already exists!")
    account = Account(user_id=user.id, balance=1000)
    account.get_user_account_num()
    account.pin = hash_password(storage.env['DEFAULT_PIN'])
    user.password = hash_password(user.password)
    user.new()
    account.new()
    role = Role(user_id=user.id, role='user')
    role.new()
    otp = OTP(user_id=user.id, code=OTP.generate_otp())
    otp.new()
    storage.save()
    username = f'{user.first_name} {user.last_name}'
    background_tasks.add_task(
            send_verification_mail, domain=storage.env['MAIL_DOMAIN'],
            api_key=storage.env['MAIL_API_KEY'], code=otp.code,
            user_mail=user.email, system_mail=storage.env['SYSTEM_MAIL'], username=username)
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
def transfer(data: TransferData, background_tasks: BackgroundTasks, user: User = Depends(get_current_user)):
    """Transfer money from the current user account to specific user."""
    amount, account_number, pin = data.amount, data.account_number, data.pin

    if amount < 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Amount can't be negative")
    if amount % 5 != 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Amount must be divisible by 5')
    if user.account.account_number == account_number:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Can't send money to yourself")
    if not verify_password(pin, user.account.pin):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid pin")
    if user.account.balance < amount:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Not enough fund')
    account = storage.get_account_by_number(Account, account_number)
    if not account:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Not a registered user')
    user_account = storage.get(Account, user.account.id)
    balance_before_transaction=user.account.balance
    user_account.balance = user_account.balance - amount
    balance_after_transaction=user.account.balance
    message_sender = f"You have transferred <b>{amount}</b> to <b>{account_number}</b>. Your new balance is <b>{user.account.balance}</b>"
    ## Sender transaction history
    transaction_sender = Transaction(
            user_id=user.id, action="Transfer",
            balance_before_transaction=balance_before_transaction,
            balance_after_transaction=balance_after_transaction,
            message=message_sender, amount=amount, receiver_sender_acc_id=account_number)
    ## Receiver transaction history
    balance_before_transaction=account.balance
    account.balance = account.balance + amount
    balance_after_transaction=account.balance
    message = f"You have received <b>{amount}</b> from <b>{user.account.account_number}</b>. Your new balance is <b>{account.balance}</b>"
    receiver = storage.get_user_by_account_number(account_number)
    transaction_receiver = Transaction(
            user_id=receiver.id, action="Receive",
            balance_before_transaction=balance_before_transaction,
            balance_after_transaction=balance_after_transaction,
            message=message, amount=amount, receiver_sender_acc_id=user.account.account_number)
    account.new()
    user_account.new()
    transaction_sender.new()
    transaction_receiver.new()
    storage.save()
    background_tasks.add_task(
            send_transaction_alert, domain=storage.env['MAIL_DOMAIN'],
            api_key=storage.env['MAIL_API_KEY'], user_mail=user.email, system_mail=storage.env['SYSTEM_MAIL'], message=message_sender)
    background_tasks.add_task(
            send_transaction_alert, domain=storage.env['MAIL_DOMAIN'],
            api_key=storage.env['MAIL_API_KEY'], user_mail=receiver.email, system_mail=storage.env['SYSTEM_MAIL'], message=message)
    return {
            'Amount': amount,
            'type': 'transfer'
            }


@user_view.get('/users/acc/{acc_number}', response_model=UserAcc)
def get_user_by_account_number(acc_number: str, _=Depends(get_current_user)):
    """Return a user given account number."""
    user = storage.get_user_by_account_number(acc_number);
    if not user:
        raise HTTPException(404, detail="Account not register")
    return user

@user_view.get('/transactions')
def get_transaction(limit: int=25, offset: int=0, user: User = Depends(get_current_user)):
    """Return user last 25 transactions."""
    transactions = [val for _, val in storage.all(Transaction, limit, offset, user.id).items()]
    return transactions


@user_view.post('/change_pin')
def change_transaction_pin(change_pin: ChangePin, user: User=Depends(get_current_user)):
    """Change the user transaction given required and correct info is pass."""
    if len(change_pin.new_pin) != 4:
        raise HTTPException(400, detail="Length of pin must be 4")
    if not verify_password(change_pin.pin, user.account.pin):
        raise HTTPException(400, detail='Invalid pin')
    account = storage.get_account_by_number(Account, user.account.account_number)
    account.pin = hash_password(change_pin.new_pin)
    account.save()
    return {'status': 'successful'}
