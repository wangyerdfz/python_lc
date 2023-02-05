/*
 * @lc app=leetcode id=322 lang=cpp
 *
 * [322] Coin Change
 */

// @lc code=start
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0){
            return 0;
        }
        int n = coins.size();
        if (n <= 0){
            return -1;
        }
        int res[amount + 1];
        for(int i = 0; i <= amount; ++i){
            res[i] = -1;
        }
        res[0] = 0;
        for(int i = 0; i <= amount; ++i){
            for (int j = 0; j < n; ++j){
                if(i - coins[j] >= 0){
                    if (res[i] == -1){
                        if (res[i - coins[j]] > -1){
                            res[i] = res[i - coins[j]] + 1;
                        }
                    }
                    else{
                        if(res[i - coins[j]] > - 1){
                            res[i] = min(res[i - coins[j]] + 1, res[i]);
                        }
                    }
                }
            }
        }
        return res[amount];

    }
};
// @lc code=end

