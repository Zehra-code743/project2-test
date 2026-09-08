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
