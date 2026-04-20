class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrom_count = len(s)

        # Calculating Odd Length Palindrom
        for i in range(len(s)):
            left_index = i-1
            right_index = i+1
            while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
                palindrom_count += 1
                left_index -= 1
                right_index += 1
        
        # Calculating Even Length Palindrom
        for i in range(len(s)):
            left_index = i
            right_index = i+1
            while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
                palindrom_count += 1
                left_index -= 1
                right_index += 1

        return palindrom_count