from typing import List

# Brute Force Approach (O(N))
def search_brute_force(nums: List[int], target: int) -> bool:
    """Finds target using simple iteration (O(N) approach)."""
    for num in nums:
        if num == target:
            return True
    return False  # Target not found

# Optimized Binary Search Approach (O(log N), worst case O(N))
def search_binary(nums: List[int], target: int) -> bool:
    """Finds target using modified binary search (O(log N) in best case, O(N) in worst case)."""
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # If the middle element is the target
        if nums[mid] == target:
            return True
        
        # If duplicates exist at the boundaries, shrink the search space
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue

        # Check if right half is sorted
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
    
    return False  # Target not found

# Example usage
if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0

    print("Brute Force Result:", search_brute_force(nums, target))  # Output: True
    print("Binary Search Result:", search_binary(nums, target))  # Output: True
