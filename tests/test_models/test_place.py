#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.place import Place
import pep8
import unittest


class test_Place(test_basemodel):
    """Place"""

    def __init__(self, *args, **kwargs):
        """Place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Place"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_pep8_Place(self):
        """pep8 test check"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """testing docstring"""
        self.assertIsNotNone(Place.__doc__)

    @unittest.skipIf(type(FileStorage) is DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        place = self.value()
        old = place.updated_at
        place.save()
        self.assertLess(old, place.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Place." + place.id, f.read())


if __name__ == "__main__":
    unittest.main()
