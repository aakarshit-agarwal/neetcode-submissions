class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        running_prod = 1
        for i in range(len(nums)):
            result[i] = result[i] * running_prod
            running_prod *= nums[i]

        running_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * running_prod
            running_prod *= nums[i]

        return result