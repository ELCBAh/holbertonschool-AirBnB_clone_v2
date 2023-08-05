#!/usr/bin/python3
"""City"""
from tests.test_models.test_base_model import test_basemodel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.city import City
import unittest


class test_City(test_basemodel):
    """City"""

    def __init__(self, *args, **kwargs):
        """City"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """City"""
        new = self.value()
        self.assertEqual((new.state_id), None)

    def test_name(self):
        """City"""
        new = self.value()
        self.assertEqual((new.name), None)


if __name__ == "__main__":
    unittest.main()
