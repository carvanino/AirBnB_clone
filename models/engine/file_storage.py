#!usr/bin/python3
""" file_storage module
Handles serialization and deserialization
"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes instnaces to JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictyionary '__objects'
        """

        return FileStorage.__objects

    def new(self, obj):
        """ Sets in obj with key <obj class name>.id
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file '__file_path
        """

        # 'object_dict is the dict of an instance with the value pair as the
        # __dict__ of the object. ex. my_model = BaseModel() ;
        # __object = {BaseModel.<id of my_model>: "my_model"}
        # object_dict = {BaseModel.<id od my_model>: "my_model.__dict__"}
        object_dict = {}
        for key, value in FileStorage.__objects.items(): # enumerate(FileStorage.__objects):
            object_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w") as json_file:
            json_file.write(json.dumps(object_dict))
            # json.dump(object_dict, json_file)

    def reload(self):
        """ Deserializes the JSON file to __objects if '__file_path' exists
        """

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path) as f:
                # python object created from json string
                # is stored in 'obj_dict_json'
                obj_dict_json = json.load(f)
                for key, value in obj_dict_json.items():  #enumerate(obj_dict_json):
                    class_name = value["__class__"]
                    # The attribute __class__ is only added on the call of the
                    # function to_dict()
                    # So it has to be removed if we want to store new instances
                    # in __objects
                    # del(value['__class__'])
                    # eval() ex. eval(BaseModel)(**dict)) will create a new
                    # instance of BaseModel with dict as its attributes
                    obj = eval(class_name)(**value)
                    self.new(obj)  # And new ./models/base_model.py. adds this object in __objects
