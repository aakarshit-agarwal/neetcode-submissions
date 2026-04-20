class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = False

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero = True

        for row in range(len(matrix) -1, 0, -1):
            for col in range(len(matrix[0]) -1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if row_zero == True:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
