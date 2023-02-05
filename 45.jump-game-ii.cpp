/*
 * @lc app=leetcode id=45 lang=cpp
 *
 * [45] Jump Game II
 */

// @lc code=start
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n == 0){
            return 0;
        }
        if(n == 1){
            return 0;
        }
        vector<int> res(n, -1);
        res[n - 1] = 0;
        for(int i = n - 2; i >= 0; --i){
            int min_ = n + 1;
            for(int j = 1; j <= min(nums[i], n - i - 1); ++j){
                if (res[i + j]  + 1 < min_){
                    min_ = res[i + j] + 1;
                }
            }
            res[i] = min_;
        }
        return res[0];
    }
};
// @lc code=end

