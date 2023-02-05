#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        import numpy as np
        n = len(dungeon)
        m = len(dungeon[0])
        path_min = np.zeros((n, m), dtype=int)
        cur = np.zeros((n, m), dtype=int)
        path_min[0, 0] = dungeon[0][0]
        cur[0, 0] = dungeon[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    cur[i, j] = cur[i, j-1] + dungeon[i][j]
                    path_min[i, j] = min(path_min[i, j-1], cur[i, j])
                elif j == 0:
                    cur[i, j] = cur[i-1, j] + dungeon[i][j]
                    path_min[i, j] = min(path_min[i-1, j], cur[i, j])
                else: # can either go from top or left
                    cur_left = cur[i, j-1] + dungeon[i][j]
                    min_left = min(path_min[i, j-1], cur_left)
                    cur_top = cur[i-1, j] + dungeon[i][j]
                    min_top = min(path_min[i-1, j], cur_top)
                    if min_top > min_left: # choose top
                        cur[i, j] = cur_top
                        path_min[i, j] = min_top
                    elif min_top ==  min_left: # if the same, check cur
                        if cur_top > cur_left: # choose top
                            cur[i, j] = cur_top
                            path_min[i, j] = min_top
                        else: # choose left
                            cur[i, j] = cur_left
                            path_min[i, j] = min_left
                    else:
                        cur[i, j] = cur_left
                        path_min[i, j] = min_left

        
        return max(-path_min[n-1,m-1], 0) + 1


                        


        
# @lc code=end

