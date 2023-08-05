#!/usr/bin/python3
"""Place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
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
        self.assertEqual((new.city_id), None)

    def test_user_id(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.user_id), None)

    def test_name(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.name), None)

    def test_description(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.description), None)

    def test_number_rooms(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.number_rooms), None)

    def test_number_bathrooms(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.number_bathrooms), None)

    def test_max_guest(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.max_guest), None)

    def test_price_by_night(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.price_by_night), None)

    def test_latitude(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.latitude), None)

    def test_longitude(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.latitude), None)

    def test_amenity_ids(self):
        """Place"""
        new = self.value()
        self.assertEqual((new.amenity_ids), [])


if __name__ == "__main__":
    unittest.main()
