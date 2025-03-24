def get_floor_and_ceil(a, x):
    """
    This function finds the floor and ceiling of 'x' in a sorted array 'a'.
    
    :param a: List[int] - A sorted list of integers.
    :param x: int - The target number.
    :return: List[int] - A list containing the floor and ceiling values.
    """
    floor, ceil = -1, -1
    low, high = 0, len(a) - 1  

    while low <= high:
        mid = (low + high) // 2  

        if a[mid] == x:
            return [x, x]  # If exact match, floor and ceil are the same
        
        elif a[mid] > x:
            ceil = a[mid]  # Update ceil (smallest number ≥ x)
            high = mid - 1  # Move left to find a smaller valid ceil
        
        else:
            floor = a[mid]  # Update floor (largest number ≤ x)
            low = mid + 1  # Move right to find a larger valid floor

    return [floor, ceil]

# Example usage
if __name__ == "__main__":
    a = [3, 4, 7, 8, 8, 10]
    x = 5
    result = get_floor_and_ceil(a, x)
    print(result)  # Output: [4, 7]
