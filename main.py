from calculator.command_factory import get_command

def main():
    print("Welcome to Chris' interactive Python calculator. Type 'help' for available calculator commands.")

    while True:
        command_input = input("> ").strip().lower()
        if command_input == "exit":
            break
        command = get_command(command_input)
        if command:
            command.execute()
        else:
            print("Unknown command here. Type 'help' to see all available calculator commands.")

if __name__ == "__main__":
    main()