class Solution:
    def isPalindrome(self, s: str) -> bool:
        numbers = "0123456789"
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        left = 0
        right = len(s) -1

        while left < right:
            if s[left] not in numbers and s[left] not in chars:
                left += 1
            elif s[right] not in numbers and s[right] not in chars:
                right -= 1 
            elif s[left] == s[right] or (s[left] in chars and s[right] in chars and s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            else:
                return False
        
        return True
