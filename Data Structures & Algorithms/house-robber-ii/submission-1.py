class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        money_max_1 = [0 for _ in nums]
        last = 0
        sec_last = 0
        for i in range(len(nums)-2, -1, -1):
            money_max_1[i] = max(last, nums[i] + sec_last)
            sec_last = last
            last = money_max_1[i]

        
        money_max_2 = [0 for _ in nums]
        last = 0
        sec_last = 0
        for i in range(len(nums)-1, 0, -1):
            money_max_2[i] = max(last, nums[i] + sec_last)
            sec_last = last
            last = money_max_2[i]

        return max(money_max_1[0], money_max_2[1])