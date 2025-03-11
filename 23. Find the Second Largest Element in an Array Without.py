def second_largest_brute_force(arr):
    """
    Brute Force Approach: Sort the array and return the second last element.
    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(1) if sorting in-place.
    """
    if len(arr) < 2:
        return None  # No second largest element possible
    
    arr.sort()  # Sorting takes O(n log n)
    return arr[-2]  # Second largest element

def second_largest_two_pass(arr):
    """
    Better Approach: Two-pass solution without sorting.
    Time Complexity: O(n) + O(n) = O(n) (Two separate passes).
    Space Complexity: O(1).
    """
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    # First pass: Find the largest element
    for num in arr:
        if num > largest:
            largest = num

    # Second pass: Find the second largest element
    for num in arr:
        if num > second_largest and num < largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

def second_largest_optimal(arr):
    """
    Optimal Approach: Single pass solution.
    Time Complexity: O(n) (Only one loop).
    Space Complexity: O(1).
    """
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest  # Previous largest becomes second largest
            largest = num  # Update largest
        elif num > second_largest and num < largest:
            second_largest = num  # Update second largest

    return second_largest if second_largest != float('-inf') else None

# Example Usage
arr = [55, 32, 97, -55, 45, 32, 88, 21]

print("Brute Force Approach:", second_largest_brute_force(arr.copy()))  # Using copy to avoid modifying the original array
print("Two Pass Approach:", second_largest_two_pass(arr))
print("Optimal Approach:", second_largest_optimal(arr))
