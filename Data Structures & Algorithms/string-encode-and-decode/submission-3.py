class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for each in strs:
            encoded_string += str(len(each)) + "-" + each
        return encoded_string

    def decode(self, s: str) -> List[str]:
        original_strs = []
        while len(s) > 0:
            index = s.find('-')
            if index == -1:
                original_strs.append(s)
                break
            leng = int(s[:index])
            this_str = s[index+1:index+1+leng]
            original_strs.append(this_str)
            s = s[index+1+leng:]
            # print(s)

        return original_strs