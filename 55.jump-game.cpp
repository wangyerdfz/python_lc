/*
 * @lc app=leetcode id=55 lang=cpp
 *
 * [55] Jump Game
 */

// @lc code=start
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n == 0){
            return false;
        }
        if (n == 1){
            return true;
        }
        vector<int> v(n, 0);
        v[0] = 1;
        int further = 0;
        for(int i = 0; i < n; ++i){
            if (v[i] == 0){
                continue;
            }
            for( int j = further + 1; j <= min(n - 1, i + nums[i]); ++j){
                v[j] = 1;
            }
            further = max(further, i + nums[i]);
            if (v[n - 1] == 1){
                return true;
            }
        }
        return v[n - 1] == 1;
    }
};
// @lc code=end

