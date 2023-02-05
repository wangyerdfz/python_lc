/*
 * @lc app=leetcode id=50 lang=cpp
 *
 * [50] Pow(x, n)
 */

// @lc code=start
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0){
            return 1;
        }
        long double prod = 1.0;
        long new_n = long(n);
        bool if_neg = n < 0;
        double base = x;
        if (if_neg){
            new_n = -1 * new_n;
        }
        while(new_n > 0){
            if (new_n & 1){
                prod *= base;
            }
            base = base * base;
            new_n = new_n / 2;
        }
        if (if_neg){
            prod = 1 /  prod;
        }
        return prod;
    }
};
// @lc code=end

