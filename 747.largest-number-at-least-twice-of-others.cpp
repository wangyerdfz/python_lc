/*
 * @lc app=leetcode id=747 lang=cpp
 *
 * [747] Largest Number At Least Twice of Others
 */

// @lc code=start
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int n = nums.size();
        if (n == 0){
            return -1;
        }
        if ( n == 1){
            return nums[0];
        }
        int max_ = nums[0];
        int max_ind = 0;
        bool if_twice = true;
        for(int i = 1; i < n; ++i){
            if(nums[i] >= max_){
                if (nums[i] >= max_ * 2){
                    if_twice = true;
                }
                else{
                    if_twice = false;
                }
                max_ = nums[i];
                max_ind = i;
            }
            else{
                if(max_ < nums[i] * 2){
                    if_twice = false;
                }
            }
        }
        if(!if_twice){
            return -1;
        }
        return max_ind;
    }
};
// @lc code=end

