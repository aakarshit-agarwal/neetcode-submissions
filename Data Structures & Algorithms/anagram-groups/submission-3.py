class Solution:

    def dict_to_key(self, freq_map):
        char_seq = "abcdefghijklmnopqrstuvwxyz"
        hash_key = ""
        for char in char_seq:
            if char in freq_map:
                hash_key += char+str(freq_map[char])
        return hash_key
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for each in strs:
            freq_hash = {}
            for char in each:
                if char not in freq_hash.keys():
                    freq_hash[char] = 0
                freq_hash[char] += 1
            freq_hash_key = self.dict_to_key(freq_hash)
            if freq_hash_key not in anagram_groups.keys():
                anagram_groups[freq_hash_key] = []
            anagram_groups[freq_hash_key].append(each)
        return list(anagram_groups.values())
