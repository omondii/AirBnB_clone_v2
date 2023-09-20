#!/usr/bin/python3
"""This module chooses the srorage engine to use based on the env varible
   If env variable == db, a  db storage engine is instantiated
   else it instantiates a filestorage engine
"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
