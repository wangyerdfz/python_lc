#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] = nums[i] + nums[i - 1]
        max_ = nums[0]
        for i in range(n):
            if nums[i] > max_:
                max_ = nums[i]

        return max_
# @lc code=end

