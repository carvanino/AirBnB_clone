#!/usr/bin/python3
"""Defines FileStorage Class
This class serilaizes instances to a JSON file and deserializes
JSON files to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """An abstracted storage engine

    Attr:
        __file_path (str): path to the JSON file
        __objects (dict): will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary "__objects"."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <class name>.id"""
        key_format = obj.__class__.__name__
        FileStorage.__objects[f"{key_format}.{id}"] = obj

    def save(self):
        """serialises __objects to the JSON file path __file_path"""
        fs_dict = FileStorage.__objects
        obj_dict = dict()
        for obj in fs_dict.keys():
            obj_dict[obj] = fs_dict[obj].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists
        Otherwise, do nothing.

        If the file doesnt exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
