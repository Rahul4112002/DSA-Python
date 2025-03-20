'''
https://docs.google.com/document/d/1Ge0sSjnuGTBfd3t-gHWEb0m-H_NKGFhGwbZpZIKYlFs/edit?tab=t.0
'''


from typing import List

# Brute Force Approach (Using float("inf") as a marker)
# Time Complexity: O(N*M) + O(N*M) ≈ O(N*M)
# Space Complexity: O(1) (modifies matrix in place)
def markInfinity(matrix: List[List[int]], row: int, col: int):
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        if matrix[i][col] != 0:  # Avoid overwriting original zeros
            matrix[i][col] = float("inf")
    for j in range(c):
        if matrix[row][j] != 0:  # Avoid overwriting original zeros
            matrix[row][j] = float("inf")

def bruteForce(matrix: List[List[int]]):
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                markInfinity(matrix, i, j)

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

# Better Approach (Using extra row and column arrays)
# Time Complexity: O(N*M) + O(N*M) ≈ O(N*M)
# Space Complexity: O(N + M) (extra row and column arrays)
def betterApproach(matrix: List[List[int]]):
    r, c = len(matrix), len(matrix[0])
    rowTrack = [0 for _ in range(r)]
    colTrack = [0 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowTrack[i] = -1
                colTrack[j] = -1

    for i in range(r):
        for j in range(c):
            if rowTrack[i] == -1 or colTrack[j] == -1:
                matrix[i][j] = 0

# Utility function to print matrix
def printMatrix(matrix: List[List[int]]):
    for row in matrix:
        print(row)
    print()

# Example Usage
if __name__ == "__main__":
    matrix1 = [[1,1,1], [1,0,1], [1,1,1]]
    print("Original Matrix:")
    printMatrix(matrix1)

    matrix1_copy = [row[:] for row in matrix1]
    print("Brute Force Output:")
    bruteForce(matrix1_copy)
    printMatrix(matrix1_copy)

    matrix1_copy = [row[:] for row in matrix1]
    print("Better Approach Output:")
    betterApproach(matrix1_copy)
    printMatrix(matrix1_copy)

    # Example 2
    matrix2 = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    print("Original Matrix:")
    printMatrix(matrix2)

    matrix2_copy = [row[:] for row in matrix2]
    print("Brute Force Output:")
    bruteForce(matrix2_copy)
    printMatrix(matrix2_copy)

    matrix2_copy = [row[:] for row in matrix2]
    print("Better Approach Output:")
    betterApproach(matrix2_copy)
    printMatrix(matrix2_copy)
