#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a User for the AirBnB clone."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

