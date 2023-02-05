#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], nums[1], nums[2])

        with_last = [0] * n
        without_last = [0] * n
        with_last[-1] = nums[-1]
        with_last[-2] = max(nums[-1], nums[-2])
        for i in range(n-3, -1, -1):
            with_last[i] = max(nums[i] + with_last[i+2], with_last[i+1])
        without_last[-2] = nums[-2]
        without_last[-3] = max(nums[-3], nums[-2])
        for i in range(n-4, -1, -1):
            without_last[i] = max(nums[i] + without_last[i+2], without_last[i+1])


        return max(nums[0] + without_last[2], with_last[1])
        # def rob_helper(nums):
        #     n = len(nums)
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return nums[0]
        #     res = []
        #     return max(nums[0] + rob_helper(nums[2:]), rob_helper(nums[1:]))

        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]
        # return max(nums[0] + rob_helper(nums[2:-1]), rob_helper(nums[1:]))

        
# @lc code=end

