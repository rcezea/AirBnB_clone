#!/usr/bin/python3

"""class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances:
"""

import re
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State


class FileStorage:
    # private class attributes
    # json file path
    __file_path = "file.json"
    # dictionary storage for all objects of a class instance by class id
    __objects = dict()

    # function to return the dictionary storing class instances
    def all(self):
        return self.__objects

    # function to update the dictionary storage with new class instances
    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    # funtion to serialize the dictionary storage to a JSON file
    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = dict()
        for key, val in self.__objects.items():
            new_dict[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as filename:
            json.dump(new_dict, filename)

    # function to deserialize dictionary storage from a JSON file
    def reload(self):
        """
        Deserializes objects from file
        """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                old_dict = json.load(file)
                for key in old_dict.values():
                    self.new(eval(key["__class__"])(**key))
        except Exception:
            return
