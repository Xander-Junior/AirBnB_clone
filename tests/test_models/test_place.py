#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import os
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.place = Place()
        cls.place.city_id = "city_id_ex"
        cls.place.user_id = "user_id_ex"
        cls.place.name = "A lovely cottage"
        cls.place.description = "A cozy, traditional cottage with modern amenities."
        cls.place.number_rooms = 3
        cls.place.number_bathrooms = 2
        cls.place.max_guest = 4
        cls.place.price_by_night = 150
        cls.place.latitude = 40.7128
        cls.place.longitude = -74.0060
        cls.place.amenity_ids = ["amenity_id_1", "amenity_id_2"]

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the object is an instance of Place."""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attributes(self):
        """Test the Place attributes."""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.city_id, "city_id_ex")
        self.assertEqual(self.place.user_id, "user_id_ex")
        self.assertEqual(self.place.name, "A lovely cottage")
        self.assertEqual(self.place.description, "A cozy, traditional cottage with modern amenities.")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["amenity_id_1", "amenity_id_2"])

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["city_id"], "city_id_ex")
        self.assertEqual(place_dict["user_id"], "user_id_ex")
        self.assertEqual(place_dict["name"], "A lovely cottage")
        self.assertEqual(place_dict["description"], "A cozy, traditional cottage with modern amenities.")
        self.assertEqual(place_dict["number_rooms"], 3)
        self.assertEqual(place_dict["number_bathrooms"], 2)
        self.assertEqual(place_dict["max_guest"], 4)
        self.assertEqual(place_dict["price_by_night"], 150)
        self.assertEqual(place_dict["latitude"], 40.7128)
        self.assertEqual(place_dict["longitude"], -74.0060)
        self.assertEqual(place_dict["amenity_ids"], ["amenity_id_1", "amenity_id_2"])

    def test_str(self):
        """Test the string representation of the Place instance."""
        place_str = str(self.place)
        self.assertEqual(place_str, f"[Place] ({self.place.id}) {self.place.__dict__}")

    def test_save(self):
        """Test the save method and if it updates 'updated_at'."""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

if __name__ == "__main__":
    unittest.main()
