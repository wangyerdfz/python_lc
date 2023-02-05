#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        import numpy as np
        test_net = np.zeros((n,n))
        for item in trust:
            test_net[item[0]-1, item[1]-1] = 1
        for i in range(n):
            if (test_net[i, :].sum() == 0) and (test_net[:, i].sum() == n-1):
                return i + 1
        return -1
        
# @lc code=end

