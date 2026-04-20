class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_occ = {}


        for each in strs:
            sorted_each = ''.join(sorted(each))
            # print(sorted_each)
            str_occ[sorted_each] = str_occ.get(sorted_each, []) + [each]

        return list(str_occ.values())