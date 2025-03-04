# Method 1: Using a While Loop
def count_digits(n):
    """
    This function counts the number of digits in an integer using a while loop.
    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """
    num = n  # Store original number
    count = 0  # Initialize count

    while num > 0:
        count += 1  # Increment count
        num //= 10  # Remove the last digit

    return count

# Example usage:
if __name__ == "__main__":
    n = 511117
    print("Number of digits (While Loop):", count_digits(n))  # Output: 6


# Method 2: Using Logarithm
import math

def count_digits_log(n):
    """
    This function counts the number of digits in an integer using logarithm.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if n == 0:
        return 1  # log10(0) is undefined, handle separately
    return int(math.log10(n)) + 1

# Example usage:
if __name__ == "__main__":
    print("Number of digits (Logarithm):", count_digits_log(n))  # Output: 6
