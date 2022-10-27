#!/usr/bin/python3
"""Defines a BaseModel Class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents BaseModel of project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel class

        Args:
            args (any): unused argument
            kwargs (dict): key-value pairs of attributes.
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, val in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(val, time_format)
                else:
                    self.__dict__[key] = val

    def save(self):
        """updates 'update_at' with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__
        of the instance
        """

        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """return the print/str representation of BaseModel instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
