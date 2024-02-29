from calculator.command_factory import get_command

def main():
    print("Welcome to the interactive calculator. Type 'help' for available commands.")

    while True:
        command_input = input("> ").strip().lower()
        if command_input == "exit":
            break
        command = get_command(command_input)
        if command:
            command.execute()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()