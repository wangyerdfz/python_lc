#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            choose = n -1 
        else:
            choose = m-1
        # calculate m - 1 choose choose 
        res = 1
        for i in range(choose):
            res *= n + m  - 2 - i
        for i in range(1, choose + 1):
            res /= i
        return int(res)
        
# @lc code=end

