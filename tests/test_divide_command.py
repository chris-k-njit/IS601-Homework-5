import pytest
from calculator.commands.divide_command import Divide

def test_divide():
    divide_command = Divide()
    assert divide_command.execute(10, 5) == 2
    assert divide_command.execute(50, 2) == 25

def test_divide_command_with_insufficient_args():
    divide_command = Divide()
    with pytest.raises(ValueError):
        divide_command.execute(10)

def test_divide_command_with_zero_divisor():
    divide_command = Divide()
    with pytest.raises(ZeroDivisionError):
        divide_command.execute(10, 0)
        