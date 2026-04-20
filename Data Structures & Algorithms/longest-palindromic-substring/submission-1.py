class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_left = -1
        max_right = -1
        max_len = 0
        for i in range(0, len(s)-1):
            if s[i] is s[i+1]:
                left, right = self.find_pal_subs(s, i, i+1)
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    max_left = left
                    max_right = right
        for i in range(0, len(s)):
            left, right = self.find_pal_subs(s, i, i)
            if right - left + 1 > max_len:
                max_len = right - left + 1
                max_left = left
                max_right = right

        return s[max_left:max_right+1]

    def find_pal_subs(self, s, left, right):
        while left-1 >= 0 and right+1 < len(s) and s[left-1] is s[right+1]:
            left -= 1
            right += 1
        return left, right