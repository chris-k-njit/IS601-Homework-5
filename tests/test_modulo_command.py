from calculator.commands.modulo_command import Modulo

def test_modulo():
    command = Modulo()
    assert command.execute(10, 3) == 1
    assert command.execute(10, 2) == 0  # Testing even division in modulo, which will return us a ZERO.
    assert command.execute(-10, 3) == -1  # Testing with negative numbers, which would provide a negative number.
