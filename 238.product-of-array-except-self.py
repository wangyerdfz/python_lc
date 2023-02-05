#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [1]
        pre = [0]*n
        pos = [0]*n
        res = [1]*n
        pre[0] = nums[0]
        pos[-1] = nums[-1]
        for i in range(1, n):
            pre[i] = pre[i-1]*nums[i]
            pos[n-i-1] = pos[n-i]*nums[n-i-1]

        for i in range(n):
            if i > 0:
                res[i]*=pre[i-1]
            if i < n-1:
                res[i]*=pos[i+1]
        return res
        
# @lc code=end

