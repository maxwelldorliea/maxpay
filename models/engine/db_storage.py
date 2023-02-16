#!/usr/bin/python3
"""This Module Handle All DB Operations For All Models."""
from models.user import User
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

models = {
        'user': User
        }


class DBStorage:
    """This class implement all db operations for all models."""
    __session = None
    __engine = None


    def __init__(self, env="production") -> None:
        """Initializes the DBStorage Engine."""
        self.__engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        if env == "development":
            Base.metadata.drop_all(self.__engine)

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
