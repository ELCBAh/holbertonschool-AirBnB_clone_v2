#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.amenity import Amenity
import pep8
import unittest


class test_Amenity(test_basemodel):
    """Amenity"""

    def __init__(self, *args, **kwargs):
        """Amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Amenity"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_Amenity(self):
        """pep8 test check"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """testing docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    @unittest.skipIf(type(FileStorage) is DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        amenity = self.value()
        old = amenity.updated_at
        amenity.save()
        self.assertLess(old, amenity.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Amenity." + amenity.id, f.read())


if __name__ == "__main__":
    unittest.main()
