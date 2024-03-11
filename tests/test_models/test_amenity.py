#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.amenity = Amenity()
        cls.amenity.name = "Wi-Fi"

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the object is an instance of Amenity."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attributes(self):
        """Test the Amenity attributes."""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "Wi-Fi")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["name"], "Wi-Fi")
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)

    def test_str(self):
        """Test the string representation of the Amenity instance."""
        amenity_str = str(self.amenity)
        self.assertEqual(amenity_str, f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}")

    def test_save(self):
        """Test the save method and if it updates 'updated_at'."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

if __name__ == "__main__":
    unittest.main()

