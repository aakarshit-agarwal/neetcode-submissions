class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number = 0
        for i in range(len(nums)):
            number = number - nums[i] + i
        number += len(nums)
        return number