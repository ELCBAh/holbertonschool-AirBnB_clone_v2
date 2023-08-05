#!/usr/bin/python3
"""
Unittests for the console
"""
import unittest
import os
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


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


if __name__ == "__main__":
    unittest.main()
