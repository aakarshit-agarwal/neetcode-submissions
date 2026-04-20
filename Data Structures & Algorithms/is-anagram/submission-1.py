class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq_first = {}
        for each in s:
            if each not in char_freq_first.keys():
                char_freq_first[each] = 0
            char_freq_first[each] += 1

        for each in t:
            if each not in char_freq_first.keys():
                return False
            char_freq_first[each] -= 1
            if char_freq_first[each] == 0:
                del char_freq_first[each]
        
        if len(char_freq_first.keys()) > 0:
            return False

        return True