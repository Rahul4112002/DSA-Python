def search_insert_position(nums, target):
    """
    This function returns the index of the target if found in the sorted list nums.
    If the target is not found, it returns the index where the target should be inserted
    to maintain the sorted order.

    :param nums: List[int] - A list of distinct integers sorted in ascending order.
    :param target: int - The target value to search for.
    :return: int - The index of the target or the insert position.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage:
if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    targets = [5, 2, 7, 0]
    results = [search_insert_position(nums, target) for target in targets]
    print(results)  # Output: [2, 1, 4, 0]
