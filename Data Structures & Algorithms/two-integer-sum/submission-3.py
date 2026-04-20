class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req_num = {}
        for i in range(len(nums)):
            if target-nums[i] in req_num.keys():
                return sorted([i, req_num[target-nums[i]]])
            else:
                req_num[nums[i]] = i

        return [-1, -1]