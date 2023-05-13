#!/usr/bin/python3
"""
Module for a class HBNBCommand
"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command exit the program"""
        return True

    def emptyline(self):
        """shouldn't execute anything"""
        pass

    def do_EOF(self, line):
        """Exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
