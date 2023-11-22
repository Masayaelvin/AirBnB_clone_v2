#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


import os

s_type  = os.getenv('HBNB_TYPE_STORAGE')

if s_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
