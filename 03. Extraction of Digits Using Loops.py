# Extraction of Digits Using Loops

# Input number
n = int(input("Enter a number: "))

# Store original number (Optional, if needed later)
num = n 

# Loop until the number becomes 0
while num > 0:
    # Extract last digit using modulus operator
    last_digit = num % 10
    
    # Print the last digit
    print(last_digit)
    
    # Remove last digit using floor division
    num = num // 10

# Example Input: 5873
# Output: 3 7 8 5
