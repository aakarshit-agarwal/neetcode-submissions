class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for each in nums:
            num_freq[each] = num_freq.get(each, 0) + 1

        freq_count = [[] for _ in range(len(nums)+1)]
        for (num, freq) in num_freq.items():
            freq_count[freq].append(num)

        res = []
        for i in range(len(freq_count)-1, -1, -1):
            for num in freq_count[i]:
                res.append(num)
                if len(res) == k:
                    return res