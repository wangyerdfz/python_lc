/*
 * @lc app=leetcode id=303 lang=cpp
 *
 * [303] Range Sum Query - Immutable
 */

// @lc code=start
class NumArray {
    int* data;
    int* cum_sum;
public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        data = new int[n];
        cum_sum = new int[n];
        data[0] = nums[0];
        cum_sum[0] = nums[0];
        for(int i = 1; i < n; ++i){
            data[i] = nums[i];
            cum_sum[i] = cum_sum[i - 1] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        return cum_sum[right] - cum_sum[left] + data[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
// @lc code=end

