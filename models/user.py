#!/usr/bin/python3
"""This Module Implements All User Features."""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List
import models


class User(BaseModel, Base):
    """Implement all user functionalities."""
    __tablename__ = 'users'
    first_name: Mapped[str] = mapped_column(String(30))
    middle_name: Mapped[str] = mapped_column(String(30), nullable=True)
    roles: Mapped[List["Role"]] = relationship()
    otp: Mapped[List["OTP"]] = relationship()
    transaction_histories: Mapped[List["Transaction"]] = relationship()
    account: Mapped["Account"] = relationship(back_populates='user')
    last_name: Mapped[str] = mapped_column(String(30))
    is_verify: Mapped[bool] = mapped_column(default=False)
    email: Mapped[str] = mapped_column(String(80), unique=True)
    password: Mapped[str] = mapped_column(String(80))
    
    def get_user_by_email(self):
        """Return user from db storage or None when not in db storage."""
        return models.storage.get_user_by_email(type(self), self.email)
