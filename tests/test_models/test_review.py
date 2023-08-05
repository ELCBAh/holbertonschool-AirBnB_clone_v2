#!/usr/bin/python3
"""Review"""
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.review import Review


class test_review(test_basemodel):
    """Review"""

    def __init__(self, *args, **kwargs):
        """Review"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Review"""
        new = self.value()
        self.assertEqual((new.place_id), None)

    def test_user_id(self):
        """Review"""
        new = self.value()
        self.assertEqual((new.user_id), None)

    def test_text(self):
        """Review"""
        new = self.value()
        self.assertEqual((new.text), None)


if __name__ == "__main__":
    unittest.main()
