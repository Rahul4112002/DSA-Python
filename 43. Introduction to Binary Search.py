from typing import List

# 🔹 Brute Force Approach (O(n) time complexity)
def search_linear(nums: List[int], target: int) -> int:
    """
    Linear Search Approach.
    Time Complexity: O(n) - Scans the entire array in the worst case.
    Space Complexity: O(1) - Uses only a constant amount of extra space.
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i  # Target found, return index
    return -1  # Target not found


# 🔹 Iterative Binary Search (O(log n) time complexity)
def search_binary_iterative(nums: List[int], target: int) -> int:
    """
    Iterative Binary Search Approach.
    Time Complexity: O(log n) - Reduces the search space by half in each step.
    Space Complexity: O(1) - Uses only a few integer variables.
    """
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        if nums[mid] == target:
            return mid  # Target found, return index
        elif nums[mid] < target:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half

    return -1  # Target not found


# 🔹 Recursive Binary Search (O(log n) time complexity)
def search_binary_recursive(nums: List[int], target: int, low: int, high: int) -> int:
    """
    Recursive Binary Search Approach.
    Time Complexity: O(log n) - Recursively divides the search space by half.
    Space Complexity: O(log n) - Due to recursive stack calls.
    """
    if low > high:
        return -1  # Base case: Target not found

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid  # Target found, return index
    elif nums[mid] < target:
        return search_binary_recursive(nums, target, mid + 1, high)  # Search right half
    else:
        return search_binary_recursive(nums, target, low, mid - 1)  # Search left half


# 🔹 Example Usage
if __name__ == "__main__":
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    target2 = 2

    print("Linear Search:", search_linear(nums1, target1))  # Expected Output: 4
    print("Iterative Binary Search:", search_binary_iterative(nums1, target1))  # Expected Output: 4
    print("Recursive Binary Search:", search_binary_recursive(nums1, target1, 0, len(nums1) - 1))  # Expected Output: 4

    print("Linear Search:", search_linear(nums1, target2))  # Expected Output: -1
    print("Iterative Binary Search:", search_binary_iterative(nums1, target2))  # Expected Output: -1
    print("Recursive Binary Search:", search_binary_recursive(nums1, target2, 0, len(nums1) - 1))  # Expected Output: -1
