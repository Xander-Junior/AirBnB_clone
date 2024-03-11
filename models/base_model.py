#!/usr/bin/python3
"""This script defines the BaseModel class, serving as the base for all other classes in the project."""

import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """Initializes the base model with id, created_at, and updated_at attributes."""
        self.id = str(uuid.uuid4())  # Generate a unique ID
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Provides a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance's __dict__."""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict

