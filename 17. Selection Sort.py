'''
Selection Sort Algorithm
 Definition:
 Selection Sort is a simple comparison-based sorting algorithm. It repeatedly selects the 
 smallest (or largest) element from the unsorted portion and swaps it with the first 
 unsorted element. The algorithm maintains two subarrays:
 1. Sorted subarray (left side)
 2. Unsorted subarray (right side)
 It iterates through the list and places each element in its correct position.
''' 


def selection_sort_ascending(arr):
    """
    Implements Selection Sort to sort an array in ascending order.
    Time Complexity: O(n^2)
    Space Complexity: O(1) (in-place sorting)
    """
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current index is the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Find the minimum element in the unsorted part
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum with the first element

def selection_sort_descending(arr):
    """
    Implements Selection Sort to sort an array in descending order.
    Time Complexity: O(n^2)
    Space Complexity: O(1) (in-place sorting)
    """
    n = len(arr)
    for i in range(n):
        max_index = i  # Assume the current index is the maximum
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:  # Find the maximum element in the unsorted part
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]  # Swap the found maximum with the first element

# Example Usage
data = [7, 8, 5, 4, 1, 6, 9, 2]
selection_sort_ascending(data)
print("Sorted in Ascending Order:", data)

data = [7, 8, 5, 4, 1, 6, 9, 2]
selection_sort_descending(data)
print("Sorted in Descending Order:", data)
