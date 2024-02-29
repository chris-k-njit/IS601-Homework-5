'''Calculator Test - No change here from previous branches'''
from calculator import Calculator # add, subtract, multiply, divide

def test_addition(): # Testing addition
    '''Testing addition function'''
    assert Calculator.add(4,4) == 8

def test_subtraction(): # Test subtraction
    '''Testing subtraction function'''
    assert Calculator.subtract(7,1) == 6

def test_multiplication(): # test multiplication
    '''Testing multiplication function'''
    assert Calculator.multiply(1,2) == 2

def test_division(): # test division
    '''Testing division function'''
    assert Calculator.divide(4,2) == 2
    