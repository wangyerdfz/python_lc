#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # assuming the num of days is more than 2
        n = len(prices)
        value_mat = -1000 * np.ones((n, 2), dtype = int)
        value_mat[n - 1, 1] = prices[n - 1]
        value_mat[n - 1, 0] = 0
        value_mat[n - 2, 1] = max(value_mat[n - 1, 1], prices[n - 2])
        value_mat[n - 2, 0] = max(value_mat[n - 1, 0], value_mat[n - 1, 1] - prices[n - 2])
        for d in range(n - 3, -1 , -1):
            value_mat[d, 1] = max(value_mat[d + 2, 0]+ prices[d], value_mat[d + 1, 1])
            value_mat[d, 0] = max(value_mat[d + 1, 0], value_mat[d + 1, 1] - prices[d])

        return value_mat[0, 0]
            


        
# @lc code=end

