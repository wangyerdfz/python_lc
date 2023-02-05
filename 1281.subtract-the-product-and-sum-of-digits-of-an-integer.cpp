/*
 * @lc app=leetcode id=1281 lang=cpp
 *
 * [1281] Subtract the Product and Sum of Digits of an Integer
 */

// @lc code=start
class Solution {
public:
    int subtractProductAndSum(int n) {
        if( n == 0){
            return 0;
        }
        if ( n == 1){
            return 0;
        }
        int sum_ = 0;
        int prod_ = 1;
        while( n > 0){
            int last_dig = n % 10;
            sum_ += last_dig;
            prod_ *= last_dig;
            n = n / 10;
        }
        return prod_ - sum_;
    }
};
// @lc code=end

