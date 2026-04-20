class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = [0 for _ in nums]
        sec_last = 0
        last = 0
        for i in range(len(max_money)-1, -1, -1):
            max_money[i] = max(last, nums[i] + sec_last)
            sec_last = last
            last = max_money[i]
        return max_money[0]