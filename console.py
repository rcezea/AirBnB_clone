
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


class HBNBCommand(cmd.Cmd):

    class_list = dict()
    class_list = {'BaseModel': BaseModel, 'User': User, 'City': City, 
    'Amenity': Amenity, 'Place': Place, 'State': State, 'Review': Review}

    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True
    do_quit = do_EOF

    def help_quit(self):
        print ("Quit command to exit the program")
    help_EOF = help_quit

    '''Updating command interpreter to have these commands
    create, show, destroy, all, update
    '''
    def do_create(self, line):
        line = line.split()
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
        pass

    def do_show(self, line):
        texts = line.split()
        if len(texts) == 0:
            print("** class name missing **")
            return
        elif len(texts) >= 1:
            if texts[0] in self.class_list:
                if texts == 1:
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

    def do_destroy(self, line):
        texts = line.split()
        if len(texts) == 0:
            print("** class name missing **")
            return
        elif len(texts) >= 1:
            if texts[0] in self.class_list:
                if texts == 1:
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
        print("Destroys an instance")

    def do_all(self, line):
        texts = line.split()
        if texts:
            if texts[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                print([(key) for key in storage.all().values()
                       if texts[0] in str(key)])
        else:
            print([str(key) for key in storage.all().values()])

    def do_update(self, line):
        texts = line.split()
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
            print("** value is missing **")
        elif len(texts) >= 4:
            if len(texts) > 4:
               for i in texts:
                  if len(texts) > 4:
                     texts.remove(texts[len(texts) - 1])
            if texts[0] in self.class_list:   
                id = ".".join(texts[:2])
                if id in storage.all():
                    obj = storage.all()[id]
                    '''
                    if texts[2] in type(obj).__dict__:
                        #v_type is type of the attribute that will be updated
                        v_type = type(obj.__class__.__dict__[texts[2]])
                        print("value type = {}".format(v_type))
                        #above we look into the dictionary of the object's class 
                        #with texts[2] as the key and return the type
                        setattr(obj, texts[2], v_type(texts[3]))
                    else:
                    '''
                    setattr(obj, texts[2], texts[3])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        storage.save()
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
