def linearSearch(arr,target):
    """
    Performs a linear search in the given array.

    Parameters:
    n (int): The size of the array.
    num (int): The target number to search for.
    arr (List[int]): The array to search in.

    Returns:
    int: The index of the target number if found, otherwise -1.

    Time Complexity: 
    - Best Case: O(1) (if the target is at the first position)
    - Worst Case: O(n) (if the target is at the last position or not present)

    Space Complexity: O(1) (only a few extra variables are used)
    """

    for i in range(0, len(arr)):  # Iterate through the array
        if arr[i] == target:  # Check if the current element matches the target
            return i  # Return the index if found

    return -1  # Return -1 if the target is not found

# Example usage:
arr = [10, 20, 30, 40, 50]
target = 30
print(linearSearch(arr,target))  # Output: 2
