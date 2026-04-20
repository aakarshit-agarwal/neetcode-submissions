class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        x1 = 0
        x2 = 1
        while n > 0:
            temp = x1 + x2
            x1 = x2
            x2 = temp
            n = n - 1
        return x2