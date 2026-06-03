# 📘 Assignment: Unit Testing with pytest

## 🎯 Objective

Learn to write and run unit tests using pytest to verify code behavior, catch bugs early, and build confidence in your code before deployment. You'll create test suites for existing Python modules and practice test-driven development principles.

## 📝 Tasks

### 🛠️ Write Unit Tests for a Calculator Module

#### Description
Create a comprehensive test suite for a provided calculator module using pytest, covering normal cases, edge cases, and error handling.

#### Requirements
Completed program should:

- Write at least 5 test functions using the `test_` naming convention
- Test basic operations: addition, subtraction, multiplication, and division
- Include at least one edge case test (e.g., division by zero)
- Use assertions (`assert`, `==`) to verify expected outputs
- Run tests using `pytest` from the command line and verify they all pass
- Example test: `test_add_positive_numbers()` verifies that `calculate.add(2, 3)` returns `5`

### 🛠️ Test a String Processing Module

#### Description
Create tests for a string processing module that validates inputs and transforms text.

#### Requirements
Completed program should:

- Write at least 4 test functions for string operations (e.g., uppercase conversion, word counting, palindrome checking)
- Test with valid inputs and invalid inputs (empty strings, None values)
- Use pytest assertions to verify function returns and behavior
- Include at least one test that validates an exception is raised for invalid input using `pytest.raises()`
- All tests should pass with 100% success rate

### 🛠️ Organize Tests and Use Fixtures

#### Description
Structure multiple test functions using pytest features like fixtures and parametrization for cleaner, more maintainable tests.

#### Requirements
Completed program should:

- Create at least one pytest fixture that sets up test data
- Use `@pytest.mark.parametrize` to test a function with multiple input/output pairs in a single test
- Organize related tests into a test class (e.g., `TestCalculator`)
- Run all tests and verify they pass
- Include at least 8 parameterized test cases across all test functions
