#!/usr/bin/python3
"""BaseModel module
Defines all common attributes aand methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ Defines the class BaseModel """

    def __init__(self):
        """ Initilizes instance of the class BaseModel """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints an informal representation of an instance of BaseModel """

        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))


    def save(self):
        """ Updates the attribute updated_at with the current datetime """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary representation of an instance """

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()

        return new_dict
