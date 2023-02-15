#!/usr/bin/python3
"""This Module Implements All User Features."""
from models.base_model import BaseModel


class User(BaseModel):
    """Implement all user functionalities."""
    name = ''
    username = ''
    password = ''
