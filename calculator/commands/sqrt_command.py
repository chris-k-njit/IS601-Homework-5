import math
from .command_interface import CommandInterface

class Sqrt(CommandInterface):
    def execute(self, *args):
        if args[0] < 0:
            print("NOTE: You cannot calculate the square root of a negative number.")
            return
        return math.sqrt(args[0])
    