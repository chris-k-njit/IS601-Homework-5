# Help to provide info to a user.
from .command_interface import CommandInterface

class Help(CommandInterface):
    def execute(self):
        print("The available commands for this calculator are: add, subtract, multiply, divide, exponent, sqrt, greet, help, goodbye, caffeine, exit")
        