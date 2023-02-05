/*
 * @lc app=leetcode id=1556 lang=cpp
 *
 * [1556] Thousand Separator
 */

// @lc code=start
class Solution {
public:
    string thousandSeparator(int n) {
        if(n <= 999){
            return to_string(n);
        }
        string res = "";
        int dig = 0;
        while(n > 0){
            int last_dig = n%10;
            res = to_string(last_dig) + res;
            n = n / 10;
            dig++;
            if(dig > 0 && dig%3 ==0 && n > 0){
                res = "." + res;
            }
        }
        return res;
    }
};
// @lc code=end

