#!/usr/bin/python3
"""State"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """State"""

    def __init__(self, *args, **kwargs):
        """State"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """State"""
        new = self.value()
        self.assertEqual((new.name), None)


if __name__ == "__main__":
    unittest.main()
