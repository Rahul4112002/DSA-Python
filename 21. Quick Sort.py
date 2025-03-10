def partition(arr, low, high):
    """
    Partitions the array using the first element as the pivot.
    
    Parameters:
    arr (list): The array to be partitioned.
    low (int): Starting index.
    high (int): Ending index.

    Returns:
    int: The final pivot index.
    
    Time Complexity: O(n) - Each element is compared once while partitioning.
    Space Complexity: O(1) - In-place swapping, no extra space used.
    """
    pivot = arr[low]  # Choosing the first element as pivot
    i = low
    j = high

    while i < j:
        # Move i to the right until we find an element greater than the pivot
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        # Move j to the left until we find an element smaller than the pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        # Swap elements if needed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j  # Return pivot index

def quick_sort(arr, low, high):
    """
    Performs Quick Sort on the given array.
    
    Parameters:
    arr (list): The array to be sorted.
    low (int): Starting index.
    high (int): Ending index.

    Time Complexity:
    - Best Case: O(n log n) → When the pivot divides the array into equal halves.
    - Average Case: O(n log n) → Expected for random data.
    - Worst Case: O(n²) → If the pivot is always the smallest or largest element.
    
    Space Complexity:
    - Best Case: O(log n) → Due to recursive calls.
    - Worst Case: O(n) → When recursion depth is maximum (unbalanced partitioning).
    """
    if low < high:
        p_index = partition(arr, low, high)  # Get pivot index
        quick_sort(arr, low, p_index - 1)  # Sort the left subarray
        quick_sort(arr, p_index + 1, high)  # Sort the right subarray

# Example usage
arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array = {arr}")
