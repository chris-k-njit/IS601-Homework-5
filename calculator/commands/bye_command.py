from .command_interface import CommandInterface

class Goodbye(CommandInterface):
    def execute(self):
        print("Adios! Thanks for trying out my calculator project.")
