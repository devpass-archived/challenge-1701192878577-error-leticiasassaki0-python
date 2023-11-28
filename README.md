## Error Handling Challenge in Python

### Challenge Description
Implement a function `divide_numbers` in Python that takes two numbers as arguments and returns the result of dividing the first number by the second number. This challenge focuses on handling errors in Python.

### Setup and Execution
- Ensure Python 3.x is installed.
- Run tests using `python -m unittest test_main.py`.
- Implement your solution in `main.py`.

### Task
- Your `divide_numbers` function should:
  - Accept two parameters `numerator` and `denominator`.
  - Handle the following error cases and return an appropriate error message:
    - If the `denominator` is 0, raise a `ZeroDivisionError` with the message 'Division by zero is not allowed.'
    - If any of the input parameters are not numbers, raise a `TypeError` with the message 'Both numerator and denominator must be numbers.'
    - If both numerator and denominator are numbers, calculate the result of dividing the numerator by the denominator and return it.
- Ensure your implementation handles all error cases and returns the correct result.
