#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        value_mat = np.zeros((n, 2), dtype = int)
        value_mat[n - 1 , 1] = prices[n - 1]
        value_mat[n - 1 , 0 ] = 0
        for i in range(n - 2, -1, -1):
            value_mat[i , 1] = max( value_mat[i + 1, 0] + prices[i], value_mat[i + 1, 1])
            value_mat[i , 0] = max( value_mat[i + 1 , 0], value_mat [i + 1, 1] - prices[i])
        return value_mat[0 , 0]

        # n = len(prices) - 1
        # i = 0
        # buy = 0
        # sell = 0
        # max_profit = 0
        # while(i < n):
        #     while(i < n and prices[i + 1] <= prices[i]):
        #         i += 1
        #     buy = prices[i]
        #     while(i < n and prices[i + 1] > prices[i]):
        #         i += 1
        #     sell = prices[i]
        #     max_profit += sell - buy
        # return max_profit
        # n = len(prices)
        # if n <= 1:
        #     return 0
        # max_profit = 0
        # for i in range(n - 1):
        #     if prices[i + 1] > prices[i]:
        #         max_profit += prices[i + 1] - prices[i]
        # return max_profit
# @lc code=end

