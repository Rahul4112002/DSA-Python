from typing import List

# BRUTE FORCE SOLUTION: O(n^2) Time | O(1) Space
def missingNumberBruteForce(nums: List[int]) -> int:
    """
    Brute force approach: Check every number from 0 to n and see if it exists in the list.

    Time Complexity: O(n^2) - Since "i not in nums" runs in O(n) inside a loop of O(n).
    Space Complexity: O(1) - No extra space used except variables.
    """
    for i in range(0, len(nums) + 1):
        if i not in nums:
            return i

# BETTER SOLUTION: O(n) Time | O(n) Space
def missingNumberBetter(nums: List[int]) -> int:
    """
    Using a frequency map (dictionary) to track missing number.

    Time Complexity: O(n) - First pass to populate the dictionary, second pass to find missing number.
    Space Complexity: O(n) - Extra dictionary storing n+1 elements.
    """
    freq = {i: 0 for i in range(0, len(nums) + 1)}  # Initialize all numbers from 0 to n with 0 count
    for i in nums:
        freq[i] += 1  # Mark present numbers

    for k, v in freq.items():  # Find the missing number
        if v == 0:
            return k

# OPTIMAL SOLUTION: O(n) Time | O(1) Space
def missingNumberOptimal(nums: List[int]) -> int:
    """
    Using sum formula to find missing number.

    Time Complexity: O(n) - We compute sum(nums) which takes O(n) time.
    Space Complexity: O(1) - Only a few variables are used.
    """
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2  # Sum of first n natural numbers
    return expected_sum - sum(nums)  # Missing number is the difference

# Example Test Cases
nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print("Brute Force Output:", missingNumberBruteForce(nums1))  # Output: 2
print("Better Solution Output:", missingNumberBetter(nums1))  # Output: 2
print("Optimal Solution Output:", missingNumberOptimal(nums1))  # Output: 2

print("Brute Force Output:", missingNumberBruteForce(nums2))  # Output: 2
print("Better Solution Output:", missingNumberBetter(nums2))  # Output: 2
print("Optimal Solution Output:", missingNumberOptimal(nums2))  # Output: 2

print("Brute Force Output:", missingNumberBruteForce(nums3))  # Output: 8
print("Better Solution Output:", missingNumberBetter(nums3))  # Output: 8
print("Optimal Solution Output:", missingNumberOptimal(nums3))  # Output: 8
