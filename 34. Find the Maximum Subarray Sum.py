def max_subarray_better(nums):
    """Better Approach: O(n^2) Time, O(1) Space"""
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]  # Running sum
            max_sum = max(max_sum, curr_sum)
    
    return max_sum

def max_subarray_kadane(nums):
    """Kadane’s Algorithm: O(n) Time, O(1) Space"""
    maxi = float("-inf")
    curr_sum = 0

    for num in nums:
        curr_sum += num  # Add current element
        maxi = max(maxi, curr_sum)  # Update maximum sum
        if curr_sum < 0:  # Reset if sum goes negative
            curr_sum = 0

    return maxi

# Example Usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Better Approach Output:", max_subarray_better(nums))
print("Kadane’s Algorithm Output:", max_subarray_kadane(nums))
