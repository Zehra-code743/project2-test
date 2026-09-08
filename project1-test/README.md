# Test Project: Python Fundamentals

This is a test project demonstrating basic Python programming concepts. It contains two simple Python scripts that showcase fundamental programming patterns.

## Project Contents

### `hello.py`
A basic "Hello World" script that prints a greeting to the console.

**Usage:**
```bash
python hello.py
```

**Output:**
```
Hello World
```

### `fibonacci.py`
A script that implements a function to generate Fibonacci numbers up to a specified limit.

**Function:** `fibonacci(n)` - Returns a list of Fibonacci numbers less than `n`

**Usage:**
```bash
python fibonacci.py
```

**Output:**
```
Fibonacci numbers up to 20: [0, 1, 1, 2, 3, 5, 8, 13]
```

**Importing the function:**
```python
from fibonacci import fibonacci
fib_sequence = fibonacci(100)
```

## How to Run

1. Ensure Python is installed on your system (Python 3.x recommended)
2. Navigate to the project directory
3. Run either script:

```bash
# Run hello.py
python hello.py

# Run fibonacci.py
python fibonacci.py
```

## Learning Objectives

This project demonstrates:
- Basic Python syntax and print statements
- Function definition and implementation
- While-loop algorithms
- Tuple unpacking in Python
- The `__main__` guard pattern for module protection
- String formatting with f-strings
- Simple algorithmic problem-solving