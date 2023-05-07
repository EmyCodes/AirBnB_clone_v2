#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os


storage = FileStorage()
storage.reload()
if 'HBNB_TYPE_STORAGE' == 'db':
    from models.engine.db_storage import DbStorage

