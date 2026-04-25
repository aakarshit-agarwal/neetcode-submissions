class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        max_len = 0
        curr_len = 0

        freq_map = {}
        while right < len(s):
            freq_map[s[right]] = 1 + freq_map.get(s[right], 0)
            curr_len = max(curr_len, freq_map[s[right]])
            while right - left + 1 - curr_len > k:
                freq_map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len