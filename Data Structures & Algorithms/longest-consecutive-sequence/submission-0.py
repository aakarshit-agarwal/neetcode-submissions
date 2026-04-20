class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set()
        curr_len = 0
        start = 0
        end = 0

        for i in nums:
            num_set.add(i)

        while len(num_set) > 0:
            start = next(iter(num_set))
            end = start
            curr_len = 1
            num_set.remove(start)

            while start-1 in num_set:
                curr_len += 1
                num_set.remove(start-1)
                start = start-1
            
            while end+1 in num_set:
                curr_len += 1
                num_set.remove(end+1)
                end = end+1

            max_len = max(max_len, curr_len)

        return max_len


