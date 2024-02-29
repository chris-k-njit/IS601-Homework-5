from .command_interface import CommandInterface

class Divide(CommandInterface):
    def execute(self, *args):
        if args[1] == 0:
            print("Expected Error: You are not able to divide by zero, division by zero is ALWAYS undefined.")
            return
        return args[0] / args[1]