class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + math.floor((right-left)/2)
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                return -1
        return -1