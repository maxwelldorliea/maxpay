#!/usr/bin/python3
"""This Module Represent Transaction Table In The DB."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class Transaction(BaseModel, Base):
    """This Module Represent Transaction Table In The DB."""
    __tablename__ = 'transactions'
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    action: Mapped[str] = mapped_column(String(20))
    amount: Mapped[int] = mapped_column()
    fees: Mapped[int] = mapped_column()
    balance_before_transaction: Mapped[int] = mapped_column()
    balance_after_transaction: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(String(20), server_default='successful')

