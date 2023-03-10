#!/usr/bin/python3
"""contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from shlex import split


class HBNBCommand(cmd.Cmd):

    class_list = dict()
    class_list = {'BaseModel': BaseModel, 'User': User,
                  'City': City,
                  'Amenity': Amenity, 'Place': Place,
                  'State': State, 'Review': Review}

    prompt = "(hbnb) "

    def do_EOF(self, line):
        print()
        return True

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self, line):
        pass

    '''Updating command interpreter to have these commands
    create, show, destroy, all, update
    '''
    def do_create(self, line):
        line = split(line)
        if len(line) > 0:
            line = line[0]
            if line in self.class_list:
                new_instance = eval(line)()
                print(new_instance.id)
                new_instance.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        msg = ["Create a new instance of a class",
               "Usage: (hbnb) create BaseModel"]
        print("\n".join(msg))

    def do_show(self, line):
        texts = split(line)
        if len(texts) == 0:
            print("** class name missing **")
            return
        elif len(texts) >= 1:
            if texts[0] in self.class_list:
                if len(texts) == 1:
                    print("** instance id missing **")
                else:
                    id = ".".join(texts[:2])
                    try:
                        display = storage.all()[id]
                        print(display)
                    except Exception:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_show(self):
        msg = ["Prints string representation of an instance",
               "Usage: (hbnh) show BaseModel 1234-1234-1234"]
        print("\n".join(msg))

    def do_destroy(self, line):
        texts = split(line)
        if len(texts) == 0:
            print("** class name missing **")
            return
        elif len(texts) >= 1:
            if texts[0] in self.class_list:
                if len(texts) == 1:
                    print("** instance id missing **")
                else:
                    id = ".".join(texts[:2])
                    try:
                        del storage.all()[id]
                        storage.save()
                    except Exception:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_destroy(self):
        msg = ["Deletes an instance based on the class name and id",
               "Usage: (hbnb) destroy BaseModel 1234-1234-1234"]
        print("\n".join(msg))

    def do_all(self, line):
        texts = split(line)
        all = storage.all()
        if texts:
            if texts[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                print([str(key) for key in all.values()
                       if texts[0] in str(key)])
        else:
            print([str(key) for key in all.values()])

    def help_all(self):
        msg = ["Prints all string representation of all instances",
               "Usage: (hbnb) all BaseModel",
               "Usage: (hbnb) all"]
        print("n".join(msg))

    def do_update(self, line):
        texts = split(line)
        if len(texts) == 0:
            print("** class name missing **")
        elif len(texts) == 1:
            if texts[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(texts) == 2:
            id = ".".join(texts[:2])
            if id not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(texts) == 3:
            print("** value missing **")
        elif len(texts) >= 4:
            if len(texts) > 4:
                for i in texts:
                    if len(texts) > 4:
                        texts.remove(texts[len(texts) - 1])
            if texts[0] in self.class_list:
                id = ".".join(texts[:2])
                if id in storage.all():
                    obj = storage.all()[id]
                    if texts[2] in type(obj).__dict__:
                        # v_type is type of the attribute
                        # that will be updated
                        v_type = type(obj.__class__.__dict__[texts[2]])
                        print("value type = {}".format(v_type))
                        # above we look into the dictionary
                        # of the object's class with
                        # texts[2] as the key and return the type
                        setattr(obj, texts[2], v_type(texts[3]))
                    else:
                        setattr(obj, texts[2], texts[3])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        storage.save()

    def help_update(self):
        msg = ["Updates an instance based on the class name",
               "Usage: update <class name> <id> <attribute> <value>"]
        print("\n".join(msg))

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
