class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        len_max = 0

        freq_map = {}
        for i in range(len(s)):
            if s[i] in freq_map.keys():
                while s[left] != s[i]:
                    del freq_map[s[left]]
                    left += 1
                left += 1
            else:
                freq_map[s[i]] = True
            right = i
            len_max = max(len_max, right-left+1)
        
        return len_max