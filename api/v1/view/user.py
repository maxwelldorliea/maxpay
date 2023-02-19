#!/usr/bin/python3
"""Implements All User Related Functionalities."""
from models import storage
from models.user import User
from models.account import Account
from models.role import Role
from api.v1.view import app_view
from schemes.user import UserRequest
from fastapi import HTTPException, status


@app_view.get('/users')
def get_users(limit: int=25):
    """Return list of user objects in storage base on limit parameter."""
    user_objs = storage.all(User, limit)
    users = []
    for _, user in user_objs.items():
        users.append(user.to_dict())
    return users

@app_view.post('/users')
def create_user(user: UserRequest):
    """Create a new user in db storage."""
    user = User(**(user).dict())
    if (user.get_user_by_email()):
        raise HTTPException(400, detail="user already exists!")
    account = Account(user_id=user.id, pin=4444, balance=1000)
    account.get_user_account_num()
    user.save()
    account.save()
    role = Role(user_id=user.id, role='user')
    role.save()
    return user.to_dict()

@app_view.get('/users/{id}')
def get_user(id: str):
    """Return a user given its id."""
    user = storage.get(User, id)
    if not user:
        raise HTTPException(
                status.HTTP_404_NOT_FOUND, detail='user not found!')
    return user
