import pytest
from app import add, multiply, divide, is_palindrome, calculate_average

def test_add():
    """Test de l'addition"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    """Test de la multiplication"""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 10) == 0

def test_divide():
    """Test de la division"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    # Test de l'exception pour division par zéro
    with pytest.raises(ValueError):
        divide(10, 0)

def test_is_palindrome():
    """Test du palindrome"""
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man a plan a canal Panama') == True
    assert is_palindrome('racecar') == True

def test_calculate_average():
    """Test du calcul de moyenne"""
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([5, 5, 5, 5]) == 5
    # Test de l'exception pour liste vide
    with pytest.raises(ValueError):
        calculate_average([])
