from calculator.command_factory import get_command
from calculator.commands.command_interface import CommandInterface
from calculator.commands.add_command import Add
from calculator.commands.divide_command import Divide
from calculator.commands.multiply_command import Multiply
from calculator.commands.sqrt_command import Sqrt
from calculator.commands.subtract_command import Subtract
from calculator.commands.exponent_command import Exponent
from calculator.commands.greet_command import Greet
from calculator.commands.help_command import Help
from calculator.commands.bye_command import Goodbye
from calculator.commands.caffeine_command import Caffeine

def main():
    print("Welcome to Chris' interactive Python calculator. Type 'help' for available calculator commands.")

    commands = {
        "add": Add(),
        "subtract": Subtract(),
        "multiply": Multiply(),
        "divide": Divide(),
        "exponent": Exponent(),
        "sqrt": Sqrt(),
        "greet": Greet(),
        "help": Help(),
        "goodbye": Goodbye(),
        "caffeine": Caffeine(),
    }
    
    while True:
        command_input = input("> ").strip().lower()
        if command_input == "exit":
            print("Exiting calculator program...")
            break
        
        if command_input in ["add", "subtract", "multiply", "divide", "exponent", "sqrt"]:
            numbers_input = input("Enter numbers separated by a space in between them: ").strip()
            numbers = list(map(float, numbers_input.split()))
            command = get_command(command_input)  # Using a factory or direct instantiation
            if command and isinstance(command, CommandInterface):
                result = command.execute(*numbers)
                print("Result:", result)
            else:
                print("Unknown command.")
        elif command_input in commands:
            commands[command_input].execute()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()