def fibonacci_recursive(n):
    """
    Recursive approach (Naive)
    Time Complexity: O(2^N) - Exponential, because it makes two recursive calls for each step.
    Space Complexity: O(N) - Due to recursion stack depth.
    """
    if n == 0 or n==1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """
    Iterative approach using a loop
    Time Complexity: O(N) - Linear, as it iterates from 2 to N.
    Space Complexity: O(1) - Constant, as it only uses a few variables.
    """
    if n == 0 or n==1:
        return n
    a, b = 0, 1  # Initial values for Fibonacci sequence
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update the values for the next iteration
    return b

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("\nFibonacci Number using different approaches:")
    print(f"Recursive: {fibonacci_recursive(n)}")   # Exponential time complexity
    print(f"Iterative: {fibonacci_iterative(n)}")   # Linear time complexity
