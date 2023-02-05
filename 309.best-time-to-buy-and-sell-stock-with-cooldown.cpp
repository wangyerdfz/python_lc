/*
 * @lc app=leetcode id=309 lang=cpp
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1){
            return 0;
        }
        if ( n == 2){
            return max(0, prices[1] - prices[0]);
        }
        int profit[2][n];
        profit[1][n - 1] = prices[n - 1];
        profit[0][n - 1] = 0;
        profit[1][n - 2] = max(prices[n - 2], profit[1][n - 1]);
        profit[0][n - 2] = max(0 , -prices[n - 2] + profit[1][n - 1]);
        for(int i = n - 3; i >=0; --i){
            profit[1][i] = max(prices[i] + profit[0][i + 2], profit[1][i + 1]);
            profit[0][i] = max(- prices[i] + profit[1][i + 1], profit[0][i + 1]);
        }
        return profit[0][0];
    }
};
// @lc code=end

