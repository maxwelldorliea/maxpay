#!/usr/bin/python3
"""This Module Represent My User Transaccount Account In The DB."""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
import models


class Account(BaseModel, Base):
    """This Module Represent My User Transaccount Account In The DB."""
    
    __tablename__ = 'accounts'
    
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), unique=True)
    user: Mapped['User'] = relationship(back_populates='account')
    account_number: Mapped[str] = mapped_column(String(10), unique=True)
    balance: Mapped[int] = mapped_column()
    pin: Mapped[str] = mapped_column(String(80))
    active: Mapped[bool] = mapped_column(default=True)
    is_block: Mapped[bool] = mapped_column(default=False)


    def get_account_by_number(self):
        """Return an account from db given it exists."""
        return models.storage.get_account_by_number(type(self), self.account_number)

    def get_user_account_num(self):
        """Assign a new user account number."""
        self.account_number = models.storage.get_user_account_num(type(self))
