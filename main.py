# from calculator.command_factory import get_command
# from calculator.commands.command_interface import CommandInterface
from calculator.commands.add_command import Add
from calculator.commands.divide_command import Divide
from calculator.commands.multiply_command import Multiply
from calculator.commands.sqrt_command import Sqrt
from calculator.commands.subtract_command import Subtract
from calculator.commands.greet_command import Greet
from calculator.commands.help_command import Help
from calculator.commands.bye_command import Goodbye
from calculator.commands.caffeine_command import Caffeine

def main():
    print("Welcome to Chris' interactive Python calculator. Type 'help' for available calculator commands.")

    commands = {
        "greet": Greet(),
        "add": Add(),
        "subtract": Subtract(),
        "multiply": Multiply(),
        "divide": Divide(),
        "sqrt": Sqrt(),
        "help": Help(),
        "bye": Goodbye(),
        "caffeine": Caffeine(),
    }
    
    while True:
        command_input = input("> ").strip().lower()
        if command_input == "exit":
            print("Exiting calculator program...")
            break
        
        if command_input in commands:
            if command_input in ["add", "subtract", "multiply", "divide", "sqrt"]:
            # Only request additional numbers for arithmetic commands
                numbers_input = input("Enter numbers separated by a space in between them: ").strip()
                numbers = list(map(float, numbers_input.split()))
                if len(numbers) < 2 and command_input in ["divide"]:  # Example for divide, adjust accordingly
                    print(f"The {command_input} command requires two numbers.")
                    continue           
                try:
                    numbers
                except ValueError:
                    print("Invalid numbers. Please try again.")
                    continue  # Skip the rest of the loop and ask for new command
                result = commands[command_input].execute(*numbers)
                print("Result:", result)
            else:
                # Directly execute commands that do not require additional numbers
                commands[command_input].execute()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
