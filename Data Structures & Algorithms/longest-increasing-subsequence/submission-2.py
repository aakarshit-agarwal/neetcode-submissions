class Solution:
    memorization_map = {}
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memorization_map = {}
        return self.longes_increasing_subsequence(nums, -1001, 0)


    def longes_increasing_subsequence(self, nums, curr_num, index):
        if index == len(nums):
            return 0
        if (curr_num, index) in self.memorization_map.keys():
            return self.memorization_map[(curr_num, index)]
        result = self.longes_increasing_subsequence(nums, curr_num, index+1)
        if nums[index] > curr_num:
            result = max(result, 1 + self.longes_increasing_subsequence(nums, nums[index], index+1))
        self.memorization_map[(curr_num, index)] = result
        return self.memorization_map[(curr_num, index)]