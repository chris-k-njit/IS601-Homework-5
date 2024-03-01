import pytest
from calculator.commands.sqrt_command import Sqrt

def test_sqrt():
    command = Sqrt()
    assert command.execute(4) == 2
    assert command.execute(16) == 4
    assert command.execute(36) == 6

def test_sqrt_with_zero():
    command = Sqrt()
    assert command.execute(0) == 0, "Square root of 0 should be 0."

def test_sqrt_with_negative_number():
    command = Sqrt()
    with pytest.raises(ValueError):
        command.execute(-1)
        