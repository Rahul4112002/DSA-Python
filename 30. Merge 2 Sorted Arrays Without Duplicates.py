def sortedArray(a, b):
    """
    Merges two sorted arrays into a single sorted array without duplicates.

    Parameters:
    a (List[int]): First sorted array.
    b (List[int]): Second sorted array.

    Returns:
    List[int]: Sorted union of both arrays without duplicates.

    Time Complexity: O(n + m)  -> We traverse both arrays once.
    Space Complexity: O(n + m) -> Resultant array stores unique elements from both.
    """

    i = 0  # Pointer for array 'a'
    j = 0  # Pointer for array 'b'
    result = []  # List to store the union

    # Merge arrays while avoiding duplicates
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # If element in 'a' is smaller or equal
            if len(result) == 0 or result[-1] != a[i]:  # Avoid duplicate insertions
                result.append(a[i])
            i += 1  # Move pointer in 'a'
        else:  # If element in 'b' is smaller
            if len(result) == 0 or result[-1] != b[j]:  # Avoid duplicate insertions
                result.append(b[j])
            j += 1  # Move pointer in 'b'

    # Append remaining elements from 'a', avoiding duplicates
    while i < len(a):
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
        i += 1

    # Append remaining elements from 'b', avoiding duplicates
    while j < len(b):
        if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])
        j += 1

    return result

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]
print(sortedArray(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7]
