#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        import numpy as np
        m = len(grid)
        n = len(grid[0])
        score_grid = 1000000 * np.ones((m, n), dtype=int)
        # score_grid[0, 0] = grid[0, 0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                   score_grid[i, j] = grid[i][j] 
                   continue
                if i > 0:
                    left = score_grid[i-1, j]
                else:
                    left = 10000000
                if j > 0:
                    top = score_grid[i, j-1]
                else:
                    top = 10000000
                score_grid[i, j] = min(left, top) + grid[i][j]

        return score_grid[m-1, n-1]
# @lc code=end

