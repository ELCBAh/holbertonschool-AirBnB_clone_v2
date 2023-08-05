#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.city import City
import pep8
import unittest


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_City(self):
        """pep8 test check"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @unittest.skipIf(type(FileStorage) is DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        city = self.value()
        old = city.updated_at
        city.save()
        self.assertLess(old, city.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("City." + city.id, f.read())
