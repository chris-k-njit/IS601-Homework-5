from io import StringIO
from unittest.mock import patch

import pytest
from main import main  

def test_main_app_flow(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
# def test_main_app_full_flow(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
#     # Simulating CLI inputs for various commands, including arithmetic operations and utilities
#     main()

    user_inputs = [
        "greet",  # Should print a greeting message
        "add", "1 2",  # Addition operation
        "multiply", "3 4",  # Multiplication operation
        "divide", "10 2",  # Division operation
        "exponent", "2 3",  # Exponentiation operation
        "sqrt", "4",  # Square root operation
        "caffeine",  # Should print a caffeine reminder
        "help",  # Should display a help menu
        "bye",  # Should print a goodbye message
        "exit"  # Exit the application
    ]
    
    # Mock input function to return the next simulated CLI input
    # def mock_input(prompt):
    #     return next(inputs, "exit")
    
    input_generator = (input for input in user_inputs)
    # Mock input to return the next value from the input_generator each time it's called.
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))

    with patch('builtins.print') as mock_print:
        main()  # Adjust depending on how you import or structure your main function.
        mock_print.assert_called()
    # Capture the application's output
    captured = capsys.readouterr().out
    
    # Assertions to verify each command's output
    assert "Hi there, welcome to Chris Keddell's interactive Python calculator." in captured.out
    assert "Result: 3" in captured.out  # Addition result
    assert "Result: 12" in captured.out  # Multiplication result
    assert "Result: 5.0" in captured.out # Division result
    assert "Result: 8" in  captured.out # Exponentiation result
    assert "Result: 2.0" in captured.out # Square root result
    assert "caffeine" in  captured.out # Caffeine reminder
    assert "Available commands:" in captured.out  # Help menu
    assert "Goodbye" in captured.out # Goodbye message

# Note: You may need to adjust the assertions based on the exact output of your application.
    