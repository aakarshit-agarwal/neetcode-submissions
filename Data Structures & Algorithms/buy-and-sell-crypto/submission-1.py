class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = []
        min_so_far = float('inf')

        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            left_min.append(min_so_far)

        right_max = []
        max_so_far = float('-inf')
        for i in range(len(prices)-1, -1, -1):
            max_so_far = max(max_so_far, prices[i])
            right_max.insert(0, max_so_far)

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, right_max[i] - left_min[i])

        return max_profit