class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for each in nums:
            if each not in counter.keys():
                counter[each] = 0
            counter[each] += 1

        freq_counter = {}
        for key, value in counter.items():
            if value not in freq_counter.keys():
                freq_counter[value] = []
            freq_counter[value].append(key)
        
        result = []
        for i in range(len(nums), 0, -1):
            if i in freq_counter.keys():
                result += freq_counter[i]
                if len(result) >= k:
                    break
        return result[:k]
            