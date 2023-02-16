#!/usr/bin/python3
"""This Module Handle All DB Operations For All Models."""
from models.user import User
from models.role import Role
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

models = {
        'user': User,
        'role': Role
        }


class DBStorage:
    """This class implement all db operations for all models."""
    __session = None
    __engine = None


    def __init__(self, dot_env=True) -> None:
        """Initializes the DBStorage Engine."""
        if dot_env:
            self.env = self.config_env()
            env = self.env
            self.__engine = create_engine("mysql://{}:{}@{}/{}".format(
                self.env['db_user'], self.env['db_pass'],
                self.env['host'], self.env['db']
                ), pool_pre_ping=True)
        else:
            self.__engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
            self.env = {}
        if self.env.get('env') == "test":
            Base.metadata.drop_all(self.__engine)

    def config_env(self) -> dict:
        """Set environment from dot env file."""
        env={}
        with open('.env') as env_file:
            for line in env_file:
                key, val = line.strip('\n').strip(' ').split('=')
                env[key] = val
        return env


    def all(self, cls=None) -> dict:
        """Return all objects in the db or all objects for the class pass."""
        objs = {}
        if not cls:
            for name, model in models.items():
                result = self.__session.query(model).all()
                for obj in result:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objs[key] = obj
            return objs

        result = self.__session.query(cls).all()
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
        objs = self.all(cls)
        key = f'{cls.__name__}.{id}'
        for k, obj in objs.items():
            if k == key:
                return obj
        return None

    def save(self) -> None:
        """Commit the current db session."""
        self.__session.commit()

    def close(self) -> None:
        """Close the current db session."""
        self.__session.close()

    def reload(self):
        """Initialize the db."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session
