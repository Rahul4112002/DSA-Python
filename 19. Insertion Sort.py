def insertion_sort_ascending(arr):
    """
    Performs insertion sort in ascending order.
    
    Time Complexity:
    - Best Case: O(n) [Already sorted]
    - Worst Case: O(n^2) [Reverse sorted]
    - Average Case: O(n^2)
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one step ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insertion_sort_descending(arr):
    """
    Performs insertion sort in descending order.
    
    Time Complexity:
    - Best Case: O(n) [Already sorted in descending]
    - Worst Case: O(n^2) [Sorted in ascending]
    - Average Case: O(n^2)
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements smaller than key one step ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = arr1.copy()  # Copy for descending sort

insertion_sort_ascending(arr1)
print("Sorted in Ascending:", arr1)

insertion_sort_descending(arr2)
print("Sorted in Descending:", arr2)
