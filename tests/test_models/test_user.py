#!/usr/bin/python3
"""User class tests module"""

import unittest
from datetime import datetime
import time
from models import storage
from models.user import User
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import re
import json
import os
import uuid


class TestUser(unittest.TestCase):

    """class User tests"""
    def tearDown(self):
        """teardown"""
        self.storageReset()

    def storageReset(self):
        """reseting storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """attribute testing"""
        Some_barry = User()
        self.assertTrue(Some_barry.first_name == "")
        self.assertTrue(Some_barry.last_name == "")
        self.assertTrue(Some_barry.email == "")
        self.assertTrue(Some_barry.password == "")

    def test_instantiation_subclass(self):
        """instantiation testing"""
        Some_barry = User()
        self.assertEqual(str(type(Some_barry)), "<class 'models.user.User'>")
        self.assertTrue(issubclass(type(Some_barry), BaseModel))
        self.assertIsInstance(Some_barry, User)


if __name__ == "__main__":
    unittest.main()
