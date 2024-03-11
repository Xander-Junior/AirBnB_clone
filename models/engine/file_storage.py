#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if __file_path exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for obj_id, obj_dict in objs.items():
                cls_name = obj_dict['__class__']
                # Dynamically instantiate objects based on their class name
                if cls_name in globals():
                    cls = globals()[cls_name]
                    self.__objects[obj_id] = cls(**obj_dict)
        except FileNotFoundError:
            pass
