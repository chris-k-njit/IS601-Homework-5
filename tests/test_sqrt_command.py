import pytest
from calculator.commands.sqrt_command import Sqrt

def test_sqrt():
    command = Sqrt()
    assert command.execute(4) == 2
    assert command.execute(16) == 4
    assert command.execute(36) == 6
    # with pytest.raises(ValueError):
    #     command.execute(-1)  # Testing with negative input should raise ValueError
