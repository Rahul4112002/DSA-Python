def find_largest_method1(nums):
    """
    Method 1: Iterative approach using a loop.
    
    Time Complexity: O(n) - We traverse the list once.
    Space Complexity: O(1) - Uses only a constant amount of extra space.
    """
    # Initialize largest with the first element
    largest = nums[0]  

    # Traverse the array and update largest if a bigger element is found
    for num in nums:
        if num > largest:
            largest = num

    return largest

def find_largest_method2(nums):
    """
    Method 2: Using Python's max() function.
    
    Time Complexity: O(n) - max() internally performs a single traversal.
    Space Complexity: O(1) - No additional space used apart from variables.
    """
    return max(nums)  # Python's built-in max function

def find_largest_method3(nums):
    """
    Method 3: Using negative infinity (-∞) as the initial largest value.
    
    Time Complexity: O(n) - We traverse the list once.
    Space Complexity: O(1) - Uses only a constant amount of extra space.
    """
    # Initialize with the smallest possible value
    largest = float('-inf')  

    for num in nums:
        largest = max(largest, num)  # Update using max function

    return largest

# Example usage
nums = [55, 32, -97, 99, 3, 67]
print("Largest element (Method 1):", find_largest_method1(nums))
print("Largest element (Method 2):", find_largest_method2(nums))
print("Largest element (Method 3):", find_largest_method3(nums))
