/*
 * @lc app=leetcode id=326 lang=cpp
 *
 * [326] Power of Three
 */

// @lc code=start
class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n == 1){
            return true;
        }
        if (n <= 0){
            return false;
        }
        while(n > 1){
            if ( n % 3 == 0){
                n = n / 3;
            }
            else{
                return false;
            }
        }
        return true;
    }
};
// @lc code=end

