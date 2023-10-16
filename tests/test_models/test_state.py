#!/usr/bin/python3
"""class State tests module"""

import unittest
import json
from models import storage
from datetime import datetime
import time
import uuid
from models.state import State
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import re
import os


class TestState(unittest.TestCase):
    """class for tests for state """

    def tearDown(self):
        """tear it down"""
        self.storageReset()

    def storageReset(self):
        """storage resetting"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation_subclass(self):
        """instantiation testing"""
        Ka_Nairo = State()
        self.assertEqual(str(type(Ka_Nairo)), "<class 'models.state.State'>")
        self.assertTrue(issubclass(type(Ka_Nairo), BaseModel))
        self.assertIsInstance(Ka_Nairo, State)

    def test_attributes(self):
        """testing attributes"""
        Ka_Nairo = State()
        self.assertTrue(Ka_Nairo.name == "")


if __name__ == "__main__":
    unittest.main()
