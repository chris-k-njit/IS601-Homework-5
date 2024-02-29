from calculator.commands.greet_command import Greet

def test_greet(capsys):
    greet_command = Greet()
    greet_command.execute()
    captured = capsys.readouterr()
    assert "Hi there, welcome to Chris Keddell's interactive Python calculator." in captured.out
