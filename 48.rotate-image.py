#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return 
        if n % 2 == 0:
            for i in range( (n ) // 2):
                for j in range( (n  ) // 2):
                    # the 4 pixels with i, j are n - 1 - j, i... n - 1 - i, n - 1 - j...j, n - 1 - i
                    tmp = matrix[i][j]
                    matrix[i][j] =  matrix[n-1-j][i]
                    matrix[n-1-j][i] = matrix[n-1-i][n-1-j] 
                    matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                    matrix[j][n-1-i] = tmp


            return
        else:
            for i in range( (n - 1) // 2):
                for j in range( (n - 1 ) // 2):
                    # the 4 pixels with i, j are j, n-1-i... n-1-i, n-1-j...n-1-j, i
                    tmp = matrix[i][j]
                    matrix[i][j] =  matrix[n-1-j][i]
                    matrix[n-1-j][i] = matrix[n-1-i][n-1-j] 
                    matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                    matrix[j][n-1-i] = tmp

            i = (n -1) //2
            for j in range((n - 1)//2):
                tmp = matrix[i][j]
                matrix[i][j] =  matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j] 
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp


            return



        
# @lc code=end

