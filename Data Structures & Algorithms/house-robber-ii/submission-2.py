class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))


    def rob_helper(self, nums):
        money_max_2 = [0 for _ in nums]
        last = 0
        sec_last = 0
        for i in range(len(nums)-1, -1, -1):
            money_max_2[i] = max(last, nums[i] + sec_last)
            sec_last = last
            last = money_max_2[i]
        return last