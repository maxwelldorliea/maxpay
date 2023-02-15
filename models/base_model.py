#!/usr/bin/python3

"""This Module Implement All Share Attributes."""
import uuid
from datetime import datetime


class BaseModel:
    """Implement All Share Atrributes."""

    def __init__(self, *args, **kwargs):
        """Initialize the base model."""
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())
            if not kwargs.get('created_at'):
                self.created_at = datetime.utcnow()
            elif type(self.created_at) is str:
                f = "%Y-%m-%dT%H:%M:%S.%f"
                self.created_at = self.created_at.strptime(self.created_at, f)
            if kwargs.get('updated_at') and type(self.updated_at) is str:
                f = "%Y-%m-%dT%H:%M:%S.%f"
                self.updated_at = self.updated_at.strptime(self.updated_at, f)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = None

    def __str__(self):
        """Return string representation of the object."""
        model = self.__class__.__name__
        return "[{}] ({}) {}".format(model, self.id, self.__dict__);

    def save(self, obj=None):
        """Save the object in the storage engine."""
        self.updated_at = datetime.utcnow();
    
    def to_dict(self):
        """Convert the object to dictionary representation."""
        obj = self.__dict__
        if obj['updated_at']:
            obj['updated_at'] = obj['updated_at'].isoformat()
        obj['created_at'] = obj['created_at'].isoformat()
        obj['__class__'] = self.__class__.__name__
        return obj

id = str(uuid.uuid4())

obj = {
        'name': 'Max',
        'role': 'Admin'
        }

base = BaseModel(**obj)
print(base)
base.save()
print(base.to_dict())
