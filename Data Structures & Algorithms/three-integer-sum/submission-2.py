class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            comb = self.twoSum(nums[i+1:], -1 * nums[i])
            for (left, right) in comb:
                if left >= 0 and right >= 0:
                    result.add((nums[i], nums[i +1+ left], nums[i+1 + right]))
        return list(result)

    def twoSum(self, nums, target):
        print(nums, target)
        left = 0
        right = len(nums)-1

        result = []
        while left < right:
            if nums[left] + nums[right] == target:
                result.append((left, right))
                left += 1

            if abs(nums[left] + nums[right]) < abs(target):
                left += 1
            else:
                right -= 1

        return result
        
