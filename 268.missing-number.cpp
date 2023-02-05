/*
 * @lc app=leetcode id=268 lang=cpp
 *
 * [268] Missing Number
 */

// @lc code=start
class Solution {
public:
    int missingNumber(vector<int>& nums) {

        int n = nums.size() + 1;
        if (n == 1){
            return 1;
        }
        int sum_ = 0;
        for (int i = 0; i < n - 1; ++i){
            sum_ += nums[i];
        }
        return n * (n - 1)/2 - sum_;
    }
};
// @lc code=end

