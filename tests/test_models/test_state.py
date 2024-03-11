#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import unittest
from models import storage
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the object is an instance of State and its inheritance from BaseModel."""
        self.assertIsInstance(self.state, State)
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attributes(self):
        """Test the State attributes."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "California")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["name"], "California")
        self.assertEqual(type(state_dict["created_at"]), str)
        self.assertEqual(type(state_dict["updated_at"]), str)

    def test_str(self):
        """Test the string representation of the State instance."""
        state_str = str(self.state)
        self.assertEqual(state_str, f"[State] ({self.state.id}) {self.state.__dict__}")

    def test_save(self):
        """Test the save method and if it updates 'updated_at'."""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_new_instance_in_storage(self):
        """Test if the new state is in storage."""
        self.assertIn(f"State.{self.state.id}", storage.all().keys())

if __name__ == "__main__":
    unittest.main()

