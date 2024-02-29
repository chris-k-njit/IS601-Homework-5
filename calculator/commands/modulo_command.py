from .command_interface import CommandInterface

class Modulo(CommandInterface):
    def execute(self, *args):
        return args[0] % args[1]
    