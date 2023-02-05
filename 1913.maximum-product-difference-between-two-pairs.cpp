/*
 * @lc app=leetcode id=1913 lang=cpp
 *
 * [1913] Maximum Product Difference Between Two Pairs
 */

// @lc code=start
class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int min_ = INT_MAX;
        int second_min_ = INT_MAX;
        int max_ = INT_MIN;
        int second_max_ = INT_MIN;
        for(int i : nums){
            if (i < second_min_ && i >= min_){
                second_min_ = i;
            }
            else if (i < second_min_ && i < min_){
                second_min_ = min_;
                min_ = i;
            }
            if ( i > second_max_ && i <= max_){
                second_max_ = i;
            }
            else if(i > second_max_ && i > max_){
                second_max_ = max_;
                max_ = i;
            }
        }
        return second_max_ * max_ - second_min_ * min_;
    }
};
// @lc code=end

