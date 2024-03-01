from .command_interface import CommandInterface

class Greet(CommandInterface):
    def execute(self):
        print("Hi there, welcome to Chris Keddell's interactive Python calculator.")
        