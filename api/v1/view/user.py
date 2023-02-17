#!/usr/bin/python3
"""Implements All User Related Functionalities."""
from models import storage
from models.user import User
from api.v1.view import app_view


@app_view.get('/users')
def get_users(limit: int=25):
    """Return list of user objects in storage base on limit parameter."""
    user_objs = storage.all(User, limit)
    users = []
    for _, user in user_objs.items():
        users.append(user.to_dict())
    return users

