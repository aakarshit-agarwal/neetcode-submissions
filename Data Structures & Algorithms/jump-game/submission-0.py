class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_true_index = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_true_index:
                last_true_index = i
        return last_true_index==0