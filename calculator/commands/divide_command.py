from .command_interface import CommandInterface

class Divide(CommandInterface):
    def execute(self, *args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")
        divisor = args[1]
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return args[0] / args[1]
        