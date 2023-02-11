#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""BaseModel class that defines all common attributes/methods for other classes
"""


class BaseModel():
    # public imstance attributes
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            from_iso = ['created_at', 'updated_at']
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in from_iso:
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value

    # defining the official representaton of the class BaseModel
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    # function to update the time an object is updated
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    # funtion to return a dictionary containing
    # all keys/values of __dict__ of the instance
    def to_dict(self):
        new_dict = dict()
        to_iso = ['created_at', 'updated_at']
        for key, value in self.__dict__.items():
            if key in to_iso:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
