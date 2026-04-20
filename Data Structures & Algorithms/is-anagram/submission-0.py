class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        for each in s:
            char_dict[each] = char_dict.get(each, 0) + 1
        
        for each in t:
            char_dict[each] = char_dict.get(each, 0) - 1


        for (key, value) in char_dict.items():
            if value is not 0:
                return False
        return True
        