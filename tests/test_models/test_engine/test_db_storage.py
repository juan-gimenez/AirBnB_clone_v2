#!/usr/bin/python
""" DB_Storage """
from models.engine.file_storage import FileStorage
import unittest
import pep8
import os
from models.user import User


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
        """ tests for db """









