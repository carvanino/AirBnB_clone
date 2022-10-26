#!/usr/bin/python3
""" Unittest Module for BaseModel Module
"""


import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelMethods(unittest.TestCase):
    """ Unittest for testing instantiation of the BaseModel class """

    my_model = BaseModel()

    def testBaseModel_attr(self):
        """ Test attributes values of a BaseModel instances """

        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertIsInstance(self.my_model.id, str)
        self.assertEqual(self.my_model.id, my_model_json['id'])
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def testSave(self):
        """ Tests the save method that updates the attribute updated_at
        of an instance of BaseModel """

        self.my_model.first_name = "Nick"
        self.my_model.save()

        dictt = self.my_model.to_dict()

        self.my_model.first_name = "Morty"
        self.my_model.save()
        new_dict = self.my_model.to_dict()

        self.assertEqual(dictt['created_at'], new_dict['created_at'])
        self.assertNotEqual(dictt['updated_at'], new_dict['updated_at'])

    def testTo_dict(self):
        """  Tests the to_dict method that returns a dictionary
        representation of an instance """

        self.assertEqual(dict, type(self.my_model.to_dict()))
        self.assertIn('__class__', self.my_model.to_dict())
        self.assertIn("id", self.my_model.to_dict())
        self.assertIn("created_at", self.my_model.to_dict())
        self.assertIn("updated_at", self.my_model.to_dict())


if __name__ == '__main__':
    unittest.main()
