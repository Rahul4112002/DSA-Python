# ==============================================
# Recursion in Python - Definition and Examples
# ==============================================

# -------------------------------
# Definition of Recursion
# -------------------------------
# Recursion is a process where a function calls itself to solve a problem.
# It breaks the problem into smaller subproblems and solves them recursively.
# A recursive function must have a base condition to prevent infinite recursion.

# --------------------------------
# Example 1: Infinite Recursion
# --------------------------------
# This function will cause an infinite loop because there is no base case.
# Uncomment the function call to test it (Warning: It will crash your program!)

def infinite_recursion():
    print("Aniruddh")
    infinite_recursion()  # Function calls itself with no stop condition

# infinite_recursion()  # Uncomment to run (Will cause stack overflow)


# -----------------------------------
# Example 2: Recursion with Base Case
# -----------------------------------
# This function prints "Aniruddh" exactly 4 times using recursion.

def recursion_with_base(count):
    if count == 4:  # Base case to stop recursion
        return
    print("Aniruddh")
    recursion_with_base(count + 1)  # Recursive call with incremented count

# Call the function with an initial count of 0
recursion_with_base(0)


# -------------------------------
# Head Recursion
# -------------------------------
# In head recursion, the function makes the recursive call first,
# and executes the logic while returning.

def head_recursion(count):
    if count == 4:
        return
    head_recursion(count + 1)  # Recursive call first
    print("Head Recursion:", count)  # Execution happens after returning

# Call the function
head_recursion(0)


# -------------------------------
# Tail Recursion
# -------------------------------
# In tail recursion, the function executes logic first,
# and then makes the recursive call.

def tail_recursion(count):
    if count == 4:
        return
    print("Tail Recursion:", count)  # Execution happens before recursion
    tail_recursion(count + 1)

# Call the function
tail_recursion(0)


# -------------------------------------
# Example 3: Factorial using Recursion
# -------------------------------------
# This function calculates the factorial of a number using recursion.
# Factorial(n) = n * Factorial(n-1), with Factorial(0) = 1.

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

# Call the function and print the result
num = 5
print(f"Factorial of {num} is:", factorial(num))


# -------------------------------------
# Example 4: Fibonacci using Recursion
# -------------------------------------
# This function calculates Fibonacci numbers using recursion.
# Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
# Base cases: Fibonacci(0) = 0, Fibonacci(1) = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Call the function and print the first 7 Fibonacci numbers
print("Fibonacci Series:")
for i in range(7):
    print(f"Fibonacci({i}) =", fibonacci(i))
