from typing import List

# Brute Force Approach (O(N))
def search_range_brute_force(nums: List[int], target: int) -> List[int]:
    first, last = -1, -1
    for i in range(len(nums)):  
        if nums[i] == target:
            if first == -1:
                first = i  # Set first occurrence
            last = i  # Update last occurrence
    return [first, last]

# Binary Search Approach (O(log N))
def binary_search_left(nums: List[int], target: int) -> int:
    """Finds the first occurrence of target using binary search."""
    low, high = 0, len(nums) - 1
    index = -1  

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            index = mid  # Possible first occurrence
            high = mid - 1  # Continue searching left
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return index

def binary_search_right(nums: List[int], target: int) -> int:
    """Finds the last occurrence of target using binary search."""
    low, high = 0, len(nums) - 1
    index = -1  

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            index = mid  # Possible last occurrence
            low = mid + 1  # Continue searching right
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return index

def search_range_binary(nums: List[int], target: int) -> List[int]:
    """Finds the first and last occurrence of target in a sorted array using Binary Search."""
    first = binary_search_left(nums, target)
    if first == -1:
        return [-1, -1]  # Target not found
    
    last = binary_search_right(nums, target)
    return [first, last]

# Example usage
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8

    print("Brute Force Result:", search_range_brute_force(nums, target))  # Output: [3, 4]
    print("Binary Search Result:", search_range_binary(nums, target))  # Output: [3, 4]
