class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)) + '#' + string)
        return ''.join(encoded_string)

    def decode(self, s: str) -> List[str]:
        print(s)
        index = 0
        got_hash = False
        length = 0
        result = []
        while index < len(s):
            if s[index] != '#' and got_hash == False:
                length = length * 10 + int(s[index])
                index += 1
            elif s[index] == '#':
                got_hash = True
                index += 1
            if got_hash:
                word = []
                for i in range(length):
                    word.append(s[index+i])
                index += length
                result.append(''.join(word))
                got_hash = False
                length = 0

        return result        
