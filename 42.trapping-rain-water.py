#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        max_list_left = [0] * n
        max_list_left[0] = height[0]
        max_list_right = [0] * n
        max_list_right[n - 1] = height[n - 1]
        i = 0
        while i + 1 < n:
            max_list_left[i + 1] = max(max_list_left[i], height[i + 1])
            i += 1
        i = n - 1
        while i >= 1:
            max_list_right[i - 1] = max(max_list_right[i], height[i - 1])
            i -= 1
        sum_ = 0
        for i in range(n):
            sum_ += min(max_list_left[i], max_list_right[i]) - height[i]
        
        return sum_

        
# @lc code=end

