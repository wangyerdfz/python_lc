/*
 * @lc app=leetcode id=204 lang=cpp
 *
 * [204] Count Primes
 */

// @lc code=start
class Solution {
public:
    int countPrimes(int n) {
        if ( n <= 1){
            return 0;
        }
        if( n == 2){
            return 0;
        }
        if (n == 3){
            return 1;
        }
        int res[n ];
        for(int i = 0; i < n; ++i){
            res[i] = 1;
        }
        res[0] = 0;
        res[1] = 0;

        for( int i = 0; i*i <= n + 1; ++i){
            if (res[i] == 0){
                continue;
            }
            for(int j = 2; j * i < n; ++j){
                res[i * j] = 0;
            }
        }
        int sum_ = 0;
        for(int i = 0; i < n; ++i){
            sum_ += res[i];
        }
        return sum_;

    }
};
// @lc code=end

