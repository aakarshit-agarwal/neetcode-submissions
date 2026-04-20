class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        min_left = 0
        min_right = 2 * len(s)
        left = 0
        char_req = {}
        to_match_count = 0
        for each_char in t:
            if each_char not in char_req.keys():
                to_match_count += 1
            char_req[each_char] = 1 + char_req.get(each_char, 0)
        for right in range(len(s)):
            if s[right] in char_req.keys():
                char_req[s[right]] = char_req.get(s[right], 0) - 1
                if char_req[s[right]] == 0:
                    to_match_count -= 1
            while left < len(s) and (s[left] not in char_req.keys() or char_req[s[left]] < 0):
                if s[left] in char_req.keys():
                    char_req[s[left]] = char_req[s[left]] + 1
                left += 1
            if to_match_count == 0 and right - left < min_right - min_left:
                min_left = left
                min_right = right

        if min_right > len(s):
            return ""
        return s[min_left: min_right+1]
