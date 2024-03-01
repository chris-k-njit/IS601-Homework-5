from calculator.commands.caffeine_command import Caffeine

def test_caffeine(capsys):
    command = Caffeine()
    command.execute()
    captured = capsys.readouterr()
    assert "You're a programmer, you need some caffeine to fuel your code." in captured.out
