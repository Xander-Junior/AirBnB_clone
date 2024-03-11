#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import os
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.review = Review()
        cls.review.place_id = "place_id_example"
        cls.review.user_id = "user_id_example"
        cls.review.text = "Great place!"

    @classmethod
    def tearDownClass(cls):
        """Tear down for the tests."""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the object is an instance of Review."""
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attributes(self):
        """Test the Review attributes."""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "place_id_example")
        self.assertEqual(self.review.user_id, "user_id_example")
        self.assertEqual(self.review.text, "Great place!")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["text"], "Great place!")
        self.assertEqual(type(review_dict["created_at"]), str)
        self.assertEqual(type(review_dict["updated_at"]), str)

    def test_str(self):
        """Test the string representation of the Review instance."""
        review_str = str(self.review)
        self.assertEqual(review_str, f"[Review] ({self.review.id}) {self.review.__dict__}")

    def test_save(self):
        """Test the save method and if it updates 'updated_at'."""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

if __name__ == "__main__":
    unittest.main()

