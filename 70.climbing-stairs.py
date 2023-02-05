#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        res = [-1] * (n + 1)
        res[1] = 1
        res[2] = 2
        res[3] = 3
        for i in range(4, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]
        
# @lc code=end

