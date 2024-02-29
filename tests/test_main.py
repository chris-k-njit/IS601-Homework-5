import pytest
from io import StringIO
from main import main  

def test_main_app_full_flow(monkeypatch, capsys):
    # Simulating CLI inputs for various commands, including arithmetic operations and utilities
    main()

    user_input = StringIO

    inputs = iter([
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
    ])
    
    # Mock input function to return the next simulated CLI input
    def mock_input(prompt):
        return next(inputs, "exit")
    
    # Use monkeypatch to replace input() with mock_input()
    monkeypatch.setattr("builtins.input", mock_input)
    # Capture print statements
    monkeypatch.setattr("sys.stdout", StringIO())
    
    # Run the main function
    # main()
    
    # Capture the application's output
    captured = capsys.readouterr().out
    
    # Assertions to verify each command's output
    assert "Hi there, welcome to Chris Keddell's interactive Python calculator." in captured
    assert "Result: 3" in captured  # Addition result
    assert "Result: 12" in captured  # Multiplication result
    assert "Result: 5.0" in captured  # Division result
    assert "Result: 8" in captured  # Exponentiation result
    assert "Result: 2.0" in captured  # Square root result
    assert "caffeine" in captured  # Caffeine reminder
    assert "Available commands:" in captured  # Help menu
    assert "Goodbye" in captured  # Goodbye message

# Note: You may need to adjust the assertions based on the exact output of your application.
    