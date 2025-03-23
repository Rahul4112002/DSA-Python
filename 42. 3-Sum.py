from typing import List

# 🔹 Brute Force Approach (O(n^3) time complexity)
def threeSum_bruteforce(nums: List[int]) -> List[List[int]]:
    """
    Brute Force approach using three nested loops.
    Time Complexity: O(n^3)
    Space Complexity: O(k) where k is the number of unique triplets.
    """
    my_set = set()
    n = len(nums)

    # check all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    my_set.add(tuple(temp))

    ans = [list(item) for item in my_set]
    return ans


# 🔹 Better Approach using HashSet (O(n^2) time complexity)
def threeSum_better(nums: List[int]) -> List[List[int]]:
    """
    HashSet approach to store visited elements.
    Time Complexity: O(n^2)
    Space Complexity: O(n) for the HashSet.
    """
    n = len(nums)
    result = set()
    
    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])
            if third in hashset:
                temp = [nums[i], nums[j], third]
                temp.sort()
                result.add(tuple(temp))
            hashset.add(nums[j])

    ans = list(result)
    return ans


# 🔹 Optimized Two Pointers Approach (O(n^2) time complexity)
def threeSum_optimized(nums: List[int]) -> List[List[int]]:
    """
    Optimized approach using sorting and two pointers.
    Time Complexity: O(n^2) → Sorting takes O(n log n) + O(n^2) for searching.
    Space Complexity: O(k) where k is the number of unique triplets.
    """
    ans = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        j, k = i + 1, n - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                
                # Skip duplicate elements
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return ans


# 🔹 Example Usage
if __name__ == "__main__":
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]

    print("Brute Force:", threeSum_bruteforce(nums1))
    print("Better Approach:", threeSum_better(nums1))
    print("Optimized Approach:", threeSum_optimized(nums1))

    print("Brute Force:", threeSum_bruteforce(nums2))
    print("Better Approach:", threeSum_better(nums2))
    print("Optimized Approach:", threeSum_optimized(nums2))

    print("Brute Force:", threeSum_bruteforce(nums3))
    print("Better Approach:", threeSum_better(nums3))
    print("Optimized Approach:", threeSum_optimized(nums3))
