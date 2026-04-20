class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_positions = {}

        for i in range(len(nums)):
            if target - nums[i] in num_positions.keys():
                return [num_positions[target-nums[i]][0], i]
            if nums[i] not in num_positions.keys():
                num_positions[nums[i]] = []
            num_positions[nums[i]].append(i)
        return []