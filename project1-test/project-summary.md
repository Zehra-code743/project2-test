# Project Summary

This is a test project demonstrating basic Python programming concepts and functions. The project contains two simple Python scripts:

## Overview

The project serves as a learning tool for fundamental Python programming patterns, including:
- Simple output operations
- Function definition and implementation
- Algorithmic thinking with the Fibonacci sequence
- Main execution block patterns

## hello.py

**Purpose**: A basic "Hello World" demonstration script

**Description**: This script prints a simple greeting to the console, commonly used as a first program when learning any programming language.

**Code**:
```python
print("Hello World")
```

**Usage**:
```bash
python hello.py
```

**Output**:
```
Hello World
```

**Learning Points**:
- Basic syntax for print statements
- Python file execution fundamentals

## fibonacci.py

**Purpose**: Demonstrates algorithmic thinking and function implementation

**Description**: This script implements a function that generates Fibonacci numbers up to a specified limit. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, 8, 13, ...).

**Key Features**:
- Function-based implementation for reusability
- Efficient while-loop algorithm
- Clean variable management with tuple unpacking
- Proper main execution guard pattern

**Code**:
```python
# Define a function named fibonacci that takes one parameter, n
# n represents the upper limit — we'll generate all Fibonacci numbers less than n
def fibonacci(n):
    # Initialize an empty list to store the Fibonacci sequence
    result = []

    # Set the first two Fibonacci numbers
    # The Fibonacci sequence starts with 0 and 1
    a, b = 0, 1

    # Loop while the current number (a) is less than the limit (n)
    while a < n:
        # Append the current Fibonacci number to the result list
        result.append(a)

        # Calculate the next Fibonacci number by adding the previous two
        # Simultaneously update a to b, and b to the sum of the old a and b
        # This is Python's tuple unpacking — both assignments happen at once
        a, b = b, a + b

    # Return the complete list of Fibonacci numbers up to (but not including) n
    return result
# This block only runs when the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Call the fibonacci function with 20 as the upper limit
    fib_numbers = fibonacci(20)

    # Print the result to the console
    # Expected output: [0, 1, 1, 2, 3, 5, 8, 13]
    print(f"Fibonacci numbers up to 20: {fib_numbers}")
```

**Usage Examples**:

**Direct Script Execution**:
```bash
python fibonacci.py
```

**Output**:
```
Fibonacci numbers up to 20: [0, 1, 1, 2, 3, 5, 8, 13]
```

**Importing the Function**:
```python
from fibonacci import fibonacci

# Use the fibonacci function directly
fib_sequence = fibonacci(100)
print(fib_sequence)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

**Key Learning Concepts Demonstrated**:
- Function definition and parameter handling
- Return value usage
- While loop control flow
- Tuple unpacking in Python
- `__main__` guard pattern for module protection
- String formatting with f-strings
- Algorithmic problem-solving (O(n) time complexity)

## Project Structure

- `hello.py`: Basic output demonstration
- `fibonacci.py`: Algorithm implementation with function and main block
- `project-summary.md`: This documentation file

## Running the Project

1. Ensure Python is installed on your system
2. Navigate to the project directory
3. Run either script directly:
   - `python hello.py` - Simple greeting
   - `python fibonacci.py` - Fibonacci sequence demonstration

## Educational Value

This project teaches:
- Fundamental Python syntax
- Function implementation and reuse
- Basic algorithmic thinking
- Module import patterns
- Code organization best practices