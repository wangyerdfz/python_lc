/*
 * @lc app=leetcode id=7 lang=cpp
 *
 * [7] Reverse Integer
 */

// @lc code=start
class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while(x != 0){
            int last_dig = x%10;
            x = x/ 10;
            if (ans > INT_MAX/10 || (ans == INT_MAX/10 && last_dig > 7)){
                return 0;
            }
            if (ans < INT_MIN/10 || (ans == INT_MIN/10 && last_dig < -8)){
                return 0;
            }
            ans = ans * 10 + last_dig;
        }
        return ans;
    }
};
// @lc code=end

