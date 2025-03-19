'''
https://docs.google.com/document/d/1N7eNCRduyhoui6hrHRXScWSFPsLUOD1Y56bVLP25BMg/edit?tab=t.0
'''


from typing import List

def longest_consecutive_naive(arr: List[int]) -> int:
    """
    Approach 1: Naive Brute Force
    Time Complexity: O(n^2) - For each element, we check its consecutive sequence.
    Space Complexity: O(1) - No extra data structures used.
    """
    max_count = 0
    n = len(arr)

    for i in range(n):
        num = arr[i]
        count = 1
        while num + 1 in arr:  # Checking for next consecutive element
            count += 1
            num += 1
        max_count = max(max_count, count)

    return max_count


def longest_consecutive_sorted(arr: List[int]) -> int:
    """
    Approach 2: Sorting-based Approach
    Time Complexity: O(n log n) - Due to sorting.
    Space Complexity: O(1) - Sorting happens in place (if allowed).
    """
    if not arr:
        return 0

    arr.sort()
    last_smaller = float("-inf")
    count = 0
    longest = 0

    for num in arr:
        if num - 1 == last_smaller:  # Consecutive number
            count += 1
        elif num != last_smaller:  # Reset count for new sequence
            count = 1
        last_smaller = num
        longest = max(longest, count)

    return longest


def longest_consecutive_hashset(arr: List[int]) -> int:
    """
    Approach 3: HashSet Optimized Approach
    Time Complexity: O(n) - Each number is processed once.
    Space Complexity: O(n) - Stores numbers in a set.
    """
    my_set = set(arr)  # Convert list to a set for O(1) lookups
    longest = 0

    for num in my_set:
        if num - 1 not in my_set:  # Start of a new sequence
            x = num
            count = 1

            while x + 1 in my_set:  # Expand the sequence
                count += 1
                x += 1

            longest = max(longest, count)

    return longest


# Example Usage
nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [2, 5, 6, 3, 1]

print("Naive Approach:", longest_consecutive_naive(nums1[:]))  # Expected: 4
print("Sorting Approach:", longest_consecutive_sorted(nums1[:]))  # Expected: 4
print("HashSet Approach:", longest_consecutive_hashset(nums1[:]))  # Expected: 4

print("Naive Approach:", longest_consecutive_naive(nums2[:]))  # Expected: 3
print("Sorting Approach:", longest_consecutive_sorted(nums2[:]))  # Expected: 3
print("HashSet Approach:", longest_consecutive_hashset(nums2[:]))  # Expected: 3
