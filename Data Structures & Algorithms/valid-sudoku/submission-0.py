class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        block_map = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                row_index = self.get_row_index(row, col)
                col_index = self.get_col_index(row, col)
                block_index = self.get_block_index(row, col)

                if row_index in row_map.keys() and board[row][col] in row_map[row_index]:
                    return False
                if col_index in col_map.keys() and board[row][col] in col_map[col_index]:
                    return False
                if block_index in block_map.keys() and board[row][col] in block_map[block_index]:
                    return False
                
                if row_index not in row_map.keys():
                    row_map[row_index] = set()
                row_map[row_index].add(board[row][col])

                if col_index not in col_map.keys():
                    col_map[col_index] = set()
                col_map[col_index].add(board[row][col])

                if block_index not in block_map.keys():
                    block_map[block_index] = set()
                block_map[block_index].add(board[row][col])

        return True

    def get_row_index(self, row, col):
        return row+1

    def get_col_index(self, row, col):
        return col+1

    def get_block_index(self, row, col):
        if row == 0 or row == 1 or row == 2:
            if col == 0 or col == 1 or col == 2:
                return 1
            if col == 3 or col == 4 or col == 5:
                return 2
            if col == 6 or col == 7 or col == 8:
                return 3
        if row == 3 or row == 4 or row == 5:
            if col == 0 or col == 1 or col == 2:
                return 4
            if col == 3 or col == 4 or col == 5:
                return 5
            if col == 6 or col == 7 or col == 8:
                return 6
        if row == 6 or row == 7 or row == 8:
            if col == 0 or col == 1 or col == 2:
                return 7
            if col == 3 or col == 4 or col == 5:
                return 8
            if col == 6 or col == 7 or col == 8:
                return 9
