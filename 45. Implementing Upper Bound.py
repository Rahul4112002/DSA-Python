def upper_bound(arr, x):
    """
    Find the index of the smallest element in arr that is greater than x.
    If no such element exists, return the length of the array.
    """
    low, high = 0, len(arr) - 1
    upper_bound_index = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            upper_bound_index = mid
            high = mid - 1
        else:
            low = mid + 1

    return upper_bound_index

# Example usage:
arr = [1, 2, 8, 10, 11, 12, 19]
k = 5
x = 5

upper_bound_index = upper_bound(arr, x)


print(f"Upper bound index of {x}: {upper_bound_index}")