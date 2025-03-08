def is_palindrome_two_pointer(s: str) -> bool:
    """
    Checks if a string is a palindrome using the two-pointer approach.
    Time Complexity: O(n), Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:  # If characters don't match, it's not a palindrome
            return False
        left += 1  # Move left pointer forward
        right -= 1  # Move right pointer backward
    return True  # If all characters match, it's a palindrome


def is_palindrome_recursive(s: str, left: int, right: int) -> bool:
    """
    Checks if a string is a palindrome using recursion.
    Time Complexity: O(n), Space Complexity: O(n) due to recursion stack.
    """
    if left >= right:  # Base case: If pointers have crossed, it's a palindrome
        return True
    if s[left] != s[right]:  # If characters don't match, it's not a palindrome
        return False
    return is_palindrome_recursive(s, left + 1, right - 1)  # Recursive call


def is_palindrome_slicing(s: str) -> bool:
    """
    Checks if a string is a palindrome using slicing.
    Time Complexity: O(n), Space Complexity: O(n) due to string slicing.
    """
    return s == s[::-1]  # Compare string with its reversed version


# Test Cases
test_strings = ["nitin", "racecar", "hello", "abcdcba", "notapalindrome"]

for s in test_strings:
    print(f"String: {s}")
    print("Two-Pointer:", is_palindrome_two_pointer(s))
    print("Recursive:", is_palindrome_recursive(s, 0, len(s) - 1))
    print("Slicing:", is_palindrome_slicing(s))
    print("-" * 30)
