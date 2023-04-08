#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        res_ = [[-1]*(i + 1) for i in range(n)]
        for j in range(n):
            res_[n-1][j] = triangle[n-1][j]
        for j in range(n-2, -1, -1):
            for i in range(j+1):
                res_[j][i] = min(res_[j+1][i], res_[j+1][i+1]) + triangle[j][i]

        return res_[0][0]

# @lc code=end

