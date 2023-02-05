/*
 * @lc app=leetcode id=263 lang=cpp
 *
 * [263] Ugly Number
 */

// @lc code=start
class Solution {
public:
    bool isUgly(int n) {
        if (n <= 0){
            return false;
        }
        if (n <= 5){
            return true;
        }
        
        while(true){
            if (n == 1){
                return true;
            }
            if (n%2 == 0){
                n = n/2;
            }
            else if(n%3 == 0){
                n = n/3;
            }
            else if (n % 5 == 0){
                n = n / 5;
            }
            else{
                return false;
            }
        }
    }
};
// @lc code=end

