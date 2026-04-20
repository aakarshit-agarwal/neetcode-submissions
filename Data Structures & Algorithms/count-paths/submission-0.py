class Solution:
    memorization = {}
    def uniquePaths(self, m: int, n: int) -> int:
        self.memorization = {}
        return self.count_unique_paths(m, n, 0, 0)

    def count_unique_paths(self, m, n, row, col):
        if row == m-1 and col == n-1:
            return 1
        if row in self.memorization.keys() and col in self.memorization[row].keys():
            return self.memorization[row][col]
        result = 0
        if row < m-1:
            result = result + self.count_unique_paths(m, n, row+1, col)
        if col < n-1:
            result = result + self.count_unique_paths(m, n, row, col+1)
        if row not in self.memorization.keys():
            self.memorization[row] = {}
        self.memorization[row][col] = result        
        return result
