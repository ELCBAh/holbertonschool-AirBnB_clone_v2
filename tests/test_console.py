#!/usr/bin/python3
"""
Unittests for the console
"""
import unittest
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Console tests"""
    def tearDown(self):
        """Tear down test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def setUp(self):
        """Set up test"""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit"""
        self.assertEqual(self.console.onecmd("quit"), None)

    def test_EOF(self):
        """Test EOF"""
        self.assertEqual(self.console.onecmd("EOF"), None)


if __name__ == "__main__":
    unittest.main()
