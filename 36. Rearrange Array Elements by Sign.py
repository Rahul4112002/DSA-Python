def rearrange_array_extra_space(nums):
    """
    Approach 1: Using Extra Lists
    Time Complexity: O(n) - Iterates through nums twice (once to separate pos/neg, once to merge).
    Space Complexity: O(n) - Uses extra space for two separate lists (pos and neg).
    """
    pos = []
    neg = []
    
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)

    # Merge positive and negative numbers in alternate positions
    for i in range(len(pos)):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]

    return nums

def rearrange_array_in_place(nums):
    """
    Approach 2: Using an Answer Array
    Time Complexity: O(n) - Iterates through nums once.
    Space Complexity: O(n) - Uses an extra list of size n.
    """
    n = len(nums)
    ans = [0] * n  # Create an array to store results
    pos_index, neg_index = 0, 1  # Alternating indices for pos/neg numbers

    for num in nums:
        if num < 0:
            ans[neg_index] = num
            neg_index += 2
        else:
            ans[pos_index] = num
            pos_index += 2

    return ans

# Example Usage
nums1 = [3, 1, -2, -5, 2, -4]
nums2 = [-1, 1]

print("Extra Space Approach Output for nums1:", rearrange_array_extra_space(nums1[:]))  # Expected: [3,-2,1,-5,2,-4]
print("In-Place Approach Output for nums1:", rearrange_array_in_place(nums1[:]))  # Expected: [3,-2,1,-5,2,-4]

print("Extra Space Approach Output for nums2:", rearrange_array_extra_space(nums2[:]))  # Expected: [1,-1]
print("In-Place Approach Output for nums2:", rearrange_array_in_place(nums2[:]))  # Expected: [1,-1]
