#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.user = User()
        cls.user.first_name = "John"
        cls.user.last_name = "Doe"
        cls.user.email = "johndoe@example.com"
        cls.user.password = "password"

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the object is an instance of User."""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        """Test the User attributes."""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "johndoe@example.com")
        self.assertEqual(self.user.password, "password")

    def test_id(self):
        """Test the type of the id."""
        self.assertEqual(type(self.user.id), str)

    def test_created_at(self):
        """Test the type of created_at."""
        self.assertEqual(type(self.user.created_at), datetime)

    def test_updated_at(self):
        """Test the type of updated_at."""
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_to_dict(self):
        """Test the conversion of object attributes to dictionary for json."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertEqual(user_dict["id"], self.user.id)

    def test_str(self):
        """Test the string representation of the User instance."""
        user_str = str(self.user)
        self.assertEqual(user_str, f"[User] ({self.user.id}) {self.user.__dict__}")

    def test_save(self):
        """Test the save method updates 'updated_at' attribute."""
        old_updated_at = self.user.updated_at
        sleep(0.1)
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_password_encryption(self):
        """Test if the user's password is not stored as plain text."""
        # This is an example, adapt it based on your encryption approach
        user = User(password="password")
        self.assertNotEqual(user.password, "password")
        # Assuming you have a method to verify the password
        self.assertTrue(user.verify_password("password"))

if __name__ == "__main__":
    unittest.main()

