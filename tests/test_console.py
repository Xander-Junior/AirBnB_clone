#!/usr/bin/python3
"""Module for testing the console."""
import unittest
from unittest.mock import patch
from io import StringIO
import console
from models import storage
from models.base_model import BaseModel
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Tests for the console."""

    def setUp(self):
        """Set up for the tests."""
        self.cli = HBNBCommand()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("quit")
            self.assertEqual('', f.getvalue().strip())

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("EOF")
            self.assertEqual('', f.getvalue().strip())

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)
    
    def test_show_missing_class(self):
        """Test show command with missing class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_show_nonexistent_class(self):
        """Test show command with a non-existent class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show NonExistentClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_missing_id(self):
        """Test show command with a valid class but missing ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

