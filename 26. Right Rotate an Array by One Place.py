from typing import List

def right_rotate_slicing(nums: List[int]) -> None:
    """
    Right rotates the array by one place using slicing.
    
    Time Complexity: O(N) - Slicing the array takes O(N) time.
    Space Complexity: O(1) - In-place modification.
    """
    nums[:] = [nums[-1]] + nums[:-1]  # Moves the last element to the front


def right_rotate_loop(nums: List[int]) -> None:
    """
    Right rotates the array by one place using a loop.
    
    Time Complexity: O(N) - Single pass through the array.
    Space Complexity: O(1) - In-place modification.
    """
    temp = nums[-1]  # Store the last element
    for i in range(len(nums) - 2, -1, -1):  # Shift elements right
        nums[i + 1] = nums[i]
    nums[0] = temp  # Place the last element at the front


# Example usage:
nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = nums1[:]  # Copy for second approach

# Using Slicing Approach
right_rotate_slicing(nums1)
print("Slicing Approach:", nums1)

# Using Loop Approach
right_rotate_loop(nums2)
print("Loop Approach:", nums2)
