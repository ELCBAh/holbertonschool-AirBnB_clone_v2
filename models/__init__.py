#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv


storage_t = getenv('HBNB_TYPE_STORAGE')

if storage_t is not "db":
    storage = FileStorage()
    storage.reload()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
