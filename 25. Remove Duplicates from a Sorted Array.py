'''
https://codeanddebugacademy.com/remove-duplicates-from-sorted-array-leetcode-26/
'''

from typing import List

def remove_duplicates_freq_map(nums: List[int]) -> int:
    """
    Removes duplicates using a frequency map.
    
    Time Complexity: O(N) - We traverse the list once to create the dictionary and once more to update the list.
    Space Complexity: O(N) - We use a dictionary to store unique elements.
    """
    my_dict = dict()
    for i in nums:
        my_dict[i] = 0  # Store unique elements as keys

    j = 0
    for n in my_dict:
        nums[j] = n
        j += 1
    return j  # Length of unique elements

def remove_duplicates_two_pointers(nums: List[int]) -> int:
    """
    Removes duplicates using the two-pointer approach.
    
    Time Complexity: O(N) - We traverse the list once with two pointers.
    Space Complexity: O(1) - No extra space is used, only modifying the input list in-place.
    """
    if len(nums) == 1:
        return 1
    i = 0
    j = i + 1
    while j < len(nums):
        if nums[j] != nums[i]:  # Found a new unique element
            i += 1
            nums[j], nums[i] = nums[i], nums[j]  # Swap to maintain order
        j += 1
    return i + 1  # Length of unique elements

# Example usage:
nums1 = [1, 1, 2, 3, 3, 4, 7, 7, 9, 9, 10]
nums2 = nums1[:]  # Copy for second approach

# Using Frequency Map Approach
count_freq = remove_duplicates_freq_map(nums1)
print("Frequency Map Approach:")
print("Unique elements count:", count_freq)
print("Modified array:", nums1[:count_freq])

# Using Two-Pointer Approach
count_tp = remove_duplicates_two_pointers(nums2)
print("\nTwo-Pointer Approach:")
print("Unique elements count:", count_tp)
print("Modified array:", nums2[:count_tp])
