class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for each in nums:
            if each in num_set:
                return True
            num_set.add(each)
        return False