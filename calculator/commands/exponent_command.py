from .command_interface import CommandInterface

class Exponent(CommandInterface):
    def execute(self, *args):
        return args[0] ** args[1]
    