#!/usr/bin/python3
"""Unit tests for BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Defines test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test instantiation of BaseModel instances."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_id_uniqueness(self):
        """Test that each BaseModel instance has a unique id."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_datetime_attributes(self):
        """Test that created_at and updated_at are datetime objects."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method returns the expected string."""
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(expected_str, str(my_model))

    def test_save_method(self):
        """Test the save method updates 'updated_at' attribute."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method returns a dictionary with correct keys and values."""
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], my_model.id)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertEqual(model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], my_model.updated_at.isoformat())
        
    def test_create_instance_with_kwargs(self):
        """Test instantiation of BaseModel instances with kwargs."""
        time_now = datetime.now().isoformat()
        kwargs = {
            'id': '123',
            'created_at': time_now,
            'updated_at': time_now,
            'name': 'Kwarg Model'
        }
        my_model = BaseModel(**kwargs)
        self.assertEqual(my_model.id, '123')
        self.assertEqual(my_model.name, 'Kwarg Model')
        # Ensure that created_at and updated_at are converted from string to datetime objects
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        # Ensure the datetime objects match the time_now within the allowed margin of error
        self.assertAlmostEqual(my_model.created_at, datetime.fromisoformat(time_now), delta=datetime.timedelta(seconds=1))
        self.assertAlmostEqual(my_model.updated_at, datetime.fromisoformat(time_now), delta=datetime.timedelta(seconds=1))

    def test_kwargs_none_for_class_attribute(self):
        """Test __class__ key in kwargs does not set an attribute."""
        kwargs = {
            '__class__': 'BaseModel',
            'id': '321',
            'name': 'No class attribute'
        }
        my_model = BaseModel(**kwargs)
        self.assertFalse(hasattr(my_model, '__class__'), "my_model should not have '__class__' as an attribute")


if __name__ == "__main__":
    unittest.main()

