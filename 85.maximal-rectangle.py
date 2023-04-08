#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        
        left = [[0]*n for _ in range(m)]
        right = [[0]*n for _ in range(m)]
        height = [[0]*n for _ in range(m)]
        for j in range(n): # do height first
            if matrix[0][j] == '1':
                height[0][j] = 1
            else:
                height[0][j] = 0
        cur_left = 0
        for j in range(n): # left
            if matrix[0][j] == '1':
                left[0][j] = cur_left
            else:
                left[0][j] = 0
                cur_left = j+1
        cur_right = n
        for j in range(n-1, -1, -1): # right
            if matrix[0][j] == '1':
                right[0][j] = cur_right
            else:
                right[0][j] = n
                cur_right = j

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[i][j] = height[i-1][j] + 1
                else:
                    height[i][j] = 0
        
        
        for i in range(1, m):
            cur_left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[i][j] = max(cur_left, left[i-1][j])
                else:
                    left[i][j] = 0
                    cur_left = j+1

        
        for i in range(1, m):
            cur_right = n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[i][j] = min(cur_right, right[i-1][j])
                else:
                    right[i][j] = n
                    cur_right = j

        max_A = -1
        for i in range(m):
            for j in range(n):
                max_A = max(max_A, height[i][j]* (right[i][j] - left[i][j]))


        return max_A
        


        





        # m = len(matrix)
        # if m == 0:
        #     return 0
        # n = len(matrix[0])
        # if n == 0:
        #     return 0
        # left = [[-1]*n for _ in range(m)]
        # right = [[-1]*n for _ in range(m)]
        # height = [[-1]*n for _ in range(m)]
        # for j in range(n): # initialize
        #     height[0][j] = 1 if matrix[0][j] == '1' else 0
        # cur_left = 0
        # cur_right = n
        # for j in range(n):
        #     if matrix[0][j] == '1': 
        #         left[0][j] = cur_left
        #     else:
        #         left[0][j] = 0
        #         cur_left = j+1

        # for j in range(n-1, -1, -1):
        #     if matrix[0][j] == '1':
        #         right[0][j] = cur_right
        #     else:
        #         right[0][j] = n
        #         cur_right = j

        # for i in range(1, m):
        #     cur_left = 0
        #     cur_right = n
        #     for j in range(n):
        #         if matrix[i][j] == '1': 
        #             height[i][j] = height[i-1][j] + 1
        #         else:
        #             height[i][j] = 0

        #     for j in range(n):
        #         if matrix[i][j] == '1': 
        #             left[i][j] = max(left[i-1][j], cur_left)
        #         else:
        #             left[i][j] = 0
        #             cur_left = j+1

        #     for j in range(n-1, -1, -1):
        #         if matrix[i][j] == '1':
        #             right[i][j] = min(cur_right, right[i-1][j])
        #         else:
        #             right[i][j] = n
        #             cur_right = j



        # maxA = -1
        # for i in range(m):
        #     for j in range(n):
        #         maxA = max((right[i][j] - left[i][j])*height[i][j], maxA)
        # return maxA


        
# @lc code=end

