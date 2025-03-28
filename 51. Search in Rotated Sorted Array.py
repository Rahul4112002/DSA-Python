from typing import List

# Brute Force Approach (O(N))
def search_brute_force(nums: List[int], target: int) -> int:
    """Finds target index using simple iteration (O(N) approach)."""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1  # Target not found

# Optimized Binary Search Approach (O(log N))
def search_binary(nums: List[int], target: int) -> int:
    """Finds target index using binary search (O(log N) approach)."""
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        
        # If the middle element is the target
        if nums[mid] == target:
            return mid
        
        # Check if the right half is sorted
        if nums[mid] <= nums[high]:  
            if nums[mid] <= target <= nums[high]:  # Target in right half
                low = mid + 1
            else:
                high = mid - 1
        else:  # Left half is sorted
            if nums[low] <= target <= nums[mid]:  # Target in left half
                high = mid - 1
            else:
                low = mid + 1
    
    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    print("Brute Force Result:", search_brute_force(nums, target))  # Output: 4
    print("Binary Search Result:", search_binary(nums, target))  # Output: 4
