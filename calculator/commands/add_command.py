# Testing add from the command interface.
from .command_interface import CommandInterface

class Add(CommandInterface):
    def execute(self, *args):
        result = sum(args)
        print(f"Debug: Adding {args} to get {result}")  # Debug print
        return result