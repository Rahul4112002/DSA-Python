def merge_array(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Parameters:
    left (list): Left sub-array (sorted)
    right (list): Right sub-array (sorted)
    
    Returns:
    list: Merged sorted array
    """
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    # Merge elements in sorted order
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements from left array
    result.extend(left[i:])
    # Append remaining elements from right array
    result.extend(right[j:])
    
    return result

def merge_sort(arr):
    """
    Performs merge sort on the given array.
    
    Parameters:
    arr (list): The array to be sorted.
    
    Returns:
    list: Sorted array.
    """
    if len(arr) <= 1:  # Base case: A single-element array is already sorted
        return arr

    mid = len(arr) // 2  # Finding the middle index
    left = merge_sort(arr[:mid])  # Recursively sorting the left half
    right = merge_sort(arr[mid:])  # Recursively sorting the right half

    return merge_array(left, right)  # Merging the sorted halves

# Example usage
arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 2, 3, 4, 4, 5, 6]
