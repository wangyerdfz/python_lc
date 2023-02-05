/*
 * @lc app=leetcode id=307 lang=cpp
 *
 * [307] Range Sum Query - Mutable
 */

// @lc code=start
class NumArray {
    int size;
    int* v;
    int* cum_sum;
public:
    NumArray(vector<int>& nums) {
        size = nums.size();
        v = new int[size];
        cum_sum = new int[size];
        if(size > 0){
            int sum_ = 0;
            for (int i = 0; i < size; ++i){
                sum_ += nums[i];
                v[i] = nums[i];
                cum_sum[i] = sum_;
            }
        }
    }
    
    void update(int index, int val) {
        if (index < 0 || index >= size){
            return;
        }
        for(int i = index; i < size; ++i){
            cum_sum[i] = cum_sum[i] + val - v[index];
        }
        v[index] = val;
    }
    
    int sumRange(int left, int right) {
        return cum_sum[right] - cum_sum[left] + v[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
// @lc code=end

