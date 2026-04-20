class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_right_min = [0] * len(prices)
        right_left_max = [0] * len(prices)

        left_min = prices[0]
        right_max = prices[-1]
        for left in range(0, len(prices)):
            right = len(prices) - left - 1
            left_right_min[left] = min(left_min, prices[left])
            left_min = left_right_min[left]

            right_left_max[right] = max(right_max, prices[right])
            right_max = right_left_max[right]

        profit_max = 0
        for i in range(0, len(prices)):
            profit_max = max(profit_max, right_left_max[i] - left_right_min[i])

        return profit_max