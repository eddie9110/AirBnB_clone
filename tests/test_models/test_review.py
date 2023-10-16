#!/usr/bin/python3
"""class Review test module"""

from datetime import datetime
import time
from models import storage
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import re
import json
import os
import uuid
import unittest


class TestReview(unittest.TestCase):
    """review class tests"""

    def tearDown(self):
        """teardown"""
        self.storage_Reset()

    def storage_Reset(self):
        """storage reset"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        """attribute testing"""
        re_view = Review()
        self.assertTrue(re_view.place_id == "")
        self.assertTrue(re_view.text == "")
        self.assertTrue(re_view.user_id == "")

    def test_instantiation_subclass(self):
        """instantiaion testing"""
        re_view = Review()
        self.assertEqual(str(type(re_view)), "<class 'models.review.Review'>")
        self.assertTrue(issubclass(type(re_view), BaseModel))
        self.assertIsInstance(re_view, Review)


if __name__ == "__main__":
    unittest.main()
