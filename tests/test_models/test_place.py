#!/usr/bin/python3
"""class Place tests module"""

import unittest
from datetime import datetime
import json
import time
import uuid
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import re
import os
from models import storage


class TestPlace(unittest.TestCase):
    """class Place tests"""

    def tearDown(self):
        """teardown"""
        self.storageReset()

    def storageReset(self):
        """reseting storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """testing attributes"""
        Ka_Nairo = Place()
        self.assertTrue(Ka_Nairo.city_id == "")
        self.assertTrue(Ka_Nairo.user_id == "")
        self.assertTrue(Ka_Nairo.name == "")
        self.assertTrue(Ka_Nairo.amenity_ids == [])
        self.assertTrue(Ka_Nairo.number_rooms == 0)
        self.assertTrue(Ka_Nairo.number_bathrooms == 0)
        self.assertTrue(Ka_Nairo.description == "")
        self.assertTrue(Ka_Nairo.price_by_night == 0)
        self.assertTrue(Ka_Nairo.latitude == 0.0)
        self.assertTrue(Ka_Nairo.longitude == 0.0)
        self.assertTrue(Ka_Nairo.max_guest == 0)

    def test_instantiation_subclass(self):
        """testing instances"""
        Ka_Nairo = Place()
        self.assertEqual(str(type(Ka_Nairo)), "<class 'models.place.Place'>")
        self.assertTrue(issubclass(type(Ka_Nairo), BaseModel))
        self.assertIsInstance(Ka_Nairo, Place)


if __name__ == "__main__":
    unittest.main()
