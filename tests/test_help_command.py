from calculator.commands.help_command import Help

def test_help(capsys):
    command = Help()
    command.execute()
    captured = capsys.readouterr()
    assert "The available commands for this calculator are: add, subtract, multiply, divide, exponent, sqrt, greet, help, goodbye, caffeine, exit" in captured.out
    # Ensure some of the command options are present in the output.
    for cmd in ["add", "subtract", "multiply"]:
        assert cmd in captured.out
