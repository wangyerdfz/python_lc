#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(n+1):
            while(heights[i] < heights[stack[-1]]):
                h = heights[stack.pop()]
                res = max(res, h * (i - stack[-1] - 1))

            stack.append(i)

        return res


        # n = len(heights)
        # if n <= 0:
        #     return 0
        # if n <= 1:
        #     return heights[0]
        # heights.append(0)
        # stack = [-1]
        # res = 0
        # for i in range(len(heights)):
        #     while heights[i] < heights[stack[-1]]:
        #         h = heights[stack.pop()]
        #         w = i - stack[-1] - 1
        #         res = max(res, h*w)

        #     stack.append(i)

        # return res
    

        # import numpy as np
        # # worse case scenario: use o n^2 to get the lowest
        # n = len(heights)
        
        # if n <= 0:
        #     return 0
        # if n == 1:
        #     return heights[0]
        # min_num = np.zeros((n, n), dtype=int)
        # for i in range(n):
        #     min_num[i, i] = heights[i]
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if heights[j] < min_num[i, j-1]:
        #             min_num[i, j] = heights[j]
        #         else:
        #             min_num[i, j] = min_num[i, j-1]

        # max_ = -1
        # for i in range(n):
        #     for j in range(i, n):
        #         if min_num[i, j] * (j-i+1) > max_:
        #             max_ = min_num[i, j] * (j-i+1)
        # return max_
        
        
# @lc code=end

