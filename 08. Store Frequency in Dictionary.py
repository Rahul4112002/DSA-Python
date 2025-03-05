# Approach 1: Using a dictionary with explicit checks
def frequency_map_method1(nums):
    freq = {}  # Initialize an empty dictionary

    for num in nums:
        if num in freq:
            freq[num] += 1  # Increment the count if already present
        else:
            freq[num] = 1  # Initialize the count if not present

    return freq

# Time Complexity: O(N) - We iterate through the list once
# Space Complexity: O(N) - In the worst case, all elements are unique and stored in the dictionary

# Approach 2: Using dictionary's get() method
def frequency_map_method2(nums):
    freq = {}  # Initialize an empty dictionary

    for num in nums:
        freq[num] = freq.get(num, 0) + 1  # Use get() to provide default value

    return freq

# Time Complexity: O(N) - Each lookup and insertion is O(1) on average
# Space Complexity: O(N) - Same as the first approach

# Example Usage
nums = [5, 6, 7, 7, 1, 9, 1, 1, 5, 1, 1]
print(frequency_map_method1(nums))
print(frequency_map_method2(nums))
