#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        value_res = -1 * np.zeros((n, 2), dtype = int)
        value_res[n -1 , 1] = prices[n - 1]
        for d in range(n - 2, -1, -1):
            value_res[d, 1] = max(value_res[d + 1, 1], prices[d])
        value_res[n- 1, 0] = 0
        for d in range(n - 2, -1  , -1):
            value_res[d, 0] = max(value_res[d + 1, 0], value_res[d + 1, 1] - prices[d])

        return value_res[0, 0]
        # n = len(prices)
        # if n <= 1:
        #     return 0
        # max_ = -100000
        # for i in range(n):
        #     if prices[i] > max_:
        #         max_ = prices[i]

        # prev_min = max_ + 1000
        # max_profit = 0
        # for i in range(n):
        #     if prices[i] < prev_min:
        #         prev_min = prices[i]
        #     if prices[i] - prev_min > max_profit:
        #         max_profit = prices[i] - prev_min
        
        # return max_profit
        
        # n = len(prices)
        # if n <= 1:
        #     return 0
        # max_profit = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]

        # return max_profit
# @lc code=end

