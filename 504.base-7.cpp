/*
 * @lc app=leetcode id=504 lang=cpp
 *
 * [504] Base 7
 */

// @lc code=start
class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0){
            return "0";
        }
        string s = "";
        bool if_neg = num < 0;
        if (if_neg){
            num = -1 * num;
        }
        while(num > 0){
            s = to_string(num%7) + s;
            num = num/7;
        }
        if (if_neg){
            s = "-" + s;
        }
        return s;
    }
};
// @lc code=end

