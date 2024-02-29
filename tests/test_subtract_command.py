from calculator.commands.subtract_command import Subtract

def test_subtract():
    subtract_command = Subtract()
    assert subtract_command.execute(13, 2) == 11
    assert subtract_command.execute(-2, -2) == 0
    assert subtract_command.execute(0, 0) == 0
