class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible_jump = [False for each in nums]
        for i in range(len(nums)-1, -1, -1):
            req_len = len(nums) - i - 1
            if nums[i] >= req_len:
                possible_jump[i] = True
            else:
                j = 0
                result = False
                while j <= nums[i] and not result:
                    result = result or possible_jump[i + j]
                    j += 1
                possible_jump[i] = result

        print(possible_jump)
        return possible_jump[0]
    