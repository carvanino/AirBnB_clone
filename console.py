#!/usr/bin/python3
""" Entry point for the command line interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the command line interpreter class
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when only a newline character is passed """
        pass

    def do_quit(self, args):
        """ Exit the program """
        return True

    def do_EOF(self, args):
        """ End of file character and quits the program """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
