/*
 * @lc app=leetcode id=342 lang=cpp
 *
 * [342] Power of Four
 */

// @lc code=start
class Solution {
public:
    bool isPowerOfFour(int n) {

        if(n <= 0){
            return false;
        }
        if (n == 1){
            return true;
        }
        // vector<bool> res(n + 1, false);
        long long cur = 1;
        while(cur <= n){
            if(cur == n){
                return true;
            }
            cur *= 4;
        }
        return false;
    }
};
// @lc code=end

