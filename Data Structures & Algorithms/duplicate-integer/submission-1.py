class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearing_values = set()
        for each in nums:
            if each in appearing_values:
                return True
            appearing_values.add(each)

        return False