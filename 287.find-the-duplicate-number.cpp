/*
 * @lc app=leetcode id=287 lang=cpp
 *
 * [287] Find the Duplicate Number
 */

// @lc code=start
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1){
            return 1;
        }
        int sum_ = 0;
        for( int i = 0; i < n; ++i){
            sum_ += nums[i];
        }
        return sum_ - (n - 1) * n / 2;
    }
};
// @lc code=end

