#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import os
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.city = City()
        cls.city.state_id = "state_id_example"
        cls.city.name = "San Francisco"

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the object is an instance of City."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes(self):
        """Test the City attributes."""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "state_id_example")
        self.assertEqual(self.city.name, "San Francisco")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "state_id_example")
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertEqual(type(city_dict["created_at"]), str)
        self.assertEqual(type(city_dict["updated_at"]), str)

    def test_str(self):
        """Test the string representation of the City instance."""
        city_str = str(self.city)
        self.assertEqual(city_str, f"[City] ({self.city.id}) {self.city.__dict__}")

    def test_save(self):
        """Test the save method and if it updates 'updated_at'."""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

if __name__ == "__main__":
    unittest.main()

