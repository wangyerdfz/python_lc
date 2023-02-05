/*
 * @lc app=leetcode id=495 lang=cpp
 *
 * [495] Teemo Attacking
 */

// @lc code=start
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int n = timeSeries.size();
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return duration;
        }
        int sum_ = 0;
        for(int i = 0; i < n - 1; ++i){
            sum_ += min( timeSeries[i + 1] - timeSeries[i], duration);
        }
        sum_ += duration;
        return sum_;
    }
};
// @lc code=end

