#!/usr/bin/python3
"""This Module Handle All DB Operations For All Models."""
from models.user import User
from models.role import Role
from models.account import Account
from models.transaction import Transaction
from models.otp import OTP
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import random

models = {
        'user': User,
        'role': Role,
        'account': Account,
        'transaction': Transaction,
        'otp': OTP
        }


class DBStorage:
    """This class implement all db operations for all models."""
    __session = None
    __engine = None


    def __init__(self, dot_env=True) -> None:
        """Initializes the DBStorage Engine."""
        self.env = self.config_env()
        if dot_env:
            self.__engine = create_engine("mysql://{}:{}@{}/{}".format(
                self.env['DB_USER'], self.env['DB_PASS'],
                self.env['HOST'], self.env['DB']
                ), pool_pre_ping=True)
        else:
            self.__engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        if self.env.get('ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def config_env(self) -> dict:
        """Set environment from dot env file."""
        env={}
        with open('.env') as env_file:
            for line in env_file:
                key, val = line.strip('\n').strip(' ').split('=')
                env[key] = val
        return env


    def all(self, cls=None, limit=25, offset=0, user_id=None) -> dict:
        """Return all objects in the db or all objects for the class pass."""
        objs = {}
        if not cls:
            for name, model in models.items():
                result = self.__session.query(model).offset(offset).limit(limit).all()
                for obj in result:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objs[key] = obj
            return objs
        if not user_id:
            result = self.__session.query(cls).offset(offset).limit(limit).all()
        else:
            result = self.__session.query(cls).where(cls.user_id == user_id).offset(offset).limit(limit).all()
        for obj in result:
            key = f'{obj.__class__.__name__}.{obj.id}'
            objs[key] = obj
        return objs

    def new(self, obj=None) -> None:
        """Add the object pass to it to the db session."""
        if not obj:
            return
        self.__session.add(obj)

    def get(self, cls=None, id=None) -> object:
        """Return an object given its id and class  name."""
        if not cls or not id:
            return None
        obj = self.__session.query(cls).where(cls.id == id).first()
        if not obj:
            return None
        return obj

    def save(self) -> None:
        """Commit the current db session."""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def close(self) -> None:
        """Close the current db session."""
        self.__session.close()

    def reload(self) -> None:
        """Initialize the db."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session

    def get_user_by_email(self, cls: User, email: str) -> User:
        """Return a user from db given its email."""
        user = self.__session.query(cls).where(cls.email == email).first()
        if not user:
            return None
        return user

    def get_account_by_number(
            self, cls: Account, account_number: str) -> Account:
        """Return an account given its number or None."""
        account = self.__session.query(cls).where(
                cls.account_number == account_number).first()

        if not account:
            return None
        return account

    def get_user_account_num(self, cls: Account) -> str:
        """Get an account number for a new user."""
        nums='0123456789'
        account_number="".join(random.choices(nums, k=10))

        while self.get_account_by_number(cls, account_number):
            account_number="".join(random.choices(num, k=10))
        return account_number

    def get_user_by_account_number(self, acc_number: str):
        """Return an user given account number."""
        acc = self.get_account_by_number(Account, acc_number)
        if not acc:
            return
        user = self.get(User, acc.user_id)
        return user

    def verify_user(self, cls: OTP, user_id: str, code: int) -> bool:
        """Verify user registration."""
        user: User = self.get(User, user_id)
        otp = self.__session.query(cls).where(cls.user_id == user_id).first()
        if not otp or otp.code != code:
            return False
        user.is_verify = True
        self.delete(otp)
        self.save()
        return True

    def update(self, cls, obj) -> None:
        """Update the current object."""
        self.__session.query(cls).update(obj)

    def delete(self, obj) -> None:
        """Delete the current object."""
        self.__session.delete(obj)
