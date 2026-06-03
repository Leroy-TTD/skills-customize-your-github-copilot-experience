# Module to be tested

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# String processing functions

def to_uppercase(text):
    """Convert text to uppercase."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()

def count_words(text):
    """Count the number of words in text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())

def is_palindrome(text):
    """Check if text is a palindrome (ignoring spaces and case)."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# Task 1: Write test functions for the calculator module
# Create functions: test_add_positive_numbers, test_subtract, test_multiply, test_divide, test_divide_by_zero
# Use assert statements to verify outputs

def test_add_positive_numbers():
    # Test that adding two positive numbers works
    pass

def test_subtract():
    # Test subtraction
    pass

def test_multiply():
    # Test multiplication
    pass

def test_divide():
    # Test division
    pass

def test_divide_by_zero():
    # Test that division by zero raises ValueError
    pass


# Task 2: Write tests for string processing
# Create functions: test_to_uppercase, test_to_uppercase_invalid, test_count_words, test_is_palindrome
# Use pytest.raises() for exception testing

def test_to_uppercase():
    # Test uppercase conversion
    pass

def test_to_uppercase_invalid():
    # Test that non-string input raises TypeError
    pass

def test_count_words():
    # Test word counting
    pass

def test_is_palindrome():
    # Test palindrome detection
    pass


# Task 3: Organize tests with fixtures and parametrization
# Create a fixture for test data
# Use @pytest.mark.parametrize to test multiple cases
# Organize tests into a test class

import pytest

@pytest.fixture
def sample_data():
    # Create and return test data
    pass

class TestCalculator:
    # Add parameterized tests for calculator functions
    pass

class TestStringProcessing:
    # Add parameterized tests for string functions
    pass
