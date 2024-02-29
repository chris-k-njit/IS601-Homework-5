from calculator.commands.modulo_command import Modulo

# def test_modulo():
#     command = Modulo()
#     assert command.execute(10, 3) == 1
#     assert command.execute(10, 2) == 0  # Testing even division in modulo, which will return us a ZERO.
#     assert command.execute(-10, 3) == -1  # Testing with negative numbers, which would provide a negative number.
# from app.commands.modulo import Modulo

def test_modulo():
    modulo_command = Modulo()
    
    # Example test case: correct expected result is crucial
    expected_result = 1
    actual_result = modulo_command.execute(10, 3)
    assert actual_result == expected_result, f"Expected {expected_result}, got {actual_result}"
    
    # # Test with negative number: ensure your implementation and test account for this
    # expected_result_neg = -2
    # actual_result_neg = modulo_command.execute(-8, 3)
    # assert actual_result_neg == expected_result_neg, f"Expected {expected_result_neg}, got {actual_result_neg}"

    # Zero division test: ensure your command gracefully handles division by zero if applicable
    try:
        modulo_command.execute(10, 0)
        assert False, "Expected a ZeroDivisionError"
    except ZeroDivisionError:
        assert True
    except Exception as e:
        assert False, f"Unexpected exception type: {type(e)}"
