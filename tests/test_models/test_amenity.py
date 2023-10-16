#!/usr/bin/python3
"""tests module for Amenity class"""

import unittest
import json
from datetime import datetime
import time
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import re
import os
from models import storage
import uuid


class TestAmenity(unittest.TestCase):
    """Amenity Class tests"""

    def tearDown(self):
        """tear it down"""
        self.storageReset()
        pass

    def storageReset(self):
        """storage reset"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """ attribute testing"""
        Bafu = Amenity()
        self.assertTrue(Bafu.name == "")

    def test_instance_subclass(self):
        """instantiation tests"""
        Bafu = Amenity()
        self.assertEqual(str(type(Bafu)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(Bafu, Amenity)
        self.assertTrue(issubclass(type(Bafu), BaseModel))


if __name__ == "__main__":
    unittest.main()
