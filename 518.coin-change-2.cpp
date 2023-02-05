/*
 * @lc app=leetcode id=518 lang=cpp
 *
 * [518] Coin Change 2
 */

// @lc code=start
//  performance issues
// class Solution {
//     int change_helper(int amount, vector<int>& coins, int start, int end){
//         if (amount <= 0){
//             return 0;
//         }
//         if ( start > end){
//             return 0;
//         }
//         if (start == end){
//             if (amount % coins[start] == 0){
//                 return 1;
//             }
//             else{
//                 return 0;
//             }
//         }
//         int sum_ = 0;
//         for(int i = start; i <= end; ++i){
//             if (amount == coins[i]){
//                 sum_ += 1;
//             }
//             if (amount > coins[i]){
//                 sum_ += change_helper(amount - coins[i], coins, i, end);
//             }
//         }
//         return sum_;
//     }
// public:
//     int change(int amount, vector<int>& coins) {
//         if (amount == 0){
//             return 1;
//         }
//         int n = coins.size();
//         if(n == 0){
//             return 0;
//         }
//         if(n == 1){
//             if (amount% coins[0] == 0){
//                 return 1;
//             }
//             return 0;
//         }
//         return change_helper(amount, coins, 0, n - 1);
//     }
// };


class Solution {

public:
    int change(int amount, vector<int>& coins) {
        if (amount == 0){
            return 1;
        }
        vector<int> res(amount + 1, 0);
        res[0] = 1;

        for(int j = 0; j < coins.size(); ++j){
            for(int i = 1; i <= amount; ++i){
                if ( i - coins[j] >= 0){
                    res[i] += res[i - coins[j]];
                }
            }
        }
        return res[amount];
    }
};
// @lc code=end

