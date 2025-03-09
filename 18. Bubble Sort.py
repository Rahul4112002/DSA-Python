# Bubble Sort Algorithm - Average/Worst Case and Best Case Implementation for Ascending and Descending Order

# Worst/Average Case Bubble Sort for Ascending Order
# Time Complexity: O(n^2) - Due to nested loops
# Space Complexity: O(1) - In-place sorting
def bubble_sort_worst_asc(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:  # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Best Case Optimized Bubble Sort for Ascending Order
# Time Complexity: O(n) - If already sorted
# Space Complexity: O(1) - In-place sorting
def bubble_sort_best_asc(arr):
    n = len(arr)
    is_swap = False
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:  # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swap = True
        if not is_swap:  # If no swaps, array is already sorted
            return

# Worst/Average Case Bubble Sort for Descending Order
# Time Complexity: O(n^2) - Nested loops still run
# Space Complexity: O(1) - In-place sorting
def bubble_sort_worst_desc(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] < arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Best Case Optimized Bubble Sort for Descending Order
# Time Complexity: O(n) - If already sorted
# Space Complexity: O(1) - In-place sorting
def bubble_sort_best_desc(arr):
    n = len(arr)
    is_swap = False
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] < arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swap = True
        if not is_swap:  # If no swaps, array is already sorted
            return

# Example usage for ascending order
arr_worst_asc = [7, 8, 5, 4, 1, 6, 9, 2]
print("Before Sorting (Worst Case Ascending):", arr_worst_asc)
bubble_sort_worst_asc(arr_worst_asc)
print("After Sorting (Worst Case Ascending):", arr_worst_asc)

arr_best_asc = [7, 8, 5, 4, 1, 6, 9, 2]
print("\nBefore Sorting (Best Case Ascending):", arr_best_asc)
bubble_sort_best_asc(arr_best_asc)
print("After Sorting (Best Case Ascending):", arr_best_asc)

# Example usage for descending order
arr_worst_desc = [7, 8, 5, 4, 1, 6, 9, 2]
print("\nBefore Sorting (Worst Case Descending):", arr_worst_desc)
bubble_sort_worst_desc(arr_worst_desc)
print("After Sorting (Worst Case Descending):", arr_worst_desc)

arr_best_desc = [7, 8, 5, 4, 1, 6, 9, 2]
print("\nBefore Sorting (Best Case Descending):", arr_best_desc)
bubble_sort_best_desc(arr_best_desc)
print("After Sorting (Best Case Descending):", arr_best_desc)
