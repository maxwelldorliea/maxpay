#!/usr/bin/python3

"""This Module Implement All Share Attributes."""
import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import func, String
from sqlalchemy.orm import DeclarativeBase
import models

class Base(DeclarativeBase):
    pass


class BaseModel:
    """Implement All Share Atrributes."""
    id: Mapped[str] = mapped_column(String(60), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(nullable=True, onupdate=func.now())


    def __init__(self, *arg, **kwargs) -> None:
        if kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            else:
                if type(self.created_at) is str:
                    fmt = '%Y-%m-%dT%H:%M:%S.%f'
                    self.created_at = datetime.strptime(self.created_at, fmt)
            if 'updated_at' not in kwargs:
                self.updated_at = None
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Return string representation of the object."""
        model = self.__class__.__name__
        return "[{}] ({}) {}".format(model, self.id, self.__dict__);

    def save(self):
        """Save the object in the storage engine."""
        self.updated_at = datetime.utcnow();
        models.storage.new(self)
        models.storage.save()

    def new(self):
        """Add an object to the db session."""
        models.storage.new(self)
    
    def to_dict(self):
        """Convert the object to dictionary representation."""
        obj = self.__dict__.copy()
        if obj['updated_at']:
            obj['updated_at'] = obj['updated_at'].isoformat()
        if obj.get('_sa_instance_state'):
            del obj['_sa_instance_state']
        obj['created_at'] = obj['created_at'].isoformat()
        obj['__class__'] = self.__class__.__name__
        return obj
