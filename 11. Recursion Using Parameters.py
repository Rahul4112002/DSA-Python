# Recursion using parameters - DSA Python Course

# Function to print 'x' n times using recursion
def print_x_n_times(x, n):
    """
    Function to print the value 'x' exactly 'n' times using recursion.
    Parameters:
        x (int): The number to print
        n (int): Number of times to print x
    """
    # Base condition: Stop when n reaches 0
    if n == 0:
        return
    print(x)  # Print the value of x
    print_x_n_times(x, n - 1)  # Recursive call with decremented n

# Testing the function
print("Printing 15 three times using recursion:")
print_x_n_times(15, 3)


# Function to print numbers from 1 to n using recursion (Head Recursion)
def print_1_to_n(i, n):
    """
    Function to print numbers from 1 to n using recursion.
    Uses head recursion (prints after recursive calls).
    Parameters:
        i (int): Current number
        n (int): Upper limit
    """
    # Base condition: Stop when i exceeds n
    if i > n:
        return
    print(i)  # Print the current number
    print_1_to_n(i + 1, n)  # Recursive call with incremented i

# Testing the function
print("\nPrinting numbers from 1 to 5 using head recursion:")
print_1_to_n(1, 5)


# Function to print numbers from 1 to n using Tail Recursion (Backtracking)
def print_1_to_n_tail(i, n):
    """
    Function to print numbers from 1 to n using tail recursion.
    Uses backtracking (prints after recursive calls).
    Parameters:
        i (int): Current number
        n (int): Upper limit
    """
    # Base condition: Stop when i exceeds n
    if i > n:
        return
    print_1_to_n_tail(i + 1, n)  # Recursive call first
    print(i)  # Print after the recursive call (backtracking)

# Testing the function
print("\nPrinting numbers from 1 to 5 using tail recursion (backtracking):")
print_1_to_n_tail(1, 5)
