class Solution:
    def numDecodings(self, s: str) -> int:
        one_digit = "123456789"
        double_digit = "12"
        ways = [0] * (len(s)+2)
        ways[-1] = 0
        ways[-2] = 1 if s[-1] is "0" else 1
        s = s + "+-"
        for i in range(len(s)-3, -1, -1):
            ways_sum = 0
            if s[i] is not "0":
                ways_sum = ways_sum + ways[i+1]
                if (s[i] is "1" and s[i+1] in "0123456789") or (s[i] is "2" and s[i+1] in "0123456"):
                    ways_sum = ways_sum + ways[i+2]
            ways[i] = ways_sum

        return ways[0]