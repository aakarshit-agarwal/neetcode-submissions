class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for word in strs:
            freq_arr_tuple = tuple(self.get_freq_arr(word))
            if freq_arr_tuple not in anagram_groups:
                anagram_groups[freq_arr_tuple] = []
            anagram_groups[freq_arr_tuple].append(word)
        
        result = []
        for group in anagram_groups.keys():
            result.append(anagram_groups[group])
        return result

    def get_freq_arr(self, string):
        freq_arr = [0] * 26
        for char in string:
            freq_arr[ord(char) - ord('a')] += 1
        return freq_arr