# Factorial using Recursion
def factorial_recursive(n):
    """
    Recursive function to calculate factorial of a number.
    Base Case:
    - If n == 0 or n == 1, return 1.
    Recursive Case:
    - factorial(n) = n * factorial(n-1)
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Factorial using For Loop
def factorial_iterative(n):
    """
    Iterative function to calculate factorial using a for-loop.
    - Initialize result as 1.
    - Multiply result with each number from 1 to n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Input from user
    num = int(input("Enter a number: "))

    # Factorial using Recursion
    print(f"Factorial of {num} using Recursion: {factorial_recursive(num)}")

    # Factorial using For Loop
    print(f"Factorial of {num} using For Loop: {factorial_iterative(num)}")
