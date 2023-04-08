#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        # complexity o (m + n)
        m = len(matrix)
        n = len(matrix[0])
        m_mark = [-1] * m
        n_mark = [-1] * n
        
        for i in range(m):
            res_ = 1
            for j in range(n):
                res_ *= matrix[i][j]
            m_mark[i] = 0 if res_ == 0 else 1

        for j in range(n):
            res_ = 1
            for i in range(m):
                res_ *= matrix[i][j]
            n_mark[j] = 0 if res_ == 0 else 1

        for i in range(m):
            if m_mark[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if n_mark[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        
            

        



        
# @lc code=end

