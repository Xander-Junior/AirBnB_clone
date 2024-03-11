#!/usr/bin/python3
"""Entry point of the command interpreter."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")  # Print newline for nice exit
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, line):
    args = line.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    try:
        new_obj = globals()[args[0]]()
        new_obj.save()
        print(new_obj.id)
    except KeyError:
        print("** class doesn't exist **")


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = args[0] + "." + args[1]
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        key = args[0] + "." + args[1]
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
    """Prints all string representation of all instances based or not on the class name."""
    all_objs = storage.all()
    print_list = []
    for obj_id, obj in all_objs.items():
        # This condition checks if arg matches the class name or if arg is empty
        if not arg or arg == obj.__class__.__name__:
            print_list.append(str(obj))
    if not arg or arg in globals():
        print(print_list)
    else:
        print("** class doesn't exist **")

    def do_update(self, arg):
    args = arg.split(" ")
    if len(args) < 2:
        print("** class name missing **" if len(args) == 0 else "** instance id missing **")
        return
    if args[0] not in globals():
        print("** class doesn't exist **")
        return
    all_objs = storage.all()
    key = f"{args[0]}.{args[1]}"
    if key not in all_objs:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return
    # Here I might add more logic to handle different attribute types properly
    setattr(all_objs[key], args[2], args[3].strip('"'))
    all_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
