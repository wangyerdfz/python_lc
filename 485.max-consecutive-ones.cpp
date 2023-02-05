/*
 * @lc app=leetcode id=485 lang=cpp
 *
 * [485] Max Consecutive Ones
 */

// @lc code=start
class Solution {
    int find_helper(vector<int>& nums, int l, int r){
        if(l == r){
            return (int) (nums[l] == 1);
        }
        if(l > r){
            return 0;
        }
        int first_one = -1;
        // find first one
        for(int i = l; i <= r; ++i){
            if(nums[i] == 1){
                first_one = i;
                break;
            }
        }
        if(first_one == -1){ // no ones
            return 0;
        }
        int first_zero = -1;
        for(int i = first_one; i <= r; ++i){
            if(nums[i] == 0){
                first_zero = i;
                break;
            }
        }
        if(first_zero == -1) { // no zeros
            return (r - first_one + 1);
        }
        return max(first_zero - first_one, find_helper(nums, first_zero, r));
    }
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        if (n == 0){
            return 0;
        }
        if(n == 1){
            return (int)(nums[0] == 1);
        }
        return find_helper(nums, 0, n - 1);
    }
};
// @lc code=end

