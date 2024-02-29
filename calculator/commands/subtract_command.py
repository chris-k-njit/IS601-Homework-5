# test subtract with command pattern.
from .command_interface import CommandInterface

class Subtract(CommandInterface):
    def execute(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    