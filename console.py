#!/usr/bin/python3
""" Console Module (the front-end)"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """ Class for the console """

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance"""
        if not line:
            print("** class name missing **")
            return
        elif line not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            found_ = storage.classes()[line]()
            found_.save()
            print(found_.id)

    def do_EOF(self, line):
        """exits console when an EOF is encountered"""
        return True

    def do_quit(self, line):
        """command to exit the program"""
        return True

    def emptyline(self):
        """Prints an empty line"""
        pass

    def default(self, line):
        """The default fallback if a command is not found """
        if not re.search("\.(\w+)\(", line):
            return
        split_line = line.split(".")[0]
        input_cmmnd = line.split(".")[1].split("(")[0]
        argmnt = line.split("(")[1][:-1]

        if not split_line:
            print("** class name missing **")
            return
        elif split_line not in storage.classes():
            print("** class doesn't exist **")
            return

        if input_cmmnd == "all":
            self.do_all(split_line)

        elif input_cmmnd == "count":
            cnt = sum(1 for w, e in storage.all().items()
                      if e.to_dict()["__class__"] == split_line)
            print(cnt)

        elif input_cmmnd == "show":
            self.do_show(split_line + " " + argmnt.strip("\""))

        elif input_cmmnd == "destroy":
            self.do_destroy(split_line + " " + argmnt.strip("\""))

        elif input_cmmnd == "update":
            re_ex = '"[^"]+", {.+}'
            if re.match(re_ex, argmnt):
                argmnt = argmnt.replace("\'", "\"")
                dict = json.loads(argmnt.split(", ", 1)[1])
                n_key = split_line + "." + argmnt.split(", ")[0].strip("\"")
                if n_key not in storage.all().keys():
                    print("** no instance found **")
                    return
                for w, e in dict.items():
                    setattr(storage.all()[n_key], w, e)
            else:
                tokns = argmnt.split(", ")
                if tokns == ['']:
                    print("** instance id missing **")
                    return
                stripped_line = "{}.{}".format(split_line,
                                               tokns[0].strip("\""))
                if stripped_line not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(tokns) < 2:
                    print("** attribute name missing **")
                    return
                if len(tokns) < 3:
                    print("** value missing **")
                    return
                self.do_update(split_line + " " + tokns[0].strip("\"") + " " +
                               tokns[1].strip("\"") + " " + tokns[2])
        else:
            super().default(line)

    def do_update(self, line):
        """Update command"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        tokns = shlex.split(line)
        if tokns[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(tokns) < 2:
            print("** instance id missing **")
            return
        stripped_line = "{}.{}".format(tokns[0], tokns[1])
        if stripped_line not in storage.all():
            print("** no instance found **")
            return

        if len(tokns) < 3:
            print("** attribute name missing **")
            return
        elif len(tokns) < 4:
            print("** value missing **")
            return
        tokns[3] = tokns[3].strip("\"")
        storage.all()[stripped_line].__dict__[tokns[2]] = tokns[3]
        storage.save()

    def do_show(self, line):
        """command that shows an instance"""
        if line == "" or line == None:
            print("** class name missing **")
        else:
            tokns = line.split(' ')
            if tokns[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokns) < 2 or tokns[1] == "":
                print("** instance id missing **")
            else:
                stripped_line = "{}.{}".format(tokns[0], tokns[1])
                if stripped_line not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[stripped_line])

    def do_destroy(self, line):
        """delete instance command"""
        if line == "" or line == None:
            print("** class name missing **")
            return
        else:
            tokns = line.split(' ')
            if tokns[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tokns) < 2 or tokns[1] == "":
                print("** instance id missing **")
            else:
                stripped_line = "{}.{}".format(tokns[0], tokns[1])
                if stripped_line not in storage.all():
                    print("** no instance found **")
                    return
                else:
                    del storage.all()[stripped_line]
                    storage.save()

    def do_all(self, line):
        """command to display all instances of a class"""
        if line != "":
            tokns = line.split(' ')
            if tokns[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for stripped_line,
                            obj in storage.all().items()
                            if type(obj).__name__ == tokns[0]]
                print(obj_list)
        else:
            obj_list = [str(obj) for stripped_line,
                        obj in storage.all().items()]
            print(obj_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
