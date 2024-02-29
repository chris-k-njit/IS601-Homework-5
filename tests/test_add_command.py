import pytest
from calculator.commands.add_command import Add

def test_add():
    add_command = Add()
    assert add_command.execute(4, 2) == 6
    assert add_command.execute(-11, -2) == -13
    assert add_command.execute(100, 0) == 100
