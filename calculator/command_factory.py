# factory to contain all commands needed for this part of the homework.
from .commands.command_interface import CommandInterface
from .commands.add_command import Add
from .commands.subtract_command import Subtract
from .commands.multiply_command import Multiply
from .commands.divide_command import Divide
from .commands.exponent_command import Exponent
from .commands.sqrt_command import Sqrt
from .commands.modulo_command import Modulo
from .commands.greet_command import Greet
from .commands.help_command import Help
from .commands.bye_command import Goodbye
from .commands.caffeine_command import Caffeine

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
