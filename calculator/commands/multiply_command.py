from .command_interface import CommandInterface

class Multiply(CommandInterface):
    def execute(self, *args):
        result = 1
        for num in args:
            result *= num
        return result
    