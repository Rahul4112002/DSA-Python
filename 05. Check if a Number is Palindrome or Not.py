def is_palindrome(n):
    """
    Function to check if a number is a palindrome without converting it to a string.
    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """
    original_num = n  # Store the original number
    reversed_num = 0   # Variable to store the reversed number

    while n > 0:
        last_digit = n % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + last_digit  # Build the reversed number
        n //= 10  # Remove the last digit from the original number

    return original_num == reversed_num  # Check if the number is the same as its reverse

# Example usage:
if __name__ == "__main__":
    num = 12321  # Example number
    print("Is palindrome:", is_palindrome(num))  # Output: True
