#!/usr/bin/python3
"""
Unittests for the console
"""
import unittest
import os
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import pep8


class TestConsole(unittest.TestCase):
    """Console tests"""

    @classmethod
    def setUpClass(cls):
        """Set up test"""
        cls.console = HBNBCommand()

    def tearDown(self):
        """Tear down test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def setUp(self):
        """Set up test"""
        FileStorage.__objects = {}

    def test_quit(self):
        """Test quit"""
        self.assertEqual(self.console.onecmd("quit"), None)

    def test_EOF(self):
        """Test EOF"""
        self.assertEqual(self.console.onecmd("EOF"), None)

    def test_pep8_City(self):
        """pep8 test check"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
