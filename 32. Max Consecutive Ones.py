from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    """
    Finds the maximum number of consecutive 1s in a binary array.

    Parameters:
    nums (List[int]): The input binary array.

    Returns:
    int: The length of the longest contiguous subarray of 1s.

    Time Complexity: O(n)  
    - The function traverses the array exactly once, making it linear.

    Space Complexity: O(1)  
    - Only a few integer variables are used, making space usage constant.
    """

    cnt = 0  # Current streak of consecutive 1s
    maxi = 0  # Maximum streak found so far

    for num in nums:
        if num == 1:
            cnt += 1  # Increment streak
        else:
            maxi = max(maxi, cnt)  # Update max streak
            cnt = 0  # Reset streak

    return max(maxi, cnt)  # Ensure we capture the last streak if it's the longest

# Example test cases
nums1 = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums1))  # Output: 3

nums2 = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums2))  # Output: 2

nums3 = [0, 0, 0, 0]
print(findMaxConsecutiveOnes(nums3))  # Output: 0

nums4 = [1, 1, 1, 1, 1]
print(findMaxConsecutiveOnes(nums4))  # Output: 5

nums5 = [1, 0, 1, 0, 1, 0, 1]
print(findMaxConsecutiveOnes(nums5))  # Output: 1

nums6 = [0, 1, 1, 1, 0, 0, 1, 1]
print(findMaxConsecutiveOnes(nums6))  # Output: 3
