#!/usr/bin/python3
"""Test module for City class"""

import re
from datetime import datetime
import time
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
import uuid
import unittest
from models import storage


class TestCity(unittest.TestCase):
    """Tests for class City"""

    def tearDown(self):
        """tear down"""
        self.storageReset()
        pass

    def storageReset(self):
        """reseting the storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """test attributes of the city class"""
        Ka_nairo = City()
        self.assertTrue(Ka_nairo.state_id == "")
        self.assertTrue(Ka_nairo.name == "")

    def test_instance_subclass(self):
        """creating an instance of the class City"""
        Ka_nairo = City()
        self.assertEqual(str(type(Ka_nairo)), "<class 'models.city.City'>")
        self.assertIsInstance(Ka_nairo, City)
        self.assertTrue(issubclass(type(Ka_nairo), BaseModel))


if __name__ == "__main__":
    unittest.main()
