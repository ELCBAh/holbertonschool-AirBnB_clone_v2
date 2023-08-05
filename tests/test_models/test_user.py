#!/usr/bin/python3
"""User"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_User(test_basemodel):
    """User"""

    def __init__(self, *args, **kwargs):
        """User"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """User"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """User"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """User"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """User"""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
