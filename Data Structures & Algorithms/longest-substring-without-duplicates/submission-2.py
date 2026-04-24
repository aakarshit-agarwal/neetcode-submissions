class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        right = 0
        max_len = 0

        length = 0
        while right < len(s):
            if s[right] not in visited:
                length += 1
                visited.add(s[right])
                max_len = max(max_len, length)
                right += 1
            else:
                length -= 1
                visited.remove(s[left])
                left += 1

        return max_len