class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_pro = 1
        left_right_pro = []
        for i in range(len(nums)):
            left_right_pro.append(curr_pro)
            curr_pro = curr_pro * nums[i]

        curr_pro = 1
        right_left_pro = []
        for i in range(len(nums)-1, -1, -1):
            right_left_pro.insert(0, curr_pro)
            curr_pro = curr_pro * nums[i]
        
        for i in range(len(nums)):
            left_right_pro[i] = left_right_pro[i] * right_left_pro[i]
        
        return left_right_pro