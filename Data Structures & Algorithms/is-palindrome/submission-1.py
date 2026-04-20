class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_char = 'abcdefghijklmnopqrstuvwxyz0987654321'
        left = 0
        right = len(s)-1

        while left < right:
            left_c = s[left].lower()
            right_c = s[right].lower()
            while left_c not in allowed_char and left < right:
                left += 1
                left_c = s[left].lower()
            while right_c not in allowed_char and left < right:
                right -= 1
                right_c = s[right].lower()
            # print(left_c, right_c)

            if left_c != right_c:
                return False
            left += 1
            right -= 1
        return True