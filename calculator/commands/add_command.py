# Testing add from the command interface.
from .command_interface import CommandInterface

class Add(CommandInterface):
    def execute(self, *args):
        return sum(args)
    