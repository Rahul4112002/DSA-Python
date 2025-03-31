from typing import List

# Brute Force Approach (O(N))
def find_min_brute_force(nums: List[int]) -> int:
    """Finds the minimum element using simple iteration (O(N) approach)."""
    return min(nums)  # Directly return the smallest element

# Optimized Binary Search Approach (O(log N))
def find_min_binary(nums: List[int]) -> int:
    """Finds the minimum element using modified binary search (O(log N) approach)."""
    n = len(nums)
    low, high = 0, n - 1
    mini = float('inf')

    while low <= high:
        mid = (low + high) // 2

        # If right half is sorted, minimum is either at mid or left side
        if nums[mid] <= nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1  # Search left
        else:  # Left half is sorted
            mini = min(mini, nums[mid])
            low = mid + 1  # Search right

    return mini

# Example usage
if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]

    print("Brute Force Result:", find_min_brute_force(nums))  # Output: 1
    print("Binary Search Result:", find_min_binary(nums))  # Output: 1
