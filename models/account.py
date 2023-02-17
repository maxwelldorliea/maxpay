#!/usr/bin/python3
"""This Module Represent My User Transaccount Account In The DB."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer


class Account(BaseModel, Base):
    """This Module Represent My User Transaccount Account In The DB."""
    
    __tablename__ = 'accounts'
    
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), unique=True)
    user: Mapped['User'] = relationship(back_populates='account')
    account_number: Mapped[int] = mapped_column(unique=True)
    balance: Mapped[int] = mapped_column()
    pin: Mapped[int] = mapped_column()
    active: Mapped[bool] = mapped_column(default=True)
    is_block: Mapped[bool] = mapped_column(default=False)
