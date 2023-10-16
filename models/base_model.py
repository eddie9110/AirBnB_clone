#!/usr/bin/python3
"""BaseModel module"""

from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """The parent class that all classes will inherit from"""
    def __init__(self, *args, **kwargs):
        """Initialising the base class"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """mtd prints a base model instance"""
        return f"[{self.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """this method updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict2 = self.__dict__.copy()
        dict2["__class__"] = type(self).__name__
        dict2["created_at"] = my_dict["created_at"].isoformat()
        dict2["updated_at"] = my_dict["updated_at"].isoformat()
        return dict2
