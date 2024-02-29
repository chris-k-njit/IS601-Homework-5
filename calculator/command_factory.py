# factory to contain all commands needed for this part of the homework.
from .commands.command_interface import CommandInterface
from .commands.add import Add
from .commands.subtract import Subtract
from .commands.multiply import Multiply
from .commands.divide import Divide
from .commands.exponent import Exponent
from .commands.sqrt import Sqrt
from .commands.modulo import Modulo
from .commands.greet import Greet
from .commands.help import Help
from .commands.goodbye import Goodbye
from .commands.caffeine import Caffeine

def get_command(command_name):
    commands = {
        "add": Add(),
        "subtract": Subtract(),
        "multiply": Multiply(),
        "divide": Divide(),
        "exponent": Exponent(),
        "sqrt": Sqrt(),
        "modulo": Modulo(),
        "greet": Greet(),
        "help": Help(),
        "goodbye": Goodbye(),
        "caffeine": Caffeine(),
    }
    return commands.get(command_name, None)
