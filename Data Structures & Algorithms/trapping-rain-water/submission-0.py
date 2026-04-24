class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        max_so_far = 0

        for i in range(len(height)):
            max_so_far = max(max_so_far, height[i])
            left_max.append(max_so_far - height[i])

        max_so_far = 0
        right_max = []
        for i in range(len(height)-1, -1, -1):
            max_so_far = max(max_so_far, height[i])
            right_max.insert(0, max_so_far - height[i])


        total_water = 0
        for i in range(len(height)):
            total_water += min(left_max[i], right_max[i])

        return total_water