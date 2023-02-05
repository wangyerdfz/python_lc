#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m <=0 or n <= 0:
            return False
        def access_val(idx):
            f_idx = idx//n
            s_idx = idx%n
            return matrix[f_idx][s_idx]

        low = 0
        high = m*n-1
        while(low < high):
            mid = low + (high - low)//2
            if access_val(mid) < target:
                low = mid + 1
            else:
                high = mid
        return (high == low) and (access_val(low) == target)
            
# @lc code=end

