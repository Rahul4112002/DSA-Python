from typing import List

def move_zeroes_method1(nums: List[int]) -> None:
    """
    Method 1: Using a Temporary Array
    Time Complexity: O(n)
    Space Complexity: O(n) (Extra space for temp array)
    """
    n = len(nums)
    temp = []

    # Copy non-zero elements to temp array
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])

    # Number of non-zero elements
    nz = len(temp)

    # Copy temp back to nums
    for i in range(nz):
        nums[i] = temp[i]

    # Fill remaining spaces with zeros
    for i in range(nz, n):
        nums[i] = 0

def move_zeroes_method2(nums: List[int]) -> None:
    """
    Method 2: In-place Two Pointers
    Time Complexity: O(n)
    Space Complexity: O(1) (No extra space used)
    """
    if len(nums) == 1:
        return

    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    else:
        return  # If no zero is found, return early

    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]  # Swap non-zero with zero
            i += 1  # Move pointer for next zero
        j += 1  # Move pointer for non-zero search

# Example usage
nums1 = [0, 1, 0, 3, 12]
nums2 = nums1.copy()

move_zeroes_method1(nums1)
print("Method 1 (Using Temp Array):", nums1)  # Output: [1, 3, 12, 0, 0]

move_zeroes_method2(nums2)
print("Method 2 (In-place Swap):", nums2)  # Output: [1, 3, 12, 0, 0]
