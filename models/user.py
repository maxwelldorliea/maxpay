#!/usr/bin/python3
"""This Module Implements All User Features."""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class User(BaseModel, Base):
    """Implement all user functionalities."""
    __tablename__ = 'users'
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
