def find_floor(arr, k):
    """
    Finds the index of the largest element in a sorted array that is less than or equal to k.
    
    Parameters:
    arr (list of int): A list of unique integers sorted in ascending order.
    k (int): The target integer.
    
    Returns:
    int: The index of the floor element, or -1 if no such element exists.
    """
    low, high = 0, len(arr) - 1
    floor_index = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] <= k:
            floor_index = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return floor_index

# Example usage:
arr1 = [1, 2, 8, 10, 11, 12, 19]
k1 = 5
print(find_floor(arr1, k1))  # Output: 1

arr2 = [1, 2, 8, 10, 11, 12, 19]
k2 = 0
print(find_floor(arr2, k2))  # Output: -1

arr3 = [1, 2, 8]
k3 = 1
print(find_floor(arr3, k3))  # Output: 0
