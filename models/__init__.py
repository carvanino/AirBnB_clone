#!/usr/bin/python3
""" Links file_storage with base_model
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
