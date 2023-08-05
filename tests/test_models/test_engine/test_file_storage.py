#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models import storage
import json


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage.__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        store = storage.all()
        self.assertIn(new.to_dict()['__class__'], store)
        self.assertIn(new, store.values())

    def test_all(self):
        """ __objects is properly returned """
        obj = storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage.all())
        self.assertEqual(len(obj), 0)

    def test_methods(self):
        """ Methods exist """
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'reload'))

    def test_attributes(self):
        """ attributes exist """
        self.assertTrue(hasattr(storage, '__file_path'))
        self.assertTrue(hasattr(storage, '__objects'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        with open("file.json", "w") as f:
            key = "{}.{}".format(type(new).__name__, new.id)
            json.dump({key: new.to_dict()}, f)
        storage.reload()
        store = FileStorage.__objects.keys()
        self.assertIn("BaseModel." + str(new.id), store)

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage.__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_docstrings(self):
        """docstrings test check"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    @classmethod
    def setUpClass(cls):
        """Set up class for testing"""
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down class for testing"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
