class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 1
        row = 0
        col = 0

        result = []
        while row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0]) and matrix[row][col] < 101:
            result.append(matrix[row][col])
            matrix[row][col] = 101

            if direction == 1:
                if row >= 0 and col+1 >= 0 and row < len(matrix) and col+1 < len(matrix[0]) and matrix[row][col+1] < 101:
                    col += 1
                    print("Right", row, col)
                else:
                    row += 1
                    direction = 2
                    print("Down-", row, col)
            elif direction == 2:
                if row+1 >= 0 and col >= 0 and row+1 < len(matrix) and col < len(matrix[0]) and matrix[row+1][col] < 101:
                    row += 1
                    print("Down", row, col)
                else:
                    col -= 1
                    direction = 3
                    print("Left-", row, col)
            elif direction == 3:
                if row >= 0 and col-1 >= 0 and row < len(matrix) and col-1 < len(matrix[0]) and matrix[row][col-1] < 101:
                    col -= 1
                    print("Left", row, col)
                else:
                    row -= 1
                    direction = 4
                    print("Up-", row, col)
            elif direction == 4:
                if row-1 >= 0 and col >= 0 and row-1 < len(matrix) and col < len(matrix[0]) and matrix[row-1][col] < 101:
                    row -= 1
                    print("Up", row, col)
                else:
                    col += 1
                    direction = 1
                    print("Right-", row, col)
            else:
                break
        return result