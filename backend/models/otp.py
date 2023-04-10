#!/usr/bin/python3
"""This Module Implement Roles that Will Be Own By User In The System."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
import random

class OTP(BaseModel, Base):
    __tablename__ = "otps"
    """This model represent role in my system."""
    code: Mapped[int] = mapped_column()
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))

    @staticmethod
    def generate_otp():
        """Generate six digit otp code."""
        numbers="0123456789"
        return int("".join(random.choices(numbers, k=6)))

