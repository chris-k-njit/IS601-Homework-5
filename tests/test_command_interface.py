import pytest
from calculator.commands.command_interface import CommandInterface

def test_command_interface_execute():
    command = CommandInterface()
    with pytest.raises(NotImplementedError):
        command.execute()
        