/*
 * @lc app=leetcode id=258 lang=cpp
 *
 * [258] Add Digits
 */

// @lc code=start
class Solution {
public:
    int trans(int num){
        int sum_ = 0;
        while(num > 0){
            sum_ += num%10;
            num = num / 10;
        }
        return sum_;
    }
    int addDigits(int num) {
        while(num >= 10){
            num = trans(num);
        }
        return num;
    }
};
// @lc code=end

