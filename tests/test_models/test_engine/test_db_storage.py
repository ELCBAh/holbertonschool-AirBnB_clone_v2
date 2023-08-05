#!/usr/bin/python3
"""Unittest for DBStorage"""
import unittest
from models.user import User
from models.engine.db_storage import DBStorage
import pep8


class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage"""
    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.user = User()
        cls.user.first_name = "XXXX"
        cls.user.last_name = "XXX"
        cls.user.email = "XXXXX@XXXXXX.X"
        cls.user.password = "XXXXXX"
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down for test"""
        del cls.user

    def test_all(self):
        """Test all method"""
        storage = DBStorage()
        all_objs = storage.all()
        self.assertIn(self.user, all_objs.values())
        self.assertIsInstance(all_objs, dict)
        self.assertTrue(hasattr(all_objs, "__class__"))

    def test_new(self):
        """Test new method"""
        storage = DBStorage()
        all_objs = storage.all()
        user = User()
        user.first_name = "XXXX"
        user.last_name = "XXX"
        user.email = "XXXXX@XXXXXX.X"
        user.password = "XXXXXX"
        storage.new(user)
        self.assertIn(user, all_objs.values())

    def test_pep8(self):
        """pep8 test check"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
