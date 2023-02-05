/*
 * @lc app=leetcode id=476 lang=cpp
 *
 * [476] Number Complement
 */

// @lc code=start
class Solution {
public:
    int findComplement(int num) {
        if (num == 0){
            return 1;
        }
        if (num == 1){
            return 0;
        }
        unsigned long base = 1;
        unsigned long sum_ = 0;
        while(num > 0){
            sum_ +=  (1 - (num & 1)) * base;
            base = base * 2;
            num = num / 2;
        }
        return (int)sum_;
    }
};
// @lc code=end

