#!/usr/bin/python3
"""BaseModel Class tests module"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import uuid
import json
import time
import os
import re


class TestBaseModel(unittest.TestCase):
    """BaseModel Class tests"""

    def tearDown(self):
        """teardown"""
        self.storageReset()

    def storageReset(self):
        """storage reseting"""
        FileStorage._Filestorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Instantce testing"""
        Ba_se_ = BaseModel()
        string = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(Ba_se_)), string)
        self.assertTrue(issubclass(type(Ba_se_), BaseModel))
        self.assertIsInstance(Ba_se_, BaseModel)

    def test_init_(self):
        """ zero args passed to init during instantiation"""
        with self.assertRaises(TypeError) as te:
            BaseModel.__init__()
        mssge = "__init__() missing 1 positional argument: **kwargs"
        self.assertEqual(str(te.exception), mssge)

    def test_attributes(self):
        """attribute testing"""
        Ba_se_ = BaseModel()
        self.assertTrue(isinstance(Ba_se_.created_at, datetime))
        self.assertTrue(isinstance(Ba_se_.updated_at, datetime))
        self.assertTrue(isinstance(Ba_se_.id, str))

    def test_uuid_(self):
        """uuid testing"""
        Ba_se_ = [BaseModel().id for ke in range(1000)]
        self.assertEqual(len(set(Ba_se_)), len(Ba_se_))

    def test_save_info(self):
        """save() testing"""
        Ba_se_ = BaseModel()
        da_te = datetime.now()
        Ba_se_.save()
        self.assertTrue(abs(Ba_se_.updated_at > Ba_se_.created_at))

    def test_datetime_mtd(self):
        """datetime mtd testing"""
        Ba_se_ = BaseModel()
        da_te = datetime.now()
        sec_nds = Ba_se_.updated_at - Ba_se_.created_at
        self.assertTrue(abs(sec_nds.total_seconds()) < 0.01)
        sec_nds = Ba_se_.created_at - da_te
        self.assertTrue(abs(sec_nds.total_seconds()) < 0.1)

    def test_str_mtd(self):
        """str mtd testing"""
        Ba_se_ = BaseModel()
        ba_se_str = "[{}] ({}) {}"
        .format("BaseModel", Ba_se_.id, Ba_se_.__dict__)
        self.assertEqual(Ba_se_.__str__(), ba_se_str)

    def test_savetime(self):
        """save updates time"""
        Ba_se_ = BaseModel()
        the_time = Ba_se_.updated_at
        Ba_se_.save()
        self.assertNotEqual(the_time, Ba_se_.updated_at)
        with open("file.json", "r") as f:
            self.assertIn(Ba_se_.to_dict(), json.loads(f.read()).values())

    def test_to_dict(self):
        """__dict__ testing"""
        Ba_se_ = BaseModel()
        Ba_se_.name = "Some__barry"
        Ba_se_.age = 25
        thing = Ba_se_.to_dict()
        self.assertEqual(thing["id"], Ba_se_.id)
        self.assertEqual(thing["__class__"], type(Ba_se_).__name__)
        self.assertEqual(thing["name"], Ba_se_.name)
        self.assertEqual(thing["age"], Ba_se_.age)
        self.assertEqual(thing["created_at"], Ba_se_.created_at.isoformat())
        self.assertEqual(thing["updated_at"], Ba_se_.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
