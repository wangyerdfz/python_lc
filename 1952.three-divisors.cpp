/*
 * @lc app=leetcode id=1952 lang=cpp
 *
 * [1952] Three Divisors
 */

// @lc code=start
class Solution {
public:
    bool isThree(int n) {
        if (n <= 3){
            return false;
        }
        if(n  == 4){
            return true;
        }
        if(n <= 8){
            return false;
        }
        // int count = 0;
        for(int i = 2; i * i <= n; ++i){
            if (n % i == 0){
                if (n / i != i){
                    return false;
                }
                else{
                    return true;
                }
            }
        }
        return false;
    }
};
// @lc code=end

