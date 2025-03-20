'''
https://docs.google.com/document/d/1RdxwcXdnTqVQnZ-j6wzFEi93e4RgPpbYjXLbC0EQ0C0/edit?tab=t.0
'''
from typing import List

# Approach 1: Using Extra Matrix
# Time Complexity: O(N^2)
# Space Complexity: O(N^2) (due to extra matrix)
def rotateExtraMatrix(matrix: List[List[int]]):
    r, c = len(matrix), len(matrix[0])
    result = [[0 for _ in range(c)] for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            result[j][r - 1 - i] = matrix[i][j]
    
    matrix[:] = result

# Approach 2: In-Place Rotation (Transpose + Reverse)
# Time Complexity: O(N^2)
# Space Complexity: O(1) (modifies matrix in place)
def rotateInPlace(matrix: List[List[int]]):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Utility function to print the matrix
def printMatrix(matrix: List[List[int]]):
    for row in matrix:
        print(row)
    print()

# Example Usage
if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original Matrix:")
    printMatrix(matrix1)

    matrix1_copy = [row[:] for row in matrix1]
    print("Rotation using Extra Matrix:")
    rotateExtraMatrix(matrix1_copy)
    printMatrix(matrix1_copy)

    matrix1_copy = [row[:] for row in matrix1]
    print("In-Place Rotation:")
    rotateInPlace(matrix1_copy)
    printMatrix(matrix1_copy)

    # Example 2
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print("Original Matrix:")
    printMatrix(matrix2)

    matrix2_copy = [row[:] for row in matrix2]
    print("Rotation using Extra Matrix:")
    rotateExtraMatrix(matrix2_copy)
    printMatrix(matrix2_copy)

    matrix2_copy = [row[:] for row in matrix2]
    print("In-Place Rotation:")
    rotateInPlace(matrix2_copy)
    printMatrix(matrix2_copy)
