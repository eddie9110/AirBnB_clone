#!/usr/bin/python3
""" test module for our FileStorage class"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os
import uuid


class TestFileStorage(unittest.TestCase):
    """testing FileStorage class"""
    def storageReset(self):
        """resetting storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """teardown"""
        self.storageReset()

    def test_name_(self):
        """name check"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """testing zero args passed"""
        self.storageReset()
        with self.assertRaises(TypeError) as fl:
            FileStorage.__init__()
        mssge = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(fl.exception), mssge)

    """testing all"""
    def all_testing_one(self, classname):
        """testing all"""
        self.storageReset()
        self.assertEqual(storage.all(), {})

        insta_nce = storage.classes()[classname]()
        storage.new(insta_nce)
        ke_y = "{}.{}".format(type(insta_nce).__name__, insta_nce.id)
        self.assertTrue(ke_y in storage.all())
        self.assertEqual(storage.all()[ke_y], insta_nce)

    def test_base_all(self):
        """testing all on BaseModel"""
        self.all_testing_one("BaseModel")

    def test_user_all(self):
        """testing all on User"""
        self.all_testing_one("User")

    def test_place_all(self):
        """testing all on Place"""
        self.all_testing_one("Place")

    def test_review_all(self):
        """testing all on Review"""
        self.all_testing_one("Review")

    def test_state_all(self):
        """testing all on State"""
        self.all_testing_one("State")

    def test_city_all(self):
        """testing all on City"""
        self.all_testing_one("City")

    def test_amenity_all(self):
        """testing all on Amenity"""
        self.all_testing_one("Amenity")

    """testing new"""
    def new_testing(self, classname):
        """testing new"""
        self.storageReset()
        cls = storage.classes()[classname]
        insta_nce = cls()
        storage.new(insta_nce)
        ke_y = "{}.{}".format(type(insta_nce).__name__, insta_nce.id)
        self.assertTrue(ke_y in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[ke_y], insta_nce)

    def test_base_new(self):
        """testing new on BaseModel"""
        self.new_testing("BaseModel")

    def test_user_new(self):
        """testing new on User"""
        self.new_testing("User")

    def test_state_new(self):
        """testing new on state"""
        self.new_testing("State")

    def test_place_new(self):
        """testing new on place"""
        self.new_testing("Place")

    def test_review_new(self):
        """testing new on review"""
        self.new_testing("Review")

    def test_city_new(self):
        """testing new on city"""
        self.new_testing("City")

    def test_amenity_new(self):
        """testing new on Amenity"""
        self.new_testing("Amenity")

    def test_wthout_args_new(self):
        """testing new with 0 args passed"""
        self.storageReset()
        with self.assertRaises(TypeError) as fl:
            storage.new()
        mssge = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(fl.exception), mssge)

    def test_excess_args_new(self):
        """testing with excess args"""
        self.storageReset()
        insta_nce = BaseModel()
        with self.assertRaises(TypeError) as fl:
            storage.new(insta_nce, 42)
        mssge = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(fl.exception), mssge)

    def reload_test_(self, classname):
        """reloading testing"""
        self.storageReset()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes()[classname]
        obj = cls()
        storage.new(obj)
        ke_y = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        storage.reload()
        self.assertEqual(obj.to_dict(), storage.all()[ke_y].to_dict())

    def test_base_reload(self):
        """ testing reload on base"""
        self.reload_test_("BaseModel")

    def test_user_reload(self):
        """ testing reloading on user """
        self.reload_test_("User")

    def test_city_reload(self):
        """ testing reloading on city """
        self.reload_test_("City")

    def test_place_reload(self):
        """ testing reloading on place"""
        self.reload_test_("Place")

    def test_review_reload(self):
        """ testing reloading on review """
        self.reload_test_("Review")

    def test_state_reload(self):
        """testing reloading on state """
        self.reload_test_("State")

    def test_amenity_reload(self):
        """ testing reloading on amenity"""
        self.reload_test_("Amenity")

    def save_testing(self, classname):
        """tesing save"""
        self.storageReset()
        cls = storage.classes()[classname]
        obj = cls()
        storage.new(obj)
        ke_y = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        dict_ = {ke_y: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(dict_)))
            f.seek(0)
            self.assertEqual(json.load(f), dict_)

    def test_base_save(self):
        """tesing save on base model"""
        self.save_testing("BaseModel")

    def test_user_save(self):
        """testing save on user"""
        self.save_testing("User")

    def test_amenity_save(self):
        """ testing save on amenity"""
        self.save_testing("Amenity")

    def test_place_save(self):
        """testing save on place"""
        self.save_testing("Place")

    def test_review_save(self):
        """ testing save on review"""
        self.save_testing("Review")

    def test_state_save(self):
        """testing save on state"""
        self.save_testing("State")

    def test_city_save(self):
        """testing save on city"""
        self.save_testing("City")

    def test_zero_args_save(self):
        """ testing zero args passed"""
        self.storageReset()
        with self.assertRaises(TypeError) as fl:
            FileStorage.save()
        mssge = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(fl.exception), mssge)

    def test_excess_args_save(self):
        """testing excess args"""
        self.storageReset()
        with self.assertRaises(TypeError) as fl:
            FileStorage.save(self, 98)
        mssge = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(fl.exception), mssge)

    def test_cls_attributes(self):
        """testing class attributes"""
        self.storageReset()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))


if __name__ == '__main__':
    unittest.main()
