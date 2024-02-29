# tests/test_exponent.py
from calculator.commands.exponent_command import Exponent

def test_exponent():
    command = Exponent()
    assert command.execute(2, 3) == 8
    assert command.execute(5, 0) == 1  # As known in mathematics, any number to the power of 0 is 1.
    assert command.execute(2, -1) == 0.5  # Testing with a negative exponent.
