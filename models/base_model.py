#!/usr/bin/python3
"""This script defines the BaseModel class, serving as the base for all other classes in the project."""

import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Initializes the base model."""
        if kwargs:
            # If kwargs is not empty, set attributes based on its key-value pairs
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    # Convert string to datetime object
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            # Create id and created_at as before if kwargs is empty
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Provides a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        """Saves the instance to the storage."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance's __dict__."""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict

