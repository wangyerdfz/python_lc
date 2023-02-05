#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        value_mat = -1000 * np.zeros((n, 3, 2), dtype = int) # num of days, num of buy and sell left and num of shares holding
        for i in range(3):
            value_mat[n - 1, i , 1] = prices[n - 1]
            value_mat[n - 1, i , 0] = 0
        for i in range(n):
            value_mat[i, 0, 0] = 0
        for i in range(n - 2, - 1, -1):
            value_mat[i, 0, 1] = max(value_mat[i + 1, 0, 0] + prices[i], value_mat[i + 1, 0, 1])
            value_mat[i, 1, 0] = max(value_mat[i + 1, 0, 1] - prices[i], value_mat[i + 1, 1, 0])
            value_mat[i, 1, 1] = max(value_mat[i + 1, 1, 0] + prices[i], value_mat[i + 1, 1, 1])
            value_mat[i, 2, 0] = max(value_mat[i + 1, 1, 1] - prices[i], value_mat[i + 1, 2, 0])
            value_mat[i, 2, 1] = max(value_mat[i + 1, 1, 0] + prices[i], value_mat[i + 1, 1, 1])
        return value_mat[0, 2, 0]






        # import numpy as np
        # n = len(prices)
        # big_matrix = -1 * np.zeros((n, 3, 2))
        # # last day:
        # for i in range(3):
        #     big_matrix[n - 1, i, 0] = 0
        # for i in range(3):
        #     big_matrix[n - 1, i, 1] = prices[n - 1]
        # for i in range(n):
        #     big_matrix[i, 0, 0] = 0
        # biggest = -1000000
        # for i in reversed(range(n)):
        #     if biggest < prices[i]:
        #         biggest = prices[i]
        #     big_matrix[i, 0, 1] = biggest
        # for i in reversed(range(n - 1)):
        #     big_matrix[i, 1, 0] = max( big_matrix[i + 1, 1, 0], big_matrix[i + 1, 0, 1] - prices[i])
        # for i in reversed(range(n - 1)):
        #     big_matrix[i ,1, 1] = max(big_matrix[i + 1, 1, 1], big_matrix[i + 1, 1, 0] + prices[i] )
        # for i in reversed(range(n - 1)):
        #     big_matrix[i, 2, 0] = max(big_matrix[i + 1, 2, 0], big_matrix[i + 1, 1, 1] - prices[i])
        # return int(big_matrix[0, 2, 0])

# @lc code=end

