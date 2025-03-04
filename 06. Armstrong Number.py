def is_armstrong(n):
    """
    Function to check if a number is an Armstrong number.
    An Armstrong number (also known as a narcissistic number) is a number that is equal
    to the sum of its own digits each raised to the power of the number of digits.
    
    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """
    original_num = n  # Store the original number
    num_digits = len(str(n))  # Count the number of digits in n
    total = 0  # Initialize sum
    
    while n > 0:
        last_digit = n % 10  # Extract last digit
        total += last_digit ** num_digits  # Raise it to the power of num_digits and add to total
        n //= 10  # Remove last digit from n
    
    return total == original_num  # Check if sum equals original number

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")