from .command_interface import CommandInterface

class Modulo(CommandInterface):
    def execute(self, *args):
        if args[1] == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return args[0] % args[1]
    