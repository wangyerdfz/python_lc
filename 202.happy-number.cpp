/*
 * @lc app=leetcode id=202 lang=cpp
 *
 * [202] Happy Number
 */

// @lc code=start
const int MAX_NUM = 1000;
class Solution {
public:
    int trans(int n){
        int res = 0;
        while(n > 0){
            res +=  (n % 10) * (n % 10);
            n = n / 10;
        }
        return res;
    }
    bool isHappy(int n) {
        if (n <= 0){
            return false;
        }
        if (n == 1){
            return true;
        }
        int tmp = trans(n);
        int count = 0;
        while(count < MAX_NUM){
            tmp = trans(tmp);
            if (tmp == 1){
                return true;
            }
            count++;
        }
        return false;
    }
};
// @lc code=end

