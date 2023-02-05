#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        import numpy as np
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = np.zeros((m, n), dtype=int)
        grid[0,0] = 1 - obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                    continue
                
                if i > 0:
                    grid[i, j] += grid[i - 1, j]
                if j > 0:
                    grid[i, j] += grid[i, j - 1]


        return grid[m-1, n-1]
        # import numpy as np
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # grid = np.zeros((m, n), dtype=int)
        
        # grid[0,0] = 1- obstacleGrid[0][0]
        # for j in range(n):
        #     for i in range(m):
        #         if i > 0 and obstacleGrid[i][j] == 0:
        #             grid[i, j] += grid[i-1, j]
        #         if j > 0 and obstacleGrid[i][j] == 0:
        #             grid[i, j] += grid[i, j-1]


        # return grid[m-1, n-1]



        
# @lc code=end

