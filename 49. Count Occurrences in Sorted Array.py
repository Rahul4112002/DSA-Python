from typing import List

# Brute Force Approach (O(N))
def count_occurrences_brute_force(arr: List[int], target: int) -> int:
    """Counts occurrences of target using simple iteration (O(N) approach)."""
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

# Binary Search Approach (O(log N))
def lower_bound(arr: List[int], target: int) -> int:
    """Finds the first occurrence (lower bound) of target using binary search."""
    low, high = 0, len(arr) - 1
    lb = -1  

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            lb = mid  # Possible lower bound
            high = mid - 1  # Continue searching left
        else:
            low = mid + 1

    return lb

def upper_bound(arr: List[int], target: int) -> int:
    """Finds the index just after the last occurrence (upper bound) of target using binary search."""
    low, high = 0, len(arr) - 1
    ub = len(arr)  

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ub = mid  # Possible upper bound
            high = mid - 1  # Continue searching left
        else:
            low = mid + 1

    return ub

def count_occurrences_binary(arr: List[int], target: int) -> int:
    """Counts occurrences of target using binary search (O(log N) approach)."""
    lb = lower_bound(arr, target)
    if lb == -1 or lb >= len(arr) or arr[lb] != target:
        return 0  # Target is not present

    ub = upper_bound(arr, target)
    return ub - lb  # Count of occurrences

# Example usage
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2

    print("Brute Force Result:", count_occurrences_brute_force(arr, target))  # Output: 4
    print("Binary Search Result:", count_occurrences_binary(arr, target))  # Output: 4
