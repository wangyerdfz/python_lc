/*
 * @lc app=leetcode id=338 lang=cpp
 *
 * [338] Counting Bits
 */

// @lc code=start
class Solution {
public:
    int count_bits(int n){
        int sum_ = 0;
        while(n > 0){
            sum_ += n%2;
            n = n >> 1;
        }
        return sum_;
    }
    vector<int> countBits(int n) {
        if (n == 0){
            return {0};
        }
        vector<int> res;
        for(int i = 0; i <= n; ++i){
            res.push_back(count_bits(i));
        }
        return res;

    }
};
// @lc code=end

