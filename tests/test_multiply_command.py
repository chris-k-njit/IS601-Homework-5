from calculator.commands.multiply_command import Multiply

def test_multiply():
    command = Multiply()
    assert command.execute(20, 30) == 600
    assert command.execute(-1, -9) == 9  # Testing multiplication with negatives, will always result in a positive with a negative x a negative number.
    assert command.execute(50, 0) == 0  # Testing multiplication by zero, always results in ZERO.
