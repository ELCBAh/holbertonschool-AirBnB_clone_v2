#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.user import User
import pep8
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_pep8_User(self):
        """pep8 test check"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @unittest.skipIf(type(FileStorage) is DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        user = self.value()
        old = user.updated_at
        user.save()
        self.assertLess(old, user.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("User." + user.id, f.read())
