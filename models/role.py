#!/usr/bin/python3
"""This Module Implement Roles that Will Be Own By User In The System."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey


class Role(BaseModel, Base):
    __tablename__ = "roles"
    """This model represent role in my system."""
    role: Mapped[str] = mapped_column(String(20))
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
