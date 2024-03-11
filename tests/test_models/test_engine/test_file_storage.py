#!/usr/bin/python3
"""Module to test the FileStorage class."""
import unittest
import json
import os
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test cases."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up tasks."""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all() returns the dictionary __objects."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new() correctly adds objects to __objects."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    @patch('json.dump')
    def test_save(self, mock_dump):
        """Test that save() correctly calls json.dump."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        mock_dump.assert_called()

    @patch('json.load')
    def test_reload_file_not_found(self, mock_load):
        """Test reload does nothing if file does not exist and does not raise."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"reload() raised an exception {e}.")

    @patch('builtins.open')
    @patch('json.load')
    def test_reload_file_exists(self, mock_load, mock_open):
        """Test reload successfully calls json.load on file content."""
        mock_load.return_value = {}
        self.storage.reload()
        mock_open.assert_called_with(self.storage._FileStorage__file_path, 'r')
        mock_load.assert_called()

    def test_reload_with_actual_objects(self):
        """Test reloading objects from a file."""
        obj = BaseModel()
        obj.save()
        storage = FileStorage()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

if __name__ == "__main__":
    unittest.main()

