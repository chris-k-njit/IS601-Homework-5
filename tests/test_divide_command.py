import pytest
from calculator.commands.divide_command import Divide

def test_divide():
    divide_command = Divide()
    assert divide_command.execute(10, 5) == 2
    assert divide_command.execute(50, 2) == 25

def test_divide_by_zero():
    divide_command = Divide()
    with pytest.raises(Exception):
        divide_command.execute(1, 0)
