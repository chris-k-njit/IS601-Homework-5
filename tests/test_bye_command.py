from calculator.commands.bye_command import Goodbye

def test_goodbye(capsys):
    command = Goodbye()
    command.execute()
    captured = capsys.readouterr()
    assert "Adios! Thanks for trying out my calculator project." in captured.out
