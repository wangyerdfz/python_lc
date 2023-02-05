#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ## lets just assume num of days > 1
        n = len(prices)
        value_mat = -1000 * np.ones((n, k + 1, 2), dtype = int)
        for i in range(k + 1):
            value_mat[n - 1, i, 1] = prices[n - 1]
            value_mat[n - 1, i, 0] = 0
        for d in range( n - 2, -1, -1):
            value_mat[d, 0, 0] = 0
            value_mat[d, 0, 1] = max(value_mat[d + 1, 0 , 1], value_mat[d, 0, 0] + prices[d])
            for i in range(1, k + 1):
                value_mat[d, i, 0] = max (value_mat[d + 1, i , 0], value_mat[d, i - 1, 1] - prices[d])
                value_mat[d, i, 1] = max(value_mat[d + 1, i , 1], value_mat[d, i, 0] + prices[d])
            
        return value_mat[0, k, 0]

            
# @lc code=end

