class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.longes_increasing_subsequence(nums, -1001, 0)


    def longes_increasing_subsequence(self, nums, curr_num, index):
        if index == len(nums):
            return 0
        result = self.longes_increasing_subsequence(nums, curr_num, index+1)
        if nums[index] > curr_num:
            result = max(result, 1 + self.longes_increasing_subsequence(nums, nums[index], index+1))
        return result