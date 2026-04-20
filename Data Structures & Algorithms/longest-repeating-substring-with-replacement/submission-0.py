class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        max_len = 0
        curr_len = 0
        left = 0
        for right in range(len(s)):
            char_freq[s[right]] = 1 + char_freq.get(s[right], 0)
            curr_len = max(curr_len, char_freq[s[right]])
            while right - left + 1 - curr_len > k:
                char_freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
