class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for each in strs:
            result += str(len(each)) + "+" + each
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0:
            leng, rem_s = self.getLen(s)
            result.append(rem_s[:leng])
            s = rem_s[leng:]
        return result


    def getLen(self, s):
        plus_reached = False
        number = 0
        for i in range(len(s)):
            if s[i] == '+':
                return number, s[i+1:]
            number = number*10 + int(s[i])
        return number, s