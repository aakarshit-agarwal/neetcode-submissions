class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0] and self.find_word(board, word, row, col, 0, set()):
                    return True
        return False
        
    def find_word(self, board, word, row, col, index, visited_set):
        if index == len(word):
            return True
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) \
        or (row, col) in visited_set:
            return False
        
        visited_set.add((row, col))
        
        result = False
        if board[row][col] == word[index]:
            result = result or self.find_word(board, word, row+1, col, index+1, visited_set) \
            or self.find_word(board, word, row-1, col, index+1, visited_set) \
            or self.find_word(board, word, row, col+1, index+1, visited_set) \
            or self.find_word(board, word, row, col-1, index+1, visited_set)

        visited_set.remove((row, col))
        return result
