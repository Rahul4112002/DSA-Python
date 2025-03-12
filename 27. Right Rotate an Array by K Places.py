from typing import List

def rotate_method1(nums: List[int], k: int) -> None:
    """
    Method 1: Brute Force (Pop and Insert)
    Time Complexity: O(k * n) (Worst case: O(n^2) if k ≈ n)
    Space Complexity: O(1) (In-place modification)
    """
    rotations = k % len(nums)  # Reduce unnecessary full rotations
    for _ in range(rotations):
        last = nums.pop()  # Remove last element
        nums.insert(0, last)  # Insert at the beginning

def rotate_method2(nums: List[int], k: int) -> None:
    """
    Method 2: Using Slicing
    Time Complexity: O(n)
    Space Complexity: O(1) (In-place modification)
    """
    n = len(nums)
    k %= n  # Handle k > n
    nums[:] = nums[n - k:] + nums[:n - k]  # Rotate using slicing

def reverse(nums: List[int], l: int, r: int) -> None:
    """
    Helper Function: Reverse a subarray in-place
    """
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

def rotate_method3(nums: List[int], k: int) -> None:
    """
    Method 3: Using Reverse Method (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1) (In-place modification)
    """
    n = len(nums)
    k %= n  # Handle k > n

    # Step 1: Reverse the last k elements
    reverse(nums, n - k, n - 1)

    # Step 2: Reverse the first n-k elements
    reverse(nums, 0, n - k - 1)

    # Step 3: Reverse the entire array
    reverse(nums, 0, n - 1)

# Example usage
nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = nums1.copy()
nums3 = nums1.copy()

k = 3
rotate_method1(nums1, k)
print("Method 1 (Brute Force):", nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

rotate_method2(nums2, k)
print("Method 2 (Slicing):", nums2)  # Output: [5, 6, 7, 1, 2, 3, 4]

rotate_method3(nums3, k)
print("Method 3 (Reverse):", nums3)  # Output: [5, 6, 7, 1, 2, 3, 4]
