def is_sorted(arr):
    """
    Function to check if the given array is sorted in ascending order.

    Time Complexity: O(n) - Since we are traversing the array once.
    Space Complexity: O(1) - No extra space is used apart from variables.
    """
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:  # If any element is greater than the next, it's not sorted.
            return False
    return True  # If loop completes, array is sorted.

# Example usage:
arr1 = [3, 5, 6, 8, 9, 10]
arr2 = [1, 2, 5, 8, 3]

print(is_sorted(arr1))  # Output: True
print(is_sorted(arr2))  # Output: False
