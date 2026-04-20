class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = 10001
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = left + math.floor((right-left)/2)
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid+1
        return nums[left]