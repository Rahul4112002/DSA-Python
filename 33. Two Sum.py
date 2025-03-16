from typing import List

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute Force Approach:
    - Uses two nested loops to check all pairs.

    Time Complexity: O(n^2)
    - Checks every pair in the array, leading to quadratic time complexity.

    Space Complexity: O(1)
    - Uses only a constant amount of extra space.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]  # Return indices of the two numbers
    return []  # Return an empty list if no solution is found (though problem guarantees one solution)


def two_sum_optimal(nums: List[int], target: int) -> List[int]:
    """
    Optimal Hash Map Approach:
    - Uses a dictionary to store elements and their indices for quick lookup.

    Time Complexity: O(n)
    - Single pass through the array with O(1) lookups in the hash map.

    Space Complexity: O(n)
    - Stores up to n elements in the hash map in the worst case.
    """
    hash_map = {}  # Dictionary to store seen numbers and their indices
    for i, num in enumerate(nums):
        remaining = target - num  # Calculate the required complement
        if remaining in hash_map:  # Check if the complement exists
            return [hash_map[remaining], i]  # Return indices of complement and current number
        hash_map[num] = i  # Store the current number and its index
    return []  # Return an empty list if no solution is found (though problem guarantees one solution)


# Example test cases
print("Brute Force Approach:")
print(two_sum_brute_force([2, 7, 11, 15], 9))  # Output: [0,1]
print(two_sum_brute_force([3, 2, 4], 6))  # Output: [1,2]
print(two_sum_brute_force([3, 3], 6))  # Output: [0,1]

print("\nOptimal Hash Map Approach:")
print(two_sum_optimal([2, 7, 11, 15], 9))  # Output: [0,1]
print(two_sum_optimal([3, 2, 4], 6))  # Output: [1,2]
print(two_sum_optimal([3, 3], 6))  # Output: [0,1]
