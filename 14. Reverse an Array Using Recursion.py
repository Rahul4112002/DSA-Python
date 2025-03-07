# 1. Recursive Approach
def reverse_array_recursive(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array_recursive(arr, left + 1, right - 1)

# Time Complexity: O(N) (Each element is swapped once)
# Space Complexity: O(N) (Recursive stack space)

# 2. Iterative Approach
def reverse_array_iterative(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Time Complexity: O(N) (Each element is swapped once)
# Space Complexity: O(1) (No extra space used)

# 3. Slicing Approach (Pythonic Way)
def reverse_array_slicing(arr, left, right):
    arr[left:right+1] = arr[left:right+1][::-1]

# Time Complexity: O(N) (Slicing internally iterates over elements)
# Space Complexity: O(N) (New slice is created in memory)

# Example Usage
arr = [5, 7, 2, 3, 6, 1, 9]
left, right = 2, 5

# Recursive
arr_recursive = arr.copy()
reverse_array_recursive(arr_recursive, left, right)
print("Recursive:", arr_recursive)

# Iterative
arr_iterative = arr.copy()
reverse_array_iterative(arr_iterative, left, right)
print("Iterative:", arr_iterative)

# Slicing
arr_slicing = arr.copy()
reverse_array_slicing(arr_slicing, left, right)
print("Slicing:", arr_slicing)
