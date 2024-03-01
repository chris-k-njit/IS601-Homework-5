import math
from .command_interface import CommandInterface

class Sqrt(CommandInterface):
    def execute(self, *args):
        if len(args) != 1:
            raise ValueError("Sqrt command requires exactly one argument.")
        if args[0] < 0:
            raise ValueError("NOTE: You cannot calculate the square root of a negative number.")
        return args[0] ** 0.5
    