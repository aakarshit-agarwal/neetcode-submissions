class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.find_longest_common_subsequence(text1, text2, 0, 0, {})

    def find_longest_common_subsequence(self, text1, text2, index1, index2, memorization):
        if index1 == len(text1) or index2 == len(text2):
            return 0
        
        if (index1, index2) in memorization.keys():
            return memorization[(index1, index2)]

        sub_seq = 0
        if text1[index1] == text2[index2]:
            sub_seq = 1 + self.find_longest_common_subsequence(text1, text2, index1+1, index2+1, memorization)
        else:
            sub_seq = max(self.find_longest_common_subsequence(text1, text2, index1, index2+1, memorization), self.find_longest_common_subsequence(text1, text2, index1+1, index2, memorization))
        memorization[(index1, index2)] = sub_seq
        return sub_seq
        