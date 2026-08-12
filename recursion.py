# Python Recursion Snippets

# Calculate factorial using recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))


# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci:", fibonacci(7))
